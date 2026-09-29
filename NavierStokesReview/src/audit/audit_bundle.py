#!/usr/bin/env python3
"""Validate and package the review repository's mapping evidence.

The bundle is intentionally conservative.  It does not infer theorem use from
file names or token hits.  It records five separate evidence layers:

1. the extracted tree snapshot and its hash;
2. current checkout paths, sizes, and hashes;
3. exact source imports and parsed source spans;
4. exact compiled-environment declaration edges;
5. repository state and explicit validation failures.

The first four layers remain separate in the JSON schema so a reviewer can see
which conclusions are filesystem facts, source diagnostics, or kernel-derived
facts.  A non-empty diagnostic layer never upgrades a claim in the kernel
layer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from tree_reconciliation import reconcile


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def git_status(repo: Path) -> list[dict[str, str]]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    rows: list[dict[str, str]] = []
    for line in result.stdout.splitlines():
        if not line:
            continue
        rows.append({"index": line[:2], "path": line[3:]})
    return rows


def current_file_hashes(repo: Path) -> dict[str, dict[str, Any]]:
    files: dict[str, dict[str, Any]] = {}
    for path in sorted(repo.rglob("*")):
        if (
            not path.is_file()
            or ".git" in path.parts
            or ".lake" in path.parts
            or "__pycache__" in path.parts
            or path.suffix == ".pyc"
        ):
            continue
        relative = path.relative_to(repo).as_posix()
        files[relative] = {
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
    return files


def source_hash_drift(source_map: dict[str, Any], repo: Path) -> list[dict[str, str]]:
    drift: list[dict[str, str]] = []
    for module, record in source_map["modules"].items():
        path = repo / record["path"]
        if not path.is_file():
            drift.append({"module": module, "path": record["path"], "reason": "missing"})
            continue
        actual = sha256(path)
        if actual != record["sha256"]:
            drift.append(
                {
                    "module": module,
                    "path": record["path"],
                    "reason": "sha256_changed",
                    "mapped": record["sha256"],
                    "actual": actual,
                }
            )
    return drift


def validate(
    repo: Path,
    tree: Path,
    source_map: dict[str, Any],
    joined: dict[str, Any],
    reconciliation: dict[str, Any],
    source_map_path: Path,
    joined_path: Path,
    reconciliation_path: Path,
) -> dict[str, Any]:
    failures: list[str] = []
    tree_hash = sha256(tree)
    if source_map["inputs"].get("tree_sha256") != tree_hash:
        failures.append("tree hash differs from the source-map input")
    drift = source_hash_drift(source_map, repo)
    if drift:
        failures.append(f"{len(drift)} mapped source files changed after source-map generation")

    routes = joined.get("routes", {})
    required_routes = [
        "NavierStokesR3.theorem_1_1",
        "NavierStokes.ActualCandidateAssembly.selected_witness",
        "NavierStokes.FiveRowRank.FiveRows",
        "NavierStokes.PositiveOrderMoments.Debt",
        "NavierStokes.MeanRankUpdate.scaleDebt",
        "NavierStokes.DefectIncrementBounds.barMoment",
        "NavierStokesR3.ProblemStatement.CandidateProperties",
    ]
    unreachable = [name for name in required_routes if not routes.get(name, {}).get("reachable", False)]
    if unreachable:
        failures.append("required compiled route missing: " + ", ".join(unreachable))
    if joined["counts"].get("joined_nodes_using_sorryAx", 0) != 0:
        failures.append("reachable compiled closure contains sorryAx users")

    status = git_status(repo)
    reconciliation_counts = reconciliation["counts"]
    return {
        "schema": "navier-stokes-review-audit-bundle/v2",
        "evidence_policy": {
            "tree": "inventory/provenance snapshot; never a substitute for current paths",
            "filesystem": "exact current checkout path, byte count, and SHA-256",
            "source": "exact imports and source-coordinate diagnostics",
            "kernel": "compiled environment declaration edges and endpoint routes",
            "heuristics": "diagnostic only; cannot establish theorem use or a contradiction",
        },
        "inputs": {
            "repository": str(repo.resolve()),
            "tree": str(tree.resolve()),
            "tree_sha256": tree_hash,
            "source_map": str(source_map_path.resolve()),
            "source_map_sha256": sha256(source_map_path),
            "joined_environment": str(joined_path.resolve()),
            "joined_environment_sha256": sha256(joined_path),
            "tree_reconciliation": str(reconciliation_path.resolve()),
            "tree_reconciliation_sha256": sha256(reconciliation_path),
        },
        "counts": {
            "tree_entries": source_map["counts"]["tree_file_entries"],
            "current_files": source_map["counts"]["current_files_excluding_git_lake"],
            "lean_modules": source_map["counts"]["current_lean_modules"],
            "source_declarations": source_map["counts"]["declarations"],
            "diagnostic_edges": source_map["counts"]["diagnostic_declaration_edges"],
            "environment_nodes": joined["counts"]["environment_nodes"],
            "environment_edges": joined["counts"]["joined_edges"],
            "exact_source_matches": joined["counts"]["exact_source_matches"],
            "reachable_sorryAx_users": joined["counts"]["joined_nodes_using_sorryAx"],
            "git_status_entries": len(status),
            "tree_ambiguous_entries": reconciliation_counts["ambiguous_tree_files"],
            "tree_missing_entries": reconciliation_counts["missing_tree_files"],
        },
        "validation": {
            "passed": not failures,
            "failures": failures,
            "source_hash_drift": drift,
            "required_routes": required_routes,
            "unreachable_required_routes": unreachable,
            "tree_reconciliation": {
                "passed": reconciliation_counts["missing_tree_files"] == 0,
                "missing_entries_are_review_obligations": reconciliation_counts["missing_tree_files"] > 0,
                "ambiguous_entries_are_review_obligations": reconciliation_counts["ambiguous_tree_files"] > 0,
            },
        },
        "git_status": status,
        "selected_routes": {
            name: routes.get(name, {"reachable": False, "path": []})
            for name in required_routes
        },
    }


def markdown(bundle: dict[str, Any]) -> str:
    counts = bundle["counts"]
    validation = bundle["validation"]
    lines = [
        "# Hardened audit bundle",
        "",
        "This is a reproducibility index for the review-side source and compiled-environment maps.",
        "The layers are deliberately not merged into one claim: filesystem identity, source navigation, and kernel reachability answer different questions.",
        "",
        "## Validation",
        "",
        f"- Bundle validation: **{'passed' if validation['passed'] else 'failed'}**",
        f"- Tree SHA-256: `{bundle['inputs']['tree_sha256']}`",
        f"- Reachable compiled declarations using `sorryAx`: `{counts['reachable_sorryAx_users']}`",
        f"- Git status entries at capture: `{counts['git_status_entries']}`",
        f"- Tree entries without a current basename: `{counts['tree_missing_entries']}`",
        f"- Tree entries with ambiguous current basenames: `{counts['tree_ambiguous_entries']}`",
        "",
        "## Counts",
        "",
        "| Layer | Count | Meaning |",
        "|---|---:|---|",
        f"| Extracted-tree entries | `{counts['tree_entries']}` | inventory snapshot |",
        f"| Current checkout files | `{counts['current_files']}` | filesystem census |",
        f"| Lean modules | `{counts['lean_modules']}` | source module census |",
        f"| Source declarations | `{counts['source_declarations']}` | parser diagnostics |",
        f"| Diagnostic declaration edges | `{counts['diagnostic_edges']}` | token-based, non-authoritative |",
        f"| Compiled environment nodes | `{counts['environment_nodes']}` | kernel environment export |",
        f"| Compiled environment edges | `{counts['environment_edges']}` | declaration references |",
        f"| Exact source matches | `{counts['exact_source_matches']}` | fully qualified name join |",
        "",
        "## Required endpoint routes",
        "",
    ]
    for name, route in bundle["selected_routes"].items():
        if route.get("reachable"):
            lines.append(f"- `{name}`: reachable through `{len(route['path']) - 1}` compiled edges")
        else:
            lines.append(f"- `{name}`: **not reachable in captured environment**")
    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "The route results show compiled reachability, not the value-level transport of a mathematical invariant. A missing value theorem remains an open correspondence obligation even when every upstream module is reachable.",
            "",
            "Tree reconciliation is intentionally reported separately: a missing or ambiguous inventory basename is a snapshot reconciliation issue, not evidence that a Lean module or theorem is absent.",
            "",
            "## Reproduction",
            "",
            "Run `NavierStokesReview/src/audit/run_hardened_audit.ps1`; it regenerates the source map and compiled environment export before this bundle is rebuilt.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--source-map", type=Path, required=True)
    parser.add_argument("--joined", type=Path, required=True)
    parser.add_argument("--reconciliation", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    bundle = validate(
        args.repo.resolve(),
        args.tree.resolve(),
        load(args.source_map),
        load(args.joined),
        load(args.reconciliation),
        args.source_map.resolve(),
        args.joined.resolve(),
        args.reconciliation.resolve(),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.markdown.write_text(markdown(bundle), encoding="utf-8")
    print(json.dumps({"schema": bundle["schema"], **bundle["counts"], **bundle["validation"]}, sort_keys=True))
    if not bundle["validation"]["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
