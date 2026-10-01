"""Measure the two public Navier--Stokes submissions without conflating graphs.

The report has two deliberately separate layers:

* an immutable Git-object source/import/declaration census for submissions A and
  B; and
* an optional elaborated environment-reference closure for the current B
  checkout, using the previously exported Lean environment JSON.

The first layer is source archaeology, not a proof-term graph. The second is
closer to Lean's declaration environment, but it is still a declaration-use
closure rather than a semantic proof of the manuscript. The output records
these limits explicitly so that graph size cannot be promoted to mathematical
verification.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Iterable


COMMIT_A = "8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538"
COMMIT_B = "f9e8bc5b38b6e212696e8a30e3e91517af887bbd"

ROUTES = {
    "A_C": "NavierStokes/ComparatorR3Theorem.lean",
    "A_D": "NavierStokes/ComparatorTheorem.lean",
    "B_C": "NavierStokes/ComparatorR3Theorem.lean",
    "B_D": "NavierStokes/PeriodicPaperTheorem.lean",
}

IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)")
NAMESPACE_RE = re.compile(r"^\s*namespace\s+([A-Za-z0-9_.]+)")
END_NAMESPACE_RE = re.compile(r"^\s*end(?:\s+[A-Za-z0-9_.]+)?\s*$")
DECL_RE = re.compile(
    r"^\s*(?:(?:private|protected|scoped|noncomputable)\s+)*"
    r"(?:theorem|lemma|def|abbrev|opaque|axiom|structure|class|inductive|"
    r"instance|example)\s+([A-Za-z0-9_'.]+)"
)

KEYWORDS = (
    "Moment", "FiveRow", "Candidate", "GlobalFiniteEnergy", "Force",
    "Pressure", "Period", "tsum", "Energy", "Uniqueness", "Comparator",
)


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=repo, check=True, text=True,
        capture_output=True, encoding="utf-8",
    )
    return result.stdout


def source_files(repo: Path, commit: str) -> list[str]:
    raw = git(repo, "ls-tree", "-r", "--name-only", commit, "NavierStokes")
    return [line for line in raw.splitlines() if line.endswith(".lean")]


def module_name(path: str) -> str:
    return path[:-5].replace("/", ".")


def source_text(repo: Path, commit: str, path: str) -> str:
    return git(repo, "show", f"{commit}:{path}")


def imports(text: str) -> list[str]:
    return [m.group(1) for line in text.splitlines() if (m := IMPORT_RE.match(line))]


def module_sources(repo: Path, commit: str) -> dict[str, str]:
    return {module_name(path): source_text(repo, commit, path)
            for path in source_files(repo, commit)}


def import_closure(sources: dict[str, str], roots: Iterable[str]) -> tuple[set[str], dict[str, list[str]]]:
    edges: dict[str, list[str]] = {}
    closure: set[str] = set()
    pending = list(roots)
    while pending:
        current = pending.pop()
        if current in closure:
            continue
        if current not in sources:
            raise KeyError(f"source module not found in Git object: {current}")
        closure.add(current)
        deps = [dep for dep in imports(sources[current]) if dep in sources]
        edges[current] = sorted(set(deps))
        pending.extend(deps)
    return closure, edges


def declarations(module: str, text: str) -> list[str]:
    namespace: list[str] = []
    found: list[str] = []
    for line in text.splitlines():
        if match := NAMESPACE_RE.match(line):
            namespace.append(match.group(1))
            continue
        if END_NAMESPACE_RE.match(line) and namespace:
            namespace.pop()
            continue
        if match := DECL_RE.match(line):
            name = match.group(1)
            if "." in name:
                found.append(name)
            elif namespace:
                found.append(".".join(namespace + [name]))
            else:
                found.append(f"{module}.{name}")
    return found


def source_declaration_census(sources: dict[str, str], closure: set[str]) -> dict[str, object]:
    all_decls: list[str] = []
    per_module: dict[str, int] = {}
    for module in sorted(closure):
        names = declarations(module, sources[module])
        per_module[module] = len(names)
        all_decls.extend(names)
    return {
        "declaration_count": len(all_decls),
        "declaration_names": sorted(set(all_decls)),
        "declarations_per_module": per_module,
    }


def keyword_modules(sources: dict[str, str], closure: set[str]) -> dict[str, list[str]]:
    return {
        key: sorted(module for module in closure
                    if key.lower() in sources[module].lower())
        for key in KEYWORDS
    }


def load_environment(repo: Path, relative: str) -> dict[str, object] | None:
    path = repo / relative
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def environment_closure(payload: dict[str, object], root: str, full: bool) -> dict[str, object]:
    nodes = {node["name"]: node for node in payload["nodes"]}
    adjacency: dict[str, list[str]] = defaultdict(list)
    for edge in payload["edges"]:
        adjacency[edge["from"]].append(edge["to"])
    if root not in nodes:
        return {"root": root, "found": False}
    seen: set[str] = set()
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        queue.extend(adjacency.get(current, []))
    matched_keys = {
        key: sorted(name for name in seen if key.lower() in name.lower())
        for key in KEYWORDS
    }
    return {
        "root": root,
        "found": True,
        "declaration_count": len(seen),
        "keyword_counts": {key: len(names) for key, names in matched_keys.items()},
        "sorry_count": sum(1 for name in seen if nodes.get(name, {}).get("usesSorryAx")),
        **({"keyword_matches": matched_keys,
            "sorry_nodes": sorted(name for name in seen
                                   if nodes.get(name, {}).get("usesSorryAx"))}
           if full else {}),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--environment",
        default="NavierStokesReview/evidence/lean_environment_closure_ns_3d_2026-09-30.json",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="retain all source modules, edges, declaration names, and environment matches",
    )
    args = parser.parse_args()

    repo = args.repo.resolve()
    sources_a = module_sources(repo, COMMIT_A)
    sources_b = module_sources(repo, COMMIT_B)
    roots_a = ["NavierStokes.ComparatorR3Theorem", "NavierStokes.ComparatorTheorem"]
    roots_b = ["NavierStokes.ComparatorR3Theorem", "NavierStokes.PeriodicPaperTheorem"]
    closure_a, edges_a = import_closure(sources_a, roots_a)
    closure_b, edges_b = import_closure(sources_b, roots_b)
    census_a = source_declaration_census(sources_a, closure_a)
    census_b = source_declaration_census(sources_b, closure_b)
    env = load_environment(repo, args.environment)
    env_roots = [
        "NavierStokesR3.theorem_1_1",
        "NavierStokes.ComparatorBridge.navier_stokes_breakdown_R3",
        "NavierStokes.PeriodicPaper.periodic_corollary",
        "NavierStokes.ActualCandidateAssembly.selected_witness",
    ]

    source_a = {
        "roots": roots_a,
        "module_count": len(closure_a),
        "declaration_count": census_a["declaration_count"],
        "keyword_module_counts": {
            key: len(names) for key, names in keyword_modules(sources_a, closure_a).items()
        },
    }
    source_b = {
        "roots": roots_b,
        "module_count": len(closure_b),
        "declaration_count": census_b["declaration_count"],
        "keyword_module_counts": {
            key: len(names) for key, names in keyword_modules(sources_b, closure_b).items()
        },
    }
    if args.full:
        source_a.update({
            "modules": sorted(closure_a),
            "edges": edges_a,
            "declarations": census_a,
            "keyword_modules": keyword_modules(sources_a, closure_a),
        })
        source_b.update({
            "modules": sorted(closure_b),
            "edges": edges_b,
            "declarations": census_b,
            "keyword_modules": keyword_modules(sources_b, closure_b),
        })

    payload = {
        "schema": "navier-stokes-review/ab-declaration-closure/v1",
        "commits": {"A": COMMIT_A, "B": COMMIT_B},
        "routes": ROUTES,
        "source_layer": {
            "measurement": "immutable Git source import and declaration census",
            "limitation": "not an elaborated proof-term closure and not a semantic proof",
            "retained_detail": "full source graph is reproducible with --full and is not committed by default",
            "A": source_a,
            "B": source_b,
            "shared_modules": sorted(closure_a & closure_b),
            "A_only_modules": sorted(closure_a - closure_b),
            "B_only_modules": sorted(closure_b - closure_a),
        },
        "current_B_environment_layer": {
            "measurement": "elaborated Lean declaration-use closure from recorded JSON",
            "limitation": "declaration-use closure, not proof-term semantics or manuscript correspondence",
            "environment_path": args.environment,
            "roots": [environment_closure(env, root, args.full) for root in env_roots] if env else [],
            "available": env is not None,
            "retained_detail": "full environment matches are retained only with --full",
        },
        "interpretation_guardrails": [
            "A/B source closure differences do not prove A false or B correct.",
            "A/B shared declarations are candidates for common-core auditing, not automatically mathematical dominators.",
            "Keyword matches locate audit targets and do not establish that a theorem consumes a physical observable.",
            "The selected five-observable bridge remains CTR-005: NOT ESTABLISHED until its exact selected values are connected.",
            "Internal repair-engine consumption remains a positive finding and must not be relabelled as bypassed wholesale.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "A_modules": len(closure_a),
        "B_modules": len(closure_b),
        "shared_modules": len(closure_a & closure_b),
        "A_only_modules": len(closure_a - closure_b),
        "B_only_modules": len(closure_b - closure_a),
        "output": str(args.output),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
