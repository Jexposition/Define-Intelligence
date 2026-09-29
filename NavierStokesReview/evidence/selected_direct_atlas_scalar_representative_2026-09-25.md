# Selected direct atlas scalar representative

Date: 2026-09-25

`SelectedDirectAtlasScalarRepresentative.lean` names the scalar family obtained
from `ActualMeanPhysicalData.Atlas.physical` at the physical point used by
`ActualCandidateConstruction.meanField`. Its domain is the lifted point type
consumed by `DefectIncrementBounds.barMoment`.

The zero-sorry completion proves three selected-path identities:

1. `meanField` is definitionally equal to the atlas scalar pulled back through
   `PhysicalMeanJetBounds.physicalPoint`.
2. `barMoment_apply` expands the selected scalar moment to the stated radial
   integral of `PressureStream.torusAverage`.
3. On the positive-radius radial section, component one of the selected direct
   stage equals that atlas scalar at the corresponding physical point.

Focused build command:

```powershell
& 'C:\Users\Admin\.elan\bin\elan.exe' run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedDirectAtlasScalarRepresentative.lean
```

Result: exit code 0, with no `sorry` and no `unsafe` in the completion.

This is an exact transport result. It does not identify the mixed selected
field with the direct scalar, evaluate the selected `barMoment`, prove a
nonzero remainder `Δm`, or derive `False`.
