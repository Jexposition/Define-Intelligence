#!/usr/bin/env python3
"""Generate the review-side repository map from the captured evidence layers.

This is deliberately a reporting tool, not a theorem-use oracle.  It joins:

* the authoritative extracted-tree hash;
* current source-module hashes and declarations;
* compiled-environment route paths;
* the explicit review claim register.

The JSON output contains one record for every mapped Lean module.  The Markdown
output is the compact human navigation layer.  A failed integrity check exits
non-zero instead of silently producing a stale map.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def route_membership(joined: dict[str, Any]) -> dict[str, set[str]]:
    membership: dict[str, set[str]] = defaultdict(set)
    for route_name, route in joined.get("routes", {}).items():
        for node in route.get("path", []):
            membership[node].add(route_name)
    return membership


def source_for_node(joined: dict[str, Any], name: str) -> dict[str, Any] | None:
    for node in joined.get("nodes", []):
        if node.get("name") == name:
            return node.get("source")
    return None


def validate_inputs(
    repo: Path, source_map: dict[str, Any], joined: dict[str, Any], tree: Path
) -> list[str]:
    failures: list[str] = []
    expected_tree_hash = source_map["inputs"]["tree_sha256"]
    actual_tree_hash = sha256(tree)
    if expected_tree_hash != actual_tree_hash:
        failures.append("authoritative tree hash differs from captured source map")

    drift = 0
    for record in source_map.get("modules", {}).values():
        path = repo / record["path"]
        if not path.is_file() or sha256(path) != record["sha256"]:
            drift += 1
    if drift:
        failures.append(f"{drift} mapped source module hashes changed")

    node_names = {node.get("name") for node in joined.get("nodes", [])}
    for route_name, route in joined.get("routes", {}).items():
        if not route.get("reachable"):
            failures.append(f"compiled route is not reachable: {route_name}")
        for node in route.get("path", []):
            if node not in node_names:
                failures.append(f"route node absent from environment: {node}")
    return failures


def build_map(
    repo: Path,
    source_map: dict[str, Any],
    joined: dict[str, Any],
    claims: dict[str, Any],
    tree: Path,
) -> dict[str, Any]:
    failures = validate_inputs(repo, source_map, joined, tree)
    membership = route_membership(joined)
    compiled_by_path: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in joined.get("nodes", []):
        source = node.get("source")
        if source and source.get("path"):
            compiled_by_path[source["path"]].append(
                {
                    "name": node.get("name"),
                    "type": node.get("type"),
                    "usesSorryAx": node.get("usesSorryAx", False),
                }
            )
    modules: list[dict[str, Any]] = []
    prefix_counts: Counter[str] = Counter()

    for module_name, record in sorted(source_map.get("modules", {}).items()):
        path = record["path"]
        parts = path.split("/")
        if parts[0] == "NavierStokes" and len(parts) == 2:
            prefix = "NavierStokes/root"
        elif parts[0] == "NavierStokes" and len(parts) >= 3:
            prefix = "/".join(parts[:2])
        else:
            prefix = parts[0]
        prefix_counts[prefix] += 1
        compiled_nodes = sorted(compiled_by_path.get(path, []), key=lambda node: node["name"])
        modules.append(
            {
                "module": module_name,
                "path": path,
                "sha256": record["sha256"],
                "line_count": record["line_count"],
                "imports": record["imports"],
                "resolved_imports": record["import_resolution"]["resolved"],
                "external_imports": record["import_resolution"]["external"],
                "missing_project_imports": record["import_resolution"]["missing_project"],
                "resolved_import_count": len(record["import_resolution"]["resolved"]),
                "external_import_count": len(record["import_resolution"]["external"]),
                "declaration_count": len(record["declarations"]),
                "declarations": record["declarations"],
                "symbol_hits": record["symbol_hits"],
                "source_flags": record["source_flags"],
                "compiled_status": "joined_to_selected_endpoint"
                if compiled_nodes
                else "not_in_selected_endpoint_environment",
                "compiled_declaration_count": len(compiled_nodes),
                "compiled_declarations": compiled_nodes,
                "compiled_route_membership": sorted(
                    route for node, routes in membership.items() if node.startswith(module_name + ".") for route in routes
                ),
            }
        )

    expected_modules = source_map["counts"]["current_lean_modules"]
    if len(modules) != expected_modules:
        failures.append(
            f"source map module count mismatch: mapped {len(modules)}, expected {expected_modules}"
        )

    route_ledger: list[dict[str, Any]] = []
    for name, route in sorted(joined.get("routes", {}).items()):
        path_rows = []
        for node in route.get("path", []):
            source = source_for_node(joined, node)
            path_rows.append(
                {
                    "name": node,
                    "source": source,
                    "usesSorryAx": next(
                        (item.get("usesSorryAx", False) for item in joined.get("nodes", []) if item.get("name") == node),
                        False,
                    ),
                }
            )
        route_ledger.append({"name": name, "reachable": route.get("reachable", False), "path": path_rows})

    return {
        "schema": "navier-stokes-review-repository-map/v1",
        "authority": {
            "tree": str(tree.resolve()),
            "tree_sha256": sha256(tree),
            "source_map_schema": source_map.get("schema"),
            "compiled_map_schema": joined.get("schema"),
            "claim_register_schema": claims.get("schema"),
        },
        "validation": {"passed": not failures, "failures": failures},
        "counts": {
            "mapped_modules": len(modules),
            "current_lean_modules": source_map["counts"]["current_lean_modules"],
            "unaccounted_lean_modules": source_map["counts"]["current_lean_modules"] - len(modules),
            "source_declarations": source_map["counts"]["declarations"],
            "compiled_nodes": joined["counts"]["environment_nodes"],
            "compiled_edges": joined["counts"]["joined_edges"],
            "exact_source_matches": joined["counts"]["exact_source_matches"],
            "unmatched_environment_nodes": joined["counts"]["unmatched_environment_nodes"],
            "ambiguous_source_matches": joined["counts"]["ambiguous_source_matches"],
            "reachable_sorryAx_users": joined["counts"]["joined_nodes_using_sorryAx"],
        },
        "prefix_counts": dict(sorted(prefix_counts.items())),
        "claims": claims.get("claims", []),
        "routes": route_ledger,
        "modules": modules,
    }


def markdown(mapping: dict[str, Any]) -> str:
    counts = mapping["counts"]
    validation = mapping["validation"]
    lines = [
        "# Repository map",
        "",
        "This map is generated from the authoritative tree-maker extract, current source hashes, and the compiled Lean environment.",
        "It is a navigation and evidence map; it does not infer mathematical correspondence from reachability.",
        "",
        "## Integrity",
        "",
        f"- Map validation: **{'passed' if validation['passed'] else 'failed'}**",
        f"- Authoritative tree: `{mapping['authority']['tree']}`",
        f"- Tree SHA-256: `{mapping['authority']['tree_sha256']}`",
        f"- Mapped Lean modules: `{counts['mapped_modules']}`",
        f"- Current Lean modules accounted for: `{counts['current_lean_modules'] - counts['unaccounted_lean_modules']}/{counts['current_lean_modules']}`",
        f"- Unaccounted Lean modules: `{counts['unaccounted_lean_modules']}`",
        f"- Source declarations: `{counts['source_declarations']}`",
        f"- Compiled environment nodes: `{counts['compiled_nodes']}`",
        f"- Compiled environment edges: `{counts['compiled_edges']}`",
        f"- Exact source joins: `{counts['exact_source_matches']}`",
        f"- Unmatched environment nodes: `{counts['unmatched_environment_nodes']}`",
        f"- Ambiguous source matches: `{counts['ambiguous_source_matches']}`",
        f"- Reachable `sorryAx` users: `{counts['reachable_sorryAx_users']}`",
        "",
        "## How to read the map",
        "",
        "1. **Tree layer:** confirms what the extracted repository inventory named at capture time.",
        "2. **Source layer:** confirms current paths, hashes, imports, declarations, and symbol locations.",
        "3. **Environment layer:** confirms declarations exported by the compiled Lean environment and exact route edges.",
        "4. **Claim layer:** records whether a review claim is supported, conditional, or still open.",
        "",
        "A route proves compiled reachability. It does not prove that an internal invariant is transported into the final field value.",
        "",
        "```mermaid",
        "flowchart LR",
        "  T[Authoritative tree snapshot] --> S[Current source hashes/imports/declarations]",
        "  S --> E[Compiled Lean environment]",
        "  E --> R[Exact endpoint routes]",
        "  R --> C[Claim register]",
        "  C --> V[Review conclusion with evidence boundary]",
        "```",
        "",
        "## Module census",
        "",
        "| Source area | Lean modules |",
        "|---|---:|",
    ]
    for prefix, count in mapping["prefix_counts"].items():
        lines.append(f"| `{prefix}` | `{count}` |")

    lines += ["", "## Selected endpoint routes", "", "| Route | Reachable | Nodes |", "|---|---:|---:|"]
    for route in mapping["routes"]:
        lines.append(f"| `{route['name']}` | `{route['reachable']}` | `{len(route['path'])}` |")

    lines += ["", "## Route ledger", ""]
    for route in mapping["routes"]:
        lines += [f"### `{route['name']}`", ""]
        for index, node in enumerate(route["path"]):
            source = node["source"]
            if source:
                location = f"{source['path']}:{source['line']}-{source['end_line']}"
            else:
                location = "unjoined source location"
            lines.append(f"{index + 1}. `{node['name']}` — `{location}`; `sorryAx={node['usesSorryAx']}`")
        lines.append("")

    lines += ["## Claim ledger", "", "| ID | Status | Evidence boundary |", "|---|---|---|"]
    for claim in mapping["claims"]:
        boundary = claim.get("evidence_boundary", claim.get("interpretation", "not specified"))
        lines.append(f"| `{claim['id']}` | `{claim['status']}` | {boundary} |")

    lines += [
        "",
        "## Complete module catalogue",
        "",
        "The JSON map retains the full import and declaration records. The compact catalogue below gives every mapped Lean module its source location, declaration/import counts, key-symbol hits, and route membership.",
        "",
        "| Module | Source | Declarations | Imports | Endpoint status | Route membership | Key symbols |",
        "|---|---|---:|---:|---|---|---|",
    ]
    for module in mapping["modules"]:
        routes = ", ".join(f"`{route}`" for route in module["compiled_route_membership"])
        symbols = ", ".join(f"`{name}`" for name in module["symbol_hits"])
        lines.append(f"| `{module['module']}` | `{module['path']}` | `{module['declaration_count']}` | `{len(module['imports'])}` | `{module['compiled_status']}` | {routes or '—'} | {symbols or '—'} |")

    lines += ["", "## Per-module evidence cards", ""]
    for module in mapping["modules"]:
        lines += [
            f"<details><summary><code>{module['module']}</code></summary>",
            "",
            f"- Source: `{module['path']}`",
            f"- SHA-256: `{module['sha256']}`",
            f"- Lines: `{module['line_count']}`",
            f"- Endpoint compilation status: `{module['compiled_status']}`",
            f"- Source flags: `{json.dumps(module['source_flags'], sort_keys=True)}`",
            f"- Imports: `{', '.join(module['imports']) or 'none'}`",
            f"- Resolved project imports: `{', '.join(module['resolved_imports']) or 'none'}`",
            f"- External imports: `{', '.join(module['external_imports']) or 'none'}`",
            f"- Missing project imports: `{', '.join(module['missing_project_imports']) or 'none'}`",
            f"- Endpoint-joined declarations: `{module['compiled_declaration_count']}`",
        ]
        if module["symbol_hits"]:
            lines.append(f"- Key symbol hits: `{json.dumps(module['symbol_hits'], sort_keys=True)}`")
        lines += ["", "Declarations:", ""]
        for declaration in module["declarations"]:
            lines.append(f"- `{declaration['kind']} {declaration['name']}` — lines `{declaration['line']}-{declaration['end_line']}`")
        if module["compiled_declarations"]:
            lines += ["", "Compiled declarations joined to the selected endpoint:", ""]
            for declaration in module["compiled_declarations"]:
                lines.append(f"- `{declaration['name']}` — `sorryAx={declaration['usesSorryAx']}`")
        lines += ["", "</details>", ""]

    lines += [
        "",
        "## Current interpretation",
        "",
        "The endpoint routes show that the five-moment and rank modules are reachable from the selected theorem. The remaining review question is value-level transport: whether the promoted moment quantities are proved equal to the moments of the final Cartesian fields and are consumed by the exported candidate predicates.",
        "",
        "The map therefore supports architectural tracing without converting a missing bridge into a kernel contradiction.",
        "",
    ]
    if validation["failures"]:
        lines += ["## Integrity failures", ""]
        lines.extend(f"- {failure}" for failure in validation["failures"])
        lines.append("")
    return "\n".join(lines)


def dot(mapping: dict[str, Any]) -> str:
    """Render the exact compiled route ledger as a Graphviz/DOT graph."""
    node_ids: dict[str, str] = {}
    nodes: list[str] = []
    edges: set[tuple[str, str]] = set()
    next_id = 0
    for route in mapping["routes"]:
        previous: str | None = None
        for node in route["path"]:
            name = node["name"]
            if name not in node_ids:
                node_ids[name] = f"n{next_id}"
                next_id += 1
                source = node["source"]
                label = name
                if source:
                    label += f"\\n{source['path']}:{source['line']}"
                nodes.append(f'  {node_ids[name]} [label="{label.replace(chr(34), chr(39))}"];')
            if previous is not None:
                edges.add((previous, name))
            previous = name
    lines = [
        "digraph SelectedEndpointRoutes {",
        "  rankdir=LR;",
        '  graph [fontname="Helvetica", labelloc="t", label="Compiled selected-endpoint route graph"];',
        '  node [shape=box, style="rounded,filled", fillcolor="#eef4ff", fontname="Helvetica", fontsize=9];',
        '  edge [color="#5b6b8c"];',
        *nodes,
    ]
    lines.extend(f"  {node_ids[left]} -> {node_ids[right]};" for left, right in sorted(edges))
    lines.append("}")
    return "\n".join(lines) + "\n"


def tex(mapping: dict[str, Any]) -> str:
    """Render a compact LaTeX appendix for the review manuscript."""
    counts = mapping["counts"]
    esc = lambda value: str(value).replace("\\", "/").replace("_", r"\_").replace("%", r"\%")
    lines = [
        r"% Generated by NavierStokesReview/src/audit/repository_map.py",
        r"\section{Repository map and evidence layers}",
        r"\label{sec:repository-map}",
        "This appendix is generated from the authoritative tree snapshot, current source hashes, and the compiled Lean environment. It is a navigation record, not an inference that compiled reachability establishes semantic transport.",
        r"\begin{center}",
        r"\begin{tabular}{lr}",
        r"Mapped Lean modules & " + str(counts["mapped_modules"]) + r"\\",
        r"Source declarations & " + str(counts["source_declarations"]) + r"\\",
        r"Compiled environment nodes & " + str(counts["compiled_nodes"]) + r"\\",
        r"Compiled environment edges & " + str(counts["compiled_edges"]) + r"\\",
        r"Exact source joins & " + str(counts["exact_source_matches"]) + r"\\",
        r"Reachable $\texttt{sorryAx}$ users & " + str(counts["reachable_sorryAx_users"]) + r"\\",
        r"\end{tabular}",
        r"\end{center}",
        r"\subsection{Selected endpoint routes}",
        r"\begin{longtable}{p{0.37\linewidth}p{0.55\linewidth}}",
        r"Route & Compiled declaration path\\\hline",
    ]
    for route in mapping["routes"]:
        path = r" $\to$ ".join(esc(node["name"]) for node in route["path"])
        lines.append(esc(route["name"]) + " & " + path + r"\\")
    lines += [
        r"\end{longtable}",
        r"\subsection{Evidence rule}",
        r"A route establishes that declarations occur in the compiled environment's dependency closure. The selected five-moment objection remains a value-level transport question: the map does not claim that the internal moment variables equal integrals of the exported Cartesian fields.",
        r"\subsection{Module index}",
        r"\begin{longtable}{p{0.30\linewidth}p{0.28\linewidth}rr}",
        r"Module & Source & Declarations & Imports\\\hline",
    ]
    for module in mapping["modules"]:
        lines.append(
            esc(module["module"])
            + " & "
            + esc(module["path"])
            + " & "
            + str(module["declaration_count"])
            + " & "
            + str(len(module["imports"]))
            + r"\\"
        )
    lines += [r"\end{longtable}", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--source-map", type=Path, required=True)
    parser.add_argument("--joined", type=Path, required=True)
    parser.add_argument("--claims", type=Path, required=True)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    parser.add_argument("--dot-output", type=Path, required=True)
    parser.add_argument("--tex-output", type=Path, required=True)
    args = parser.parse_args()

    mapping = build_map(
        args.repo.resolve(),
        load(args.source_map.resolve()),
        load(args.joined.resolve()),
        load(args.claims.resolve()),
        args.tree.resolve(),
    )
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.write_text(markdown(mapping), encoding="utf-8")
    args.dot_output.parent.mkdir(parents=True, exist_ok=True)
    args.dot_output.write_text(dot(mapping), encoding="utf-8")
    args.tex_output.parent.mkdir(parents=True, exist_ok=True)
    args.tex_output.write_text(tex(mapping), encoding="utf-8")
    print(json.dumps({"passed": mapping["validation"]["passed"], "counts": mapping["counts"]}))
    if not mapping["validation"]["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
