#!/usr/bin/env python3
"""Human-readable queries over the generated source/environment map.

This is a navigation layer only.  It reports exact source spans and compiled
environment metadata already captured by the audit run; it does not infer a
mathematical theorem from a token hit.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_matches(source_map: dict[str, Any], query: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    query = query.lower()
    for module, record in source_map["modules"].items():
        for declaration in record["declarations"]:
            if query in declaration["name"].lower() or query in declaration["short_name"].lower():
                rows.append(
                    {
                        "name": declaration["name"],
                        "kind": declaration["kind"],
                        "path": record["path"],
                        "line": declaration["line"],
                        "end_line": declaration["end_line"],
                        "sha256": record["sha256"],
                        "source_flags": record["source_flags"],
                    }
                )
    return sorted(rows, key=lambda row: (row["name"], row["path"], row["line"]))


def environment_matches(joined: dict[str, Any], query: str) -> list[dict[str, Any]]:
    query = query.lower()
    return sorted(
        [
            {
                "name": node["name"],
                "type": node.get("type"),
                "source": node.get("source"),
                "usesSorryAx": node.get("usesSorryAx", False),
            }
            for node in joined.get("nodes", [])
            if query in node.get("name", "").lower()
        ],
        key=lambda row: row["name"],
    )


def render(query: str, source: list[dict[str, Any]], env: list[dict[str, Any]], joined: dict[str, Any]) -> str:
    lines = [f"# Mapping query: `{query}`", "", "## Source declarations", ""]
    if source:
        lines += ["| Name | Kind | Source span | SHA-256 |", "|---|---|---|---|"]
        for row in source:
            lines.append(
                f"| `{row['name']}` | `{row['kind']}` | `{row['path']}:{row['line']}-{row['end_line']}` | `{row['sha256'][:16]}…` |"
            )
    else:
        lines.append("No source declaration matched.")
    lines += ["", "## Compiled environment declarations", ""]
    if env:
        lines += ["| Name | Exact source join | sorryAx in node |", "|---|---|---|"]
        for row in env:
            source_info = row["source"]
            joined_text = "unmatched"
            if source_info:
                joined_text = f"{source_info['path']}:{source_info['line']}-{source_info['end_line']}"
            lines.append(f"| `{row['name']}` | `{joined_text}` | `{row['usesSorryAx']}` |")
    else:
        lines.append("No compiled declaration matched.")
    lines += [
        "",
        "## Evidence boundary",
        "",
        "Source spans establish where a declaration is written. Compiled rows establish what the captured environment exports and joins by exact fully qualified name. Neither section alone proves value-level transport of an invariant.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-map", type=Path, required=True)
    parser.add_argument("--joined", type=Path, required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source_map = load(args.source_map.resolve())
    joined = load(args.joined.resolve())
    source = source_matches(source_map, args.query)
    environment = environment_matches(joined, args.query)
    output = render(args.query, source, environment, joined)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
