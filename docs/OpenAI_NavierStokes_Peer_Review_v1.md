# Independent peer review of the OpenAI Navier–Stokes formalisation

## Current selected-support correction: Priority 227 (2026-10-01)

The selected periodic-support gate replay is
[`priority_227_selected_periodic_support_gate_replay_2026-10-01.md`](../NavierStokesReview/src/audit/priority_227_selected_periodic_support_gate_replay_2026-10-01.md),
with evidence in
[`selected_periodic_support_gate_replay_2026-10-01.md`](../NavierStokesReview/evidence/selected_periodic_support_gate_replay_2026-10-01.md).
It is a compiled conditional gate, not a selected-field refutation. The exact
support and nonzero transport premises remain open, so the controlled status
stays `CTR-005: NOT ESTABLISHED`.

## Current release correction: Priority 226 (2026-10-01)

The verified private/public release state is
[`priority_226_release_state_2026-10-01.md`](../NavierStokesReview/src/audit/priority_226_release_state_2026-10-01.md).
It is a dated release snapshot; the scientific disposition is unchanged.

## Current evidence correction: Priority 225 (2026-10-01)

The latest selected-field gate is
[`selected_mixed_barmoment_shell_gate_2026-10-01.md`](../NavierStokesReview/evidence/selected_mixed_barmoment_shell_gate_2026-10-01.md).
It closes finite-prefix and conditional branch-linearity checks while
preserving the explicit final support/integrability gate. It does not change
the active disposition: `CTR-005: NOT ESTABLISHED`.

## Current control correction: Priority 224 (2026-10-01)

The current corpus re-grounding is
[`priority_224_workspace_corpus_regrounding_2026-10-01.md`](../NavierStokesReview/src/audit/priority_224_workspace_corpus_regrounding_2026-10-01.md).
It supersedes older navigation pointers only. Current endpoint evidence is
Priorities 218, 221, and 223. The active disposition remains
`CTR-005: NOT ESTABLISHED`, not a selected-field defect or literal CMI
failure.

## Current control correction: Priority 214 (2026-09-30)

The current tree reconciliation is
`../NavierStokesReview/evidence/tree_reconciliation_current_2026-09-30.md`.
It supersedes the dated tree snapshot for current bookkeeping only: 49 tree
entries, 47 file entries, 3,466 checkout files, 47 explicit tree-relative
resolutions, 0 missing entries, and 0 ambiguities. The older
report remains historical evidence. The current Git inventory contains two
intentional untracked rows: the protected `NavierStokes/R3/TestPressure.lean`
source file and the raw 366 MB environment-closure JSON, which remains local
by design. This control correction does not change `CTR-005: NOT ESTABLISHED`
or promote a selected-field defect, force-nonsmoothness result, literal CMI
failure, impossibility theorem, compiler-cheat claim, or `False`.

## Current source correction: Priority 203 (2026-09-30)

The latest cross-file trace confirms that the selected construction contains a
real internal invariant: two preserved mean-mass identities and three
residual-debt classes. Those data feed actual physical fields, residual-rate
estimates, force extension, and the exported candidate. The unresolved
`CTR-005` finding is narrower than “moment machinery is absent”: the inspected
selected closure still does not expose a production theorem identifying that
internal structure with the manuscript’s named `(M,I,J,S,C_p)` observables
after the final Cartesian/periodic/localised/summed field construction.

Evidence: `NavierStokesReview/src/audit/priority_203_internal_to_endpoint_crossfile_trace_2026-09-30.md`.

## Document control and current evidence

This review is governed by
[`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md) and
[`DOCUMENTATION_RECONCILIATION_2026-09-30.md`](DOCUMENTATION_RECONCILIATION_2026-09-30.md).
Current endpoint findings must be checked against the Priority 218, 221, and
223 source reviews and matching evidence files in `NavierStokesReview/src/audit/`
and `NavierStokesReview/evidence/`, together with the earlier 186–204 source
reviews. Dated tranche notes are historical
evidence, not competing live verdicts. Priority 204 is scope control only: it
reconciles the repository census, effective fork register, indexed-file count,
and selected endpoint closure. Its 29-row disposition ledger is not a count
of currently Git-untracked files. The current Git state has two intentional
untracked rows, recorded separately in document control: the protected
author-side `NavierStokes/R3/TestPressure.lean` file and the local generated
366 MB environment-closure JSON excluded from the public release.

This review is the decision document accompanying the [research paper](OpenAI_NavierStokes_Research_Paper.md). The paper presents the publication-level argument; this file records the review decision, source-level findings, corrections to earlier objections, and questions that remain open. The detailed evidence is retained in the [NavierStokesReview evidence dossier](../NavierStokesReview/evidence/evidence_tree.md) and the linked source reviews.

Read the [research paper's Executive Verdict](OpenAI_NavierStokes_Research_Paper.md#executive-verdict) for the argument in manuscript order. Do not treat the dated audit state below as a substitute for that argument.

## Live audit state: Priority 209 (2026-09-30)

The authoritative register currently records 2,797 indexed modules, 588
modules in the captured Navier–Stokes endpoint closure, 2,209 rows outside
that closure, 906 evidence-inspected rows, 1,884 source-indexed rows still
queued for semantic review, 0 missing project import edges, 10 source rows
containing a `sorry` token, and 86 supplemental evidence records. Seven rows
carry the specific `source_indexed_sorry_token` status; three lexical rows are
already evidence-inspected. “Outside the captured endpoint closure” is a
scope label, not a claim that a module is dead or unreachable in OpenAI’s own
build graph. The full-repository review remains active.

### Superseding source adjudication: moment/rank restoration (2026-09-29)

The earlier review language describing CTR-005 as a missing selected-path
five-moment transport theorem was too strong and is withdrawn in that form.
Raw source inspection shows that the profile moment and rank-repair machinery
is not merely imported: it is used to establish coefficient matches and the
finite Cartesian residual identity, which then feeds residual rates,
all-order flatness, actual physical data, and the candidate properties.

`ActualCandidateAssembly.Witness` does not repeat the reduced-profile
certificate as a named `(M,I,J,S,C_p)` field. That packaging fact is not a
proof that the mechanism was bypassed, nor is it a CMI refutation. The active
review question is now exact semantic correspondence: whether the proved
reduced-profile consequences, selected fields, pressure, force, support, and
global endpoint have precisely the scope claimed in the paper and required by
the CMI formulation. No nonzero selected-field defect, impossibility theorem,
or `False` has been established by the tuple omission.

## Audit evidence update: Priority 154–155 source tranches (2026-09-29)

The manuscript record now links the latest source-grounded reviews rather than
leaving them only in the audit register:

- [Priority 154: Euler transport, frame, and heat-source review](../NavierStokesReview/src/audit/priority_154_euler_transport_frame_heat_source_review_2026-09-29.md)
- [Priority 154 machine-readable evidence](../NavierStokesReview/evidence/source_tranche_euler_transport_frame_heat_2026-09-29.json)
- [Priority 155: Euler Gaussian and Gevrey review](../NavierStokesReview/src/audit/priority_155_euler_gaussian_gevrey_source_review_2026-09-29.md)
- [Priority 155 machine-readable evidence](../NavierStokesReview/evidence/source_tranche_euler_gaussian_gevrey_2026-09-29.json)
- [Current semantic coverage register](../NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-29.md)

These tranches record genuine conditional transport, heat, Gaussian, and
Gevrey infrastructure. They do not establish the selected Navier–Stokes
endpoint or the final Cartesian transport of `(M,I,J,S,C_p)`. They also do not
establish a nonzero defect, impossibility theorem, or kernel `False`. The
current classification therefore remains a selected-field correspondence
failure (`CTR-005`), not an assertion that the upstream moment machinery is
absent.

### Current source tiers

The cumulative source review records real R3 competitor exclusion and energy
consequences, positive-radius Cartesian potential/curl bridges, torus-average
and radial-weight identities, primary and periodised-copy bounds, slow-axis
identities, moving-strip moment/rank estimates, and comparative pressure-test
bounds. These are substantive intermediate results.

They do not establish the final selected-field equality for `(M,I,J,S,C_p)`
through sum, curl/localisation, periodisation, torus averaging, radial
pullback, support/integrability, and the axis route. No nonzero defect,
impossibility theorem, or kernel `False` was obtained. The live register
counts above are authoritative; older tranche counts remain historical
provenance only.

## Publication decision

**Do not accept the published claim that this repository supplies a solution of
the Navier–Stokes problem on the inspected record.** The object under review

is the solution claim OpenAI published, not a merely compiling endpoint and
not an optional implementation detail. The source exports an R³ C/D-shaped
proposition, but the proof record does not expose the selected-field theorem
identifying that endpoint with the five-moment construction used to justify
the paper's claim. That is an affirmative failure to discharge the burden of
proof for the published solution. `NOT FORMALLY REFUTED` remains only the
narrow status that this review has not yet derived a kernel-level `False` from
the selected endpoint.

## Scope correction: literal C/D theorem versus advertised mechanism

The whole-space endpoint must be reviewed separately from the paper's
five-moment explanation. `NavierStokes/R3/Theorem.lean:27-53` exports the
literal R³ C/D breakdown proposition, and residual-defined forcing is not by
itself a contradiction of that existential target. The live adverse finding is
that the final selected export does not expose the paper tuple
$$
(M,I,J,S,C_p)
$$
as an identity for the mixed velocity, pressure, residual, and force. That is
a failure to establish the advertised mechanism, not a completed `False`
theorem for the literal endpoint.

## Finding 18: base-profile geometry is not a one-component collapse

The reduced `(t, s, z)` profile is embedded into three Cartesian basis directions before spatial curl. The only proven zero is on the radial gauge anchor. No global zero-swirl theorem was found.

## Finding 19: the selected-interface bridge remains the real objection

The repository has genuine upstream five-moment repair algebra, but the generic finite-stage summation interface does not state that the selected stages preserve the paper's named moments through the final residual and force construction. This is a correspondence gap, not yet a zero-sorry contradiction.

The force boundary must also be quoted accurately: the zero-force branch starts at `t ≥ 2`, not `t ≥ 1`; `force_smooth` is conditional on residual-jet and extension premises.

The review's source-to-claim route is set out in
[`SEMANTIC_CORRESPONDENCE_MAP.md`](SEMANTIC_CORRESPONDENCE_MAP.md). This is
important because the issue is not a missing filename or a failed compiler
run. The source contains the relevant moment, correction, pressure, residual,
and R3 modules. The unresolved question is whether the identities proved for
those layers are transported to the actual selected Cartesian field consumed
by `CandidateProperties`. In particular, stagewise and finite-prefix results
must not be silently read as a theorem for the final infinite mixed sum,
torus-average/radial moment, or absolute pressure representative.

## Finding 20: local and exported composition are not one exposed theorem

`LocalResidualFlatness` and `LocalPaperTheorem` work with the selected raw
stage aliases and a supplied schedule. The public whole-space endpoint is
instead extracted from `ActualCandidateAssembly.Witness` and then passed
through the R³ localisation layer. `PaperLocalization` proves local agreement
of velocity and pressure on an open set at late times, but the combined result
does not state equality of the forces or identify the five named moments with
the exported residual. The inspected record therefore does not establish that
the local five-moment construction is the object used by the CMI endpoint.

This strengthens CTR-005 as a source-level failure of the authors' affirmative
proof record. It is sufficient to withhold acceptance of the paper's advertised
Navier–Stokes solution claim; the reviewer is not required to derive `False` merely because OpenAI
the composition theorem is absent from the inspected record. It does not,
however, assert that
`selected_candidate` has already been refuted at the Lean-kernel level.

## Finding 21: the compact-pressure attack does not replace the correspondence failure

The R³ candidate imposes compact support on each pre-singular pressure slice.
That condition is an adversarial audit target, but the inspected comparison
path does not simply set pressure to zero. `PressureRecovery` derives the
differentiated Poisson identity against compact tests from the residual
equations; `ActualPressureFlux` and `PressureFlux` turn it into the uniform
cutoff flux bound; and `WholeSpaceComparisonClosure` constructs the scalar rate
estimate internally. The intermediate axiom probe reports only standard Lean
foundations for these endpoints.

The claim that compact pressure support forces the candidate velocity to vanish
is therefore rejected as a standalone counterexample. It does not answer the
load-bearing objection: the selected-path theorem still does not identify the
paper's named moments and force with the fields consumed by the exported R³
endpoint. That correspondence claim remains unestablished.

## Finding 22: response summaries require four scope qualifications

The current source supports the main outline of the supplied technical
summaries, but several formulations would overstate the evidence if copied
without qualification.

First, `FiveRowPositiveOrderBridgeProbe.lean` proves an algebraic identity for
the repair maps under the promotion
`(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)`. It does not identify the selected Cartesian
field with the paper's `(M,I,J,S,C_p)` integrals, and it does not transport that
identity through the residual and force estimates. The bridge repairs the
algebraic objection; it does not close CTR-005.

Second, the residual-defined force satisfies the repository's formal
existential candidate predicate. That is not a ruling on the phrase “given,
externally applied force” in the CMI problem description. The formal predicate
contains smoothness, support, residual, energy, and blow-up fields, but no
independence axiom. The provenance criticism is therefore material and worth
reviewing, but it is not by itself a Lean contradiction of C or D.

Third, force cancellation at the origin is a local endpoint result. The source
proves residual equality on `0 < t < 1` and supplies a smooth extension at the
endpoint; the selected force tends to zero at the origin. This does not prove a
global force norm statement or that the force is nonzero at every point at
time one.

Fourth, the generic zero-velocity and five-debt probes establish interface
non-implication, not emptiness of the selected witness. The selected-label
construction gives explicit witnesses for the selected primary label and
active pair. The exact adjudication is recorded in
`NavierStokesReview/evidence/response_claims_adjudication_2026-09-24.md`.

These qualifications do not convert the review into a repair request. The
current source record is insufficient to accept the selected-path
identifications and analytic premises used by the published claim. The phrase
“not formally refuted” reports only that the current Lean attack has not
derived `False`; it does not mean that the unproved paper-to-endpoint bridge
is presumed valid. The active programme is adversarial: derive a concrete
contradiction where possible, or independently close a gap only after the
source survives that test.

## Finding 23: the burden of proof is asymmetric

The review should not be framed as though the advertised claim and the review
carry equal burdens. OpenAI made the CMI-level claim, but the inspected source
record does not establish the object and hypotheses presented in the paper. A
compiling existential endpoint is not enough to establish the advertised paper
solution claim when the selected witness does not export the paper's
five-moment identity or its transport into the residual and force.

The correct conclusion is therefore affirmative but limited: the published
claim is **not established** by the inspected paper-to-code record. This is
the review verdict because the inspected record does not identify the selected
construction with the five-moment mechanism and its analytic composition. “Not
formally refuted” is only a subordinate
report that the current Lean search has not derived `False`; it is not evidence
that the authors' unproved bridges hold, and it is not a reason to defer the
negative review conclusion.

The missing object is a field-level composition theorem starting at the actual
selected stages and ending at the paper tuple, residual, pressure, force, and
analytic endpoint consequences. The review records its absence and rejects the
advertised claim on that basis; it does not supply a repair for the source.

Evidence: `NavierStokesReview/evidence/burden_of_proof_underclaim_audit_2026-09-24.md`.

## Recommendation

**Do not treat the endpoint's successful compilation as proof of the published
paper's complete CMI interpretation.** Raw source inspection now establishes
that the profile moment/rank repair chain is used to obtain coefficient
matching, finite Cartesian residual identities, residual estimates, selected
physical data, and candidate properties. The earlier claim that this engine
was missing from the selected proof is withdrawn.

The public `Witness` does not repeat the reduced-profile certificate as a
named `(M,I,J,S,C_p)` field, but that omission is not a proof of a failed
construction. The remaining review must test each claimed CMI condition and
paper consequence for the same selected fields, pressure, force, support, and
global endpoint. No concrete mismatch, impossibility theorem, or `False` has
been proved by tuple absence.

## Materials and scope

The review targets commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd` in the fork branch `review/cmi-first-navier-stokes-2026-09-22`. The downloaded non-Git directory is treated as a historical comparison snapshot. No upstream source file was edited.

The audit separates four questions:

1. Does the code elaborate and kernel-check?
2. What exact proposition is exported?
3. Does the candidate construction prove the hypotheses consumed by that proposition?
4. Does the proposition match the paper and a CMI alternative?

## Positive evidence

The R3 endpoint is not an empty wrapper. `ProblemStatement.lean` defines explicit smoothness, support, divergence, PDE, initial-data, energy, and speed-growth predicates. `WholeSpaceUniqueness.lean` and `WholeSpaceComparisonClosure.lean` contain a real comparison chain for a global finite-energy competitor. The selected endpoint reports only the standard logical foundations `propext`, `Classical.choice`, and `Quot.sound`; the intentional challenge-file `sorry` declarations were not found on that endpoint path.

The construction also contains an actual-field route. `ActualStageEstimates`, `ActualMeanPhysicalData`, and the state-realisation lemmas pass the activated velocity and pressure fields into residual estimates rather than merely naming a stale nominal field. This removes one plausible but currently unsupported criticism.

## Findings requiring revision

### Historical Finding 1: the selected-field transport was previously treated as missing

The following section records the earlier audit hypothesis and its evidence.
It is retained for provenance, but its blanket conclusion is superseded by
the raw-source adjudication above and by
`NavierStokesReview/evidence/profile_moment_selected_path_adjudication_2026-09-29.md`.

The paper makes five moment quantities and their repair a load-bearing part of
the construction. `PositiveOrderMoments.lean` does contain a genuine five-row
definition: `rowDensity` and `moments` at lines 77-85 use the same five
order-n integrands as the paper's equations (5.10)-(5.11). This is positive
evidence and should not be misreported as a formula mismatch.

The unresolved issue is the selected-field composition. The production field
at `ActualCandidateAssembly.lean:515-523` is the sum of the particular,
signed, and stream-mean fields. The exported `Witness` at
`ActualCandidateAssembly.lean:1121-1151` exports sums, extensions, a force,
`CandidateProperties`, and endpoint consequences, but no equality identifying
that mixed field with `PositiveOrderMoments.moments`,
`FiveProfileMoments.physicalMoments`, or the paper tuple `(M,I,J,S,C_p)`.

This is not a request for optional explanatory detail. The paper uses those
identities to remove pressure/stress tails and to preserve the outer fields.
Without the selected-field transport theorem, the source record does not
establish that the object advertised as the Navier-Stokes solution is the
five-moment object proved in the paper.

This consequence is load-bearing rather than terminological. The paper uses
the moments as premises for exterior matching, radial stress-tail removal,
post-modulation restoration, and the five-equation correction cycle. The
formal record therefore does not establish those downstream conclusions for
the exported Cartesian fields. It is important not to overstate the result in
the other direction: the missing theorem does not prove that the selected
field violates the identities. It proves that the paper's downstream use of
them is not transported to the selected endpoint. The correct classification
is consequently **CTR-005: not established as paper-to-code correspondence**,
not a kernel derivation of `False`.

| Paper use | Why it matters | Current formal status |
| --- | --- | --- |
| Exterior matching | Five-integral matching is used to preserve outer pressure and velocity | No selected-field identity established |
| Stress-tail removal | Total moment identities are used to remove radial tails | Not connected to the exported field |
| Modulation repair | All five integrals are restored after modulation | Upstream algebra exists; selected-field transport is unproved |
| Correction cycle | Two rows are preserved and three defects are cancelled | Runtime repair exists; paper-level selected-field identification is unproved |

The direct textual basis is recorded in the [selected moment transport source
trace](../NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md)
and the [full selected transport audit](../NavierStokesReview/evidence/selected_transport_audit_full_2026-09-28.md),
alongside the [load-bearing paper dependency matrix](../NavierStokesReview/evidence/paper_moment_dependency_matrix_2026-09-29.md).

The runtime audit also rules out an overstrong version of the objection. In
`MeanRankUpdate.lean`, `scaleDebt` carries three debt coordinates with explicit
length and velocity powers. In `FiveRowRank.lean`, the first two rows constrain
the correction functions `dv` and `ga`; they do not define total kinetic
energy. The source theorem `five_rows` constructs these corrections for
nonzero debt. The remaining issue is therefore transport into the selected
Cartesian field, not an immediate contradiction from clamped energy rows.

### Finding 2: the three-debt interface is not the selected five-moment certificate

`FiveRowRank.lean:21-22` defines `Debt := Fin 3 → ℝ`; its repair functions
consume three debt coordinates, while the first two rows of `FiveRows` impose
the correction constraints. `FiveRowPositiveOrderBridgeProbe.lean` verifies
only the explicit promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)`. That algebraic
promotion does not prove that the selected mixed velocity and pressure fields
have the paper's five integrals, nor that the promoted rows drive the residual
and force used by `Witness`.

Accordingly, the direct dimensional objection to `PositiveOrderMoments` is
withdrawn, but the central composition objection is strengthened: the source
contains both real five-row formulae and a distinct three-debt runtime repair,
yet the published solution record does not export the theorem that connects
the selected endpoint to the paper's five-moment mechanism.

### Finding 3: regularity is not a substitute for moment tracing

`MovingFieldRowNonImplicationProbe.lean` formalises the relevant logical point: smooth moving fields need not satisfy the required row identities. Any paper passage that moves from smoothness or field reconstruction directly to zero angular debt must be supplemented by the missing integral identities and their use in the residual estimates.

### Finding 4: the force is active through the singular regime

`PositiveTimeForce.lean` uses a smooth cutoff that is still one on the interval containing the singular time. The force is residual-driven and remains active as the speed becomes unbounded. This defeats any stronger description of the result as an unforced or autonomous singularity.

It does not defeat CMI alternatives (C) or (D) by itself, because the official problem statement permits smooth forcing. The paper should state the result as a forced breakdown construction and should not imply a force-free result.

### Finding 5: the generic `JetRate` interface needs a non-vacuity contract

`JetRate` accepts an arbitrary filter without a `NeBot` premise. Over `Filter.bot`, its eventual bound is vacuous. The selected `originPast` route has a separate non-bottom proof, so this is not currently a demonstrated endpoint exploit. It is nevertheless a serious interface defect: future lemmas can silently prove rates on empty regions unless non-vacuity is made explicit or proved at every consumer.

### Finding 6: external regularisation objections must be labelled correctly

Non-Newtonian viscosity and hypo-dissipation are different equations. They are appropriate robustness questions, not internal failures of a formal theorem about the classical Newtonian equation. The paper and review should keep these objections in a separate physical-scope section.


## Technical objections and adjudication

### Moment-system objection

The original action-reaction objection was too strong. `FiveRowRank.FiveRows` is an explicit conjunction of five radial integral identities, including the two zero-moment rows. `five_rows`, `CorrectionState.rank_rows_on_patch`, and `DefectIncrementBounds.RankGeometry.fiveRows` prove or transport those equations for the rank subsystem. `PositiveOrderMoments` separately defines five integral moments and proves exact repair.

The remaining issue is endpoint correspondence. The selected witness does not expose a theorem identifying its actual stage fields with `FiveRows`, `PositiveOrderMoments.moments`, or the paper tuple `(M, I, J, S, C_p)`. This is a material reproducibility gap, not evidence that the first two rows were merely inserted by type definition.

### Profile-tail collision route: exact source boundary

The proposed upgrade from CTR-005 to a kernel contradiction is well-targeted
but requires a missing field-level calculation. `FiveRows` constrains the
correction profiles `dv` and `ga`; its two zero rows do not assert that the
total assembled Cartesian velocity or its kinetic energy has zero moment. A
review-side zero-sorry module proves that a nonzero three-coordinate runtime
debt is compatible with the two zero correction rows.

The selected cycle separately carries a genuine local two-moment invariant,
so the conditional obstruction remains available: a proved nonzero selected
cycle correction moment would imply `False`. The inspected endpoint still
does not provide the required map from the Cartesian `potentialSum`/pressure
fields to the radial profile types accepted by `barMoment` or
`PositiveOrderMoments.moments`. The proposed existential evaluation
`∃ Δm, moments = Δm` would be tautological and cannot establish a nonzero
remainder.

This route therefore strengthens the live research target without justifying
a fabricated contradiction. The paper-level result remains **NOT
ESTABLISHED** because the affirmative five-moment selected-field theorem is
missing; the selected-path `False` search remains open.

Evidence: `NavierStokesReview/evidence/ctr005_profile_tail_collision_route_2026-09-25.md`.

### Force regularity and residual provenance

The force remains active at `t = 1`, but `PositiveTimeForce.timeCutoff` is a smooth bump and `timeCutoff_contDiff` proves global smoothness. The source does not support a discontinuous-cutoff objection. `CandidateFromLimits.force` agrees with the activated residual for `0 ≤ t < 1` and obtains its global smooth extension from locally uniform residual limits and boundary jets. This confirms a posteriori force engineering, but does not prove force divergence. A stronger adverse result would require a zero-`sorry` theorem showing that the selected residual fails those endpoint limits or that the resulting force violates smoothness, support, or decay; that stronger result is not asserted here.

## Adversarial audit questions

1. Does any declaration identify the paper's five quantities with the exact rows used by the selected candidate?
2. Does any exported theorem consume `PositiveOrderMoments.moments_repair` as the implementation of Appendix A?
3. Are the two fixed zero-moment rows proved for the actual activated field, rather than merely imposed in the row type?
4. Does any theorem prevent every `JetRate` consumer from using `Filter.bot` vacuously?
5. Does the paper claim autonomous blow-up, or only a forced CMI alternative? The source supports only the latter description.

## Final assessment

The formal endpoint should not be dismissed as a mere compile illusion.
Conversely, a clean endpoint axiom report does not verify the paper's
construction line by line. The evidence supports a negative publication
decision on the published solution claim: the repository has a formal C/D-shaped
endpoint and substantial construction machinery, while the paper's
endpoint-level five-moment transport remains unproved at the source level.
The review does not yet possess a zero-sorry theorem showing that the
exported endpoint is false; that narrower technical status does not reverse
the burden-of-proof decision.

## Review artefacts

- `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean`
- `NavierStokesReview/src/probes/FiveRowsStructureProbe.lean`
- `NavierStokesReview/src/probes/MovingFieldRowNonImplicationProbe.lean`
- `NavierStokesReview/src/probes/ForceActivityProbe.lean`
- `NavierStokesReview/src/probes/OriginPastNeBotProbe.lean`
- `OpenAI_NavierStokes_Axiom_Ledger.md`

## Correction to the moment finding

The initial wording treated the dimension and exponent mismatch as the strongest adverse result. That wording was too strong. `FiveRowPositiveOrderBridgeProbe.lean` now proves, without `sorry`, that the positive-order repair and the physical-rank repair agree after promoting `(P, Jθ, Jz)` to `(0, 0, -P, -Jθ, -Jz)`. The probe also proves the exact five weighted moments for that promoted repair.

The review therefore withdraws any suggestion that `FiveRowRank` is inconsistent with the five-row repair. The remaining major-revision issue is endpoint transport: the inspected source record does not establish that `CorrectionState.debt`, `ZeroMasses`, and `RankGeometry.fiveRows` carry the paper's named `(M, I, J, S, C_p)` quantities into the actual selected witness and residual estimates. Without that theorem on the inspected record, the public paper-to-code correspondence remains unestablished. This is narrower than a formal refutation.

## Finding 8: import availability does not establish paper-to-endpoint transport

`SelectedImportClosureProbe.lean` imports `NavierStokes.R3.Theorem` and resolves both `PositiveOrderMoments.Debt` and `FiveRowRank.Debt`. The repository therefore contains, and the selected import closure can see, both moment layers.

That positive fact does not close the review. The selected witness is assembled through `ActualCandidateAssembly.selected_witness`, the actual stage estimates, and the germ endpoint. The inspected source still lacks a named theorem that identifies the paper's `(M,I,J,S,Cp)` with the promoted physical debt and proves that the identity is preserved in the fields used by the residual estimates. This is a correspondence obligation. It is not a zero-sorry contradiction.

## Withdrawn objection: initial-face regularity

The earlier claim that `ContDiffOn` only covers `0 < t < 1` was incorrect. `preSingularDomain` is `Ico 0 1 × univ`, including `t = 0`, and the source specifies relative half-domain smoothness. This objection is withdrawn and must not be used as evidence against the endpoint.

## Finding 7: the repository is not globally zero-sorry

A repository-wide source census finds four admitted declarations in `ComparatorChallenges`: two in `ComparatorChallenges/NavierStokes.lean` and two in `ComparatorChallenges/Euler.lean`. This directly contradicts any unqualified statement that every Lean source file in the repository is fully derived.

The finding must not be inflated. The challenge module is marked as a standalone comparator with intentional placeholders, and the inspected dependency reports for the exported R³ theorem and selected witness do not include it. The correct peer-review demand is therefore disclosure and scope separation: identify the challenge files as admitted, and do not use their existence either to dismiss the selected endpoint automatically or to claim repository-wide zero-sorry verification.

## Finding 9: the selected convergence interface is derived

The earlier review required a direct audit of the construction interface before treating the endpoint as an illusion of proof. That audit has now been performed. `StageEstimates` does not contain an unconstrained “infinite residual is flat” field. It contains finite-prefix smoothness and jet-rate bounds. `ActualCycleResidualBounds.finite_residual_rates` derives the finite residual rates from the actual cycle invariant and `PhysicalData`; `StageEstimates.exists_schedule` derives the scale schedule and vanishing joint residual jets; and `CandidateConsequences.mixed_exists_force_with_consequences` constructs the force and derives the candidate consequences.

The same audit found that the spatial localisation is curl-based and accompanied by a divergence-free theorem, while the quantitative moment-repair path derives the coefficient smallness used by `ModulatedCone.profiles_trueCone`. The proposed objections that convergence, incompressibility after localisation, or cone preservation were merely asserted are therefore not supported by the selected source.

This finding does not certify the underlying analysis outside Lean. It does establish the correct review boundary: the remaining correspondence criticism concerns whether the formal symbols are adequately identified with the paper's named moments and physical interpretation, not whether the selected endpoint simply assumes its own conclusion.

## Finding 12: the selected-witness falsification lane remains open

The earlier pressure discussion was too willing to treat a failed
trivialisation probe as a cleared hypothesis. That is corrected here. The R3
`CandidateProperties` record requires compact pressure support and a residual
identity, but it does not expose a global pressure-Poisson/Leray equation. The
force can therefore absorb the pressure gradient at the record level. This is
an unresolved semantic attack: the review must add the global elliptic premise
and test it against the selected pressure and velocity before deciding the
support/topology contradiction.

The force-jet attack remains equally active. `force_smooth` consumes a family
of residual-limit premises `hlim`; it does not derive those premises from the
velocity blow-up. The required proof is a selected-field lower bound showing
that the residual derivatives cannot have the endpoint jets used by the
gluing theorem.

Finally, `SelectedWitnessInhabitationProbe.lean` gives a zero-sorry
type-level countermodel: the inhabited `Witness` envelope can be paired with
an arbitrary nonzero five-debt payload because no such payload occurs in the
type. This proves that the envelope does not certify five-moment transport. It
does not yet prove the actual selected fields violate the moments, so the next
step is to add the missing field-level equality and attack it directly.


## Selected-path transport boundary

`ActualCandidateAssembly.Witness` packages the stage schedule, residual force,
periodic `CandidateProperties`, and endpoint consequences. The R3 theorem then
passes that package through `R3/ActualCandidate.of_localized_fields`. None of
these interfaces consumes an equality between the selected fields and
`PositiveOrderMoments.moments` or `FiveRowRank.FiveRows`. This is a load-bearing
transport omission, not yet a proof that the concrete fields fail those
moments. The active falsification task is to use the actual selected residual,
pressure, and origin data to derive `False`, rather than to treat a generic
type-level countermodel as field-level evidence.

## Finding 10: selected aliases are not admitted proofs

The block at `ActualCandidateAssembly.lean:1163-1181` defines three selected stage sequences and proves `selected_witness` for the selected parameters. The supporting construction sets `selectedBudget := 0` and proves the selected threshold inequality. These facts are unusual enough to audit, but they do not constitute `sorry` placeholders: the aliases have definitions, the geometric condition is a theorem, and the endpoint witness is obtained through the actual witness chain.

The zero-sorry `SelectedBudgetProbe.lean` confirms the literal parameter facts. It also clarifies the key distinction: `B = 0` is not a zero-stage construction because the raw sequences remain indexed by `j : ℕ`. The review should now ask whether the paper requires a positive budget or another quantitative condition that the selected endpoint fails to expose. In the absence of that comparison, this issue is not a formal refutation.

The earlier trivial transport probe has been removed from the evidence set. It constructed arbitrary existential scalars and therefore did not prove that the paper-to-code transport theorem is false.

## Finding 11: the native residual bound is not an inserted invariant field

The selected residual path was traced through `CycleAnalyticInvariant`, `ActualCycleResidualBounds.native_residual`, and `residual_jetRate`. The invariant stores component estimates and a residual decomposition. The native bound is derived by combining the mean, base, alias, Gaussian, and source estimates, after which the jet-rate theorem consumes the derived bound alongside state-realisation and exterior estimates.

This clears the specific allegation that the endpoint declares its final residual estimate as an unproved invariant field. It does not settle whether the formal estimates capture the paper's intended analysis or whether the named five moments are transported into the selected debt system. Those remain correspondence questions.

## Finding 12: the zero-row accusation is false, but the selected moment bridge is not shown

The suggested Newton’s-third-law objection was tested at source level. `FiveRowRank.FiveRows` is not a record that declares the first two rows zero by construction. It is a conjunction of five explicit radial integral equations. `five_rows`, `rank_rows_on_patch`, and `RankGeometry.fiveRows` prove or transport those equations for the rank subsystem. `PositiveOrderMoments` also contains a genuine five-coordinate integral repair theorem.

The remaining criticism is stronger when stated narrowly. `ActualCandidateAssembly.selected_witness` returns `Witness` over three raw stage sequences and the downstream schedule, force, blow-up, decay, and boundary properties. The selected endpoint does not expose a theorem identifying those stage fields with `FiveRowRank.FiveRows`, `PositiveOrderMoments.moments`, or the paper’s five named quantities. The zero-sorry `SelectedMomentBridgeAudit.lean` probe records this type boundary.

This is a material correspondence and reproducibility defect. It is not yet a formal disproof, because an absent public bridge does not establish that no transitive theorem exists. The present adjudication records a correspondence failure; escalation requires a false selected equality or a zero-sorry countermodel, not a request for revision.

## Finding 13: the cutoff is smooth, active, and residual-driven

The proposed cutoff loophole was inspected in the actual R³ implementation. `PositiveTimeForce.timeCutoff` is a rescaled smooth bump with `ContDiff ℝ ∞` regularity. It is equal to one on `[3/8,1]`, so the force remains active through the singular time, but it is not discontinuous at `t = 1`. `ForceActivityProbe.lean` compiles the endpoint value and continuity claims without `sorry`.

The residual concern survives in a narrower form. `CandidateFromLimits.force` agrees with the activated Navier–Stokes residual before one and uses a smooth extension at the endpoint. The extension depends on locally uniform residual limits and boundary jets constructed upstream. This confirms a posteriori force engineering, but it does not prove that the force diverges. Blow-up of the velocity alone is insufficient to infer blow-up of the residual because cancellation is possible and is precisely what the extension obligations address.

The appropriate review demand is therefore a zero-sorry proof that the selected residual fails the required endpoint limits or that the selected force fails global smoothness, compact positive-time support, or decay. Until such a result exists, this is a physical interpretation and proof-obligation concern, not a formal C/D refutation.

## Revised recommendation

The recommendation is **do not accept the published CMI-solution claim on the inspected record**. The repository-wide zero-sorry claim is false because four challenge-file declarations are admitted, and the paper does not yet present a source-linked theorem mapping all named paper moments into the selected endpoint. Those are publication-blocking reproducibility and correspondence defects. They are not, by themselves, a formal disproof of the literal selected C/D theorem. The review need not derive `False` before rejecting the advertised solution claim; a selected-path contradiction remains a separate escalation target.

## Physical realizability verdict: force-conservation proposal

The proposed counter-argument asks whether Newton's third law forces

$$
\int_{\mathbb R^3} f(x,t)\,dx=0
\quad\text{and}\quad
\nabla\cdot f=0.
$$

Those conditions cannot be used as CMI disproof criteria without an additional theorem or admissibility assumption. In the forced alternatives, the external body force is not an internal stress. It may inject net momentum, and incompressibility is imposed on the velocity field rather than on the body force. The repository's `CandidateProperties` likewise requires force smoothness, positive-time support, rapid decay, the Navier–Stokes residual identity, and the stated energy/blow-up consequences, but not either proposed conservation identity.

The endpoint axiom replay was rerun on 2026-09-30 and is recorded in
[`selected_endpoint_compile_boundary_reaudit_2026-09-29.md`](../NavierStokesReview/evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md).
It reports only `propext`, `Classical.choice`, and `Quot.sound` for the
queried endpoint declarations. This confirms the narrow foundational footprint
without converting the missing selected-field moment identity into a kernel
contradiction.

The code inspection also answers the implementation question. `PositiveTimeForce.force` contains no pressure gradient; it is only `timeCutoff z.1 • f z`. The pressure gradient enters through `navierStokesResidual` in `CandidateFromLimits.force`, which agrees with the activated residual before `t = 1` and is smoothly extended at the endpoint. Therefore the proposed momentum/divergence test does not refute the formal C/D proposition. It remains a legitimate physical-provenance concern because the force is selected from the candidate residual.

**Verdict:** the proposed conservation trap is not an ironclad counterexample. The live formal target is to prove, without `sorry`, that the selected residual cannot have the endpoint limits or force predicates required by the code. Evidence: `NavierStokesReview/evidence/force_conservation_obstruction_adjudication_2026-09-23.md`.

## Finding 14: fixed-data perturbation exposes residual path dependence

The independent-data objection has now been tested against the concrete
residual operator rather than left as a physical analogy. The zero-sorry probe
`IndependentDataPerturbationProbe.lean` defines

$$
e_a(t,x)=(t-t_0)a,qquad a\ne0,
$$

and proves that `e_a` is globally smooth and spatially divergence-free. At
the reference time its spatial derivatives and Laplacian vanish, while its
time derivative is `a`. The exact residual defect is therefore `a`, so the
perturbed velocity cannot satisfy the same fixed force as the base velocity.

This formally establishes path dependence: a force selected as the residual
of one trajectory does not remain the residual after an independent velocity
variation. It does not, by itself, prove that the literal existential C/D
statement is false. The chosen test field is not compactly supported or
finite-energy on `ℝ³`, and no source theorem currently states that
`StageEstimates.exists_schedule` must be stable under an admissible variation.
The result is a direct causality objection and a precise target for a stronger
selected-path theorem, not a fabricated `False` certificate.

Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`.

