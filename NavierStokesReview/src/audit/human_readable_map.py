"""Generate a human-readable architecture map and compact module atlas.

The exhaustive repository_map JSON remains the machine evidence layer. This
script produces the reading layer: a short architecture document, a compact
one-row-per-module atlas, a layered DOT graph, a compact LaTeX rendering, and a
compressed full declaration graph for exact-type review.
It only reports facts already present in the source/environment map.
"""

from __future__ import annotations

import argparse
import gzip
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--map", required=True, type=Path)
    p.add_argument("--routes", required=True, type=Path)
    p.add_argument("--architecture", required=True, type=Path)
    p.add_argument("--atlas", required=True, type=Path)
    p.add_argument("--dot", required=True, type=Path)
    p.add_argument("--tex", required=True, type=Path)
    p.add_argument("--repo", required=True, type=Path)
    p.add_argument("--explanations", required=True, type=Path)
    p.add_argument("--html", required=True, type=Path)
    p.add_argument("--claims", required=True, type=Path)
    p.add_argument("--declaration-index", required=True, type=Path)
    p.add_argument("--audit-graph", required=True, type=Path)
    p.add_argument("--mathematical-spec", required=True, type=Path)
    return p.parse_args()


def group_for(path: str) -> str:
    if path.startswith("NavierStokesReview/"):
        return "NavierStokesReview"
    if path.startswith("NavierStokes/"):
        return "NavierStokes"
    if path.startswith("Euler/"):
        return "Euler"
    if path.startswith("ComparatorChallenges/"):
        return "ComparatorChallenges"
    return "Root wrappers"


GROUP_DESCRIPTIONS = {
    "NavierStokes": "Author source for the construction, correction, moment, pressure, periodic, and R3 machinery. The module rows below report declarations and imports directly; the description is an inventory label, not an inferred theorem interpretation.",
    "Euler": "Author source for the companion Euler branch and its supporting construction modules.",
    "NavierStokesReview": "Review-side audit scripts, probes, environment exports, and supporting formal checks. These files are not part of the author endpoint unless the compiled status says so.",
    "ComparatorChallenges": "Standalone comparator/challenge declarations. They are recorded for repository completeness and are outside the selected endpoint closure in this run.",
    "Root wrappers": "Lean files at the source root, including root-level wrappers and entry points.",
}


def load_routes(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| Target |"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            break
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0]:
            rows.append({"target": cells[0], "reachable": cells[1], "span": cells[2], "edges": cells[3]})
    return rows


def short_symbols(module: dict) -> str:
    names = [d["short_name"] for d in module.get("declarations", [])]
    if not names:
        return "—"
    return ", ".join(names[:5]) + (", …" if len(names) > 5 else "")


def status_label(module: dict) -> str:
    return "selected closure" if module["compiled_status"] == "joined_to_selected_endpoint" else "not captured at endpoint"


ROLE_RULES = [
    (("ProblemStatement",), "formal candidate/admissibility specification"),
    (("Theorem",), "endpoint theorem or theorem packaging"),
    (("Candidate", "Assembly", "Construction", "Witness"), "candidate construction and export layer"),
    (("R3", "WholeSpace", "CompactCandidate"), "whole-space or R³ realisation and packaging"),
    (("Pressure", "PressureStream", "PressureRecovery", "PressureFlux", "Riesz"), "pressure, elliptic recovery, or pressure transport"),
    (("Energy", "Viscous", "Dissipation", "CompactEnergy", "L2"), "energy, dissipation, or finite-energy estimates"),
    (("Residual", "Jet", "Limit", "Boundary"), "residual, endpoint-limit, jet, or boundary regularity"),
    (("Moment", "Rank", "Debt", "Correction", "Repair", "Mean", "Gauge"), "finite-dimensional moment, rank, debt, or correction control"),
    (("Potential", "Wave", "Pulse", "Germ", "Profile"), "potential, wave, pulse, germ, or profile construction"),
    (("Periodic", "Period", "Localization", "Localized", "Cutoff", "Support", "Activation"), "localisation, cutoff, support, or periodisation"),
    (("Coordinate", "Chart", "Cyl", "Radial", "Axis", "Spatial", "Temporal", "Time"), "coordinate, geometric, spatial, or temporal interface"),
    (("Smooth", "ContDiff", "Regularity", "Bounds", "Estimate", "Norm", "Sobolev", "Decay", "Integrability"), "analytic regularity, bounds, decay, or integrability"),
]


def role_summary(module: dict) -> str:
    haystack = module["module"] + " " + " ".join(d["short_name"] for d in module.get("declarations", []))
    hits = []
    for tokens, description in ROLE_RULES:
        if any(token.lower() in haystack.lower() for token in tokens):
            hits.append(description)
    if not hits:
        return "support module identified by its declared names"
    unique = list(dict.fromkeys(hits))
    if len(unique) == 1:
        return unique[0]
    return "; ".join(unique[:3])


REVIEW_LENSES = [
    (("ProblemStatement", "Theorem"), "Check the exported predicate, domains, quantifiers, and endpoint conclusions against the CMI statement. Do not infer requirements from upstream module names."),
    (("Candidate", "Assembly", "Construction", "Witness"), "Trace which concrete fields enter the exported witness and which upstream invariants are actually present in its type."),
    (("Moment", "Rank", "Debt", "Correction", "Repair", "Mean", "Gauge"), "Check whether moment or debt identities are identities of correction data only, or are transported to the assembled Cartesian fields."),
    (("Pressure", "Riesz", "Poisson", "Flux"), "Check whether the source proves an absolute pressure/Poisson or Leray identity, rather than only a comparison, support, or flux statement."),
    (("Energy", "Viscous", "Dissipation", "CompactEnergy", "L2"), "Check the exact spatial domain, time interval, integrability hypotheses, and whether the estimate is a candidate consequence or a global theorem."),
    (("Residual", "Jet", "Limit", "Boundary", "Force"), "Check how the residual is defined, which endpoint filters are non-vacuous, and whether force regularity is derived or supplied as a premise."),
    (("Periodic", "Period", "Localization", "Localized", "Cutoff", "Support", "Activation"), "Check product-rule commutators, support boundaries, periodisation, and whether local identities survive assembly."),
    (("Coordinate", "Chart", "Cyl", "Radial", "Axis", "Spatial", "Temporal", "Time"), "Check chart domains and excluded axes, then locate the theorem transporting off-chart formulas to the global field."),
    (("Potential", "Wave", "Pulse", "Germ", "Profile", "Stage"), "Check stage matching, summation or limit operations, and whether local smoothness estimates control the final assembled field."),
]


def review_lens(module: dict) -> str:
    haystack = module["module"] + " " + module["path"] + " " + " ".join(d["short_name"] for d in module.get("declarations", []))
    for tokens, lens in REVIEW_LENSES:
        if any(token.lower() in haystack.lower() for token in tokens):
            return lens
    return "Read the declarations and imports to determine the mathematical object; then check which hypotheses are exported to downstream modules."


def connection_summary(module: dict, reverse: dict[str, list[str]]) -> str:
    """Give a non-Lean reader a bounded explanation of the module's place.

    This is deliberately structural: it describes the module's declared role,
    incoming imports, downstream users, and named entry points without claiming
    that names alone establish a mathematical theorem.
    """
    imports = module.get("resolved_imports", [])
    dependents = reverse.get(module["module"], [])
    declarations = [d["short_name"] for d in module.get("declarations", [])]
    entry_points = ", ".join(f"`{name}`" for name in declarations[:4]) or "no parsed declarations"
    family = group_for(module["path"])
    return (
        f"This {family} module is catalogued as {role_summary(module)}. "
        f"It receives {len(imports)} resolved project imports and is used by "
        f"{len(dependents)} other mapped modules. Its first named entry points are {entry_points}. "
        "Use those declarations and the import path to determine the mathematical role; this summary is not a substitute for their hypotheses."
    )


def focus_symbols(module: dict, limit: int = 10) -> str:
    names = [d["short_name"] for d in module.get("declarations", [])]
    if not names:
        return "No declarations were recorded in the source map."
    return ", ".join(f"`{name}`" for name in names[:limit]) + (", …" if len(names) > limit else "")


def source_sections(module: dict, repo: Path) -> str:
    source = repo / module["path"]
    if not source.exists():
        return "not available in the checked source path"
    try:
        text = source.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "source could not be read during map generation"
    names = re.findall(r"(?m)^\s*(?:section|namespace)\s+([^\s{]+)", text)
    names = list(dict.fromkeys(names))[:5]
    return ", ".join(f"`{name}`" for name in names) if names else "no top-level section/namespace marker recorded"


def reverse_imports(modules: list[dict]) -> dict[str, list[str]]:
    reverse: dict[str, list[str]] = defaultdict(list)
    known = {m["module"] for m in modules}
    for module in modules:
        for imported in module.get("resolved_imports", []):
            if imported in known:
                reverse[imported].append(module["module"])
    for values in reverse.values():
        values.sort()
    return reverse


def declaration_rows(modules: list[dict]) -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    for module in modules:
        for declaration in module.get("declarations", []):
            rows.append({
                "name": declaration["name"],
                "short_name": declaration["short_name"],
                "kind": declaration["kind"],
                "module": module["module"],
                "path": module["path"],
                "line": declaration["line"],
                "end_line": declaration.get("end_line", declaration["line"]),
                "status": module["compiled_status"],
            })
    rows.sort(key=lambda row: str(row["name"]))
    return rows


def latex_type(name: str, formal_type: str | None) -> str:
    """Translate only syntax that is unambiguous in the captured metadata.

    The source/environment join does not expose every elaborated type. Missing
    types are therefore marked as unavailable rather than reconstructed from a
    declaration name.
    """
    if not formal_type:
        return r"\text{formal type not captured in this audit export}"
    value = formal_type
    replacements = [
        (r"EuclideanSpace ℝ (Fin 3)", r"\mathbb{R}^3"),
        (r"Fin 3 → ℝ", r"\mathbb{R}^3"),
        (r"Fin 5 → ℝ", r"\mathbb{R}^5"),
        ("NavierStokesResidual", r"\mathcal{R}_{NS}"),
        ("VelocityField", r"u(t,x)"),
        ("PressureField", r"p(t,x)"),
        ("CandidateProperties", r"\mathsf{CandidateProperties}"),
        ("GlobalFiniteEnergySolution", r"\mathsf{GlobalFiniteEnergySolution}"),
        ("Iff", r"\Longleftrightarrow"),
        ("→", r"\to"),
    ]
    for source, target in replacements:
        value = value.replace(source, target)
    return value


