# Selected scalar radial-moment transport

## Result

The review-side completion
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`
now proves, for every selected cycle stage and every point in the carrier,

```lean
DefectIncrementBounds.barMoment 2
  (selectedCycle j).state.mean.angular n s = 0

DefectIncrementBounds.barMoment 1
  (selectedCycle j).state.mean.axial n s = 0
```

These statements compile without `sorry`, `axiom`, or `unsafe`. The proof is
not a new analytic assumption: `DefectIncrementBounds.barMoment` is defined as
`CorrectionState.radialMoment`, and the result is obtained from the actual
`CycleAnalyticInvariant.masses` field.

## What this proves

It closes the proposed claim that the selected scalar correction/state path
loses its two local radial moments during iteration. It also shows that a
nonzero scalar `barMoment` contradiction cannot be obtained from the selected
cycle state alone.

## What it does not prove

The result is not yet a moment identity for the final exported Cartesian
velocity. `selectedDirectStages` applies the scalar through the physical atlas,
the angular frame, localisation, and later curl construction. The remaining
question is whether those operations preserve the same radial quantity or
introduce an explicit boundary/cutoff term. That field-level calculation is
still required before a nonzero selected `Delta m` can be claimed.

Build result: `lake build NavierStokesReview` passed with 3697 jobs using
Lean `v4.34.0-rc2`.
