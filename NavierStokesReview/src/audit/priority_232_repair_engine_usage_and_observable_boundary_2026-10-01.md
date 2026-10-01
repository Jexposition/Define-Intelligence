# Priority 232: repair-engine usage versus final observable boundary

Date: 2026-10-01  
Status: source-checked against production declarations  
Disposition: internal repair integration established; final manuscript-observable correspondence not established

## Question

The earlier phrase “the packaging fact is not evidence that the repair engine
was bypassed” was too weak on its own. This audit resolves the two propositions
separately:

1. Was the five-row/rank repair machinery actually consumed by the selected
   production construction?
2. Does the inspected production endpoint prove that the completed selected
   Cartesian, localised, periodised, summed field realises the manuscript’s
   named `(M,I,J,S,C_p)` observables?

They are not the same proposition.

## Positive production evidence: no wholesale bypass

The following source chain is a positive dependency chain, not an inference
from imports or names alone.

| Stage | Production declaration | What the source establishes |
|---|---|---|
| Row construction | `FiveRowRank.FiveRows`, `FiveRowRank.exists_five_row_repair` (`NavierStokes/FiveRowRank.lean`) | Correction rows are constructed with support, rank, and exact moment-row statements. |
| Actual rank use | `DefectIncrementBounds.fiveRows`, `DefectIncrementBounds.solved_rows`, `DefectIncrementBounds.fiveRows_preserve_masses` (`NavierStokes/DefectIncrementBounds.lean:635-682, 773-823`) | The actual rank increment, not merely a desired abstract increment, is used to cancel measured defects and preserve the two mass rows. |
| Cycle state | `ActualCyclePreservation.state_runInvariant`, `state_particularData`, `state_waveData`, `state_wave_transport`, `state_coherent` (`NavierStokes/ActualCyclePreservation.lean:826-912`) | The corrected invariant and transported analytic/wave data are carried through the actual cycle state. |
| Physical data | `ActualCandidateAssembly.physicalData` (`NavierStokes/ActualCandidateAssembly.lean:1079-1085`) | Actual cycle states, uncut velocity prefixes, and pressure prefixes are passed to `ActualCycleResidualBounds.PhysicalData`. |
| Residual rates | `ActualCycleResidualBounds.Invariant.residual_jetRate` and `finite_residual_rates` (`NavierStokes/ActualCycleResidualBounds.lean:1158-1208`) | The actual invariant and physical data produce residual jet-rate information for the cycle family. |
| Selected estimates | `GluedStageEstimates.actualStageEstimates` through `ActualCandidateAssembly.estimates` (`NavierStokes/ActualCandidateAssembly.lean:1087-1098`) | The concrete physical-data and residual-rate route is used to build the selected stage-estimate object. |
| Endpoint | `ActualCandidateAssembly.Witness` and `witness` (`NavierStokes/ActualCandidateAssembly.lean:1121-1185`) | The selected schedules, sums, extensions, force, consequences, decay, and boundary limits are packaged into the exported proposition. |

This supports the precise verdict:

> The repair engine was not bypassed wholesale. Its finite-stage correction
> information is consumed downstream in the selected construction.

That statement does **not** say that every manuscript observable has been
transported to the final field.

## Negative endpoint evidence: the semantic edge remains open

The endpoint `Witness` contains the selected sums and their analytic
consequences, but the inspected production type contains no declaration that
has the following role:

\[
  \operatorname{Obs}_{\mathrm{paper}}
  (u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  = (M,I,J,S,C_p).
\]

The review-side Priority 230 and 231 completions now expose the actual selected
radial composition and its weighted-integral reduction. They intentionally
retain the pointwise coordinate, differentiability, support, and integrability
hypotheses. Those hypotheses are not silently obtained from `Witness`, and the
completions do not assign a value to the resulting integral.

The remaining semantic route is therefore:

\[
\text{cycle repair coordinates}
\to \text{selected sums}
\to \text{curl/cutoff commutator}
\to \text{periodisation}
\to \text{torus average and radial integral}
\to \text{pressure convention and residual/force observables}.
\]

The source record positively establishes the first internal route and does not
establish the final equality. It does not prove that the equality is false.

## Adjudication

| Proposition | Status | Reason |
|---|---|---|
| The five-row/rank repair engine is used in the selected production route | **Established** | The actual rank lemmas feed the cycle invariant, physical data, residual rates, estimates, and `Witness`. |
| The selected endpoint is merely a generic rate contract with no concrete upstream construction | **Rejected** | `physicalData`, `finite_residual_rates`, and `actualStageEstimates` are concrete production declarations. |
| The exported endpoint proves the full manuscript-observable identity `(M,I,J,S,C_p)` after all selected-field transformations | **Not established** | No consumed production declaration with that completed semantic type was located; the value-level completions still retain explicit hypotheses. |
| The repair engine is mathematically irrelevant to the blow-up construction | **Rejected** | The selected endpoint consumes repaired data upstream; the local `origin_blowup` conjunct is not an independence proof for the full conjunction. |
| The selected observable identity is false | **Not established** | No direct mismatch or impossibility theorem has been proved. |

Accordingly, `CTR-005` is a correspondence failure for the complete
paper-to-endpoint claim, not a claim that the repair engine was absent or
bypassed wholesale.

## Evidence links

- `src/audit/priority_229_manuscript_dependency_declaration_ledger_2026-10-01.md`
- `evidence/priority_230_selected_mixed_full_product_rule_2026-10-01.md`
- `evidence/priority_231_selected_mixed_radial_integral_composition_2026-10-01.md`
- `src/probes/SelectedBaseMomentCompatibilityProbe.lean`
- `src/probes/SelectedWitnessPathProbe.lean`
- `src/extensions/SelectedEndpointMomentTransportObstruction.lean`

## Next test

The next admissible escalation is a source-level theorem or counterexample for
the remaining completed observable composition. Until that is obtained, the
controlled disposition remains `CTR-005: NOT ESTABLISHED`, with no promotion to
a selected mismatch, force nonsmoothness, literal CMI failure, impossibility,
or `False`.