## Finding 29: the five-moment branch is present, but the selected transport theorem is not

The dependency closure was rerun from `ActualCandidateAssembly.lean` rather
than inferred from direct imports. It reaches 507 local modules, including
154 occurrences of `PositiveOrderMoments`, 146 of `FiveProfileMoments`, 104 of
`FiveRowRank`, 42 of `physicalMoments`, and 44 of `CorrectionState.debt`.
`MeanRankUpdate.physical_five_rows`, `CorrectionState.rank_model_rows`, and
`ActualStageEstimates.RunData.rank_class` show that the upstream construction
does use genuine rank and debt data.

That result withdraws any broad allegation that the five-moment subsystem is
dead or globally disconnected. It strengthens the narrower objection. The
selected `Witness` type at `ActualCandidateAssembly.lean:1121-1151` and its
`selected_witness` instantiation at lines 1177-1180 contain no equality
identifying the final mixed sums with `PositiveOrderMoments.moments`,
`FiveProfileMoments.physicalMoments`, `FiveRowRank.FiveRows`, or the paper's
tuple `(M,I,J,S,C_p)`. The missing theorem is therefore a selected-endpoint
transport obligation. It is material to the paper-to-code claim, but it is not
itself a zero-sorry contradiction to the concrete endpoint.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Finding 31: the proposed zero-row collision is not a selected-field contradiction

The claim that a compact perturbation must force `False` through the first two
rows of `FiveRowRank.FiveRows` was tested at the declaration and theorem
levels. `FiveRows` constrains the correction functions `dv` and `ga`; its first
two equations are explicit radial correction integrals. The theorem
`FiveRowRank.five_rows` proves all five rows for every admissible
`d : Fin 3 → ℝ`, including a nonzero debt. The downstream theorem
`DefectIncrementBounds.fiveRows_preserve_masses` preserves two radial moments
of the correction state, not a generic energy integral of the selected
Cartesian velocity.

The selected `Witness` type contains stage sequences, extensions, force
properties, consequences, norm growth, decay, and endpoint jets. It contains
no `Debt`, `FiveRows`, `physicalMoments`, or equality to the paper tuple. A
zero-sorry probe therefore establishes that a nonzero rank debt and the
selected witness can coexist as separate data. The compact fixed-force
perturbation remains an operator-level obstruction, but it is not transported
into the selected correction state by the endpoint theorem.

This rejects the direct collision argument without clearing CTR-005. The
remaining decisive question is whether a selected-path theorem identifies the
paper's five moments with the correction-state rows and carries that identity
into the mixed residual and force. Evidence:
`NavierStokesReview/evidence/five_row_collision_boundary_2026-09-24.md`.

## Finding 32: the zero rows give a conditional perturbation obstruction

The correction subsystem does support a genuine contradiction once the
perturbation has been transported into the correction increment. A new
zero-sorry completion proves that the full `FiveRows` predicate forces
`barMoment 2 h.angular = 0` and `barMoment 1 h.axial = 0`; adding either
corresponding nonzero hypothesis yields `False`.

The production recurrence does carry a related internal invariant: its
`CycleAnalyticInvariant.masses` field is propagated through every selected
cycle stage. `SelectedCycleMomentTransport.lean` exposes that fact and proves
the same conditional impossibility for a nonzero selected-cycle radial
moment. This removes the stronger claim that the cycle has no local mass
preservation theorem.

That result does not yet apply to the selected witness. `FiveRows` constrains
the correction increment, while `Witness` exposes the assembled stages,
pressure, force, endpoint consequences, and norm growth. The selected theorem
does not provide an equality identifying an independently injected Cartesian
perturbation with `h.angular` or `h.axial`. It also does not identify these
radial moments with kinetic energy or `(M, I, J, S, C_p)`.

The correct conclusion is therefore a live conditional attack, not a completed
endpoint refutation: prove the missing selected-path transport and the
nonzero-moment calculation, then the new theorem supplies the contradiction.
Evidence: `NavierStokesReview/evidence/correction_invariant_scope_2026-09-24.md`;
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.

## Finding 22: the force attack now has an exact conditional contradiction

The review has now attacked the selected witness itself. The zero-sorry probe
`SelectedWitnessEndpointResidualProbe.lean` extracts the actual
`CandidateProperties` package and proves that, before the singular time, the
selected force is exactly the selected Navier–Stokes residual. It then proves
the following implication:

$$
\begin{aligned}
\lVert u(t,0)\rVert&\longrightarrow\infty,\\
\lVert f(t,0)\rVert&\leq B,\\
c\lVert u(t,0)\rVert&\leq\lVert\mathcal R(u,p)(t,0)\rVert,\quad c>0
\end{aligned}
\qquad(t\to1^-)
\quad\Longrightarrow\quad\bot.
$$

This is stronger than the earlier residual-naming objection. The probe now
also instantiates the selected schedule and proves that its origin speed tends
to infinity while its actual mixed residual tends to zero. Consequently, the
positive lower bound in the displayed contradiction is impossible for that
selected raw residual. This is evidence of deliberate residual cancellation,
not evidence that the force is singular.

The composition question is now settled on the selected path. The zero-sorry
probe `SelectedForceOriginCompositionProbe.lean` uses the late-time activation
identities, the periodic plateau at the origin, and the selected
`VanishingJointJets` premise to prove

$$
\lVert f(t,0)\rVert\longrightarrow0\qquad(t\to1^-).
$$

The selected force therefore does not diverge at the origin. This closes the
force-explosion route and records genuine residual cancellation. It does not
validate the paper's five-moment or absolute-pressure interpretation, and it
does not itself produce `False`.

Evidence: `NavierStokesReview/evidence/selected_force_origin_composition_2026-09-24.md`.

## Finding 14: the selected endpoint is divergence-free

The proposed direct test of `selectedPotentialStages` targets the wrong object.
Those are intermediate potential fields. The final velocity is produced by the
solenoidal construction, and `CandidateProperties` requires its divergence to
vanish on `0 < t < 1`. The zero-sorry probe
`SelectedDivergenceAudit.lean` imports the selected endpoint and extracts that
property directly as `hc.divergence_free`.

This closes the raw-stage incompressibility objection. It does not validate the
analytic estimates or the paper's moment correspondence, and it does not close
the remaining endpoint residual audit.

## Finding 15: pressure support, energy, and temporal gluing require narrower claims

The source does explicitly give compact spatial support to each pre-singular
pressure slice through `CandidateProperties.pressure_support`, and the selected
endpoint exposes that field. It also contains an exact viscous energy identity
in `R3/ViscousEnergyBalance.lean` and a derivative form in
`R3/CompactEnergy.lean`, with the expected forcing-work and Laplacian
dissipation terms. The zero-sorry `AnalyticObjectionsProbe.lean` confirms that
the selected endpoint exposes pressure support, finite energy, and global force
smoothness.

These facts support a serious modelling objection: the inspected record does not
establish why its compact pressure localisation represents the intended
whole-space pressure, or where the exact energy identity is applied to the
selected fields. They do not yet establish a CMI contradiction. With an arbitrary
external force, the pressure equation includes the force contribution, so the
usual force-free Riesz-transform argument cannot be applied without an
additional hypothesis such as `div f = 0`.

The temporal interface is likewise not visibly a kink: `CandidateFromLimits`
uses `SpacetimeGluing.smoothExtension` and records all endpoint derivatives via
`force_boundary_jets`. The remaining adverse test is whether the selected
dependency path actually supplies the required residual limits and jets, not
whether a stage switch is syntactically present.

## Pressure-support objection: narrowed finding

The selected R3 construction does compactly localise pressure: `SpatialLocalization.cutPressure` multiplies the pressure by a spatial cutoff, and `R3CompactCandidate.localized_pressure_tsupport` transfers that support to the candidate properties. This is a material paper-to-code question because whole-space pressure is ordinarily recovered through a non-local Poisson/Riesz relation.

The objection must be stated narrowly. The repository also contains compact-test pressure identities in `ConservativeDifference`, `PressureRecoveryHelpers`, `PressureRecovery`, and `RieszTestOperators`. Those results are comparison/recovery theorems with explicit hypotheses, and `WholeSpaceUniqueness.classical_uniqueness_on_Icc` constructs those hypotheses for the candidate-versus-competitor comparison. This removes the claim that the selected pressure path is disconnected. It still does not certify the analytic estimates merely because they compile, nor does it show a contradiction: the arbitrary external force can absorb a pressure-gradient residual unless an independent pressure or force constraint is proved.

## Filter-vacuity correction

The generic `JetRate` predicate does not carry a `NeBot` condition, so arbitrary-filter lemmas should not be presented as automatically non-vacuous. The selected endpoint is narrower than that generic interface: `JointResidualLimits.past_filter_neBot` proves the one-sided endpoint filter is non-vacuous, and `FilterNonVacuityAudit.lean` verifies the instantiation without `sorry`. The correct review statement is therefore “generic filter API hazard, selected endpoint not shown vacuous,” not “the main theorem is proved over `Filter.bot`.”

## Finding 16: the five-moment transport obligation remains open

The source does not support the strongest version of the earlier dimensional
objection. `FiveRowRank` uses a three-coordinate debt and fixes two correction
moments to zero, but `PositiveOrderMoments` contains a real five-coordinate
integral repair. The zero-sorry `FiveRowPositiveOrderBridgeProbe` verifies the
explicit promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)` and the resulting exact
five weighted identities.

That positive result does not clear the paper. The selected endpoint still
needs a source-linked theorem identifying the paper's `(M,I,J,S,C_p)` with the
promoted coordinates and carrying that identity into the actual state,
`StateRealization.chartIdentity`, residual estimates, and `selected_witness`.
The public `CandidateConsequences` bundle contains maximality, lifespan,
unboundedness, force nonzero, and force-jet decay, but no moment-realisation
field. This is the strongest current formal correspondence objection.

## Finding 17: pressure support does not by itself trivialise the candidate

The R³ candidate explicitly localises each pressure slice with
`SpatialLocalization.cutPressure`, and `CandidateProperties.pressure_support`
records containment in a compact set. The repository also has
`PressureRecovery`, `ActualPressureFlux`, compact-test Poisson identities, and
Riesz pairings. These modules are comparison infrastructure with explicit
equal-residual, smoothness, incompressibility, and energy premises; the
selected candidate enters them through `candidate_unique_on_Icc`.

The zero-sorry `SemanticTransportPressureProbe` proves that compact support
alone does not imply a scalar pressure slice is zero. The adverse finding is
therefore narrower: the current record does not establish the selected-path
pressure Poisson and recovery bridge, and it does not justify asserting a
trivialisation loop without those premises.

**Peer-review assessment:** the paper-to-code moment correspondence remains
materially under-documented. The selected pressure-recovery comparison is
present, but its analytic estimates remain a legitimate inspection target.
Neither lane has yielded a zero-sorry contradiction of the claimed C/D
predicate.

## Technical Discrepancies

### The missing selected-endpoint moment transport
The repository compiles on the inspected Lean path, and the source contains
three-component spatial evaluations. That is not a certification of the full
mathematical claim. The base profile (`TailGaugePotential`) and residual bounds
(`PhysicalResidualJetBounds`) do not support the stronger pure-axial or fake-2D
allegation; `radialNormalize_anchor` regulates a precise line rather than
annihilating the global field.

However, a critical correspondence question remains at the final assembly boundary (`ActualCandidateAssembly.selected_witness`). The selected proof term is not moment-free: its declaration closure contains `FiveProfileMoments`, `FiveRowRank`, and `PositiveOrderMoments`, and the actual estimates and physical-data construction consume genuine upstream profile, rank, and repair results. The proof also has an explicit base-axis route for the blow-up limit through `GermCandidateAssembly.origin_blowup` and `FinalSlowBase.axis_tendsto`. The latter is a local proof of one conjunct, not evidence that the paper's restoration mechanism can be removed from the selected construction. What the inspected endpoint does not expose is a final theorem identifying the completed mixed Cartesian fields and residual with the paper's five-coordinate moment arrays $(M, I, J, S, C_p)$.

Consequently, while the repository's modules are internally valid and satisfy the mechanical requirements of the type checker, the result type leaves the paper's final physical identification unexported on the inspected endpoint. The five-moment machinery is active upstream and participates in the selected proof term, but no inspected theorem closes the complete selected-field composition through `StateRealization`, residual estimates, localisation, and `selected_witness` to the paper's named quantities. The claimed exact paper-to-code correspondence is therefore not established by the inspected source. This is not a claim that the formal blow-up predicate is absent, that the moment mechanism is dispensable, or that the selected integrals have already been shown false.

### A machine-checked countermodel to the generic stage interface

The objection is stronger than a missing-name search. A zero-sorry Lean probe constructs a nonempty `StageEstimates` object whose potential, direct, and pressure stages are all zero. Its finite background and residual rate obligations also hold, while a separate theorem proves that the corresponding zero velocity is not unbounded at time one. The generic stage interface therefore admits a static field and cannot itself encode either the five named moments or the blow-up conclusion.

This is a formal refutation of the interface-level implication claimed by any reading that identifies `StageEstimates` with the paper's physical repair system. It is not a formal refutation of `selected_witness`, because the selected endpoint adds further premises for the actual base, physical realization, axis preservation, and origin growth. The remaining load-bearing failure is narrower: no theorem inspected so far transports the paper's five moments through all of those additional premises into an equality for the completed exported candidate. The selected proof does use upstream moment and rank results, so the audit does not describe the mechanism as dead, omitted, or bypassed wholesale.

Evidence: `NavierStokesReview/evidence/stage_estimates_moment_blindness_2026-09-24.md`.

## Pressure-chain finding

The compact-pressure objection does not currently refute the selected C/D
predicate. The exact R3 source records compact pressure support, but the force
is an unrestricted smooth external field and may carry the pressure-gradient
part of the residual. `PressureRecovery` derives gradient pairings only under
explicit comparison hypotheses, while `ActualPressureFlux` converts those
pairings into the cutoff flux used by `WholeSpaceUniqueness`. The zero-sorry
pressure probe proves that compact support does not imply a slice is zero.

This route is therefore closed only as the narrow implication that compact
support forces a slice to vanish. That is not an acceptance of the pressure
construction. The selected endpoint still lacks
an inspected theorem connecting its compactly localised pressure and local
`StateRealization`/`chartIdentity` identities to the paper's global pressure
semantics. The adverse finding that remains is narrower and stronger: the
selected endpoint also has no inspected theorem transporting the paper's five
named moments into the selected residual and force construction. Evidence:
`NavierStokesReview/evidence/pressure_recovery_chain_audit_2026-09-24.md`.

### Finding 22: comparison recovery is not absolute pressure verification

The pressure conclusion must not be over-cleared. `PressureRecovery.Hypotheses`
contains smoothness, divergence-free velocity, equal residuals, and finite
energy for a pair `(u,p)` and `(v,q)`. It has no absolute pressure-Poisson
representative or pressure-normalisation field. The zero-sorry
`PressureRecoveryAbsolutePremiseProbe.lean` instantiates it with identical zero
velocities and any common smooth pressure. Consequently, the recovery theorem
can certify a pressure-difference identity while saying nothing by itself about
whether the selected pressure has the global semantics asserted in the paper.

This is a formally demonstrated limitation of the comparison interface, not yet
a contradiction to `selected_witness`. The remaining decisive test is to show
that `PhysicalFields.pressure_germ`, `StateRealization.base_equation`, and the
selected `VanishingJointJets` premise jointly imply the required absolute
global pressure relation, or else to derive a contradiction from those actual
premises. Evidence:
`NavierStokesReview/evidence/physical_transport_bridge_spec_extraction_2026-09-24.md`.

The selected residual trace shows where the live endpoint obligation enters:
`StageEstimates.exists_schedule` derives `VanishingJointJets` from rate
estimates, and `ActualCandidateAssembly.selected_witness` consumes it through
the generic germ theorem. The public interface does not expose the five named
moments as premises of that limit. This is the current CTR-005 transport
objection, not yet a zero-sorry contradiction to the selected theorem.
Evidence: `NavierStokesReview/evidence/selected_residual_endpoint_trace_2026-09-24.md`.

## Axis scope of the residual bridge

The selected residual proof has a second interface limitation, specifically at the boundary interface where the off-axis chart meets the singular origin. The discrepancy is isolated to two distinct coordinate regimes:

1. **The Off-Axis Cartesian Fields:** The core engine that lifts coordinates and evaluates residual properties (`StateRealization.chartIdentity`, Line 927 of `NavierStokes/PhysicalResidualJetBounds.lean`) explicitly excludes the singular axis. The type parameter requires `radius_ne : ∀ x ∈ U, x.1.1 ≠ 0`.
2. **The On-Axis Global Limits:** The construction of the vanishing jet fields along the singular temporal limit requires a joint bound across the central axis (`GlobalBaseError.originPast`, Line 159 of `NavierStokes/GlobalBaseError.lean`), which evaluates spatial coordinates passing through `r = 0`.

The repository does structurally separate these regions. The terminal theorem
(`selected_residual_jetRate`, `ActualCycleResidualBounds.lean:956-989`)
combines an estimate on `S` with a base estimate on `Sᶜ`. The `houtside`
hypothesis is the transport step that makes this legitimate: outside `S`, the
selected velocity and pressure are eventually equal to the base fields. Thus
the source proves a piecewise rate bound; it does not prove a discontinuity or
an automatic failure at the axis.

The genuine limitation is narrower. `chartIdentity` is not an origin theorem,
and the selected public interface does not state that the paper's five
moments or an absolute pressure-Poisson identity are preserved when the
piecewise residual bound is assembled. This leaves a selected-path
correspondence obligation under CTR-005. It does not show that the nonlinear
terms fail to match at `r → 0`, because the source may be intentionally
placing the correction support away from the origin and using the base germ
there. A formal refutation still requires a false equality or an incompatible
origin consequence for the actual selected fields.

Evidence: `NavierStokesReview/evidence/state_realization_axis_scope_audit_2026-09-24.md`.

## Finding 23: the rate interface cannot carry the paper's five debt

The formal review now contains a second zero-sorry result beside the
zero-stage countermodel. `StageEstimatesMomentBlindnessProbe` proves
`interface_does_not_determine_five_debt`: the generic rate record cannot
determine an arbitrary `PositiveOrderMoments.Debt`. This closes a precise
interface question. The paper's five quantities cannot be treated as present
merely because the selected construction imports five-moment modules or
because a three-coordinate debt can be promoted algebraically.

The result does not prove that the selected endpoint has the wrong moments.
It identifies the missing load-bearing theorem: the actual selected velocity,
pressure, and residual have not been shown in the inspected record to realise
the five named integrals and preserve them through the selected schedule. In
the absence of that theorem or a contradiction from its concrete premises,
the correct verdict is
**formal correspondence failure not yet converted into a formal refutation**.

Evidence: `NavierStokesReview/evidence/stage_estimates_moment_blindness_2026-09-24.md`.

## Editorial control

This is the active human-readable review. Its evidence boundary and the status
of older notes are defined in [`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md).
It is intentionally not a chronological audit log: claims are stated with
their present status and linked evidence, while unresolved objections remain
explicitly unresolved.

## Finding 24: the five-moment machinery is live upstream, but its selected-endpoint transport is not shown

The review withdraws the stronger claim that the five-moment branch is dead or
disconnected. `GlobalStressSupport.moments_zero` is used by
`EntranceAlignedBase.aligned_moments_zero`; the modulated construction derives
finite residual identities, and `FinalSlowBase` exports those identities for the
same profile that supplies the base origin blow-up. The zero-sorry
`SelectedBaseMomentCompatibilityProbe` verifies this chain directly.

That correction does not remove CTR-005. The selected endpoint accepts generic
`StageEstimates` and local `PhysicalFields`/germ data. Those interfaces do not
state that the final mixed sums equal the repaired five rows or the paper's
`(M,I,J,S,C_p)`. No theorem carrying that equality into the selected residual,
pressure, force, and `VanishingJointJets` premises was found in the inspected
path. The correct criticism is therefore a missing selected-mixed-sum transport
theorem, not a nonexistent upstream repair subsystem.

**Status:** material correspondence failure; no zero-sorry `False` theorem yet.

Evidence: `NavierStokesReview/evidence/selected_base_moment_chain_reaudit_2026-09-24.md`.

## Finding 25: the force-jet attack now has a precise missing theorem

The new zero-sorry probe `SelectedResidualLowerBoundObstructionProbe.lean`
proves the exact conditional contradiction: if the selected origin residual
satisfies a fixed positive lower bound

$$c\lVert u(t,0)\rVert \leq \lVert\mathcal R(u,p)(t,0)\rVert,$$

then the residual's vanishing endpoint jets and the origin velocity blow-up
derive `False`. The probe also proves the one-sided residual norm limit from
`VanishingJointJets` on the actual non-bottom endpoint filter.

The selected source instead proves the raw residual and final force tend to
zero at the origin. The positive lower bound is therefore not merely
unlocated; it is incompatible with the selected cancellation. This closes the
force-jet route as a formal disproof strategy. The remaining falsification
work must identify a different false selected premise, most directly in the
transport of the paper's five moments or in the absolute pressure semantics.

## Finding 26: the selected-witness falsification boundary is still open

The direct attacks have been tested against the production path. The force
attack now has a stronger selected-path result: the final force tends to zero
at the origin while the selected speed diverges, so the proposed force
explosion is not available. The pressure attack identifies the absence of a
global Poisson/Leray premise, but compact support alone does not imply
triviality.
The moment-blindness probe shows that the exported witness envelope does not
carry the paper's five-debt payload, but it does not prove a wrong moment for
the concrete selected sums.

These are not clearances. They identify the exact unresolved tests required
turning the architectural objections into a zero-sorry `False` theorem.
The current review verdict remains **not established**, with a live formal
falsification programme and no completed selected-witness contradiction.

Evidence: `NavierStokesReview/evidence/selected_witness_boundary_attack_status_2026-09-24.md`.

The companion zero-sorry probe `SelectedWitnessAttackBoundaryProbe.lean`
now fixes the logical scope of this finding. It proves that the exported
`Witness` does not entail zero for every five-coordinate debt and that scalar
blow-up can coexist with a scalar residual tending to zero. Consequently,
the missing velocity-to-residual lower bound is not a technicality: it is the
premise required to turn the force-jet objection into `False`.

Evidence: `NavierStokesReview/evidence/selected_witness_attack_boundary_2026-09-24.md`.

## Finding 27: the flat residual premise is all-order but debt-blind

`JointResidualLimits.VanishingJointJets` is defined by a quantifier over every
natural derivative order. The selected construction derives it from finite
residual-rate estimates through `ActualCycleResidualBounds`,
`ActualStageEstimates`, `StageEstimates.exists_schedule`, and
`MixedDiagonalResidual.exists_physical_schedule_residual_zero`. The result is
not a truncated `H^3` condition.

The late time switch and the periodic spatial localisation are also source
supported. The switch is globally smooth, equals one for `t ≥ 3/4`, and its
positive-order derivatives vanish on the late side. The localisation compares
the complete residual by neighbourhood equality, preserving advection,
diffusion, pressure gradient, and all local derivative orders.

Those identities nevertheless take no `FiveRowRank.Debt`,
`PositiveOrderMoments.Debt`, or paper-moment parameter. They cannot supply the
missing selected transport theorem. This is a precise debt-blind interface
finding, not evidence of a temporal discontinuity or deleted three-dimensional
cross term.

Evidence: `NavierStokesReview/evidence/vanishing_joint_jets_and_localisation_trace_2026-09-24.md`.

## Finding 28: fixed-force perturbations expose residual dependence

The phrase “given, externally applied force” has a stronger causal meaning
than the source's construction: `CandidateFromLimits.force` is built from the
selected residual and then extended through the endpoint. To test the
consequence rather than merely describe it, the review adds a smooth velocity
perturbation (e) while keeping pressure and force fixed.

