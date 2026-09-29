"""Profile every Lean module outside the captured NS endpoint closure.

This is a repository-wide source-accounting instrument.  It is deliberately
not a theorem prover and it does not turn token hits into semantic findings.
Each row retains the exact source hash, imports, declaration locations, marker
locations, and admitted-token locations so that later mathematical review can
be reproduced against the same file contents.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DECL_RE = re.compile(
    r"^\s*(?:@[\w.]+(?:\s+[^\n]*)?\s*)*"
    r"(?:(?:private|protected|noncomputable|unsafe)\s+)*"
    r"(?P<kind>theorem|lemma|def|abbrev|structure|class|inductive|axiom|"
    r"instance|opaque|example)\b\s*(?P<name>[A-Za-z_][A-Za-z0-9_'.]*)?"
)
IMPORT_RE = re.compile(r"^\s*import\s+(?P<module>[A-Za-z0-9_.'/-]+)")
NAMESPACE_RE = re.compile(r"^\s*namespace\s+(?P<name>[A-Za-z0-9_'.]+)")

MARKERS: dict[str, tuple[str, ...]] = {
    "endpoint": ("selected_witness", "theorem_1_1", "CandidateProperties", "candidateStatement"),
    "moments": ("barMoment", "FiveRows", "FiveProfile", "PositiveOrderMoments", "Debt", "moment"),
    "geometry": ("curl", "divergence", "Cartesian", "cylind", "axis", "radial", "chart"),
    "periodicity": ("period", "torus", "periodize", "periodic", "Fourier", "average"),
    "pressure": ("pressure", "Poisson", "Leray", "Riesz"),
    "residual_force": ("residual", "force", "NavierStokes", "Euler"),
    "regularity_energy": ("smooth", "analytic", "Gevrey", "Sobolev", "energy", "dissipation", "Integrable"),
    "support_localisation": ("support", "compact", "cutoff", "localiz", "extension", "germ"),
    "series_limits": ("tsum", "summable", "Filter", "limit", "tendsto", "convergence", "locallyFinite"),
    "comparison": ("Comparator", "uniqueness", "comparison", "competitor", "GlobalFiniteEnergy"),
    "cmi_paper": ("Fefferman", "Clay", "CMI", "Alternative", "paper", "singular", "blowup", "blow-up"),
}


def strip_comments_preserve_lines(text: str) -> str:
    """Remove nested Lean comments while retaining line count and strings."""
    out: list[str] = []
    i = 0
    depth = 0
    in_string = False
    escaped = False
    while i < len(text):
        ch = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if depth:
            if ch == "/" and nxt == "-":
                depth += 1
                out.extend((" ", " "))
                i += 2
                continue
            if ch == "-" and nxt == "/":
                depth -= 1
                out.extend((" ", " "))
                i += 2
                continue
            out.append("\n" if ch == "\n" else " ")
            i += 1
            continue
        if in_string:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue
        if ch == "/" and nxt == "-":
            depth = 1
            out.extend((" ", " "))
            i += 2
            continue
        if ch == '"':
            in_string = True
        out.append(ch)
        i += 1
    return "".join(out)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def branch_for(path: str) -> str:
    first = path.replace("\\", "/").split("/", 1)[0]
    return first or "root"


def declaration_rows(lines: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    namespace = ""
    for number, line in enumerate(lines, start=1):
        ns = NAMESPACE_RE.match(line)
        if ns:
            namespace = ns.group("name")
        match = DECL_RE.match(line)
        if not match:
            continue
        name = match.group("name") or "<anonymous>"
        qualified = f"{namespace}.{name}" if namespace and name != "<anonymous>" else name
        rows.append(
            {
                "line": number,
                "kind": match.group("kind"),
                "name": name,
                "qualified_name": qualified,
                "text": line.strip()[:500],
            }
        )
    return rows


def marker_lines(lines: list[str]) -> dict[str, list[int]]:
    lowered = [line.lower() for line in lines]
    result: dict[str, list[int]] = {}
    for family, tokens in MARKERS.items():
        hits = [
            number
            for number, line in enumerate(lowered, start=1)
            if any(token.lower() in line for token in tokens)
        ]
        if hits:
            result[family] = hits
    return result


def profile_file(root: Path, relative: str, endpoint_modules: set[str]) -> dict[str, Any]:
    path = root / relative
    raw = path.read_text(encoding="utf-8")
    stripped = strip_comments_preserve_lines(raw)
    lines = stripped.splitlines()
    imports = [m.group("module") for line in lines if (m := IMPORT_RE.match(line))]
    declarations = declaration_rows(lines)
    markers = marker_lines(lines)
    admitted_lines = [
        number
        for number, line in enumerate(lines, start=1)
        if re.search(r"\b(?:sorry|admit)\b", line)
    ]
    proof_control_lines = [
        number
        for number, line in enumerate(lines, start=1)
        if re.search(r"\bby_contra!?\b", line)
    ]
    path_text = relative.replace("\\", "/")
    endpoint_tokens = sorted(
        {
            token
            for token in MARKERS["endpoint"]
            if token.lower() in stripped.lower()
        }
    )
    direct_project_imports = [name for name in imports if name.startswith(("NavierStokes", "Euler", "Comparator"))]
    return {
        "path": path_text,
        "module": path_text[:-5].replace("/", ".") if path_text.endswith(".lean") else path_text.replace("/", "."),
        "branch": branch_for(path_text),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "lines": len(raw.splitlines()),
        "comment_stripped_lines": len(lines),
        "imports": imports,
        "direct_project_imports": direct_project_imports,
        "declarations": declarations,
        "declaration_count": len(declarations),
        "marker_lines": markers,
        "marker_families": sorted(markers),
        "endpoint_tokens": endpoint_tokens,
        "admitted_token_lines": admitted_lines,
        "proof_control_lines": proof_control_lines,
        "outside_captured_endpoint_closure": True,
        "endpoint_module_name_collision": path_text[:-5].replace("/", ".") in endpoint_modules,
        "semantic_status": "structurally_profiled_not_semantically_reviewed",
    }


def render_markdown(rows: list[dict[str, Any]], root: Path, register_path: Path) -> str:
    branch_counts = Counter(row["branch"] for row in rows)
    marker_counts = Counter(family for row in rows for family in row["marker_families"])
    risky = sorted(
        rows,
        key=lambda row: (
            bool(row["admitted_token_lines"]),
            "endpoint" in row["marker_families"],
            len(row["marker_families"]),
            row["declaration_count"],
        ),
        reverse=True,
    )
    lines = [
        "# Full external-source structural profile",
        "",
        "This report profiles every indexed Lean file outside the captured",
        "Navier--Stokes endpoint import closure. `outside_captured_endpoint_closure`",
        "is a scoped graph fact, not a dead-code or irrelevance claim.",
        "The report is source-accounting evidence, not a semantic theorem and not",
        "a proof that any marker is used by a mathematical claim.",
        "",
        f"- Source root: `{root}`",
        f"- Register input: `{register_path}`",
        f"- Files profiled: **{len(rows)}**",
        f"- Files containing admitted-token matches: **{sum(bool(r['admitted_token_lines']) for r in rows)}**",
        "",
        "## Branch counts",
        "",
        "| Branch | Files |",
        "|---|---:|",
    ]
    lines.extend(f"| `{branch}` | {count} |" for branch, count in sorted(branch_counts.items()))
    lines += ["", "## Marker-family counts", "", "| Family | Files |", "|---|---:|"]
    lines.extend(f"| `{family}` | {count} |" for family, count in sorted(marker_counts.items()))
    lines += [
        "",
        "## Highest-review-risk structural rows",
        "",
        "This queue is prioritisation only. Every row remains unreviewed semantically",
        "until a bounded source report records the declarations and proof obligations.",
        "",
        "| Path | Branch | Lines | Decls | Marker families | Admitted tokens |",
        "|---|---|---:|---:|---|---:|",
    ]
    for row in risky[:150]:
        families = ", ".join(row["marker_families"])
        lines.append(
            f"| `{row['path']}` | `{row['branch']}` | {row['lines']} | {row['declaration_count']} | {families} | {len(row['admitted_token_lines'])} |"
        )
    lines += [
        "",
        "## Required interpretation",
        "",
        "1. An import or token hit is a navigation signal, not proof of theorem use.",
        "2. A source file outside the selected endpoint closure may belong to Euler,",
        "   a comparator, an alternate theorem, or an independent construction.",
        "3. Admitted-token rows require direct source review and endpoint reachability",
        "   checks; this profile does not infer contamination.",
        "4. A paper-level bridge is cleared only by an inspected declaration and its",
        "   proof term connecting the exact selected field to the claimed observable.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    register = json.loads(args.register.read_text(encoding="utf-8"))
    rows = register.get("rows", [])
    if not rows:
        # Older register snapshots used a module list; keep the tool explicit
        # about which representation it consumed rather than silently treating
        # the top-level module count as an iterable.
        candidate = register.get("modules", [])
        rows = candidate if isinstance(candidate, list) else []
    endpoint_modules = {row["module"] for row in rows if row.get("reachable")}
    external_paths = [row["path"] for row in rows if not row.get("reachable")]
    profiles = [profile_file(args.root, relative, endpoint_modules) for relative in external_paths]
    payload = {
        "schema": "external-source-profile/v1",
        "tool": "external_source_profile.py",
        "scope": "all indexed Lean modules outside the captured endpoint closure",
        "semantic_status": "structural_profile_only",
        "root": str(args.root),
        "register": str(args.register),
        "counts": {
            "indexed_external_files": len(profiles),
            "admitted_token_files": sum(bool(row["admitted_token_lines"]) for row in profiles),
            "endpoint_marker_files": sum(bool(row["endpoint_tokens"]) for row in profiles),
        },
        "files": profiles,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.markdown.write_text(render_markdown(profiles, args.root, args.register), encoding="utf-8")


if __name__ == "__main__":
    main()
