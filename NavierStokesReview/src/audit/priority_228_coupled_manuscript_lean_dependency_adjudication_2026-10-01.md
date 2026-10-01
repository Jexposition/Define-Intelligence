# Priority 228: coupled manuscript-to-Lean dependency adjudication

Date: 2026-10-01  
Status: source-checked; endpoint semantic edge remains open  
Scientific disposition: `CTR-005: NOT ESTABLISHED`

## Question

The earlier wording said that the absence of a named five-tuple field in
`ActualCandidateAssembly.Witness` was “not evidence that the repair engine was
bypassed”. That wording was incomplete. This audit separates the four claims
that must not be conflated:

1. the repair mathematics exists;
2. the repair mathematics is used by the actual selected construction;
3. its internal invariant is identified with the manuscript's five named
   observables after the complete selected-field composition;
4. the public endpoint therefore certifies the manuscript's complete proof.

The first two are positively supported. The third was not located in the
inspected production source. The fourth therefore remains unestablished.

## Authority and method

The source order for this adjudication is:

1. live production Lean declarations in `NavierStokes/`;
2. the extracted manuscript `docs/navier-stokes openai.txt`;
3. compiled review probes and evidence records;
4. current document-control and historical audit notes.

Names, imports, compilation, and interface co-occurrence were not treated as
proof of a value-level identity. A positive claim below is tied to a theorem
signature and its consuming declaration. A negative claim is limited to the
inspected production closure and is not an impossibility theorem.

## Manuscript dependency ledger

| Manuscript mechanism | Mathematical role in the paper | Lean evidence | Adjudication |
|---|---|---|---|
| Five profile integrals | Match pressure datum, radial velocity, stress, and exterior tails at profile joins | `docs/navier-stokes openai.txt:470-560`, `1426-1588`, `8091-8511`; `NominalProfile.FiveMomentCertificate`, `NominalProfile.Witness.five_moments` | Real reduced-profile mathematics is present and used upstream |
| Modulation restoration | Modulation changes the five profile functions by (O(N^{-1})), then five bumps restore the exact profile moments | Manuscript `:2190-2347`, `:8447-8511`; `NominalProfile`, `PositiveOrderMoments`, `FiveRowRank` | The profile-level correction engine is substantive |
| Correction cycle | Two preserved mass rows and three rows cancelling (P,J_\theta,J_z) defects | Manuscript `:697-735`, `4622-4915`; `DefectIncrementBounds.fiveRows_preserve_masses`, `linearRows_eq_neg_of_fiveRows`, `RankGeometry.solved_rows` | The actual rank/correction path consumes these local identities |
| Curl and cutoff corrections | Recompute the full residual, retain curl/cutoff terms, and preserve divergence freedom by cutting potentials before curl | Manuscript `:562-735`, `2964-3065`; `SpatialLocalization.cutVelocity_product_rule`, `MixedPeriodicAssembly.periodicVelocity` | These operations are part of the construction, not omitted from the paper or Lean route |
| Summation and flatness | Locally finite shrinking-cutoff sum, finite-prefix residual comparison, all-order residual flatness | Manuscript `:746-784`, `2964-3065`; `LocalResidualFlatness.exists_schedule_all_jetRates`, `ActualCycleResidualBounds.finite_residual_rates` | Actual rate/flatness route is proved from selected construction data |
| Smooth force extension | Extend the actual residual through (t=1) from derivative recurrence and locally uniform residual limits | Manuscript `:6072-6240`; `CandidateFromLimits.tracedResidual_smooth`, `force_smooth`, `force_eq_activated_residual` | Force regularity is derived from residual-jet data, not inserted as a bare `ContDiff` premise |
| Public endpoint | Package the selected sums, extensions, force, candidate consequences, decay, boundary jets, and blow-up | `ActualCandidateAssembly.Witness:1121-1151`, `selected_witness:1177-1181` | The endpoint is genuine, but its public proposition has no final named five-observable equality |

## Positive proof that the repair engine is not bypassed wholesale

The following chain is a positive source trace, not an inference from import
reachability:

```text
NominalProfile / PositiveOrderMoments / FiveRowRank
    -> local five-row profile and rank corrections
    -> DefectIncrementBounds.fiveRows_preserve_masses
       and RankGeometry.solved_rows
    -> ActualCyclePreservation.Invariant
       (masses, debt, residual, regularity fields)
    -> ActualCycleResidualBounds.Invariant.residual_jetRate
    -> ActualCycleResidualBounds.finite_residual_rates
    -> ActualStageEstimates.stageEstimates_of_representations
    -> GluedStageEstimates.actualStageEstimates
    -> LocalResidualFlatness.selected_schedule
    -> CandidateFromLimits.force_smooth / force_eq_activated_residual
    -> ActualCandidateAssembly.Witness / selected_witness
```

The decisive production signatures are:

- `DefectIncrementBounds.fiveRows_preserve_masses` proves preservation of the
  two exact radial mass rows for the actual rank stage.
- `DefectIncrementBounds.RankGeometry.solved_rows` proves the three linear rows
  equal the negative measured defects for the actual rank increment.
- `CorrectionStep.CycleAnalyticInvariant` stores `debt` and `masses` as fields
  of the actual cycle invariant, alongside residual and regularity data.
- `ActualCycleResidualBounds.Invariant.residual_jetRate` consumes the actual
  invariant and `PhysicalData` to produce a residual jet-rate theorem.
