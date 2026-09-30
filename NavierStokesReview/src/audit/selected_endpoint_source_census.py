"""Whole-tree source census for the selected Navier--Stokes endpoint.

This is a repository audit instrument, not a surrogate PDE calculation.  It
reads every current Lean source file in the repository (excluding build and
VCS directories), builds the local import
closure from the exported endpoint roots, counts declarations and exact
symbol occurrences, and reports declaration blocks where moment symbols and
endpoint/field symbols co-occur.  The co-occurrence results are lexical
triage, not proof of theorem transport; every candidate still requires
manual source verification.

The output is intentionally numerical and complete over the current source
tree.  It never invents a profile, cutoff, quadrature rule, field value, or
radial integral.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


DECL_RE = re.compile(
    r"^\s*(?:(?:private|protected|noncomputable|unsafe)\s+)*"
    r"(theorem|lemma|def|abbrev|structure|class|inductive|opaque|axiom|example)"
    r"\s+([A-Za-z_][A-Za-z0-9_'.]*)"
)
IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)", re.MULTILINE)
IDENT_RE_TEMPLATE = r"(?<![A-Za-z0-9_']){name}(?![A-Za-z0-9_'])"

CLUSTERS: dict[str, tuple[str, ...]] = {
    "moment": (
        "barMoment",
        "FiveRows",
        "FiveProfileMoments",
        "PositiveOrderMoments",
        "NominalProfile",
        "five_moments",
        "massMoment",
        "angularMoment",
    ),
    "debt": ("Debt",),
    "endpoint": (
        "selected_witness",
        "ActualCandidateAssembly",
        "CandidateProperties",
        "candidateStatement",
        "breakdownStatement",
    ),
    "field": (
        "potentialSum",
        "ASum",
        "BSum",
        "PSum",
        "VelocityField",
        "PhysicalData",
        "Cartesian",
    ),
    "rates": ("NativeBounds", "StageEstimates", "JetRate", "VanishingJointJets"),
    "transform": (
        "SpatialLocalization",
        "MixedPeriodicAssembly",
        "torusAverage",
        "periodize",
        "curl",
        "tsum",
        "StateRealization",
    ),
    "pressure": (
        "PressureRecovery",
        "pressure_support",
        "Riesz",
        "Poisson",
        "PressureFlux",
    ),
}


@dataclass(frozen=True)
class SourceFile:
    module: str
    path: str
    lines: int
    bytes: int
    imports: tuple[str, ...]
    symbol_counts: dict[str, int]
    clusters: tuple[str, ...]


@dataclass(frozen=True)
class Declaration:
    module: str
    path: str
    line: int
    kind: str
    name: str
    symbols: tuple[str, ...]
    clusters: tuple[str, ...]


def module_name(repo_root: Path, path: Path) -> str:
    return ".".join(path.relative_to(repo_root).with_suffix("").parts)


def symbols_in(text: str, names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = len(re.findall(IDENT_RE_TEMPLATE.format(name=re.escape(name)), text))
    return {name: count for name, count in counts.items() if count}


def clusters_for(symbol_counts: dict[str, int]) -> tuple[str, ...]:
    return tuple(
        cluster
        for cluster, names in CLUSTERS.items()
        if any(name in symbol_counts for name in names)
    )


def read_sources(repo_root: Path, source_root: Path) -> tuple[list[SourceFile], dict[str, Path]]:
    paths = sorted(
        path
        for path in source_root.rglob("*.lean")
        if ".lake" not in path.parts and ".git" not in path.parts
    )
    names = tuple(name for names in CLUSTERS.values() for name in names)
    records: list[SourceFile] = []
    module_paths: dict[str, Path] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        module = module_name(repo_root, path)
        imports = tuple(IMPORT_RE.findall(text))
        counts = symbols_in(text, names)
        records.append(
            SourceFile(
                module=module,
                path=path.relative_to(repo_root).as_posix(),
                lines=text.count("\n") + (0 if text.endswith("\n") else 1),
                bytes=path.stat().st_size,
                imports=imports,
                symbol_counts=counts,
                clusters=clusters_for(counts),
            )
        )
        module_paths[module] = path
    return records, module_paths


def local_closure(
    records: dict[str, SourceFile], roots: tuple[str, ...]
) -> tuple[set[str], set[str], set[str]]:
    reachable: set[str] = set()
    missing_local: set[str] = set()
    external: set[str] = set()
    known_prefixes = {module.split(".", 1)[0] for module in records}
    queue: deque[str] = deque(roots)
    while queue:
        module = queue.popleft()
        if module in reachable:
            continue
        if module not in records:
            if module.split(".", 1)[0] in known_prefixes:
                missing_local.add(module)
            else:
                external.add(module)
            continue
        reachable.add(module)
        queue.extend(records[module].imports)
    return reachable, missing_local, external


def declarations_for(repo_root: Path, files: Iterable[SourceFile]) -> list[Declaration]:
    declarations: list[Declaration] = []
    all_names = tuple(name for names in CLUSTERS.values() for name in names)
    for source in files:
        path = repo_root / source.path
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        starts: list[tuple[int, str, str]] = []
        for index, line in enumerate(lines):
            match = DECL_RE.match(line)
            if match:
                starts.append((index, match.group(1), match.group(2)))
        for position, (start, kind, name) in enumerate(starts):
            stop = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
            body = "\n".join(lines[start:stop])
            counts = symbols_in(body, all_names)
            declarations.append(
                Declaration(
                    module=source.module,
                    path=source.path,
                    line=start + 1,
                    kind=kind,
                    name=name,
                    symbols=tuple(sorted(counts)),
                    clusters=clusters_for(counts),
                )
            )
    return declarations


def aggregate_files(files: Iterable[SourceFile]) -> dict[str, object]:
    files = list(files)
    symbol_counts: Counter[str] = Counter()
    cluster_counts: Counter[str] = Counter()
    import_edges = 0
    for source in files:
        symbol_counts.update(source.symbol_counts)
        cluster_counts.update(source.clusters)
        import_edges += len(source.imports)
    return {
        "files": len(files),
        "lines": sum(source.lines for source in files),
        "bytes": sum(source.bytes for source in files),
        "import_edges": import_edges,
        "symbol_occurrences": dict(sorted(symbol_counts.items())),
        "files_by_cluster": dict(sorted(cluster_counts.items())),
    }


def declaration_rows(declarations: Iterable[Declaration], allowed: set[str] | None = None) -> list[dict[str, object]]:
    rows = []
    for declaration in declarations:
        if allowed is not None and declaration.module not in allowed:
            continue
        rows.append(
            {
                "module": declaration.module,
                "path": declaration.path,
                "line": declaration.line,
                "kind": declaration.kind,
                "name": declaration.name,
                "symbols": list(declaration.symbols),
                "clusters": list(declaration.clusters),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument(
        "--source-root",
        type=Path,
        help="Root containing Lean source. Defaults to the whole repository, excluding .lake/.git.",
    )
    parser.add_argument(
        "--root",
        action="append",
        dest="roots",
        default=["NavierStokes.R3.Theorem", "NavierStokes.ActualCandidateAssembly"],
        help="Local Lean module root; repeat for additional endpoint roots.",
    )
    parser.add_argument("--json", type=Path)
    parser.add_argument("--markdown", type=Path)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    source_root = (args.source_root or repo_root).resolve()
    files, module_paths = read_sources(repo_root, source_root)
    by_module = {source.module: source for source in files}
    reachable, missing_local, external_imports = local_closure(by_module, tuple(args.roots))
    declarations = declarations_for(repo_root, files)
    active_declarations = [decl for decl in declarations if decl.module in reachable]

    moment_names = set(CLUSTERS["moment"] + CLUSTERS["debt"])
    endpoint_names = set(CLUSTERS["endpoint"] + CLUSTERS["field"] + CLUSTERS["rates"])
    bridge_candidates = [
        decl
        for decl in declarations
        if moment_names.intersection(decl.symbols)
        and endpoint_names.intersection(decl.symbols)
    ]
    active_bridge_candidates = [decl for decl in bridge_candidates if decl.module in reachable]

    all_stats = aggregate_files(files)
    active_stats = aggregate_files(by_module[module] for module in sorted(reachable))
    decl_cluster_counts: Counter[str] = Counter()
    for declaration in active_declarations:
        decl_cluster_counts.update(declaration.clusters)

    result = {
        "instrument": "selected_endpoint_source_census",
        "status": "source census only; no surrogate field calculation",
        "repo_root": repo_root.as_posix(),
        "source_root": source_root.as_posix(),
        "roots": list(args.roots),
        "tree": all_stats,
        "local_import_closure": {
            "reachable_modules": len(reachable),
            "missing_local_imports": sorted(missing_local),
            "external_import_roots": sorted(external_imports),
            "active": active_stats,
        },
        "declarations": {
            "all": len(declarations),
            "active": len(active_declarations),
            "active_by_cluster": dict(sorted(decl_cluster_counts.items())),
        },
        "bridge_candidate_counts": {
            "all_source_declarations": len(bridge_candidates),
            "active_closure_declarations": len(active_bridge_candidates),
        },
        "bridge_candidates": declaration_rows(active_bridge_candidates),
        "active_declarations": declaration_rows(active_declarations),
        "module_index": [
            {
                "module": source.module,
                "path": source.path,
                "lines": source.lines,
                "bytes": source.bytes,
                "imports": list(source.imports),
                "symbol_counts": source.symbol_counts,
                "clusters": list(source.clusters),
                "reachable": source.module in reachable,
            }
            for source in files
        ],
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(encoded)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(encoded, encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        report_date = date.today().isoformat()
        rows = [
            f"# Selected-endpoint source census ({report_date})",
            "",
            "This report is generated from every current Lean file under `NavierStokes/`.",
            "It is lexical source evidence for audit triage, not a proof of theorem transport.",
            "No surrogate profile, numerical field, cutoff, or radial integral is used.",
            "",
            f"- Full source files: **{all_stats['files']}**",
            f"- Full source lines: **{all_stats['lines']}**",
            f"- Full source bytes: **{all_stats['bytes']}**",
            f"- Local modules reachable from the two endpoint roots: **{len(reachable)}**",
            f"- Active source lines: **{active_stats['lines']}**",
            f"- Missing local imports in the closure: **{len(missing_local)}**",
            f"- External import roots not present in this repository: **{len(external_imports)}**",
            f"- Parsed declarations: **{len(declarations)}** total, **{len(active_declarations)}** active",
            f"- Lexical moment/endpoint declaration candidates: **{len(active_bridge_candidates)}** active",
            "",
            "## Active lexical bridge candidates",
            "",
            "These rows identify declaration blocks containing both a moment/debt symbol and an endpoint/field/rate symbol. They are triage targets, not transport proofs.",
            "",
            "| File | Line | Declaration | Symbols |",
            "| --- | ---: | --- | --- |",
        ]
        for row in declaration_rows(active_bridge_candidates):
            symbols = ", ".join(row["symbols"])
            rows.append(f"| `{row['path']}` | {row['line']} | `{row['name']}` | `{symbols}` |")
        rows.extend(
            [
                "",
                "## Interpretation boundary",
                "",
                "A lexical co-occurrence is not a theorem-level equality. The selected-field transport question remains open until the exact declaration body proves the composition through sums, curl, localisation, periodisation, radial averaging, and the axis route.",
                "",
            ]
        )
        args.markdown.write_text("\n".join(rows), encoding="utf-8")


if __name__ == "__main__":
    main()
