# Priority 143: Euler cylinder-angle and classical-field source review

Date: 2026-09-29
Scope: direct raw-source review of five queued Euler cylinder modules. This is a source review, not a completion claim for the Euler branch and not a verdict about the Navier--Stokes endpoint.

## Files and declared roles

| File | Raw declarations reviewed | What the file establishes |
|---|---|---|
| `Euler/CylinderAnglePrimitive.lean` | `angleShift` 15, `kernelCurve` 21, `kernelIntegral` 27, `kernelIntegral_add` 29, `kernelIntegral_smul` 41, `kernelIntegral_norm` 52, `primitiveLinear` 68, `primitive` 73, `primitive_translation` 82, `sobolevPrimitive` 98, `sobolevPrimitive_norm` 101 | A bounded angular primitive on cylinder (L^2), its linear/continuous operator structure, norm estimate, translation commutation, and Sobolev lift. |
| `Euler/CylinderAngleRepresentative.lean` | `sobolevKernel_continuous` 16, `sobolevPrimitive_eq_integral` 21, `pointEvaluation_translation` 31, `pointEvaluation_primitive_kernel` 41, `pointEvaluation_primitive_classical` 55, `primitive_ae_classical` 73 | Identifies the lifted Sobolev primitive with a Bochner integral and classical pointwise/ almost-everywhere representatives under explicit hypotheses. |
| `Euler/CylinderAngleWordBounds.lean` | `primitive_hasDerivWithinAt` 17, `primitive_mixed_translation` 22, `primitive_block_bound` 28, `primitive_block_majorant` 34, `pathPrimitive` 49, `pathPrimitive_norm` 56, `pathPrimitive_block_bound` 66, `pathPrimitive_block_majorant` 74 | Propagates angular-primitive translation and mixed-word/Gevrey block bounds through a bounded continuous operator. |
| `Euler/CylinderBoundedCover.lean` | `cover` 24, `cover_norm_le` 35, `coverLinear` 42, `coverMap` 53, `coverMap_norm_le` 58, `coverPathMap` 69, `coverPath` 82, `coverOrbit` 91, `coverOrbit_contDiff` 96, `coverOrbit_apply` 103, `coverOrbit_zero` 127 | Lifts genuine periodic Sobolev cylinder fields to bounded continuous functions on the real covering space and proves norm/translation identities. |
| `Euler/CylinderClassicalWordBounds.lean` | `strongWord` 23, `strongWord_snoc` 30, `strongWord_translation` 40, `strongWord_smooth` 59, `strongWord_ae` 69, `representative_strongWord` 79, `classicalWord_memLp` 90, `classicalBaseSize_eq` 96, `classicalBlockSize` 104, `classicalBlockSize_eq` 109, `path_classicalBlockSize_le` 122 | Connects actual classical mixed derivatives of a smooth cylinder orbit to finite (L^2) word sums, with exact norm identification and time-evaluation contraction. |

## Import and dependent-module trace

The raw imports are:

- `CylinderAnglePrimitive` imports `CylinderSobolevOperators` and interval-integral basics.
- `CylinderAngleRepresentative` imports `CylinderAnglePrimitive`, `AnglePrimitiveKernel`, and `SobolevPointEvaluation`.
- `CylinderAngleWordBounds` imports `CylinderAnglePrimitive`, `ParameterSobolevProductGevrey`, and `LpCylinderOrbit`.
- `CylinderBoundedCover` imports `CylinderSobolevWordBounds` and `SobolevJointEvaluation`.
- `CylinderClassicalWordBounds` imports `CylinderOrbitSobolev`.

The direct dependent-import search identifies `CylinderAngleAverageRepresentative`, `CylinderAngleEvolution`, `CylinderScalarRepresentative`, `CylinderSmoothTimeField`, `CylinderScalarPrimitive`, `CylinderTimeWords`, and `FieldTowerSmoothTimeField` as consumers or transitive consumers of these modules.

## Formal content and limits

The source contains genuine operator and representative identities. The angular primitive is bounded by the period (P), and the cover uses the Sobolev embedding bound rather than confusing a cylinder (L^2) norm with a full-space pointwise norm. The classical-word result explicitly requires a `SmoothOrbit` hypothesis and derives (L^2) membership and exact finite-word norm identities from that solved orbit.

These modules do not construct the selected Navier--Stokes candidate, derive a global pressure-Poisson equation, define force independence, or carry the five radial observables. Their pointwise and almost-everywhere statements are conditional on the relevant Sobolev representatives, smooth orbit, mean-zero, and translation hypotheses.

## Endpoint cross-check

No reviewed declaration names `ActualCandidateAssembly`, `CandidateProperties`, `VelocityField`, `PressureField`, `navierStokesResidual`, `barMoment`, `FiveRowRank`, or `PositiveOrderMoments`. No five-observable transport equality, nonzero moment defect, impossibility theorem, or kernel-level `False` was obtained. This is a bounded source-review finding, not a claim that the wider Euler construction is dead or that the selected endpoint is disproved.

## Classification

`source_reviewed`: direct raw declarations, imports, and dependent import names inspected.
`mathematical finding`: genuine bounded angular, Sobolev representative, classical derivative, and covering-space results under explicit hypotheses.
`CMI relevance`: indirect Euler infrastructure only; no selected Navier--Stokes endpoint bridge located in this tranche.
`falsification result`: none.
