#!/usr/bin/env python3
"""Inventory supplied review inputs without copying generated or binary data.

The inventory is deliberately evidence-oriented: every input gets a SHA-256,
size, line count where applicable, headings, and keyword locations.  It keeps
the original files outside the fork while making the exact review corpus
reproducible.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


KEYWORDS = (
    "axiom",
    "sorry",
    "CMI",
    "Clay",
    "Alternative C",
    "Alternative D",
    "Navier",
    "force",
    "scaling",
    "pressure",
    "smooth",
    "energy",
    "zero division",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git_revision(repo: Path) -> str | None:
    try:
        return subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def markdown_summary(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    headings = [line.strip() for line in lines if line.lstrip().startswith("#")]
    keyword_hits = {
        keyword: sum(1 for line in lines if keyword.lower() in line.lower())
        for keyword in KEYWORDS
    }
    return {
        "line_count": len(lines),
        "headings": headings,
        "keyword_line_counts": keyword_hits,
    }


def record(path: Path, label: str) -> dict[str, Any]:
    item: dict[str, Any] = {
        "label": label,
        "path": str(path),
        "name": path.name,
        "extension": path.suffix.lower(),
        "size_bytes": path.stat().st_size,
        "sha256": sha256(path),
    }
    if path.suffix.lower() in {".md", ".txt", ".lean", ".toml", ".yaml", ".json"}:
        item["text"] = markdown_summary(path)
    return item


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--input-root", type=Path, required=True)
    parser.add_argument("--backup-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    paths: list[tuple[Path, str]] = []
    input_names = [
        "Technical Audit Report_ Evaluating the Validity and Mathematical Utility of the OpenAI Astra Proof Certificates.md",
        "Navier-Stokes Research Paper Refinement.md",
        "Note on the Logical Inconsistencies in the Formalised Navier-Stokes Blowup Construction.md",
        "Note on the Logical Inconsistencies in the Formalised Navier-Stokes Blowup Construction (1).md",
        "Note on the Logical Inconsencies in the Formalised Navier-Stokes Blowup Construction (2).md",
        "Note on the Logical Inconsistencies in the Formalised Navier-Stokes Blowup Construction (2).md",
        "navier-stokes.pdf",
        "NavierStokesAndEuler-main.zip",
    ]
    for name in input_names:
        path = args.input_root / name
        if path.is_file():
            paths.append((path, "supplied-root"))

    if args.backup_root.is_dir():
        for path in sorted(args.backup_root.iterdir()):
            if path.is_file():
                paths.append((path, "supplied-backup"))

    for relative in (
        "docs/OpenAI_NavierStokes_CMI_First_Review_Plan.md",
        "docs/OpenAI_NavierStokes_Audit_Tracker.md",
        "docs/OpenAI_NavierStokes_Axiom_Ledger.md",
        "docs/OpenAI_NavierStokes_Research_Paper.md",
        "docs/OpenAI_NavierStokes_Peer_Review_v1.md",
        "NavierStokesReview/README.md",
    ):
        path = args.repo / relative
        if path.is_file():
            paths.append((path, "fork-review-document"))

    # De-duplicate by resolved path while preserving the first label.
    seen: set[Path] = set()
    records = []
    for path, label in paths:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        records.append(record(resolved, label))

    payload = {
        "schema": "navier-stokes-review-input-inventory/v1",
        "generated_from": {
            "repository": str(args.repo.resolve()),
            "git_revision": git_revision(args.repo.resolve()),
            "input_root": str(args.input_root.resolve()),
            "backup_root": str(args.backup_root.resolve()),
        },
        "count": len(records),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"count": len(records), "output": str(args.output), "git_revision": payload["generated_from"]["git_revision"]}, indent=2))


if __name__ == "__main__":
    main()