The zero-sorry theorem in
`NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean` proves
that simultaneous satisfaction of the same fixed-force equation requires

$$
\partial_t e-\Delta e+(u\cdot\nabla)e+(e\cdot\nabla)u+(e\cdot\nabla)e=0.
$$

The companion extension in
`NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean`
instantiates the obstruction for `PositiveTimeForce.force`. Thus a nonzero
perturbation defect cannot be absorbed by the unchanged force. This is a
formal, source-level demonstration that the construction is path-dependent:
the force must be recomputed when the selected velocity path changes.

The result must not be overstated. It does not prove that an arbitrary
perturbation is one of the admissible witnesses in the repository, nor that
`exists_schedule` fails for every perturbation. It therefore establishes a
causality and correspondence defect in the claimed physical interpretation,
not yet an unconditional `False` theorem for the literal existential C/D
statement. Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`.

## Finding 30: the fixed-force obstruction survives spatial localisation

The earlier affine-time test was useful for isolating the operator identity but
was not spatially localised. The new extension
`NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean`
constructs a smooth compactly supported potential, takes its spatial curl, and
uses that curl in a time-affine perturbation. The source proves smoothness,
slice compact support, and exact divergence freedom without `sorry`.

At the switch time, the perturbation itself, its spatial derivative, and its
spatial Laplacian vanish, while its temporal derivative is the curl field. The
potential is chosen so that the curl at the origin is `coordinateVector 0`, a
nonzero vector. The theorem
`compactPerturbation_breaks_any_fixed_force_at_origin` therefore proves that a
base field satisfying `navierStokesResidual u p = f` cannot also satisfy that
same fixed-force equation after this localised perturbation.

This closes the earlier localisation limitation in the operator test. It still
does not prove `False` from the literal existential C/D endpoint: the endpoint
does not state perturbation stability or quantify over this test field. The
load-bearing CMI objection remains the missing theorem connecting the selected
residual construction to the independent-data semantics claimed in the paper.

Evidence: `NavierStokesReview/evidence/compact_fixed_force_perturbation_2026-09-24.md`.

## Finding 33: temporal patching is an open interface question, not a proved jump

The stage-transition audit does not find a piecewise-in-time stage definition.
`GermCandidateAssembly.initializedSeries` selects a base/initial field at index
zero and a raw stage at each successor index. The constructor does not itself
require adjacent fields to match, so a proof of selected-field continuity must
come from the later summed-field regularity theorems. This is a legitimate
interface obligation, but it is not a proof that the selected field has a
temporal discontinuity or an energy-gradient jump.

The distinction is now formal. `initialized_series_admits_concrete_boundary_mismatch`
constructs unequal raw entries at indices zero and one, using a nonzero
coordinate vector for the first stage. Because the index is not a time
coordinate, this establishes only that the raw selector lacks an adjacent-stage
matching contract. It does not establish a temporal PDE jump, nor does it show
that the concrete family satisfies the selected endpoint hypotheses.

The source does contain the relevant positive results: `timeSwitch` is used
through a `ContDiffOn ℝ ∞` theorem, late local equality preserves temporal
derivatives, and spatial localization transfers residual jet limits by local
equality. The zero-sorry probe
`NavierStokesReview/src/probes/TemporalPatchingDiscontinuityProbe.lean`
records those facts and the exact indexed-prefix recurrence.

The review therefore retains `CTR-017` as an unresolved verification task:
close it only by deriving a nonzero derivative mismatch for the selected
spacetime sum, not merely by pointing to the absence of an adjacent-stage
equation. The external-source distinction is recorded in
`docs/OpenAI_NavierStokes_Source_Context_Register.md`: residual construction is
a real causal/provenance criticism, but it is not by itself a literal C/D
contradiction under the existential formulation.

## Finding 31: the compact obstruction reaches the selected witness

`selected_candidate_fixed_force_obstruction` now destructs
`ActualCandidateAssembly.selected_witness` and binds its selected velocity,
pressure, and force. At $(t,x)=(1/2,0)$, the compact divergence-free
perturbation has defect `coordinateVector 0`, so the selected field and its
perturbation cannot satisfy the same fixed-force residual equation. The
extension compiles without `sorry`, `axiom`, or `unsafe` declarations.

This is a selected-path causality result, not a global existential
contradiction. `CandidateProperties` does not state perturbation stability or
an independence predicate for the force. The result strengthens CTR-012 while
leaving CTR-005, the missing selected five-moment transport theorem, as the
load-bearing correspondence objection.

Evidence: `NavierStokesReview/evidence/selected_witness_fixed_force_obstruction_2026-09-24.md`.

## Selected-force provenance closure

The provenance claim is now directly extracted from the selected endpoint.
`SelectedResidualProvenance.selected_candidate_force_is_residual_output`
proves that the selected force equals the selected Navier--Stokes residual at
every interior time. This removes any ambiguity about whether the concern is
merely terminological: the construction really does choose the force from the
candidate motion. The proof still has a precise boundary. The exported C/D
predicate asks for existence of a smooth force and does not state that the
force must be chosen independently, nor that the witness must be stable under
independent perturbations. The causal objection is therefore established as a
paper-to-code provenance failure, while a literal formal refutation still
requires an additional admissibility premise or a false selected identity.

Evidence: `NavierStokesReview/evidence/selected_residual_provenance_2026-09-24.md`.

## Finding 34: the runtime rank layer is real, but endpoint transport remains unshown

The correction-row re-audit rules out an exaggerated version of the zero-row
objection. `MeanRankUpdate.physical_five_rows` proves the full runtime row
system for arbitrary three-coordinate debt, and the actual cycle consumes
that debt through `CorrectionState`. The first two rows constrain the radial
moments of the correction functions and preserve the corresponding internal
mean moments. They are not an energy axiom and do not force the selected
Cartesian velocity to vanish.

The remaining objection is more precise. The public `Witness` exports the
mixed fields, pressure, force, residual consequences, jets, and blow-up, but
no equality identifying the internal correction moments with the paper's
`(M,I,J,S,C_p)` or transporting that equality into the final residual and
force. This is a material paper-to-endpoint correspondence gap. It is not
itself a selected-witness `False` theorem.

Evidence: `NavierStokesReview/evidence/selected_rank_transport_reaudit_2026-09-24.md`.

## Finding 36: periodised Cartesian fields and radial support are not yet identified

The source constructs the selected velocity from a periodised Cartesian
potential and proves unit spatial periodicity. Separately, the radial moment
operator consumes a scalar field whose support is bounded in its radial
coordinate. The review completion
`PeriodicRadialSupportObstruction.lean` proves the conditional implication

$$
g(r+1,Y)=g(r,Y),quad \operatorname{supp}(g)\subseteq [a,b]
\quad\Longrightarrow\quad g=0.
$$

The inspected endpoint does not provide the Cartesian-to-radial identification
or the support premise for the selected scalar. This is therefore a precise
transport obligation, not a claim that the selected velocity vanishes and not
a kernel-level refutation. The live issue remains passage of the selected
`tsum` through curl, torus averaging, the weighted radial integral, and the
five-moment interpretation.

Evidence: `NavierStokesReview/evidence/periodic_radial_support_obstruction_2026-09-26.md`.

## Selected endpoint radial observable: mixed-field split

The endpoint velocity is not the potential branch alone. The source
definition in `MixedPeriodicAssembly.lean` combines the localised potential
velocity with a separately cut and periodised direct potential. The
zero-sorry completion `SelectedMixedProductionRadialComponent.lean` makes
this scope explicit on the radial section:

$$
u_{\mathrm{mixed},1}=u_{\mathrm{potential},1}+
\bigl(\operatorname{periodize}(\operatorname{cutPotential}u_{\mathrm{direct}})\bigr)_1.
$$

This sharpens CTR-005. The potential-only `barMoment` representative is not
definitionally the exported mixed field, while the direct summand has not yet
been identified with a scalar radial observable or evaluated under the
weighted integral. The result therefore establishes a typed transport
boundary, not a nonzero remainder or a `False` contradiction.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_radial_component_2026-09-26.md`.

## Endpoint transport recheck

The final source trace does not support the claim that the five-moment system
is dead. `ActualCandidateAssembly.physicalData` is built from actual cycle
fields, `ActualStageEstimates` consumes `CorrectionState.debt`, and the rank
layer proves its five integral rows for the constructed correction. The
upstream machinery is therefore substantive.

The exported `Witness` still exposes only the schedule, mixed stage fields,
away extensions, force, candidate properties, residual consequences, blow-up,
decay, and endpoint jets. It does not expose an equality to
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or `(M,I,J,S,C_p)`. The correct objection is that the
paper's five-moment interpretation is not transported into the public
endpoint. That is a load-bearing correspondence defect, not a theorem that
the selected fields violate the moments.

Evidence: `NavierStokesReview/evidence/selected_endpoint_direct_source_trace_2026-09-24.md`.

## Finding 35: the whole-space uniqueness route is formally active

The no-global-solution conclusion was checked against its actual dependency
chain. `WholeSpaceUniqueness.classical_uniqueness_on_Icc` derives equality on
each closed interval before time one from the two residual equations,
incompressibility, smoothness, finite-energy bounds, compact support of the
reference velocity, and compact-test pressure recovery. The selected wrapper
`candidate_global_agrees_before_one` supplies the candidate properties, and
`CandidateProperties.no_global_solution_one` uses compact support together
with the speed blow-up.

This removes two weaker objections from the review. The R³ theorem is not
merely a candidate-existence shell, and compact pressure support is not used to
make the pressure or velocity vanish. The pressure argument recovers relative
gradient information for the comparison estimate; it does not expose an
absolute pressure representative. That remains a correspondence question, not
a pressure-trivialisation contradiction.

The audited declarations use only the standard Lean axioms
`propext`, `Classical.choice`, and `Quot.sound`. No selected-path `False`
result follows from this audit.

Evidence: [`whole_space_uniqueness_audit_2026-09-24.md`](../NavierStokesReview/evidence/whole_space_uniqueness_audit_2026-09-24.md).

## Fixed-force stability is a separate formal objection

The review-side theorem `FixedForcePerturbationStability.lean` defines an
explicit stronger requirement: the same force and pressure must continue to
satisfy the residual equation after every smooth, compactly supported,
divergence-free velocity perturbation. The selected candidate fails this
requirement. The compact perturbation at $(t,x)=(1/2,0)$ contributes the
nonzero defect `coordinateVector 0`, while the force is held fixed.

This is a precise formalisation of the causal/provenance concern surrounding
the residual-designed force. It is not, by itself, a refutation of the
literal C/D existential statement, because that endpoint exports one selected
force and one selected candidate and does not quantify over perturbations. The
result therefore belongs under CTR-012, alongside the direct residual
provenance theorem, while CTR-005 remains the unresolved paper-to-endpoint
transport objection.

Evidence: [`fixed_force_stability_extension_2026-09-24.md`](../NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md).

The initial-data loophole in that first probe has now been removed. The review
extension `SameDatumFixedForcePerturbation.lean` uses the factor
`t(t-t₀)`, so the perturbation is zero at the selected initial time as well as
at the interior switch. It remains smooth, compactly supported on each spatial
slice, and divergence-free, but its temporal derivative at the switch is
nonzero at the origin. The theorem
`selected_candidate_fails_fixed_force_same_datum_stability` therefore proves
fixed-force path dependence without changing the zero initial datum. The result
still concerns a strengthened forward-data predicate; it is not a standalone
`False` derivation from the literal existential C/D endpoint.

Evidence: [`same_datum_fixed_force_obstruction_2026-09-24.md`](../NavierStokesReview/evidence/same_datum_fixed_force_obstruction_2026-09-24.md).

## Active-stage non-vacuity is conditional

The stage-control implementation explicitly branches on whether
`ActiveParticularStageControls.ActivePair` is nonempty. That branch cannot be
used as proof that the selected construction is vacuous. The review theorem
`active_pair_of_selected_label` establishes the positive conditional fact:
once a concrete `ActualPrimary.Label B N0` is supplied, its chart-band lower
bound and `CommonWindow.self_mem` produce an active pair.

The review-side construction now resolves that reachability question. From
`slowMask_sum_sq = 1`, `primary_activeLabel_at_band_of_mem` constructs an active
label at every positive band. The explicit point `(√(2a),(0,1))` belongs to the
selected reference annulus, so `selected_primary_label_nonempty` constructs a
label above `prepared.N`, and `selected_active_pair_nonempty` constructs the
corresponding stage pair.

The follow-up probe makes the boundary precise. `potentialSum` is defined as a
natural-indexed `tsum` of stage fields, so an assumed empty `ActivePair` does
not turn the diagonal series into a limit over an empty subtype. The generic
empty branch remains relevant to interface review, but it is not reachable on
the selected construction. The load-bearing unresolved issue is therefore
not inhabitability; it is the missing selected-field theorem transporting the
paper's five moments into the Cartesian velocity and residual identities.

Evidence: [`selected_active_pair_reachability_2026-09-24.md`](../NavierStokesReview/evidence/selected_active_pair_reachability_2026-09-24.md);
[`selected_label_inhabitability_audit_2026-09-24.md`](../NavierStokesReview/evidence/selected_label_inhabitability_audit_2026-09-24.md);
[`SelectedLabelConstructionProbe.lean`](../NavierStokesReview/src/probes/SelectedLabelConstructionProbe.lean).

## CMI wording and formal admissibility

Fefferman's statement uses the language of a given, externally applied force
and requires smooth decay estimates. OpenAI's release presents the same
balance as a smooth applied force whose acceleration, pressure, transport, and
viscosity terms cancel. The residual-defined force remains a serious causal
and provenance objection. The exported C/D predicate, however, contains no
formal force-independence or perturbation-stability condition. The compact
fixed-force theorem is therefore a formal objection to the stronger
forward-data reading, not a standalone proof of `False` for the literal
existential endpoint.

## Finding 36: global germ transport is substantial but not semantically complete

The source audit does not support describing the global assembly as a hollow
wrapper. `CandidateConsequences.mixed_exists_force_with_consequences`
(`CandidateConsequences.lean:185-215`) constructs a force together with
`CandidateProperties`, the maximal-lifespan and H³ consequences, force-jet
decay, and all-order boundary jets. `ActualCandidateAssembly.physicalData`,
`estimates`, and `endpoints` (`1079-1115`) supply actual cycle data to the
finite-stage construction, and `Witness` (`1121-1151`) packages the resulting
selected fields.

The remaining defect is an interface omission, not a missing PDE theorem in
those modules. `Witness` exposes no equality transporting the paper's
$(M,I,J,S,C_p)$ moments into the selected mixed velocity, pressure, residual,
or force. It also exposes no fixed-force same-datum stability condition. The
zero-sorry `GlobalTransportBridgeProbe.lean` proves that the selected candidate
has the full `Consequences` bundle while the independently constructed
same-datum perturbation breaks the fixed-force predicate. The separate
`EndpointContractNonImplication.lean` theorem proves that
`CandidateProperties` alone does not imply that predicate.

This is the precise CTR-016/CTR-012 result. It establishes that the exported
global contract is weaker than the forward-data and five-moment interpretation
used in the paper. It does not, without an additional premise or a false
selected identity, derive `False` from the literal C/D existential.

Evidence: [`global_germ_transport_audit_2026-09-24.md`](../NavierStokesReview/evidence/global_germ_transport_audit_2026-09-24.md),
[`endpoint_contract_nonimplication_2026-09-24.md`](../NavierStokesReview/evidence/endpoint_contract_nonimplication_2026-09-24.md).

## Revision note: global germ transport recheck

The global-transport audit was rechecked against the actual cycle construction,
not only against the final `Witness` type. `state_runInvariant`
(`ActualCyclePreservation.lean:826-848`) inducts the selected cycle while
retaining analytic, coherence, and periodicity data. `state_particularData`,
`state_waveData`, and `state_wave_transport` (`850-912`) supply the inputs used
by `ActualCycleCoherence.mean_input_of_transport` (`ActualCycleCoherence.lean:803-820`).
The stage constructors and chart equalities are also real:
`ActualCandidateConstruction.lean:392-404,464-502` defines the native stages
and prefix identities, while `ActualCandidateAssembly.lean:392-424`
identifies the actual fields with their chart expressions.

This removes the claim that the selected endpoint is merely a disconnected
wrapper. It does not remove the load-bearing correspondence objection. The
transport chain carries cycle, covariance, wave, chart, and residual data into
`physicalData`, `estimates`, and `endpoints`; `Witness`
(`ActualCandidateAssembly.lean:1121-1151`) still exports no equality to
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or the paper's $(M,I,J,S,C_p)$ tuple. The precise
finding is therefore a missing field-level semantic identification, not an
absence of global PDE assembly.

The zero-sorry `GlobalTransportBridgeProbe.lean` result remains unchanged: the
selected candidate has the full `Consequences` bundle while the independently
defined fixed-force same-datum stability predicate fails. That result is a
formal selected-path provenance objection. It does not turn the literal
existential C/D statement into `False`, because that statement does not include
the stronger perturbation-stability or force-independence predicate.

## Finding 37: the burden of proof is asymmetric

The source-to-claim matrix changes the emphasis of the review. The repository
does export a substantial C/D-shaped endpoint. `Witness` includes the selected
stage sums, extensions, force, `CandidateProperties`, force regularity, H3
growth, and endpoint jets; the R3 and periodic comparator modules then derive
the corresponding no-global-solution statements.

That positive result does not discharge the authors' larger published claim.
The paper presents the five quantities `(M,I,J,S,C_p)` as the mechanism that
makes the selected construction a Newtonian fluid solution. The source contains
the relevant five-moment systems, but the exported `Witness` contains no
selected-field equality identifying those moments with the final mixed velocity,
pressure, residual, or force. The constrained three-debt promotion is a useful
local bridge, not the missing global identification.

The correct conclusion is consequently stronger than “a compiler warning was
found” and independent of whether the review has already derived `False`: the
repository has not established that the public paper's central five-moment
construction is the object proved by the exported endpoint. That affirmative
the missing composition theorem is sufficient to withhold acceptance of the
published solution claim. Until the selected-path transport theorem is present
in the inspected source, the public solution claim should not be accepted. A
kernel-level refutation remains a
separate threshold requiring a false selected premise or a zero-sorry
contradiction.

Evidence: `NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.

## Finding 39: the literal R³ target must be separated from the paper mechanism

The review has completed the whole-space target check. The source does not
stop at the periodic `Witness`: `NavierStokes/R3/ActualCandidate.lean` converts
the selected periodic fields to compactly supported whole-space fields and
preserves the residual equation, divergence-free condition, blow-up, and
energy bound. `NavierStokes/R3/Theorem.lean:27-53` exports
`ProblemStatement.breakdownStatement` for every positive viscosity.

This matters for the verdict. The residual-defined-force objection, fixed-force
perturbation, mirror-force construction, and compact-pressure arguments do not
contradict an existential C/D statement. They either change the force or test a
stability property that the literal alternative does not quantify over. The
published paper also openly identifies residual cancellation as the central
construction task.

The live negative finding is narrower but still material: the final selected
export does not expose a theorem identifying the paper's five cumulative
moments
$$
(M,I,J,S,C_p)
$$
with the actual mixed fields used by the residual and force. The upstream
five-moment formulas and cancellation theorems are real; the missing item is
their selected-field composition theorem.

Accordingly, this review rejects any claim that the five-moment paper-to-code
correspondence has been demonstrated on the inspected record. It does not
claim that the literal R³ C/D proposition has already been formally
contradicted. The review therefore rejects the advertised paper-to-Lean claim
on the present record: the selected-field transport is absent from the
inspected endpoint evidence. A selected-field `False` theorem is a stronger
separate result.

Evidence: `NavierStokesReview/evidence/cmi_target_and_claim_level_reconciliation_2026-09-25.md`.

## Finding 38: the selected physical-data record does not export the paper's moment payload

The selected path is materially populated. `ActualCandidateAssembly.physicalData`
constructs `PhysicalData` for the actual finite-stage fields, and
`ActualCycleResidualBounds.Invariant.residual_jetRate` consumes that record to
obtain the residual bounds used downstream. This rules out the imprecise claim
that the final endpoint is only a disconnected wrapper.

The record nevertheless contains smoothness, germs, and exterior agreement,
not an equality to `PositiveOrderMoments.moments`,
`FiveProfileMoments.physicalMoments`, `FiveRowRank.FiveRows`, or the paper's
`(M,I,J,S,C_p)`. The zero-sorry
`SelectedPhysicalDataMomentInterfaceProbe.lean` makes the interface omission
explicit by pairing the actual selected record with an arbitrary nonzero debt.

That result is an interface non-implication, not a claim that the selected
integrals have already been shown false. It is nevertheless sufficient to
withhold the published solution claim: the source record does not establish
the selected-field moment composition. A `False` theorem would strengthen the
review but is not required to establish this failure of affirmative proof.

Evidence: `NavierStokesReview/evidence/selected_physical_data_moment_interface_2026-09-24.md`.

## Source-trace correction to the central finding

The repository does contain the paper-shaped five-moment construction. The
five densities are defined at `PositiveOrderMoments.lean:76-85`, their
positive-order cancellation is proved at `GlobalSlowProfiles.lean:1043-1055`,
and the assembled slow base uses it at `AssembledSlowBase.lean:592-617`.
This removes the weaker allegation that the five-moment formulas are absent or
dead.

It does not remove the central publication objection. The final mixed fields
are assembled at `ActualCandidateAssembly.lean:515-523`, but the exported
`Witness` contract (`1121-1151`) does not state that their velocity, pressure,
residual, or force realise the paper's
$$
(M,I,J,S,C_p)
$$
identities. The missing theorem is therefore a selected-field transport
theorem. Since OpenAI presents the construction as a solution, not as an
unconnected collection of upstream lemmas, this missing link is sufficient to
withhold the affirmative solution claim. It is not yet a direct proof that the
selected integrals are false.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.

## Finding 14: the release is not globally admission-free

The repository's default Lake targets include `ComparatorChallenges`. Its two
Navier–Stokes challenge declarations and two Euler challenge declarations are
implemented with `by sorry`. A review-side Lean module reproduces this through
`#print axioms`: each declaration depends on `sorryAx`. This is a concrete
failure of a repository-wide zero-sorry description and must be disclosed in
any release record.

The result is deliberately scoped. `NavierStokes/ComparatorSolution.lean`
imports the independent comparator definitions and the project bridges rather
than the challenge module, and the inspected selected R³ theorem remains
standard-axiom-only. The admission census therefore strengthens the release
integrity objection without being misrepresented as a proof that the selected
R³ endpoint itself depends on `sorryAx`.

Evidence: `NavierStokesReview/evidence/repository_admission_axiom_log_2026-09-25.md`.

## Finding 40: selected-witness export does not certify the five-moment payload

The review now tests the actual selected endpoint rather than inferring its
scope from a generic stage contract. `ActualCandidateAssembly.Witness` is
inhabited by `selected_witness`, and its definition exports the selected
schedule, assembled fields, force, candidate properties, force regularity,
H3 growth, force-jet decay, and endpoint jets. It does not export a
`PositiveOrderMoments.Debt`, a `FiveRows` proposition, or an equality
identifying the selected mixed fields with
$$
(M,I,J,S,C_p).
$$

