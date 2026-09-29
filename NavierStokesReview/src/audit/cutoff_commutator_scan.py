"""CUDA-first 3D audit of OpenAI's Cartesian cutoff/curl construction.

The source operation is `SpatialLocalization.spatialCutoff` followed by
`cutVelocity = SpatialCurl.spatialCurl (cutPotential A)`:

    c(x,y,z) = cutoff(16*(x^2+y^2)) * cutoff(4*z)
    A = (S(r,z)/r) e_theta
    curl(c*A) = c*curl(A) + (grad c) cross A.

This instrument evaluates that operation on a genuine 3D Cartesian volume,
not a 1D radial sample.  It uses a nonseparable axisymmetric stream S(r,z),
constructs A_x,A_y,A_z in Cartesian coordinates, computes the analytic curl
and commutator components, independently finite-differences the Cartesian curl,
measures the 3D divergence residual, integrates full x-y slices for radial
moment curves, sweeps resolutions/profile scales/modulations, and emits plots.

CUDA is the primary backend when available. CPU is only a fallback for a
machine without CUDA, not a second result being marketed as evidence.

The stream is still an explicit diagnostic profile rather than the
noncomputable selected Lean `ASum`/`BSum`/`PSum` value.  The output therefore
tests the exact cutoff/curl mechanism and its numerical stability; it does not
silently become a selected-field `Delta m != 0` theorem.
"""

from __future__ import annotations

import argparse
import csv
import gc
import json
from pathlib import Path
from typing import Any

import numpy as np

try:
    import cupy as cp
except ImportError:  # pragma: no cover
    cp = None


DEFAULT_RESOLUTIONS = (129, 193, 257)
DEFAULT_PROFILE_SCALES = (0.5, 1.0, 2.0)
DEFAULT_MODULATIONS = (0.0, 0.25)
RADIAL_DOMAIN = 0.5
AXIAL_DOMAIN = 0.5


def cuda_available() -> bool:
    if cp is None:
        return False
    try:
        return int(cp.cuda.runtime.getDeviceCount()) > 0
    except cp.cuda.runtime.CUDARuntimeError:
        return False


def cuda_device_name() -> str | None:
    if not cuda_available():
        return None
    name = cp.cuda.runtime.getDeviceProperties(0)["name"]
    return name.decode(errors="replace") if isinstance(name, bytes) else str(name)


def module_for(backend: str):
    if backend == "gpu":
        if not cuda_available():
            raise RuntimeError("GPU backend requested but CUDA is unavailable")
        return cp
    if backend == "cpu":
        return np
    raise ValueError(backend)


def host(value: Any) -> Any:
    if cp is not None and isinstance(value, cp.ndarray):
        return value.get()
    return value


def scalar(value: Any) -> float:
    return float(host(value))


def safe_divide(numerator: Any, denominator: Any, xp: Any) -> Any:
    """Backend-neutral masked division; CuPy does not accept NumPy's `where`."""

    safe_denominator = xp.where(denominator != 0.0, denominator, 1.0)
    return xp.where(denominator != 0.0, numerator / safe_denominator, 0.0)


def trapz(values: Any, grid: Any, axis: int, xp: Any) -> Any:
    method = getattr(xp, "trapezoid", None)
    if method is not None:
        return method(values, grid, axis=axis)
    return xp.sum(
        (xp.take(values, range(1, values.shape[axis]), axis=axis) +
         xp.take(values, range(0, values.shape[axis] - 1), axis=axis)) / 2.0
        * xp.diff(grid), axis=axis
    )


def exp_neg_inv_glue(x: Any, xp: Any) -> Any:
    out = xp.zeros_like(x)
    positive = x > 0.0
    out[positive] = xp.exp(-1.0 / x[positive])
    return out