- `ActualCycleResidualBounds.finite_residual_rates` is called by
  `ActualStageEstimates.stageEstimates_of_representations`, which is called by
  `GluedStageEstimates.actualStageEstimates`, which constructs the estimates
  used by `ActualCandidateAssembly.estimates`.
- `ActualCandidateAssembly.Witness` uses the actual `potentialSum`, direct sum,
  pressure sum, activated fields, forcing, candidate consequences, decay, and
  boundary limits.

This rules out the claim that the five-row/rank mechanism was wholly dead,
unused, or bypassed by a zero-field rate shell. It also corrects the weaker
wording “not evidence of bypass”: the source contains affirmative evidence of
internal integration.

## The exact unresolved edge

The positive chain does not prove the stronger composition below:

\[
\begin{aligned}
&\text{NominalProfile / rank invariant} \\
&\quad\Longrightarrow
\operatorname{Moments}_{\mathrm{paper}}
  (u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  =(M,I,J,S,C_p),
\end{aligned}
\]

where the right-hand side is evaluated on the completed selected Cartesian
field after the actual infinite sums, curls, potential cutoffs, periodisation,
torus averaging, radial integration, pressure construction, residual, and
force export.

The production source does define lower-level moment operators. For example,
`DefectIncrementBounds.barMoment_apply` identifies `barMoment` with a weighted
radial integral of a torus average, and `FiveRowRank.FiveRows` proves five local
rows for reduced correction fields. Those declarations do not, in the
inspected selected closure, conclude an equality between the final
`MixedPeriodicAssembly.periodicVelocity`/activated fields and the manuscript's
five profile functions. Nor does `Witness` require such an equality.

The review-side AX-033/ghost-debt probes establish only that the `Witness`
proposition does not entail an arbitrary abstract five-coordinate debt being
zero. They do not prove that the concrete selected physical field has a
nonzero debt. That distinction is essential.

## Four-way verdict

| Claim | Current status |
|---|---|
| “The five-moment/rank machinery is absent.” | **Rejected by source evidence.** |
| “The machinery is wholly bypassed by the selected construction.” | **Not supported; internal consumption is positively traced.** |
| “The internal invariant is fully transported to the manuscript's final five observables.” | **Not established in the inspected production endpoint.** |
| “The selected construction therefore proves the complete manuscript/CMI claim.” | **Not established by the current paper-to-endpoint record.** |

The controlled conclusion is therefore:

> **The repair engine is partially integrated and load-bearing inside the
> selected construction, but the final semantic correspondence from its
> internal invariant to the manuscript's ((M,I,J,S,C_p)) observables remains
> unclosed at the exported endpoint.**

This is neither a claim that the engine was bypassed nor a claim that the
selected field has a nonzero defect. It is an adverse correspondence finding:
the current Lean proposition proves its own residual/force/blow-up contract,
but the inspected source does not yet establish that this contract is the
complete five-observable construction described by the manuscript.

## Why Lean can compile without the missing edge

Lean checks the proposition actually declared. `Witness` can be inhabited if
the selected schedule, actual sums, residual limits, smooth force, candidate
consequences, decay, and blow-up premises are proved. It does not need a
separately named five-observable field unless that equality is part of the
proposition or an argument required by a theorem used to construct it.

This is not evidence of a compiler cheat. `noncomputable` definitions are
expected for analytic choices and infinite-sum constructions, and the current
selected endpoint audits report only standard foundational dependencies. The
problem is specification correspondence: a sound kernel can verify a weaker
or differently packaged proposition than the full prose-level claim it is
being used to advertise.

## Required next proof, without assuming the answer

The next task is a declaration-level and value-level crosswalk, not another
name scan:

1. instantiate the actual selected sums in the manuscript's five observable
   definitions;
2. prove the exact pointwise/chart identities needed to identify the selected
   cylindrical components and pressure convention;
3. prove passage through curl-before-cutoff, periodisation, torus averaging,
   radial integration, and the locally finite `tsum`;
4. prove the resulting five identities, or derive a concrete mismatch from
   the same definitions;
5. only then change `CTR-005` to a stronger disposition.

Until that calculation is complete, “partially integrated, endpoint
correspondence unresolved” is the strongest source-supported statement.

## Reproduction note

The source-level selected-transport census completed successfully and is
recorded in the linked evidence files. A fresh closure-aware replay against
the retained 366 MB environment graph was also attempted, but exceeded the
120-second execution limit and was stopped. It produced no evidence output
and is not used to support the verdict. The existing pinned closure record
at Priority 212 remains the authority for the six-root no-`sorryAx` and
standard-axiom results; the present Priority 228 result is based on the live
production declarations and the completed source census.

## Evidence links

- `../../evidence/priority_228_coupled_manuscript_lean_dependency_adjudication_2026-10-01.md`
- `../../evidence/priority_228_selected_transport_census_2026-10-01.md`
- `../../evidence/priority_228_selected_transport_census_2026-10-01.json`
- `priority_203_internal_to_endpoint_crossfile_trace_2026-09-30.md`
- `priority_200_connected_cmi_manuscript_crosswalk_2026-09-30.md`
- `priority_211_selected_transport_whole_tree_2026-09-30.md`
- `priority_227_selected_periodic_support_gate_replay_2026-10-01.md`
