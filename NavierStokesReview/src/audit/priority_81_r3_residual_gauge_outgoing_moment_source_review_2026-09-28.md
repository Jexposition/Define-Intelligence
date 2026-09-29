# Priority 81 source review: R3 packaging, residual bridges, gauge mass, and outgoing moments

Date: 2026-09-28
Scope: direct source review of the next six reachable modules selected from the regenerated live register.

## Reviewed source

1. `NavierStokes/R3CompactCandidate.lean`
2. `NavierStokes/ResidualRegularity.lean`
3. `NavierStokes/GaugeRadialResidualBounds.lean`
4. `NavierStokes/MixedDiagonalResidual.lean`
5. `NavierStokes/OutgoingSchedule.lean`
6. `NavierStokes/ResidualCalculus.lean`

## Findings

### `R3CompactCandidate.lean`

`R3CompactCandidate.Properties` packages pre-singular smoothness, compact velocity/pressure/force support, future time support, divergence, residual equality, energy, initial conditions, and local blow-up properties (approximately lines 23–37). The module defines the direct and periodic localised fields and proves support and local-agreement results. `of_periodic_local_model` transfers a periodic `CandidateProperties` witness to compact whole-space properties, and `of_localized_fields` consumes `CandidateProperties` for the same raw sums (`A`, `B`, and `P`) to produce the compact candidate (approximately lines 178–252).

This is a concrete R³ packaging bridge. It is not evidence that the packaging is empty. It also does not add a theorem asserting that the compact Cartesian field has the complete paper tuple `(M,I,J,S,C_p)`.

### `ResidualRegularity.lean`

The module proves joint smoothness of the concrete Navier–Stokes residual, spatial-period transfer, locality/congruence, and zero-residual consequences for local zero extensions. The residual is treated as an actual differential expression, not an uninterpreted placeholder (approximately lines 13–107 and 113–291).

These theorems support local PDE reuse and the R³ localisation construction. They do not define or evaluate the paper’s radial observables.

### `GaugeRadialResidualBounds.lean`

This module provides a direct positive bridge that must be retained in the audit. `pressureDefect_eq_mass` identifies `pressureDefect` with `PressureStream.pressureMass` of the generated radial source, and its documentation states that this is the actual zeroth radial moment with the same auxiliary-torus average used by the gauge (approximately lines 66–80). `reconstructed_identity`, `radialMinusAlias_identity`, `radialMinusAlias_class`, `similarity_identity`, and `similarity_class` then connect reconstructed pressure aliases and debt classes under explicit primitive-data, matching, and fixed-pressure hypotheses (approximately lines 84–250).

This is not merely a generic rate interface. It is a concrete reduced radial pressure/mass relation. Its scope is still narrower than the complete selected field: it does not establish all five paper observables after the full Cartesian assembly, nor does it export such a tuple into the public R³ `Witness`.

### `MixedDiagonalResidual.lean`

The module defines mixed velocity, pressure, and residual from the actual stage families. `residual_eq_originalResidual` is definitionally equal to the `MixedPeriodicAssembly.originalResidual` of the actual `potentialSum` fields (approximately lines 39–50). The module proves smoothness, finite-tail jet rates, residual jet rates, and `physical_vanishingJointJets`, deriving joint zero jets from finite-stage hypotheses rather than simply postulating them (approximately lines 52–198).

This closes a concrete residual/series route. It does not prove that the series-produced Cartesian field preserves the complete radial moment tuple.

### `OutgoingSchedule.lean`

This is the strongest moment result in this tranche. The module constructs an outgoing radial/angular pulse and proves exact repair identities. `pulse_closes_prefix` cancels the actual prefix mass and angular contributions against pulse integrals (approximately lines 617–625). `massMoment_endpoint` and `angularMoment_endpoint` prove that the two combined log-coordinate moments vanish at the endpoint, `exact_axial_moments` packages both equalities, and the post-pulse declarations preserve them (approximately lines 739–949).

This directly disproves any blanket statement that the repository contains no moment transport. The result is nevertheless not the full claim under audit: it covers two named reduced profile moments in the outgoing schedule, not a theorem identifying all five paper quantities with the final selected 3D Cartesian field after curl/localisation/periodisation and public `Witness` packaging.

### `ResidualCalculus.lean`

The module proves additivity and perturbation formulas for temporal derivatives, spatial derivatives, pressure gradients, divergence, Laplacian, advection, and the full Navier–Stokes residual. It also proves time-scalar multiplication and divergence-free consequences (approximately lines 17–268).

These identities make the residual’s dependence on field perturbations explicit. They are useful for the force-provenance audit, but by themselves are not a CMI admissibility theorem and do not establish the five-moment endpoint transport.

## Correspondence result

Priority 81 materially strengthens the positive side of the source record:

- R³ packaging transfers a periodic local candidate to compact whole-space properties.
- The residual is concretely defined from the actual assembled fields.
- The gauge layer identifies a pressure defect with an auxiliary-torus averaged zeroth radial mass.
- The outgoing schedule proves exact cancellation of two reduced combined moments.

The remaining issue is now stated more precisely. The audit is not claiming that OpenAI’s code has no moment theorems. The open question is whether these reduced moment and residual identities are composed into the complete selected Cartesian observable map and exported through `ActualCandidateAssembly.Witness` with the paper’s full `(M,I,J,S,C_p)` semantics.

Status remains `CTR-005: selected endpoint correspondence not established`. This tranche does not prove `Delta m != 0`, an impossibility theorem, or `False`.

