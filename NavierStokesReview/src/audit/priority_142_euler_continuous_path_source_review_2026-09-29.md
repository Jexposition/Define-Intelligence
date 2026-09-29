# Priority 142: Euler continuous-path and cylinder source review

Date: 2026-09-29
Scope: direct raw-source review of five queued Euler modules selected from the repository-wide register. This is a source review, not a completion claim for the Euler branch and not a verdict about the Navier--Stokes endpoint.

## Files and declared roles

| File | Raw declarations reviewed | What the file establishes |
|---|---|---|
| `Euler/ContinuousInverseDerivative.lean` | `hasFDerivAt_inverse` 17 | A generic derivative-of-inverse theorem under explicit local composition and left-inverse hypotheses. It is inverse-function calculus, not a PDE existence theorem. |
| `Euler/ContinuousPathCalculus.lean` | `coefficientLinear` 36, `coefficientMap` 52, `coefficientMap_norm` 62, `contDiff_multiplier` 70, `multiplier_bound` 78, `contDiff_apply` 86, `apply_bound` 92 | Continuous operator-valued path multiplication, norm bounds, parameter differentiability, and application bounds. |
| `Euler/ContinuousPathComposition.lean` | `postcomposition_norm` 47, `compositionLift` 57, `compositionLift_norm` 61, `compose` 65, `contDiff_compose` 74, `compose_bound` 85, `adjointMap` 121, `adjointMap_norm` 128, `contDiff_adjoint` 137, `adjoint_bound` 144 | Continuous operator composition and adjoint paths with norm, smoothness, and bound propagation. |
| `Euler/CylinderActionWords.lean` | `pathTranslate_norm_map` 22, `pathTranslateIsometry` 35, `path_block_constant` 39, `timeTranslateIsometry` 49, `timeTranslateIsometry_add` 53, `timeTranslateIsometry_zero` 65, `time_block_constant` 73, `pathLp_orbit_contDiff` 84, `pathLp_block_le` 97 | Isometric path/time translations and conditional regularity/block bounds on cylinder (L^2) paths. |
| `Euler/CylinderAngleEvolution.lean` | `pathPrimitive_translation` 20, `pathPrimitive_orbit_contDiff` 26, `primitive_sobolevPath` 32, `pointField_primitive_formula` 43, `pathPrimitive_time_derivative` 66, `classicalPrimitive_time_derivative` 73 | Angular primitive, mean-zero translation, Sobolev-path, pointwise formula, and time-derivative identities under stated hypotheses. |

## Import and dependent-module trace

The reviewed files import these upstream layers:

- `ContinuousInverseDerivative` imports `Mathlib.Analysis.Calculus.FDeriv.OfCompLeft`.
- `ContinuousPathCalculus` imports `ContinuousTimeIntegral` and `OperatorGevreyCalculus`.
- `ContinuousPathComposition` imports `ContinuousPathCalculus` and `TransverseGramInverse`.
- `CylinderActionWords` imports `IsometricActionWords`, `LpCylinderOrbit`, `CylinderTranslationAdjoint`, and `MeanPathLpBlocks`.
- `CylinderAngleEvolution` imports `CylinderAngleRepresentative`, `CylinderAngleWordBounds`, and `CylinderTimeRegularity`.

The raw import search identifies these consumers:

- `ContinuousInverseDerivative`: `PacketContinuousInverse`, `SmoothFlowJacobian`, and `ParentParticleRegularity`.
- `ContinuousPathCalculus`: `LpCylinderRectangular`, `LinearDuhamelParameter`, `SmoothPathSuperposition`, `SmoothTimeSuperposition`, and `TimeH1GeneratorBounds`.
- `ContinuousPathComposition`: `BoundedFieldCalculus`, `ContinuousGramPath`, `ContinuousAccelerationForcing`, `ContinuousSpatialFamily`, and `CylinderPathProduct`.
- `CylinderActionWords`: `CylinderDirichletTimeBounds`, `CylinderDirichletPhysicalBounds`, `CylinderDirichletSobolev`, and `MeanCylinderWordBounds`.
- `CylinderAngleEvolution`: `CylinderPotentialPath`.

## Formal content and limits

These files contain genuine conditional functional-analysis and cylinder-calculus infrastructure. Their assumptions are visible in the declarations: local inverse identities, complete normed/inner-product spaces, differentiability hypotheses, mean-zero conditions, and explicit derivative or majorant bounds. None of the five files names `ActualCandidateAssembly`, `CandidateProperties`, `VelocityField`, `PressureField`, `navierStokesResidual`, `barMoment`, `FiveRowRank`, or `PositiveOrderMoments`.

The inverse derivative theorem does not establish that a PDE flow map is invertible. The path-calculus theorems propagate regularity and bounds but do not derive Navier--Stokes or Euler equations. The cylinder primitive theorems require the relevant mean-zero and time-derivative premises rather than proving them from the selected whole-space candidate.

## Endpoint cross-check

The reviewed declarations do not state a selected Cartesian five-observable equality, a global pressure-Poisson representation, a force-provenance predicate, or a nonzero moment defect. They therefore neither close nor refute the selected-field transport question. This is a source-scope boundary, not evidence that these modules are dead, irrelevant, or false.

## Classification

`source_reviewed`: direct raw declarations, imports, and dependent import names inspected.
`mathematical finding`: genuine generic inverse, operator-path, translation, primitive, and regularity results under explicit hypotheses.
`CMI relevance`: indirect Euler infrastructure only; no selected Navier--Stokes endpoint bridge located in this tranche.
`falsification result`: none. No nonzero moment defect, impossibility theorem, or kernel-level `False` was obtained.
