# Reachable R3, primary-coherence, mean-bound, and signed-wave tier

**Date:** 2026-09-27  
**Scope:** direct source review of four modules reachable from the selected
candidate closure.

## Source facts

| Module | Verified declarations | What they establish | What remains unproved at the selected endpoint |
|---|---|---|---|
| `NavierStokes/R3/CandidateBreakdown.lean:18-81` | `CandidateProperties.not_global_agreement`, `no_global_solution_one`, `force_nonzero_of_no_global_solution`, `uniform_l2_sq_bound` | Compact support plus speed unboundedness excludes a smooth global finite-energy competitor under the whole-space comparison chain; the formal candidate also yields a uniform (L^2)-square bound. | No five-observable transport theorem and no absolute pressure-Poisson representative. |
| `NavierStokes/ActualPrimaryCoherence.lean:1722-1804,1866-1902` | `globalPotential_forward`, `globalPotential_forward_germ`, `cartesianPotential`, `cartesianVelocity`, `cartesianPotential_smooth`, `cartesianVelocity_axis_zero`, `piece_cartesian_velocity` | Actual primary chart data is lifted to periodic Cartesian potentials and literal spatial curls, with positive-radius representation, smoothness, axis-zero germs, and component-level piece-to-Cartesian identities. | No theorem evaluating the final selected (ASum/BSum/PSum) through ((M,I,J,S,C_p)). |
| `NavierStokes/MeanMomentBounds.lean:283-304,426-498` | `liftedTorusAverage`, `radialWeighted`, `pressureMass_radialWeighted`, `meanClass_radialMoment`, `meanClass_radialMoment_lift` | Torus averaging and radial weighting are genuine typed operators; pressure mass reduces to an integrated radial moment, with smoothness/support/jet-class bounds. | The operators are not composed here with the final selected whole-space Cartesian field and do not provide its numerical five-tuple. |
| `NavierStokes/PhysicalSignedWave.lean:1040-1128,1266-1304,1380-1425` | `physicalPotential`, `physicalVelocity`, `wave_physical`, `complexPhysicalPressure_periodic`, `primaryPhysicalVelocity`, `primary_wave_physical` | Signed and primary wave components have explicit cutoffs, periodicity, smoothness, pressure modes, and literal Cartesian-curl representations. | No final selected-field radial pullback, support/integrability evaluation, or five-moment equality. |

## Adjudication

This tier rejects the description of the repository as disconnected profile names
or as a purely generic-rate shell. It also does not prove that a cutoff/curl
commutator has a nonzero integral. The source establishes the local operators and
their composition identities; the unresolved question is their value-level
composition through the selected infinite field and the five paper observables.

The current classification remains **not established as a paper-to-endpoint
correspondence under CTR-005**. No zero-sorry nonzero remainder, impossibility
theorem, or selected-path `False` was found in this tier.

## Reproducible anchors

- `NavierStokes/R3/CandidateBreakdown.lean:18-81`
- `NavierStokes/ActualPrimaryCoherence.lean:1722-1804,1866-1902`
- `NavierStokes/MeanMomentBounds.lean:283-304,426-498`
- `NavierStokes/PhysicalSignedWave.lean:1040-1128,1266-1304,1380-1425`