def audit_status_for(name: str, claims: list[dict]) -> str:
    """Attach only statuses supported by the review claim register."""
    names: dict[str, set[str]] = defaultdict(set)
    for claim in claims:
        required_names = claim.get("required_names", []) or claim.get("required_source_names", [])
        for required in required_names:
            names[required].add(claim["id"])
    ids = names.get(name, set())
    if "CTR-005" in ids:
        return "CORRESPONDENCE_GAP"
    if "CTR-012" in ids:
        return "PROVENANCE_CONDITIONED"
    if "CTR-032" in ids:
        return "VERIFIED_STANDARD_AXIOM_SCOPE"
    if "MAP-001" in ids:
        return "VERIFIED_ROUTE_ONLY"
    return "NOT_CLASSIFIED"


def write_audit_graph(path: Path, data: dict, claims: list[dict]) -> None:
    """Write a synchronized module/declaration graph with explicit gaps.

    Source declarations are the primary nodes. Environment declarations are
    joined by fully-qualified name where possible; unmatched environment nodes
    are retained as compiled-only nodes so the audit cannot silently discard
    elaborated dependencies.
    """
    modules = data["modules"]
    source_rows = declaration_rows(modules)
    source_by_name = {str(row["name"]): row for row in source_rows}
    module_by_name = {m["module"]: m for m in modules}
    environment_path = path.parent / "lean_environment_closure_2026-09-26.json"
    joined_path = path.parent / "joined_environment_source_map_2026-09-26.json"
    environment = json.loads(environment_path.read_text(encoding="utf-8")) if environment_path.exists() else {"nodes": [], "edges": []}
    joined = json.loads(joined_path.read_text(encoding="utf-8")) if joined_path.exists() else {"nodes": []}
    env_by_name = {node.get("name"): node for node in environment.get("nodes", []) if node.get("name")}
    joined_by_name = {node.get("name"): node for node in joined.get("nodes", []) if node.get("name")}
    exact_type_names = {
        "NavierStokesR3.theorem_1_1",
        "NavierStokesR3.theorem_1_1_with_initial_rest",
        "NavierStokes.ActualCandidateAssembly.selected_witness",
        "NavierStokesR3.ProblemStatement.CandidateProperties",
        "NavierStokes.FiveRowRank.FiveRows",
        "NavierStokes.PositiveOrderMoments.Debt",
        "NavierStokes.MeanRankUpdate.scaleDebt",
        "NavierStokes.DefectIncrementBounds.barMoment",
    }

    def compact_type(name: str, formal: str | None) -> tuple[str | None, str | None]:
        if not formal:
            return None, None
        if name in exact_type_names:
            return formal, latex_type(name, formal)
        return None, None

    nodes: list[dict] = []
    full_nodes: list[dict] = []
    for row in source_rows:
        name = str(row["name"])
        env = joined_by_name.get(name) or env_by_name.get(name)
        module = module_by_name.get(str(row["module"]), {})
        formal = env.get("type") if env else None
        contains_sorry = bool(module.get("source_flags", {}).get("sorry_token")) or bool(env and env.get("usesSorryAx"))
        compact_formal, compact_latex = compact_type(name, formal)
        metadata_gaps = ["docstring_not_captured"]
        if not formal:
            metadata_gaps.append("elaborated_type_not_captured")
        elif compact_formal is None:
            metadata_gaps.append("elaborated_type_omitted_from_compact_graph")
        full_node = {
            "id": name,
            "name": name,
            "node_kind": "source_declaration",
            "node_level": "declaration",
            "file_path": str(row["path"]),
            "line_range": [int(row["line"]), int(row["end_line"])],
            "kind": str(row["kind"]),
            "formal_type_lean": formal,
            "mathematical_type_latex": latex_type(name, formal) if formal else None,
            "axiom_footprint": ["sorryAx"] if env and env.get("usesSorryAx") else [],
            "contains_sorry": contains_sorry,
            "is_active_export_path": module.get("compiled_status") == "joined_to_selected_endpoint",
            "audit_status": audit_status_for(name, claims),
            "docstring": None,
            "metadata_gaps": [gap for gap in metadata_gaps if gap != "elaborated_type_omitted_from_compact_graph"],
        }
        full_nodes.append(full_node)
        compact_node = dict(full_node)
        compact_node["formal_type_lean"] = compact_formal
        compact_node["mathematical_type_latex"] = compact_latex
        compact_node["metadata_gaps"] = metadata_gaps
        nodes.append(compact_node)
    known_names = {str(row["name"]) for row in source_rows}
    for name, env in sorted(env_by_name.items()):
        if name in known_names:
            continue
        source = env.get("source") or {}
        compact_formal, compact_latex = compact_type(name, env.get("type"))
        metadata_gaps = ["source_declaration_not_joined", "docstring_not_captured"]
        if compact_formal is None and env.get("type"):
            metadata_gaps.append("elaborated_type_omitted_from_compact_graph")
        full_node = {
            "id": name,
            "name": name,
            "node_kind": "compiled_environment_declaration",
            "node_level": "compiled_declaration",
            "file_path": source.get("path"),
            "line_range": [source.get("line"), source.get("end_line")],
            "kind": source.get("kind"),
            "formal_type_lean": env.get("type"),
            "mathematical_type_latex": latex_type(name, env.get("type")) if env.get("type") else None,
            "axiom_footprint": ["sorryAx"] if env.get("usesSorryAx") else [],
            "contains_sorry": bool(env.get("usesSorryAx")),
            "is_active_export_path": name == environment.get("root") or bool(source),
            "audit_status": "COMPILED_ONLY_NOT_SOURCE_JOINED",
            "docstring": None,
            "metadata_gaps": [gap for gap in metadata_gaps if gap != "elaborated_type_omitted_from_compact_graph"],
        }
        full_nodes.append(full_node)
        compact_node = dict(full_node)
        compact_node["formal_type_lean"] = compact_formal
        compact_node["mathematical_type_latex"] = compact_latex
        compact_node["metadata_gaps"] = metadata_gaps
        nodes.append(compact_node)
    edges = []
    for edge in environment.get("edges", []):
        source = edge.get("from")
        target = edge.get("to")
        if source and target:
            source_file = (joined_by_name.get(source) or env_by_name.get(source) or {}).get("source", {}).get("path")
            target_file = (joined_by_name.get(target) or env_by_name.get(target) or {}).get("source", {}).get("path")
            edges.append({
                "source": source,
                "target": target,
                "dependency_type": "COMPILED_DECLARATION_USE",
                "is_across_file_boundary": bool(source_file and target_file and source_file != target_file),
            })
    for module in modules:
        for imported in module.get("resolved_imports", []):
            edges.append({
                "source": module["module"],
                "target": imported,
                "dependency_type": "MODULE_IMPORT",
                "is_across_file_boundary": True,
            })
    edge_counts = {}
    for edge in edges:
        edge_counts[edge["dependency_type"]] = edge_counts.get(edge["dependency_type"], 0) + 1
    source_with_types = sum(1 for row in source_rows if (joined_by_name.get(row["name"]) or env_by_name.get(row["name"])) and (joined_by_name.get(row["name"]) or env_by_name.get(row["name"])).get("type"))
    source_without_types = len(source_rows) - source_with_types
    compiled_without_source = len(nodes) - len(source_rows)
    typed_compiled_nodes = sum(1 for node in full_nodes if node.get("node_kind") == "compiled_environment_declaration" and node.get("formal_type_lean"))
    dependency_taxonomy = {
        "MODULE_IMPORT": {"available": True, "count": edge_counts.get("MODULE_IMPORT", 0), "meaning": "resolved source-module import"},
        "COMPILED_DECLARATION_USE": {"available": True, "count": edge_counts.get("COMPILED_DECLARATION_USE", 0), "meaning": "captured elaborated-environment use; call/type/coercion/instance origin is not retained"},
        "DIRECT_CALL": {"available": False, "count": 0, "meaning": "not inferable from the captured environment edge record"},
        "TYPE_DEPENDENCY": {"available": False, "count": 0, "meaning": "not inferable from the captured environment edge record"},
        "IMPLICIT_COERCION": {"available": False, "count": 0, "meaning": "not inferable from the captured environment edge record"},
        "INSTANCE_MATCH": {"available": False, "count": 0, "meaning": "not inferable from the captured environment edge record"},
    }
    payload = {
        "schema": "repository_audit_graph.v2",
        "repository_metadata": {
            "target_repo": str(data.get("root", "")),
            "source_map": "NavierStokesReview/evidence/repository_map_2026-09-26.json",
            "environment_map": "NavierStokesReview/evidence/lean_environment_closure_2026-09-26.json",
            "joined_source_map": "NavierStokesReview/evidence/joined_environment_source_map_2026-09-26.json",
            "root_endpoints": [environment.get("root", "NavierStokesR3.theorem_1_1")],
            "counts": {
                "source_nodes": len(source_rows),
                "compiled_environment_nodes": len(env_by_name),
                "compiled_only_nodes": len(nodes) - len(source_rows),
                "joined_nodes_with_types": sum(1 for row in source_rows if row["name"] in joined_by_name),
                "source_nodes_with_exact_types": source_with_types,
                "source_nodes_without_exact_types": source_without_types,
                "typed_compiled_nodes": typed_compiled_nodes,
                "typed_nodes_total": sum(1 for node in full_nodes if node.get("formal_type_lean")),
                "compiled_nodes_without_source_join": compiled_without_source,
                "docstrings_captured": 0,
                "edges": len(edges),
                "edge_counts": edge_counts,
            },
        },
        "audit_contract": {
            "source_of_truth": "captured source/environment maps",
            "unavailable_fields_are_null": True,
            "name_based_translation_is_not_proof": True,
            "endpoint_axiom_scope": "Use endpoint evidence for standard axioms; declaration nodes only record sorryAx when exported.",
            "compact_type_scope": "Exact elaborated types are retained for the selected review declarations; the complete environment export remains the regeneration input.",
            "dependency_taxonomy": dependency_taxonomy,
            "edge_semantics_boundary": "Only module imports and generic compiled declaration-use edges were captured. The four finer-grained edge categories remain unavailable rather than guessed.",
        },
        "nodes": nodes,
        "edges": edges,
        "claims": claims,
    }
    path.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")
    full_payload = dict(payload)
    full_payload["schema"] = "repository_audit_graph.v2.full"
    full_payload["audit_contract"] = dict(payload["audit_contract"])
    full_payload["audit_contract"]["compact_type_scope"] = "This compressed companion retains every captured elaborated environment type and its generated notation; the ordinary graph is the reader-oriented compact view."
    full_payload["nodes"] = full_nodes
    full_path = path.with_name(path.stem + "_full.json.gz")
    with gzip.open(full_path, "wt", encoding="utf-8", newline="\n") as stream:
        json.dump(full_payload, stream, separators=(",", ":"), ensure_ascii=False)
        stream.write("\n")


