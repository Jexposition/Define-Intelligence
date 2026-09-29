# Priority 77 source review: axis evaluation, dilation, extension, and ODE jets

Date: 2026-09-28
Scope: eight directly inspected Lean source files in `NavierStokes/`
Method: source declarations and theorem statements were read from the live checkout. This report records what is present and what remains unproved; it does not infer a non-zero defect, an impossibility theorem, or `False`.

## Source findings

### `AxisCoefficientSpace.lean`

Defines `Window`, interval projection, raw jets, `Compatible`, the compatible submodule, coefficient-space smoothness, derivative and norm estimates, and the `AxisSpace` abstraction. The file provides genuine interval coefficient analysis. Its inspected declarations do not contain a selected-endpoint equality for the five paper observables.

Anchors: lines 28–102, 118–245, and 260–450.

### `AxisEvaluation.lean`

Defines `polynomialJet`, `term`, `mixedSeries`, and `profile`, together with majorants, summability, uniform `tsum` evaluation, smoothness, jet bounds, and linear evaluation maps. This is an actual axis-series evaluator, not an empty interface. It does not identify the final selected Cartesian field with `(M, I, J, S, C_p)` in the inspected source.

Anchors: lines 29–54, 57–126, and 135–488.

### `AxisResolvent.lean`

Defines factorial majorants, vanishing-below-degree conditions, regular radial inverses, alternating resolvent series, filtration powers, and resolvent equations/uniqueness. These results control an analytic axis resolvent. They are not, by themselves, a physical moment-transport theorem for the selected witness.

Anchors: lines 28–130, 139–190, and 195–476.

### `BasePhaseGeometry.lean`

Defines reference scales, damping and normalisation bounds, local base/error/phase/frame estimates, family data, modal and kinematic jets, energy/coefficient/frame bounds, and phase-geometry ODE estimates. This is substantive geometric regularity machinery. No global selected-field five-observable equality appears in the inspected declarations.

Anchors: lines 28–137, 159–226, and 524–1137.

### `LocalizedGaussianBounds.lean`

Proves zero and inactive germs, local/global Gaussian cutoff gains, indexed tails, uniform complement jets, and source/harmonic complement bounds. It supplies localised regularity and tail estimates. It does not state that the paper radial observables survive localisation.

Anchors: lines 29–45, 57–92, 149–245, 259–319, and 351–557.

### `OutgoingDilation.lean`: positive moment evidence

This file materially narrows the audit. It defines the actual dilated reduced-profile fields `E`, `U`, `H`, `Pi`, `energyDensity`, and `canonicalKernel`, and defines

\[
M=\int U,\quad I=\int H,\quad J=\int HU,\quad
S=\int\left(U^2-\frac{E^2}{2}\right),
\]

along with `totalS`, `renormalizedI`, and `axisDatum`, the pressure-axis datum used here as the relevant (C_p)-type quantity. It proves scaling identities, integrability, zero identities, axis limits, and the reduced `DilatedSpecification`. Therefore the claim “the repository contains no five-moment mathematics” is false and must not appear in the audit.

The unresolved question is narrower and stronger: the inspected source does not prove that these reduced observables are equal to the corresponding observables of the complete selected Cartesian field after every selected stage, vector-potential/curl lift, localisation, periodisation, `tsum`, pressure construction, and final `Witness` packaging.

Anchors: lines 21–57, 61–78, 80–151, and 294–609.

### `ParametricRadialExtension.lean`

Constructs a smooth even radial extension with parameter cutoffs, squared-radius descent, half-plane lifting, mixed jets, pullbacks, axis jets, zero exterior, and compact support. This provides meaningful axis regularity and support infrastructure, but no final selected Cartesian five-moment transport statement.

Anchors: lines 24–113, 115–210, and 214–362.

### `WeightedODEJets.lean`

Defines directional/list jets and proves smoothness, congruence, algebraic/product/cross-jet rules, ODE solution-jet identities, norm envelopes, and weighted finite-order estimates. These are genuine parameter-ODE controls. They do not constitute a radial-observable transport theorem into `selected_witness`.

Anchors: lines 30–165, 194–260, and 294–754.

## Cross-layer conclusion

The tranche establishes three separate facts:

1. Reduced-profile moment definitions and identities are present and substantive, especially in `OutgoingDilation.lean`.
2. Axis, radial, localisation, series, and ODE layers contain real analytical infrastructure, including some post-curl/base radial identities in neighbouring files.
3. The complete selected-field transport theorem remains unlocated in the inspected source. The correct status is therefore an open correspondence audit, not “moment machinery absent”, not “the curl must create a non-zero defect”, and not `False`.

The next audit action is declaration-level closure from these reduced observables through the selected stage/curl/localisation/periodisation/sum/pressure path into `ActualCandidateAssembly.Witness`, while recording any positive bridge theorem if found.
