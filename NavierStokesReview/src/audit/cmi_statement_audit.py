"""Static CMI-facing audit of the exported Lean statement path.

This is deliberately a source audit, not a proof checker. It records the
exact declarations and clauses that must be compared with Clay's alternatives
(C) and (D), and reports whether the expected source markers are present.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


FILES = {
    "comparator_definitions": ROOT / "NavierStokes" / "ComparatorDefinitions.lean",
    "r3_problem": ROOT / "NavierStokes" / "R3" / "ProblemStatement.lean",
    "r3_bridge": ROOT / "NavierStokes" / "R3" / "ComparatorBridge.lean",
    "r3_uniqueness": ROOT / "NavierStokes" / "R3" / "WholeSpaceUniqueness.lean",
    "compact_force_decay": ROOT / "NavierStokes" / "CompactSpatialForceDecay.lean",
    "exported_solution": ROOT / "NavierStokes" / "ComparatorSolution.lean",
    "periodic_solution": ROOT / "NavierStokes" / "PeriodicPaperComparator.lean",
    "periodic_statement": ROOT / "NavierStokes" / "PeriodicPaperTheorem.lean",
    "periodic_adapter": ROOT / "NavierStokes" / "PeriodicComparatorSolution.lean",
}


REQUIRED_MARKERS = {
    "comparator_definitions": [
        "InitialVelocityConditionDecay",
        "ForceConditionDecay",
        "NavierStokesExistenceAndSmoothnessRn",
        "globally_bounded_energy",
    ],
    "r3_problem": [
        "CandidateProperties",
        "GlobalFiniteEnergySolution",
        "energy_bounded",
        "speed_unbounded",
    ],
    "r3_bridge": [
        "forceConditionDecay_of_compact",
        "globalSolutionOfComparator",
        "comparator_of_breakdown",
    ],
    "r3_uniqueness": [
        "candidate_global_agrees_before_one",
        "No growth, decay, support or derivative bound",
    ],
    "compact_force_decay": [
        "iteratedFDerivWithin",
        "futureDomain",
        "forceConditionDecay",
    ],
    "exported_solution": [
        "navier_stokes_breakdown_R3",
        "navier_stokes_breakdown_periodic",
        "#print axioms",
    ],
    "periodic_solution": [
        "GlobalSmoothSolution",
        "forceConditionPeriodic",
    ],
    "periodic_statement": [
        "GlobalSmoothSolution",
        "pressure_periodic",
    ],
    "periodic_adapter": [
        "pressure_periodic :=",
        "NavierStokesExistenceAndSmoothnessPeriodic",
    ],
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    records = []
    for key, path in FILES.items():
        text = path.read_text(encoding="utf-8")
        records.append(
            {
                "key": key,
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": digest(path),
                "line_count": len(text.splitlines()),
                "markers": {
                    marker: (marker in text)
                    for marker in REQUIRED_MARKERS[key]
                },
            }
        )

    output = ROOT / "NavierStokesReview" / "evidence" / "cmi_statement_audit.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(
            {
                "repository_root": str(ROOT),
                "kind": "static-source-audit",
                "note": "Marker presence is evidence for review navigation, not semantic validation.",
                "files": records,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"output": str(output), "files": len(records)}, indent=2))


if __name__ == "__main__":
    main()