def smooth_transition_with_derivative(x: Any, xp: Any) -> tuple[Any, Any]:
    """Mathlib `Real.smoothTransition` and its derivative on the active band."""

    a = exp_neg_inv_glue(x, xp)
    b = exp_neg_inv_glue(1.0 - x, xp)
    da = xp.zeros_like(x)
    db = xp.zeros_like(x)
    pa = x > 0.0
    pb = (1.0 - x) > 0.0
    da[pa] = a[pa] / x[pa] ** 2
    # d/dx[-1/(1-x)] = -1/(1-x)^2.  The sign matters in the
    # smoothTransition quotient derivative and was the source of the large
    # false product-rule residual in the first run.
    db[pb] = -b[pb] / (1.0 - x[pb]) ** 2
    denominator = a + b
    transition = safe_divide(a, denominator, xp)
    derivative = safe_divide(da * denominator - a * (da + db), denominator ** 2, xp)
    transition = xp.where(x <= 0.0, 0.0, xp.where(x >= 1.0, 1.0, transition))
    derivative = xp.where((x <= 0.0) | (x >= 1.0), 0.0, derivative)
    return transition, derivative


def source_cutoff(r: Any, z: Any, xp: Any) -> tuple[Any, Any, Any]:
    """Exact numerical form of `SpatialLocalization.spatialCutoff`.

    `SmoothCutoffs.cutoffBump` has rIn=1/2 and rOut=1.  On nonnegative radial
    input this is smoothTransition(2-2q), hence the radial argument 16*r^2
    becomes smoothTransition(2-32*r^2).  The axial argument is handled with
    the exact absolute-value symmetry of the Mathlib bump.
    """

    radial_arg = 2.0 - 32.0 * r ** 2
    axial_arg = 2.0 - 8.0 * xp.abs(z)
    radial, d_radial_arg = smooth_transition_with_derivative(radial_arg, xp)
    axial, d_axial_arg = smooth_transition_with_derivative(axial_arg, xp)
    cutoff = radial * axial
    d_cutoff_r = d_radial_arg * (-64.0 * r) * axial
    sign_z = xp.where(z > 0.0, 1.0, xp.where(z < 0.0, -1.0, 0.0))
    d_cutoff_z = radial * d_axial_arg * (-8.0 * sign_z)
    return cutoff, d_cutoff_r, d_cutoff_z


def stream_field(r: Any, z: Any, scale: float, modulation: float, xp: Any):
    """Nonseparable smooth axisymmetric stream and its analytic derivatives."""

    axial_scale = 0.75 * scale
    radial_exp = -(r / scale) ** 2
    axial_exp = -(z / axial_scale) ** 2
    gaussian = xp.exp(radial_exp + axial_exp)
    wave_number = 7.0 / scale
    wave = 1.0 + modulation * xp.cos(wave_number * z)
    d_wave = -modulation * wave_number * xp.sin(wave_number * z)
    stream = r ** 2 * gaussian * wave
    d_stream_r = 2.0 * r * gaussian * (1.0 - (r / scale) ** 2) * wave
    d_stream_z = r ** 2 * gaussian * (-2.0 * z / axial_scale ** 2 * wave + d_wave)
    return stream, d_stream_r, d_stream_z


