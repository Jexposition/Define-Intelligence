# Priority 80 source review: axis, endpoint, radial pullback, and reference-path transport

Date: 2026-09-28
Scope: direct source review of six reachable `NavierStokes` modules.  This report records what the declarations prove and what they do not prove. It is not a build or endpoint-validity certificate.

## Reviewed source

1. `NavierStokes/BoundaryAxisJets.lean`
2. `NavierStokes/GenericEndpointExtension.lean`
3. `NavierStokes/PhaseJetBounds.lean`
4. `NavierStokes/RadialPullback.lean`
5. `NavierStokes/ReferencePath.lean`
6. `NavierStokes/WeightedRadialPrimitive.lean`

## Findings

### `BoundaryAxisJets.lean`

The module develops the signed radial and squared-radius axis machinery. It proves radial/axis jet identities, evenness, localised descent, ordinary positive-radius derivatives, joint smoothness, holomorphic parameter variants, interior cutoff identities, and axis-vanishing statements. The relevant declarations include `radialJet_succ`, `radialJet_even`, `axisJet_square`, `axisJet_zero`, `radialJet_joint_contDiffOn`, and the full/local axis pullback results (approximately lines 21–99, 103–320, 339–607, and 631–878).

This is genuine local axis regularity. It is not a global Cartesian observable evaluator and does not assert `barMoment`, `FiveRows`, or a selected-field equality with `(M,I,J,S,C_p)`.

### `GenericEndpointExtension.lean`

The module generalises smooth strip gluing and endpoint extension. It proves normal-trace identities, derivative matching, smooth extensions across the past/future boundary, closure-jet continuity, and propagation of additive spatial periods to the completed boundary values. The period-transfer declarations include `normalTrace_add_period`, `smoothExtension_add_period`, `stripClosedField_add_period`, `upperClosed_add_period`, `lowerClosed_add_period`, and `extension_add_period` (approximately lines 23–413 and 612–854).

These declarations transfer regularity and periodicity. They do not evaluate a radial moment, invoke `barMoment` or `FiveRows`, or connect an endpoint extension to `ActualCandidateAssembly.Witness`.

### `PhaseJetBounds.lean`

The module defines polynomial jet contracts over parameter domains and proves closure under constants, linear/bilinear maps, products, powers, composition, compact-range inversion, and affine precomposition. It then instantiates these contracts for normal geometry, phase families, frame data, rounded frequencies, viscosity, and epsilon rates (approximately lines 20–365 and 371–1031).

This is quantitative local phase/geometry infrastructure. It gives no five-moment evaluator and no theorem transporting a selected Cartesian field to the paper tuple.

### `RadialPullback.lean`

This is the strongest positive result in this tranche and must not be collapsed into a generic “no bridge” statement. Under explicit positivity, support, and smoothness hypotheses, it proves exact reduced radial integral identities for power-coordinate normalisation and physical compact pullbacks. In particular:

- `total_normalized_eq_radialIntegral` states that the transformed total integral equals the original physical radial interval integral (lines 324–334).
- `physicalCompact_eq_radialIntegral` expands the physical compact pullback into the original radial integral and its cutoff correction (lines 356–365).
- Additional declarations establish smoothness, support, derivative identities, finite-jet bounds, and supported `MeanClass` transport (approximately lines 382–485 and 756–856).

The theorem is a real reduced-profile change-of-variables bridge. Its hypotheses are generic `RadialAlias` functions and its conclusions are reduced radial/mean-class identities. The file does not identify the source with the final selected 3D Cartesian field, and it does not compose the identity through Cartesian curl, the selected `tsum`, spacetime localisation, torus periodisation, or the public `Witness` boundary.

### `ReferencePath.lean`

The module constructs a same-radius reference continuation with smooth slope damping, a frozen continuation, logarithmic radius/time coordinates, and reference error-jet bounds. The declaration `histories` is explicitly documented as rebuilding “Actual pressure, moments, and lag variables” from the reference continuation (lines 601–610). Its structure supplies the reference `f`, `U`, smoothness proofs, and `pressure0` to `ProfileHistories.Profiles`.

This confirms that reduced pressure/moment state is recomputed from a reference profile in this layer. It does not show that those reduced histories are equal to observables of the final selected Cartesian velocity and pressure after the later assembly pipeline, nor does it export such an equality to `Witness`.

### `WeightedRadialPrimitive.lean`

The module proves uniform two-edge weighted bounds for compact radial primitives and transport inverses. It also proves exact left/right collar identities, finite-jet estimates, and `MeanClass` transport. The key declarations are `compact_primitive_uniform`, `transport_compact_primitive_uniform`, `compact_jet_eq_past_on_left`, `compact_jet_eq_neg_future_on_right`, `transport_compact_finiteJets_uniform`, `meanClass_canonical_transport`, and `supported_meanClass_canonical_transport` (approximately lines 229–377, 662–988, and 1042–1102).

This is substantive reduced-profile integral and regularity machinery. Its generic vector-valued source and `MeanClass` target do not constitute the selected Cartesian five-observable tuple, and no `Witness` or `selected_witness` transport theorem is declared here.

## Correspondence result

This tranche changes the audit in one important direction: the repository contains more genuine intermediate radial transport than a simple packaging-only description suggests. `RadialPullback` and `WeightedRadialPrimitive` prove exact or controlled reduced integral transport, while `ReferencePath.histories` rebuilds reduced pressure/moment state from a reference path.

It does not close the selected-field correspondence. The reviewed declarations do not establish the composite statement

```text
selected Cartesian field
  -> curl/localisation/tsum/periodisation
  -> torus or radial observable
  -> (M, I, J, S, C_p)
  -> ActualCandidateAssembly.Witness
```

Therefore the evidence remains `CTR-005: endpoint correspondence not established`, not “moment machinery absent”. This tranche does not prove a non-zero defect, an impossibility theorem, or `False`.

## Next registered queue

After regeneration, the queue must be read from the live register rather than copied from an earlier report. The next priority modules are expected to be the remaining boundary/extension/radial support files, beginning with `BoundaryAxisJets`-adjacent endpoint modules where they remain reachable and unreviewed.

