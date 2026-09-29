#!/usr/bin/env python3
"""Build a path-aware, reproducible audit map for the Lean repository.

This tool deliberately separates evidence levels:

* filesystem and SHA-256 records are exact for the checkout being audited;
* import edges are exact for source imports and are resolved by module path;
* declaration records are source-coordinate diagnostics;
* declaration references are heuristic until replaced by Lean environment
  metadata from a compiled `.olean` environment.

The extracted tree is an inventory input, not an authority about current
source contents.  Basename-only tree exports are reported as such and are
never used to infer a source path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Iterable


TREE_FILE_RE = re.compile(r"📄\s+(.+?)\s*$")
IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)")
NAMESPACE_RE = re.compile(r"^\s*namespace\s+([A-Za-z0-9_.]+)")
SECTION_RE = re.compile(r"^\s*(?:(?:noncomputable|scoped)\s+)*section(?:\s+([A-Za-z0-9_.]+))?")
END_RE = re.compile(r"^\s*end(?:\s+([A-Za-z0-9_.]+))?\s*$")
DECL_RE = re.compile(
    r"^\s*(?:(?:private|protected|noncomputable|unsafe|partial|classical|opaque)\s+)*"
    r"(def|theorem|lemma|structure|class|abbrev|inductive|axiom|opaque|example)\s+"
    r"([A-Za-z0-9_'.]+)"
)
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*")

ROOT_MODULES = (
    "NavierStokes.ActualCandidateAssembly",
    "NavierStokes.R3.ActualCandidate",
    "NavierStokes.R3.Theorem",
    "NavierStokes.ActualCandidateConstruction",
    "NavierStokes.PositiveOrderMoments",
    "NavierStokes.FiveRowRank",
    "NavierStokes.MeanRankUpdate",
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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


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


def source_files(repo: Path) -> list[Path]:
    return sorted(
        path
        for path in repo.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and ".lake" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    )


def parse_declarations(lines: list[str]) -> list[dict[str, Any]]:
    # Keep each namespace command as one scope.  Extending a flat component
    # list loses the boundary between `namespace A.B` and a nested
    # `namespace C`, so `end C` can accidentally pop `B` instead of `C`.
    namespace_scopes: list[list[str]] = []
    block_stack: list[tuple[str, list[str] | None]] = []
    declarations: list[dict[str, Any]] = []
    for line_number, line in enumerate(lines, 1):
        namespace_match = NAMESPACE_RE.match(line)
        if namespace_match:
            parts = namespace_match.group(1).split(".")
            namespace_scopes.append(parts)
            block_stack.append(("namespace", parts))
            continue
        section_match = SECTION_RE.match(line)
        if section_match:
            name = section_match.group(1)
            block_stack.append(("section", name.split(".") if name else None))
            continue
        end_match = END_RE.match(line)
        if end_match and block_stack:
            namespace = end_match.group(1)
            if namespace:
                parts = namespace.split(".")
                match_index = next(
                    (
                        index
                        for index in range(len(block_stack) - 1, -1, -1)
                        if block_stack[index][1] == parts
                    ),
                    None,
                )
                if match_index is not None:
                    removed = block_stack[match_index:]
                    del block_stack[match_index:]
                    for kind, scope in removed:
                        if kind == "namespace" and scope in namespace_scopes:
                            namespace_scopes.remove(scope)
            else:
                kind, scope = block_stack.pop()
                if kind == "namespace" and scope in namespace_scopes:
                    namespace_scopes.remove(scope)
            continue
        declaration_match = DECL_RE.match(line)
        if declaration_match:
            kind, short_name = declaration_match.groups()
            namespace = [part for scope in namespace_scopes for part in scope]
            qualified = ".".join((*namespace, short_name))
            declarations.append(
                {"line": line_number, "kind": kind, "name": qualified, "short_name": short_name}
            )
    for index, declaration in enumerate(declarations):
        next_line = declarations[index + 1]["line"] if index + 1 < len(declarations) else len(lines) + 1
        declaration["end_line"] = next_line - 1
    return declarations


def project_imports(imports: Iterable[str], modules: dict[str, Any]) -> dict[str, list[str]]:
    resolved: list[str] = []
    external: list[str] = []
    missing_project: list[str] = []
    for imported in imports:
        if imported in modules:
            resolved.append(imported)
        elif imported.startswith("NavierStokes") or imported.startswith("Euler"):
            missing_project.append(imported)
        else:
            external.append(imported)
    return {"resolved": resolved, "external": external, "missing_project": missing_project}


def scan_modules(repo: Path) -> dict[str, dict[str, Any]]:
    modules: dict[str, dict[str, Any]] = {}
    paths = [path for path in repo.rglob("*.lean") if ".git" not in path.parts and ".lake" not in path.parts]
    for path in sorted(paths):
        relative = path.relative_to(repo)
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        imports = [match.group(1) for line in lines if (match := IMPORT_RE.match(line))]
        declarations = parse_declarations(lines)
        hits = {
            symbol: [line_number for line_number, line in enumerate(lines, 1) if symbol in line]
            for symbol in SYMBOLS
        }
        hits = {symbol: locations for symbol, locations in hits.items() if locations}
        modules[module_name(relative)] = {
            "path": relative.as_posix(),
            "sha256": sha256(path),
            "line_count": len(lines),
            "imports": imports,
            "declarations": declarations,
            "symbol_hits": hits,
            "source_flags": {
                "unsafe": any(re.search(r"\bunsafe\b", line) for line in lines),
                "axiom_declaration": any(re.match(r"^\s*axiom\b", line) for line in lines),
                "sorry_token": any(re.search(r"\bsorry\b", line) for line in lines),
                "admit_token": any(re.search(r"\badmit\b", line) for line in lines),
            },
        }
    for module in modules.values():
        module["import_resolution"] = project_imports(module["imports"], modules)
    return modules


def dependency_subgraph(modules: dict[str, dict[str, Any]], depth: int) -> dict[str, Any]:
    queue: deque[tuple[str, int]] = deque((root, 0) for root in ROOT_MODULES)
    seen: set[str] = set()
    edges: list[dict[str, Any]] = []
    while queue:
        current, level = queue.popleft()
        if current in seen or level > depth:
            continue
        seen.add(current)
        module = modules.get(current)
        if module is None:
            continue
        for imported in module["import_resolution"]["resolved"]:
            edges.append({"from": current, "to": imported, "depth": level + 1})
            queue.append((imported, level + 1))
    missing = sorted(
        {name for module in modules.values() for name in module["import_resolution"]["missing_project"]}
    )
    return {"roots": list(ROOT_MODULES), "depth": depth, "reachable_modules": sorted(seen), "edges": edges, "missing_project_imports": missing}


def declaration_reference_diagnostics(modules: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Extract source-text references, explicitly marked as non-authoritative."""
    declarations: list[tuple[str, str, dict[str, Any]]] = []
    for module, data in modules.items():
        for declaration in data["declarations"]:
            declarations.append((module, declaration["name"], declaration))
    by_full_name = {name: (module, declaration) for module, name, declaration in declarations}
    by_short: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for module, name, declaration in declarations:
        by_short[declaration["short_name"]].append((module, declaration))
    edges: list[dict[str, Any]] = []
    source_cache: dict[str, list[str]] = {}
    repo = Path(__file__).resolve().parents[3]
    for module, data in modules.items():
        source = modules[module]["path"]
        if source not in source_cache:
            source_cache[source] = (repo / source).read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
        text_lines = source_cache[source]
        for declaration in data["declarations"]:
            body = "\n".join(text_lines[declaration["line"] - 1 : declaration["end_line"]])
            tokens = set(TOKEN_RE.findall(body))
            for token in tokens:
                target = by_full_name.get(token)
                if target is not None and token != declaration["name"]:
                    edges.append({"from": declaration["name"], "to": token, "module": module, "resolution": "qualified-token"})
                candidates = by_short.get(token, [])
                if len(candidates) == 1:
                    target_module, target_decl = candidates[0]
                    if target_decl["name"] != declaration["name"] and "." not in token:
                        edges.append({"from": declaration["name"], "to": target_decl["name"], "module": module, "resolution": "unique-short-token"})
    unique = {(edge["from"], edge["to"], edge["resolution"]): edge for edge in edges}
    return sorted(unique.values(), key=lambda edge: (edge["from"], edge["to"], edge["resolution"]))


