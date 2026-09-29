# Selected production direct atlas pullback

**Date:** 2026-09-25  
**Status:** source-backed selected-field identity  
**Claim class:** CTR-005 calculation evidence

## Result

The zero-sorry completion
`NavierStokesReview/src/completions/SelectedProductionDirectAtlasPullback.lean`
proves the selected direct component in two stages.

For every stage `j` and spacetime point `w`, the source identity
`ActualCandidateAssembly.directStages_eq` transports the selected direct
branch to `ActualCandidateConstruction.angularMeanStages`. Unfolding that
branch gives

$$
 D^{\mathrm{dir}}_{j,1}(w)=
 A^{\mathrm{phys}}\!\left(\operatorname{physicalPoint}(w)\right)
 \left(\operatorname{angularVector}(\operatorname{radialProjection}(w))\right)_1,
$$

where the atlas is
`meanAtlas selectedBudget selectedThreshold`, the chart carrier is
`ActualPrimary.standardRegion.carrier`, and the degree is
`CoordinateAlgebra.A ActualPrimary.h`.

The second theorem applies `SpatialLocalization.cutPotential`. Therefore the
component exported by the production direct branch is

$$
 \bigl(\operatorname{cutPotential}(D^{\mathrm{dir}}_j)(w)\bigr)_1
 =\operatorname{spatialCutoff}(w.2)\,
 A^{\mathrm{phys}}(\operatorname{physicalPoint}(w))
 \left(\operatorname{angularVector}(\operatorname{radialProjection}(w))\right)_1.
$$

On `ActualMeanStageData.radialSection p`, the previous scalar gate expands
the cutoff to

$$
 \chi(r,z)=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z).
$$

## Source anchors

| Component | Source |
|---|---|
| Selected direct definition | `NavierStokes/ActualCandidateAssembly.lean:536-538` |
| Direct-to-native transport | `NavierStokes/ActualCandidateAssembly.lean:553-556` |
| Native angular stage | `NavierStokes/ActualCandidateConstruction.lean:392-401` |
| Atlas-backed mean field | `NavierStokes/ActualCandidateConstruction.lean:355-366` |
| Production cutoff | `NavierStokes/SpatialLocalization.lean:164-172` |
| Positive-radius scalar expansion | `NavierStokesReview/src/completions/SelectedProductionDirectScalarGate.lean:21-46` |
| Pullback completion | `NavierStokesReview/src/completions/SelectedProductionDirectAtlasPullback.lean:22-68` |

## Consequence for the review

The native radial zero cannot be substituted directly for the production
field. The live quantity remains the cutoff-weighted scalar after atlas
pullback, torus averaging, and radial integration. This result does **not**
prove that the weighted remainder is nonzero, and it does **not** prove
`False`. It is a concrete selected-field calculation that narrows the
affirmative burden under CTR-005.

## Verification

The completion was checked with Lean 4.34.0-rc2 using the repository Lake
environment. The file compiled with no `sorry`, custom axiom, or `unsafe`
declaration.
