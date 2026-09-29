# Selected positive-potential chart component

## Result

`NavierStokesReview/src/completions/SelectedPotentialChartComponent.lean`
compiles without `sorry`, a custom `axiom`, or `unsafe` declarations.  It
specialises the production selected field rather than a toy replacement.

For every valid positive-radius chart point and every successor stage, the
first Cartesian component satisfies

$$
\bigl(\operatorname{curl}(A_{j+1})\bigr)_1
 = \bigl(\operatorname{chartPotentialParts}_{j+1}\bigr)_1
 = \bigl(\operatorname{chartWaveParts}_{j+1}\bigr)_1
   + \bigl(\operatorname{chartStreamParts}_{j+1}\bigr)_1.
$$

The first equality is obtained from the production theorem
`positivePotential_on_chart`; the second is the source recurrence
`chartPotentialParts_succ`.  The completion therefore confirms that the
selected wave and stream terms enter the same production chart component.

## Source anchors

| Item | Location | Meaning |
|---|---|---|
| selected completion | `NavierStokesReview/src/completions/SelectedPotentialChartComponent.lean:26-42` | Selected curl component on the production chart. |
| stage unfolding | `SelectedPotentialChartComponent.lean:36-39` | Unfolds `selectedPotentialStages` and applies `potentialStages_succ`. |
| chart transport | `ActualCandidateAssembly.lean:1025-1035` | `positivePotential_on_chart` supplies the field equality. |
| component extraction | `SelectedPotentialChartComponent.lean:40-42` | Applies `congrArg` to Cartesian component `1`. |
| wave/stream split | `ActualCandidateConstruction.lean:638-650` | `chartPotentialParts_succ` supplies the production decomposition. |

## What this establishes

The selected production field is not disconnected from the chart-level wave
and stream data at this component.  Any radial calculation must account for
both terms after the chart map, and must retain the cutoff-gradient
commutator already identified in
`selected_cutoff_curl_commutator_2026-09-25.md`.

## What remains open

This identity is local to a valid positive-radius chart and one Cartesian
component.  It does not identify the scalar field consumed by
`DefectIncrementBounds.barMoment_apply`, does not perform the torus average,
and does not evaluate axis, outer-support, or infinite-sum limits.  It
therefore proves neither `Delta m ≠ 0` nor `False`.

## Build record

Command: `lake build NavierStokesReview` under Lean `v4.34.0-rc2`.

Result: `Build completed successfully (3712 jobs).`
