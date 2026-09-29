#!/usr/bin/env python3
"""Build a reproducible source-tree and Lean dependency map for the review.

The generated map is review-side evidence.  It does not modify the authors'
``NavierStokes`` source tree and it treats the extracted tree as a path
inventory, while using the checked-out filesystem and Lean imports as the
authoritative source for current content and dependency edges.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


TREE_FILE_RE = re.compile(r"📄\s+(.+?)\s*$")
IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)")
DECL_RE = re.compile(
    r"^\s*(?:noncomputable\s+)?"
    r"(def|theorem|lemma|structure|class|abbrev|inductive)\s+"
    r"([A-Za-z0-9_'.]+)"
)

SYMBOLS = (
    "selected_witness",
    "selected_candidate",
    "CandidateProperties",
    "potentialStages",
    "selectedPotentialStages",
    "selectedDirectStages",
    "barMoment",
    "pressure_support",
    "navierStokesResidual",
    "FiveRows",
    "scaleDebt",
)

ROOT_MODULES = (
    "NavierStokes.ActualCandidateAssembly",
    "NavierStokes.R3.ActualCandidate",
    "NavierStokes.R3.Theorem",
    "NavierStokes.ActualCandidateConstruction",
    "NavierStokes.PositiveOrderMoments",
    "NavierStokes.FiveRowRank",
    "NavierStokes.MeanRankUpdate",
)


def module_name(relative: Path) -> str:
    return ".".join(relative.with_suffix("").parts)


def read_tree_entries(tree_path: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        tree_path.read_text(encoding="utf-8", errors="replace").splitlines(), 1
    ):
        match = TREE_FILE_RE.search(line)
        if match:
            entries.append({"line": line_number, "name": match.group(1)})
    return entries


def scan_lean(repo: Path) -> dict[str, dict[str, Any]]:
    modules: dict[str, dict[str, Any]] = {}
    for path in sorted(repo.rglob("*.lean")):
        if ".git" in path.parts or ".lake" in path.parts:
            continue
        relative = path.relative_to(repo)
        name = module_name(relative)
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        imports = [match.group(1) for line in lines if (match := IMPORT_RE.match(line))]
        declarations = [
            {"line": line_number, "kind": match.group(1), "name": match.group(2)}
            for line_number, line in enumerate(lines, 1)
            if (match := DECL_RE.match(line))
        ]
        hits = {
            symbol: [line_number for line_number, line in enumerate(lines, 1) if symbol in line]
            for symbol in SYMBOLS
        }
        hits = {symbol: locations for symbol, locations in hits.items() if locations}
        modules[name] = {
            "path": relative.as_posix(),
            "line_count": len(lines),
            "imports": imports,
            "declarations": declarations,
            "symbol_hits": hits,
        }
    return modules


def dependency_subgraph(modules: dict[str, dict[str, Any]], depth: int) -> dict[str, Any]:
    queue: deque[tuple[str, int]] = deque((root, 0) for root in ROOT_MODULES)
    seen: set[str] = set()
    edges: list[dict[str, str]] = []
    missing: set[str] = set()
    while queue:
        current, level = queue.popleft()
        if current in seen or level > depth:
            continue
        seen.add(current)
        module = modules.get(current)
        if module is None:
            missing.add(current)
            continue
        for imported in module["imports"]:
            edges.append({"from": current, "to": imported})
            if imported not in seen:
                queue.append((imported, level + 1))
    return {
        "roots": list(ROOT_MODULES),
        "depth": depth,
        "reachable_modules": sorted(seen),
        "edges": edges,
        "missing_import_modules": sorted(missing),
    }


def build_payload(repo: Path, tree_path: Path, depth: int) -> dict[str, Any]:
    tree_entries = read_tree_entries(tree_path)
    modules = scan_lean(repo)
    actual_files = [
        path.relative_to(repo).as_posix()
        for path in sorted(repo.rglob("*"))
        if path.is_file() and ".git" not in path.parts and ".lake" not in path.parts
    ]
    actual_names = {Path(path).name for path in actual_files}
    tree_names = {entry["name"] for entry in tree_entries}
    symbol_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for module, data in modules.items():
        for symbol, locations in data["symbol_hits"].items():
            symbol_index[symbol].append(
                {"module": module, "path": data["path"], "lines": locations}
            )
    return {
        "schema": "navier-stokes-review-source-tree-map/v1",
        "inputs": {
            "repository": str(repo.resolve()),
            "extracted_tree": str(tree_path.resolve()),
            "tree_line_count": len(tree_path.read_text(encoding="utf-8", errors="replace").splitlines()),
        },
        "counts": {
            "tree_file_entries": len(tree_entries),
            "tree_unique_names": len(tree_names),
            "actual_files_excluding_git_lake": len(actual_files),
            "actual_lean_modules": len(modules),
        },
        "basename_inventory_only": {
            "tree_names_not_in_current_files": sorted(tree_names - actual_names),
            "current_names_not_in_tree": sorted(actual_names - tree_names),
            "note": "Basename comparison is diagnostic only; duplicate names require path-level reconciliation.",
        },
        "key_paths": {
            path: (repo / path).is_file()
            for path in (
                "NavierStokes/R3.lean",
                "NavierStokes/R3PressureFourier.lean",
                "NavierStokes/R3EnergyNorms.lean",
                "NavierStokes/R3EnergyBoundary.lean",
                "NavierStokes/R3/ActualCandidate.lean",
                "NavierStokes/R3/Theorem.lean",
                "NavierStokes/ActualCandidateAssembly.lean",
                "NavierStokes/ActualCandidateConstruction.lean",
                "NavierStokes/PositiveOrderMoments.lean",
                "NavierStokes/FiveProfileMoments.lean",
                "NavierStokes/FiveRowRank.lean",
                "NavierStokes/MeanRankUpdate.lean",
                "NavierStokes/R3/PressureRecovery.lean",
                "NavierStokes/R3/ActualPressureFlux.lean",
            )
        },
        "symbol_index": {key: value for key, value in sorted(symbol_index.items())},
        "dependency_subgraph": dependency_subgraph(modules, depth),
        "modules": modules,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--depth", type=int, default=2)
    args = parser.parse_args()
    payload = build_payload(args.repo.resolve(), args.tree.resolve(), args.depth)
    rendered = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps({"counts": payload["counts"], "output": str(args.output) if args.output else None}, indent=2))


if __name__ == "__main__":
    main()
