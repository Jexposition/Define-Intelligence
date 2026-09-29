"""Produce compact, line-addressed summaries for a fixed Lean source tranche.

This is a navigation aid, not a proof and not a semantic absence detector.  It
records imports, declarations, exact keyword locations, and sorry tokens so a
reviewer can open the source at the cited lines and inspect the proof bodies.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_FILES = [
    "R3PressureNearKernel.lean",
    "R3PressureKernel.lean",
    "R3SmoothPressure.lean",
    "LocalHeatFormula.lean",
    "NaturalAxisJointAnalytic.lean",
    "InitialHarmonicContinuation.lean",
    "LocalPotentialRebundle.lean",
    "PeriodizePDE.lean",
    "ComparatorR3Theorem.lean",
    "ComparatorTheorem.lean",
    "LocalPaperTheorem.lean",
    "R3/ParabolicSupport.lean",
    "SharpGluedStageBounds.lean",
    "SharpParticularGluing.lean",
    "WholeDomainInitializationBounds.lean",
]

KEYWORDS = (
    "moment",
    "barMoment",
    "FiveRows",
    "Debt",
    "curl",
    "period",
    "pressure",
    "support",
    "NativeBounds",
    "StageEstimates",
    "tsum",
    "residual",
    "force",
    "CandidateProperties",
    "Witness",
    "selected_witness",
    "poisson",
    "Leray",
    "sorry",
)

DECL_RE = re.compile(
    r"^(?P<kind>theorem|lemma|def|abbrev|structure|class|inductive|axiom|instance)\b"
)


def declaration_lines(lines: list[str]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        match = DECL_RE.match(stripped)
        if match:
            rows.append({"line": number, "kind": match.group("kind"), "text": stripped})
    return rows


def summarise(root: Path, relative: str) -> dict[str, object]:
    path = root / relative
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    hits = {
        keyword: [number for number, line in enumerate(lines, start=1) if keyword.lower() in line.lower()]
        for keyword in KEYWORDS
        if any(keyword.lower() in line.lower() for line in lines)
    }
    return {
        "file": relative,
        "bytes": path.stat().st_size,
        "lines": len(lines),
        "imports": [line.strip() for line in lines if line.strip().startswith("import ")],
        "declarations": declaration_lines(lines),
        "keyword_lines": hits,
        "sorry_token_lines": hits.get("sorry", []),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("files", nargs="*", default=DEFAULT_FILES)
    args = parser.parse_args()

    rows = [summarise(args.root, relative) for relative in args.files]
    payload = {
        "tool": "source_tranche_summary.py",
        "scope": "source navigation only; not a theorem prover or absence detector",
        "root": str(args.root),
        "files": rows,
        "file_count": len(rows),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
