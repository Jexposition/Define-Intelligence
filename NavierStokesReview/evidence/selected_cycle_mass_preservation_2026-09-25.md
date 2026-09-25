# Selected cycle mass preservation

## Result

The selected recurrence is definitionally the same recurrence covered by the
actual cycle-preservation theorem. The review-side theorem
`NavierStokesReview.SelectedCycleMasses.selected_cycle_zeroMasses` compiles
without `sorry`, `axiom`, or `unsafe` and proves, for every stage `j`,

```lean
GaugeMassPreservation.ZeroMassesOn
  ActualInitialization.geometry.region.carrier
  (ActualCandidateConstruction.selectedCycle j).state
```

## Source ledger

| Source | Lines | Role |
|---|---:|---|
| `ActualCandidateConstruction.lean` | 35-42 | Defines `cycle` as the fixed-parameter `CycleState.iterate`. |
| `ActualCandidateConstruction.lean` | 212-214 | Defines `selectedCycle` as the selected `cycle`. |
| `ActualCyclePreservation.lean` | 149-159 | Defines the preserved `state` recurrence. |
| `ActualCyclePreservation.lean` | 826-838 | `state_runInvariant` and `state_invariant` carry the analytic invariant through every stage. |
| `CorrectionStep.lean` | 9408-9449 | `CycleAnalyticInvariant.masses` is an explicit `ZeroMassesOn` field. |
| `GaugeMassPreservation.lean` | 140-142 | Defines `ZeroMassesOn` as two radial moments of the mean state. |
| `NavierStokesReview/src/completions/SelectedCycleMasses.lean` | 20-29 | Source-level selected-path theorem. |

## Audit consequence

This closes one proposed attack in its advertised form: the active correction
cycle does not merely assume the two zero rows at stage zero; it carries the
corresponding mean-state radial identities through the selected recurrence.
It does not prove that the final Cartesian `VelocityField` exported by
`selected_witness` has the same `barMoment` values. That remaining calculation
must still pass through the mean-field map, angular vector, curl, cutoffs,
torus average, and boundary terms.

Build result: `lake build NavierStokesReview` passed with 3696 jobs using
Lean `v4.34.0-rc2`.
