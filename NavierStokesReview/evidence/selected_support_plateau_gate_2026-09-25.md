# Selected support versus cutoff plateau

**Date:** 2026-09-25  
**Classification:** selected-field calculation gate; no contradiction established

## Question

The production direct branch is multiplied by `SpatialLocalization.spatialCutoff`.
The native direct moment cannot be transferred to the production branch unless
the selected support is proved to lie in the region where that cutoff equals
one.

## Source definitions

1. `NavierStokes/MixedDiagonalExtensions.lean:99-102` defines
   `SublevelShrinkingSupport h C qbig f` by
   ```lean
   ∀ w, w.1 < 1 → PhysicalWaveSum.physicalQ h w < qbig →
     f w ≠ 0 → AnnularEndpoint.radius w ≤ AnnularEndpoint.outerRadius h C w
   ```
2. `NavierStokes/AnnularEndpoint.lean:27-28,46-48` defines the two quantities
   as the physical radial distance and
   ```lean
   C * Real.sqrt (PhysicalWaveSum.physicalQ h w).
   ```
3. `NavierStokes/CutStageEstimates.lean:672-673` defines the local validity
   region using `physicalQ h w < qbig`.
4. `NavierStokes/ActualCandidateConstruction.lean:155-190` defines `qbig`
   and the selected physical domain, but does not identify that domain with
   the Cartesian cutoff plateau.
5. `NavierStokes/ActualCandidateConstruction.lean:882-885` proves the
   selected angular stages satisfy `SublevelShrinkingSupport`.
6. `NavierStokes/SpatialLocalization.lean:133-147` defines the cutoff plateau
   by the separate conditions
   ```lean
   radialSquare x < 1 / 32 ∧ |x 2| < 1 / 8
   ```
   and proves `spatialCutoff x = 1` there.

## Consequence

The support predicate controls a similarity-radius quantity.  The plateau
predicate controls Cartesian coordinates.  The inspected source contains no
theorem transporting the selected `SublevelShrinkingSupport` bound into the
two plateau inequalities.  Therefore the native direct `barMoment` zero
cannot be substituted for the cutoff-weighted production moment.

This is a precise unresolved transport obligation under CTR-005 and CALC-20.
It is not evidence that the cutoff-weighted moment is nonzero, and it does not
yield `False` without a selected pointwise or integral calculation.

## Required next theorem

Prove, for the selected direct field, either

```text
selected support → SpatialLocalization.plateau
```

or an explicit selected value for the weighted term

```text
barMoment k (fun z => SpatialLocalization.spatialCutoff z.2 • direct z).
```

The second branch must retain the cutoff and its torus-average boundary
terms.