The zero-sorry extension
`NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
formalises the boundary: a nonzero five-coordinate payload can coexist with
the actual selected witness, and the witness does not entail that every such
payload is zero. This is an interface non-implication, not a claim that the
selected physical integrals have already been calculated incorrectly. The
upstream five-moment formulae remain active and are not being described as
dead code.

The publication consequence is direct. Because the paper presents the
five-moment mechanism as part of its solution, the inspected source record
does not establish transport of those identities through the mixed sums,
residual, pressure, and force. The advertised solution claim therefore
remains **NOT ESTABLISHED** on the inspected record. A selected-field `False`
theorem would strengthen this finding but is not required to reject an
affirmative claim whose load-bearing correspondence is not exported.

Evidence: `NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md`.

## Finding 41: the live route is an actual selected-field remainder

The review has now narrowed the remaining kernel-level attack to a concrete
calculation. `potentialSum` is a natural-indexed sum of cut stages. The selected
stage fields are then passed through spatial curl and Cartesian chart maps,
while `barMoment` is formed later as a radial/toroidal profile integral. The
two zero rows in `FiveRows` constrain the correction profiles `dv` and `ga`;
they do not, by themselves, constrain the total Cartesian sum.

The required contradiction is therefore explicit: calculate the selected
finite-prefix and tail profile contributions, include derivatives of
localisation masks and axis/tail boundary terms, and prove a nonzero remainder.
Only then can the correction invariant be combined with the selected field to
derive `False`. The symbolic radial-integral helper records candidate
calculations but does not substitute for the missing Lean field identity.

This is a stronger objection than repeating that a bridge is absent. It
identifies the exact expression that must be evaluated and the exact point at
which a symbolic leak would become a kernel contradiction. No nonzero selected
remainder is asserted without that calculation.

## Finding 42: companion Euler interval result

The parent-child Euler interval audit does not support the proposed simple
Zeno or first-order seam-discontinuity argument. The inspected source proves
positive interval geometry and uses explicit value and first-derivative matching
in its joining lemmas. An all-order time-jet theorem remains an open question,
but a higher-order defect must be exhibited before it can support a refutation.
This result is kept separate from the Navier–Stokes selected-field finding.

## Finding 43: selected-field calculation gate

The review has followed the proposed remainder route into the concrete stage
definitions. The selected fields are assembled from actual initial and
positive stages, cylindrical angular data, Cartesian chart fields, spatial
curl, and a locally finite cut-stage `tsum`. This rules out describing the
construction as a generic zero-field placeholder.

It does not yet yield the requested `Delta m ≠ 0`. `barMoment_apply` accepts a
scalar radial-profile field after torus averaging. The inspected source does
not provide the theorem that turns the selected Cartesian `VelocityField`,
including cutoff derivatives, curl terms, and axis/tail boundary terms, into
that scalar profile. The two zero rows in `FiveRows` therefore remain local
correction invariants, not a ready-made equality for the exported field.

This is the correct aggressive target: calculate one selected finite prefix,
transport it through the Cartesian-to-radial map, and prove a nonzero
remainder. Until that equality and value exist in zero-sorry Lean, the record
supports a failure to establish the advertised five-moment solution
mechanism, not a fabricated selected-path `False` theorem. The symbolic
calculator is evidence only after its input expressions are linked to the
selected field.

## Finding 44: selected series is non-vacuous, radial moment remains unproved

The review has now checked the actual selected series rather than stopping at
the type boundary. `selected_witness` supplies a concrete schedule, and
`SolenoidalDiagonal.potentialSum_eventuallyEq_partial` proves that at every
positive preterminal point the selected `tsum` is locally a finite prefix.
`potentialSum_allJets_eventuallyEq_partial` proves the same statement for all
iterated Frechet derivatives. The selected construction therefore cannot be
dismissed as an empty-limit artefact.

That result does not close the paper's five-moment argument. The selected
field is a Cartesian `VelocityField` assembled from cutoff potentials and
spatial curls. `barMoment`, by contrast, is defined on a scalar radial-profile
field after torus averaging. The inspected source contains no theorem that
performs this conversion for the selected field. `NominalProfile` contains an
explicit five-coordinate formula for nominal profiles, but it does not prove
that the formula is the moment vector of the selected mixed `tsum`.

The remaining falsification test is consequently concrete: expand one local
finite prefix, retain all derivatives of the localisation masks, transport
the curl through the positive-radius chart, evaluate the axis and outer-tail
terms, and only then apply `barMoment_apply`. A nonzero resulting remainder
would combine with the correction invariant to yield a zero-sorry `False`
theorem. No such selected `Delta m` has yet been proved, so this finding is a
strengthened, source-level burden-of-proof objection rather than a claimed
formal refutation.

Evidence:
`NavierStokesReview/evidence/selected_field_finite_prefix_transport_2026-09-25.md`.

## Finding 45: a concrete selected direct prefix, with the radial gate still open

The review now proves a selected-field identity at the stage level. The
review-side module `SelectedDirectPrefixField.lean` imports the actual
`selected_witness` construction and establishes that each selected direct
stage is the corresponding angular mean stage. Its finite uncut prefix equals
the mean angular field of the selected cycle state at the terminal index.
This is source-level evidence about the published construction, not a generic
countermodel.

That identity does not yet yield the advertised five moments. The selected
prefix is a Cartesian spacetime velocity field. `barMoment` is a scalar
radial profile operator with torus averaging. The missing calculation must
retain the localisation-mask derivatives, positive-radius curl terms, and
axis and outer-support contributions before applying the radial integral. No
selected `Delta m ≠ 0` has been proved, and no selected-path `False` is
claimed here.

This is nevertheless a sharper counter-paper finding than a bare statement
that a bridge is absent: the selected stage recurrence has been identified,
and the exact next operation required to validate the paper's Appendix A
mechanism is exposed. The published claim of a completed five-moment
Navier--Stokes solution therefore remains **NOT ESTABLISHED** on the inspected
record; this is an adverse adjudication, not a repair request.

Evidence: `NavierStokesReview/evidence/selected_direct_prefix_field_2026-09-25.md`.

## Finding 46: the proposed stage mass leak is not present

The active selected recurrence is definitionally the recurrence covered by
`ActualCyclePreservation.state_invariant`. A zero-sorry review completion now
proves that every selected cycle state carries `ZeroMassesOn`; the two
preserved mean-state radial moments are not lost merely because the stages are
iterated. This removes the unproved claim that the first two correction rows
necessarily accumulate a stage-level remainder.

The calculation is still not complete at the advertised field level. The
selected direct prefix is a Cartesian velocity field, whereas `barMoment` is
defined on scalar radial profiles after torus averaging. The remaining test
must explicitly transport the selected coefficient through the angular frame,
localisation masks, Cartesian curl, axis and outer-support terms, and the
radial integral. No selected `Delta m ≠ 0` or `False` theorem has been proved.
The publication claim therefore remains **NOT ESTABLISHED**, while this
specific stage-leak objection is withdrawn as unsupported.

Evidence: `NavierStokesReview/evidence/selected_cycle_mass_preservation_2026-09-25.md`.

## Finding 47: the selected angular field has a concrete component formula

The review now proves that component one of the selected angular mean field is
the physical-atlas scalar coefficient times the corresponding component of the
totalised angular frame. This supplies a concrete expression for the next
radial calculation and confirms that the selected direct family is not being
treated as an arbitrary abstract vector.

The formula remains a positive-radius expression with the coefficient hidden
behind the physical atlas. It does not by itself establish a moment mismatch.
The remaining calculation must evaluate the coefficient, preserve all cutoff
and curl terms, and compute the axis and outer-support contributions before a
nonzero `Delta m` can be asserted.

Evidence: `NavierStokesReview/evidence/selected_angular_component_formula_2026-09-25.md`.

## Finding 48: selected direct stages are chart-realised off the axis

The review now proves a stronger selected-path fact: under the source's
positive-radius chart hypotheses, each selected direct stage agrees with the
corresponding `chartDirectStages` field. This rules out treating the direct
stage family as a merely generic or vacuous witness.

It does not settle the paper's five-moment claim. The identity is restricted to
the chart domain, while the advertised radial moments require the selected
Cartesian field after localisation, spatial curl, torus averaging, and the
axis/outer-support limits. The repository still provides no theorem identifying
that vector-valued expression with the scalar `barMoment` input. A nonzero
`Delta m` therefore remains unproved, as does any kernel-level `False`.

Evidence: `NavierStokesReview/evidence/selected_direct_chart_transport_2026-09-25.md`.

## Finding 49: the positive-radius scalar recovery gate is now explicit

The review-side completion `SelectedCartesianRadialGate.lean` proves that the
scalar atlas coefficient can be recovered from component one of the selected
angular field wherever the first radial-chart coordinate is nonzero. It also
derives nonvanishing of the Cartesian radius. This is a concrete selected
coordinate identity, not a generic interface objection.

The identity stops before the advertised radial moment. It does not evaluate
the selected cut-stage curl, its cutoff-derivative terms, the torus average,
or the axis and outer-support boundaries. Consequently no selected
`Delta m ≠ 0` and no kernel-level `False` follows yet. The published solution
claim remains **NOT ESTABLISHED** because the affirmative paper still needs
the full field-level transport calculation.

Evidence: `NavierStokesReview/evidence/selected_cartesian_radial_gate_2026-09-25.md`.

## Finding 50: localisation creates an explicit curl commutator

The selected construction cannot be audited by replacing a cut potential with
the curl of its uncut potential. In `SelectedCutoffCurlCommutator.lean`, the
review proves the exact identity

$$
\operatorname{curl}(\chi A)
=\chi\operatorname{curl}(A)
+\operatorname{curlLinear}\big((D\chi).\operatorname{smulRight}(A)\big).
$$

This follows the source order: `cutStage` multiplies each potential by a
smooth scaled cutoff, `potentialSum` sums those cut stages, and `velocitySum`
then applies the spatial curl. The extra term is therefore a load-bearing
part of any Cartesian-to-radial moment calculation. The source does not,
however, establish that its selected torus-averaged radial moment is nonzero.
The review records the exact term as an open calculation, not as `Delta m ≠ 0`
or a kernel contradiction.

Evidence: `NavierStokesReview/evidence/selected_cutoff_curl_commutator_2026-09-25.md`.

A separate CUDA refinement run on an explicitly declared three-dimensional
diagnostic profile records a stable signed defect over 129/193/257/321-point
volumes, while its finite-difference curl and divergence errors decrease but
remain nonzero. This is numerical support for the explicit profile mechanism,
not a calculation of the selected Lean `tsum` field and not evidence of
`Delta m ≠ 0` at the endpoint. Evidence:
`NavierStokesReview/evidence/cutoff_commutator_resolution_audit_2026-09-29.md`.

## Current calculation gate: support is not the cutoff plateau

The selected stages are proved to satisfy a similarity-radius support
condition, namely

$$\operatorname{radius}(w)\leq C\sqrt{\operatorname{physicalQ}(w)}.$$

The production cutoff is known to equal one only on the separate Cartesian
plateau

$$x_0^2+x_1^2<\frac1{32},\qquad |x_2|<\frac18.$$

The inspected source does not provide the selected transport theorem linking
these two conditions. Consequently, the native order-two zero for the uncut
direct profile cannot be transferred to the production field. The live
obligation is either to prove the selected support-to-plateau implication or
to evaluate the weighted scalar profile, including its torus-average and
boundary terms.

This strengthens the concrete CTR-005 correspondence objection. It does not
by itself prove a nonzero remainder or a kernel contradiction.

Evidence: `NavierStokesReview/evidence/selected_support_plateau_gate_2026-09-25.md`.

## Selected Cartesian field and the scalar moment operator

The next source-level check separates a type/interface fact from the stronger
physical conclusion that the review is seeking. The selected production object
is a Cartesian velocity field on `SpaceTime`. The operator used for the named
radial moments, `DefectIncrementBounds.barMoment`, instead consumes a scalar
family on `PressureStream.Lift P` and averages the two auxiliary coordinates.

The review completion
`NavierStokesReview/src/completions/SelectedBarMomentInterface.lean` proves
the exact identity after supplying both missing data:

$$
\operatorname{barMoment}_k(g_j)(n,p)
= \int r^k\,\operatorname{torusAverage}
  \bigl(q\mapsto (u_j(\phi(q)))_1\bigr)(r,p)\,dr,
$$

where `φ : Point P → SpaceTime` and `g_j(q) = (u_j (φ q))₁`.

This does not yet prove that the selected infinite Cartesian sum has this
radial profile, that the axis and outer boundary terms vanish, or that its
moment differs from the correction invariant. It is therefore a concrete
selected-field transport defect under CTR-005, not a claimed `Delta m ≠ 0` or
kernel contradiction. The published solution claim is not established for
the actual endpoint fields because the required transport is absent from the
current record.

Evidence: `NavierStokesReview/evidence/selected_barMoment_interface_2026-09-25.md`.

## Finding 59: a selected positive-stage component reaches the production split

The new zero-sorry completion `SelectedPotentialChartComponent.lean` proves,
on each valid positive-radius chart, that the first component of the actual
selected successor-stage curl equals the sum of the production wave and
stream components.  This is positive selected-field evidence, not a theorem
about an abstract or substitute field.

The result strengthens CTR-005 by locating the next calculation precisely.
The mixed component must still be transported into the scalar
`barMoment_apply` input, including torus averaging, the cutoff-gradient term,
axis and outer-support limits, and the infinite-stage passage.  No nonzero
selected remainder or kernel contradiction follows from this identity alone.

Evidence: `NavierStokesReview/evidence/selected_potential_chart_component_2026-09-25.md`.

## Finding 52: component-level localisation term

The selected completion further expands the first Cartesian component of the
cutoff term as

$$
\bigl((\nabla\chi)\times A\bigr)_0
  =(D_1\chi)A_2-(D_2\chi)A_1.
$$

This is a concrete selected-field calculation. It identifies the exact two
products that any radial/toroidal integration must evaluate. It is not yet a
numerical mismatch: the selected integral and its boundary terms remain open.

## Finding 51: the selected radial profile is recoverable only off the axis

The selected angular field has now been evaluated on the actual radial
section. `SelectedRadialSectionComponent.lean` proves that, for `r > 0`, its
first Cartesian component equals the scalar coefficient used to construct the
field. This provides a concrete selected input for the radial calculation.

The restriction is not cosmetic. The source defines the angular frame by
division by the Cartesian radius and totalises it to zero on the axis. Thus a
global proof must separately evaluate the axis extension and cannot simply
divide by `r` at `r = 0`. The theorem still does not identify the full mixed
velocity with `barMoment`, and it supplies no nonzero remainder or `False`.

Evidence: `NavierStokesReview/evidence/selected_radial_section_component_2026-09-25.md`.

## Finding 52: the selected radial calculation has a proved axis branch

The review-side completion `SelectedRadialAxisBoundary.lean` proves that the
first Cartesian component of every selected direct stage is zero on the axis,
where both radial Cartesian coordinates vanish. This is the exact production
boundary value of the totalised angular frame. It should not be described as a
temporal or spatial discontinuity: no derivative mismatch has been proved.

The result strengthens the counter-paper's calculation. Any claimed transport
from the scalar moment invariant to the full Cartesian field must now join the
positive-radius coefficient identity to this axis branch, while also retaining
the cutoff-gradient curl term, meridional contribution, torus average, and
outer-support boundary. The published solution claim remains **NOT
ESTABLISHED** because that composition is still absent from the inspected record; no `Delta m ≠ 0`
or kernel-level `False` is asserted here.

Evidence: `NavierStokesReview/evidence/selected_radial_axis_boundary_2026-09-25.md`.

## Finding 53: the selected velocity is not one combined curl

The source-level completion `SelectedMixedVelocityDecomposition.lean` fixes
the order of the exported mixed field. It is

$$
\operatorname{curl}\!\left(\sum_j\chi_j A_j\right)
 +\sum_j\chi_j B_j,
$$

not `curl (potential sum + direct sum)`. The periodic assembly also cuts and
periodises these two summands separately. Consequently, the cutoff-gradient
commutator is a mandatory term for the potential branch, but it cannot be
used to infer a defect in the direct branch. A genuine selected `Delta m` must
transport both branches through the cylindrical projection, torus average,
radial integration, and boundary terms. This strengthens the affirmative
burden of the published five-moment claim while leaving the kernel-level
contradiction open.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

## Finding 54: direct scalar angular stages have zero order-2 moment

The new completion `SelectedDirectStageMomentTransport.lean` checks the
selected direct branch itself. Stage zero is a selected cycle mean-angular
field. Each later stage is the difference of two consecutive selected cycle
mean-angular fields. The selected cycle invariant gives zero order-2 radial
moment for both states, and the exported primitive regularity gives the
smoothness/support premises needed by `radialMoment_sub_on`. Lean therefore
proves zero order-2 `barMoment` for every selected native angular stage.

This closes one possible location for a selected nonzero remainder, but it
does not close CTR-005. The theorem concerns the scalar native stage before
the final Cartesian assembly. The exported velocity still contains a
curl-generated potential sum plus a separately added direct sum. The remaining
affirmative calculation must transport the potential branch and the mixed
field through localisation, cylindrical projection, torus averaging, radial
integration, and boundary terms. No selected `Delta m ≠ 0` or `False` has been
proved.

Evidence: `NavierStokesReview/evidence/selected_direct_stage_moment_transport_2026-09-25.md`.

## Finding 55: selected potential-stage chart equality

The review-side completion `SelectedPotentialStageChartTransport.lean` now
checks the potential branch at the field level. On the actual Cartesian chart
domain, the curl of each selected potential stage agrees with the potential
field supplied by the selected stage-realisation structure. This closes a
local source correspondence that had previously been only described through
the surrounding construction.

The result is deliberately narrower than the paper's five-moment conclusion.
The exported velocity is still a curled potential sum plus a separately added
direct angular sum. The new theorem does not identify the potential field with
the scalar radial input of `barMoment`, and it does not prove the required
torus-average, axis, outer-support, or boundary identities. Accordingly, no
selected nonzero `Delta m` or kernel-level `False` follows from it. The
publication claim remains **NOT ESTABLISHED** until the complete selected
Cartesian-to-radial transport is proved.

Evidence: `NavierStokesReview/evidence/selected_potential_stage_chart_transport_2026-09-25.md`.

### Positive-radius component transport

The review source now proves the exact first Cartesian component of the
selected polar-chart velocity. On a valid positive-radius chart it is the
rotation

$$
u_1=\sin(\theta)u_r+\cos(\theta)u_\theta.
$$

This matters because the radial gate cannot treat a Cartesian component as an
unrotated scalar profile. The theorem closes that local coordinate identity
only. It does not provide the global torus average, the axis and outer-support
limits, or the equality between the final mixed field and `barMoment` input.
The load-bearing selected-field objection therefore remains a correspondence
failure, not a proved kernel contradiction.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

## Selected base branch present; scalar moment remains unproved

The base-profile audit does not support the hypothesis that the selected base
potential is an empty or purely formal object. `TailGaugePotential` defines
the selected constructed potential, and its compiled curl equality identifies
that curl with `FinalSlowBase.velocity` for every preterminal time. The same
source construction proves that the norm of this selected velocity diverges on
the spatial axis as (t\to1^{-}). The review completion transports that
identity to the constructed potential.

This positive result narrows, rather than removes, the central objection. The
The unresolved endpoint is the absent identification of the complete mixed Cartesian field, including
the curled potential branch and the separately added direct branch, with the
scalar field consumed by `barMoment_apply`. No such selected global equality,
nonzero radial remainder, or kernel contradiction has yet been proved.

Evidence: `NavierStokesReview/evidence/selected_base_profile_transport_2026-09-25.md`.

## Finding 56: the selected direct component has an explicit chart factor

The review completion `SelectedPhysicalComponentTransport.lean` now proves the
selected direct branch component on its source chart.  It is not the raw
angular profile alone:

$$
u^{\mathrm{direct}}_{j,1}(w)
=\cos(\theta(w))\,Q_n^{-A(h)}
\,a_j\!\left(\operatorname{swapCylinder}\bigl(G_n(\operatorname{polarCoordinates}(w))\bigr)_1\right).
$$

This is a selected-path transport result.  It corrects any argument that
silently substitutes the scalar profile into the Cartesian component, but it
does not yet prove that the full mixed field has a nonzero radial `barMoment`.
The potential/curl branch, torus average, axis and outer-support limits remain
part of the required calculation.  The publication claim remains
**NOT ESTABLISHED** because that selected composition is still absent, while
no kernel-level `False` is asserted from this formula alone.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

## Finding 57: the direct scalar moment is zero, but the mixed endpoint remains unresolved

The new zero-sorry completion `SelectedDirectRadialMomentBridge.lean` closes
the direct branch one step further.  On the positive radial section,

$$
u^{\mathrm{direct}}_{j,1}(\operatorname{radialSection}(p))
=\operatorname{meanField}_j(\operatorname{radialSection}(p)),
$$

and the selected native scalar satisfies

$$
\int_{\mathbb R} r^2\operatorname{torusAverage}(a_j(n))(r,s)\,dr=0.
$$

This result removes the direct scalar branch as a source of a nonzero
order-two remainder under the stated carrier hypotheses.  It does not settle
the claimed endpoint: the curled potential branch has not been identified with
the same scalar operator after localisation, summation, axis treatment, and
outer-support limits.  The paper's advertised five-moment conclusion remains
unestablished for the mixed field, but this direct-branch result is not itself
a refutation.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

## Finding 57: the remaining graph-to-torus representation gate

The direct angular branch now has a genuine selected order-two radial identity,
but that identity does not yet reach the complete exported velocity. The
source defines the selected radial coefficient on one positive-radial graph,
whereas the `barMoment` interface integrates the scalar field over the two
auxiliary torus coordinates before performing the radial integral.

In symbols, the source currently supplies a graph value

$$
a_j(n,R,s)=D_j\bigl(\operatorname{physicalPoint}(h,
\operatorname{radialSection}(R,s))\bigr),
$$

while `barMoment_apply` requires

$$
\int_{\mathbb R}R^2\operatorname{torusAverage}(D_j(n))(R,s)\,dR.
$$

The radial-section lemmas prove the first expression and the direct branch
moment theorem evaluates the second expression for the native scalar branch.
No theorem currently identifies the curled potential branch's graph sample
with the required torus average. The published five-moment claim therefore
still lacks a selected-field transport theorem through the full production
assembly. This is a burden-of-proof failure in the advertised construction,
not a claim that Lean has derived `False`.

Evidence: `NavierStokesReview/evidence/selected_torus_average_representation_gap_2026-09-25.md`.

### Finding 58: selected stream-to-curl transport is present

The selected source does contain a real transport theorem. A zero-sorry
completion specialising `ActualCandidateAssembly.stream_on_chart` proves
that the selected mean stream reaches the Cartesian potential branch through
spatial curl on the production chart. This removes the narrower allegation
that the mean stream is disconnected from the endpoint.

The theorem stops at a vector-valued chart identity. It does not identify the
curl field with the scalar torus-averaged input of `barMoment_apply`, and it
does not calculate the axis or outer-support remainder. The load-bearing
objection therefore remains a missing selected-field representation theorem,
not a proved numerical leak.

Evidence: `NavierStokesReview/evidence/selected_stream_curl_chart_transport_2026-09-25.md`.

### Finding 59: rank data reaches the stream, but not the exported moment

The selected construction does use the rank correction. The source defines
`rankNative` through `VariableGaugeMean.rankPotential`, adds it to the
temporal potential, and maps the resulting scalar to the stream angular field
(`ActualCandidateConstruction.lean:459-470`). The successor theorem at
`:492-494` identifies this with `CycleData.streamFamily`. In addition,
`LocalRankDefect.desired_mass_zero` is consumed in the rank-potential
identities (`LocalRankDefect.lean:590-618`).

That positive result sharpens rather than removes the objection. The selected
stream is exported by `CycleData.stream_moving`
(`ActualMeanPhysicalData.lean:915-917`) as a regularity/support/periodicity
structure. The endpoint moment operator is a different interface:
`barMoment_apply` first takes `PressureStream.torusAverage` and then performs
the radial integral. The selected curl theorem reaches the vector-valued chart
field, but no theorem in the audited path identifies that field with the
scalar torus-average input after localisation, summation, and boundary
passage.

The review therefore records a specific selected-field burden-of-proof
failure: the rank correction is active, yet the published five-moment meaning
has not been transported to the field exported by the endpoint. This is not a
claim that a numerical remainder has already been proved. The required
counterexample remains a selected nonzero `barMoment` value or inequality
contradicting a selected invariant.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

## Finding 51: the selected cutoff creates a mandatory curl commutator

The selected production field applies `SolenoidalDiagonal.cutStage` before
the natural-indexed potential sum. The zero-sorry completion
`selected_cut_stage_curl_expansion` proves, for each selected stage,

$$
\operatorname{curl}(\chi A)=\chi\operatorname{curl}(A)
 +(\nabla\chi)\times A.
$$

This narrows the remaining objection. A chart theorem for the uncut stage is
not by itself a theorem about the field exported by the cut-and-summed
construction. The commutator, its support, its axis behaviour, and its
outer-boundary contribution must be carried into the scalar `barMoment`
interface. The source audit has not yet shown that this contribution is
nonzero, so this is a concrete unclosed transport obligation rather than a
claimed kernel contradiction.

Evidence: `NavierStokesReview/evidence/selected_cutoff_curl_commutator_2026-09-25.md`.
## Selected Cartesian-to-radial transport finding: 2026-09-25

The review does not rely on a claim that the physical chart point and the
moment point type are unrelated. SelectedPhysicalPointTransport.lean proves
that the relevant lift aliases are compatible when the pressure-stream
parameter is Plane.

The load-bearing issue is the missing selected-field identification. The
production endpoint exports Cartesian stage sums after cutoff, curl, and
tsum; barMoment consumes a scalar profile on the pressure-stream lift. The
review completion proves the barMoment integral once an explicit
point-to-spacetime map and scalar-profile equality are supplied. The selected
endpoint does not currently export that post-curl, post-tsum equality or the
associated torus-average and boundary-limit transport.

This is a concrete correspondence objection under CTR-005. It is not a
source-backed nonzero remainder and not a kernel-level False. The published
solution claim therefore remains NOT ESTABLISHED AS A CMI SOLUTION because
the inspected endpoint does not establish the selected-field correspondence.

Evidence: NavierStokesReview/evidence/selected_physical_point_transport_2026-09-25.md.

## Selected production direct branch: cutoff transport remains unproved

The source audit distinguishes the native direct profile from the field used
by the selected production assembly. The native theorem proves a zero
order-two radial `barMoment` for the uncut scalar profile. The production
field instead contains

$$
u_{\mathrm{prod}}(t,x)=u_{\mathrm{periodic}}(t,x)+\chi(x)v(t,x),
$$

on the unit cube, where `χ` is `SpatialLocalization.spatialCutoff`. This is
proved without `sorry` by
`NavierStokesReview/src/completions/SelectedProductionDirectCutoff.lean`.
The identity follows `MixedPeriodicAssembly.lean:36-38`,
`SpatialLocalization.lean:165-166`, and `PeriodicLocalization.lean:272-278`.

Consequently, the native zero cannot be substituted for the production-field
zero. The review must evaluate the cutoff-weighted scalar pullback, its torus
average, and the curl/localisation boundary terms before asserting

$$
\Delta m=\operatorname{barMoment}_2(u_{\mathrm{prod}})\ne 0.
$$

This is a concrete paper-to-code calculation objection under CTR-005 and an
unmet burden for the claimed solution. It is not yet a proved nonzero
remainder or a Lean proof of `False`; the responsible verdict remains
NOT ESTABLISHED AS A CMI SOLUTION.

Evidence: NavierStokesReview/evidence/selected_production_direct_cutoff_2026-09-25.md.

## Finding 53: radial support does not establish the cutoff plateau

The source uses two different predicates. `SublevelShrinkingSupport` bounds a
physical radius by a similarity outer radius. `SpatialLocalization.plateau`
requires both a radial inequality and the independent axial condition
$|x_2|<1/8$. The zero-sorry review completion
`SelectedSupportPredicateScope.lean` supplies an interface witness at radius
zero and axial coordinate one. It satisfies the radial predicate for every
nonnegative outer-radius constant but is outside the plateau.

This is a concrete limitation on the paper-to-code calculation. The native
zero of the uncut `barMoment` cannot be transferred to the cutoff-weighted
production field merely from the selected radial support theorem. The result
does not assert that the selected smooth field contains this witness, so it is
not a proved nonzero remainder or a kernel contradiction. The current record
therefore does not establish the selected scalar pullback, torus average, and
radial integral with the cutoff and curl commutator retained.

Evidence: `NavierStokesReview/evidence/selected_support_predicate_scope_2026-09-25.md`.
## Selected auxiliary graph-image finding: averaging-domain coverage

The source-level calculation identifies a concrete transport obligation. The
`barMoment` operator first applies `PressureStream.torusAverage`, which
integrates both auxiliary coordinates over $[0,1]$, and only then performs the
radial integral. The selected physical chart is represented by
`PhysicalResidualBridge.absoluteLift` and is related to the common graph only
on the positive-radius domain.

The zero-sorry completion
`NavierStokesReview/src/completions/SelectedTorusLiftImageScope.lean` constructs
a linear functional separating the radial and time directions. It proves that
the auxiliary component of every positive-radius graph point has nonnegative
radial coordinate, while $(0,1/2)$ belongs to the averaging square and has
negative radial coordinate. Thus the graph image does not cover the full domain
over which `torusAverage` integrates.

This is stronger than a generic request to “add a bridge”, but it is not yet a
refutation of the selected witness. The repository could still export a global
extension or prove invariance in the missed auxiliary region. The selected
`barMoment` value and any nonzero remainder remain uncomputed. The review
therefore retains the verdict `NOT ESTABLISHED AS A CMI SOLUTION`, without
claiming `False`.

The direct production map is covered by the same result: `physicalPoint` misses
an explicit auxiliary point in the unit averaging square. The raw
`ActualMeanPhysicalData.Scalar` family is defined on the full point domain,
whereas the exported `meanField` samples the atlas through `physicalPoint`.
The remaining selected bridge is therefore an equality or a computed
difference between the raw scalar family consumed by `barMoment` and the
production pullback. The image result alone does not prove a nonzero moment or
`False`.

### Valid-band observation boundary

The source definition of `Atlas.physical` makes the observation boundary
explicit. `SelectedAtlasPhysicalErasure.lean` proves that two native scalar
families agreeing at every valid chart sample produce the same selected
physical value. The exported `meanField` therefore cannot, by this fact alone,
distinguish native values outside its valid chart samples.

That result is not yet a refutation. `barMoment` integrates the native scalar
family over the full lifted torus domain, so a selected theorem must still
show either that every integration point is represented by a valid chart or
that the unobserved contribution vanishes. The review records this as a
concrete CALC-26 transport obligation and retains the verdict `NOT ESTABLISHED
AS A CMI SOLUTION` rather than claiming a nonzero remainder or `False`.

Evidence: `NavierStokesReview/evidence/selected_atlas_physical_erasure_2026-09-25.md`.

## Atlas domain boundary and the remaining selected calculation

The latest source-backed result makes the production boundary explicit. In
`ActualMeanPhysicalData.lean:96`, `Atlas.Valid` requires

$$0<z.2.1.1.$$

and in `ActualMeanPhysicalData.lean:125`, `Atlas.physical` returns zero when
no such valid chart sample exists. The zero-sorry completion
`SelectedAtlasDomainBoundary.lean` therefore proves

$$z.2.1.1\le0\Longrightarrow
\operatorname{Atlas.physical}(A,U,d,f,z)=0.$$

This is a concrete boundary in the selected atlas, not a speculative claim
about the paper's intended geometry. It strengthens CTR-005 because
`barMoment` is evaluated over the native scalar-family domain, whereas the
exported field is a zero-extended valid-chart sample. The review still cannot
infer a nonzero omitted contribution: the selected native scalar has not been
shown nonzero on that region, and no torus-average difference has yet been
computed. The result therefore records a selected transport obligation, not
`Delta m ≠ 0` or Lean `False`.

Evidence: `NavierStokesReview/evidence/selected_atlas_domain_boundary_2026-09-25.md`.

## Selected direct production component: the native zero is weighted

The direct branch is not exported as the native scalar profile to which the
upstream moment theorem applies. `ActualCandidateAssembly.directStages` is the
angular mean stage, but the production assembly first applies
`SpatialLocalization.cutPotential`. The zero-sorry completion
`SelectedProductionDirectScalarGate.lean` gives the exact positive-radius
identity

$$
\bigl(\operatorname{cutPotential}(D_j)(r,z)\bigr)_1
=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z)\,m_j(r,z).
$$

The native theorem proves an order-two radial moment for $m_j$ before this
localisation. It does not prove the same statement for the weighted production
component. The required calculation must therefore retain the factor
$\chi(r,z)$, the torus average, the potential/curl contribution, and the
boundary terms. This is a concrete selected-field burden under CTR-005. It
does not yet prove that the weighted remainder is nonzero, so it is not a
kernel-level refutation.

Evidence: `NavierStokesReview/evidence/selected_production_direct_scalar_gate_2026-09-25.md`.

## Selected direct component: atlas pullback made explicit

The selected direct component can now be followed through the atlas selector,
not merely identified with a named native stage. The zero-sorry completion
`SelectedProductionDirectAtlasPullback.lean` uses
`ActualCandidateAssembly.directStages_eq` and the definitions of
`meanAngularField` and `meanField` to prove

$$
D^{\mathrm{dir}}_{j,1}(w)=
A^{\mathrm{phys}}(\operatorname{physicalPoint}(w))
\left(\operatorname{angularVector}(\operatorname{radialProjection}(w))\right)_1.
$$

The production direct branch then multiplies this expression by
`SpatialLocalization.spatialCutoff`. On the radial section the factor is

$$
\chi(r,z)=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z).
$$

This is a concrete selected-field identity and strengthens the burden under
CTR-005. The upstream native moment zero still cannot be transferred to the
exported production field until this atlas pullback is transported through
`torusAverage` and `barMoment`. No nonzero remainder or kernel contradiction
has been established by this result.

Evidence: `NavierStokesReview/evidence/selected_production_atlas_pullback_2026-09-25.md`.
## Selected potential branch: finite partial-curl transport

The selected potential branch has now been checked at the field level. The
zero-sorry completion
`NavierStokesReview/src/completions/SelectedPotentialPrefixCurlExpansion.lean`
proves that, at every preterminal point, the selected Cartesian potential
velocity is eventually equal to the spatial curl of a finite partial
potential:

\[
u_{\mathrm{pot}}
  =_{\mathcal N x}
\nabla\times\operatorname{partialPotential}_N.
\]

This result closes one concrete composition step in the production path. It
does not yet establish the stronger equality between the finite curl and a
finite sum of stage curls on the same neighbourhood. Nor does it transport
the potential branch through the cylindrical chart, `torusAverage`, and
`barMoment`. The selected weighted direct branch and the potential/curl
commutator therefore remain part of the live calculation.

The review conclusion is unchanged: the published solution claim remains
**not established** pending an affirmative selected-field calculation. This
completion is evidence of progress in that calculation, not a proof of a
nonzero moment remainder and not a kernel-level contradiction.

Evidence: `NavierStokesReview/evidence/selected_potential_partial_curl_2026-09-25.md`.

## Selected potential stagewise curl

The selected potential branch now has a stronger, domain-specific identity.
On the open `physicalDomain`, the selected potential velocity is eventually
equal to a finite sum of the curls of the individual cutoff stages. The proof
is in
`NavierStokesReview/src/completions/SelectedPotentialStagewiseCurlOnPhysicalDomain.lean`
and the build record is in
`NavierStokesReview/evidence/selected_potential_stagewise_curl_2026-09-25.md`.

## Finding 58: the direct atlas scalar is now explicit

The direct production branch is no longer ambiguous at the scalar-definition
boundary. `SelectedDirectAtlasScalarRepresentative.lean` identifies the
`Atlas.physical` family on the lifted point type consumed by `barMoment`, proves
its pullback from `meanField`, and records the exact radial-integral expansion.
On the positive-radius radial section, the selected direct stage's first
component is equal to this scalar at the corresponding physical point.

That result strengthens the review because the remaining question is now
concrete: evaluate the mixed selected field, including the cutoff-weighted
direct branch, the potential/curl commutator, and the final `tsum`. It is not
yet a nonzero moment calculation. The review therefore records no `Δm ≠ 0`
and no kernel contradiction.

Evidence: `NavierStokesReview/evidence/selected_direct_atlas_scalar_representative_2026-09-25.md`.

This exposes the exact product-rule terms, including `(∇χ) × A`, that must be
carried into the radial calculation. It does not establish their integral,
does not establish `Δm ≠ 0`, and does not prove `False`. The review therefore
has a concrete selected-field calculation in progress, while the published
Navier--Stokes solution claim remains **not established**.
## Selected native direct prefix: an exact zero before localisation

The selected direct branch now has a finite-prefix calculation rather than
only an upstream invariant. In
`SelectedDirectNativePrefixMoment.lean`, the sum of the selected native
angular stages telescopes to the selected cycle state. The same completion
then transports the cycle invariant to
`DefectIncrementBounds.barMoment 2` and proves that this native prefix moment
is exactly zero on the selected carrier.

This result narrows the live objection. The exported field is not that native
scalar alone: production multiplies the direct branch by a spatial cutoff and
combines it with the curl of the cutoff potential stages. Therefore the native
identity cannot be transferred to the exported mixed velocity without proving
the cutoff, chart, torus-average, and `tsum` transport. The review records no
nonzero remainder or kernel contradiction at this stage.

Evidence: `NavierStokesReview/evidence/selected_direct_native_prefix_moment_2026-09-25.md`.

## Finding 59: production localisation creates an explicit shell term

The selected direct branch has now been traced through its actual production
cutoff. `SelectedProductionDirectPrefixCutoff.lean` proves, for every finite
prefix, that production multiplies the native direct component by
`SpatialLocalization.spatialCutoff`. On the positive-radius radial section,
the uncut prefix is the selected cycle mean field, so the production field is
the same field with the cutoff factor attached.

The completion also proves the exact finite-prefix identity

$$
\sum_{j\leq J}(\chi u_j)_1-\sum_{j\leq J}(u_j)_1
=(\chi-1)\sum_{j\leq J}(u_j)_1.
$$

This is the concrete calculation that the review required. It identifies the
precise term that must be integrated after the Cartesian-to-radial and torus
transports. It does not, by itself, establish that the term is nonzero. The
current source only proves positivity and ordering of the moving annulus
radii; it does not provide the selected cutoff placement and selected
nonvanishing value needed for a numerical contradiction. The review therefore
records a load-bearing selected-field remainder, not an unsupported `False`
claim.

Evidence: `NavierStokesReview/evidence/selected_production_direct_prefix_cutoff_2026-09-25.md`.

### Finding 60: the exported potential branch contains a cutoff/curl commutator

The selected-field completion
`NavierStokesReview/src/completions/SelectedPotentialProductionProductRule.lean`
proves that the production potential branch is not the native curl alone. On
the unit cube, the repository's definitions give

$$
V_{\mathrm{prod}}(t,x)=\chi(x)\,\operatorname{curl}A(t,x)
 +\operatorname{curlLinear}\!\left(D\chi(x)\,A(t,x)\right).
$$

The second term is the spatial cutoff/curl commutator. It is a concrete
correspondence issue because the paper's radial moment discussion cannot be
applied to the exported field until this term has been carried through the
Cartesian-to-radial and torus-average maps.

The result is deliberately narrower than a disproof. The source currently
does not establish that the selected commutator has a nonzero weighted radial
integral. This finding records the exact missing selected calculation rather
than asserting `False`.

Evidence: `NavierStokesReview/evidence/selected_potential_production_product_rule_2026-09-25.md`.

### Finding 61: the selected radial scalar is now explicit, but the moment bridge is not closed

The review completion
`NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean`
extends the selected production calculation to the positive-radial section.
For the actual selected schedule, with the source physical-domain and unit-cube
hypotheses made explicit, it proves

$$
V_{\mathrm{prod},1}=\chi(\operatorname{curl}A)_1
 +\bigl(\operatorname{curlLinear}(D\chi\,A)\bigr)_1.
$$

The differentiability used in the product rule is derived from the selected
schedule and the source `potentialSum_contDiffOn` theorem. This is stronger
than a generic interface observation: it is a selected-path component identity.

It still does not establish that this component is the scalar family consumed
by `barMoment` on the full `PressureStream.Lift` averaging domain. The graph
image, axis and support limits, torus average, final `tsum`, and weighted value
remain to be proved. Accordingly, the result strengthens CTR-005 as a concrete
calculation obligation, but does not prove `Δm ≠ 0` or `False`.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

## Finding 63: the potential component now has the exact moment-interface type

The review-side completion
`NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean`
removes one narrow ambiguity. It defines a section from the physical lifted
point coordinates to the positive-radial cylindrical coordinates, lifts the
selected potential-production component to the exact scalar-field type
accepted by `DefectIncrementBounds.barMoment`, and proves the source
integral expansion

$$
\operatorname{barMoment}_k(F_a)(n,p)=
\int r^k\,\operatorname{torusAverage}(F_{a,n})(r,p)\,dr.
$$

On `ActualMeanStageData.radialSection p`, with `0 < p.2.1`, the section is
identified with the source physical-point construction and pulls back to the
previously proved positive-radius production scalar. The result is selected
field evidence, not a generic type complaint.

It does not yet identify the full mixed Cartesian endpoint with this scalar.
The cutoff/curl commutator, auxiliary torus average, axis and outer-support
limits, and final natural-number sum still require exact transport. No
nonzero weighted remainder or kernel contradiction follows from this local
bridge alone. The publication finding remains **NOT ESTABLISHED** under
CTR-005 because the affirmative paper claim still lacks the complete selected
composition theorem.

Evidence: `NavierStokesReview/evidence/selected_potential_production_barmoment_section_2026-09-26.md`.

### Finding 62: the source supplies a local lift, but not the selected moment transport

The source audit found a genuine positive-radius compatibility. The type
`PhysicalResidualTZ.Lift` is definitionally the same product as
`PressureStream.Lift PhysicalGraphBounds.Plane`, and
`ActualMeanPotentialRealization.physicalPoint_forward` identifies the two
physical-point constructions away from the axis. The selected stage curls are
also transported to the chart by `ActualCandidateAssembly.stageRealizations`.

That evidence rules out an overly broad claim that the coordinate types are
simply unrelated. It does not close CTR-005. The endpoint still lacks a single
theorem transporting the final localised `tsum` through the cutoff/curl
commutator, torus averaging, axis and outer-support limits, and finally
`DefectIncrementBounds.barMoment`. Until that composition is proved and its
weighted value is evaluated, the five-moment paper claim is not established;
this finding is not a kernel contradiction.

Source anchors: `NavierStokes/PhysicalResidualTZ.lean:19-21,385-452`,
`NavierStokes/ActualMeanPotentialRealization.lean:20-27,331-358`, and
`NavierStokes/ActualCandidateAssembly.lean:1059-1088`.

## Finite-prefix torus-average result

The review construction now contains a zero-sorry finite-prefix calculation,
not merely a type-level objection. The lifted scalar supplied to
`DefectIncrementBounds.barMoment` is built through `pointToCyl`; that map
does not use its auxiliary `Plane` argument. Direct unfolding therefore gives

$$
\operatorname{torusAverage}(F_{a,N,n})(r,p)
=F_{a,N,n}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr),
$$

and hence

$$
\operatorname{barMoment}_k(F_{a,N})(n,p)
=\int r^k V_{a,N}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr)\,dr.
$$

This fixes the exact finite-prefix integration target. It is not yet an
evaluation of that integral and does not identify the review scalar with the
complete mixed Cartesian `tsum` in `selected_witness`. Axis and outer-boundary
terms, infinite-prefix interchange, and the selected five-row equality remain
open. Accordingly, the finding strengthens CTR-005 and the publication claim
remains **NOT ESTABLISHED**; no `Delta m != 0` or kernel `False` is claimed.

Evidence: `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md`.

## Axis similarity scale: a confirmed premise, not a contradiction

The source does not leave the similarity scale at the symmetry axis
undefined. `NavierStokes/AxisPreservation.lean:130-148` proves

$$
\operatorname{physicalQ}(h,(t,0))=1-t
$$

for the preterminal interval and proves that this scale tends to zero as
\(t\to1^-\). The proof uses the defining positive solution equation for
`coordinateQ` at axial coordinate zero and a standard continuity argument.

This matters because the cutoff schedule can approach the axis endpoint through
a known scale. It is not, by itself, a failure of the candidate: the review
still must evaluate the selected Cartesian `tsum`, its curl/cutoff terms, and
the resulting `barMoment` integral before asserting a nonzero remainder or a
kernel contradiction.

## Finite-prefix endpoint result

The review now has a zero-sorry endpoint theorem for every fixed finite stage
prefix. It combines the source identity q_h(t,0) = 1 - t with the source
finite-family cutoff theorem. Hence, as t tends to 1 from below, all cutoffs
with indices j < N are eventually equal to one for any fixed N.

This is evidence about the selected construction, not a proof of a temporal
discontinuity or a nonzero radial remainder. The neighbourhood may depend on
N, so the theorem does not commute the endpoint limit with the infinite
tsum. The remaining test is the exact prefix-to-tsum transport followed by
evaluation of the selected torusAverage and barMoment integral.

Evidence:
NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md.

The source-scope record makes the remaining endpoint issue explicit: the
finite-tail and all-jet `potentialSum` theorems require positive scale, while
the selected axis limit tends to zero. This is a missing infinite transport
calculation, not a proof that the selected sum fails.

Evidence:
NavierStokesReview/evidence/selected_tsum_endpoint_scope_2026-09-26.md.

## Selected mixed finite-prefix scope

The selected endpoint has now been traced through both summation branches. A
zero-sorry completion proves separate local finite representatives for the
curl-generated potential branch and the direct potential branch on the source
physical domain. The prefix indices are independent.

This closes the finite local field representation, but it does not provide a
common prefix, an endpoint interchange, or a field-level equality with the
radial `barMoment` input. The remaining objection is therefore a precise
selected-field transport obligation under CTR-005, not a claimed `False`.

Evidence:
`NavierStokesReview/evidence/selected_mixed_velocity_finite_prefix_2026-09-26.md`.

## Local finite-prefix control does not close the selected-field calculation

The review-side completion
`SelectedPotentialProductionTsumScope.lean` now proves a narrower positive
fact. At every point where the production scale is positive and the coefficient
sequence tends to infinity, the source `potentialSum` is eventually equal, for
every derivative order, to one finite prefix in a neighbourhood of that point.
In symbols,

$$
\exists N\;\forall k,\qquad
D^k\!\left(\sum_{j=0}^{\infty} A_j\right)
=D^k\!\left(\sum_{j<N} A_j\right)
\quad\text{locally}.
$$

This removes any suggestion that the local `tsum` is merely an unexpanded
formal symbol. It still does not provide the missing global composition theorem
identifying the selected Cartesian field with the scalar family integrated by
`barMoment`. In particular, it does not evaluate the torus average, the axis
and tail terms, or the weighted radial integral. The selected-field five-moment
claim therefore remains **NOT ESTABLISHED**, while no nonzero remainder or
kernel-level contradiction has been proved.

Evidence:
`NavierStokesReview/evidence/selected_potential_production_tsum_scope_2026-09-26.md`.

## Mixed endpoint observable

The review completion `SelectedMixedProductionBarMoment.lean` now applies the
source `barMoment` operator to a scalar pullback of the actual mixed endpoint
component. For positive radius, the pullback agrees with the component on the
physical radial section. This is a genuine selected-field transport result,
but it is not yet a moment evaluation: the periodised cut direct branch,
axis/tail terms, and infinite-sum interchange remain open. Accordingly, the
record supports a load-bearing correspondence objection but does not establish
`Δm ≠ 0` or a Lean `False` theorem.

Evidence:
`NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

