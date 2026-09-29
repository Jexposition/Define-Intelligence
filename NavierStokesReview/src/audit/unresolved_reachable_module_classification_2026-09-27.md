# Unresolved Reachable Module Classification

**Date:** 2026-09-27
**Scope:** first 23 modules in the current reachable-but-not-yet-semantic queue
**Authority:** live source files under `NavierStokes/`; this report is not inferred from filenames alone.

## Purpose

This is a source-reading tranche, not a completion claim. Each module was opened, its import header and declaration region inspected, and its role classified against the selected endpoint route. The classification asks a narrow question:

> Does this module itself establish a theorem transporting the paper's five radial observables through the final selected Cartesian field?

Reachability is recorded separately from transport. A module can contain genuine mathematics and still not close the endpoint correspondence.

## Findings

| Module | What the source does | Endpoint consequence |
|---|---|---|
| `ActualCarrierTransport.lean` | Transports carrier geometry and labels between actual-cycle parameterisations. | No final Cartesian five-moment observable. |
| `ActualCopySliceRegularity.lean` | Builds regularity, frame, coefficient, forcing, and copied-slice data. | No endpoint moment equality. |
| `ActualSignedDynamics.lean` | Defines signed native units, pulses, motion, and smoothness. | Rate/dynamics support only. |
| `ActualSignedGaussianCoherence.lean` | Proves Gaussian and block transport identities between chart and physical scales. | Local chart transport, not selected-field transport. |
| `ActualSignedReferenceGeometry.lean` | Supplies singleton, reband, and signed exterior geometry. | No global radial observable. |
| `AnnularAuxiliary.lean` | Constructs positive radial auxiliary maps, germs, and derivatives. | Auxiliary profile layer only. |
| `BandReindexedSignedMeanGain.lean` | Reindexes finite signed mean-gain fields and proves `StateMomentBalances.meanBar`/`physicalSigma` cross identities. | Not the final `DefectIncrementBounds.barMoment`. |
| `BlowupImplication.lean` | Gives an abstract implication from unbounded speed to failure of bounded extension. | Consequence logic, not construction of moments. |
| `CompactSmoothFamily.lean` | Provides compact smooth-family and derivative infrastructure. | No radial moment transport. |
| `ConeAlgebra.lean` | Proves scalar cone and root inequalities. | Profile admissibility only. |
| `CurrentModeGeometry.lean` | Defines chart radii, annuli, and native mode maps. | Local geometry, no global moment identity. |
| `DiagonalScale.lean` | Defines logarithmic weights, scales, and doubling envelopes. | Rate control only. |
| `FiniteHeadClass.lean` | Defines finite-head comparison and jet classes. | No finite-head-to-moment theorem. |
| `Flatness.lean` | Proves `PowerFlat` composition rules. | Jet flatness does not imply moment preservation. |
| `GaussianEnvelope.lean` | Establishes Gaussian envelopes and quadratic decay bounds. | No selected-field identification. |
| `GrowingMode.lean` | Defines modal operators and growth estimates. | Upstream rate data only. |
| `HarmonicCovariance.lean` | Handles angular covariance, error membership, and harmonic admissibility. | No endpoint observable. |
| `LocalizedCurlRealization.lean` | Realises localised curl modes; proves smoothness, divergence-free fields, and zero germs. | Confirms real Cartesian curl infrastructure, but no post-localisation moment theorem. |
| `MixedDiagonalExtensions.lean` | Builds one-sided endpoint extensions and shrinking-support facts. | Extension support, not moments. |
| `MixedFiniteBackground.lean` | Builds finite-prefix backgrounds and stage jet rates. | Feeds rate interface; no five-moment equality. |
| `ModulatedStockBounds.lean` | Defines stock profile data, coordinates, and smoothness bounds. | No transport into final field. |
| `NativePrincipalEquations.lean` | States principal coefficient equations for native profiles. | Local profile equations, not selected endpoint proof. |
| `ParticularPaddedBackground.lean` | Constructs padded cells, local normals, germs, and polynomial pieces. | No cumulative-moment transport through selected sums. |

## Important positive evidence

The tranche strengthens, rather than weakens, the calibrated audit:

1. The source contains genuine profile, geometry, curl, regularity, and rate machinery.
2. `LocalizedCurlRealization.lean` confirms that the 3D Cartesian construction is not a purely axial placeholder.
3. `BandReindexedSignedMeanGain.lean` contains real intermediate moment-like cross identities.
4. None of the inspected declarations has the required endpoint shape:

   ```text
   final_selected_field
     -> torusAverage / radial pullback / barMoment
     -> (M, I, J, S, C_p)
   ```

5. This does not prove that no such theorem exists elsewhere. It reduces the unresolved search set and records the exact layers that have now been ruled out as the missing endpoint bridge.

## Classification

| Question | Status |
|---|---|
| Are these modules reachable and substantive? | Yes, on the current source/environment map. |
| Are they dead code? | No. That claim remains retracted. |
| Do they prove the selected Cartesian five-moment transport theorem? | Not in the inspected declarations. |
| Do they prove a non-zero selected-field defect? | No. The CUDA calculation is a profile diagnostic, not a Lean theorem about `selected_witness`. |
| Does this tranche derive `False`? | No. |

## Next source tranche

Continue from the remaining unresolved reachable queue, prioritising modules that can still alter the endpoint interpretation:

1. `MixedPeriodicAssembly.lean`, `SpatialLocalization.lean`, `SolenoidalDiagonal.lean`, and `ActualPrimaryCoherence.lean` for exact value composition.
2. `PressureStream.lean`, `DefectIncrementBounds.lean`, and all `barMoment` consumers for observable scope.
3. R3 candidate, pressure, energy, and uniqueness modules for the actual exported predicate.
4. Only after the source closure is complete, classify any numerical defect as profile-only, selected-field, or formal contradiction.