def build_payload(repo: Path, tree_path: Path, depth: int) -> dict[str, Any]:
    entries = read_tree_entries(tree_path)
    modules = scan_modules(repo)
    files = source_files(repo)
    tree_names = {entry["name"] for entry in entries}
    current_names = {path.name for path in files}
    duplicate_tree_names = sorted(name for name in tree_names if sum(entry["name"] == name for entry in entries) > 1)
    duplicate_current_names = sorted(name for name in current_names if sum(path.name == name for path in files) > 1)
    reference_edges = declaration_reference_diagnostics(modules)
    return {
        "schema": "navier-stokes-review-hardened-source-map/v1",
        "evidence_levels": {
            "filesystem": "exact checkout paths, sizes, and SHA-256 hashes",
            "imports": "exact source import lines resolved against local module names",
            "declarations": "source-coordinate parser; use Lean environment export for final authority",
            "declaration_references": "diagnostic token matching only; never kernel evidence",
        },
        "inputs": {
            "repository": str(repo.resolve()),
            "extracted_tree": str(tree_path.resolve()),
            "tree_sha256": sha256(tree_path),
            "tree_line_count": len(tree_path.read_text(encoding="utf-8", errors="replace").splitlines()),
        },
        "counts": {
            "tree_file_entries": len(entries),
            "tree_unique_basenames": len(tree_names),
            "current_files_excluding_git_lake": len(files),
            "current_lean_modules": len(modules),
            "declarations": sum(len(module["declarations"]) for module in modules.values()),
            "diagnostic_declaration_edges": len(reference_edges),
            "duplicate_tree_basenames": len(duplicate_tree_names),
            "duplicate_current_basenames": len(duplicate_current_names),
        },
        "inventory": {
            "tree_names_not_in_current_basenames": sorted(tree_names - current_names),
            "current_basenames_not_in_tree": sorted(current_names - tree_names),
            "duplicate_tree_basenames": duplicate_tree_names,
            "duplicate_current_basenames": duplicate_current_names,
            "warning": "basename comparison is diagnostic only; paths and hashes are authoritative",
        },
        "key_paths": {
            relative.as_posix(): (repo / relative).is_file()
            for relative in (
                Path("NavierStokes/R3.lean"),
                Path("NavierStokes/R3PressureFourier.lean"),
                Path("NavierStokes/R3EnergyNorms.lean"),
                Path("NavierStokes/R3EnergyBoundary.lean"),
                Path("NavierStokes/R3/ActualCandidate.lean"),
                Path("NavierStokes/R3/Theorem.lean"),
                Path("NavierStokes/ActualCandidateAssembly.lean"),
                Path("NavierStokes/ActualCandidateConstruction.lean"),
                Path("NavierStokes/PositiveOrderMoments.lean"),
                Path("NavierStokes/FiveProfileMoments.lean"),
                Path("NavierStokes/FiveRowRank.lean"),
                Path("NavierStokes/MeanRankUpdate.lean"),
                Path("NavierStokes/R3/PressureRecovery.lean"),
                Path("NavierStokes/R3/ActualPressureFlux.lean"),
            )
        },
        "dependency_subgraph": dependency_subgraph(modules, depth),
        "diagnostic_declaration_edges": reference_edges,
        "modules": modules,
    }