## Conditional mixed-moment additivity

`SelectedMixedProductionBarMomentLinearity.lean` proves the exact potential
plus direct branch split and applies the source `barMoment_add` theorem under
common `Shell` hypotheses. Thus the algebraic identity

$$
\operatorname{barMoment}_k(\widetilde u)
= \operatorname{barMoment}_k(\widetilde u_{\mathrm{potential}})
+ \operatorname{barMoment}_k(\widetilde u_{\mathrm{direct}})
$$

is available conditionally. The selected witness does not export those
common hypotheses for its complete infinite-sum branches. This does not give
the selected weighted value, a nonzero commutator, a five-moment identity, or
`False`; it makes the remaining CTR-005 obligation more specific.

Evidence:
`NavierStokesReview/evidence/selected_mixed_barmoment_linearity_2026-09-26.md`.

## Source-path and packaging correction

The source review confirms the energy portions of the construction. There is
no current `SelectedCandidate.lean` module. The selected path is
`ActualCandidateAssembly.selected_witness` (`ActualCandidateAssembly.lean:1177`)
followed by the R3 wrapper (`R3/ActualCandidate.lean:127-151`) and the public
theorems (`R3/Theorem.lean:26-80`). The `hc` value extracted from
`selected_witness` is a `CandidateProperties` structure. Its fields include
the residual identity and `UniformFiniteEnergy`; the latter is constructed via
`CompactEnergy.uniform_finite_energy` at `R3/ActualCandidate.lean:119`.

The precise remaining objection is therefore not that these fields are absent.
It is that the exported `hc` record contains no theorem identifying the
paper's five moments with the final Cartesian fields or with `barMoment`.
Moreover, the whole-space wrapper transforms the periodic local model by local
compactification and applies the smooth positive-time force layer. Any claim
that the periodic radial moment is preserved by this transformation still
requires a field-level transport theorem. This supports CTR-005 and CTR-012,
but does not by itself prove `False`.

The R3 packaging boundary has now been checked directly in zero-sorry Lean.
`SelectedR3PackagingBoundary.lean` shows that a nonzero five-coordinate
payload can coexist with the exported R3 `CandidateProperties` witness. This
confirms that the record does not carry the advertised five-moment transport;
it does not claim that the selected Cartesian field itself has a nonzero
moment. The remaining escalation still requires the selected integral or a
different source-backed contradiction.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.

## Source-map correction and global-integral semantics

The current source does not contain `SelectedCandidate.lean` or
`R3/SelectedCandidate.lean`. The selected witness and candidate are instead
defined in `NavierStokes/ActualCandidateAssembly.lean:1177-1184`; the R3
wrappers are in `NavierStokes/R3/ActualCandidate.lean:127-151`, and the
exported theorem family is in `NavierStokes/R3/Theorem.lean:26-80`. The
corresponding energy declarations are present at
`NavierStokes/R3/CompactEnergy.lean:343` and
`NavierStokes/R3/Theorem.lean:66`. The review therefore treats the mistaken
filename as a documentation defect only, not as evidence that the endpoint or
energy estimate is absent.

The new zero-sorry completion `PeriodicGlobalIntegral.lean` proves a narrower
analytic fact: strict positivity of a unit-periodic radial scalar on one
fundamental interval makes it non-integrable on the real line, and the global
Bochner integral then reduces to zero through `integral_undef`. The selected
mixed pullback has not been shown to satisfy the positivity premise, and the
weighted moments remain unevaluated. This sharpens the integrability question
without changing the controlled verdict or supplying `Delta m != 0`/`False`.

Evidence:
`NavierStokesReview/evidence/source_path_reconciliation_2026-09-26.md`;
`NavierStokesReview/evidence/periodic_global_integral_semantics_2026-09-26.md`.

The follow-up completion proves the auxiliary torus average is independent of
its auxiliary coordinate and reduces the actual mixed observable to the
literal weighted radial integral. The remaining question is now value-level,
not merely a type mismatch: the direct cut-and-periodised term, endpoint
interchange, and five-moment identification are still unproved.

Evidence:
`NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The selected mixed radial pullback is unit-periodic because the endpoint is
periodised in Cartesian space. The repository's generic theorem proves that a
bounded radial support premise would force this pullback to vanish. Since the
selected witness exports neither that support premise nor a nonzero point, the
result is a concrete compatibility objection, not an unconditional refutation.

Evidence:
`NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

## Mixed endpoint observable

The review completion `SelectedMixedProductionBarMoment.lean` now applies the
source `barMoment` operator to a scalar pullback of the actual mixed endpoint
component. For positive radius, the pullback agrees with the component on the
physical radial section. This is a genuine selected-field transport result,
but it is not yet a moment evaluation: the periodised cut direct branch,
axis/tail terms, and infinite-sum interchange remain open. Accordingly, the
record supports a load-bearing correspondence objection but does not establish
`Δm ≠ 0` or a Lean `False` theorem.

Evidence:
`NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.
## Source-map correction and current proof boundary

The current checkout confirms the root-level R3 files and the detailed `NavierStokes/R3/` modules. The selected route is `ActualCandidateConstruction` → `ActualCandidateAssembly.selected_witness` → `R3/ActualCandidate` → `R3/Theorem`. The R3 endpoint therefore cannot be criticised on the basis that the cited R3, energy, or pressure modules are missing.

The endpoint contract is explicit and nontrivial. `CandidateProperties` includes smoothness, periodicity, initial rest, force support, divergence-freeness, residual equality, and speed unboundedness; the R3 packaging invokes the finite-energy theorem. The remaining objection is the affirmative one: the exported selected field has not yet been connected by a proved field-level transport theorem to the paper’s five named moments.

The pressure chain is similarly present but scoped. `R3/PressureRecovery.lean:388-438` and `R3/ActualPressureFlux.lean:36-58` prove comparison identities under explicit hypotheses and compact spatial tests. They do not by themselves prove the absolute selected-pressure representative or the five-moment identity. The review therefore records a correspondence burden, not a pressure-trivialisation contradiction.

Evidence: `NavierStokesReview/evidence/source_tree_logic_map_2026-09-26.md`.

## Periodisation boundary in the moment calculation

The compact-support argument must stop at the pre-periodised field. Source
lemmas establish support for `SpatialLocalization.cutPotential`, whereas the
selected mixed velocity is assembled by `MixedPeriodicAssembly.periodicVelocity`
and is unit-periodic. The audited `barMoment` then integrates over all real
radial values. Thus the implication from compact support to vanishing of the
selected radial moment requires an additional transport theorem. The review
has not found that theorem and does not infer a nonzero remainder or `False`.

Evidence: `NavierStokesReview/evidence/periodic_global_integral_semantics_2026-09-26.md`.
## Audit-method control: compiled reachability versus source navigation

The review’s repository map now has an explicit authority boundary. The extracted tree is used for inventory, live-file hashes for identity, source parsing for navigation, and a compiled Lean-environment export for endpoint declaration dependencies. The endpoint export is rooted at `NavierStokesR3.theorem_1_1`; it records 30,721 project declarations and 327,757 environment-derived edges, with no reachable `sorryAx` users in the recorded run. The corrected source parser reports 50,191 declarations and 186,194 token edges, which remain diagnostic only.

This control prevents a filename or token-match discrepancy from being promoted into a semantic refutation. It also prevents a clean endpoint closure from being misreported as proof that the exported witness carries the paper’s five-moment interpretation. CTR-005 therefore remains a selected-field transport obligation, not a claim about missing files or a kernel contradiction. Reproduction details are in `NavierStokesReview/evidence/hardened_mapping_method_2026-09-26.md`.

The corrected compiled-closure join also removes a possible underclaim: the relevant upstream declarations are not dead code. Exact environment routes reach `FiveRows`, both debt types, `scaleDebt`, `periodicVelocity`, `barMoment`, and the R³ packaging. The review therefore does not argue that these modules are absent or unreachable. The precise objection is that the exported candidate contract does not expose the value-level equality transporting the five named moments through the assembled Cartesian field and into the endpoint.

The raw endpoint signature confirms the boundary. `ActualCandidateAssembly.Witness`
is a proposition-valued nested existential definition, not a structure carrying
the paper’s five moments. It packages the selected schedule, away extensions,
forcing, candidate properties, consequences, H³ growth, force jet bounds, and
endpoint jet matching, but no `Debt`, `FiveRows`, `barMoment`, or selected
field equality for `(M,I,J,S,C_p)`. This is not evidence that the upstream
moment algebra is absent. It is evidence that its values have not been
transported into the exported Cartesian witness. The source-level cross-check
is recorded in
`NavierStokesReview/evidence/claim_cross_examination_2026-09-27.md`.

Evidence: `NavierStokesReview/evidence/selected_endpoint_routes_2026-09-26.md`.

## Reproducible mapping update: 2026-09-26

The review now uses the tree-maker export as a hashed inventory snapshot and
reconciles it with the live checkout without trusting rendered indentation.
The run contains 3,021 tree file entries, 3,058 live files, 2,997
unique-basename resolutions, 24 retained ambiguities, and zero missing
basenames. The compiled endpoint closure contains 30,721 project declarations
and no reachable `sorryAx` users. Its 327,757 raw environment edges are kept
distinct from the 227,128 edges whose endpoints have exact source-span joins.

This strengthens reproducibility and corrects path-level underclaims. It does
not change the substantive review result: reachability of `FiveRows`,
`PositiveOrderMoments`, `scaleDebt`, `periodicVelocity`, and `barMoment` is not
a theorem that their values are transported into the exported Cartesian
witness. The selected field-level transport obligation remains open.

The review-side claim register records this distinction explicitly:
`MAP-001` and `CTR-032` are structurally supported, `CTR-012` remains
conditional, and `CTR-005` remains open. The register validates mapping
prerequisites only; it does not convert compiled reachability into a
field-level transport theorem.

## Mapping control and unresolved endpoint

The hardened map confirms that the relevant upstream declarations are compiled
and reachable. It does not support a dead-code objection. The exact-name join
also retains ambiguous and unmatched environment nodes instead of silently
assigning source locations. The selected endpoint remains kernel-clean in the
captured closure, with zero reachable `sorryAx` users.

The review's load-bearing objection is therefore narrower and stronger: no
source-backed selected-path theorem has yet transported the values of
`FiveRows`/`barMoment` through localisation, curl, periodisation, summation,
and R³ packaging into the exported witness. This is a correspondence failure,
not a claimed kernel-level `False` result.

The current repository map is available through the synchronized source-map
records `hardened_source_map_2026-09-29.json` and
`hardened_source_map_2026-09-29.md`. It accounts for 2,794 Lean modules and
distinguishes live-source identity, source navigation, and compiled endpoint
reachability. This corrects file-presence
and dead-code overclaims. The map still leaves the substantive burden exactly
where it belongs: a selected-path value theorem transporting the five named
moments through the assembled Cartesian field into the exported witness.

Guide and reproduction: `docs/REPOSITORY_MAP_GUIDE.md`.

The browser map and mathematical reading layer are `docs/REPOSITORY_ARCHITECTURE_MAP.html` and `docs/MATHEMATICAL_SPECIFICATION.md`. The declaration-level graph is `NavierStokesReview/evidence/repository_audit_graph_2026-09-26.json`; it records exact joins and explicit metadata gaps without treating dependency reachability as field-level semantic transport.

## Paper-nuance correction: CMI wording and residual design

The source PDFs require a precise distinction. Fefferman describes the force
as given and externally applied, and imposes smoothness, decay or periodicity,
and global energy conditions on the alternatives. But the formal alternatives
(C) and (D) are existential statements; they do not contain a syntactic
independence predicate forbidding a force constructed from a selected flow.

OpenAI's Navier--Stokes paper explicitly chooses the flow and pressure and
defines the residual force, with smooth all-order cancellation as the central
technical task. The review therefore does not call residual construction an
automatic CMI violation. The adverse question is whether the Lean endpoint
actually carries the paper's five moments, correction stages, pressure,
localisation, residual cancellation, and whole-space obstruction into the
selected witness. CTR-005 remains that affirmative correspondence burden.

The Euler paper makes the corresponding parent--child stage and stability
claims explicitly. The review will not infer a temporal kink or Zeno failure
from nested intervals alone; those claims require source-level matching,
summability, and limit theorems. The full crosswalk is recorded in
`NavierStokesReview/evidence/paper_nuance_crosswalk_2026-09-27.md`.

## Verification status after the source cross-examination

The review does not allege that the five-moment mathematics is missing. The
current source route reaches real upstream definitions and theorems in
`PositiveOrderMoments.lean`, `FiveProfileMoments.lean`, `FiveRowRank.lean`,
`MeanRankUpdate.lean`, `MixedPeriodicAssembly.lean`, and
`DefectIncrementBounds.lean`. The adverse finding is narrower: no selected-path
theorem has been located that evaluates the complete assembled Cartesian field
and proves its equality with the paper tuple `(M,I,J,S,C_p)`.

The exact packaging boundary is `ActualCandidateAssembly.Witness` at
`1121-1151`, followed by `selected_witness` at `1177-1181`. It is a nested
existential proposition, not a structure carrying named moment fields. Its
payload proves the selected schedule, extensions, candidate properties,
consequences, H³ growth, and force endpoint jets. It does not quantify
`PositiveOrderMoments.Debt`, require `FiveRowRank.FiveRows`, apply `barMoment`
to the final Cartesian field, or assert the required five-moment equality.

This is a publication-level correspondence failure under CTR-005, not a
kernel-level `False` result. The source ledger also corrects two related
overstatements: the `StageEstimates` countermodel shows interface blindness,
not that the selected field is zero; and pressure recovery is comparative, not
proof that the selected pressure violates an absolute Poisson equation.

After the incompatible `.olean` cache was removed, a fresh aggregate build and
a bounded `NavierStokes.R3.Theorem` build exceeded their execution limits
without emitting a Lean error. This is recorded as incomplete post-clean
verification, not as a theorem failure. See
`NavierStokesReview/evidence/fresh_build_status_2026-09-27.md`.

## Finding 40: current source inventory and admission scope

The refreshed source map accounts for 2,790 Lean modules and 50,191 parsed
declarations. It records 3,021 tree entries, 2,997 unique-basename resolutions,
24 ambiguities, and no missing basenames. No `unsafe`, `axiom`, or `admit`
declarations were found. Four actual admitted bodies remain in the standalone
comparator challenge files; six additional `sorry` tokens occur only in
comments describing zero-sorry probes.

This closes the repository-inventory question, not the selected mathematical
transport question. The source map is current, whereas the last completed
compiled endpoint closure remains dated 2026-09-26. No conclusion about the
five-moment equality or a kernel-level `False` is upgraded by the census.

## Route-scope clarification: 2026-09-27

The reachable five-moment and rank modules are active upstream dependencies,
not dead files. Their observed consumers prove slow-base/exterior primitive
identities and correction-state/update invariants. The review therefore does
not infer a contradiction from their mere presence or from their separation
from the final proposition.

The unresolved test is value-level: locate a theorem that carries those
identities through the selected `potentialSum` fields, curl/localisation,
periodisation, `torusAverage`, and the exported Cartesian candidate. The
current `Witness` proposition has no such named equality. This is the precise
scope of CTR-005; it is not a kernel-level `False` result.

## Partial bridge inventory: 2026-09-27

The completion layer contains real intermediate bridges: finite-prefix curl
expansions, cutoff-gradient commutator identities, local radial scalar
formulae, torus/radial reductions, typed mixed-field `barMoment` pullbacks,
and selected cycle/base moment facts. The review therefore does not claim that
all bridge mathematics is absent.

The narrower finding is that no inspected declaration exports the final
value-level equality identifying the named paper tuple `(M,I,J,S,C_p)` with
the fully assembled selected Cartesian field after `potentialSum`, curl,
localisation, periodisation, `torusAverage`, radial pullback, `barMoment`, and
axis/whole-space extension. The exact inventory is in
`NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.
No nonzero remainder has yet been calculated; CTR-005 remains a correspondence
 burden, not a kernel-level `False` derivation.

## Global cross-layer verification boundary

The current source inspection confirms genuine results outside the moment
route: whole-space energy balance and uniform finite energy, smooth
localisation and periodisation, divergence-free assembly, origin residual-jet
transfer, and smooth late-time activation. These declarations must not be
relabelled as absent merely because they do not transport the paper's named
five observables.

The remaining distinctions are exact. Pressure recovery is comparative in
`p - q`; the selected pressure has no inspected standalone absolute Poisson
transport theorem. The force is constructed from traced residual jets in
`CandidateFromLimits.lean:80-110`, so CTR-012 records provenance and
trajectory dependence. Neither fact alone derives `False` from the literal
existential endpoint. Euler parent/child declarations are kept in their
separate source tree and are not imported as evidence about Navier--Stokes.

See `NavierStokesReview/evidence/global_cross_layer_audit_2026-09-27.md` for
the flat source ledger.

## Source cross-check of the proposed hidden bridge locations

The proposed junction search was completed against the live source. The
candidate files are present, and the local mathematics is substantive:
`LocalPaperTheorem.lean:128-176` proves local schedule properties;
`PaperLocalization.lean:28-48` proves local compact-candidate packaging;
`EntranceAlignedBase.lean:666-671` proves an aligned-base
`PositiveOrderMoments.moments` identity; and
`CorrectionState.lean:449-476` together with
`DefectIncrementBounds.lean:621-646,775-813` proves local `FiveRows`,
correction-moment vanishing, and rank-stage preservation.

These findings remove any defensible claim that the upstream five-row branch
is absent or wholly unused. They do not close CTR-005. None of the inspected
conclusions identifies the final mixed Cartesian field assembled at
`ActualCandidateAssembly.Witness` with the five paper observables after
`potentialSum`, curl, localisation, periodisation, `torusAverage`, and
`barMoment`. The remaining objection is therefore a value-level endpoint
transport obligation, not an import or naming objection.

The upstream route is stronger than this short junction list alone.
`GlobalSlowProfiles.profiles_moments`
(`GlobalSlowProfiles.lean:1043-1060`) proves all five rows for the constructed
positive-order profile sequence. `GlobalStressSupport.moments_zero`
(`GlobalStressSupport.lean:144-157`) transfers them to the axial and angular
histories, and `AssembledSlowBase.lean:592-617` uses the zero mass row to
prove an exterior primitive vanishes. These are transported local results;
the unresolved step is their identification with the final mixed Cartesian
fields after the complete assembly and projection chain.

## Reachable outgoing-profile identities

The selected source closure also contains a distinct outgoing-profile route:

```text
ActualCandidateAssembly
→ InitialPhysicalData → ActualPrimaryBounds → CorrectionInitialization
→ MeanRankUpdate → FiveProfileMoments → UniformAngularReset
→ OutgoingTail → OutgoingSchedule
```

`OutgoingSchedule.lean:739-747` defines the scalar `massMoment` and
`angularMoment` integrals. The theorems at `OutgoingSchedule.lean:846-927`
prove their endpoint cancellation, and `OutgoingTail.lean:908-923` preserves
the corresponding two identities through the extended angular profile. This
is genuine reachable profile mathematics and corrects any claim that the
moment branch is absent or unused.

The result does not close CTR-005. These declarations concern two scalar
outgoing-profile quantities used by the correction/rank route. They do not
identify the complete five named observables with the final `ASum`, `BSum`,
and `PSum` Cartesian fields after curl, localisation, periodisation, infinite
summation, torus averaging, and radial pullback. The remaining objection is a
value-level endpoint transport obligation, not an import or naming objection.

## Endpoint assembly correction

The source review confirms a genuine field-realisation chain. `finalPotential`
and `finalPotential_sameCurl` connect the slow-base vector potential to
`FinalSlowBase.velocity` (`TailGaugePotential.lean:433-450`). The initial and
positive stage fields are connected to Cartesian curl/chart representatives by
`ActualPhysicalStageBounds.lean:616-656` and
`ActualCandidateAssembly.lean:1003-1077`. The endpoint then constructs
`ASum`, `BSum`, and `PSum` and applies localisation, periodisation, and time
activation (`ActualCandidateAssembly.lean:1125-1151`).

The live objection is consequently more exact: upstream declarations prove
profile/history moment identities, including the two outgoing scalar endpoint
identities in `OutgoingSchedule.lean:739-950`, but the audit has not located a
selected-field theorem computing the named five observables on the final
activated Cartesian output after curl, localisation, periodisation, infinite
summation, torus averaging, and radial pullback. This is a value-level
transport question and must not be restated as a dead-code or no-assembly
claim.

### Scope of the finite-modification certificate

Direct inspection of `AssembledSlowBase.lean:1514-1529` shows that
`FiniteModification` carries one explicit mass-equality field, alongside
field, pressure, and support conditions. It does not itself carry the complete
five-observable equality. The other local identities are genuine separate
profile and rank results; the unresolved question is their value-level
composition into the final `ASum`/`BSum`/`PSum` field.

### Why the selected-field bridge is substantive

The paper's own construction makes the bridge a load-bearing obligation. Its
Section 4.2, equation (4.15), defines \(M,I,J,S,C_p\), and Lemma 4.4 uses
matching cumulative integrals to preserve exterior pressure, radial velocity,
and stress. Section 5.2, equations (5.10)--(5.11), uses a five-equation repair
system to remove exterior pressure/stress terms. The later localisation argument
also retains the terms generated when cutoffs are applied to vector potentials
and then differentiated.

The correct audit question is therefore whether a declaration in the selected
production path proves the corresponding equality for the final Cartesian
`ASum`/`BSum`/`PSum` field after summation, curl, localisation, periodisation,
torus averaging, radial pullback, and axis/outer-domain extension. Upstream
profile and rank certificates are positive evidence and must not be called dead
code. They do not substitute for that final value-level theorem. Because it is
not located in the inspected record, the paper-to-endpoint correspondence remains unestablished
under CTR-005. This is not evidence of an incorrect moment value or a kernel
contradiction; those require a concrete remainder or impossibility proof.

### Logarithmic profile/history bridge

The audit also verified a genuine intermediate bridge in
`NominalConeAssembly.lean`. The chart identities at lines 366-446 connect
the outgoing radial quantities `M` and `J`, and the corresponding heat-switch
quantities `I` and `S`, to the logarithmic history objects. The constructor
`NominalConeAssembly.Witness.log_histories` at lines 452-470 maps the profile
record into those outgoing and heat-switch histories, while lines 596-667
transport the associated parameters and derivatives. This is positive
evidence that the profile mechanism is used upstream. It is not, however, a
theorem whose input is the final `ASum`/`BSum`/`PSum` field or whose conclusion
computes the five observables after curl, localisation, periodisation,
activation, torus averaging, and radial pullback. The finding is therefore a
selected-field value-level transport failure on the current record, not a claim that
the profile/history branch is dead.
### Partial selected-field bridges and the adverse classification

