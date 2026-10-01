# Priority 234: semantic integration closure

Date: 2026-10-01  
Disposition: `CTR-005: NOT ESTABLISHED`  
Scope: production `NavierStokes/` source, selected endpoint, manuscript
correspondence

## Question

Was the repair engine bypassed, or is it used in the selected construction?
Separately, does the production endpoint prove that the completed selected
Cartesian, localised, periodised, summed fields realise the manuscript's
five observables `(M,I,J,S,C_p)`?

## Positive source result

The repair engine was not bypassed wholesale. The inspected production path
contains the following value-bearing chain:

```text
FiveRowRank / mass-preservation lemmas
  -> ActualCyclePreservation.state_* and ActualCycleCoherence
  -> ActualCycleResidualBounds.PhysicalData and residual-rate bounds
  -> GluedStageEstimates.actualStageEstimates
  -> MixedCandidateAssembly.StageEstimates.exists_schedule
  -> VanishingJointJets / three smooth sums
  -> GermCandidateAssembly.exists_candidate_witness_of_finite_stages
  -> ActualCandidateAssembly.Witness / selected_witness
```

This is not an import-only observation. The declarations are consumed as
arguments in the production terms:

* `ActualCandidateAssembly.lean:1079-1098` constructs `physicalData` and
  `estimates`; `estimates` calls
  `GluedStageEstimates.actualStageEstimates` with the actual cycle coherence,
  representations, and physical data.
* `GluedStageEstimates.lean:681-701` documents and defines the actual glued
  stage-estimate constructor. Its input includes actual `PhysicalData`; its
  construction derives the stage estimates from component bounds and the
  physical data rather than taking a physical derivative estimate as an
  external premise.
* `MixedCandidateAssembly.lean:29-65` defines the finite-stage contract. It
  contains smoothness, gain/loss data, finite background bounds, and finite
  residual jet-rate bounds. It is not the final five-observable theorem, but
  it is also not an empty generic proposition.
* `MixedCandidateAssembly.lean:67-85` derives the selected schedule and
  `VanishingJointJets` from the stage-estimate contract.
* `GermCandidateAssembly.lean:164-271` consumes that contract, support and
  extension data, and the axis construction to produce the actual mixed
  sums, force consequences, boundary jets, smooth force, residual equality,
  and speed blow-up.
* `ActualCandidateAssembly.lean:1090-1098,1121-1151,1177-1185` packages those
  actual values into `Witness`, `selected_witness`, and `selected_candidate`.

The connected hierarchy is deeper than the five-row names alone. The
production sources `IntegratedMeanBalances.lean`, `StateMomentBalances.lean`,
and `CorrectionInitialization.lean` define and use radial integrals,
weighted integrability, pressure and flux identities, torus averages, and
state-to-mean identities. Therefore the earlier claim that the repository
only had disconnected profile code or that `NativeBounds` was simply supplied
from nowhere is rejected by the source record.

## Negative source result

The positive chain does not establish the stronger proposition

\[
\operatorname{Obs}_{\mathrm{paper}}
 (u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
   =(M,I,J,S,C_p).
\]

The selected `Witness` at `ActualCandidateAssembly.lean:1121-1151`
contains the selected schedule, three potential sums, extensions, activated
velocity and pressure, a force, `CandidateProperties`, residual equality,
smoothness, support/decay, and blow-up consequences. It does not contain a
production equality identifying the completed selected fields with the
manuscript's five named observables. The inspected consumed production route
also does not provide that final semantic identification under another name.

This is not evidence that the selected values are numerically or
mathematically wrong. It is evidence that the manuscript-to-endpoint identity
has not been established by the current production theorem boundary.

## Why this is not contradictory

The following propositions are distinct:

1. `RepairUsed`: finite/profile correction data feed the selected residual
   construction.
2. `EndpointConsequences`: the selected construction has smooth force,
   residual equality, and speed blow-up under the terms proved in the source.
3. `ObservableBridge`: the final selected Cartesian/localised/periodised/
   summed fields equal the manuscript's `(M,I,J,S,C_p)` observables.
4. `SelectedMismatch`: those final observables differ from the manuscript
   tuple.

The source presently supports (1) and the stated endpoint consequences in
(2). It does not establish (3), and no value-level theorem establishes (4).
`CTR-005` concerns the missing implication from the manuscript's mechanism to
the exported endpoint, not a claim that the repair engine was unused.

## Required closure work

The remaining work is not a name search or a toy model. It must:

1. trace the actual selected `ASum`, `BSum`, and `PSum` through curl,
   localisation, periodisation, finite sums, and `tsum`;
2. discharge support, integrability, and pointwise composition hypotheses for
   the selected objects;
3. compare the resulting radial/state observables with the manuscript
   definitions; and
4. search alternate declarations, generated modules, and Git history before
   retaining the bounded statement “no production theorem located”.

Until that closure produces either the final bridge or a concrete mismatch,
the controlled status remains `CTR-005: NOT ESTABLISHED`.

Evidence sources:

* `NavierStokesReview/evidence/priority_232_repair_engine_usage_and_observable_boundary_2026-10-01.json`
* `NavierStokesReview/evidence/priority_233_moment_hierarchy_semantic_boundary_2026-10-01.json`
* `NavierStokesReview/evidence/priority_232_symbol_search_raw_2026-10-01.txt`
