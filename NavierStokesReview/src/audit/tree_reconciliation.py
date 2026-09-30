#!/usr/bin/env python3
"""Reconcile a tree-maker inventory with the current checkout.

The tree-maker export is useful inventory evidence, but its rendered branch
indentation is not a stable path encoding.  This module therefore never
turns a basename into a path unless the current checkout contains exactly one
file with that basename.  Duplicate basenames and missing files remain
explicitly unresolved.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
TREE_ITEM_RE = re.compile(r"(?P<kind>📂|📄)\s+(?P<name>.+?)\s*$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_name(name: str) -> str:
    name = ANSI_RE.sub("", name).strip()
    # `docs/doc_tree.md` annotates historical entries after the filename.
    # The annotation is presentation metadata, not part of the checkout path.
    name = re.sub(r"\s+\(historical archive\)\s*$", "", name)
    if name.endswith("/"):
        name = name[:-1]
    return name


def read_tree_entries(tree: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for line_number, raw in enumerate(
        tree.read_text(encoding="utf-8", errors="replace").splitlines(), 1
    ):
        line = ANSI_RE.sub("", raw)
        match = TREE_ITEM_RE.search(line)
        if match is None:
            continue
        entries.append(
            {
                "line": line_number,
                "kind": "directory" if match.group("kind") == "📂" else "file",
                "name": clean_name(match.group("name")),
                "display_indent": len(line[: match.start()].expandtabs(2)),
            }
        )
    return entries


def checkout_files(repo: Path) -> list[Path]:
    return sorted(
        path
        for path in repo.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and ".lake" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    )


def reconcile(repo: Path, tree: Path) -> dict[str, Any]:
    entries = read_tree_entries(tree)
    files = checkout_files(repo)
    by_basename: dict[str, list[str]] = defaultdict(list)
    for path in files:
        by_basename[path.name].append(path.relative_to(repo).as_posix())

    tree_files = [entry for entry in entries if entry["kind"] == "file"]
    tree_names = sorted({entry["name"] for entry in tree_files})
    resolved: list[dict[str, str]] = []
    ambiguous: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    directory_stack: list[tuple[int, str]] = []
    for entry in entries:
        # The tree is a rendered hierarchy.  Retain its directory context so
        # a child such as `ARCHIVE_MANIFEST_2026-09-30.md` is resolved below
        # the preceding `archive` directory rather than as a repository-wide
        # basename.
        while directory_stack and entry["display_indent"] <= directory_stack[-1][0]:
            directory_stack.pop()
        context = Path(*[name for _, name in directory_stack])

        if entry["kind"] == "directory":
            # The first rendered directory is the tree's own root (`docs` in
            # `docs/doc_tree.md`), so the tree path already supplies it.
            if not directory_stack and entry["name"] == tree.parent.name:
                continue
            directory_stack.append((entry["display_indent"], entry["name"]))
            continue

        # Prefer an explicit path relative to the tree's directory and its
        # rendered directory context.  This avoids turning a known path into
        # a false basename ambiguity.
        tree_relative = (tree.parent / context / entry["name"]).resolve()
        if tree_relative.is_file() and repo.resolve() in tree_relative.parents:
            resolved.append(
                {
                    "tree_line": str(entry["line"]),
                    "tree_name": entry["name"],
                    "basename": Path(entry["name"]).name,
                    "current_path": tree_relative.relative_to(repo).as_posix(),
                    "resolution": "explicit-tree-relative-path",
                }
            )
        else:
            # Otherwise, reconcile by the actual basename while retaining the
            # original tree label in the evidence record.  This is deliberately
            # conservative for entries that do not carry a resolvable path.
            basename = Path(entry["name"]).name
            candidates = by_basename.get(basename, [])
            if len(candidates) == 1:
                resolved.append(
                    {
                        "tree_line": str(entry["line"]),
                        "tree_name": entry["name"],
                        "basename": basename,
                        "current_path": candidates[0],
                        "resolution": "unique-current-basename",
                    }
                )
            elif not candidates:
                missing.append(entry)
            else:
                ambiguous.append({**entry, "current_candidates": candidates})

    current_paths = {path.relative_to(repo).as_posix() for path in files}
    return {
        "schema": "navier-stokes-review-tree-reconciliation/v1",
        "authority": {
            "tree": "inventory snapshot with basename evidence",
            "checkout": "exact current relative paths and hashes",
            "rule": "no path is inferred from a basename when the current basename is ambiguous",
        },
        "inputs": {
            "repository": str(repo.resolve()),
            "tree": str(tree.resolve()),
            "tree_sha256": sha256(tree),
            "tree_line_count": len(tree.read_text(encoding="utf-8", errors="replace").splitlines()),
        },
        "counts": {
            "tree_entries": len(entries),
            "tree_file_entries": len(tree_files),
            "tree_unique_file_basenames": len(tree_names),
            "current_files": len(files),
            "uniquely_resolved_tree_files": len(resolved),
            "ambiguous_tree_files": len(ambiguous),
            "missing_tree_files": len(missing),
            "duplicate_current_basenames": sum(1 for paths in by_basename.values() if len(paths) > 1),
        },
        "tree_entries": entries,
        "resolved": resolved,
        "ambiguous": ambiguous,
        "missing": missing,
        "current_paths": sorted(current_paths),
    }


def markdown(payload: dict[str, Any]) -> str:
    counts = payload["counts"]
    lines = [
        "# Tree reconciliation",
        "",
        "The extracted tree is an inventory snapshot. Current checkout paths are authoritative; unique basenames are used only to reconcile inventory entries, never to manufacture a path from an ambiguous name.",
        "",
        "## Inputs",
        "",
        f"- Tree: `{payload['inputs']['tree']}`",
        f"- Tree SHA-256: `{payload['inputs']['tree_sha256']}`",
        "",
        "## Counts",
        "",
        "| Quantity | Count |",
        "|---|---:|",
        f"| Tree entries | `{counts['tree_entries']}` |",
        f"| Tree file entries | `{counts['tree_file_entries']}` |",
        f"| Current checkout files | `{counts['current_files']}` |",
        f"| Resolved tree entries | `{counts['uniquely_resolved_tree_files']}` |",
        f"| Ambiguous tree entries | `{counts['ambiguous_tree_files']}` |",
        f"| Missing tree entries | `{counts['missing_tree_files']}` |",
        f"| Duplicate current basenames | `{counts['duplicate_current_basenames']}` |",
        "",
        "## Interpretation",
        "",
        "A resolved entry establishes only that the named file exists at the resolved current path. It does not establish import reachability or theorem use. Explicit tree-relative paths are preferred; basename fallback remains conservative. Ambiguous and missing entries are retained as review obligations.",
        "",
    ]
    if payload["ambiguous"]:
        lines.extend(["## Ambiguous entries", ""])
        for entry in payload["ambiguous"][:20]:
            lines.append(
                f"- line `{entry['line']}` `{entry['name']}`: `{', '.join(entry['current_candidates'])}`"
            )
        lines.append("")
    if payload["missing"]:
        lines.extend(["## Missing current basenames", ""])
        for entry in payload["missing"][:20]:
            lines.append(f"- line `{entry['line']}` `{entry['name']}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    payload = reconcile(args.repo.resolve(), args.tree.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.markdown.write_text(markdown(payload), encoding="utf-8")
    print(json.dumps({"counts": payload["counts"], "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