The audit does not claim that every bridge is absent. The review tree proves several intermediate facts: typed scalar pullback into `barMoment`, torus-average reduction, a finite-prefix/`tsum` jet scope, and the cutoff--curl commutator. It also contains a positive-radius component-recovery formula. These are useful and should be credited.

They are not the endpoint theorem required by the paper. The adverse finding is that the current formal record does not evaluate the final activated Cartesian field, rather than merely an intermediate scalar representative, through summation, curl, localisation, periodisation, torus averaging, radial pullback, integrability/support, and the axis boundary. In particular, the conditional zero theorem in `PeriodicGlobalIntegral.lean:57-75` assumes positivity, proves non-integrability of a periodic function, and invokes `integral_undef`; it does not establish the selected field's physical moment value.

The defensible verdict therefore remains **not established as a paper-to-code correspondence**, while explicitly rejecting the weaker overclaim that no intermediate bridge exists. No unconditional `False` follows from these partial results.

### Source-tier re-audit and calibrated implication

The source-tier review confirms that the adverse finding is not based on absent or fictitious upstream mathematics. `PositiveOrderMoments.lean:21-23,77-84,192-301` contains a real five-coordinate debt and exact profile repair/target-moment theorems. `MeanRankUpdate.lean:24-44,137-169,195-200` contains a distinct three-coordinate physical debt interface and proves `FiveRows` for correction increments. These results are positive evidence for the construction's upstream machinery, but neither theorem has the final selected Cartesian field as input and the five-observable tuple as output.

The selected construction is also materially connected. `ActualCandidateConstruction.lean:205-257,289-345,832-970` defines the selected cycle, chart stages, direct/stream mean stages, and potential-stage field identities. `SpatialLocalization.lean:164-203,209-290,313-340` proves cutoff-before-curl, displays the cutoff-gradient commutator, and proves local periodised-field identities, periodicity, divergence freedom, and residual transfer. This rules out the weaker allegation that the construction is only a disconnected profile toy. The inspected record does not contain the value-level composition through `tsum`, curl, localisation, periodisation, torus averaging, radial pullback, support/integrability, and the axis boundary.

The correct peer-review statement is therefore: the formal record contains genuine local and intermediate certificates, but it does not yet establish that the final exported selected field realizes the five cumulative moments used in the paper's global mechanism. This is a load-bearing correspondence failure under CTR-005. It is not, without a computed nonzero remainder or impossibility theorem, a kernel-level `False` result.

### Additional correction/residual-tier check

The next source tier was also inspected. `InitialPhysicalData.lean` constructs selected physical source coefficients, carriers, pressure coefficients, and support data. `CorrectionStep.lean` retains the nonlinear covariance, transport, pressure, and residual cross-terms in the correction cycle. `BaseResidual.lean` constructs the asymptotic slow-base sums, Cartesian potential and velocity prefixes, spatial-curl rate bounds, pressure prefixes, and axis/growth estimates. These findings positively establish populated intermediate mathematics.

They do not change the endpoint classification. None of the inspected declarations exports the complete selected-field equality for the five paper observables after `tsum`, curl, localisation, periodisation, torus averaging, radial pullback, integrability/support, and axis extension. The remaining adversarial test is therefore concrete: compute the selected value, prove an impossibility, or locate the full transport theorem. A commutator formula or local moment balance alone is not a nonzero remainder.

### Further source tier: positive intermediate mathematics, unresolved endpoint composition

The next five priority-ranked modules were also inspected: `SlowBorelBase.lean`,
`SlowResidualMatching.lean`, `SignedStressPrimitive.lean`,
`UniformAngularReset.lean`, and `MeanChartCompatibility.lean`. They contain
real smooth slow-series bounds, radial stress and truncation identities,
compact signed moment-correction constructions, uniformly invertible reset
systems, and pullback/naturality results for torus averages, pressure, temporal
families, source moments, and rank/debt data.

This evidence narrows rather than removes CTR-005. The inspected declarations
remain at profile, correction, physical-pullback, or chart-compatibility level;
they do not provide the final value-level theorem for the selected Cartesian
`ASum`/`BSum`/`PSum` field through every operation in the paper's route. The
review therefore rejects both extremes: the machinery is not absent, but the
full selected-field five-moment correspondence is not yet established. A
nonzero remainder, an impossibility proof, or the complete positive bridge is
still required before any stronger verdict is justified.

The R3 packaging and adjacent source tier were checked as well.
`R3/ActualCandidate.lean` genuinely packages localized velocity and pressure
with smooth positive-time force, residual, support, finite-energy, and C/D
properties. `ActualInitialization.lean`, `FinalSlowBase.lean`,
`TerminalStress.lean`, and `MeanResidual.lean` provide populated initial,
slow-base, terminal-stress, and angular-mean identities. This rules out a
claim that the endpoint is only an empty wrapper. It still does not provide
the selected Cartesian field's final five-moment value theorem, so the
CTR-005 classification remains unchanged.

The formal contract and the next endpoint-adjacent tier were checked directly.
`ProblemStatement.lean` defines the actual candidate predicate and explicitly
does not assert existence there. `PeriodizedWaveBounds.lean` proves genuine
copy-sum and jet bounds, `GaugeMomentBalances.lean` proves measured moving-gauge
pressure identities, `BaseExterior.lean` proves canonical heat-exterior
identities, and `ActualBaseResidual.lean` proves chart/residual invariance and
base-field smoothness. These are substantive source results, but they still do
not provide the selected Cartesian field's final five-moment equality.

### Calibration of the additional adversarial comments

The comments correctly demand a field-level audit of the five-observable route.
They overstate three present results: the cutoff/curl commutator has not been
shown to have a nonzero radial integral; the concrete endpoint is not proved to
use only generic rates; and the record does not show that zero percent of the
paper's mathematics is formalised. Conversely, `Witness` still does not export
the final selected-field equality for `(M, I, J, S, C_p)`, so upstream imports
and intermediate certificates cannot close CTR-005 by themselves.

The residual force and fixed-force perturbation remain a serious provenance
test, but they do not add a force-independence premise to the literal
existential C/D proposition. The peer-review verdict therefore remains
**not established as paper-to-code correspondence**, while the audit continues
independently toward either a concrete nonzero remainder, an impossibility
theorem, or a positive full transport theorem.

The next reachable tier was also inspected. `CorrectionState.lean` contains
actual correction-state radial moments and `FiveRows`; `HeatTailEdit.lean`
contains weighted heat-tail pressure, energy, angular-debt, and jet estimates;
and `ActualMeanPhysicalData.lean` transports stage overlap and native-jet data.
These are positive intermediate certificates. They do not close the final
selected Cartesian five-observable transport, and they produce no nonzero
remainder or kernel contradiction.

### Latest reachable tier: continuation, slow base, rebase, and rank coherence

The next eight reachable modules were inspected directly. `OffplaneCorrectionExtensions`
extends positive-radius pressure/rank models to supported Cartesian continuation
data; `SlowBaseEndpoint` lifts profile, potential, velocity, and pressure data
to smooth away extensions; and `ConstructedSlowBase` proves finite coefficient
identities, stress-zero-core facts, jet flatness, smoothness, divergence,
origin growth, and residual identities for nominal and modified scales.
`BasePrefixIdentity` supplies finite-prefix curl/profile, radial-flux, pressure,
stress-force, and coefficient-match identities. `ActualReferenceRebase` proves
rebase/pullback identities for actual residual sources, frames, amplitudes,
pressures, phases, and periodic subcovers. `HarmonicWaveInteraction` proves
local harmonic-block, zero-mode, convolution, nonlinear-interaction, divergence,
and residual-difference identities. `ActualPrimaryDynamics` supplies primary
pulse geometry, copied velocity/pressure germs, cutoff/curl smoothness, and
local residual formulas. `RankStateCoherence` supplies fibre moments, measured
debt, normalised rank stages, and `FiveRows` conclusions for correction states.

These findings strengthen the positive source record and rule out a dead-code
description. They still do not provide the final theorem whose input is the
selected `ASum`/`BSum`/`PSum` Cartesian field and whose conclusion evaluates
\((M,I,J,S,C_p)\) after summation, curl, localisation, periodisation, torus
averaging, radial pullback, support/integrability, and the axis limit. The
cutoff-gradient commutator is therefore an adversarial calculation target, not
yet a proved nonzero defect. The calibrated classification remains **not
established as paper-to-code correspondence under CTR-005**; no kernel `False`
has been obtained. The current register contains 85 explicit source reviews
and 513 reachable modules awaiting semantic classification.

### Latest source tier: axisymmetric residual and mean-residual routes

Four further reachable modules were inspected. `AxisymmetricResidual` proves
regular-axisymmetric Cartesian velocity, pressure, divergence, differential,
Laplacian, and residual formulas, including an on-axis route.
`PhysicalParticularWave` proves particular-wave carrier, potential, curl,
pressure, chart-change, periodicity, and reference-domain identities.
`LeadingStress` proves reduced stress divergence, pressure derivatives, radial
pullbacks, and positive-radius residual transport. `LiftedMeanResidual` proves
smooth angular averaging, periodic invariance, conservative flux, averaged
differential identities, and nonlinear residual lifting.

These are positive local bridges, not the final selected-field theorem. They do
not evaluate \((M,I,J,S,C_p)\) after the complete sum/curl/localisation/
periodisation/torus-average/radial-pullback, support/integrability, and axis
route. No nonzero remainder, impossibility theorem, or kernel `False` was
obtained. The current register records 85 explicit source reviews and 513
reachable modules awaiting semantic classification.

### Latest source tier: wave bounds, signed data, and primary residuals

Four additional reachable modules were inspected: `LinearWaveBounds.lean`,
`ActualPhysicalStageBounds.lean`, `ActualSignedWaveData.lean`, and
`PrimaryResidualClass.lean`. They contain genuine coefficient, cutoff, curl,
signed-support, potential, pressure, native-stage, divergence, linear
residual, and primary-projection results.

This tier strengthens the positive source record and rules out describing the
repository as disconnected profile names. It does not provide the final
selected-field theorem evaluating `(M,I,J,S,C_p)` after summation, curl,
localisation, periodisation, torus averaging, radial pullback,
support/integrability, and the axis limit. A cutoff-gradient commutator is a
required term in that calculation, not a proved nonzero defect. No
impossibility theorem or kernel `False` was obtained. The register now records
85 explicit reviews and 513 reachable modules awaiting semantic
classification.

### Latest source tier: initial mean, cycle prefixes, and moment resets

Four additional reachable modules were inspected: `ActualInitialMeanEquation`,
`CyclePhysicalPrefixes`, `FiveProfileMoments`, and `AngularMomentReset`. They
contain initialized angular/mean-zero and divergence identities, finite local
Cartesian stage-prefix and residual identities, a genuine reduced
five-coordinate repair map, and a pressure-neutral local angular reset.

This tier strengthens the positive source record but does not provide the
final selected-field theorem evaluating `(M,I,J,S,C_p)` after summation, curl,
localisation, periodisation, torus averaging, radial pullback,
support/integrability, and the axis limit. No impossibility theorem or kernel
`False` was obtained. The register now records 85 explicit reviews and 513
reachable modules awaiting semantic classification.
### Latest source tier: graph, interaction, axis, pulse, rebasing, and stress review (2026-09-28)

Six further reachable modules were inspected: `GraphCalculus`, `LocalizedMeanInteraction`, `NaturalAxisRange`, `PulseGrowth`, `TorusMeanRequestRebase`, and `BaseStressClasses`. They confirm substantive off-axis graph calculus, local interaction classes, axis/cutoff control, scalar pulse-growth algebra, request rebasing, and weighted stress/jet estimates. They do not establish the final selected-field equality for `(M,I,J,S,C_p)`. The register now records 335 semantically inspected reachable modules and 278 still open. No nonzero defect, impossibility theorem, or kernel `False` was obtained.

### Latest source tier: assembly, geometry, and axis-series review (2026-09-28)

Six further reachable modules were inspected: `PrimaryFieldAssembly`,
`R3/ComparisonGronwall`, `UniformHarmonicInteraction`, `ActualCycleGeometry`,
`ActualPolarCoverage`, and `AxisSeries`. They confirm substantive periodised
field assembly, covariance and torus-average declarations, R3 comparison
inequalities, harmonic interaction bounds, actual geometry identities,
axis-aware coverage, and scalar profile-series estimates. They do not establish
the final selected-field equality for `(M,I,J,S,C_p)`. The register now records
329 semantically inspected reachable modules and 284 still open. No nonzero
defect, impossibility theorem, or kernel `False` was obtained.

### Latest source tier: scales, endpoint coordinates, and R3 comparison estimates (2026-09-28)

Four further reachable modules were inspected: `ChartScales`, `EndpointCoordinates`, `R3/CompactComparisonBounds`, and `R3/ComparisonFiniteEnergy`. They confirm substantive scale/asymptotic, endpoint-coordinate, compact comparison, finite-energy, and tensor-difference mathematics. They do not establish the final selected-field equality for `(M,I,J,S,C_p)`. The register now records 339 semantically inspected reachable modules and 274 still open. No nonzero defect, impossibility theorem, or kernel `False` was obtained from this tranche.
### 2026-09-28 priority-69 source tranche: nine modules registered

Direct source review completed for `AnnularEndpoint.lean`, `AxisContraction.lean`, `PhysicalCopyBounds.lean`, `R3/LocalizedFluxEstimates.lean`, `ResetEnergyBounds.lean`, `ScaledActualParticularControl.lean`, `TerminalCone.lean`, `ViscousPropagator.lean`, and `VolterraAnalyticBounds.lean`. These modules add substantive support/germ, periodisation, reduced-axis, tail-energy, cone, coefficient-propagator, and analytic Volterra bounds. They do not state the final selected Cartesian `torusAverage`/`barMoment` transport theorem, and this tranche yields no nonzero defect, impossibility theorem, or kernel `False`.

The regenerated full semantic register now reports **355 evidence-inspected reachable modules** and **258 reachable modules still open**. The authoritative outputs are `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`, `.md`, and `.html`, mirrored under `docs/`. Detailed evidence is in `NavierStokesReview/src/audit/priority_69_annular_axis_copy_flux_reset_cone_propagator_source_review_2026-09-28.md`.

### 2026-09-28 priority-70 source tranche

Four further reachable modules were inspected: `ActivationBounds`, `ActualWaveRegularity`, `CommonBaseContext`, and `CopySolveCompatibility`. They confirm substantive activation, smooth wave/curl/tsum regularity, base/stress-context, and generic copy-solve transport mathematics. They do not establish the final selected-field equality for `(M,I,J,S,C_p)`. The register now records 359 semantically inspected reachable modules and 254 still open. No nonzero defect, impossibility theorem, or kernel `False` was obtained from this tranche.

### 2026-09-28 priority-71 source tranche

Four further reachable modules were directly source-reviewed: `LocalizedCurlRealization`, `MixedDiagonalExtensions`, `ActualCarrierTransport`, and `FiniteHeadClass`. They confirm substantive local curl/divergence and germ realization, potential support/extension, carrier-record binding, and finite-prefix jet-class transfer. They do not establish the final selected-field equality for `(M,I,J,S,C_p)`. The register remains at 359 semantically inspected reachable modules and 254 still open because these rows were previously evidence-classified. No nonzero defect, impossibility theorem, or kernel `False` was obtained from this tranche.

### 2026-09-28 priority-72 source tranche

Four further reachable modules were directly source-reviewed: `CorrectedPulseAmplitude`, `PrimaryGeometryAssembly`, `R3/ComparisonTimeAverages`, and `SlowFirstOrderEdge`. They confirm substantive corrected energy-reset, reduced phase/chart geometry, finite-energy time-average, and conditional radial-stress mathematics. `SlowFirstOrderEdge` states that global moment closure is supplied by separate renormalized-moment and slow-order theorems; its scalar weighted closure is not the final selected Cartesian five-observable transport theorem. The register now reports 363 semantically inspected reachable modules and 250 still open. No nonzero defect, impossibility theorem, or kernel `False` was obtained from this tranche.

### 2026-09-28 priority-73 source tranche

Six further reachable modules were directly source-reviewed: `ActualBaseVelocityBounds`, `BaseContextAssembly`, `PhaseEstimates`, `PrimaryRepresentatives`, `PositiveRepresentatives`, and `ReservedPatches`. They confirm substantive actual coefficient/support and rate identities, reduced stress realisation, phase/representative geometry, and radial five-row patch mathematics. They do not establish the final selected-field equality for `(M,I,J,S,C_p)`. The register now reports **369 semantically inspected reachable modules and 244 still open**. No nonzero defect, impossibility theorem, or kernel `False` was obtained from this tranche. Detailed evidence: `NavierStokesReview/src/audit/priority_73_base_representative_reserved_source_review_2026-09-28.md`.
## Latest source-coverage update: 2026-09-28

The authoritative register now reports **375 semantically inspected reachable modules and 238 still open** out of 588 reachable, with 0 missing project import edges. The latest six direct reviews classify activation/control/extension/frame layers and preserve the calibrated finding: endpoint five-observable transport remains unestablished; no `Delta m != 0`, impossibility theorem, or `False` was obtained in this tranche.
## Latest source-coverage update: 2026-09-28 cutoff/Volterra/wave-interaction tranche

The authoritative register now reports **381 semantically inspected reachable modules and 232 still open** out of 588 reachable, with 0 missing project import edges. The latest six direct reviews add positive evidence for local-finite sums, angular moments, tail energy, and exact support-separated curl cancellation. The calibrated finding remains: complete endpoint five-observable transport is unestablished; no `Delta m != 0`, impossibility theorem, or `False` was obtained in this tranche.
## Latest source-coverage update: 2026-09-28 radial/chart/integral tranche

The authoritative register now reports **392 semantically inspected reachable modules and 221 still open** out of 588 reachable, with 0 missing project import edges. The latest eleven direct reviews add positive base-radial and actual-integral evidence. The calibrated finding remains: complete endpoint five-observable transport is unestablished; no `Delta m != 0`, impossibility theorem, or `False` was obtained in this tranche.

## Latest source-coverage update: 2026-09-28 axis/dilation/extension/ODE tranche

The authoritative register now reports **400 semantically inspected reachable modules and 213 still open** out of 588 reachable, with 0 missing project import edges. The latest eight direct reviews add positive axis-series, radial-extension, and reduced-profile moment evidence, especially the actual `M`, `I`, `J`, `S`, and axis-datum definitions in `OutgoingDilation`. The calibrated finding remains: complete selected Cartesian endpoint transport is unestablished; no `Delta m != 0`, impossibility theorem, or `False` was obtained in this tranche.

## Latest source-coverage update: 2026-09-28 priority-78

The authoritative register now reports **2,790 indexed; 588 reachable; 414 evidence-inspected; 199 reachable still open**, with 0 missing project import edges. The latest fourteen direct reviews add positive phase-defect, axis-algebra, coefficient-weight, polar-chart, stress-activation, and weighted-Volterra evidence. The calibrated finding remains: complete selected Cartesian endpoint transport is unestablished; no `Delta m != 0`, impossibility theorem, or `False` was obtained. Evidence: `NavierStokesReview/src/audit/priority_78_phase_defect_axis_algebra_weighted_volterra_source_review_2026-09-28.md`.

## Latest source-coverage update: 2026-09-28 priority-79

The authoritative register now reports **2,790 indexed; 588 reachable; 420 evidence-inspected; 193 reachable still open**, with 0 missing project import edges. The latest six direct reviews add positive axis-operator, chart/component, matching-cone, physical-coordinate, signed-covariance, and moving-edge evidence. The calibrated finding remains: complete selected Cartesian endpoint transport is unestablished; no `Delta m != 0`, impossibility theorem, or `False` was obtained. Evidence: `NavierStokesReview/src/audit/priority_79_axis_chart_matching_coordinate_covariance_edge_source_review_2026-09-28.md`.
## Priority 80 source cross-check (2026-09-28)

Six further reachable modules were inspected directly. They supply axis regularity, endpoint gluing, phase-jet bounds, exact reduced radial integral identities, reference-history reconstruction, and weighted radial/mean-class transport. This strengthens the positive intermediate record while leaving the selected-field correspondence unresolved. No reviewed declaration proves a final Cartesian `barMoment` equality or selected `Witness` transport, and no nonzero defect or kernel `False` is claimed.
## Priority 81 source cross-check (2026-09-28)

The review found actual reduced-moment and residual bridges: exact two-moment outgoing cancellation, pressure-defect-to-mass equality, potential-sum residual identity with physical joint jets, and periodic-to-compact R3 packaging. These findings rule out a blanket “moment-free code” description. The load-bearing open question remains the full selected Cartesian five-observable transport into the exported `Witness`; no nonzero defect or kernel contradiction is claimed.

## Priority 82 source cross-check (2026-09-28)

The next six direct reviews add actual three-component debt bounds, annular exterior vanishing, exact R³ energy and support scaling, a selected-to-compact candidate wrapper, and exact reduced entrance flux identities. These are substantive positive bridges and should be cited when describing the code. They remain intermediate or reduced-layer results; no reviewed declaration composes them into the complete selected Cartesian `(M,I,J,S,C_p)` equality at `ActualCandidateAssembly.Witness`. The calibrated classification therefore remains a correspondence failure under review, not a claimed kernel contradiction.

## Priority 83 source cross-check (2026-09-28)

The latest six direct reviews add exact mask-partition normalisation, actual mixed curl-plus-angular field/divergence and axis-germ results, Gaussian tail control, leading-stress edge/exterior bounds, signed torus/radial request identities with zero adjusted moments, and pulse covariance/cone positivity. These findings further rule out descriptions of the repository as a hollow or moment-free shell. They remain intermediate layers and do not establish the full selected Cartesian five-observable transport into `Witness`; no nonzero defect or kernel contradiction is claimed.

## Priority 84 source cross-check (2026-09-28)

The latest six direct reviews add positive-axis profile existence, pulse-lag and reset identities, radial heat moment ODEs, renormalised release moments, heated physical axial-viscosity cancellation, and torus/Jacobian/periodisation averages. The current register is 2,790 indexed, 588 reachable, 450 evidence-inspected, and 163 reachable-open, with zero missing project import edges. These results correct any blanket claim that the repository lacks moment or averaging mathematics; they do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `ActualCandidateAssembly.Witness`. No `Delta m != 0`, impossibility theorem, or `False` is claimed. Evidence: `NavierStokesReview/src/audit/priority_84_axis_heat_release_torus_source_review_2026-09-28.md`.

## Priority 85 source cross-check (2026-09-28)

`RepairConeBounds.actual_moments` proves genuine reduced-profile five-coordinate transport to `freeRows`, and `physical_rows`, `physical_stock_values`, `physical_transport`, `physical_lags`, and `physical_stocks` carry that result through explicit physical chart quantities. `HeatSwitchCone` and the signed geometry/stage-control modules add compensated cone, finite-sum, covariance, support, and jet results. The current register is 2,790 indexed, 588 reachable, 456 evidence-inspected, and 157 reachable-open, with zero missing project import edges. The peer review must therefore avoid saying the five-moment bridge is absent everywhere; the unresolved issue is its composition into the final Cartesian selected endpoint and public `Witness`. No `Delta m != 0`, impossibility theorem, or `False` is claimed. Evidence: `NavierStokesReview/src/audit/priority_85_signed_geometry_repair_cone_source_review_2026-09-28.md`.

## Priority 86 source cross-check (2026-09-28)

`BaseRankPatch.five_rows` is direct evidence of a local `FiveRowRank.FiveRows` theorem for the full final base. The accompanying six-file tranche also proves actual cycle/covariance preservation, variable-gauge rank bounds, physical terminal compensation, and concrete mean-stage support data. The current register is 2,790 indexed, 588 reachable, 462 evidence-inspected, and 151 reachable-open, with zero missing project import edges. These findings strengthen the local/reduced construction record but do not establish its full composition into the final selected Cartesian field and public `Witness`. No `Delta m != 0`, impossibility theorem, or `False` is claimed. Evidence: `NavierStokesReview/src/audit/priority_86_rank_cycle_compensation_source_review_2026-09-28.md`.

## Priority 87 source cross-check (2026-09-28)

The latest six direct reviews add actual axisymmetric/local residual grouping, diagonal stage-to-limit jet and spatial-curl rates, compact temporal/spatial force decay, and a uniform \(R^3\) compact-force \(L^2\) bound. The authoritative register is 2,790 indexed; 588 reachable; 468 evidence-inspected; 145 reachable-open; and 0 missing project import edges. These are positive intermediate results. `DiagonalResidual` does not prove a fixed-tail radial-moment identity, and the tranche does not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_87_residual_grouping_decay_compact_force_source_review_2026-09-28.md`.

## Priority 88 source cross-check (2026-09-28)

The latest fifteen direct reviews add actual reduced cone/stress and loop-moment algebra, analytic axis/heat extensions, similarity-coordinate transitions, Cartesian axisymmetric curl and support identities, periodised-copy solves, and temporal mean updates. The authoritative register is 2,790 indexed; 588 reachable; 483 evidence-inspected; 130 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_88_profile_cone_cover_similarity_mean_source_review_2026-09-28.md`.

## Priority 89 source cross-check (2026-09-28)

The latest eleven direct reviews add compact/reduced moment repair, torus inverse and alias transport, reduced stress algebra, local gauge-mass preservation, and Cartesian curl covariance. The authoritative register is 2,790 indexed; 588 reachable; 494 evidence-inspected; 119 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_89_moment_repair_stress_alias_curl_source_review_2026-09-28.md`.

## Priority 90 source cross-check (2026-09-28)

The latest five direct reviews add generalised-power/bump moment-matrix nonsingularity, prepared and scheduled outgoing profiles, R3 Gaussian integrability, and smooth quadratic repair. The authoritative register is 2,790 indexed; 588 reachable; 499 evidence-inspected; 114 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_90_moment_matrix_prepared_profiles_gaussian_solver_source_review_2026-09-28.md`.

## Priority 91 source cross-check (2026-09-28)

## Priority 92 source cross-check (2026-09-28)

The next seven direct reviews add real R3 energy/dissipation estimates, smooth positive-time force localisation, off-axis residual polar reconstruction, scalar forced Gronwall bounds, and uniform primary/curl rate classes. The authoritative register is 2,790 indexed; 588 reachable; 508 evidence-inspected; 105 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_92_r3_energy_force_polar_graph_uniform_weights_source_review_2026-09-28.md`.

The next two direct reviews add a real smooth parametric torus-inverse/Fourier layer and a real periodic-phase/common-cover assembly layer. They establish zero-mean and periodicity preservation, inverse-multiplier and finite-jet bounds, compact clock windows, locally finite tsum periodisation, phase and angular-lift identities, geometry transport, and carrier-adapter germs/jets. The authoritative register is 2,790 indexed; 588 reachable; 501 evidence-inspected; 112 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_91_parametric_inverse_periodic_phase_source_review_2026-09-28.md`.
## Priority 93 source cross-check (2026-09-28)

The next six direct reviews add real joint-limit/flat-residual extension results, reduced matching-debt and profile-existence bounds, relative maximal-lifespan reasoning, exact rate-class reindexing, pulse energy-history control, and an off-axis radial-flux residual bridge. The authoritative register is 2,790 indexed; 588 reachable; 514 evidence-inspected; 99 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_93_limits_debt_lifespan_reindex_pulse_flux_source_review_2026-09-28.md`.
## Priority 94 source cross-check (2026-09-28)

## Priority 95 source cross-check (2026-09-28)

The next eighteen direct reviews confirm real relative pressure-flux and compact-test Poisson identities, temporal pressure integration, Riesz/Fourier operator estimates, viscosity and normal scaling, whole-space comparison closure, support bookkeeping, and tangent-projection algebra. The authoritative register is 2,790 indexed; 588 reachable; 539 evidence-inspected; 74 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish an absolute selected-pressure representative or the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_95_r3_pressure_comparison_scaling_source_review_2026-09-28.md`.

The next seven direct reviews add real reduced history/repair identities, initial mean/covariance/rank data, harmonic support and angular calculus, exterior prefix/germ agreement, local particular-mean covariance gain, and signed potential/pressure support. The authoritative register is 2,790 indexed; 588 reachable; 521 evidence-inspected; 92 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_94_histories_means_harmonic_exterior_source_review_2026-09-28.md`.

The next nineteen direct reviews add concrete core/support geometry, switching and its explicit residual identity, comparative weak pressure/Poisson recovery, compact pressure-flux tests, Riesz test regularity, reduced schedule pressure, tail/cone bounds, and uniform block-rate infrastructure. The authoritative register is 2,790 indexed; 588 reachable; 558 evidence-inspected; 55 reachable-open; and 0 missing project import edges. These are positive intermediate results. They do not establish an absolute selected-pressure representative or the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`, a nonzero defect, an impossibility theorem, or `False`. Evidence: `NavierStokesReview/src/audit/priority_96_core_support_pressure_recovery_localization_source_review_2026-09-28.md`.

The next eleven direct reviews correct the scope of the remaining bridge. `ActualMeanPotentialRealization` and `TailGaugePotential` contain genuine local Cartesian-curl/potential identities, and `NominalConeAssembly` contains genuine reduced/chart moment identities. The unresolved issue is their composition through the selected global sums, localisation, periodisation, and public `Witness` observables. This is a narrower CTR-005 correspondence question, not evidence that all curl or moment infrastructure is absent. Evidence: `NavierStokesReview/src/audit/priority_97_local_curl_profile_moment_bridge_source_review_2026-09-28.md`.

The next eleven direct reviews add genuine signed native regularity, gauge/alias decay and coherence, interval-copy and tangent transport, support preservation, reduced exterior matching, axis pressure data, positive-time signed wave data, and reduced pressure-kernel bounds. These strengthen the intermediate construction record but do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport into `Witness`. Evidence: `NavierStokesReview/src/audit/priority_98_signed_gauge_copy_support_axis_transport_source_review_2026-09-28.md`.

The next twelve direct reviews add current-band support, signed request/amplitude/pressure `tsum` transport, cycle-state coherence, angular curl invariance, dependent-family periodisation, reduced natural-axis bridges, future pressure data, physical-stage bounds, and comparative pressure-flux estimates. They narrow the remaining composition question but do not establish the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` theorem, a nonzero defect, an impossibility result, or `False`. Evidence: `NavierStokesReview/src/audit/priority_109_carrier_cycle_signed_axis_pressure_source_review_2026-09-28.md`.

The next four direct reviews add initial-state construction, state/block/axis cycle coherence, particular-cycle native data, and reduced corrected-pressure matching and bounds. Priority 111 adds three direct reviews of cycle preservation, curl-corrected particular realization, and germ/cutoff transport. Priority 112 adds direct reviews of activation stocks, locally finite diagonal `tsum` jet/tail bounds, and compensated outgoing-profile integral identities. Priority 113 adds heated outgoing reduced-profile identities, mode-solenoidal reindexing, and shaped-wait temporal bounds. These are substantive intermediate bridges but do not establish the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` theorem, a nonzero defect, an impossibility result, or `False`. Evidence: `NavierStokesReview/src/audit/priority_110_cycle_initial_particular_pressure_source_review_2026-09-28.md`, `NavierStokesReview/src/audit/priority_111_cycle_preservation_particular_realization_source_review_2026-09-28.md`, `NavierStokesReview/src/audit/priority_112_activation_diagonal_extended_heated_source_review_2026-09-28.md`, and `NavierStokesReview/src/audit/priority_113_heated_mode_reindex_shaped_wait_source_review_2026-09-28.md`.


