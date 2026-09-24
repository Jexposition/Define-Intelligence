# Global germ-transport validity audit

Date: 2026-09-24  
Tracking: CTR-016

## Source ledger

| Location | What is proved | What is not exported |
|---|---|---|
| `NavierStokes/CandidateConsequences.lean:185-215` | `mixed_exists_force_with_consequences` turns supplied local smoothness, divergence, residual-jet limits, away extensions, and origin growth into a global force, `CandidateProperties`, `Consequences`, H³ growth, force-jet decay, and endpoint boundary jets. | No five-moment field identity or force-independence predicate. |
| `NavierStokes/ActualCandidateAssembly.lean:1079-1098` | `physicalData` and `estimates` consume actual cycle states, uncut velocity/pressure fields, representations, and residual bounds. | No equality to `(M,I,J,S,C_p)` at the exported boundary. |
| `NavierStokes/ActualCandidateAssembly.lean:1100-1115` | `endpoints` supplies the germ-stage endpoint inputs used by the finite-stage schedule. | No separate theorem identifies those germs with the paper's moment functionals. |
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` packages the selected sums, away extensions, force, candidate properties, consequences, H³ blow-up, force decay, and boundary jets. | No `FiveRowRank.FiveRows`, `PositiveOrderMoments.moments`, or `(M,I,J,S,C_p)` field. |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1181` | `selected_witness` is the concrete instantiation of `Witness`. | It adds no transport or independence premise. |

## Zero-sorry global transport probe

`NavierStokesReview/src/probes/GlobalTransportBridgeProbe.lean:27-34`
proves that the selected candidate has both `CandidateProperties` and the full
`CandidateConsequences.Consequences` bundle while failing
`FixedForceSameDatumStable`. Lines 36--43 prove the corresponding universal
non-implication: the global consequence bundle does not imply same-datum
fixed-force stability.

The result is stronger than an isolated perturbation test because it is paired
with the same selected candidate's exported global consequences. It still does
not prove the literal C/D existential false. The endpoint does not quantify
over perturbations, require force independence, or export the five named
moment identity. The formal conclusion is therefore a verified contract gap
under CTR-016 and CTR-012, not `False`.

## Verification

The probe was checked with Lean 4.34.0-rc2 using `lake env lean`. The review
library was rebuilt with `lake build NavierStokesReview`. No source files under
the upstream `NavierStokes/` tree were changed.

## Recheck of the actual transport chain

The source inspection was extended beyond the exported `Witness` declaration.
The following chain is present in the selected construction:

| Source location | Transport step | Boundary of the result |
|---|---|---|
| `ActualCyclePreservation.lean:826-848` | `state_runInvariant` inducts the actual cycle state and retains analytic, coherence, and periodicity records. | It is a cycle-state invariant, not a theorem about the paper's five named moments. |
| `ActualCyclePreservation.lean:850-912` | `state_particularData`, `state_particularInputs`, `state_waveData`, and `state_wave_transport` derive the data consumed by the mean atlas. | These are analytic and wave-transport interfaces; they do not identify `PositiveOrderMoments.moments` with the selected mixed field. |
| `ActualCycleCoherence.lean:803-820` | `mean_input_of_transport` packages covariance and wave transport into `InitialCycleInput`. | The transported objects are covariance and wave fields, not the published tuple `(M,I,J,S,C_p)`. |
| `ActualCandidateConstruction.lean:392-404, 464-502` | Native angular, pressure, and stream stages are defined; prefix lemmas telescope adjacent cycle increments. | The prefix equalities are additive stage identities, not a global five-moment identity. |
| `ActualCandidateAssembly.lean:392-424` | `direct_on_chart`, `stream_on_chart`, and `meanPressure_on_chart` identify the actual fields with chart expressions on the chart domain. | The chart equalities are local spatial identities and do not export a pressure/Leray or five-moment certificate. |
| `ActualCandidateAssembly.lean:476-490` | `runData` and `meanCycleInput` feed the selected invariant and wave data into the stage-estimate construction. | This is positive provenance for the selected endpoint, not evidence that the paper's moment tuple reaches `Witness`. |
| `ActualCandidateAssembly.lean:1079-1098` | `physicalData` and `estimates` consume the actual cycle state, uncut fields, representations, and residual data. | No equality to `FiveProfileMoments.physicalMoments`, `PositiveOrderMoments.moments`, or `FiveRowRank.FiveRows` is exported. |

This recheck therefore corrects both extremes. The global germ construction is
not an empty wrapper, and the five-moment machinery is not absent from the
upstream closure. But the selected endpoint still does not display the
load-bearing semantic transport theorem that would make the public five-moment
interpretation a theorem about the selected velocity, pressure, residual, and
force.

## Formal status

`GlobalTransportBridgeProbe.lean:27-34` proves the selected candidate carries
the complete `Consequences` bundle while failing the review-side
`FixedForceSameDatumStable` predicate. Lines 36-43 prove the corresponding
universal non-implication. This is a zero-sorry contract result. It does not
derive `False` from the literal C/D existential, because the exported endpoint
does not quantify over perturbations or require force independence.