def markdown_report(payload: dict[str, Any]) -> str:
    counts = payload["counts"]
    graph = payload["dependency_subgraph"]
    lines = [
        "# Hardened source and logic map",
        "",
        "This report is generated from the extracted tree and the current checkout. Paths, imports, and hashes are evidence; declaration token edges are diagnostic only until replaced by Lean environment metadata.",
        "",
        "## Inventory",
        "",
        f"- Extracted tree: `{payload['inputs']['extracted_tree']}`",
        f"- Tree SHA-256: `{payload['inputs']['tree_sha256']}`",
        f"- Tree entries / unique basenames: `{counts['tree_file_entries']}` / `{counts['tree_unique_basenames']}`",
        f"- Current files / Lean modules: `{counts['current_files_excluding_git_lake']}` / `{counts['current_lean_modules']}`",
        f"- Current declarations: `{counts['declarations']}`",
        f"- Duplicate tree basenames: `{counts['duplicate_tree_basenames']}`; duplicate checkout basenames: `{counts['duplicate_current_basenames']}`",
        "",
        "## Endpoint module closure",
        "",
        f"Roots: `{', '.join(graph['roots'])}`",
        f"Resolved modules at depth `{graph['depth']}`: `{len(graph['reachable_modules'])}`",
        f"Resolved import edges: `{len(graph['edges'])}`",
        f"Missing project imports: `{len(graph['missing_project_imports'])}`",
        "",
        "## Interpretation rule",
        "",
        "A module being reachable does not prove that a declaration is used by an endpoint. Conversely, a declaration-level source-token edge is not a kernel dependency. The final declaration closure must come from Lean environment metadata, followed by `#print axioms` on each load-bearing endpoint.",
        "",
        "## Next machine check",
        "",
        "Export the selected endpoint's declaration environment from the compiled Lean project, compare it with this source map, and investigate every edge involving `barMoment`, `FiveRows`, `selected_witness`, `navierStokesResidual`, and `pressure_support`.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--depth", type=int, default=100)
    args = parser.parse_args()
    payload = build_payload(args.repo.resolve(), args.tree.resolve(), args.depth)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown_report(payload), encoding="utf-8")
    print(json.dumps({"counts": payload["counts"], "output": str(args.output), "markdown": str(args.markdown) if args.markdown else None}, indent=2))


if __name__ == "__main__":
    main()
