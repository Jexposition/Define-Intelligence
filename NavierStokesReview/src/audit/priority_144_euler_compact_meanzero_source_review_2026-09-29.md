# Priority 144: Euler compact-translation and mean-zero source review

Date: 2026-09-29
Scope: direct raw-source review of five queued Euler modules. This is a source review, not a completion claim for the Euler branch and not a verdict about the Navier--Stokes endpoint.

## Files and declared roles

| File | Raw declarations reviewed | What the file establishes |
|---|---|---|
| `Euler/CylinderCompactTranslation.lean` | `CompactField` 28, `continuous` 38, `toLp` 41, `toLp_ae` 44, `derivative` 47, `derivative_bound` 53, `translation_support` 64, `increment_bound` 82, `hasFDerivAt_zero` 103, `derivativeMap_translation` 124, `translation_hasFDerivAt` 137, `translation_fderiv` 144, `translation_contDiff` 166 | Gives compact smooth cylinder fields a genuine (L^2) translation orbit, with support control, dominated Fréchet differentiation, and smoothness. |
| `Euler/CylinderCompactBounds.lean` | `supportMass` 24, `derivative_support` 33, `toLp_norm_le` 39, `norm_iteratedFDeriv_translation_le` 82, `translation_gevrey` 89, `translation_block_bound` 97 | Converts compact support and local derivative bounds into (L^2) translation/Gevrey and block estimates using one fixed support mass. |
| `Euler/CylinderConstantMap.lean` | `map` 18, `map_ae` 21, `map_norm` 24, `map_comp` 26, `map_id` 37, `map_translation` 41, `pathMap` 52, `pathMap_norm` 59, `pathMap_translation` 69, `pathMap_orbit_contDiff` 75 | Applies fixed bounded linear maps to cylinder (L^2) classes and continuous paths, preserving translation and regularity with norm control. |
| `Euler/CylinderConstantMapBounds.lean` | `pathMap_block_bound` 18 | Propagates external-word block bounds through a fixed bounded map without changing the path radius, up to (|L|). |
| `Euler/CylinderCorrectorMeanZero.lean` | `average_primitive` 19, `pathAverage_primitive` 31, `derivativePath_zero` 37, `pathAverage_derivativePath` 44, `pathAverage_potentialPath` 55, `potentialPath_mean_zero` 60, `pathAverage_slowCurl` 66, `slowCurl_mean_zero` 76 | Proves preservation of the cylinder's zero angular mean by the primitive, potential path, and slow-curl operations under explicit path smoothness and zero-mean hypotheses. |

## Import and dependent-module trace

The compact translation layer imports `LpCylinderTranslation`, dominated-derivative, isometric-action calculus, and mean-value calculus. Compact bounds imports compact translation and parameter Sobolev coefficients. Constant maps import cylinder translation and parameter Sobolev linear algebra. The mean-zero corrector layer imports `CylinderSlowCurl`, `CylinderPotentialPath`, and `CylinderAngleAverageTime`.

The direct dependent-import search identifies `CylinderPathBilinear`, `CylinderScalarPrimitive`, `CylinderRetractRepresentative`, `PacketTerminalDatum`, `PacketCylinderFieldBounds`, `PacketCylinderScalarGradientBounds`, `PacketTerminalDatumBounds`, `TransversePacketCorrectorMean`, `TransversePacketJoinedCorrectorSupport`, and `TransversePacketPrimaryCorrector` as consumers or transitive consumers.

## Formal content and limits

This tranche contains substantive compact-support, derivative, map, and mean-zero algebra. In particular, `potentialPath_mean_zero` and `slowCurl_mean_zero` are real invariant-preservation theorems, but their invariant is the cylinder angular average and their premises include `pathAverage P p = 0`. They are not the five cumulative radial observables ((M,I,J,S,C_p)), nor do they identify a final whole-space Cartesian field.

The compact support estimates are conditional on a supplied compact field, local derivative bounds, and a compact support set. The fixed-map estimates are conditional on the bounded linear map. None of the reviewed modules derives the selected Navier--Stokes residual, pressure, external force, or CMI endpoint.

## Endpoint cross-check

No reviewed declaration names `ActualCandidateAssembly`, `CandidateProperties`, `VelocityField`, `PressureField`, `navierStokesResidual`, `barMoment`, `FiveRowRank`, or `PositiveOrderMoments`. No five-observable transport equality, nonzero moment defect, impossibility theorem, or kernel-level `False` was obtained. The zero-mean results narrow a genuine upstream invariant but do not establish its transport into the selected endpoint.

## Classification

`source_reviewed`: direct raw declarations, imports, and dependent import names inspected.
`mathematical finding`: genuine conditional compact-translation, bounded-map, block-bound, and angular-mean preservation results.
`CMI relevance`: indirect Euler infrastructure; the mean-zero layer is relevant as an upstream invariant but is not a selected NS five-observable bridge.
`falsification result`: none.
