# Selected active-pair reachability

## Result

`NavierStokesReview/src/audit/SelectedActivePairReachability.lean` compiles
without `sorry`, `axiom`, or `unsafe` declarations. It proves that every
concrete `ActualPrimary.Label B N0` supplies an inhabited
`ActualParticularStageControls.ActivePair B N0`.

The proof uses the source definitions rather than the existence of a later
stage estimate:

1. `PrimaryGeometryAssembly.four_le_threshold` gives
   $$4 \leq (\mathrm{choice}\ B\ N0).\mathrm{prepared}.N.$$
2. The subtype property of a selected label gives
   $$N \leq \mathrm{cellBand}(L).$$
3. Hence the selected band is positive.
4. `CommonWindow.self_mem` places that band in its own level window, so
   `(L, cellBand L)` is an `ActivePair`.

## Vacuity boundary

This does not, by itself, produce a selected label. The source type
`ActualPrimary.Label B N0` is a subtype of positive mask labels, and the
review theorem deliberately retains a separate conditional result when that
label type is merely assumed nonempty. Consequently, the empty branch in
`ActualParticularStageControls.raw_jets` cannot be called a selected-path
vacuity exploit on the evidence currently available. Any stronger claim
requires a theorem about inhabitance of the selected label subtype or a
concrete false property of the selected field.

## Source coordinates

- `NavierStokes/BaseChartJets.lean:825-827`: `CellIndex` and its lower-band
  subtype property.
- `NavierStokes/PrimaryGeometryAssembly.lean:496`: four-band lower bound.
- `NavierStokes/CorrectionInitialization.lean:3757-3762`:
  `CommonWindow.levels` and `self_mem`.
- `NavierStokes/ActualParticularStageControls.lean:442-445`: `Active` and
  `ActivePair`.
- `NavierStokes/ActualParticularStageControls.lean:941-958`: the explicit
  nonempty/empty split in `raw_jets`.

## Classification

The empty-`ActivePair` branch is a real source branch, but it is not a proved
selected-witness contradiction. The audit therefore closes only the claim
that this branch can be treated as evidence of vacuous selected execution
without first proving that the selected label type is empty.

