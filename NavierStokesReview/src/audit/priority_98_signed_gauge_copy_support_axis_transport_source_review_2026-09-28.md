# Priority 98 source review: signed regularity, gauge/copy transport, support, axis data, and tangent scaling

Date: 2026-09-28

## Scope

This tranche directly reviews eleven reachable source modules:

1. `ActualSignedNativeRegularity.lean`
2. `ExponentLedger.lean`
3. `GaugeAliasDecay.lean`
4. `GaugeStateCoherence.lean`
5. `IntervalCopyTransport.lean`
6. `LabelSupportPreservation.lean`
7. `ModulatedExterior.lean`
8. `NaturalAxisData.lean`
9. `PositiveTimeSignedData.lean`
10. `PressureDatum.lean`
11. `ScaledTangentTransport.lean`

## Source findings

### `ActualSignedNativeRegularity.lean`

The module proves radial/dyadic pullback regularity, zero-outside jets, native-cylinder maps, smooth and flat potential/pressure requests, and residual-derived request jets. The final `nativeRegular`, `nativeRegular_from_residuals`, and `cycleNative` declarations show that the signed physical family has regularity data sufficient for its stage interface. This is positive regularity evidence. It is not a theorem identifying the final selected Cartesian field with `(M,I,J,S,C_p)`.

### `ExponentLedger.lean`

The file defines wave, mean, mean-update, particular, signed, and signed-bar exponents and proves exact arithmetic identities and lower-margin inequalities. This validates rate bookkeeping at the exponent layer. It contains no field-level radial observable or endpoint transport statement.

### `GaugeAliasDecay.lean`

The module proves finite-jet fibre/local alias bounds, local pressure mass localisation, compact-alias gains, superflat mean classes, frequency bounds, and zero-mass source/pressure alias facts. These are genuine gauge/alias decay and cancellation results. They do not evaluate the selected global Cartesian `barMoment` observables.

### `GaugeStateCoherence.lean`

The module proves fibre-local pressure alias identities, endpoint congruence, gauge reconstruction, supported pressure aliases, band scaling, radial-frequency transport, and similarity reconstruction. These are coherent reduced/gauge data transitions. The pressure results remain local/reduced and do not provide an absolute whole-space selected pressure representative or the final five-observable equality.

### `IntervalCopyTransport.lean`

The module proves anchored/copy solve uniqueness and time-data transport, transported velocity and pressure identities, forcing continuity, zero-entry facts, and common-solve transport. This is real copy-path transport, including scaling and clock interval conditions. It does not transport the paper's five radial moments into `ActualCandidateAssembly.Witness`.

### `LabelSupportPreservation.lean`

The file proves zero germs and support preservation for raw, corrected, native, particular, signed, block-summed, and transported-mask data. These results control support and germ behaviour under localisation. They do not prove moment preservation under the complete selected global assembly.

### `ModulatedExterior.lean`

The module proves reduced exterior integral equality, squared-swirl and pressure matching after the nominal exterior, exact heat-exterior fields, residual and residual-jet vanishing, and terminal extension statements. This is substantive reduced exterior matching. It is not yet a selected Cartesian/localised/periodised five-moment theorem.

### `NaturalAxisData.lean`

The file defines reduced axis quantities and proves parameter bounds, unique pressure-related roots, positivity and derivative properties, and existence of cutoff parameters. This is reduced axis geometry and pressure-data control, not global Cartesian pressure semantics.

### `PositiveTimeSignedData.lean`

The module defines positive-time signed potential/pressure copy families, cells, carriers, supports, smoothness, wave data, germ identities, and physical bounds. It supplies concrete stage data to later interfaces. It does not expose the final selected Cartesian `(M,I,J,S,C_p)` equality.

### `PressureDatum.lean`

The module defines a weighted pressure kernel and proves integrability, sign, smoothness, complex analytic continuation, derivative signs, prefix-mass inequalities, and ideal-prefix bounds. This is a reduced pressure datum, not an absolute global Poisson/Leray representation of the selected `p`.

### `ScaledTangentTransport.lean`

The module proves coordinate/path/slot transport, finite transported copy cutoffs, tangent normal scaling, compatible copy solves, real and complex pressure/velocity transport, and finite transported periodisation. This is strong intermediate transport infrastructure. The reviewed declarations still stop short of composing the selected full field into the five final radial observables.

## Adjudication

Priority 98 adds positive evidence for regularity, rates, gauge coherence, copy transport, support preservation, reduced exterior matching, axis pressure data, signed stage data, and scaled tangent transport. It narrows the remaining audit question but does not close it. No `Delta m != 0`, impossibility theorem, or `False` is inferred.

