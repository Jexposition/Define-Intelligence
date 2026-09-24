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
