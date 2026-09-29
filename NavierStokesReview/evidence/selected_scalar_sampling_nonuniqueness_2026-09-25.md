# Raw scalar sampling non-uniqueness

**Date:** 2026-09-25  
**Classification:** selected interface evidence; not a selected nonzero moment and not `False`  
**Build:** `lake build NavierStokesReview` passed, 3718 jobs; the added completion contains no `sorry`, custom axiom, or `unsafe`.

## Source path

`ActualMeanPhysicalData.Scalar` is the raw type

```text
ℕ → Point → ℝ
```

at `NavierStokes/ActualMeanPhysicalData.lean:24-26`. The production field is
sampled through `PhysicalMeanJetBounds.physicalPoint` in
`NavierStokes/ActualCandidateConstruction.lean:358-361`.

`SelectedTorusLiftImageScope.lean:84-105` proves that the production map
misses `unreachablePhysicalPoint`. The new completion
`NavierStokesReview/src/completions/SelectedScalarSamplingNonuniqueness.lean:22-58`
defines

```text
offImageFamily n z := if ρ z.2.2 < 0 then 1 else 0
```

and proves two facts:

1. `offImageFamily` is zero at every `physicalPoint h w`.
2. `offImageFamily` is one at the explicit missed point.

Therefore the map

```text
ScalarFamily → (ℕ → SpaceTime → ℝ)
f ↦ (fun n w => f n (physicalPoint h w))
```

is not injective at the plain scalar-family level.

## Audit consequence

The production pullback cannot, by sampling alone, identify the complete raw
scalar family integrated by `torusAverage` and `barMoment`. A selected proof
still could close this gap by proving uniqueness in the actual smooth,
overlap, support, and chart class. This completion does not show that the
selected raw family takes a nonzero value on the missed region, does not
evaluate `barMoment`, and does not derive `Δm ≠ 0` or `False`.

The next controlled target is therefore a selected regularity-class
uniqueness theorem, followed by the actual weighted integral if uniqueness is
not available.
