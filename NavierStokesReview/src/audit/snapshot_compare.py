#!/usr/bin/env python3
"""Compare a downloaded source archive with the checked-out review snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path


TEXT_SUFFIXES = {".lean", ".toml", ".yaml", ".yml", ".json", ".md", ".txt"}


def normalise(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", dest="archive", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with zipfile.ZipFile(args.archive) as archive:
        entries = {
            name.split("/", 1)[1]: normalise(archive.read(name))
            for name in archive.namelist()
            if not name.endswith("/")
            and "/" in name
            and Path(name).suffix.lower() in TEXT_SUFFIXES
        }

    equal: list[str] = []
    changed: list[str] = []
    missing: list[str] = []
    for relative, archive_bytes in sorted(entries.items()):
        path = args.repo / relative
        if not path.is_file():
            missing.append(relative)
        elif normalise(path.read_bytes()) == archive_bytes:
            equal.append(relative)
        else:
            changed.append(relative)

    payload = {
        "schema": "navier-stokes-review-snapshot-comparison/v1",
        "archive": str(args.archive.resolve()),
        "repository": str(args.repo.resolve()),
        "archive_text_entries": len(entries),
        "equal_after_line_ending_normalisation": len(equal),
        "changed": len(changed),
        "missing_in_repository": len(missing),
        "changed_paths": changed,
        "missing_paths": missing,
        "archive_text_sha256": digest(b"\n".join(entries[key] for key in sorted(entries))),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