def write_mathematical_spec(path: Path, data: dict, claims: list[dict], routes: list[dict[str, str]]) -> None:
    counts = data["counts"]
    modules = data["modules"]
    source_rows = declaration_rows(modules)
    by_name = {str(row["name"]): row for row in source_rows}
    selected = [row for row in source_rows if by_name.get(str(row["name"]), {}).get("status") == "joined_to_selected_endpoint"]
    env_path = path.parent.parent / "NavierStokesReview" / "evidence" / "joined_environment_source_map_2026-09-26.json"
    env = json.loads(env_path.read_text(encoding="utf-8")) if env_path.exists() else {"nodes": []}
    env_by_name = {n.get("name"): n for n in env.get("nodes", [])}
    exact_type_joins = sum(1 for row in source_rows if row["name"] in env_by_name and env_by_name[row["name"]].get("type"))
    compiled_only = len(env.get("unmatched", []))
    audit_graph_path = path.parent.parent / "NavierStokesReview" / "evidence" / "repository_audit_graph_2026-09-26.json"
    audit_graph = json.loads(audit_graph_path.read_text(encoding="utf-8")) if audit_graph_path.exists() else {}
    audit_counts = audit_graph.get("repository_metadata", {}).get("counts", {})
    source_with_types = audit_counts.get("source_nodes_with_exact_types", exact_type_joins)
    full_graph_edges = audit_counts.get("edges", "unavailable")
    full_graph_typed_nodes = audit_counts.get("typed_nodes_total", "unavailable")
    generic_use_edges = audit_counts.get("edge_counts", {}).get("COMPILED_DECLARATION_USE", "unavailable")
    module_import_edges = audit_counts.get("edge_counts", {}).get("MODULE_IMPORT", "unavailable")
    focus = [
        "NavierStokesR3.theorem_1_1", "NavierStokesR3.theorem_1_1_with_initial_rest",
        "NavierStokes.ActualCandidateAssembly.selected_witness", "NavierStokesR3.ProblemStatement.CandidateProperties",
        "NavierStokes.FiveRowRank.FiveRows", "NavierStokes.PositiveOrderMoments.Debt",
        "NavierStokes.MeanRankUpdate.scaleDebt", "NavierStokes.DefectIncrementBounds.barMoment",
    ]
    out = [
        "# Mathematical specification and audit navigation",
        "",
        "> This is a reading layer over the captured Lean source and environment maps. It translates only metadata that was actually extracted. It is not a replacement proof and it does not infer a theorem from a filename.",
        "",
        "## How to use this document",
        "",
        "1. Start with the endpoint route below.",
        "2. Read the plain-language layer description before opening Lean.",
        "3. Follow the linked source spans and the interactive map for imports and users.",
        "4. Treat every `UNAVAILABLE` or `NOT_CLASSIFIED` marker as an audit task, not as evidence of failure.",
        "",
        "## Formal objects in ordinary notation",
        "",
        "| Lean object or pattern | Reader notation | Status of translation |",
        "|---|---|---|",
        r"| `Fin 3 → ℝ` | \(\mathbb{R}^3\) | syntax-level translation |",
        r"| `Fin 5 → ℝ` | \(\mathbb{R}^5\) | syntax-level translation |",
        r"| `VelocityField` | a time-space vector field \(u(t,x)\) | only when the captured type confirms it |",
        r"| `PressureField` | a scalar field \(p(t,x)\) | only when the captured type confirms it |",
        r"| `navierStokesResidual` | \(\mathcal{R}_{NS}(u,p)\) | notation aid; inspect the source definition for its exact terms |",
        "| `FiveRows` / `Debt` / `barMoment` | finite-dimensional correction or moment data | names do not prove field-level transport |",
        "",
        "## Endpoint route",
        "",
        """```text
source inventory → Lean source declarations → compiled environment
                         ↓ exact-name join
                 selected_witness → CandidateProperties
                         ↓
                 theorem_1_1 / theorem_1_1_with_initial_rest
```""",
        "",
        "The graph distinguishes structural reachability from semantic identity. In particular, a reachable moment declaration does not by itself establish an equation of the form",
        "",
        r"\[\mathsf{Moment}_{\mathrm{paper}}(u,p)=\mathsf{Debt}_{\mathrm{runtime}}.\]",
        "",
        "That equality is the field-level transport obligation tracked by CTR-005.",
        "",
        "| Route target | Source span | Reachability |",
        "|---|---|---|",
    ]
    for row in routes:
        out.append(f"| `{row['target']}` | `{row['span']}` | {row['reachable']} |")
    out += ["", "## Review lanes", "", "| Lane | Mathematical question | Evidence boundary |", "|---|---|---|",
        "| CTR-005 | Do the five named paper moments reach the selected Cartesian fields after correction, localisation, curl, periodisation, summation, and R³ packaging? | `CORRESPONDENCE_GAP` means the selected-path transport theorem is not in the captured endpoint contract; it is not a kernel contradiction. |",
        "| CTR-012 | Is the force treated as a prescribed datum, or is its provenance residual-defined? | A residual provenance trace is a provenance concern; it does not alone negate an existential formal statement. |",
        "| Pressure | Is there an absolute global Poisson/Leray identity, or only comparison/support/flux facts? | Read exact pressure declarations and hypotheses. |",
        "| Energy | What domain and interval do the energy estimates cover? | Do not infer a global statement from a candidate consequence name. |",
        "| Axis/chart | Do off-axis chart identities transport to the on-axis route? | Record the excluded domain and the separate endpoint theorem. |",
        "| Axiom hygiene | Does the selected endpoint use `sorryAx`? What is the repository-wide source count? | Keep endpoint dependency scope separate from repository metadata. |",
        "",
        "## Selected declaration index",
        "",
        "The rows below are the declarations most relevant to the current review register. The complete machine dataset retains every source declaration and every compiled edge.",
        "The table is deliberately reader-facing: long elaborated Lean terms are not useful as prose. Each exact captured type remains available in the interactive map and in `repository_audit_graph_2026-09-26_full.json.gz`; the ordinary JSON is the compact query graph.",
        "",
        "| Declaration | What it does in the construction | Captured type | Source | Status |",
        "|---|---|---|---|---|",
    ]
    roles = {
        "NavierStokesR3.theorem_1_1": "Exported R³ breakdown proposition. This is the endpoint whose dependency scope must be checked against the CMI statement.",
        "NavierStokesR3.theorem_1_1_with_initial_rest": "Existential R³ candidate package with the initial-rest and endpoint consequences shown in its formal type.",
        "NavierStokes.ActualCandidateAssembly.selected_witness": "Concrete witness bundle consumed by the candidate theorem. Follow its fields before interpreting the public existential result.",
        "NavierStokesR3.ProblemStatement.CandidateProperties": "Admissibility predicate for velocity, pressure, force, support, regularity, divergence, residual, energy, and blow-up conditions.",
        "NavierStokes.FiveRowRank.FiveRows": "Finite correction-row predicate. It constrains the correction object; it is not automatically a theorem about the assembled Cartesian velocity field.",
        "NavierStokes.PositiveOrderMoments.Debt": "Upstream finite-dimensional moment/debt type used by the positive-order repair branch.",
        "NavierStokes.MeanRankUpdate.scaleDebt": "Runtime transformation that rescales or updates a debt vector between correction stages.",
        "NavierStokes.DefectIncrementBounds.barMoment": "Scalar/radial moment operator at the correction interface. Its domain and relation to the final Cartesian field require source-level inspection.",
    }

    def captured_type_summary(name: str, typ: str | None) -> str:
        if not typ:
            return "UNAVAILABLE: elaborated type not captured"
        if len(typ) > 240:
            return "captured; full elaborated type in the audit graph"
        return typ

    for name in focus:
        row = by_name.get(name)
        if not row:
            out.append(f"| `{name}` | `UNAVAILABLE: no exact source declaration match` | `UNAVAILABLE` | — | `NOT_FOUND_IN_SOURCE_MAP` |")
            continue
        typ = env_by_name.get(name, {}).get("type")
        src = f"[`{row['path']}:{row['line']}-{row['end_line']}`](../{row['path']})"
        role = roles.get(name, "No reader-facing role has been classified; inspect the source span and exact graph node.")
        out.append(f"| `{name}` | {role} | `{md_escape(captured_type_summary(name, typ))}` | {src} | `{audit_status_for(name, claims)}` |")
    out += ["", "## Coverage and limitations", "", f"The source map contains **{counts['mapped_modules']} modules**, **{counts['source_declarations']} source declarations**, **{counts['compiled_nodes']} compiled environment declarations**, and **{counts['compiled_edges']} source-located joined edges**. Exact source joins: **{counts['exact_source_matches']}**. Reachable `sorryAx` users at the selected endpoint: **{counts['reachable_sorryAx_users']}**.", "", f"The full audit graph is a separate, wider view: it contains the joined source declarations, **{compiled_only} compiled-only declarations**, **{full_graph_typed_nodes} typed graph nodes**, and **{full_graph_edges} edges** consisting of **{generic_use_edges} generic compiled-use edges** plus **{module_import_edges} module-import edges**. These totals are not interchangeable with the source-located joined-edge count above.", "", "### Coverage matrix", "", "| Audit layer | Captured result | What a mathematician may conclude |", "|---|---:|---|", f"| Source modules | {counts['mapped_modules']} | Every indexed Lean module has a source path, import list, flags, and declaration inventory. |", f"| Source declarations | {counts['source_declarations']} | Every declaration found by the source parser is searchable and linked to a source span. |", f"| Exact source/environment joins | {exact_type_joins} | These names have an exact source/environment match; this is not a claim that their theorem meanings have been transported. |", f"| Source declarations with captured types | {source_with_types} | These source declarations have captured elaborated types; the remainder are explicit type-coverage gaps. |", f"| Compiled-only declarations with captured types | {compiled_only} | These environment declarations have no joined current-source declaration in this capture. |", f"| Total typed graph nodes | {full_graph_typed_nodes} | This is the source-plus-compiled typed population in the full graph, not the number of mathematical propositions proved. |", f"| Source declarations without captured types | {counts['source_declarations'] - source_with_types} | No type should be inferred from a name, role label, or import edge. |", "| Declaration docstrings | 0 captured | Reader descriptions are navigation aids, not source-authored theorem explanations. |", "| Fine-grained call/type/coercion/instance edges | not captured | Generic compiled-use edges are shown; the four finer categories are deliberately not guessed. |", "", "The source map does not capture declaration docstrings or every elaborated type. Those fields remain explicit `null` in the JSON graph. A human-readable translation therefore distinguishes syntax-level notation, exact environment types, and unresolved semantic obligations. The repository review should not convert any of these metadata gaps into a claim about mathematical invalidity without a declaration-level theorem or counterexample.", "", "Companions: [interactive architecture map](REPOSITORY_ARCHITECTURE_MAP.html), [module explanations](LEAN_MODULE_EXPLANATIONS.md), [declaration index](LEAN_DECLARATION_INDEX.md), [review method](REVIEW_MAPPING_METHOD.md), [raw graph](../NavierStokesReview/evidence/repository_audit_graph_2026-09-26.json), and [full exact-type graph](../NavierStokesReview/evidence/repository_audit_graph_2026-09-26_full.json.gz).", ""]
    path.write_text("\n".join(out), encoding="utf-8")


