#!/usr/bin/env python3
"""Build a read-only consolidation gate from the untracked inventory.

This tool does not stage, move, delete, or archive anything.  It verifies the
inventory hashes against the current worktree and records the manual review
state required before any disposition can change.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def archive_target(relative: str) -> str | None:
    if relative.startswith("docs/"):
        return "docs/archive/"
    if relative.startswith("NavierStokesReview/evidence/"):
        return "NavierStokesReview/evidence/archive/"
    return None


def review_question(relative: str, category: str) -> str:
    if category == "protected-source":
        return "Confirm it is OpenAI source or a protected source artifact; never stage or move in this workflow."
    if category == "unknown-artifact":
        return "Identify provenance and purpose before any disposition."
    if category == "archive-candidate":
        return "Compare against canonical documents and manifest; archive only after confirmed consolidation."
    if category == "review-document":
        return "Cross-reference claims, citations, and canonical destination before staging."
    if category == "review-evidence":
        return "Cross-reference result against source ledger and retain only with reproducible provenance."
    return "Classify manually before any disposition."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    repo = args.repo.resolve()
    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    duplicate_groups: dict[str, list[str]] = defaultdict(list)
    for item in inventory["records"]:
        duplicate_groups[item["sha256"]].append(item["path"])

    rows = []
    for item in inventory["records"]:
        relative = item["path"]
        path = repo / relative
        exists = path.is_file()
        current_sha = digest(path) if exists else None
        integrity = "verified_current_hash" if exists and current_sha == item["sha256"] else "missing_or_changed"
        duplicates = duplicate_groups[item["sha256"]]
        rows.append(
            {
                "path": relative,
                "category": item["category"],
                "inventory_sha256": item["sha256"],
                "current_sha256": current_sha,
                "integrity_status": integrity,
                "duplicate_paths": duplicates if len(duplicates) > 1 else [],
                "tracked_reference_count": len(item.get("referenced_by_tracked_files", [])),
                "worktree_reference_count": len(item.get("referenced_by_worktree_files", [])),
                "content_review_status": "pending_manual_source_review",
                "disposition_gate": "HOLD_NO_STAGE_NO_MOVE",
                "archive_target_if_later_approved": archive_target(relative),
                "review_question": review_question(relative, item["category"]),
            }
        )

    rows.sort(key=lambda row: row["path"].lower())
    payload = {
        "schema": "navier-stokes-untracked-consolidation-matrix/v1",
        "repository": str(repo),
        "inventory": str(args.inventory),
        "inventory_git_revision": inventory["git_revision"],
        "generated_git_revision": subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip(),
        "count": len(rows),
        "integrity_verified_count": sum(row["integrity_status"] == "verified_current_hash" for row in rows),
        "rows": rows,
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Untracked consolidation matrix",
        "",
        f"Repository: `{repo}`",
        f"Inventory revision: `{payload['inventory_git_revision']}`",
        f"Generated at revision: `{payload['generated_git_revision']}`",
        f"Entries: **{len(rows)}**",
        f"Current hashes verified: **{payload['integrity_verified_count']} / {len(rows)}**",
        "",
        "This is a consolidation gate, not an archive instruction. Every row remains on hold until manual content review, source cross-reference, and document-control confirmation are complete.",
        "",
        "| Path | Category | Integrity | Tracked refs | Worktree refs | Duplicate paths | Content review | Gate |",
        "| --- | --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['path']}` | {row['category']} | {row['integrity_status']} | "
            f"{row['tracked_reference_count']} | {row['worktree_reference_count']} | "
            f"{len(row['duplicate_paths'])} | {row['content_review_status']} | {row['disposition_gate']} |"
        )
    lines.extend(
        [
            "",
            "## Required review before any archive move",
            "",
            "1. Read each entry and compare it with the canonical paper, audit ledger, plan, and evidence documents.",
            "2. Record whether its claims are retained, merged, superseded, or rejected by source evidence; do not infer this from filenames.",
            "3. Update the archive manifest with old path, new path, reason, and SHA-256 only after confirmation.",
            "4. Stage only explicitly approved paths. Protected OpenAI source remains outside this consolidation workflow.",
        ]
    )
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"count": len(rows), "integrity_verified": payload["integrity_verified_count"]}))


if __name__ == "__main__":
    main()
