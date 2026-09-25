# Selected direct-stage chart transport

## Source result

`NavierStokesReview/src/completions/SelectedDirectPrefixField.lean` now proves
`selected_direct_stage_eq_chart`. For the selected budget and threshold, every
selected direct stage agrees on an admissible positive-radius chart with the
corresponding `chartDirectStages` field.

The proof uses the source identities
`ActualCandidateAssembly.lean:553-556`, which identify `directStages` with
`ActualCandidateConstruction.angularMeanStages`, and
`ActualCandidateConstruction.lean:561-572`, which transport the angular mean
stage through the atlas chart.

For the potential branch, the assembly order is explicit in
`SolenoidalDiagonal.lean:31-38,182-188,252-266`: `scaledCutoff` is applied to
each stage before the `tsum`, and `velocitySum` is the spatial curl of the
summed potential. The local finiteness theorem then reduces the velocity to a
finite sum of curls. The chart-level curl transport is stated in
`ActualMeanPotentialRealization.lean:245-252`.

This order answers two audit questions. The correction/state zero rows are
proved before this vector-valued cutoff/curl assembly; they are not identities
for the final Cartesian field. Conversely, the source does not justify a
nonzero remainder merely from that ordering: the cutoff derivatives and curl
terms still have to be evaluated for the selected field.

## Boundary of the result

This is a genuine selected-path transport identity, but it is only a
positive-radius chart statement. It does not extend the chart across the axis,
does not expand the Cartesian curl, and does not identify the resulting vector
field with the scalar radial-profile input of `DefectIncrementBounds.barMoment`.
Consequently it neither proves nor disproves a nonzero selected `Delta m`.

The completion builds without `sorry`, `axiom`, or `unsafe` as part of
`lake build NavierStokesReview` (3697 jobs) under Lean `v4.34.0-rc2`.
