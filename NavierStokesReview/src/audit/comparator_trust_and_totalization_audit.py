"""Targeted trust-boundary and totalisation audit for the Navier--Stokes checkout.

This is deliberately not a proof checker and must not be reported as one.  It
records three source-level questions that are easy to conflate:

1. Does the Comparator challenge contain admitted placeholder bodies?
2. Does the submitted solution import or reference that challenge module?
3. Where do selected-route declarations use noncomputable choice, conditional
   fallbacks, extensions, or other totalising constructions that require a
   semantic follow-up?

The output is an auditable index with exact files and line numbers.  It is a
triage instrument for the declaration/proof-term and semantic audits, not an
AST proof of absence and not evidence of a compiler escape.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


TRUST_PATTERNS: dict[str, re.Pattern[str]] = {
    "sorry_token": re.compile(r"\bsorry\b"),
    "unsafe_declaration": re.compile(r"\bunsafe\s+(?:def|theorem|abbrev|opaque)\b"),
    "partial_declaration": re.compile(r"\bpartial\s+(?:def|theorem)\b"),
    "opaque_declaration": re.compile(r"\bopaque\s+(?:def|theorem)\b"),
    "implemented_by": re.compile(r"implemented_by"),
    "extern_attribute": re.compile(r"\[\s*extern\b"),
    "native_decide": re.compile(r"\bnative_decide\b"),
    "of_reduce_bool": re.compile(r"\bLean\.ofReduceBool\b"),
    "run_tac": re.compile(r"\brun_tac\b"),
    "custom_axiom": re.compile(r"^\s*axiom\s+"),
}

TOTALISATION_PATTERNS: dict[str, re.Pattern[str]] = {
    "noncomputable_declaration": re.compile(r"^\s*noncomputable\s+(?:def|abbrev|instance)\b"),
    "classical_choice": re.compile(r"\b(?:Classical\.choice|Exists\.choose|Classical\.epsilon)\b"),
    "conditional_branch": re.compile(r"\b(?:if|dite)\s+h?\s*:"),
    "function_extend": re.compile(r"\bFunction\.extend\b"),
    "nonempty_some": re.compile(r"\bNonempty\.some\b"),
    "sinf_ssup": re.compile(r"\b(?:sInf|sSup)\b"),
    "filter_bot": re.compile(r"\bFilter\.bot\b"),
}


@dataclass(frozen=True)
class Hit:
    category: str
    path: str
    line: int
    text: str


def iter_lean_files(root: Path) -> Iterable[Path]:
    yield from sorted((root / "NavierStokes").rglob("*.lean"))
    yield from sorted((root / "ComparatorChallenges").rglob("*.lean"))


def scan_file(path: Path, root: Path) -> list[Hit]:
    hits: list[Hit] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return hits
    relative = path.relative_to(root).as_posix()
    for number, raw in enumerate(lines, 1):
        # Keep this conservative: comments are retained and therefore flagged
        # for review rather than silently classified as declarations.
        text = raw.strip()
        for category, pattern in TRUST_PATTERNS.items():
            if pattern.search(raw):
                hits.append(Hit(category, relative, number, text))
        for category, pattern in TOTALISATION_PATTERNS.items():
            if pattern.search(raw):
                hits.append(Hit(category, relative, number, text))
    return hits


def find_module_config(root: Path) -> dict[str, object]:
    candidates = [root / "lakefile.toml", root / "lakefile.lean", root / "lean-toolchain"]
    rows: list[dict[str, object]] = []
    for path in candidates:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for term in ("ComparatorChallenges.NavierStokes", "NavierStokes.ComparatorSolution"):
            lines = [i for i, line in enumerate(text.splitlines(), 1) if term in line]
            if lines:
                rows.append({"term": term, "path": path.relative_to(root).as_posix(), "lines": lines})
    return {"configuration_hits": rows}


def challenge_solution_rows(root: Path) -> dict[str, object]:
    challenge = root / "ComparatorChallenges" / "NavierStokes.lean"
    solution = root / "NavierStokes" / "ComparatorSolution.lean"
    result: dict[str, object] = {}
    for label, path in (("challenge", challenge), ("solution", solution)):
        if not path.exists():
            result[label] = {"exists": False}
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        result[label] = {
            "exists": True,
            "path": path.relative_to(root).as_posix(),
            "imports": [
                {"line": i, "text": line.strip()}
                for i, line in enumerate(lines, 1)
                if line.lstrip().startswith("import ")
            ],
            "headline_declarations": [
                {"line": i, "text": line.strip()}
                for i, line in enumerate(lines, 1)
                if "navier_stokes_breakdown" in line
            ],
            "sorry_lines": [i for i, line in enumerate(lines, 1) if re.search(r"\bsorry\b", line)],
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--selected-only", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    files = list(iter_lean_files(root))
    if args.selected_only:
        selected_names = {
            "ActualCandidateAssembly.lean",
            "ActualCandidate.lean",
            "Theorem.lean",
            "ComparatorBridge.lean",
            "ComparatorR3Theorem.lean",
            "ComparatorTheorem.lean",
            "PeriodicPaperTheorem.lean",
            "PeriodicPaperComparator.lean",
            "LocalPaperTheorem.lean",
            "PaperLocalization.lean",
            "JointResidualLimits.lean",
            "ValidBandGluing.lean",
            "SmoothPathFamily.lean",
            "PreparedOutgoing.lean",
            "CompactSmoothFamily.lean",
        }
        files = [path for path in files if path.name in selected_names or "ComparatorChallenges" in path.parts]
    hits = [hit for path in files for hit in scan_file(path, root)]
    payload = {
        "schema": "ns-comparator-trust-totalization-audit/v1",
        "scope": "selected-route source triage; not AST closure and not a kernel proof",
        "root": str(root),
        "files_scanned": len(files),
        "configuration": find_module_config(root),
        "challenge_solution": challenge_solution_rows(root),
        "counts": {
            "trust_boundary_hits": sum(hit.category in TRUST_PATTERNS for hit in hits),
            "totalisation_hits": sum(hit.category in TOTALISATION_PATTERNS for hit in hits),
            "files_with_hits": len({hit.path for hit in hits}),
        },
        "hits": [asdict(hit) for hit in hits],
        "interpretation": {
            "challenge_sorry": "A challenge placeholder is not evidence that the submitted solution has a sorry dependency.",
            "solution_dependency": "Must be established by import/proof-term/Comparator checks; this lexical report only records source-level evidence.",
            "totalisation": "Each fallback, choice, extension, or noncomputable constructor requires a same-object and branch-validity follow-up.",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"files_scanned": len(files), "counts": payload["counts"], "output": str(args.output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