## Concluding adjudication: literal CMI compliance and force provenance

The review must distinguish three propositions that are often collapsed into one:

1. whether the Lean endpoint proves its stated existential breakdown proposition;
2. whether that proposition is equivalent to Fefferman’s literal Alternative (C); and
3. whether the construction realises the physical, forward-Cauchy interpretation suggested by Fefferman’s explanatory language and by the OpenAI manuscript.

### Literal CMI level

Fefferman’s Alternative (C) asks for a smooth divergence-free initial field and a smooth force satisfying the stated decay conditions such that no global smooth solution with bounded kinetic energy exists. The text calls the force “given” and “externally applied”, but it does not add a formal predicate requiring independence between the method used to choose \(f\) and the solution eventually exhibited.

The OpenAI manuscript is explicit about its method: for a chosen incompressible \(u\) and pressure \(p\), it defines \(f\) as the momentum residual and then proves that the residual and all derivatives extend smoothly through the singular time. This is not a concealed compiler device. It is an inverse-design construction stated in the manuscript itself.

The Lean endpoint is aimed at the same existential structure. NavierStokes/R3/ProblemStatement.lean:92-109 requires a smooth compactly supported force, a pre-singular smooth candidate, the residual identity, bounded energy on \(0\leq t<1\), and speed unbounded as \(t\uparrow1\). ProblemStatement.lean:119-135 defines a global competitor with the same force and zero initial datum, smooth for all future times and uniformly finite-energy. ProblemStatement.lean:150-153 then states the breakdown proposition as existence of the candidate together with nonexistence of such a global competitor. NavierStokes/R3/Theorem.lean:46-49 exports that proposition.

Accordingly, the absence of a literal final-field tuple \((M,I,J,S,C_p)\) is not by itself a value-level proof that the selected force is nonsmooth. But it is also not permissible to conclude from the comparator theorem alone that OpenAI has verified the manuscript's CMI solution. Fefferman's C statement is embedded in the connected definition of a smooth, physically reasonable solution: the force and initial data must satisfy (4)--(5), and any accepted global solution must satisfy (1)--(3), (6), and (7). If the Lean definitions and proofs are accepted extensionally, they establish a Lean proposition with those declared clauses. The review question is stronger: whether those clauses are realised by the same selected fields, residual force, and load-bearing moment/correction mechanism described in the manuscript. That paper-to-endpoint equivalence remains unestablished.

### Physical-projection level

The competing Physical-Projection Equivalence hypothesis identifies a genuine issue with an overly syntactic reading. In the manuscript’s similarity ansatz, \(U\), \(E\), and \(\Pi\) are not arbitrary bookkeeping variables: they determine the cylindrical velocity and pressure components in the core and annulus. The five cumulative radial integrals therefore have physical meaning within that reduced axisymmetric construction. They control pressure data, radial velocity, stress matching, and the five-equation correction cycle. The source record confirms the corresponding Lean machinery is active and consumed by finite residual identities and flatness estimates.

But the stronger inference does not follow automatically:

\[
  \text{profile identity in }(X,\eta)
  \not\Rightarrow
  \text{same five-observable equality for the final whole-space field}
\]

without the relevant change-of-variables, boundary, cutoff, summation, periodisation, pressure, and integrability theorems. The paper itself describes later curls, cutoffs, correction sums, and localisation. A review must therefore ask whether the profile identities are preserved at each point where the paper uses them, rather than demand a tuple field merely because the endpoint has a different representation.

The correct conclusion is not that the moments are “mere abstract scaffolding”, and not that their absence from Witness proves failure. Their reduced-profile role is load-bearing and internally represented. What remains unclosed is the complete semantic composition from those profile identities to the final selected endpoint and its interpretation as the paper’s full construction.

### Force provenance level

The residual definition

\[
  f=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
\]

does reverse the usual explanatory direction of a forward Cauchy problem: the trajectory is designed first and the force is obtained from it. A fixed-force perturbation result can therefore establish path dependence of this design. That is a material physical-provenance objection.

It is not, by itself, a contradiction of Alternative (C), because Alternative (C) quantifies over one admissible pair \((u_0,f)\) and asks whether a global physically reasonable solution exists for that pair. Once the residual-defined \(f\) is constructed and shown to satisfy the required regularity and decay conditions, the literal existential statement does not contain a second quantifier demanding that \(f\) remain valid under arbitrary perturbations of \(u\). The provenance objection therefore challenges the physical interpretation and the manuscript’s causal presentation, not the literal existential proposition by itself.

### Final adjudication

The earlier formulation that “both hypotheses are equally defensible” is too imprecise. The findings have a definite hierarchy:

| Question | Adjudication |
|---|---|
| Does the profile mechanism have physical meaning in the paper? | Yes. It is part of the reduced cylindrical construction and correction argument. |
| Is moment/rank restoration absent from the selected Lean construction? | No. The source shows it feeding finite identities and residual-flatness obligations. |
| Does the lack of a final tuple field refute Alternative (C)? | No. That is not the literal CMI endpoint predicate. |
| Does compilation alone prove exact paper-to-code correspondence? | No. The complete selected-field composition remains an audit question. |
| Does residual-defined forcing violate the literal existential quantifier? | Not automatically. It remains a force-provenance and physical-interpretation objection. |
| Has a selected-path mismatch, impossibility theorem, or False been proved? | No, not on the current record. |

The defensible review verdict is therefore: **the forced Lean endpoint is a substantive formalisation of an existential breakdown proposition and is not refuted merely because Witness lacks a literal five-moment tuple; nevertheless, exact equivalence between that endpoint, the complete 165-page construction, and the physical forward-Cauchy interpretation remains unestablished until the remaining cross-layer composition is proved or disproved.** This is a narrower and stronger conclusion than either “the moments are irrelevant” or “the endpoint is already formally false”.

Evidence: NavierStokesReview/evidence/selected_profile_moment_dependency_adjudication_2026-09-29.md, docs/navier-stokes openai.txt:109-124,488-496,523-546,727-753, docs/navierstokes.txt:25-81, and NavierStokes/R3/ProblemStatement.lean:92-153.


### Source correction: the moment mechanism is not missing internally

The review withdraws any wording suggesting that the selected construction proves blow-up while omitting the moment/rank restoration mechanism. The source shows the opposite: repaired profile moments feed conservative stress/pressure identities, finite Cartesian residual identities, and the jet-flatness obligations used by the construction. `origin_blowup` is only the proof of one conjunct, not the complete candidate proof.

The unresolved issue is not a literal tuple-field test. In the paper, `(M,I,J,S,C_p)` are reduced-profile cumulative integrals used at joins and correction stages. The remaining question is whether those identities and their stated consequences are semantically carried through the complete selected mixed assembly, infinite sums, localisation, periodisation, pressure, force, support, and endpoint interpretation. That is the adverse correspondence question currently under audit. It supports a calibrated “not established” finding, but it is not itself a proof of a mismatch or `False`. Evidence: `NavierStokesReview/evidence/selected_profile_moment_dependency_adjudication_2026-09-29.md`.

## Final source-grounded adjudication of the physical-projection hypothesis

The earlier statement that Hypotheses A and B were both defensible without a hierarchy was too loose. The manuscript supports the physical-projection part of Hypothesis B: (E,U,Pi) determine the leading cylindrical velocity and pressure components (`docs/navier-stokes openai.txt:331-368`), and the five cumulative radial quantities are used to preserve pressure, radial velocity, and stress across joins (`:488-496`, `:523-546`), to restore the modulated profile (`:539-546`), and to cancel the five classes of correction defects (`:727-735`). The review therefore does not classify the moments as irrelevant or as disconnected bookkeeping.

The remaining question is not whether the paper uses the moments. It does. The question is whether the exact consequences used in the paper are carried through the selected Cartesian assembly, shrinking-cutoff sum, pressure reconstruction, localisation, periodisation, support, and final force. The paper does not state this obligation as a single endpoint record equation

\[
\operatorname{moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  =(M,I,J,S,C_p).
\]

Accordingly, the absence of that one tuple from `ActualCandidateAssembly.Witness` is not a refutation. It is also not a positive proof of every paper-level consequence. The raw Lean source shows active profile certificates, repaired coefficient matching, finite Cartesian residual identities, jet estimates, and selected chart identities. The earlier blanket statement that the moment/rank mechanism is missing or bypassed is withdrawn. The adverse finding is narrower: exact end-to-end equivalence between the internal consequences and every paper assertion remains unestablished on the inspected record.

Fefferman's text describes the force as given and externally applied (`docs/navierstokes.txt:25-40`), while Alternative (C) is formally existential over one admissible pair (`:74-77`). OpenAI's manuscript openly defines the force from the chosen residual and makes smooth cancellation the construction target (`docs/navier-stokes openai.txt:109-124`). Thus residual-designed forcing reverses the usual explanatory direction of a forward Cauchy problem and remains a serious physical-provenance objection, but it is not by itself a contradiction of the literal existential CMI predicate.

The final review conclusion is therefore definite but calibrated: the forced Lean endpoint is a substantive formalisation of an existential breakdown proposition, and its moment/rank mechanism is internally used. The current record does not yet establish that the endpoint is equivalent to every paper-level physical consequence or to Fefferman's forward-Cauchy interpretation. A concrete selected-field mismatch, an impossibility theorem, or a proved failure of a mandatory paper consequence would be required before escalating this correspondence finding to a formal refutation. This is an audit of the advertised claim, not a request that OpenAI repair its work.

Evidence: `NavierStokesReview/evidence/physical_projection_equivalence_adjudication_2026-09-29.md`.

## Adjudication of the force-smoothness rebuttal (2026-09-29)

The raw source does not support the stronger claim that `NativeBounds` are
accepted as an unproved substitute for the five-moment mechanism. Concrete
physical data feed `actualStageEstimates`, selected estimates derive the common
schedule and all residual jet rates, and `CandidateFromLimits.force_smooth` is
derived from the full residual boundary-jet limits. The adverse finding remains
that the inspected endpoint does not export the complete paper-to-selected-
field observable correspondence. The supplied claims that the manuscript
states an explicit Fredholm-adjoint-Laurent “if and only if” theorem, that the
five moments are the sole cancellation route, or that every residual summand
diverges at `t=1` were not found in the extracted manuscript. AX-033 is an
abstract non-entailment result, not a physical nonzero-moment countermodel.

Evidence: `NavierStokesReview/src/audit/priority_161_rebuttal_force_smoothness_moment_boundary_adjudication_2026-09-29.md`.

## Whole-formulation CMI crosswalk: adjudication of the five-step rebuttal

The supplied rebuttal correctly insists that Fefferman's force conditions,
OpenAI's residual construction, the paper's five-moment mechanism, and the
Lean endpoint must be analysed as a connected system. The audit therefore does
not treat Alternative (C) as a free-standing software label. It checks the
force smoothness/decay predicates, the no-global-solution conclusion, the
manuscript's correction mechanism, and the selected-field composition together.

The rebuttal nevertheless makes two unsupported implications. First,

\[
\|u(t)\|_{\infty}\to\infty
\quad\not\Rightarrow\quad
\partial_tu,(u\cdot\nabla)u,\Delta u,\nabla p
\text{ each diverge}.
\]

The signed residual can contain cancellations; a termwise divergence theorem
at a common point or in a specified norm is required. Secondly, the extracted
manuscript establishes five-moment matching and correction as load-bearing, but
the current text search does not establish an explicit sole-mechanism
Fredholm/adjoint/Laurent “if and only if” theorem.

The source-grounded conclusion is consequently precise. The comparator route
does prove the literal forced CMI-shaped existential proposition, using a force
whose smoothness is derived through concrete physical data, residual rates,
derivative recurrence, boundary limits, and smooth extension. The public
`Witness` still does not expose the complete semantic identification between
those selected fields and every paper-level five-moment consequence. That is a
real paper-to-code correspondence gap, **NOT ESTABLISHED**, but it is not yet a
selected-field nonsmoothness proof or a formal refutation of Alternative (C).

Evidence: `NavierStokesReview/src/audit/priority_163_full_cmi_dependency_crosswalk_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_full_cmi_dependency_crosswalk_2026-09-29.json`.

### Full-closure correction

The endpoint import closure must not be described as moment-blind in the broad
repository sense. A direct closure run rooted at `NavierStokes.R3.Theorem`
found 588 project modules, including 32 modules with exact moment/rank symbols.
Representative declarations include `FiveProfileMoments.physicalMoments_eq`,
`PositiveOrderMoments.moments_repair_target`,
`GlobalStressSupport.moments_zero`, `MeanRankUpdate.physical_five_rows`, and
`TerminalCompensation.physicalMoments_cancel`.

The remaining finding is narrower: `ActualCandidateAssembly.Witness` does not
export a theorem identifying the final selected Cartesian observables with
`(M,I,J,S,C_p)`. Import reachability proves that the upstream machinery is
present, not that its identities are transported through the selected sums,
localisation, periodisation, and activation. The audit therefore retains
`CTR-005` as a final correspondence finding, not as a claim that the moment
machinery is dead or absent.

Evidence: `NavierStokesReview/evidence/source_tranche_full_closure_moment_symbol_census_2026-09-29.json`.

## Source-complete control note: Priority 165

The full semantic definitions and section-by-section map are maintained in
[`CMI_OpenAI_Full_Semantic_Crosswalk.md`](CMI_OpenAI_Full_Semantic_Crosswalk.md).

The force-smoothness adjudication is recorded in
[`priority_195_four_operation_force_smoothness_adjudication_2026-09-30.md`](../NavierStokesReview/src/audit/priority_195_four_operation_force_smoothness_adjudication_2026-09-30.md).
It preserves the mathematical importance of the five-moment repair while
recording that the manuscript describes additional residual-control operations.
The remaining gap is the final selected-field identification with the
manuscript's five observables, not a proved failure of the selected force.
That document is now the controlling reference for the whole Fefferman
specification and the whole OpenAI manuscript, rather than treating the
forced Alternative C wrapper as the whole claim.

The review's exact position is three-part. First, the Lean source contains a
real selected physical construction, correction-state data, residual-rate
derivation, smooth-force route, and a compiled proposition with the shape of
Fefferman Alternative C. Second, the manuscript makes its five-moment
matching and correction identities load-bearing for the stated construction.
Third, the audit has not located the final theorem that identifies the
completed selected Cartesian velocity, pressure, residual, and force with
every corresponding manuscript observable after the selected composition.
The omission establishes a paper-to-endpoint correspondence gap; it does not
by itself prove a selected numerical mismatch or a kernel contradiction.
Conversely, the compiled C-shaped proposition must not be reported as proof
that the entire manuscript and every connected CMI condition have been
formally verified.

Evidence and required source coverage:
`NavierStokesReview/evidence/priority_164_direct_cmi_alternative_c_proof_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_cycle_invariant_residual_jet_trace_2026-09-29.json`;
`NavierStokesReview/src/audit/priority_163_full_cmi_dependency_crosswalk_adjudication_2026-09-29.md`.

## Priority 164: positive adjudication of the formal forced branch

The review now records a direct zero-sorry proof of the formal forced CMI
Alternative (C) route. `NavierStokesR3.theorem_1_1` supplies the actual
candidate and its no-global-solution result; `comparator_of_breakdown` proves
the corresponding smooth decay conditions and transfers any hypothetical
global comparator solution back to the forbidden whole-space solution. The
fresh axiom report contains only `propext`, `Classical.choice`, and
`Quot.sound`.

This settles the formal CMI-shaped proposition positively. It does not settle
the broader claim that every load-bearing five-moment argument in the
manuscript has been identified with the selected endpoint field. That remains
an adverse fidelity question, not a reason to call Alternative (C) false.

Evidence: `NavierStokesReview/evidence/priority_164_direct_cmi_alternative_c_proof_2026-09-29.md`;
`NavierStokesReview/evidence/priority_164_direct_cmi_alternative_c_proof_2026-09-29.json`.

## Priority 164 source correction: invariant-backed force route

The source audit has now inspected `CorrectionStep.CycleAnalyticInvariant`
directly. The selected rate chain is not built from an unsupported empty
interface. The invariant contains actual representation, defect, zero-mass,
residual, smoothness, support, periodicity, and reconstruction obligations.
`CorrectionState.debt` records the three radial defects
\((P,J_\theta,J_z)\), while `masses` records two further zero-mass
constraints. These fields feed the finite residual rates and the subsequent
smooth-force construction.

This positive result does not close the paper correspondence. The inspected
invariant is a correction-state contract; it is not a final equality proving
that the completed selected Cartesian fields realise the manuscript's
\((M,I,J,S,C_p)\) after all sums, curl, localisation, periodisation, pressure,
and force operations. The review therefore rejects both extremes: it does not
call the residual route unsupported, and it does not credit the endpoint with
the paper's complete five-observable transport theorem without finding that
theorem.

Evidence: `NavierStokesReview/src/audit/priority_164_cycle_invariant_residual_jet_trace_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_cycle_invariant_residual_jet_trace_2026-09-29.json`.

## Priority 166: adjudication of the five-moment force-smoothness rebuttal

The supplied rebuttal correctly identifies a serious paper-to-endpoint
question, but its strongest mathematical claims are not supported by the
source record. The manuscript itself states that individual terms in the
momentum residual may diverge while their sum and all derivatives extend
smoothly through the singular time (`docs/navier-stokes openai.txt:108-113`).
It then attributes cancellation to a connected construction: oscillatory
pulse fluxes cancel the leading singular stress, further corrections remove
remaining singular errors, and the five radial moment equations are one of
the correction operations (`docs/navier-stokes openai.txt:118-123,287-293,711-735`).

Therefore the implication

\[
\|u(t)\|_{\infty}\to\infty
\quad\Longrightarrow\quad
\|\partial_tu\|_{\infty},\|(u\cdot\nabla)u\|_{\infty},
\|\Delta u\|_{\infty},\|\nabla p\|_{\infty}\to\infty
\]

is not established by velocity blow-up alone. A residual is a sum,
\(R=T_1+T_2+T_3+T_4\), and singular summands can cancel. The paper's
mathematical burden is to prove the cancellation and smooth extension, not to
infer termwise divergence from the norm of one summand. The extracted paper
does not support the stronger assertion that the five moments are the sole
cancellation route or that it states a Fredholm-adjoint-Laurent “if and only
if” theorem in the form asserted by the rebuttal.

The narrower endpoint objection remains valid. `ActualCandidateAssembly.Witness`
does not visibly export a theorem identifying the completed selected Cartesian
velocity, pressure, and force with every paper-level consequence of
\((M,I,J,S,C_p)\). That is a genuine correspondence gap. It is not a proof
that the selected force is nonsmooth or that the selected moments are
nonzero. The concrete route is not an empty `NativeBounds` assumption:
`actualStageEstimates` consumes physical data, `finite_residual_rates`
consumes the cycle invariant and residual data, and `CandidateFromLimits`
derives the smooth force from residual derivative limits. Evidence:
`NavierStokesReview/evidence/agent_log_rebuttal_adjudication_2026-09-29.md`.

## Priority 167: selected-field composition trace

The subsequent declaration-level trace confirms that the selected endpoint is
not an empty rate wrapper. Concrete stage data feed `StageEstimates`; the
schedule theorem derives vanishing joint residual jets; actual `potentialSum`
terms are locally finite `tsum`s; the mixed construction applies the Cartesian
curl, cutoff, periodisation, and time activation; and the force is obtained by
smooth residual extension. The trace still does not locate a theorem
identifying the completed selected Cartesian fields with the manuscript's
five cumulative observables `(M,I,J,S,C_p)`. This strengthens the bounded
`CTR-005` finding without changing it into a selected mismatch or a formal
refutation. Evidence:
`NavierStokesReview/src/audit/priority_167_selected_field_composition_trace_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_selected_field_composition_trace_2026-09-29.json`.

The resulting classification is exact:

| Question | Current record |
|---|---|
| Are the five moments load-bearing in the manuscript? | Yes, for matching, stress/pressure consequences, and correction compatibility. |
| Are they the only cancellation mechanism? | Not established; the manuscript explicitly describes pulse-flux and further correction mechanisms. |
| Does blow-up alone imply every residual summand diverges? | No. |
| Is the selected residual/force route a bare generic interface assumption? | No. Concrete cycle and residual-rate data feed it. |
| Does `Witness` expose the complete final five-observable correspondence? | Not located in the inspected endpoint. |
| Is a selected-field mismatch, nonsmooth force, or literal CMI failure proved? | No. |

The audit therefore retains `CTR-005` as **NOT ESTABLISHED AS COMPLETE
PAPER-TO-ENDPOINT CORRESPONDENCE**, while rejecting the rebuttal's stronger
claims as unsupported. This is an adverse audit of the advertised
correspondence, not a request that OpenAI repair its work and not a claim of
formal `False` without a direct selected-field theorem.

The adjacent Priority 162 review records the narrower correction-state
boundary: genuine `barMoment`/`FiveRows` identities exist for correction-state
fields, but the inspected declarations do not identify them with the final
activated Cartesian field. See
`NavierStokesReview/src/audit/priority_162_barmoment_correction_state_vs_selected_field_source_review_2026-09-29.md`.

## Priority 163: full CMI dependency crosswalk, not isolated Alternative (C)

This review must evaluate Fefferman's complete admissibility conditions,
OpenAI's complete construction, and the Lean endpoint as one connected claim.
It therefore rejects both shortcuts: the absence of a named final
`(M,I,J,S,C_p)` field in `Witness` is not by itself a proof that the selected
force is invalid, while compilation of a Fefferman-shaped existential
proposition is not by itself proof that the 165-page manuscript has been
transported into the selected endpoint.

The source record establishes that the manuscript uses the five reduced-profile
moments as load-bearing matching and correction data. It also establishes that
the selected Lean route derives force smoothness through concrete physical
data, residual rates, derivative recurrence, boundary limits, and smooth
extension. The current adverse finding is narrower and exact: the inspected
public endpoint does not expose the complete semantic identification between
those selected fields and every paper-level moment consequence. That is
**NOT ESTABLISHED** paper-to-endpoint correspondence.

The following claims are not currently established and must not be presented
as conclusions: that velocity blow-up forces every residual summand to diverge;
that the extracted manuscript states a sole-mechanism Fredholm/adjoint/Laurent
“if and only if” theorem; that `NativeBounds` are accepted from thin air; or
that the selected force is nonsmooth. The literal forced CMI-shaped route is
supported by the comparator declarations, subject to the recorded build
caveat. It remains a separate question from complete equivalence with the
paper's physical mechanism and Fefferman's forward-Cauchy interpretation.

The next required audit is the adverse selected-field trace through `tsum`,
curl, localisation, periodisation, pressure, force, support, and endpoint
limits. Escalation to **FORMALLY REFUTED** requires a direct selected mismatch,
an impossibility theorem, a false mandatory CMI premise, or a selected-path
`False`; it must not be inferred from an omitted tuple alone.

Evidence: `NavierStokesReview/src/audit/priority_163_full_cmi_dependency_crosswalk_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_full_cmi_dependency_crosswalk_2026-09-29.json`.
## Priority 169: declaration-level adjudication of the force-smoothness rebuttal

The latest source check rejects the rebuttal's stronger assertions while
retaining its central correspondence concern. The manuscript explicitly says
that individual residual terms may diverge while their sum and all derivatives
extend smoothly through the singular time. It also describes pulse-flux
cancellation, covariance correction, auxiliary-time inversion, further
correction, and five radial moment equations as distinct connected operations.
Therefore velocity blow-up does not imply divergence of every residual summand,
and the five moments are not the manuscript's sole cancellation route.

The Lean route is stronger than an unsupported generic rate assumption.
ActualCandidateAssembly.estimates consumes concrete physical data;
ActualCycleResidualBounds.finite_residual_rates consumes the actual cycle
invariant and physical fields; physical_vanishingJointJets derives endpoint
residual flatness; and CandidateFromLimits.force_smooth derives the smooth force
extension. The invariant contains genuine debt, mass, rank-row, pressure, and
radial-moment controls.

The adverse finding remains material. The inspected Witness endpoint does not
expose a theorem identifying the completed activated Cartesian field and force
construction with the manuscript's full (M,I,J,S,Cp) semantics after the
complete sum, curl, localisation, periodisation, pressure, and endpoint
operations. Thus CTR-005 remains NOT ESTABLISHED complete paper-to-endpoint
correspondence. This does not prove a selected mismatch, nonsmooth force,
literal CMI failure, or kernel False.

Evidence:
NavierStokesReview/src/audit/priority_169_declaration_level_invariant_force_adjudication_2026-09-29.md;
NavierStokesReview/evidence/source_tranche_priority_169_invariant_force_adjudication_2026-09-29.json.

## Source-adjudication update: connected CMI semantics (2026-09-29)

The review treats Fefferman's “physically reasonable” wording as a connected
mathematical acceptance class.  The periodic sentence introduces an alternative
branch whose conditions (8)--(11) remain mandatory once selected.  The current
Lean source also shows a real concrete chain from cycle physical data through
finite residual rates, vanishing joint jets, and `force_smooth`; the endpoint
must not be described as accepting empty `NativeBounds`.

The remaining adverse finding is `CTR-005`: the inspected endpoint does not yet
expose the theorem identifying the completed selected Cartesian construction
with every paper-level five-moment consequence after the full composition.
This is a paper-to-endpoint correspondence failure, not a proof that the
selected force is nonsmooth.  The source-backed distinction and the required
next bridge search are recorded in
`NavierStokesReview/src/audit/priority_168_fefferman_physical_admissibility_and_force_chain_2026-09-29.md`
and `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`.

## Source-adjudication update: connected endpoint status (2026-09-29)

The connected reading of Fefferman's specification is binding: “physically
reasonable” links the force/data conditions to the accepted global solution
class, while “may look” selects the periodic branch rather than waiving its
conditions. The selected Lean source also contains a concrete residual
flatness route from actual physical data and cycle invariants to a smooth
force and a comparison-based C-shaped existential proposition.

The review must therefore not claim that Alternative (C) is disproved solely
because the exported Witness lacks a named five-tuple. The precise adverse
finding is that the source has not established the manuscript's stronger
paper-to-endpoint claim: no selected-field theorem has been located
transporting (M,I,J,S,Cp) through the completed Cartesian construction and
force extension. A selected mismatch or impossibility theorem is still
required before declaring literal CMI failure.

Evidence:
NavierStokesReview/src/audit/priority_169_connected_cmi_endpoint_adjudication_2026-09-29.md;
NavierStokesReview/evidence/priority_169_connected_cmi_endpoint_adjudication_2026-09-29.json.

## Source-adjudication update: invariant-backed residual route (2026-09-29)

The latest rebuttal correctly treats the five-moment machinery as important,
but overstates the consequences of its endpoint omission. The manuscript
explicitly allows divergent residual summands whose total residual and all
derivatives cancel smoothly. It also describes pulse covariance, stress-cone
representation, wave and mean corrections, pressure corrections, cutoffs, and
radial-moment matching as a connected construction. The five moments are not
optional, but they are not the only operation in the residual argument.

The Lean selected route is concrete: actual cycle invariants and physical data
feed residual-rate bounds, which feed vanishing joint residual jets and the
smooth-force extension. Therefore it is inaccurate to call the selected force
smoothness an unlinked or empty `NativeBounds` assumption. The adverse finding
is more precise: no selected-field theorem has been located that identifies the
completed Cartesian velocity, pressure, and force with the manuscript's
((M,I,J,S,C_p)) observables. That sustains CTR-005 for the claim of complete
paper-to-endpoint verification, without proving a selected mismatch or literal
CMI failure.

Evidence:
NavierStokesReview/src/audit/priority_170_invariant_debt_to_force_trace_2026-09-29.md;
NavierStokesReview/evidence/priority_170_invariant_debt_to_force_trace_2026-09-29.json.

## P2 source-bound refinement: observable domain boundary

The selected endpoint is built from actual `potentialSum` terms, mixed
Cartesian curl/localisation, periodisation, and time activation. The source
therefore contains a genuine selected-field construction. The remaining
correspondence question is more exact than a search for a five-tuple field:
`DefectIncrementBounds.barMoment` consumes a lifted scalar pressure-stream
field and integrates its torus average, while `Witness` exports activated
Cartesian velocity, pressure, and force fields. A theorem must identify these
domains and transport the observable through the completed operator chain.

That theorem has not been located in the inspected source. This sustains
CTR-005 as a paper-to-endpoint correspondence gap, but it is not a proof of a
nonzero selected defect or of literal CMI failure.

Evidence:
`NavierStokesReview/src/audit/priority_171_selected_observable_type_boundary_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_171_selected_observable_type_boundary_2026-09-29.json`.

## Numerical diagnostic update: CUDA 3D curl/cutoff calculation

The tracked diagnostic was run on full three-dimensional Cartesian volumes,
with resolution, stream-scale, and axial-modulation sweeps and a plotted
report. The declared profile shows a stable integrated commutator defect under
refinement, while the independently computed finite-difference curl and
divergence errors decrease. This is a stronger numerical test of the
cutoff-gradient mechanism than a one-dimensional profile scan.

The result remains deliberately bounded in interpretation. It does not bind
the diagnostic stream to the selected Lean `ASum`/`BSum`/`PSum`, periodisation,
`torusAverage`, `barMoment`, or axis definitions, so it does not prove a
selected-field defect or literal CMI failure.

Evidence:
`NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.md`;
`NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.json`;
`NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.csv`;
`NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.png`.
## Connected CMI semantics: whole-space C is not a standalone slogan

The review treats Fefferman's prose as connected mathematical content. His
definition begins with a fluid model, specified unknowns, a given initial
datum, and a given externally applied force. “For physically reasonable
solutions” introduces the growth-at-infinity concern; “Hence” connects that
concern to the all-order data restrictions (4) and (5). “We accept ... only
if” makes (6) and (7) necessary for the accepted whole-space solution class.
“Alternatively” and “Thus” open a distinct periodic branch with (8) and (9),
whose accepted solutions must satisfy (10) and (11). “Retaining the heart of
the problem” therefore preserves the connected package when it introduces
alternatives (A)--(D).

Accordingly, the correct whole-space audit target is not only

\[
\exists u_0\,\exists f\;\neg\exists(p,u),
\]

but that existential statement together with the connected conditions
\((1),(2),(3),(4),(5),(6),(7)\) on
\(\mathbb{R}^{3}\times[0,\infty)\). The periodic alternative must be audited
separately with \((8),(9),(10),(11)\). The selected Lean path does contain a
concrete residual-limit/jet-recurrence force route and a global-comparator
contradiction, so the review must not call it an empty shell. The separate
remaining issue is that the inspected exported endpoint does not expose a
field-level theorem transporting the manuscript's five moments
\((M,I,J,S,C_p)\) through the completed selected Cartesian construction.

That supports **CTR-005: NOT ESTABLISHED as the manuscript's complete
paper-to-endpoint correspondence**. It does not, without a selected failed
condition, a concrete selected mismatch, an impossibility theorem, or a
contradiction, prove that the literal C-shaped proposition is false. The
source-preserving semantic network and all current boundaries are recorded in
`docs/navierstokes.txt:25-81` and
`NavierStokesReview/src/audit/priority_172_fefferman_semantic_network_2026-09-29.md`.

## Priority 173: connected CMI compliance versus manuscript fidelity

Fefferman's wording is a connected specification. “May look for spatially
periodic solutions” selects a separate branch and does not waive its data and
accepted-solution requirements. Whole-space C requires the connected package
`(1)--(7)`, not only an existential pair of symbols.

The selected Lean path has explicit smooth-force, force-decay, pre-singular
PDE, initial-data, energy, and comparator-exclusion components. The force
provenance objection remains material because Fefferman calls the force given
and externally applied while OpenAI discovers it from a chosen residual. But
the displayed C statement does not state a separate independence predicate, so
residual discovery alone does not prove literal C false when smoothness and
decay are established.

The manuscript's five-moment mechanism remains load-bearing, and complete
transport into the selected Cartesian endpoint remains `NOT ESTABLISHED
(CTR-005)`. This is a paper-to-endpoint fidelity finding, not a claim that the
selected concrete force is already nonsmooth or that literal C has already
been contradicted.

Evidence: `NavierStokesReview/src/audit/priority_173_fefferman_c_connected_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_173_fefferman_c_connected_adjudication_2026-09-29.json`.

The follow-on force-smoothness adjudication rejects the claim that velocity
blow-up forces every residual summand to diverge and rejects the claim that the
five radial equations are the manuscript's only cancellation mechanism. The
selected Lean route derives smooth forcing from actual residual recurrence and
locally uniform jet limits. The paper-specific selected-Cartesian transport of
`(M,I,J,S,C_p)` remains **NOT ESTABLISHED (CTR-005)**; no selected mismatch or
force nonsmoothness theorem has been proved.

Evidence: `NavierStokesReview/src/audit/priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.json`.

## Priority 175: declaration-level bridge-candidate classification

The seven lexical candidates emitted by the endpoint census have now been
inspected as declarations. They are rate estimates, local potential-germ
identities, axis-growth transfer, or schedule/vanishing-jet packaging. None
proves that the final activated Cartesian fields realise `(M,I,J,S,C_p)`.
This closes the candidate-name search without converting its negative result
into a selected mismatch, force singularity, or impossibility theorem.

Evidence: `NavierStokesReview/src/audit/priority_175_lexical_bridge_candidate_classification_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_175_lexical_bridge_candidate_classification_2026-09-29.json`.

## Priority 176: selected-field composition and observable domain

The selected route is source-bound through `tsum`, Cartesian curl, cutoff,
periodisation, direct-field addition, and time activation. This confirms a
genuine composed endpoint. The unresolved issue is narrower and exact:
`barMoment` is a pressure-stream radial integral, and the inspected source has
not identified it with the final activated Cartesian five-observable tuple.
This preserves CTR-005 without claiming a selected numerical defect.

Evidence: `NavierStokesReview/src/audit/priority_176_selected_field_composition_domain_trace_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_176_selected_field_composition_domain_trace_2026-09-29.json`.

## Priority 177: word-level CMI connection control

Fefferman's connective wording is part of the mathematical specification.
“Given” and “externally applied” describe the data/provenance role of the
force; “For physically reasonable solutions” introduces the accepted class;
“Hence” connects the growth concern to `(4),(5)`; and “only if” makes `(6),(7)`
necessary. “Alternatively” and “may look” select the periodic branch, while
“Thus”, “In place of”, and “We then accept” impose `(8),(9)` and `(10),(11)`
within that branch. “Retaining the heart of the problem” prevents the audit
from reducing C or D to an equation-only existential.

The formal endpoint has a real residual-limit, smooth-force, and comparator
route. The remaining publication-level issue is still the selected-field
transport of the manuscript's five-moment correction consequences into that
connected C/D target. The review therefore records **NOT ESTABLISHED
(CTR-005)** for complete paper-to-endpoint fidelity, without asserting a
selected mismatch, nonsmooth force, literal C/D failure, or kernel
contradiction.

Evidence:
`NavierStokesReview/src/audit/priority_177_fefferman_word_connection_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_177_fefferman_word_connection_adjudication_2026-09-29.json`.

## Priority 179: no isolated C reading

The review now treats Fefferman's CMI statement as a semantic dependency
network. “May look” is branch latitude, not a waiver. In the selected
periodic branch, “Thus”, “In place of”, and “We then accept” make `(8),(9)`
and `(10),(11)` binding. In the whole-space branch, “Hence” and “only if” bind
`(4),(5)` and `(6),(7)`. The phrases “physically reasonable” and “retaining
the heart of the problem” carry those conditions into the alternatives.

Accordingly, the review does not claim that a formal C-shaped route is enough
to establish the manuscript's full physical proof. It records the stronger
paper-to-endpoint requirement and keeps `CTR-005` at **NOT ESTABLISHED** until
the selected fields, force, pressure, and five-moment mechanism are connected
by a value-level theorem. It does not convert that missing correspondence
into an unsupported literal C/D refutation.

Source-complete record:
[`priority_179_fefferman_full_semantic_dependency_network_2026-09-29.md`](../NavierStokesReview/src/audit/priority_179_fefferman_full_semantic_dependency_network_2026-09-29.md).

## Priority 180: force-smoothness rebuttal control

The latest source check preserves the important adverse point that the
manuscript's five-moment equations are load-bearing. It rejects three stronger
claims not proved by the source: velocity blow-up does not imply termwise
divergence of every residual summand; the five equations are not shown to be
the manuscript's only cancellation operation; and `force_smooth` is not a
free-standing `NativeBounds` assumption on the selected path. The Lean route
derives smooth forcing from concrete residual recurrence and locally uniform
jet limits.

The paper-to-endpoint issue remains material and adverse: the inspected public
`Witness` does not identify the completed activated Cartesian fields with
`(M,I,J,S,C_p)`. The review therefore retains **NOT ESTABLISHED (CTR-005)**,
without claiming a selected nonzero defect, force nonsmoothness, impossibility,
literal C/D failure, or `False`.

## Connected CMI adjudication: the endpoint must not be over- or under-claimed

The source-controlled Fefferman reading is now applied to the complete
connected target. “For physically reasonable solutions” introduces the
accepted class; “Hence” links the spatial-growth concern to `(4),(5)`; and
“only if” makes `(6),(7)` necessary for accepted whole-space solutions.
“Alternatively ... may look for” selects the periodic branch without waiving
its conditions; “Thus”, “In place of”, and “We then accept” bind `(8),(9)` and
`(10),(11)` within that branch. “Such smooth, physically reasonable
solutions” and “retaining the heart of the problem” carry this network into
the alternatives.

The source trace also corrects the direction of the audit conclusion. The
Lean comparator does not merely match the outer existential syntax. Its
`InitialVelocityConditionDecay` encodes initial-data smoothness,
divergence-freeness, and all-order decay; `ForceConditionDecay` encodes force
smoothness and all-order space-time decay; and
`NavierStokesExistenceAndSmoothnessRn` encodes the PDE, incompressibility,
initial condition, global smoothness, square-integrability, and uniform energy
requirements for a competing global solution. The comparator theorem derives
the corresponding whole-space existential/nonexistence proposition.

Therefore the review must state both conclusions, without collapsing either:

1. **Operational C-shaped result:** the inspected Lean path provides the
   connected whole-space C-shaped proposition, subject to its recorded build
   and axiom status. This is not, by itself, full Fefferman
   physical/semantic compliance.
2. **Manuscript-fidelity result:** the inspected public endpoint does not yet
   identify the completed selected Cartesian fields, pressure, force, and
   residual with every manuscript-level consequence of the five-moment
   mechanism after the full sum, curl, localisation, periodisation, averaging,
   and packaging chain. The claim that Lean verifies the manuscript's exact
   five-moment proof is therefore **NOT ESTABLISHED (CTR-005)**.

The second conclusion is not a proof that the operational C-shaped proposition
is false. Conversely,
the first conclusion is not proof that the Lean route is the manuscript's
five-moment route. Fefferman's words “given” and “externally applied” preserve
a material physical-provenance objection, but the displayed C predicate does
not state a separate independence-from-trajectory axiom. The manuscript also
explicitly discusses defining the force from the residual and arranging smooth
cancellation of the total residual. A literal C refutation therefore requires
a failed connected premise, a concrete selected mismatch, an impossibility
theorem, or a contradiction, not merely the absence of the final moment
identity.

Evidence: `NavierStokesReview/src/audit/priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.json`;
`NavierStokes/ComparatorDefinitions.lean:124-238`;
`NavierStokes/ComparatorR3Theorem.lean:21-44`.

Evidence: `NavierStokesReview/src/audit/priority_179_latest_force_smoothness_rebuttal_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_179_latest_force_smoothness_rebuttal_2026-09-29.json`.

## Priority 180: selected-field boundary adjudication

The latest rebuttal correctly insists that the manuscript's five-moment
system is load-bearing. The review therefore does not describe
`(M,I,J,S,C_p)` as optional notation or as removable from the paper's
construction. It does, however, reject three stronger inferences that the
current source record does not prove: `||u||_∞ → ∞` does not imply that every
summand of the residual diverges; the manuscript does not establish that the
five equations are its only cancellation operation; and the Lean theorem
`force_smooth` is not a bare `NativeBounds` assumption.

The selected Lean path is substantive. Concrete residual recurrence,
vanishing joint jets, locally uniform endpoint limits, and the smooth force
extension provide a conditional chain of the form

\[
  H_{\mathrm{selected}} \Rightarrow J_{\mathrm{flat}}
  \Rightarrow F\in C^\infty,
  \qquad F=\mathcal R(u,p)\text{ for }0\leq t<1.
\]

The unresolved paper-to-endpoint obligation is different:

\[
  J_{\mathrm{flat}} \Rightarrow
  \operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}})
  =(M,I,J,S,C_p).