def evaluate_volume(points: int, scale: float, modulation: float, backend: str, trusted_radius: float) -> dict[str, Any]:
    """Evaluate one complete 3D Cartesian volume."""

    xp = module_for(backend)
    line = xp.linspace(-0.5, 0.5, points, dtype=xp.float64)
    dx = float(1.0 / (points - 1))
    x, y, z = xp.meshgrid(line, line, line, indexing="ij")
    r2 = x * x + y * y
    r = xp.sqrt(r2)
    stream, d_stream_r, d_stream_z = stream_field(r, z, scale, modulation, xp)
    cutoff, d_cutoff_r, d_cutoff_z = source_cutoff(r, z, xp)

    inv_r = safe_divide(1.0, r, xp)
    inv_r2 = safe_divide(1.0, r2, xp)
    raw_ur = -d_stream_z * inv_r
    raw_uz = d_stream_r * inv_r
    axis = r == 0.0
    axis_profile = 2.0 * xp.exp(-(z / (0.75 * scale)) ** 2) * (
        1.0 + modulation * xp.cos((7.0 / scale) * z)
    )
    raw_uz = xp.where(axis, axis_profile, raw_uz)

    # A=(S/r)e_theta = (-S*y/r^2, S*x/r^2, 0) in Cartesian coordinates.
    Ax = -cutoff * stream * y * inv_r2
    Ay = cutoff * stream * x * inv_r2
    Az = xp.zeros_like(Ax)

    comm_ur = -d_cutoff_z * stream * inv_r
    comm_uz = d_cutoff_r * stream * inv_r
    local_ur = cutoff * raw_ur + comm_ur
    local_uz = cutoff * raw_uz + comm_uz
    radial_to_x = safe_divide(x, r, xp)
    radial_to_y = safe_divide(y, r, xp)
    local_x = local_ur * radial_to_x
    local_y = local_ur * radial_to_y
    comm_x = comm_ur * radial_to_x
    comm_y = comm_ur * radial_to_y

    # Independent Cartesian finite-difference curl of the actual A field.
    dAy_dx = xp.gradient(Ay, dx, axis=0, edge_order=2)
    dAy_dz = xp.gradient(Ay, dx, axis=2, edge_order=2)
    dAx_dz = xp.gradient(Ax, dx, axis=2, edge_order=2)
    dAx_dy = xp.gradient(Ax, dx, axis=1, edge_order=2)
    curl_x = -dAy_dz
    curl_y = dAx_dz
    curl_z = dAy_dx - dAx_dy
    curl_error = xp.sqrt((curl_x - local_x) ** 2 + (curl_y - local_y) ** 2 + (curl_z - local_uz) ** 2)

    divergence = (
        xp.gradient(local_x, dx, axis=0, edge_order=2)
        + xp.gradient(local_y, dx, axis=1, edge_order=2)
        + xp.gradient(local_uz, dx, axis=2, edge_order=2)
    )
    # The cylindrical representation is smooth at r=0, but the Cartesian
    # finite-difference diagnostic sees the removable 1/r factors explicitly.
    # Keep a deliberately conservative trusted mask for derivative validation;
    # the full field and its commutator remain evaluated on the whole volume.
    trusted = (r > max(10.0 * dx, trusted_radius)) & (xp.abs(x) < 0.5 - 2.0 * dx) & (xp.abs(y) < 0.5 - 2.0 * dx) & (xp.abs(z) < 0.5 - 2.0 * dx)

    def xy_integral(field: Any) -> Any:
        return trapz(trapz(field, line, axis=1, xp=xp), line, axis=0, xp=xp)

    weighted_mass = xy_integral(cutoff * raw_uz)
    local_mass = xy_integral(local_uz)
    comm_mass = xy_integral(comm_uz)
    defect = local_mass - weighted_mass
    # `gradient(..., axis=0)` is ∂/∂x, whereas the analytic expression on
    # the right is ∂/∂r.  Convert the radial derivative to Cartesian x
    # before comparing.  This is an independent product-rule check, not a
    # comparison of unlike coordinate derivatives.
    d_product_dr = cutoff * d_stream_r + d_cutoff_r * stream
    d_product_dx = d_product_dr * safe_divide(x, r, xp)
    product_error = xp.max(xp.abs(xp.gradient(cutoff * stream, dx, axis=0, edge_order=2)[trusted] - d_product_dx[trusted]))
    result = {
        "backend": backend,
        "points": points,
        "scale": scale,
        "modulation": modulation,
        "line": line,
        "mid": points // 2,
        "raw_uz": raw_uz,
        "local_uz": local_uz,
        "comm_uz": comm_uz,
        "comm_x": comm_x,
        "comm_y": comm_y,
        "cutoff": cutoff,
        "weighted_mass": weighted_mass,
        "local_mass": local_mass,
        "comm_mass": comm_mass,
        "defect": defect,
        "divergence": divergence,
        "curl_error": curl_error,
        "interior": trusted,
        "product_rule_max_error": scalar(product_error),
    }
    result["summary"] = {
        "backend": backend,
        "points": points,
        "scale": scale,
        "modulation": modulation,
        "weighted_mass_linf": scalar(xp.max(xp.abs(weighted_mass))),
        "local_mass_linf": scalar(xp.max(xp.abs(local_mass))),
        "commutator_mass_linf": scalar(xp.max(xp.abs(comm_mass))),
        "defect_linf": scalar(xp.max(xp.abs(defect))),
        "defect_l1": scalar(trapz(xp.abs(defect), line, axis=0, xp=xp)),
        "defect_signed_volume": scalar(trapz(defect, line, axis=0, xp=xp)),
        "divergence_linf_trusted": scalar(xp.max(xp.abs(divergence[trusted]))),
        "curl_error_linf_trusted": scalar(xp.max(xp.abs(curl_error[trusted]))),
        "product_rule_max_error": scalar(product_error),
    }
    return result


