# Selected atlas physical-map erasure

**Date:** 2026-09-25  
**Classification:** selected interface result; not a selected-field contradiction

## Result

`NavierStokesReview/src/completions/SelectedAtlasPhysicalErasure.lean`
compiles with no `sorry`, custom axiom, or `unsafe` declaration.  Its main
theorem is:

```lean
atlas_physical_congr_of_valid
```

For an atlas `A`, scalar families `f` and `g`, and a point `z`, if they agree
at every valid chart sample,

```text
∀ n z, A.Valid U z n →
  f n (A.chart n z) = g n (A.chart n z),
```

then `A.physical U degree f z = A.physical U degree g z`.

The proof follows the source definition at
`NavierStokes/ActualMeanPhysicalData.lean:125-131`: when a valid band exists,
`Atlas.physical` evaluates one chosen valid chart sample; when none exists, it
returns zero.  The theorem therefore formalises exactly which native scalar
values the selected physical map can observe.

## Consequence for the moment audit

The production map in
`NavierStokes/ActualCandidateConstruction.lean:355-366` evaluates
`Atlas.physical` at `PhysicalMeanJetBounds.physicalPoint`.  By contrast,
`barMoment` is defined in `NavierStokes/DefectIncrementBounds.lean:214-220`
as an integral of a scalar family after `PressureStream.torusAverage`.

Thus the following implication is not available from the current source:

```text
agreement on valid chart samples
  ⇒ equality of the full native-family barMoment integral.
```

That implication requires a further selected transport theorem showing that
the torus-average integration domain is covered by valid chart samples, or
that the unobserved values contribute zero.  The result is a precise
transport obligation, not a proof that the selected endpoint is inconsistent.

## Verification command

```powershell
& 'C:\Users\Admin\.elan\bin\elan.exe' run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedAtlasPhysicalErasure.lean
```

Result: exit code `0`.