\]

The inspected `Witness` does not state that final selected-field identity.
Thus the current record establishes **NOT ESTABLISHED (CTR-005)** for the
claim that the exported endpoint machine-checks the manuscript's complete
five-moment mechanism. It does not yet establish a nonzero selected defect,
force nonsmoothness, an impossibility theorem, a literal C/D failure, or
`False`.

Evidence: `NavierStokesReview/src/audit/priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.json`.

## Priority 177: connected Fefferman specification

The CMI text is audited as a connected specification rather than as isolated
equation citations. Its wording binds given data, force provenance, whole-space
or periodic branch conditions, accepted smoothness and energy, and the
nonexistence target. This supports a stricter paper-level crosswalk while not
claiming that the selected C/D proposition has been formally falsified.

Evidence: `NavierStokesReview/src/audit/priority_177_fefferman_word_connection_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_177_fefferman_word_connection_adjudication_2026-09-29.json`.

## Global radial-integral gate in the selected-field audit

The selected mixed radial pullback is periodic on the inspected construction,
whereas `barMoment` integrates over the unbounded real radial variable. The
review therefore separates three statements that must not be conflated:

\[
\text{periodic}+\text{radially supported}\Rightarrow f=0,
\quad
\text{periodic}+\text{positive on }(0,1)\Rightarrow f\notin L^1(\mathbb R),
\quad
\neg L^1\Rightarrow \int_{\mathbb R}f=0\text{ by `integral_undef`}.
\]

The selected endpoint does not yet provide the required support,
integrability, positivity, or nonzero-value premise. Thus this is a real
semantic gate for the paper's radial observables, not a completed selected
defect. It strengthens `CTR-005` as a paper-to-endpoint correspondence
finding while leaving literal C/D failure unproved.

Evidence: `NavierStokesReview/src/audit/priority_181_global_barmoment_integrability_gate_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_181_global_barmoment_integrability_gate_2026-09-29.json`.
## Current semantic control: Fefferman's connected admissibility package

The review treats Fefferman's wording as a connected specification. “Given”
and “externally applied” describe the data and physical provenance side of the
forward problem; “physically reasonable” introduces the accepted class;
“Hence” links the spatial-growth concern to `(4),(5)`; and “only if” makes
`(6),(7)` necessary for accepted whole-space solutions. “Alternatively” and
“may look” select the periodic branch only. “Thus”, “In place of”, and “We
then accept” bind `(8),(9),(10),(11)` once that branch is selected. The phrase
“retaining the heart of the problem” carries this network into the four
alternatives.

Accordingly, the review does not claim that Fefferman asked only for `(1)--(3)`.
It also does not infer literal C/D failure from the absence of a named final
five-moment tuple. The inspected Lean route contains a substantive operational
C-shaped package, while the complete correspondence between the manuscript's
five-moment correction mechanism and the selected Cartesian endpoint remains
`NOT ESTABLISHED (CTR-005)`. A literal C/D failure requires a connected failed
condition, selected value mismatch, impossibility theorem, or contradiction.

Evidence: `NavierStokesReview/src/audit/priority_182_fefferman_semantic_word_to_condition_closure_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_182_fefferman_semantic_word_to_condition_closure_2026-09-29.json`.

The wording “may look for spatially periodic solutions” is a branch choice,
not a waiver. Once chosen, “Thus”, “In place of”, and “We then accept” bind
(8), (9), (10), and (11). The whole-space C route retains (4), (5), (6), and
(7). This is why a C-shaped theorem cannot be assessed by checking only the
Navier--Stokes equations and a blow-up limit.

The force language must be handled with the same precision. “Given,
externally applied” supplies physical provenance and forward-problem meaning,
but the displayed C/D quantifiers do not state an additional trajectory-
independence predicate. OpenAI's manuscript expressly uses residual-defined
forcing and makes smoothness of the total residual the analytic obligation.
Thus residual design is a material physical-provenance objection, but not by
itself a formal C/D counterexample. Conversely, a compiling C-shaped theorem
does not, without a selected-field correspondence argument, establish every
manuscript-level claim about the five-moment mechanism. The review reports
these as separate layers rather than treating either as a substitute for the
other.

## Priority 183: adjudication of the force-smoothness rebuttal

The latest rebuttal correctly rejects any attempt to treat the paper's five
moments as optional notation. The paper uses them in profile matching,
modulation repair, compatibility-defect correction, and preservation of the
exterior quantities. The rebuttal overreaches in three places, however.

First, `‖u(t)‖∞ → ∞` does not imply that each term in the residual diverges.
The manuscript's construction is explicitly designed so that singular pieces
can cancel in their sum. A termwise-divergence claim requires a separate
asymptotic calculation.

Secondly, the manuscript does not support the assertion that the five moments
are its only cancellation operation. Its residual construction also contains
wave-amplitude equations, covariance corrections, auxiliary-time inversion,
pressure reconstruction, cutoff commutators, nonlinear remainder estimates,
and repeated full-residual recomputation. The five moments are a load-bearing
solvability and matching mechanism, but they are not interchangeable with the
whole residual proof.

Thirdly, the selected Lean route does not derive `force_smooth` from an
unconnected `NativeBounds` premise. `CandidateFromLimits` consumes the actual
residual derivative recurrence and locally uniform endpoint limits, constructs
a smooth extension, and proves agreement with the activated residual before
the terminal time. Upstream concrete physical-data and residual-rate
constructions feed that route.

The adverse finding remains exact and material. The inspected export does not
yet contain an explicit theorem identifying the completed selected Cartesian
velocity, pressure, residual, and force with the manuscript's five observables
`(M,I,J,S,C_p)` after `tsum`, curl, localisation, periodisation, torus
averaging, and global radial integration. Thus the paper's complete
mechanism-to-endpoint correspondence is **NOT ESTABLISHED (CTR-005)**. This
does not itself prove that the selected force is nonsmooth, that the selected
moments are nonzero, or that Fefferman's literal C/D proposition is false.

The review therefore rejects both underclaiming and overclaiming: it does not
credit a green Lean build as proof of the manuscript's full physical argument,
and it does not convert an absent transport theorem into a selected-path
counterexample without the required value-level calculation.

Evidence:
`NavierStokesReview/src/audit/priority_183_force_smoothness_moment_rebuttal_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_183_force_smoothness_moment_rebuttal_adjudication_2026-09-29.json`.

## Priority 184: selected-path foundation audit

The latest source inspection rejects the claim that `force_smooth` is merely
an unlinked `NativeBounds` assumption. `ActualCandidateAssembly` constructs a
concrete `Witness`; the periodic assembly transports vanishing joint jets and
locally uniform residual limits; and `CandidateFromLimits.force_smooth` is
derived from those premises. The inspection found no explicit `axiom`,
`sorry`, or `admit` in the targeted selected-path modules. `noncomputable` and
`Classical.choice` are standard mechanisms for integrals, limits, infinite
sums, and extension selection.

That correction does not resolve `CTR-005`. The source still does not expose a
selected-field theorem identifying the completed Cartesian velocity, pressure,
or force with \((M,I,J,S,C_p)\) after the actual series, curl, localisation,
periodisation, torus-average, radial-integral, and integrability steps. Thus
the endpoint's smooth-force route and the paper's named five-observable
correspondence must be reported separately. A selected nonzero defect or CMI
failure has not been proved merely by the missing endpoint identity.

Evidence:
`NavierStokesReview/src/audit/priority_184_selected_path_foundation_audit_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_184_selected_path_foundation_audit_2026-09-29.json`.

## Priority 185: adjudication of the five-moment smoothness rebuttal

The manuscript's five moments are load-bearing and remain part of the adverse
review. The source check nevertheless rejects the rebuttal's stronger claims.
Velocity blow-up does not entail termwise divergence of every residual term,
because the manuscript explicitly arranges cancellation in the total
residual. The manuscript also describes several distinct residual operations,
so it does not establish that the five equations are the only cancellation
route. Finally, the selected Lean route does not obtain `force_smooth` from a
free-standing generic rate contract. It derives concrete residual rates from
the actual cycle invariant and physical data, obtains vanishing joint jets,
and then applies the smooth extension construction.

The unresolved issue is still decisive for the paper-to-code claim:

\[
J_{\rm flat}\Rightarrow
\operatorname{PaperMoments}(u_{\rm selected},p_{\rm selected})
=(M,I,J,S,C_p)
\]

has not been established after the selected infinite sum, curl, localisation,
periodisation, torus average, and global radial integral. The current record
therefore supports `CTR-005 = NOT ESTABLISHED` for complete manuscript
fidelity. It does not support a selected nonzero defect, nonsmooth force,
literal CMI failure, or `False` without the corresponding value-level theorem.

Evidence:
`NavierStokesReview/src/audit/priority_185_rebuttal_adjudication_2026-09-30.md`;
`NavierStokesReview/evidence/source_tranche_priority_185_rebuttal_adjudication_2026-09-30.json`.

## Priority 186: Fefferman's full semantic network is binding

The source-preserving semantic closure is recorded in
`NavierStokesReview/src/audit/priority_186_fefferman_full_word_connection_closure_2026-09-30.md`.
This review does not treat “may look for spatially periodic solutions” as a
waiver. It is branch latitude. “Thus, we assume” binds `(8),(9)`, “In place
of” replaces only the whole-space data controls `(4),(5)`, and “We then
accept” binds `(10),(11)`. “Physically reasonable” and “retaining the heart of
the problem” carry the connected global regularity and energy problem into the
alternatives.

Accordingly, the C/D audit is against the connected packages, not `(1)--(3)`
in isolation. The current record supports a substantive operational C-shaped
Lean route, but it does not establish that the route is the complete selected
physical construction described by the manuscript. That remains
`CTR-005 = NOT ESTABLISHED`. No literal C/D failure is inferred without a
selected failed condition, value mismatch, impossibility theorem, or
contradiction.
## Priority 187: adjudication of the jet-flatness circularity rebuttal

The five radial moments remain load-bearing in the manuscript's profile
matching, modulation restoration, stress propagation, and correction system.
The latest rebuttal is nevertheless too strong when it says that omission of
the final tuple makes the Lean force-smoothness proof circular. The selected
route constructs concrete physical data and residual-rate premises, derives a
schedule with vanishing joint residual jets, and proves smooth extension of
the residual-defined force. Thus the following implication is source-backed:

\[
H_{\rm selected}\Rightarrow J_{\rm flat}\Rightarrow F\in C^\infty.
\]

The missing implication is different:

\[
J_{\rm flat}\Rightarrow
\operatorname{PaperMoments}(u_{\rm selected},p_{\rm selected})
=(M,I,J,S,C_p).
\]

No inspected endpoint theorem supplies that completed selected Cartesian,
pressure, residual, and force identification after the sum, curl,
localisation, periodisation, averaging, radial integration, and global
admissibility steps. The paper-to-endpoint claim therefore remains **NOT
ESTABLISHED (CTR-005)**. This does not prove that the selected force is
nonsmooth or that the operational C-shaped proposition is false. Such a
promotion requires a selected mismatch, failed connected condition,
impossibility theorem, or contradiction.

The claim that velocity blow-up forces every residual summand to diverge is
also rejected: divergent summands can cancel in the total residual. The
manuscript lists several distinct residual-control operations, so the claim
that the five equations are its only cancellation mechanism is not established.

Evidence: `NavierStokesReview/src/audit/priority_187_circularity_adjudication_2026-09-30.md`.

## Priority 188: connected CMI compliance and the remaining correspondence gate

Fefferman's “may look for spatially periodic solutions” is a branch choice,
not a waiver. The connected C/D obligations include the relevant data decay or
periodicity, the Navier--Stokes equations, incompressibility, the initial
condition, global smoothness, and the whole-space energy or periodic accepted-
solution conditions. The comparator definitions and the inspected C/D theorem
encode that full formal package.

Accordingly, the review records a positive result for the repository's formal
connected forced C/D propositions. It does not reduce C or D to equations
`(1)--(3)`. Separately, the manuscript-to-selected-field correspondence for
the load-bearing five moments remains **NOT ESTABLISHED (CTR-005)** because no
inspected endpoint theorem identifies the completed selected Cartesian fields
with `(M,I,J,S,C_p)`. This is not itself a proof that C or D is false; that
stronger result requires a selected failed connected condition, mismatch,
impossibility theorem, or contradiction.

Controlling crosswalk: [`CMI_OpenAI_Full_Semantic_Crosswalk.md`](CMI_OpenAI_Full_Semantic_Crosswalk.md),
Priority 188.

## Priority 189: source correction on physical wording

The inspected OpenAI manuscript does not say that its forced construction
“would never occur in physical reality”. It presents a physical description,
defines the force as the momentum residual, and states that individual
residual terms may diverge while the total residual and all derivatives extend
smoothly through the singular time (docs/navier-stokes openai.txt:106-124).
The later passages describe pulses, corrections, localisation, summation, and
force extension (:252-321).

This correction does not turn Fefferman into an equation-only test. “May look
for spatially periodic solutions” selects the periodic branch; “Thus”, “In
place of”, “we then accept”, “physically reasonable”, and “retaining the heart
of the problem” connect the branch data and accepted-solution conditions.
The review therefore keeps the connected CMI package in scope while retaining
the precise status: the selected Cartesian five-moment transport remains
**NOT ESTABLISHED (CTR-005)**. No selected failed Fefferman condition or
literal C/D refutation has been proved by this source correction alone.

Evidence: [priority 189 source correction](../NavierStokesReview/src/audit/priority_189_openai_physical_wording_source_check_2026-09-30.md);
[source tranche](../NavierStokesReview/evidence/source_tranche_priority_189_openai_physical_wording_source_check_2026-09-30.json).
## Semantic scope of the CMI alternatives

Fefferman's specification must be read as a connected semantic package. The
sentence “we may look for spatially periodic solutions” permits selection of
the periodic branch. It does not waive the conditions that follow. “Thus, we
assume” binds periodic data conditions (8) and (9); “in place of” replaces the
whole-space decay controls (4) and (5), not the Navier--Stokes equation,
initial condition, smoothness, or accepted-solution conditions; and “we then
accept” binds (10) and (11). The phrases “physically reasonable” and
“retaining the heart of the problem” connect those clauses to the global
existence and smoothness question.

The full clause network is recorded in
[`priority_193_fefferman_semantic_branch_network_2026-09-30.md`](../NavierStokesReview/src/audit/priority_193_fefferman_semantic_branch_network_2026-09-30.md),
with machine-readable source evidence in
[`source_tranche_priority_193_fefferman_semantic_branch_network_2026-09-30.json`](../NavierStokesReview/evidence/source_tranche_priority_193_fefferman_semantic_branch_network_2026-09-30.json).

This changes the review standard in an important way. A claim that the
repository proves a CMI alternative must be checked against the connected
package: admissible data and force, the PDE, incompressibility, initial data,
global regularity, bounded energy or periodicity, and the global nonexistence
quantifier. The comparator source contains those formal components. That
positive result is distinct from the stronger paper-to-selected-field claim.

The OpenAI manuscript makes its own connected obligation explicit: it defines
the force from the total residual, acknowledges that individual residual terms
may be singular, and requires the total residual and all Cartesian derivatives
to extend smoothly through the singular time. Profile extension, five-moment
stress and pressure-tail cancellation, wave corrections, localisation,
summation, and flat residual estimates are therefore part of the manuscript's
claimed mechanism. The current audit has not located a theorem identifying
that complete mechanism with the selected Cartesian endpoint. That remains
`CTR-005: NOT ESTABLISHED`.

This finding is not a claim that Fefferman meant equations (1)--(3) only, and
it is not a claim that literal C or D has already been falsified. Literal
falsification requires a selected failed connected condition, a selected
value-level mismatch, an impossibility theorem, or a contradiction. The
semantic scope and the exact evidence boundary are controlled by
[`CMI_OpenAI_Full_Semantic_Crosswalk.md`](CMI_OpenAI_Full_Semantic_Crosswalk.md).
# Live control checkpoint: 2026-09-30 continuation

The latest connected source crosswalk is Priority 201:
`../NavierStokesReview/src/audit/priority_201_selected_closure_census_2026-09-30.md`.
It incorporates Priority 200's positive literal result and records the
current full closure census and compiled review-side candidate disposition.

This checkpoint supersedes any older header count or branch description in
this document. The active private review branch is
`review/cmi-first-navier-stokes-reconciled-2026-09-30` at the current scoped
review commit. The separate public review branch is
`review/cmi-first-navier-stokes-disposition-public-2026-09-30`; the remote
branch was verified after the latest scoped review push.

The current worktree inventory contains two intentional untracked rows: the
protected `NavierStokes/R3/TestPressure.lean` source and the local raw 366 MB
environment-closure JSON. The source is deliberately not staged or edited.
The accidental root `$null` diagnostic
was moved, without deletion, to the local ignored archive
`archive/$null_2026-09-30.txt`; its SHA-256 and disposition are recorded in
`archive/ARCHIVE_MANIFEST_2026-09-30.md`. The current inventory and matrix
are linked at:

- `../NavierStokesReview/evidence/untracked_content_inventory_2026-09-30.md`
- `../NavierStokesReview/evidence/untracked_consolidation_matrix_2026-09-30.md`
- `../NavierStokesReview/evidence/tree_reconciliation_current_2026-09-30.md`

The scientific control finding is unchanged and source-bounded: the upstream
moment/rank/curl/localisation/residual machinery is genuine and active; the
exported `Witness` does not repeat a named final equality identifying the
selected Cartesian fields with the reduced-profile tuple
`(M,I,J,S,Cp)`. That is `CTR-005: NOT ESTABLISHED` for complete
paper-to-selected-endpoint correspondence. It is not a proved nonzero
selected-field defect, impossibility theorem, force nonsmoothness theorem,
compiler-cheat finding, or `False`. Current adjudication links are:

- `../NavierStokesReview/src/audit/priority_198_latest_rebuttal_adjudication_2026-09-30.md`
- `../NavierStokesReview/src/audit/priority_193_fefferman_semantic_branch_network_2026-09-30.md`
- `../NavierStokesReview/evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md`

Older register counts and earlier branch names remain historical snapshots;
they are not live workspace state.
## Live audit result: Priority 201 closure census (2026-09-30)

The current full-source census and compiled candidate disposition are linked
at
`NavierStokesReview/src/audit/priority_201_selected_closure_census_2026-09-30.md`.
It confirms zero missing local imports in the 588-module selected closure and
finds no active production declaration that identifies the final selected
Cartesian fields with `(M,I,J,S,Cp)`. Two review-side `barMoment` identities
compile only with caller-supplied pullback data. This strengthens `CTR-005`
as a paper-to-endpoint correspondence finding, while not proving a selected
field defect or literal CMI failure.
## Live audit result: Priority 202 actual invariant trace (2026-09-30)

The latest positive source correction is recorded in
`../NavierStokesReview/src/audit/priority_202_actual_moment_invariant_trace_2026-09-30.md`.
The actual correction cycle carries two preserved mean-mass identities and
three residual-debt classes. The review therefore does not claim that the
selected path lacks moment machinery. The unresolved correspondence question

is whether those internal coordinates are explicitly identified with the
paper's `(M,I,J,S,Cp)` after the final Cartesian transformations and export.

### Priority 205 endpoint-census adjudication

The source-controlled result is documented in
../NavierStokesReview/evidence/source_tranche_priority_205_endpoint_census_and_completion_adjudication_2026-09-30.md.
The selected closure was searched and seven production candidates were read
manually. They provide real schedule, residual-rate, germ, and blow-up
statements. None provides the final selected Cartesian identification with the
paper's five observables. The review completion SelectedBarMomentInterface is
conditional on caller-supplied pullback data and is not evidence that the
selected witness transports those observables.

Accordingly, the review must state both sides together: the selected proof is
not an empty or disconnected Lean shell, and the complete paper-to-selected
field correspondence is still CTR-005: NOT ESTABLISHED. This does not prove a
nonzero selected defect, nonsmooth force, literal CMI failure, impossibility,
compiler cheat, or False.

## Current environment and whole-tree control checkpoint

The fresh Navier--Stokes environment closure was exported from the live
checkout with the pinned `leanprover/lean4:v4.34.0-rc2` toolchain. It records
30,919 declarations, 329,127 declaration edges, zero missing names, and zero
`sorryAx` nodes across the six selected Navier--Stokes roots. The raw 366 MB
graph is retained locally by SHA-256 rather than staged as a public artefact;
the summary is linked at
[`lean_environment_closure_ns_3d_2026-09-30_summary.md`](../NavierStokesReview/evidence/lean_environment_closure_ns_3d_2026-09-30_summary.md)
and the audit record is
[`priority_212_ns_environment_closure_2026-09-30.md`](../NavierStokesReview/src/audit/priority_212_ns_environment_closure_2026-09-30.md).

This closure removes the stale-environment qualification for the selected NS
roots. It does not prove the missing selected-field observable identity. The
whole-tree transport census and its manual candidate review remain the
controlling evidence for that question:
[`selected_transport_audit_2026-09-30_review_sources.md`](../NavierStokesReview/evidence/selected_transport_audit_2026-09-30_review_sources.md)
and
[`priority_211_selected_transport_whole_tree_2026-09-30.md`](../NavierStokesReview/src/audit/priority_211_selected_transport_whole_tree_2026-09-30.md).

The active disposition therefore remains `CTR-005: NOT ESTABLISHED` for
complete manuscript-to-selected-endpoint correspondence. No selected nonzero
moment defect, force nonsmoothness, literal CMI failure, impossibility
theorem, compiler escape, or `False` is claimed.
