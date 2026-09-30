# Priority 205: endpoint census and completion adjudication

Date: 2026-09-30

## Purpose

This tranche re-runs the existing endpoint source census and the review-probe
logic-contract audit, then manually checks every active lexical bridge
candidate and the one review-authored `manual_transport_candidate`. It is a
source and proof-scope reconciliation, not a numerical field calculation.

## Reproduction

The canonical V-lab Python environment ran:

```text
python NavierStokesReview/src/audit/selected_endpoint_source_census.py
python NavierStokesReview/src/audit/probe_logic_contract_audit.py
```

The source census was run from the repository root with endpoint roots
`NavierStokes.R3.Theorem` and `NavierStokes.ActualCandidateAssembly`.

## Machine results

- Whole-repository source census: 2,797 files, 649,766 lines, 7,530 import
  edges.
- Selected endpoint closure: 588 local modules, 380,791 lines, 2,378 import
  edges, and **0 missing local imports**.
- Parsed declarations: 50,208 total, 31,882 in the selected closure.
- Lexical moment/endpoint co-occurrence candidates: 7 in the selected closure.
- Review-probe declarations audited: 264.
- Review-probe audit result: 0 unconditional endpoint claims authorised by
  the instrument.

The whole-repository figure and the direct `NavierStokes/` figure of 817 Lean
files are different scopes. Neither is a claim that the remaining repository
files are dead or unreachable in OpenAI's own build graph.

## The seven production-side lexical candidates

The seven candidates are:

1. `ActualPhysicalStageBounds.initialDirect_rate`
   (`NavierStokes/ActualPhysicalStageBounds.lean:595-605`): a `JetRate`
   theorem for an angular field.
2. `ActualPhysicalStageBounds.background_from_representations`
   (`:726-...`): a `JetRate` theorem for represented velocity stages.
3. `GermCandidateAssembly.potentialSum_eq_base_germ`
   (`NavierStokes/GermCandidateAssembly.lean:75-95`): an eventual germ
   equality for a potential sum near the base plateau.
4. `InitializedPhysicalBackground.directIncrement_rate`
   (`NavierStokes/InitializedPhysicalBackground.lean:93-103`): another
   `JetRate` theorem.
5. `MixedAxisPreservation.origin_blowup_global`
   (`NavierStokes/MixedAxisPreservation.lean:470-487`): the axis blow-up
   transfer under eventual zero stage germs.
6. `MixedCandidateAssembly.StageEstimates.exists_schedule`
   (`NavierStokes/MixedCandidateAssembly.lean:67-90`): schedule and
   `VanishingJointJets` extraction from `StageEstimates`.
7. `MixedCandidateWitness.SelectedSchedule`
   (`NavierStokes/MixedCandidateWitness.lean:25-31`): the schedule predicate
   containing smooth sums and vanishing residual jets.

None of these declarations has a conclusion identifying the final selected
Cartesian velocity, pressure, residual, or force with the manuscript tuple
`(M,I,J,S,C_p)`. The apparent co-occurrences arise from a `NominalProfile`
parameter or from rate/field terms, not from a moment-transport equality.

## Review-side manual candidate

`NavierStokesReview/src/completions/SelectedBarMomentInterface.lean:32-39`
proves:

```text
barMoment k (pullbackScalar φ (selectedPotentialComponent j)) n p
  = ∫ r, r ^ k * torusAverage (...) (r,p)
```

This is a correct definitional rewrite for an explicitly supplied map `φ` and
pullback. The same file defines
`SelectedBarMomentTransportData` at lines 46-52, requiring the caller to
supply `pointToSpaceTime` and `scalarProfile_eq_selected`. Its comment at
lines 41-44 explicitly records that `selected_witness` exports neither
object. The lemma therefore exposes the missing data obligation; it does not
prove that the production selected path supplies it.

`PeriodicGlobalIntegral.selected_mixed_barMoment_zero_of_positive_pullback`
is conditional on a positivity premise and uses non-integrability of a
periodic pullback. It is not a selected-field moment value. The probes
`ActualCandidateAssemblyIsolationProbe` and `SelectedWitnessPathProbe` also
state that their conclusions are type-boundary observations, not selected
physical defects.

## Controlled conclusion

The new sweep does not discover a hidden production bridge. It confirms the
bounded finding already recorded in Priorities 199--204:

> The selected construction has genuine internal profile, rank, residual,
> localisation, force, and blow-up machinery, but the inspected production
> endpoint does not expose a compiled theorem identifying its final selected
> Cartesian observables with `(M,I,J,S,C_p)`.

Therefore `CTR-005` remains **NOT ESTABLISHED** for complete
manuscript-to-selected-endpoint correspondence. This tranche does **not**
prove a nonzero selected defect, force nonsmoothness, literal CMI failure,
impossibility, a compiler cheat, or `False`.

## Linked records

- `evidence/selected_endpoint_source_census_2026-09-30.md`
- `evidence/selected_transport_audit_2026-09-30.md`
- `src/audit/priority_199_selected_endpoint_declaration_crosscheck_2026-09-30.md`
- `src/audit/priority_201_selected_closure_census_2026-09-30.md`
- `src/audit/priority_202_actual_moment_invariant_trace_2026-09-30.md`
- `src/extensions/SelectedEndpointMomentTransportObstruction.lean`
- `src/completions/SelectedBarMomentInterface.lean`
