# Priority 171: selected observable type boundary

Date: 2026-09-29
Status: source-bound P2 progress; no selected-field defect claimed.

The production source defines the selected endpoint from actual `potentialSum`
terms, mixed Cartesian curl/localisation, periodisation, and time activation:
`ActualCandidateAssembly.lean:1121-1151`, `SolenoidalDiagonal.lean:31-67`,
`SpatialLocalization.lean:164-217`, and `MixedPeriodicAssembly.lean:32-49`.
The cutoff-gradient commutator is explicit in
`SpatialLocalization.lean:199-207`.

The observable boundary is different. `DefectIncrementBounds.lean:22-25`
defines `Point P := PressureStream.Lift P` and `ScalarField D :=
MeanIncrementBounds.Field D`. Its `barMoment` at `:214-220` is

```lean
barMoment k f n p =
  ∫ r, r ^ k * PressureStream.torusAverage (f n) (r, p)
```

The `Witness` endpoint instead supplies activated Cartesian velocity, pressure,
and force. The source therefore requires an explicit scalar/component pullback,
convergence, support and integrability proof, and equality through the
completed sum, curl, localisation, periodisation, averaging, radial integral,
and axis extension before `barMoment` can be identified with the manuscript's
\((M,I,J,S,C_p)\).

This is a positive type/domain finding about the missing bridge. It is not a
proof of a selected nonzero defect or an impossibility theorem.

Status:

- selected `tsum`/curl/localisation/periodisation route: established;
- invariant-backed residual-rate and smooth-force route: established;
- selected Cartesian equality with the five paper observables: not established;
- selected defect, literal CMI failure, or Lean contradiction: not proved.
