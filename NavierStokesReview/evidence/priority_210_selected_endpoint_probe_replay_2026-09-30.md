# Priority 210: selected-endpoint probe replay

Date: 2026-09-30
Status: compiled and source-calibrated
Scope: review-side probes against the selected Navier--Stokes endpoint

## Purpose

This tranche replays the selected-path probes after reconciling the current
source register and materialising a missing project dependency. It records
what the kernel checks and what the propositions do not entail. It does not
promote a type-level non-entailment into a selected-field defect.

## Environment and commands

Repository: `Define-Intelligence-github`

Toolchain: `leanprover/lean4:v4.34.0-rc2`

Initial command:

```text
lake env lean NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean
```

Initial result: the lake cache lacked
`NavierStokes.LocalScheduleWitness.olean`. This was a build-cache condition,
not a theorem result. The repository utility
`NavierStokesReview/src/audit/direct_lean_closure.py` was then run with:

```text
python NavierStokesReview/src/audit/direct_lean_closure.py NavierStokes.LocalScheduleWitness --workers 1
```

The closure completed successfully and compiled `NavierStokes.LocalScheduleWitness`.
The four target probes were then replayed with `lake env lean`.

## Replay results

| Probe | Result | What it establishes |
|---|---|---|
| `SelectedMomentBridgeAudit.lean` | exit 0 | The endpoint exposes `Witness`, `FiveRowRank.FiveRows`, and `PositiveOrderMoments.moments`; the checked `Witness` result type has no displayed final five-observable equality. |
| `SelectedWitnessPathProbe.lean` | exit 0 | Selected periodic/R3 properties coexist with an explicitly constructed abstract nonzero `Debt`; this is a contract non-entailment result, not a claim about the selected physical integrals. |
| `SelectedWitnessEndpointResidualProbe.lean` | exit 0 | The selected path proves axis speed blow-up and original-residual decay; the probe itself records that a positive residual lower bound would be additionally required for a contradiction. |
| `SelectedForceOriginCompositionProbe.lean` | exit 0 | At the origin, periodic residual equals original residual and the selected force has the recorded zero-limit route. |
| `SelectedDependencyAxiomProbe.lean` | exit 0 | `selected_witness`, `physicalData`, `actualStageEstimates`, and `residual_jetRate` report only `propext`, `Classical.choice`, and `Quot.sound`. |

## Source interpretation

The replay confirms the positive selected construction already recorded in
Priorities 202--205: actual cycle invariants, physical data, residual-rate
estimates, force extension, and the axis blow-up route are connected on the
selected path. It also confirms the bounded `CTR-005` finding: the reviewed
production export does not expose a theorem identifying the completed
selected Cartesian observables with the manuscript tuple
`(M,I,J,S,C_p)`.

The following stronger claims remain unsupported by this replay:

- the selected physical field has a nonzero five-moment defect;
- the selected residual force is nonsmooth;
- the literal Fefferman forced alternative fails;
- the repository contains a compiler escape or contradiction;
- the five-moment mechanism is the only possible cancellation route;
- the endpoint proves `False`.

The correct status remains `CTR-005: NOT ESTABLISHED` for complete
manuscript-to-selected-endpoint correspondence. The positive internal
transport and the unexported final observable identification must both remain
visible in later reports.

## Reproducibility anchors

- `NavierStokesReview/src/probes/SelectedMomentBridgeAudit.lean`
- `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean`
- `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean`
- `NavierStokesReview/src/probes/SelectedForceOriginCompositionProbe.lean`
- `NavierStokesReview/src/probes/SelectedDependencyAxiomProbe.lean`
- `NavierStokesReview/src/audit/direct_lean_closure.py`
- `NavierStokes/ActualCandidateAssembly.lean:1079-1151,1177-1185`
- `NavierStokes/ActualCyclePreservation.lean:826-828`
- `NavierStokes/ActualCycleResidualBounds.lean:1156-1172`
- `NavierStokes/CandidateFromLimits.lean:45-112`
- `NavierStokes/GermCandidateAssembly.lean:146-271`
