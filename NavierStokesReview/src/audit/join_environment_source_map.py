#!/usr/bin/env python3
"""Join Lean environment dependencies to source-coordinate declarations.

The source scanner and the Lean environment exporter intentionally have
different evidence levels.  This tool joins them by exact declaration name,
then reports unmatched environment nodes instead of guessing from basenames.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROUTE_TARGETS = (
    "NavierStokesR3.theorem_1_1",
    "NavierStokes.ActualCandidateAssembly.selected_witness",
    "NavierStokes.FiveRowRank.FiveRows",
    "NavierStokes.FiveRowRank.Debt",
    "NavierStokes.PositiveOrderMoments.Debt",
    "NavierStokes.MeanRankUpdate.scaleDebt",
    "NavierStokes.MixedPeriodicAssembly.periodicVelocity",
    "NavierStokes.DefectIncrementBounds.barMoment",
    "NavierStokes.R3CompactCandidate.velocity",
    "NavierStokesR3.ProblemStatement.CandidateProperties",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def declaration_index(source_map: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for module, record in source_map["modules"].items():
        for declaration in record["declarations"]:
            index[declaration["name"]].append(
                {
                    "module": module,
                    "path": record["path"],
                    "sha256": record["sha256"],
                    "line": declaration["line"],
                    "end_line": declaration["end_line"],
                    "kind": declaration["kind"],
                }
            )
    return index


def short_name(name: str) -> str:
    return name.rsplit(".", 1)[-1]


def dependency_routes(
    root: str, edges: list[dict[str, Any]], targets: tuple[str, ...] = ROUTE_TARGETS
) -> dict[str, dict[str, Any]]:
    adjacency: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        adjacency[edge["from"]].append(edge["to"])
    routes: dict[str, dict[str, Any]] = {}
    queue: list[str] = [root]
    parents: dict[str, str | None] = {root: None}
    while queue:
        current = queue.pop(0)
        for child in adjacency.get(current, []):
            if child not in parents:
                parents[child] = current
                queue.append(child)
    for target in targets:
        if target not in parents:
            routes[target] = {"reachable": False, "path": []}
            continue
        path: list[str] = []
        current: str | None = target
        while current is not None:
            path.append(current)
            current = parents[current]
        path.reverse()
        routes[target] = {"reachable": True, "path": path}
    return routes


def join(source_map: dict[str, Any], environment: dict[str, Any]) -> dict[str, Any]:
    index = declaration_index(source_map)
    nodes = environment["nodes"]
    exact: list[dict[str, Any]] = []
    unmatched: list[str] = []
    ambiguous: list[dict[str, Any]] = []
    for node in nodes:
        name = node["name"]
        matches = index.get(name, [])
        if len(matches) == 1:
            exact.append({**node, "source": matches[0]})
        elif len(matches) > 1:
            ambiguous.append({"name": name, "matches": matches})
        else:
            unmatched.append(name)

    by_name = {item["name"]: item for item in exact}
    endpoint_reachable = [item for item in exact if item["name"] in by_name]
    source_counts = Counter(item["source"]["path"] for item in endpoint_reachable)
    sorry_nodes = [item["name"] for item in exact if item.get("usesSorryAx")]
    edges = [
        edge
        for edge in environment["edges"]
        if edge["from"] in by_name and edge["to"] in by_name
    ]
    routes = dependency_routes(environment["root"], edges)
    return {
        "schema": "navier-stokes-review-joined-environment-source-map/v1",
        "inputs": {
            "source_map": source_map["inputs"],
            "source_map_sha256": None,
            "environment_root": environment["root"],
            "environment_schema": environment["schema"],
        },
        "counts": {
            "environment_nodes": len(nodes),
            "exact_source_matches": len(exact),
            "ambiguous_source_matches": len(ambiguous),
            "unmatched_environment_nodes": len(unmatched),
            "joined_edges": len(edges),
            "joined_nodes_using_sorryAx": len(sorry_nodes),
        },
        "root": environment["root"],
        "root_source": by_name.get(environment["root"]),
        "reachable_source_file_counts": dict(sorted(source_counts.items())),
        "nodes": exact,
        "edges": edges,
        "ambiguous": ambiguous,
        "unmatched": unmatched,
        "routes": routes,
    }


def markdown(payload: dict[str, Any]) -> str:
    counts = payload["counts"]
    lines = [
        "# Joined Lean environment and source map",
        "",
        "This artifact joins the compiled Lean environment to source paths and declaration spans by exact declaration name.",
        "Basename matching and token matching are not used for the join.",
        "",
        f"- Root: `{payload['root']}`",
        f"- Environment nodes: `{counts['environment_nodes']}`",
        f"- Exact source matches: `{counts['exact_source_matches']}`",
        f"- Ambiguous source matches: `{counts['ambiguous_source_matches']}`",
        f"- Unmatched environment nodes: `{counts['unmatched_environment_nodes']}`",
        f"- Joined kernel edges: `{counts['joined_edges']}`",
        f"- Joined nodes marked `usesSorryAx`: `{counts['joined_nodes_using_sorryAx']}`",
        "",
        "## Root source span",
        "",
    ]
    root_source = payload.get("root_source")
    if root_source:
        source = root_source["source"]
        lines.append(
            f"`{source['path']}:{source['line']}-{source['end_line']}` "
            f"({source['kind']}, SHA-256 `{source['sha256']}`)."
        )
    else:
        lines.append("No exact source declaration match was found for the root.")
    lines.extend(["", "## Source files represented in the joined closure", ""])
    for path, count in payload["reachable_source_file_counts"].items():
        lines.append(f"- `{path}`: `{count}` declarations")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "An exact match records a source location for a compiled declaration. "
            "An unmatched node is not evidence of a missing theorem: it may be a generated, imported, or namespace-normalised environment declaration. "
            "It is recorded for follow-up rather than silently inferred.",
        ]
    )
    lines.extend(["", "## Selected endpoint routes", ""])
    for target, route in payload["routes"].items():
        if not route["reachable"]:
            lines.append(f"- `{target}`: not reachable in the joined environment graph")
            continue
        path = route["path"]
        terminal = next(
            (node for node in payload["nodes"] if node["name"] == target), None
        )
        if terminal and terminal.get("source"):
            source = terminal["source"]
            location = f"{source['path']}:{source['line']}-{source['end_line']}"
        else:
            location = "source span unavailable"
        lines.append(
            f"- `{target}` ({location}, `{len(path) - 1}` edges): "
            + " -> ".join(f"`{node}`" for node in path)
        )
    return "\n".join(lines) + "\n"


def routes_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Selected endpoint dependency routes",
        "",
        "This compact report records exact compiled-environment routes from the exported endpoint to selected audit targets.",
        "Routes are kernel-environment edges; source locations are attached only after exact declaration-name joining.",
        "",
        f"- Root: `{payload['root']}`",
        f"- Environment nodes: `{payload['counts']['environment_nodes']}`",
        f"- Exact source matches: `{payload['counts']['exact_source_matches']}`",
        "",
        "| Target | Reachable | Source span | Edges |",
        "|---|---:|---|---:|",
    ]
    by_name = {node["name"]: node for node in payload["nodes"]}
    for target, route in payload["routes"].items():
        terminal = by_name.get(target)
        source = terminal.get("source") if terminal else None
        location = (
            f"`{source['path']}:{source['line']}-{source['end_line']}`"
            if source
            else "unavailable"
        )
        lines.append(
            f"| `{target}` | `{route['reachable']}` | {location} | "
            f"`{len(route['path']) - 1 if route['reachable'] else 0}` |"
        )
    lines.extend(["", "## Routes", ""])
    for target, route in payload["routes"].items():
        lines.append(f"### `{target}`")
        if route["reachable"]:
            lines.append("")
            lines.append(" -> ".join(f"`{node}`" for node in route["path"]))
        else:
            lines.append("")
            lines.append("No route found in the joined graph.")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-map", type=Path, required=True)
    parser.add_argument("--environment", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--routes-markdown", type=Path)
    args = parser.parse_args()
    source_map = load(args.source_map)
    environment = load(args.environment)
    payload = join(source_map, environment)
    payload["inputs"]["source_map_sha256"] = sha256(args.source_map)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.markdown.write_text(markdown(payload), encoding="utf-8")
    if args.routes_markdown:
        args.routes_markdown.write_text(routes_markdown(payload), encoding="utf-8")
    print(json.dumps({"schema": payload["schema"], **payload["counts"]}, sort_keys=True))


if __name__ == "__main__":
    main()
