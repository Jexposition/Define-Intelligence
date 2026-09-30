#!/usr/bin/env python3
"""Hash and classify untracked review-repository content without changing it."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


PROTECTED = {
    "NavierStokes/R3/TestPressure.lean",
}


def git_paths(repo: Path) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(repo), "ls-files", "--others", "--exclude-standard", "-z"],
        check=True,
        capture_output=True,
    )
    return [item for item in result.stdout.decode("utf-8", "surrogateescape").split("\x00") if item]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def category(relative: str) -> tuple[str, str]:
    if relative in PROTECTED:
        return "protected-source", "do-not-touch-or-stage"
    if relative == "$null":
        return "unknown-artifact", "manual-identification-required"
    if relative.startswith("NavierStokesReview/evidence/"):
        return "review-evidence", "retain-or-consolidate-after-crosscheck"
    if relative.startswith("NavierStokesReview/src/"):
        return "review-tool-or-audit", "review-and-stage-explicitly-if-approved"
    if relative.startswith("docs/archive/"):
        return "archive-candidate", "verify-manifest-and-cross-references-before-move"
    if relative.startswith("docs/"):
        return "review-document", "cross-reference-before-staging"
    return "unclassified", "manual-classification-required"


def tracked_references(repo: Path, basename: str) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(repo), "grep", "-l", "-F", "--", basename],
        check=False,
        capture_output=True,
        text=True,
        errors="replace",
    )
    if result.returncode not in (0, 1):
        return []
    return [line for line in result.stdout.splitlines() if line]


def worktree_references(repo: Path, basename: str) -> list[str]:
    """Search the complete worktree, including untracked text files.

    The earlier inventory used ``git grep`` only.  That is deliberately kept
    as a separate compatibility field, but it is insufficient for a
    consolidation gate because untracked evidence can reference another
    untracked report.  ripgrep skips binary files and respects the worktree
    path filter below, so the result is a read-only textual cross-reference.
    """
    result = subprocess.run(
        ["rg", "-l", "-F", "--hidden", "-g", "!.git/**", "--", basename],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
        errors="replace",
    )
    if result.returncode not in (0, 1):
        return []
    return sorted(
        (line.replace("/", "\\") for line in result.stdout.splitlines() if line),
        key=str.lower,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()

    records = []
    for relative in git_paths(repo):
        path = repo / relative
        kind, disposition = category(relative)
        data = path.read_bytes()
        is_binary = b"\x00" in data[:8192]
        record = {
            "path": relative,
            "size_bytes": path.stat().st_size,
            "sha256": digest(path),
            "binary": is_binary,
            "category": kind,
            "disposition": disposition,
            "referenced_by_tracked_files": tracked_references(repo, Path(relative).name),
            "referenced_by_worktree_files": worktree_references(repo, Path(relative).name),
        }
        if not is_binary:
            record["line_count"] = data.decode("utf-8", "replace").count("\n") + (1 if data else 0)
        records.append(record)

    records.sort(key=lambda item: item["path"].lower())
    payload = {
        "schema": "navier-stokes-untracked-content-inventory/v2",
        "repository": str(repo),
        "git_revision": subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip(),
        "count": len(records),
        "records": records,
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Untracked content inventory",
        "",
        f"Repository: `{repo}`",
        f"Git revision: `{payload['git_revision']}`",
        f"Untracked entries: **{len(records)}**",
        "",
        "This is a read-only SHA-256 inventory. It authorises no staging, deletion, or archive move.",
        "Tracked references preserve the earlier git-only view; worktree references include untracked text evidence.",
        "",
        "| Path | Bytes | SHA-256 | Category | Disposition | Tracked refs | Worktree refs |",
        "| --- | ---: | --- | --- | --- | ---: | ---: |",
    ]
    for item in records:
        lines.append(
            f"| `{item['path']}` | {item['size_bytes']} | `{item['sha256']}` | "
            f"{item['category']} | {item['disposition']} | "
            f"{len(item['referenced_by_tracked_files'])} | "
            f"{len(item['referenced_by_worktree_files'])} |"
        )
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"count": len(records), "json": str(args.json), "markdown": str(args.markdown)}))


if __name__ == "__main__":
    main()
