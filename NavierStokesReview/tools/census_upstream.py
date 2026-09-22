from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


TOKENS = ("sorry", "admit", "axiom", "opaque", "unsafe", "noncomputable", "#print axioms")
MAIN_DECLS = (
    "navier_stokes_breakdown_R3",
    "navier_stokes_breakdown_periodic",
    "euler_breakdown_R3",
    "exists_compact_smooth_euler_singularity",
)
EXCLUDED_DIRS = {".git", ".lake", ".github", ".vscode"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def line_hits(path: Path, patterns: tuple[str, ...]) -> dict[str, list[int]]:
    hits = {pattern: [] for pattern in patterns}
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return hits
    for number, line in enumerate(lines, 1):
        for pattern in patterns:
            if pattern in line:
                hits[pattern].append(number)
    return hits


def inventory(repo: Path) -> dict:
    files = sorted(
        path
        for path in repo.rglob("*")
        if path.is_file() and not any(part in EXCLUDED_DIRS for part in path.relative_to(repo).parts)
    )
    lean = [path for path in files if path.suffix == ".lean"]
    markdown = [path for path in files if path.suffix.lower() in {".md", ".markdown"}]
    manifests = [path for path in files if path.name in {"lakefile.toml", "lake-manifest.json", "lean-toolchain", "formalization.yaml"}]
    records = []
    for path in lean:
        relative = path.relative_to(repo).as_posix()
        raw = path.read_text(encoding="utf-8", errors="replace")
        records.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "lexical_counts": {token: raw.count(token) for token in TOKENS},
                "line_hits": line_hits(path, TOKENS + MAIN_DECLS),
            }
        )
    return {
        "repo": str(repo),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "file_counts": {
            "all_files": len(files),
            "lean_files": len(lean),
            "markdown_files": len(markdown),
            "manifest_files": len(manifests),
        },
        "manifests": [path.relative_to(repo).as_posix() for path in manifests],
        "lean_files": records,
    }


def compare(old: Path | None, new: Path) -> dict | None:
    if old is None or not old.exists():
        return None
    old_files = {
        path.relative_to(old).as_posix(): path
        for path in old.rglob("*")
        if path.is_file() and not any(part in EXCLUDED_DIRS for part in path.relative_to(old).parts)
    }
    new_files = {
        path.relative_to(new).as_posix(): path
        for path in new.rglob("*")
        if path.is_file() and not any(part in EXCLUDED_DIRS for part in path.relative_to(new).parts)
    }
    common = sorted(set(old_files) & set(new_files))
    changed = [name for name in common if sha256(old_files[name]) != sha256(new_files[name])]
    return {
        "old_repo": str(old),
        "new_repo": str(new),
        "old_files": len(old_files),
        "new_files": len(new_files),
        "added": sorted(set(new_files) - set(old_files)),
        "removed": sorted(set(old_files) - set(new_files)),
        "changed_sha256": changed,
    }


def markdown(data: dict, comparison: dict | None) -> str:
    totals = {token: 0 for token in TOKENS}
    important = []
    for record in data["lean_files"]:
        for token, count in record["lexical_counts"].items():
            totals[token] += count
        if any(record["line_hits"].get(decl) for decl in MAIN_DECLS):
            important.append(record)
    lines = [
        "# Upstream source census",
        "",
        f"Generated: `{data['generated_utc']}`",
        f"Repository: `{data['repo']}`",
        "",
        "This is a lexical and provenance census, not a proof verdict. Token counts include comments and strings; each candidate must be checked through imports and kernel output.",
        "",
        "## Inventory",
        "",
        f"- Files: {data['file_counts']['all_files']} total, {data['file_counts']['lean_files']} Lean, {data['file_counts']['markdown_files']} Markdown.",
        f"- Manifest files: {', '.join('`' + item + '`' for item in data['manifests'])}.",
        "",
        "## Raw lexical totals",
        "",
    ]
    lines += [f"- `{token}`: {totals[token]}" for token in TOKENS]
    lines += ["", "## Main declaration locations", ""]
    for record in important:
        hits = []
        for decl in MAIN_DECLS:
            for line in record["line_hits"].get(decl, []):
                hits.append(f"`{decl}` at line {line}")
        lines.append(f"- `{record['path']}`: " + "; ".join(hits))
    if comparison:
        lines += ["", "## Downloaded copy versus current clone", "", f"- Old files: {comparison['old_files']}", f"- Current files: {comparison['new_files']}", f"- Added in current clone: {len(comparison['added'])}", f"- Removed in current clone: {len(comparison['removed'])}", f"- SHA-256 changed common files: {len(comparison['changed_sha256'])}"]
    lines += ["", "## Interpretation guardrails", "", "1. A zero `sorry` count is not sufficient: the theorem statement, imports, definitions, and `#print axioms` output must all be inspected.", "2. `axiom`, `opaque`, and `noncomputable` lexical hits require declaration-level classification; comments and documentation can produce false positives.", "3. CMI alignment is separate from Lean soundness: a kernel-checked theorem can still formalise a weaker or different PDE problem.", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Census a Lean repository without modifying it")
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    data = inventory(repo)
    comparison = compare(args.compare.resolve() if args.compare else None, repo)
    payload = {"census": data, "comparison": comparison}
    (out / "UPSTREAM_SOURCE_CENSUS.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (out / "UPSTREAM_SOURCE_CENSUS.md").write_text(markdown(data, comparison), encoding="utf-8")
    print(json.dumps({"lean_files": data["file_counts"]["lean_files"], "comparison": comparison}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