def write_declaration_index(path: Path, modules: list[dict]) -> None:
    rows = declaration_rows(modules)
    out = [
        "# Lean declaration index",
        "",
        "This index maps every source declaration recorded by the source parser to its module, kind, and source span. It is the declaration-level companion to the module architecture map.",
        "",
        f"Coverage: **{len(rows)} declarations** across **{len(modules)} modules**.",
        "",
        "| Declaration | Kind | Module | Source span | Endpoint status |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        source = f"[{row['path']}:{row['line']}-{row['end_line']}](../{row['path']})"
        status = "selected closure" if row["status"] == "joined_to_selected_endpoint" else "not captured at endpoint"
        out.append(f"| `{row['name']}` | `{row['kind']}` | `{row['module']}` | {source} | {status} |")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def load_claims(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("claims", [])


def route_excerpt(row: dict[str, str], repo: Path) -> str:
    span = row.get("span", "")
    match = re.match(r"(.+):(\d+)(?:-(\d+))?$", span)
    if not match:
        return "source span could not be parsed"
    source_path, start, end = match.group(1), int(match.group(2)), int(match.group(3) or match.group(2))
    source = repo / source_path
    if not source.exists():
        return "source file not found in the checked repository"
    try:
        lines = source.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return "source file could not be read"
    start = max(1, start)
    end = min(len(lines), end)
    excerpt = lines[start - 1:end]
    numbered = "\n".join(
        f"{line_no:>5} |{(' ' + line.rstrip()) if line.rstrip() else ''}"
        for line_no, line in enumerate(excerpt, start=start)
    )
    return numbered[:12000]


def module_anchor(module_name: str) -> str:
    return "module-" + re.sub(r"[^a-z0-9]+", "-", module_name.lower()).strip("-")


def module_links(names: list[str], total: int, limit: int = 8) -> str:
    if not names:
        return "none recorded in the source import graph"
    shown = names[:limit]
    result = ", ".join(f"[`{name}`](LEAN_MODULE_EXPLANATIONS.md#{module_anchor(name)})" for name in shown)
    if total > limit:
        result += f"; and {total - limit} more"
    return result


def html_module_links(names: list[str], total: int, limit: int = 12) -> str:
    """Render bounded, clickable module-neighbour links for the HTML map."""
    if not names:
        return "<span class='muted'>none recorded in the source import graph</span>"
    shown = names[:limit]
    result = ", ".join(
        f"<a href='#{module_anchor(name)}'><code>{html.escape(name)}</code></a>"
        for name in shown
    )
    if total > limit:
        result += f"; <span class='muted'>{total - limit} more not shown</span>"
    return result


def write_explanations(path: Path, data: dict, repo: Path) -> None:
    modules = sorted(data["modules"], key=lambda m: m["module"])
    reverse = reverse_imports(modules)
    groups = module_rows(modules)
    counts = data["counts"]
    out: list[str] = [
        "# Lean module explanations",
        "",
        "This is the human reading layer for the Lean source tree. It answers four questions for every file: what role the file appears to play, what named objects it declares, what it imports, and which modules use it.",
        "",
        "## How to read an entry",
        "",
        "- **Exact source facts** are the path, declaration names, imports, reverse dependents, line count, source flags, and compiled-closure status.",
        "- **Role** is a navigation summary inferred transparently from the filename and declaration vocabulary. It is not a substitute for reading a theorem body.",
        "- **Used by** is a reverse import relation. It shows architectural dependency, not mathematical implication.",
        "- **Endpoint status** says whether the module was joined to the compiled environment captured from `NavierStokesR3.theorem_1_1`.",
        "",
        f"Coverage: **{counts['mapped_modules']} modules**, **{counts['source_declarations']} source declarations**, **{counts['exact_source_matches']} exact source joins**.",
        "",
    ]
    for group, group_modules in groups.items():
        out += [f"## {group}", "", GROUP_DESCRIPTIONS[group], ""]
        for module in group_modules:
            name = module["module"]
            dependents = reverse.get(name, [])
            imports = module.get("resolved_imports", [])
            flags = [key for key, value in module.get("source_flags", {}).items() if value]
            out += [
                f"### `{name}` {{#{module_anchor(name)}}}",
                "",
                f"**File:** `{module['path']}` ({module['line_count']} lines)",
                f"**Plain-language role:** {role_summary(module)}.",
                f"**How it connects:** {connection_summary(module, reverse)}",
                f"**Reviewer lens:** {review_lens(module)}",
                f"**Objects declared here:** {focus_symbols(module)}",
                f"**Source sections/namespaces:** {source_sections(module, repo)}.",
                f"**Inputs:** {module_links(imports, len(imports))}.",
                f"**Used by:** {module_links(dependents, len(dependents))}.",
                f"**Proof-route status:** `{status_label(module)}`.",
                f"**Source flags:** {', '.join(f'`{flag}`' for flag in flags) if flags else 'none recorded'}.",
                "**Interpretation boundary:** The dependency and declaration facts are machine-extracted. The role sentence is a labelled navigation aid; any claim about the mathematical theorem represented by this file must be checked against its source declarations and proof terms.",
                "",
            ]
    path.write_text("\n".join(out), encoding="utf-8")


def html_module_card(module: dict, reverse: dict[str, list[str]], repo: Path) -> str:
    name = module["module"]
    imports = module.get("resolved_imports", [])
    dependents = reverse.get(name, [])
    flags = [key for key, value in module.get("source_flags", {}).items() if value]
    source_url = "../" + module["path"].replace("\\", "/")
    all_symbols = " ".join(d["short_name"] for d in module.get("declarations", []))
    symbols = ", ".join(module["declarations"][i]["short_name"] for i in range(min(8, len(module.get("declarations", []))))) or "none recorded"
    return f'''<article id="{module_anchor(name)}" class="module-card" data-family="{html.escape(group_for(module["path"]))}" data-status="{html.escape(module["compiled_status"])}" data-search="{html.escape((name + " " + module["path"] + " " + role_summary(module) + " " + all_symbols).lower())}">
  <details>
    <summary><code>{html.escape(name)}</code> <span class="badge">{html.escape(group_for(module["path"]))}</span> <span class="badge">{html.escape(status_label(module))}</span></summary>
    <div class="card-body">
      <p><strong>File:</strong> <a href="{html.escape(source_url)}"><code>{html.escape(module["path"])}</code></a> ({module["line_count"]} lines)</p>
      <p><strong>Role:</strong> {html.escape(role_summary(module))}. <span class="boundary">Navigation summary inferred from the filename and declaration vocabulary.</span></p>
      <p><strong>How it connects:</strong> {html.escape(connection_summary(module, reverse))}</p>
      <p><strong>Reviewer lens:</strong> {html.escape(review_lens(module))}</p>
      <p><strong>Declared objects:</strong> <code>{html.escape(symbols)}</code></p>
      <p><strong>Source sections/namespaces:</strong> <code>{html.escape(source_sections(module, repo))}</code></p>
      <p><strong>Imports:</strong> {html_module_links(imports, len(imports))}</p>
      <p><strong>Used by:</strong> {html_module_links(dependents, len(dependents))}</p>
      <p><strong>Source flags:</strong> {html.escape(", ".join(flags) or "none recorded")}. <strong>Endpoint:</strong> {html.escape(status_label(module))}.</p>
      <p class="boundary"><strong>Review boundary:</strong> imports and declarations establish architecture, not theorem validity. Read the linked source before treating the role as a mathematical claim.</p>
    </div>
  </details>
</article>'''


def write_html(path: Path, data: dict, routes: list[dict[str, str]], repo: Path) -> None:
    modules = sorted(data["modules"], key=lambda m: m["module"])
    reverse = reverse_imports(modules)
    counts = data["counts"]
    families = sorted({group_for(m["path"]) for m in modules})
    route_cards = "".join(
        f'<li><code>{html.escape(row["target"])}</code> <span>{html.escape(row["span"])}</span> <em>{html.escape(row["reachable"])}</em></li>'
        for row in routes
    )
    cards = "\n".join(html_module_card(m, reverse, repo) for m in modules)
    family_options = "".join(f'<option value="{html.escape(family)}">{html.escape(family)}</option>' for family in families)
    html_text = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Navier–Stokes repository architecture map</title>
<style>
:root {{ color-scheme: light; --ink:#202735; --muted:#5e6878; --line:#d9dee8; --panel:#fff; --blue:#174a7a; --cream:#fff8e8; --rose:#fff0f4; --green:#eaf7ed; }}
* {{ box-sizing:border-box; }} body {{ margin:0; background:#f4f6f9; color:var(--ink); font:15px/1.55 system-ui,-apple-system,Segoe UI,sans-serif; }}
header {{ padding:28px clamp(18px,4vw,64px); background:linear-gradient(135deg,#102d4d,#23689b); color:white; }} header h1 {{ margin:0 0 8px; font-size:clamp(25px,4vw,42px); }} header p {{ max-width:1000px; margin:0; color:#e4f0fb; }}
main {{ max-width:1500px; margin:0 auto; padding:24px clamp(16px,3vw,48px) 80px; }} section {{ background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:20px; margin:18px 0; box-shadow:0 2px 8px #13233d0b; }}
h2 {{ margin-top:0; color:var(--blue); }} h3 {{ color:var(--blue); }} code {{ font-family:ui-monospace,SFMono-Regular,Consolas,monospace; font-size:.92em; }}
.flow {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:9px; align-items:stretch; margin:16px 0; }} .node {{ padding:14px 10px; border:1px solid #a9c2db; border-radius:10px; background:#eff6fd; text-align:center; font-weight:650; }} .arrow {{ display:none; }}
.controls {{ position:sticky; top:0; z-index:2; background:#fffffff2; backdrop-filter:blur(8px); display:flex; gap:10px; flex-wrap:wrap; align-items:center; border:1px solid var(--line); padding:12px; border-radius:10px; }} input,select,button {{ padding:10px 12px; border:1px solid #bcc7d5; border-radius:7px; background:white; color:var(--ink); }} input {{ flex:1; min-width:260px; }} button {{ cursor:pointer; }}
.stats {{ display:flex; gap:10px; flex-wrap:wrap; margin:12px 0; }} .stat {{ background:#eef3f8; border-radius:8px; padding:9px 12px; }} .stat strong {{ display:block; font-size:20px; color:var(--blue); }}
.module-card {{ border-bottom:1px solid var(--line); padding:5px 0; }} .module-card[hidden] {{ display:none; }} summary {{ cursor:pointer; padding:10px 4px; }} summary code {{ color:#123e68; }} .badge {{ display:inline-block; font-size:12px; border:1px solid #c5cfdb; border-radius:999px; padding:2px 7px; margin-left:6px; color:var(--muted); background:#f7f9fb; }} .card-body {{ padding:3px 14px 13px; }} .card-body p {{ margin:7px 0; }} .boundary {{ color:var(--muted); font-size:.94em; }}
.routes li {{ padding:6px 0; }} .routes em {{ color:#287a39; }} .note {{ background:var(--cream); border-left:4px solid #d99b2b; padding:12px 15px; }} .gap {{ background:var(--rose); border-left:4px solid #c95873; padding:12px 15px; }} a {{ color:#125b99; }} footer {{ color:var(--muted); font-size:13px; margin-top:28px; }}
</style></head>
<body><header><h1>Navier–Stokes repository architecture map</h1><p>Human-readable navigation for the Lean source tree. Start with the route, then search for any module. Every card separates exact source facts from a labelled navigation summary.</p></header>
<main>
<section><h2>How the construction is organised</h2><p>The source is a layered construction, not a single proof file. The arrows below describe the dependency route that a reviewer must follow from the formal problem statement to the exported theorem.</p>
<div class="flow"><div class="node">Problem statement<br><small>what the endpoint requires</small></div><div class="node">Candidate assembly<br><small>base, germs, stages</small></div><div class="node">Moments and repairs<br><small>debt, rank, corrections</small></div><div class="node">Local / periodic fields<br><small>cutoffs, velocity, pressure</small></div><div class="node">R³ packaging<br><small>energy, decay, residual</small></div><div class="node">Exported theorem<br><small><code>theorem_1_1</code></small></div></div>
<div class="note"><strong>Central review question:</strong> structural reachability shows that modules are connected. It does not by itself prove that a quantity defined in the moment or correction layer is equal to the corresponding quantity of the final Cartesian field after curl, localisation, periodisation, summation, and R³ packaging.</div></section>
<section><h2>Selected endpoint route</h2><p>The route evidence is source-coordinate based. Open the source file from a card when a theorem meaning matters.</p><ul class="routes">{route_cards}</ul></section>
<section><h2>Coverage</h2><div class="stats"><div class="stat"><strong>{counts["mapped_modules"]}</strong>Lean modules mapped</div><div class="stat"><strong>{counts["source_declarations"]}</strong>source declarations</div><div class="stat"><strong>{counts["exact_source_matches"]}</strong>exact source joins</div><div class="stat"><strong>{counts["reachable_sorryAx_users"]}</strong>reachable <code>sorryAx</code> users</div></div><p>Endpoint status refers to the captured environment for <code>NavierStokesR3.theorem_1_1</code>; it is not a repository-wide claim about every file.</p></section>
<section><h2>Search the complete module atlas</h2><div class="controls"><input id="search" placeholder="Search module, file, role, or declaration…"><select id="family"><option value="">All families</option>{family_options}</select><select id="status"><option value="">All endpoint statuses</option><option value="joined_to_selected_endpoint">Selected endpoint closure</option><option value="not_in_selected_endpoint_environment">Not captured at endpoint</option></select><button id="openAll">Open visible cards</button><button id="closeAll">Close cards</button></div><p id="resultCount"></p><div id="cards">{cards}</div></section>
<section><h2>Interpretation rules</h2><div class="gap"><strong>Do not read the role sentence as a proof.</strong> Imports, declarations, source flags, and endpoint joins are exact inventory facts. The plain-language role is generated from transparent filename/declaration vocabulary so that a non-Lean reader can navigate the tree. Mathematical conclusions require checking the linked source theorem and its hypotheses.</div><p>Use the Markdown architecture map for a printable explanation, the module-explanation file for a searchable text archive, the DOT file for graph tools, and the raw JSON for exact machine evidence.</p></section>
<footer>Generated from the repository source/environment map. Source links are relative to the repository root. This page is an audit navigation layer, not part of the author proof.</footer>
</main>
<script>
const cards=[...document.querySelectorAll('.module-card')], search=document.querySelector('#search'), family=document.querySelector('#family'), status=document.querySelector('#status'), count=document.querySelector('#resultCount');
function filter(){{const q=search.value.toLowerCase().trim(), f=family.value, s=status.value; let n=0; cards.forEach(c=>{{const ok=(!q||c.dataset.search.includes(q))&&(!f||c.dataset.family===f)&&(!s||c.dataset.status===s); c.hidden=!ok; if(ok)n++;}}); count.textContent=n+' of '+cards.length+' modules shown';}}
search.addEventListener('input',filter); family.addEventListener('change',filter); status.addEventListener('change',filter); document.querySelector('#openAll').onclick=()=>cards.filter(c=>!c.hidden).forEach(c=>c.querySelector('details').open=true); document.querySelector('#closeAll').onclick=()=>cards.forEach(c=>c.querySelector('details').open=false); filter();
</script></body></html>'''
    path.write_text(html_text, encoding="utf-8")


def write_html_v2(path: Path, data: dict, routes: list[dict[str, str]], repo: Path, claims: list[dict]) -> None:
    """Write the interactive review surface used by human readers.

    The page is deliberately offline and data-driven. It exposes the same
    source/environment facts as the JSON map, but adds declaration search,
    claim evidence, source excerpts, and directed import-path queries.
    """
    modules = sorted(data["modules"], key=lambda m: m["module"])
    reverse = reverse_imports(modules)
    counts = data["counts"]
    families = sorted({group_for(m["path"]) for m in modules})
    declarations = declaration_rows(modules)
    known = {m["module"] for m in modules}
    graph = {
        m["module"]: [x for x in m.get("resolved_imports", []) if x in known]
        for m in modules
    }
    route_rows = []
    for row in routes:
        excerpt = route_excerpt(row, repo)
        route_rows.append(
            "<details class='route-card'><summary><code>"
            + html.escape(row["target"])
            + "</code> <span>"
            + html.escape(row["span"])
            + "</span> <em>"
            + html.escape(row["reachable"])
            + "</em></summary><div class='route-body'><pre>"
            + html.escape(excerpt)
            + "</pre></div></details>"
        )
    claim_rows = []
    for claim in claims:
        evidence = "".join(f"<li><code>{html.escape(x)}</code></li>" for x in claim.get("evidence", []))
        required = "".join(f"<li><code>{html.escape(x)}</code></li>" for x in claim.get("required_source_names", []))
        claim_rows.append(
            "<article class='claim-card'><div class='claim-head'><strong>"
            + html.escape(claim.get("id", ""))
            + "</strong><span class='badge'>"
            + html.escape(claim.get("status", ""))
            + "</span><span class='badge'>"
            + html.escape(claim.get("level", ""))
            + "</span></div><h3>"
            + html.escape(claim.get("title", ""))
            + "</h3><p>"
            + html.escape(claim.get("interpretation", ""))
            + "</p><div class='claim-columns'><div><b>Required declarations</b><ul>"
            + required
            + "</ul></div><div><b>Evidence files</b><ul>"
            + evidence
            + "</ul></div></div></article>"
        )
    cards = "\n".join(html_module_card(m, reverse, repo) for m in modules)
    family_options = "".join(f"<option value='{html.escape(f)}'>{html.escape(f)}</option>" for f in families)
    endpoint_module = next((m["module"] for m in modules if m["path"] == "NavierStokes/R3/Theorem.lean"), "NavierStokes.R3.Theorem")
    moment_module = next((m["module"] for m in modules if m["path"] == "NavierStokes/FiveRowRank.lean"), "NavierStokes.FiveRowRank")
    graph_json = json.dumps(graph, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    declaration_json = json.dumps(declarations, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html_text = """<!doctype html>
<html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Lean repository review map</title>
<style>
:root{--ink:#172333;--muted:#5a6876;--line:#d7e0e8;--blue:#135b91;--cream:#fff8e8;--rose:#fff0f2;--green:#e9f7ed;--panel:#f7f9fb}
*{box-sizing:border-box}body{margin:0;font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif;color:var(--ink);background:#f2f5f8}header{background:#102d48;color:#fff;padding:30px max(20px,calc((100% - 1400px)/2));}header h1{margin:0 0 5px;font-size:clamp(25px,4vw,42px)}header p{max-width:950px;margin:0;color:#dbe8f4}main{max-width:1400px;margin:auto;padding:18px}section{background:#fff;border:1px solid var(--line);border-radius:10px;padding:18px;margin:14px 0;box-shadow:0 2px 9px #19324a0d}h2{margin-top:0;color:#123e68}h3{margin:7px 0}.flow{display:flex;gap:7px;flex-wrap:wrap;align-items:stretch}.node{flex:1 1 150px;min-width:130px;background:#eaf2f9;border:1px solid #b8cee0;border-radius:8px;padding:11px;text-align:center;color:#123e68}.node small{color:var(--muted)}.note,.gap{padding:12px 15px;border-left:4px solid #d99b2b;background:var(--cream)}.gap{border-left-color:#c95873;background:var(--rose)}.stats{display:flex;gap:10px;flex-wrap:wrap}.stat{background:var(--panel);padding:10px 14px;border-radius:8px}.stat strong{display:block;font-size:24px;color:var(--blue)}.controls{display:flex;gap:8px;flex-wrap:wrap;position:sticky;top:8px;z-index:2;background:#fffffff2;padding:10px;border:1px solid var(--line);border-radius:8px}.controls input,.controls select,.controls button{padding:9px 11px;border:1px solid #bdcad7;border-radius:6px;background:#fff}.controls input{flex:1;min-width:260px}.controls button{cursor:pointer}.module-card{border-bottom:1px solid var(--line)}.module-card[hidden]{display:none}.module-card summary,.route-card summary{cursor:pointer;padding:9px 3px}.module-card summary code,.route-card summary code{color:#123e68}.badge{display:inline-block;font-size:12px;border:1px solid #c5cfdb;border-radius:999px;padding:2px 7px;margin-left:5px;color:var(--muted);background:#f7f9fb}.card-body{padding:2px 14px 13px}.boundary{color:var(--muted);font-size:.93em}.route-card{border-bottom:1px solid var(--line)}.route-body{padding:10px}.route-body pre{overflow:auto;max-height:420px;background:#11202e;color:#e8f0f7;padding:12px;border-radius:7px;font:12px/1.45 ui-monospace,Consolas,monospace}.claim-card{border:1px solid var(--line);border-radius:8px;padding:13px;margin:10px 0;background:#fcfdff}.claim-head{display:flex;gap:6px;align-items:center}.claim-columns{display:grid;grid-template-columns:1fr 1fr;gap:18px}.claim-columns ul{margin-top:5px;padding-left:20px}.tool-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.tool-panel{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:13px}.tool-panel input,.tool-panel select,.tool-panel button{width:100%;margin:4px 0;padding:9px;border:1px solid #bdcad7;border-radius:6px;background:#fff}.tool-output{white-space:pre-wrap;max-height:380px;overflow:auto;background:#11202e;color:#e8f0f7;padding:11px;border-radius:6px;font:12px/1.45 ui-monospace,Consolas,monospace}a{color:#125b99}footer{color:var(--muted);font-size:13px;margin:25px 0}@media(max-width:760px){.claim-columns,.tool-grid{grid-template-columns:1fr}}
</style></head><body>
<header><h1>Lean repository review map</h1><p>Offline navigation for the source tree, the selected compiled route, and the review claims. Search declarations, inspect exact source spans, and test dependency paths without treating reachability as proof of semantic correctness.</p></header>
<main>
<section><h2>Read the construction as a chain</h2><div class='flow'><div class='node'>Problem statement<br><small>formal predicate</small></div><div class='node'>Candidate assembly<br><small>base, germs, stages</small></div><div class='node'>Moments and repairs<br><small>debt and rank</small></div><div class='node'>Local / periodic fields<br><small>curl, cutoffs, pressure</small></div><div class='node'>R³ packaging<br><small>energy and decay</small></div><div class='node'>Exported theorem<br><small>theorem_1_1</small></div></div><p class='note'><b>Review rule:</b> an import path proves architectural reachability. It does not prove that a moment, pressure identity, or physical interpretation survives every transformation into the exported field.</p></section>
 <section><h2>Coverage snapshot</h2><div class='stats'><div class='stat'><strong>__MODULES__</strong>Lean modules</div><div class='stat'><strong>__DECLARATIONS__</strong>source declarations</div><div class='stat'><strong>__EDGES__</strong>compiled edges</div><div class='stat'><strong>__JOINS__</strong>exact source joins</div><div class='stat'><strong>__SORRY__</strong>reachable sorryAx users</div></div><p>Endpoint status is scoped to the captured environment for <code>NavierStokesR3.theorem_1_1</code>. It is not a repository-wide zero-sorry assertion.</p><details><summary>What this map does and does not capture</summary><table><tr><th>Layer</th><th>Status</th><th>Reading rule</th></tr><tr><td>Source modules and declarations</td><td>Complete indexed inventory</td><td>Use source spans and imports to navigate.</td></tr><tr><td>Elaborated declaration types</td><td>Exact where environment data joined; otherwise explicit unavailable</td><td>Never infer a type from a name or role label.</td></tr><tr><td>Dependency semantics</td><td>Module imports and generic compiled-use edges</td><td>Direct calls, type dependencies, coercions, and instance matches were not captured and are not guessed.</td></tr><tr><td>Mathematical meaning</td><td>Reader-facing role labels only</td><td>Check the linked Lean declaration and hypotheses before making a PDE claim.</td></tr></table></details></section>
<section><h2>Review claims</h2><p>Each card states the claim level, required declarations, interpretation, and evidence paths. “Open” means the transport or provenance question remains unresolved, not that the Lean kernel has derived <code>False</code>.</p>__CLAIMS__</section>
<section><h2>Selected endpoint route</h2><p>Expand a target to see the exact source-coordinate excerpt used by the route report.</p>__ROUTES__</section>
<section><h2>Declaration finder</h2><p>This searches the complete source declaration index, not only the selected route. Select a result to open its source file at the recorded line.</p><div class='controls'><input id='declQuery' placeholder='Search declaration, module, file, or kind…'><select id='declStatus'><option value=''>All endpoint statuses</option><option value='joined_to_selected_endpoint'>Selected endpoint closure</option><option value='not_in_selected_endpoint_environment'>Not captured at endpoint</option></select></div><p id='declCount'></p><div id='declResults'></div></section>
<section><h2>Import-path finder</h2><p>Find a directed path through resolved project imports. This answers “how does module A reach module B?” Use module names, not declaration names. It does not claim that the path is a mathematical implication.</p><div class='tool-grid'><div class='tool-panel'><label>From module</label><input id='fromModule' list='moduleNames' placeholder='e.g. __ENDPOINT_MODULE__'><label>To module</label><input id='toModule' list='moduleNames' placeholder='e.g. __MOMENT_MODULE__'><button id='findPath'>Find shortest path</button><button id='useEndpointPath' type='button'>Load endpoint → moment example</button></div><div class='tool-panel'><div id='pathResult' class='tool-output'>No path query run.</div></div></div><datalist id='moduleNames'>__MODULE_OPTIONS__</datalist></section>
<section><h2>Complete module atlas</h2><div class='controls'><input id='moduleQuery' placeholder='Search module, path, role, or declaration…'><select id='family'><option value=''>All families</option>__FAMILIES__</select><select id='moduleStatus'><option value=''>All endpoint statuses</option><option value='joined_to_selected_endpoint'>Selected endpoint closure</option><option value='not_in_selected_endpoint_environment'>Not captured at endpoint</option></select><button id='openAll'>Open visible cards</button><button id='closeAll'>Close cards</button></div><p id='moduleCount'></p><div id='cards'>__CARDS__</div></section>
 <section><h2>Evidence boundary</h2><div class='gap'><b>Do not read generated role labels as theorem summaries.</b> Paths, imports, declarations, source spans, hashes, flags, and endpoint joins are inventory facts. Role labels are navigation aids. Mathematical conclusions require reading the linked declaration and its hypotheses.</div><p>Reading companions: <a href='MATHEMATICAL_SPECIFICATION.md'>mathematical specification</a>, <a href='REPOSITORY_ARCHITECTURE_MAP.md'>architecture map</a>, <a href='REPOSITORY_MODULE_ATLAS.md'>module atlas</a>, <a href='LEAN_MODULE_EXPLANATIONS.md'>module explanations</a>, and <a href='LEAN_DECLARATION_INDEX.md'>declaration index</a>. Machine graph: <a href='../NavierStokesReview/evidence/repository_audit_graph_2026-09-26.json'>compact audit graph JSON</a> · <a href='../NavierStokesReview/evidence/repository_audit_graph_2026-09-26_full.json.gz'>full exact-type graph (gzip)</a>.</p></section>
<footer>Generated offline from the repository source/environment map. This page is a review navigation layer, not part of the author proof.</footer>
</main>
<script>
const graph=__GRAPH__, declarations=__DECLARATIONS__;
const esc=s=>String(s).replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]));
function declarationFilter(){const q=document.querySelector('#declQuery').value.toLowerCase().trim(),s=document.querySelector('#declStatus').value;const rows=declarations.filter(r=>(!q||(r.name+' '+r.short_name+' '+r.module+' '+r.path+' '+r.kind).toLowerCase().includes(q))&&(!s||r.status===s));const out=rows.slice(0,250).map(r=>`<div class='claim-card'><a href='../${esc(r.path)}#L${r.line}'><code>${esc(r.name)}</code></a> <span class='badge'>${esc(r.kind)}</span><br><small>${esc(r.path)}:${r.line}-${r.end_line} · ${esc(r.status)}</small></div>`).join('');document.querySelector('#declResults').innerHTML=out||'<p>No declarations match.</p>';document.querySelector('#declCount').textContent=rows.length+' matching declarations'+(rows.length>250?' (showing first 250)':'');}
function findPath(){const from=document.querySelector('#fromModule').value.trim(),to=document.querySelector('#toModule').value.trim(),out=document.querySelector('#pathResult');if(!(from in graph)||!(to in graph)){out.textContent='One or both module names are not in the source graph.';return;}const queue=[from],prev={[from]:null};for(const current of queue){if(current===to)break;for(const next of graph[current]||[]){if(!(next in prev)){prev[next]=current;queue.push(next);}}}if(!(to in prev)){out.textContent='No directed import path found.';return;}const path=[];for(let x=to;x!==null;x=prev[x])path.push(x);path.reverse();out.innerHTML=path.map((name,i)=>`<a href='#module-${name.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')}'>${esc(name)}</a>${i<path.length-1?'\\n↓\\n':''}`).join('');}
document.querySelector('#useEndpointPath').onclick=()=>{document.querySelector('#fromModule').value='__ENDPOINT_MODULE__';document.querySelector('#toModule').value='__MOMENT_MODULE__';findPath();};
document.querySelector('#declQuery').addEventListener('input',declarationFilter);document.querySelector('#declStatus').addEventListener('change',declarationFilter);document.querySelector('#findPath').addEventListener('click',findPath);declarationFilter();
const cards=[...document.querySelectorAll('.module-card')],mq=document.querySelector('#moduleQuery'),fam=document.querySelector('#family'),ms=document.querySelector('#moduleStatus'),mc=document.querySelector('#moduleCount');function moduleFilter(){const q=mq.value.toLowerCase().trim(),f=fam.value,s=ms.value;let n=0;cards.forEach(c=>{const ok=(!q||c.dataset.search.includes(q))&&(!f||c.dataset.family===f)&&(!s||c.dataset.status===s);c.hidden=!ok;if(ok)n++;});mc.textContent=n+' of '+cards.length+' modules shown';}mq.addEventListener('input',moduleFilter);fam.addEventListener('change',moduleFilter);ms.addEventListener('change',moduleFilter);document.querySelector('#openAll').onclick=()=>cards.filter(c=>!c.hidden).forEach(c=>c.querySelector('details').open=true);document.querySelector('#closeAll').onclick=()=>cards.forEach(c=>c.querySelector('details').open=false);moduleFilter();
</script></body></html>"""
    replacements = {
        "__CLAIMS__": "\n".join(claim_rows),
        "__ROUTES__": "\n".join(route_rows),
        "__MODULE_OPTIONS__": "".join(f"<option value='{html.escape(m['module'])}'>" for m in modules),
        "__FAMILIES__": family_options,
        "__CARDS__": cards,
        "__GRAPH__": graph_json,
        "__ENDPOINT_MODULE__": html.escape(endpoint_module),
        "__MOMENT_MODULE__": html.escape(moment_module),
    }
    html_text = html_text.replace("const graph=__GRAPH__, declarations=__DECLARATIONS__;", "const graph=" + graph_json + ", declarations=" + declaration_json + ";")
    html_text = html_text.replace("__MODULES__", str(counts["mapped_modules"]))
    html_text = html_text.replace("__DECLARATIONS__", str(counts["source_declarations"]), 1)
    html_text = html_text.replace("__EDGES__", str(counts["compiled_edges"]))
    html_text = html_text.replace("__JOINS__", str(counts["exact_source_matches"]))
    html_text = html_text.replace("__SORRY__", str(counts["reachable_sorryAx_users"]))
    for key in ("__CLAIMS__", "__ROUTES__", "__MODULE_OPTIONS__", "__FAMILIES__", "__CARDS__", "__ENDPOINT_MODULE__", "__MOMENT_MODULE__"):
        html_text = html_text.replace(key, replacements[key])
    path.write_text(html_text, encoding="utf-8")


def write_detailed_architecture(path: Path, data: dict, routes: list[dict[str, str]], atlas_name: str, explanations_name: str) -> None:
    counts = data["counts"]
    groups = module_rows(data["modules"])
    endpoint_modules = [m for m in data["modules"] if m["compiled_status"] == "joined_to_selected_endpoint"]
    out = [
        "# Human-readable repository architecture map",
        "",
        "> This is the map to read before opening Lean. It explains the mathematical flow, the software layers, and the exact place where each family connects. The exhaustive [module explanation cards](LEAN_MODULE_EXPLANATIONS.md) then give one entry for every file.",
        "",
        "## What is being mapped",
        "",
        "For the paper-to-code argument, start with",
        "[`SEMANTIC_CORRESPONDENCE_MAP.md`](SEMANTIC_CORRESPONDENCE_MAP.md). This",
        "architecture page supplies the broader module and dependency navigation;",
        "it is not a replacement for the claim-by-claim field correspondence",
        "analysis.",
        "",
        "The source tree is not one proof file. It is a layered construction. A typical path is:",
        "",
        "```text",
        "formal problem statement",
        "        ↓",
        "candidate construction and finite-stage data",
        "        ↓",
        "moment/debt repair and profile updates",
        "        ↓",
        "potential, wave, germ, and temporal assembly",
        "        ↓",
        "periodic/localised velocity, pressure, and residual fields",
        "        ↓",
        "whole-space R³ packaging and energy consequences",
        "        ↓",
        "exported existential theorem",
        "```",
        "",
        "The arrows mean that declarations/imports connect the layers. They do not, by themselves, prove that every informal interpretation survives the entire route.",
        "",
        "## Mathematical reading of the selected route",
        "",
        "### 1. Problem and endpoint layer",
        "",
        "`NavierStokes/R3/ProblemStatement.lean` defines the formal candidate predicate. `NavierStokes/R3/Theorem.lean` packages the selected candidate into the exported theorem `NavierStokesR3.theorem_1_1`. This is the final logical interface: a reviewer must first identify exactly what this predicate requires, rather than infer requirements from the paper narrative.",
        "",
        "### 2. Concrete candidate assembly",
        "",
        "`ActualCandidateAssembly.lean` is the construction junction. It names the initial, zeroth, particular, mean, signed, germ, and stage data, and exports `selected_witness`. Its imports are the incoming construction graph; its witness is the object consumed by the R³ theorem route.",
        "",
        "### 3. Germs, stages, and profiles",
        "",
        "The `Germ*`, `Stage*`, `Potential*`, `Wave*`, `Pulse*`, `Profile*`, and `Time*` families build the local pieces and control their smoothness, support, rates, and endpoint limits. These files explain how the candidate is assembled, but a declaration-level connection is still not the same thing as a field-level identity after infinite summation and localisation.",
        "",
        "### 4. Moment and correction layer",
        "",
        "`FiveRowRank.lean`, `PositiveOrderMoments.lean`, `FiveProfileMoments.lean`, `MeanRankUpdate.lean`, and `DefectIncrementBounds.lean` form the finite-dimensional correction branch. In plain terms, they define debt vectors, moment rows, profile corrections, and estimates used to repair selected quantities. The audit therefore records these modules as reachable, not dead. The unresolved question is stronger: where is the theorem that transports those named quantities into the final Cartesian field exported by `selected_witness`?",
        "",
        "### 5. Periodic and residual assembly",
        "",
        "`MixedPeriodicAssembly.lean` and related `Periodic*`, `Localized*`, `Cutoff*`, and `Support*` modules turn local or periodic pieces into assembled velocity, pressure, and residual objects. This is where support, cutoff, divergence, temporal activation, and residual identities meet. Any moment claim must survive these operations, not only hold for an isolated profile or correction increment.",
        "",
        "### 6. R³ and energy layer",
        "",
        "`R3CompactCandidate.lean`, `R3ActualCandidate.lean`, `R3CompactEnergy.lean`, `R3EnergyNorms.lean`, `R3EnergyBoundary.lean`, and the other `R3*` modules package whole-space regularity, compact support/decay, pressure, energy, and comparison statements. These modules are part of the author source and must be read as the final analytical interface, not as evidence that upstream informal quantities have automatically been preserved.",
        "",
        "### 7. What the current route proves and does not prove",
        "",
        "- The route proves structural reachability: the selected endpoint depends on the listed source modules in the captured environment.",
        "- The route does not by reachability alone prove value-level equality between the five named moment quantities and the final Cartesian velocity/pressure fields.",
        "- The route does not turn source names into physical meaning. The module cards mark inferred roles explicitly so that a human reviewer can verify each one against the source.",
        "- The endpoint `sorryAx` result is an endpoint dependency result, not a blanket claim about every standalone file in the repository.",
        "",
        "## Selected endpoint route with source coordinates",
        "",
        "| Target | Source span | Reachability |",
        "|---|---|---|",
    ]
    for row in routes:
        out.append(f"| `{row['target']}` | `{row['span']}` | {row['reachable']} |")
    out += [
        "",
        "## Key connection table",
        "",
        "| Layer | Representative files | Receives | Produces | Review question |",
        "|---|---|---|---|---|",
        "| Formal specification | `R3/ProblemStatement.lean`, `R3/Theorem.lean` | candidate fields and predicates | exported theorem package | What exactly is required by the formal predicate? |",
        "| Assembly | `ActualCandidateAssembly.lean`, `ActualCandidateConstruction.lean` | base, germ, stage, pressure, and exterior data | `selected_witness` and candidate fields | Which concrete fields enter the witness? |",
        "| Moments/corrections | `FiveRowRank.lean`, `PositiveOrderMoments.lean`, `MeanRankUpdate.lean` | profile/debt data | correction rows and update estimates | Are the named moments transported to the final field? |",
        "| Local/periodic fields | `MixedPeriodicAssembly.lean`, `PeriodicResidualLimits.lean` | local velocity, pressure, cutoffs | assembled velocity/residual limits | Are identities preserved across localisation and periodisation? |",
        "| R³ analysis | `R3CompactCandidate.lean`, `R3CompactEnergy.lean`, `R3Pressure*.lean` | assembled candidate and force | whole-space support, energy, pressure, comparison facts | Do these facts match the advertised whole-space problem? |",
        "| Review layer | `NavierStokesReview/src/audit/*` | source tree and Lean environment | maps, joins, claims, probes | Are source facts separated from semantic conclusions? |",
        "",
        "## Coverage and integrity",
        "",
        f"The map accounts for **{counts['mapped_modules']} / {counts['current_lean_modules']} Lean modules**, with **{counts['unaccounted_lean_modules']} unaccounted**. It records **{counts['source_declarations']} source declarations**, **{counts['compiled_nodes']} compiled nodes**, **{counts['exact_source_matches']} exact source joins**, and **{counts['reachable_sorryAx_users']} reachable `sorryAx` users** in the selected endpoint environment. The selected endpoint closure contains **{len(endpoint_modules)} source-joined modules**.",
        "",
        "## Reading order",
        "",
        "1. Read this page for the architecture and the unresolved transport question.",
        "2. Read the selected route evidence for exact declaration spans.",
        "3. Search `LEAN_MODULE_EXPLANATIONS.md` for any file name. Its card gives imports, dependents, declarations, flags, and endpoint status.",
        "4. Search `LEAN_DECLARATION_INDEX.md` when the question starts from a theorem, definition, or namespace rather than a file.",
        "5. Use `REPOSITORY_MODULE_ATLAS.md` for compact filtering and the raw JSON only for machine-level evidence.",
        "6. Open `REPOSITORY_ARCHITECTURE_MAP.html` for claim cards, source excerpts, declaration search, and import-path queries.",
        "7. Treat the role summaries as navigation, not as proof claims.",
        "",
        f"Companion files: [module cards]({explanations_name}), [declaration index](LEAN_DECLARATION_INDEX.md), [{atlas_name}]({atlas_name}), [interactive map](REPOSITORY_ARCHITECTURE_MAP.html), [selected route evidence](../NavierStokesReview/evidence/selected_endpoint_routes_2026-09-26.md), and `REPOSITORY_ARCHITECTURE_MAP.tex`.",
        "",
    ]
    path.write_text("\n".join(out), encoding="utf-8")


def module_rows(modules: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for module in modules:
        groups[group_for(module["path"])].append(module)
    for values in groups.values():
        values.sort(key=lambda m: m["module"])
    return dict(sorted(groups.items()))


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_atlas(path: Path, data: dict) -> None:
    groups = module_rows(data["modules"])
    counts = data["counts"]
    out: list[str] = [
        "# Complete Lean module atlas",
        "",
        "This is the exhaustive, compact index behind the architecture map. Each row is a source-backed inventory record; it is not a theorem summary.",
        "",
        f"Coverage: **{counts['mapped_modules']} / {counts['current_lean_modules']} Lean modules**. Unaccounted modules: **{counts['unaccounted_lean_modules']}**.",
        "",
        "Endpoint status means only whether the module was joined to the compiled environment captured from `NavierStokesR3.theorem_1_1`.",
        "",
    ]
    for group, modules in groups.items():
        out += [f"## {group} ({len(modules)} modules)", "", GROUP_DESCRIPTIONS[group], ""]
        out += ["| Module | Source | Declarations | Imports | Endpoint status | Declared symbols |", "|---|---|---:|---:|---|---|"]
        for m in modules:
            flags = []
            if m["source_flags"].get("sorry_token"):
                flags.append("source `sorry` token")
            if m["source_flags"].get("unsafe"):
                flags.append("unsafe")
            status = status_label(m)
            if flags:
                status += "; " + ", ".join(flags)
            out.append(
                f"| `{md_escape(m['module'])}` | `{m['path']}:{m['line_count']}` | {m['declaration_count']} | {m['resolved_import_count'] + m['external_import_count']} | {status} | `{md_escape(short_symbols(m))}` |"
            )
        out.append("")
    path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def write_architecture(path: Path, data: dict, routes: list[dict[str, str]], atlas_name: str) -> None:
    counts = data["counts"]
    groups = module_rows(data["modules"])
    endpoint_count = sum(m["compiled_status"] == "joined_to_selected_endpoint" for m in data["modules"])
    out = [
        "# Repository architecture map",
        "",
        "> Start here. This document explains the system. The exhaustive module list is in [the module atlas](REPOSITORY_MODULE_ATLAS.md); the raw declaration graph is evidence, not the reading view.",
        "",
        "## One-page orientation",
        "",
        "The repository has two distinct layers:",
        "",
        "1. **Author source** under `NavierStokes/`, `Euler/`, and the comparator files. This is the mathematical construction being audited.",
        "2. **Review tooling** under `NavierStokesReview/`. This parses source, exports Lean’s elaborated environment, joins declarations to source spans, and records claims without treating names as proofs.",
        "",
        "The selected endpoint is `NavierStokesR3.theorem_1_1`. The audit follows the route below and then checks which stronger semantic statements are actually exported.",
        "",
        "```mermaid",
        "flowchart LR",
        "  T[Hashed tree inventory] --> S[Live Lean source]",
        "  S --> C[Source declarations and imports]",
        "  S --> E[Lean compiled environment]",
        "  E --> J[Exact declaration-name join]",
        "  J --> W[selected_witness]",
        "  W --> A[ActualCandidateAssembly]",
        "  A --> R[Rank and moment machinery]",
        "  A --> P[Periodic and spatial assembly]",
        "  A --> Q[R3 candidate packaging]",
        "  R --> M[FiveRows / Debt / scaleDebt / barMoment]",
        "  P --> V[periodicVelocity]",
        "  Q --> H[CandidateProperties]",
        "  H --> X[theorem_1_1]",
        "  M -. missing value-level transport .-> X",
        "```",
        "",
        "## What the route establishes",
        "",
        "| Route component | What is established | What is not established by reachability |",
        "|---|---|---|",
        "| `selected_witness` | The selected construction is used by the endpoint. | That every upstream invariant has been transported to the exported field. |",
        "| `FiveRows`, both `Debt` types, `scaleDebt` | These declarations are reachable in the captured closure. | Equality of their values with the paper’s five Cartesian-field moments. |",
        "| `periodicVelocity` | The periodic assembly declaration is reachable. | That pre-periodised support and radial `barMoment` values are preserved after assembly. |",
        "| `CandidateProperties` | The endpoint packages the formal candidate predicate. | That the predicate carries every informal paper interpretation. |",
        "| `sorryAx` check | No reachable `sorryAx` users were found in the captured endpoint. | A repository-wide absence of `sorry` in every standalone file. |",
        "",
        "## Source families",
        "",
        "| Family | Modules | Reading purpose |",
        "|---|---:|---|",
    ]
    for group, modules in groups.items():
        out.append(f"| `{group}` | {len(modules)} | {GROUP_DESCRIPTIONS[group]} |")
    out += [
        "",
        "## Exact endpoint targets",
        "",
        "| Target | Source span | Reachability |",
        "|---|---|---|",
    ]
    for row in routes:
        out.append(f"| `{row['target']}` | `{row['span']}` | {row['reachable']} |")
    out += [
        "",
        "## How to use this map",
        "",
        "1. Begin with this page to understand the layers and the selected route.",
        "2. Open the exact target source span from the table.",
        "3. Use the module atlas to find every declaration and its imports without opening the raw graph.",
        "4. Use the JSON only when an exact hash, declaration list, or compiled edge is needed.",
        "5. Keep semantic conclusions separate from structural reachability. The live selected-field burden is CTR-005: the value-level transport of the five named moments through localisation, curl, periodisation, summation, and R3 packaging.",
        "",
        "## Map integrity",
        "",
        f"The current map validates **{counts['mapped_modules']} / {counts['current_lean_modules']} modules**, with **{counts['unaccounted_lean_modules']} unaccounted**, **{counts['source_declarations']} source declarations**, **{counts['compiled_nodes']} compiled nodes**, **{counts['exact_source_matches']} exact source joins**, and **{counts['reachable_sorryAx_users']} reachable `sorryAx` users**. `{endpoint_count}` modules have exact source joins in the selected endpoint closure.",
        "",
        f"Exhaustive atlas: [{atlas_name}]({atlas_name}). Raw evidence: `NavierStokesReview/evidence/repository_map_2026-09-26.json`.",
        "",
    ]
    path.write_text("\n".join(out), encoding="utf-8")


def write_dot(path: Path, routes: list[dict[str, str]]) -> None:
    nodes = {
        "tree": ("Inventory tree", "#e8f1ff"),
        "source": ("Live source", "#e8f1ff"),
        "parse": ("Source declarations\nand imports", "#eef7e8"),
        "env": ("Compiled Lean\nenvironment", "#eef7e8"),
        "join": ("Exact-name join", "#fff3d6"),
        "witness": ("ActualCandidateAssembly\nselected_witness", "#f8e1ed"),
        "rank": ("FiveRows / Debt /\nscaleDebt", "#f8e1ed"),
        "moments": ("PositiveOrderMoments\nand barMoment", "#f8e1ed"),
        "periodic": ("periodicVelocity", "#f8e1ed"),
        "r3": ("R3 candidate\npackaging", "#f8e1ed"),
        "endpoint": ("NavierStokesR3.\ntheorem_1_1", "#d8f0dc"),
        "gap": ("CTR-005 value-level\ntransport obligation", "#ffe0e0"),
    }
    edges = [
        ("tree", "source", "inventory -> contents"),
        ("source", "parse", "parse"),
        ("source", "env", "compile"),
        ("env", "join", "exact declarations"),
        ("join", "witness", "selected route"),
        ("witness", "rank", "rank route"),
        ("rank", "moments", "moment route"),
        ("witness", "periodic", "assembly route"),
        ("witness", "r3", "packaging route"),
        ("r3", "endpoint", "formal predicate"),
        ("moments", "gap", "reachability != value equality"),
        ("periodic", "gap", "support transport not inferred"),
        ("gap", "endpoint", "review burden"),
    ]
    out = ["digraph RepositoryArchitecture {", "  rankdir=LR;", "  graph [fontname=Helvetica, bgcolor=white];", "  node [shape=box, style=filled, fontname=Helvetica];", "  edge [fontname=Helvetica, color=\"#555555\"];" ]
    for key, (label, colour) in nodes.items():
        out.append(f'  {key} [label="{label}", fillcolor="{colour}"];')
    for left, right, label in edges:
        style = " [style=dashed]" if left == "gap" or right == "gap" else ""
        out.append(f'  {left} -> {right} [label="{label}"]{style};')
    out.append("}")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def tex_escape(value: str) -> str:
    return (value.replace("\\", "\\textbackslash{}")
            .replace("&", "\\&").replace("%", "\\%")
            .replace("_", "\\_").replace("#", "\\#")
            .replace("{", "\\{").replace("}", "\\}"))


def write_tex(path: Path, data: dict, routes: list[dict[str, str]]) -> None:
    counts = data["counts"]
    groups = module_rows(data["modules"])
    out = [
        r"\documentclass[10pt]{article}",
        r"\usepackage[margin=1.8cm]{geometry}",
        r"\usepackage{longtable,booktabs,hyperref,xcolor}",
        r"\title{Repository Architecture Map}",
        r"\author{Audit working document}",
        r"\begin{document}", r"\maketitle",
        r"\section*{Purpose}",
        r"This document is the readable architecture layer. The machine-readable JSON remains the exact evidence layer; this document does not infer theorem meaning from names.",
        r"\section*{Pipeline}",
        r"\[\text{tree inventory}\to\text{live source}\to\text{source declarations}\to\text{compiled environment}\to\text{exact-name join}\to\texttt{selected\_witness}\to\texttt{CandidateProperties}.\]",
        r"\section*{Endpoint targets}",
        r"\begin{longtable}{p{0.43\linewidth}p{0.32\linewidth}p{0.12\linewidth}}\toprule Target & Source span & Reachable\\\midrule",
    ]
    for row in routes:
        out.append(f"{tex_escape(row['target'])} & {tex_escape(row['span'])} & {tex_escape(row['reachable'])}\\\\")
    out += [r"\bottomrule\end{longtable}", r"\section*{Coverage}", f"The map accounts for {counts['mapped_modules']} of {counts['current_lean_modules']} Lean modules, with {counts['unaccounted_lean_modules']} unaccounted. It records {counts['source_declarations']} source declarations, {counts['compiled_nodes']} compiled nodes, {counts['exact_source_matches']} exact source joins, and {counts['reachable_sorryAx_users']} reachable \\texttt{{sorryAx}} users.", r"\section*{Compact module index}", r"\begin{longtable}{p{0.28\linewidth}p{0.27\linewidth}r r p{0.20\linewidth}}\toprule Module & Source & Decls. & Imports & Endpoint\\\midrule"]
    for group, modules in groups.items():
        for m in modules:
            status = "selected" if m["compiled_status"] == "joined_to_selected_endpoint" else "not captured"
            out.append(f"{tex_escape(m['module'])} & {tex_escape(m['path'])} & {m['declaration_count']} & {m['resolved_import_count'] + m['external_import_count']} & {status}\\\\")
    out += [r"\bottomrule\end{longtable}", r"\end{document}", ""]
    path.write_text("\n".join(out), encoding="utf-8")


def main() -> int:
    args = parse_args()
    data = json.loads(args.map.read_text(encoding="utf-8"))
    routes = load_routes(args.routes)
    write_atlas(args.atlas, data)
    write_explanations(args.explanations, data, args.repo)
    write_detailed_architecture(args.architecture, data, routes, args.atlas.name, args.explanations.name)
    claims = load_claims(args.claims)
    write_declaration_index(args.declaration_index, data["modules"])
    write_audit_graph(args.audit_graph, data, claims)
    write_mathematical_spec(args.mathematical_spec, data, claims, routes)
    write_html_v2(args.html, data, routes, args.repo, claims)
    write_dot(args.dot, routes)
    write_tex(args.tex, data, routes)
    print(json.dumps({"architecture": str(args.architecture), "atlas": str(args.atlas), "explanations": str(args.explanations), "declaration_index": str(args.declaration_index), "audit_graph": str(args.audit_graph), "mathematical_spec": str(args.mathematical_spec), "html": str(args.html), "modules": data["counts"]["mapped_modules"], "declarations": data["counts"]["source_declarations"], "claims": len(claims), "routes": len(routes)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
