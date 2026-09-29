# Priority 114: final reachable-module source review

Date: 2026-09-28
Scope: the eight modules previously marked `reachable_not_semantically_inspected` in the authoritative semantic-coverage register.

## Result

All eight remaining reachable modules were inspected at source level. They contain substantial mathematics: reduced radial stress and moment identities, smooth rank/debt preservation, Cartesian curl lifts, locally finite `tsum` control, lattice periodisation, periodic integration, and endpoint Sobolev estimates.

The review did not find a declaration proving the complete selected-field composition

\[
\text{profile moments}
\to \text{potential lift}
\to \nabla\times
\to \text{localisation}
\to \text{periodisation/tsum}
\to \text{final Cartesian field}
\to \text{radial }\bar{\mathrm{Moment}}.
\]

This is a correspondence result, not a proof that the eventual defect is non-zero. No `Delta m`, impossibility theorem, or kernel-level `False` is claimed here.

## Module-by-module findings

| Module | Source declarations and mathematical role | Boundary result |
|---|---|---|
| `SignedWaveUpdate.lean` | Defines requested radial stress primitives, covariance control, signed inverse coefficients, local curl realisation, `tsum` assembly, radial/tangential component identities, double-average stress identities, and signed-square identities. | Real reduced stress and local torus-average transport; no final selected Cartesian `barMoment` or `(M,I,J,S,Cp)` theorem. |
| `EntranceAlignedBase.lean` | Builds aligned and modulated slow bases. `aligned_moments_zero` proves positive-order `PositiveOrderMoments.moments` identities for reduced histories; mass primitives, pressure coefficients, support, smoothness, and finite identities are also proved. | Genuine reduced-profile moment preservation in `(X, eta)` variables; no global Cartesian radial-observable transport. |
| `InitializedPhysicalBackground.lean` | Constructs initialized potential and velocity from spatial curls and angular fields; proves smoothness, decomposition, finite/native rates, local representation, and rate transport. | Genuine curl-lifted physical background and jet transport; no five-observable final-field identity. |
| `MeanStageRegularity.lean` | Proves smoothness of moving fields, temporal stage reconstruction, actual debt smoothness, rank geometry, moving rank increments, and temporal rank preservation. | Genuine state/rank preservation; no final Cartesian `barMoment` theorem. |
| `PeriodicIntegration.lean` | Defines cube coordinates, periodic integration, partial derivatives, product rules, zero integral of periodic coordinate derivatives, and parameter-dependent cube-integral calculus. | Cube-periodic integration identities; these are not radial `barMoment` identities for the selected field. |
| `PeriodicLocalization.lean` | Defines lattice translation and periodisation, locally finite translated sums, smoothness, lattice periodicity, inner-cube equality, origin equality, and time-support preservation. | Genuine periodisation regularity/support; no theorem that periodisation preserves weighted radial moments. |
| `PeriodicSobolev.lean` | Defines periodic line/cube energies and derivative-H3 norms, proves the periodic pointwise bound, and derives candidate derivative-H3 blow-up from speed blow-up. | Endpoint functional-analytic consequence; it neither constructs nor transports the five radial observables. |
| `PrimaryCopyBounds.lean` | Defines native jets and closure operations, affine copies, local finite copy sums, outer cutoffs, periodised native fields, support, and uniform jet bounds. | Strong local/jet and copy-sum control; no weighted radial-integral convergence or final tuple equality. |

## Cross-module conclusion

The source review confirms three separate layers:

1. **Reduced/profile layer:** exact moment and stress identities genuinely exist, including `PositiveOrderMoments.moments` and signed radial stress primitives.
2. **Geometric/analytic layer:** curl lifts, localisation, periodisation, locally finite sums, and jet bounds are genuinely formalised.
3. **Selected endpoint observable:** the inspected modules do not supply the composite theorem that evaluates the final selected Cartesian field through the paper-level radial observables.

The register must therefore distinguish “intermediate bridge mathematics inspected” from “final selected-field transport established”. The latter remains unestablished until a declaration with that full input/output composition is found or constructed.

