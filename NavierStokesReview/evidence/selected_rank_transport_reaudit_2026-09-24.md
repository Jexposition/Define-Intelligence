# Selected rank transport re-audit

**Date:** 2026-09-24
**Scope:** `CorrectionState`, `MeanRankUpdate`, `ActualMeanPhysicalData`,
`ActualStageEstimates`, and `ActualCandidateAssembly`
**Purpose:** verify whether the two zero rows in `FiveRowRank` create a
selected-field contradiction, or only an internal correction invariant.

## Source ledger

| Source location | Verified fact | Consequence |
|---|---|---|
| `NavierStokes/FiveRowRank.lean:241-247` | `FiveRows V G d dv ga` imposes `∫ R, R^2 * dv R = 0` and `∫ R, R * ga R = 0`, then three debt equations. | The zero rows constrain correction functions, not total kinetic energy. |
| `NavierStokes/MeanRankUpdate.lean:136-151` | `fiveRows_scaled` preserves the two zero correction rows under scaling. | The scaling law is an exact three-debt transport law. |
| `NavierStokes/MeanRankUpdate.lean:162-174` | `physical_five_rows` proves the full five-row predicate for arbitrary admissible `d : Fin 3 → ℝ`. | The runtime rank system is not restricted to zero debt. |
| `NavierStokes/CorrectionState.lean:241-251` | `debt` is `Fin 3 → ℝ`; `ZeroMasses` names two radial moments of the mean state. | These invariants are not definitions of Cartesian mass or kinetic energy. |
| `NavierStokes/CorrectionState.lean:449-490` | `rank_model_rows` and `rank_rows_on_patch` apply the physical five-row theorem to the actual rank construction. | The rank layer is active upstream. |
| `NavierStokes/DefectIncrementBounds.lean:701-721,773-813` | `rankStage` updates the state, proves the rows for the actual increment, and preserves the two radial moments. | A genuine internal correction invariant exists. |
| `NavierStokes/ActualMeanPhysicalData.lean:1148-1190` | `cycleRank_class` consumes `CorrectionState.debt` for the actual cycle; the rank family is built from that debt. | The selected upstream path is not debt-blind. |
| `NavierStokes/ActualCandidateAssembly.lean:1079-1098` | `physicalData` and `estimates` are built from actual cycle fields, physical field representations, and residual-rate bounds. | The final estimates are source-linked to actual fields. |
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` exports schedules, mixed sums, pressure, force, endpoint properties, jets, decay, and blow-up. | It does not export `FiveRows`, `ZeroMasses`, or the paper tuple `(M,I,J,S,C_p)`. |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1185` | `selected_witness` is an instance of `Witness`; `selected_candidate` extracts only the candidate fields and force properties. | The selected endpoint transport equality remains unexhibited. |

## Formal verification

The following source artefacts compile without `sorry`, `axiom`, or `unsafe`:

* `NavierStokesReview/src/completions/MeanRankUpdateAudit.lean`
* `NavierStokesReview/src/completions/CorrectionInvariantScope.lean`
* `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`
* `NavierStokesReview/src/probes/SelectedBaseMomentCompatibilityProbe.lean`
* `NavierStokesReview/src/extensions/SelectedResidualProvenance.lean`

The upstream base/profile probe confirms that the five-moment construction is
real and contributes finite residual identities and base blow-up. The
correction-state completion confirms that the two zero rows preserve their
named radial moments. Neither result identifies those moments with the final
mixed R³ velocity, the selected pressure, the residual force, or the paper's
five named quantities.

## Disposition

The following stronger claims are rejected by the source:

1. the five-moment branch is dead code;
2. the first two rows freeze total mass or kinetic energy;
3. a compact perturbation automatically collides with the rank rows;
4. the selected endpoint is already formally inconsistent.

The surviving CTR-005 target is exact: exhibit a theorem transporting the
paper's five moments through the actual cycle, mixed sums, pressure/residual
construction, and `selected_witness`, or exhibit a zero-sorry violation of one
of those concrete equalities. Until then this is a paper-to-endpoint
correspondence failure, not a Lean proof of `False`.
