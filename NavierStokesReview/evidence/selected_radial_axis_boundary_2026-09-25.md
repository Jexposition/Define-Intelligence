# Selected radial-axis boundary result

**Date:** 2026-09-25  
**Review target:** the selected direct angular stage, not a generic proxy  
**Lean module:** `NavierStokesReview/src/completions/SelectedRadialAxisBoundary.lean`

## Result

The review-side module compiles with no `sorry`, custom `axiom`, or `unsafe`
declaration. It proves two exact source consequences:

1. `meanAngularField_axis_component_one` shows that the component with index
   `1` of the actual angular field is zero whenever the two radial Cartesian
   coordinates are both zero.
2. `selected_direct_stage_axis_component_one` transports that result to every
   selected direct stage.

The proof unfolds the production definitions. `meanAngularField` is scalar
`meanField` multiplied by `PhysicalMeanJetBounds.angularVector`; the latter is
defined by the two coordinate divisions in
`NavierStokes/PhysicalMeanJetBounds.lean:518-520`. At the axis both numerators
are zero, and Lean's total real division gives the zero component.

## Boundary interpretation

The positive-radius theorem in
`NavierStokesReview/src/completions/SelectedRadialSectionComponent.lean:22-30`
recovers component `1` as the scalar coefficient under `0 < r`. The new theorem
supplies the separate axis branch. This is a genuine boundary decomposition,
not a proof that the field is discontinuous: no radial limit theorem, derivative
matching theorem, or nonzero moment has yet been established.

The result also does not identify the full curl-generated selected velocity with
`DefectIncrementBounds.barMoment`. The remaining calculation must still include
the meridional component, cutoff derivatives, torus average, outer support, and
the exact scalar projection used by `barMoment_apply`.

## Source anchors

- `NavierStokes/ActualCandidateConstruction.lean:363-366` — production
  `meanAngularField` definition.
- `NavierStokes/PhysicalMeanJetBounds.lean:518-520` — totalised angular frame.
- `NavierStokesReview/src/completions/SelectedRadialAxisBoundary.lean:22-30` —
  axis component theorem.
- `NavierStokesReview/src/completions/SelectedRadialAxisBoundary.lean:32-42` —
  selected-stage transport.
- `NavierStokes/DefectIncrementBounds.lean:214-220` — scalar radial moment
  operator and its integral expansion.

## Verification

Command:

```text
lake build NavierStokesReview
```

Result: `Build completed successfully (3701 jobs)` with the repository-pinned
Lean `v4.34.0-rc2` toolchain.

No `Delta m ≠ 0` or kernel-level `False` follows from this result alone.