def release_volume(result: dict[str, Any]) -> None:
    for key in ("raw_uz", "local_uz", "comm_uz", "comm_x", "comm_y", "cutoff", "divergence", "curl_error", "interior"):
        result.pop(key, None)
    if result.get("backend") == "gpu" and cp is not None:
        cp.get_default_memory_pool().free_all_blocks()
    gc.collect()


def plot_report(path: Path, result: dict[str, Any], summaries: list[dict[str, Any]]) -> None:
    import matplotlib.pyplot as plt

    line = host(result["line"])
    mid = result["mid"]
    raw_line = host(result["raw_uz"])[:, mid, mid]
    local_line = host(result["local_uz"])[:, mid, mid]
    comm_line = host(result["comm_uz"])[:, mid, mid]
    comm_xy = np.sqrt(host(result["comm_x"])[..., mid] ** 2 + host(result["comm_y"])[..., mid] ** 2 + host(result["comm_uz"])[..., mid] ** 2)
    comm_xz = host(result["comm_uz"])[..., mid, :]
    defect = host(result["defect"])
    divergence = np.abs(host(result["divergence"])[..., mid])
    curl_error = np.abs(host(result["curl_error"])[..., mid])

    figure, axes = plt.subplots(2, 3, figsize=(21, 12), constrained_layout=True)
    axis = axes[0, 0]
    axis.plot(line, raw_line, "--", color="#444444", linewidth=2, label=r"Pure $u_z$")
    axis.plot(line, local_line, color="blue", linewidth=2.2, label=r"Localised $(\nabla\times(cA))_z$")
    axis.plot(line, comm_line, color="red", linewidth=2, label=r"Commutator $[(\nabla c)\times A]_z$")
    axis.axhline(0, color="#999999", linewidth=1)
    axis.set_title("3D Cartesian curl/cutoff line at y=z=0", fontweight="bold")
    axis.set_xlabel(r"x")
    axis.set_ylabel("Amplitude")
    axis.grid(True, linestyle="--", alpha=0.45)
    axis.legend(fontsize=8)

    image = axes[0, 1].imshow(np.log10(np.maximum(comm_xy, 1e-18)), origin="lower", extent=[-0.5, 0.5, -0.5, 0.5], cmap="inferno")
    figure.colorbar(image, ax=axes[0, 1], label=r"$\log_{10}|(\nabla c)\times A|$")
    axes[0, 1].set_title("Full 3D commutator magnitude, z=0", fontweight="bold")
    axes[0, 1].set_xlabel("x")
    axes[0, 1].set_ylabel("y")

    image = axes[0, 2].imshow(comm_xz.T, origin="lower", extent=[-0.5, 0.5, -0.5, 0.5], aspect="auto", cmap="coolwarm")
    figure.colorbar(image, ax=axes[0, 2], label=r"$[(\nabla c)\times A]_z$")
    axes[0, 2].set_title("Axial commutator slice, y=0", fontweight="bold")
    axes[0, 2].set_xlabel("x")
    axes[0, 2].set_ylabel("z")

    axes[1, 0].plot(line, defect, color="purple", linewidth=2)
    axes[1, 0].axhline(0, color="#999999", linewidth=1)
    axes[1, 0].set_title("Full x-y integrated moment defect", fontweight="bold")
    axes[1, 0].set_xlabel("z")
    axes[1, 0].set_ylabel(r"$\Delta M(z)$")
    axes[1, 0].grid(True, linestyle="--", alpha=0.45)

    image = axes[1, 1].imshow(np.log10(np.maximum(divergence, 1e-18)), origin="lower", extent=[-0.5, 0.5, -0.5, 0.5], cmap="magma")
    figure.colorbar(image, ax=axes[1, 1], label=r"$\log_{10}|\nabla\cdot u|$")
    axes[1, 1].set_title("3D divergence residual, z=0", fontweight="bold")
    axes[1, 1].set_xlabel("x")
    axes[1, 1].set_ylabel("y")

    image = axes[1, 2].imshow(np.log10(np.maximum(curl_error, 1e-18)), origin="lower", extent=[-0.5, 0.5, -0.5, 0.5], cmap="viridis")
    figure.colorbar(image, ax=axes[1, 2], label=r"$\log_{10}|\mathrm{FDcurl}-\mathrm{analyticcurl}|$")
    axes[1, 2].set_title("Independent Cartesian curl error, z=0", fontweight="bold")
    axes[1, 2].set_xlabel("x")
    axes[1, 2].set_ylabel("y")

    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path, dpi=180)
    plt.close(figure)


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Deep 3D Cartesian curl/cutoff calculation",
        "",
        "This is a CUDA-first 3D reconstruction of the exact cutoff shape in",
        "`SpatialLocalization.spatialCutoff`, followed by `curl(c*A)` on a",
        "nonseparable axisymmetric stream. It is not the selected Lean tsum.",
        "",
        "## Source bindings",
        "",
        "- `SpatialLocalization.lean:41-53`: exact squared-radius/axial cutoff.",
        "- `SpatialLocalization.lean:165-171`: cutoff potential and curl field.",
        "- `SpatialLocalization.lean:200-208`: product-rule commutator.",
        "- `SpatialLocalization.lean:210-214`: periodised potential route.",
        "- `ActualPrimaryCoherence.lean:1633-1871`: physical potential and Cartesian lift.",
        "",
        "## Finest-resolution summaries",
        "",
        "| backend | points | scale | modulation | defect L∞ | defect L1 | divergence L∞ | Cartesian curl error L∞ | product-rule error |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in payload["final_rows"]:
        lines.append("| {backend} | {points} | {scale:.3g} | {modulation:.3g} | {defect_linf:.6e} | {defect_l1:.6e} | {divergence_linf_trusted:.6e} | {curl_error_linf_trusted:.6e} | {product_rule_max_error:.6e} |".format(**row))
    lines.extend([
        "",
        "## Interpretation boundary",
        "",
        "A stable nonzero defect in this exact-cutoff 3D diagnostic establishes",
        "a numerical mechanism for moment alteration in the explicit profile.",
        "It does not establish selected `Delta m != 0`: the selected field still",
        "requires binding its actual potential sums, periodisation, `torusAverage`,",
        "`barMoment`, and axis route.",
        "",
        "## Runtime and reproducibility",
        "",
        f"- Backend: `{payload['runtime']['backend']}`",
        f"- CUDA device: `{payload['runtime']['cuda_device']}`",
        f"- Resolutions: `{payload['parameters']['resolutions']}`",
        f"- Profile scales: `{payload['parameters']['profile_scales']}`",
        f"- Modulations: `{payload['parameters']['modulations']}`",
        f"- Trusted derivative radius: `{payload['parameters']['trusted_radius']}` (axis-excluded validation mask; full 3D field remains plotted)",
        f"- Plot: `{payload['plot']}`",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--json", type=Path)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--csv", type=Path)
    parser.add_argument("--plot", type=Path)
    parser.add_argument("--no-plot", action="store_true")
    parser.add_argument("--backend", choices=("auto", "cpu", "gpu"), default="auto")
    parser.add_argument("--resolutions", type=int, nargs="+", default=DEFAULT_RESOLUTIONS)
    parser.add_argument("--profile-scales", type=float, nargs="+", default=DEFAULT_PROFILE_SCALES)
    parser.add_argument("--modulations", type=float, nargs="+", default=DEFAULT_MODULATIONS)
    parser.add_argument("--plot-scale", type=float, default=1.0)
    parser.add_argument("--plot-modulation", type=float, default=0.25)
    parser.add_argument("--plot-points", type=int, default=257)
    parser.add_argument("--trusted-radius", type=float, default=0.1,
                        help="fixed cylindrical radius excluded from derivative error metrics")
    args = parser.parse_args()

    backend = "gpu" if args.backend == "auto" and cuda_available() else ("cpu" if args.backend == "auto" else args.backend)
    if backend == "gpu" and not cuda_available():
        raise SystemExit("GPU requested but CUDA is unavailable")
    resolutions = tuple(sorted(set(int(x) for x in args.resolutions)))
    scales = tuple(float(x) for x in args.profile_scales)
    modulations = tuple(float(x) for x in args.modulations)
    if any(x < 65 for x in resolutions):
        raise SystemExit("resolutions must be at least 65")
    if any(x <= 0 for x in scales):
        raise SystemExit("profile scales must be positive")
    if not 0.0 < args.trusted_radius < 0.5:
        raise SystemExit("trusted radius must lie in (0, 0.5)")

    rows: list[dict[str, Any]] = []
    for scale in scales:
        for modulation in modulations:
            result = evaluate_volume(max(resolutions), scale, modulation, backend, args.trusted_radius)
            rows.append(result["summary"])
            release_volume(result)
            for points in resolutions[:-1]:
                result = evaluate_volume(points, scale, modulation, backend, args.trusted_radius)
                rows.append(result["summary"])
                release_volume(result)

    plot_points = args.plot_points if args.plot_points in resolutions else max(resolutions)
    plot_result = evaluate_volume(plot_points, args.plot_scale, args.plot_modulation, backend, args.trusted_radius)
    plot_path = None if args.no_plot else (args.plot or args.repo_root / "NavierStokesReview/evidence/cutoff_commutator_deep_2026-09-27.png")
    if plot_path is not None:
        plot_report(plot_path, plot_result, rows)

    final_rows = []
    for scale in scales:
        for modulation in modulations:
            candidates = [row for row in rows if row["scale"] == scale and row["modulation"] == modulation]
            final_rows.append(max(candidates, key=lambda row: row["points"]))
    payload: dict[str, Any] = {
        "instrument": "cutoff_commutator_scan",
        "status": "deep 3D Cartesian profile calculation; not selected_witness evaluation",
        "source_bindings": {
            "cutoff": "NavierStokes/SpatialLocalization.lean:41-53",
            "cut_potential": "NavierStokes/SpatialLocalization.lean:165-171",
            "product_rule": "NavierStokes/SpatialLocalization.lean:200-208",
            "periodic_potential": "NavierStokes/SpatialLocalization.lean:210-214",
            "physical_potential": "NavierStokes/ActualPrimaryCoherence.lean:1633-1871",
        },
        "parameters": {
            "backend": backend,
            "resolutions": list(resolutions),
            "profile_scales": list(scales),
            "modulations": list(modulations),
            "trusted_radius": args.trusted_radius,
            "domain": {"x": [-0.5, 0.5], "y": [-0.5, 0.5], "z": [-0.5, 0.5]},
        },
        "rows": rows,
        "final_rows": final_rows,
        "plot": str(plot_path) if plot_path is not None else None,
        "runtime": {
            "backend": backend,
            "cupy_imported": cp is not None,
            "cuda_available": cuda_available(),
            "cuda_device": cuda_device_name(),
        },
        "validation": {
            "exact_source_cutoff_reconstructed": True,
            "full_3d_cartesian_volume": True,
            "analytic_and_finite_difference_curl": True,
            "divergence_residual_recorded": True,
            "selected_field_bound": False,
            "selected_delta_m_proved": False,
        },
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    print(encoded)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(encoded, encoding="utf-8")
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    if args.markdown:
        write_markdown(args.markdown, payload)
    release_volume(plot_result)


if __name__ == "__main__":
    main()
