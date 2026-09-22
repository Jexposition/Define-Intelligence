"""Compile one Lean module closure without Lake's generated C/IR cache.

This review utility is intentionally independent of the upstream source. It
parses only project-local imports, leaves package modules to their existing
compiled interfaces, and invokes the pinned Lean executable directly with
`-o` and `-i`. That avoids recreating the multi-gigabyte Lake IR directory
when a target's transitive axiom report is the only required output.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path


IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)")
PROJECT_PREFIXES = ("Euler", "NavierStokes")


@dataclass(frozen=True)
class CompileResult:
    module: str
    status: str
    returncode: int
    output: str


def module_source(root: Path, module: str) -> Path | None:
    if not module.startswith(PROJECT_PREFIXES):
        return None
    path = root.joinpath(*module.split(".")).with_suffix(".lean")
    return path if path.is_file() else None


def imports(source: Path) -> list[str]:
    found: list[str] = []
    for line in source.read_text(encoding="utf-8").splitlines():
        match = IMPORT_RE.match(line)
        if match:
            found.append(match.group(1))
    return found


def closure(root: Path, target: str) -> dict[str, Path]:
    result: dict[str, Path] = {}
    pending = [target]
    while pending:
        module = pending.pop()
        if module in result:
            continue
        source = module_source(root, module)
        if source is None:
            raise FileNotFoundError(f"project module source not found: {module}")
        result[module] = source
        pending.extend(dep for dep in imports(source) if dep.startswith(PROJECT_PREFIXES))
    return result


def levels(nodes: dict[str, Path]) -> list[list[str]]:
    dependencies = {
        module: [dep for dep in imports(source) if dep in nodes]
        for module, source in nodes.items()
    }
    remaining = set(nodes)
    result: list[list[str]] = []
    while remaining:
        ready = sorted(module for module in remaining if not (set(dependencies[module]) & remaining))
        if not ready:
            raise RuntimeError(f"import cycle or unresolved dependency: {sorted(remaining)[:10]}")
        result.append(ready)
        remaining.difference_update(ready)
    return result


def lean_path(root: Path) -> str:
    paths = []
    for package in sorted((root / ".lake" / "packages").iterdir()):
        candidate = package / ".lake" / "build" / "lib" / "lean"
        if candidate.is_dir():
            paths.append(str(candidate))
    paths.append(str(root / ".lake" / "build" / "lib" / "lean"))
    return os.pathsep.join(paths)


def compile_one(root: Path, module: str, source: Path, lean: Path) -> CompileResult:
    relative = Path(*module.split("."))
    output = root / ".lake" / "build" / "lib" / "lean" / relative.with_suffix(".olean")
    interface = output.with_suffix(".ilean")
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.is_file() and output.stat().st_mtime >= source.stat().st_mtime:
        return CompileResult(module, "cached", 0, "")
    env = os.environ.copy()
    env["LEAN_PATH"] = lean_path(root)
    process = subprocess.run(
        [str(lean), str(source), "-o", str(output), "-i", str(interface)],
        cwd=root,
        env=env,
        text=True,
        capture_output=True,
    )
    output_text = (process.stdout + process.stderr).strip()
    status = "compiled" if process.returncode == 0 else "failed"
    return CompileResult(module, status, process.returncode, output_text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="project module, for example Euler.Solution")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--lean",
        type=Path,
        default=Path(r"C:\Users\Admin\.elan\toolchains\leanprover--lean4---v4.34.0-rc2\bin\lean.exe"),
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3]
    nodes = closure(root, args.target)
    groups = levels(nodes)
    results: list[CompileResult] = []
    for group in groups:
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {
                executor.submit(compile_one, root, module, nodes[module], args.lean): module
                for module in group
            }
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                print(f"{result.status}: {result.module}", flush=True)
                if result.status == "failed":
                    print(result.output, flush=True)
                    return result.returncode or 1
    summary = {
        "target": args.target,
        "project_modules": len(nodes),
        "groups": len(groups),
        "results": [result.__dict__ for result in results],
    }
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
