# Selected-field correspondence in the OpenAI Navier–Stokes formalisation

## Priority 237: what the audit must now test

The review is not one claim about one interface. It separates three arrows:

\[
\text{Fefferman specification}\leftrightarrow\text{Lean comparator},
\qquad
\text{manuscript}\leftrightarrow\text{Lean construction},
\qquad
\text{Lean construction}\leftrightarrow\text{selected endpoint}.
\]

The current record positively traces the five-row/radial repair engine into
the selected production route; it does not support the obsolete claim that
the machinery was bypassed wholesale. It still lacks the completed selected
observable identity after Cartesian lifting, curl, localisation,
periodisation, summation, pressure/residual composition, and endpoint limits.
That remains `CTR-005: NOT ESTABLISHED`, not a proved mismatch.

The next adversarial work therefore reconstructs the CMI comparator
independently, checks class inclusion and quantifier order, freezes only
\((u^\circ,f)\), and tests whether the nonexistence proof remains valid without
privileged knowledge of how the residual force was designed. It also follows
force smoothness derivative-by-derivative, expands all selected product-rule
remainders, audits limits and infinite sums, checks uniform energy and
uniqueness against the weakest admissible competitor, and mutates comparator
conditions to identify the proof's real load-bearing assumptions.

This is an adversarial programme, not assistance to OpenAI. It also avoids
unsupported conclusions: backward force construction alone does not refute C,
public commit opacity does not prove an error, and compilation does not prove
whole-document CMI or manuscript correspondence.

## Priority 238: one comparator edge established; proof differential remains open

The review-side probe independently compiles the one-way adapter

\[
  \text{ComparatorSolution}(v,p,f)
  \Longrightarrow
  \text{R3 GlobalFiniteEnergySolution}(v,p,f).
\]

This is substantive positive evidence: it supports transferring R3 global
nonexistence into comparator nonexistence and is not merely a theorem-name
match. It does not establish reverse inclusion, equality of the solution
classes, complete connected Fefferman semantics, or the final selected
Cartesian/localised/periodised/summed identification with
\((M,I,J,S,C_p)\). The controlled paper disposition remains
`CTR-005: NOT ESTABLISHED` for complete manuscript-to-selected-endpoint
correspondence.

The audit now treats the September 8 and September 10 public objects as two
submissions. The next provenance task is to compute their proof-term closures,
identify their shared core, compare same-witness and fixed-force claims, and
classify added energy, force-regularity, integrability, pressure,
competitor-class, parameter-range, and paper-facing modules. The provenance
delta raises scrutiny; it does not itself prove error or concealment.

Evidence: `NavierStokesReview/src/probes/CMIComparatorClassInclusionProbe.lean`,
`NavierStokesReview/src/audit/priority_238_cmi_comparator_class_inclusion_2026-10-01.md`.

## Priority 239: two submissions, not one opaque current tree

The 8 September and 10 September public objects are treated as separate
formal submissions. The audit compares their declaration-level proof closures
and shared core, then tests whether later additions establish or only restate
same-witness identity, fixed force and initial data, candidate energy,
all-order force regularity, genuine integrability, pressure semantics, the
weakest competitor class, and the manuscript parameter range. This is a
provenance and semantic-differential programme, not an accusation of intent.
It does not replace the selected-field and five-observable transport audit.

Evidence: `NavierStokesReview/src/audit/priority_239_two_submission_semantic_differential_2026-10-01.md`.

## Priority 240: first source-backed A/B contract result

The first direct comparison of the two public source snapshots establishes a
specific strengthening in the later R3 contract. The 8 September
`R3CompactCandidate.Properties` record contains the candidate's local
smoothness, support, residual, incompressibility, initial-data, and blow-up
fields, but the inspected record has no explicit pre-singularity uniform
energy field and states force smoothness as `ContDiffOn` on the future domain.
The 10 September `R3.ProblemStatement.CandidateProperties` record explicitly
adds `UniformFiniteEnergy (Ico 0 1) u`, global `ContDiff` force regularity, and
compact positive-time force support.

Mathematically, this proves a contract difference, not the reason for the
difference. It does not show that the earlier route is false: the stronger
facts may have been derivable elsewhere or may be part of later paper-facing
aggregation. The review therefore keeps the required A/B proof-term and
witness-identity investigation open. This result also does not resolve the
selected-field equality

\[
\operatorname{Obs}_{\rm paper}(u_{\rm selected},p_{\rm selected},f_{\rm selected})
=(M,I,J,S,C_p).
\]

Evidence:
`NavierStokesReview/src/audit/priority_240_submission_ab_contract_findings_2026-10-01.md`.

## Priority 241: executed A/B declaration-closure measurement

The first executed measurement under the expanded provenance programme reads
the two public source objects directly. The source/import route closure is 579
modules for Submission A and 605 for Submission B, with 578 shared modules,
one A-only module, and 27 B-only modules. The B-only set is concentrated in
the later R3, periodic-paper, parabolic-scaling, force, energy, support, and
viscous-balance layers.

The current B Lean environment export was also queried separately. The four
headline root declaration-use closures contain 30,721, 30,771, 30,840, and
29,785 declarations respectively, with no `sorryAx` nodes in the recorded
closures. These are not interchangeable measurements: the A/B result is a
raw Git source/import census, while the B result follows elaborated
declaration-use edges. Neither is a proof-term semantic closure or a theorem
that the final selected field realises the manuscript observables.

This narrows the audit rather than resolving it. It confirms a large shared
construction base and a targeted B-only route expansion, but does not show
that A was false, that B repaired a known failure, or that the A and B witness
tuples are identical. The selected-field observable bridge remains

\[
\operatorname{Obs}_{\rm paper}(u_{\rm selected},p_{\rm selected},f_{\rm selected})
=(M,I,J,S,C_p),
\]

unestablished. The positive production finding also remains: the internal
five-row/radial repair engine is consumed and was not bypassed wholesale.

Evidence:
[`priority_241_ab_declaration_closure_and_semantic_seams_2026-10-01.md`](../NavierStokesReview/src/audit/priority_241_ab_declaration_closure_and_semantic_seams_2026-10-01.md),
[`priority_241_ab_declaration_closure_2026-10-01.json`](../NavierStokesReview/evidence/priority_241_ab_declaration_closure_2026-10-01.json),
and [`ab_declaration_closure.py`](../NavierStokesReview/src/audit/ab_declaration_closure.py).

## Current public-release provenance result: Priority 236 (2026-10-01)

The repository history is itself part of the audit evidence. The raw Git
objects `8937a8f4` (8 September) and `f9e8bc5` (10 September) both have the
commit message `.`. The measured diff is 188 files, with 25,143 insertions and
81 deletions. The C route changes from
`R3CompactCandidate.selected_compact_candidate` to
`NavierStokesR3.theorem_1_1`; the periodic route changes from
`ActualCandidateAssembly.selected_candidate` to
`PeriodicPaper.periodic_corollary`.

This does not prove that either route is false. It does prove that the later
formal object cannot be treated as a transparent continuation of the earlier
announcement route without declaration-level proof-term reconstruction. The
audit must determine which added modules change the witness, strengthen
hypotheses, close analytic obligations, or merely provide paper-facing
wrappers. Provenance opacity increases the required scrutiny; it is not by
itself evidence of concealment or mathematical error.

Evidence: [`priority_236_public_release_provenance_delta_2026-10-01.md`](../NavierStokesReview/src/audit/priority_236_public_release_provenance_delta_2026-10-01.md)
and its [`JSON record`](../NavierStokesReview/evidence/priority_236_public_release_provenance_delta_2026-10-01.json).

## Current dependency-graph and provenance control: Priority 235 (2026-10-01)

The wording “the packaging fact is not evidence that the repair engine was
bypassed” is now replaced by a positive source-backed finding. The engine was
not bypassed wholesale: `FiveRowRank` and its mass-preservation lemmas feed
the actual cycle invariant; the radial/state-moment hierarchy feeds physical
data and residual-rate estimates; those estimates feed flatness, force
extension, and the selected-witness route. This is evidence of internal
production use, not a concession based on silence.

The remaining issue is a different edge. The audit has not yet proved the
completed selected-field identity

\[
\operatorname{Obs}_{\rm paper}(u_{\rm selected},p_{\rm selected},f_{\rm selected})
=(M,I,J,S,C_p)
\]

after Cartesian lifting, curl, localisation, periodisation, finite summation,
`tsum`, pressure/residual composition, and the endpoint limits. Internal use
of the repair engine therefore cannot be substituted for verification of that
final arrow, and the missing arrow cannot be treated as a proved mismatch.

The audit method is being widened accordingly. It now requires a typed
proof-dependency hypergraph, an object-identity ledger, premise-direction and
vacuity audits, a limit/interchange register, pressure/energy/uniqueness and
convention checks, review-side mutation tests, and a semantic comparison of
the public September proof routes. The controlling rule is: **verify the
arrow, not merely its endpoints**.

Evidence: [`priority_235_dependency_graph_provenance_and_semantic_integrity_2026-10-01.md`](../NavierStokesReview/src/audit/priority_235_dependency_graph_provenance_and_semantic_integrity_2026-10-01.md)
and its [`JSON record`](../NavierStokesReview/evidence/priority_235_dependency_graph_provenance_and_semantic_integrity_2026-10-01.json).

## Current moment-hierarchy adjudication: Priority 233 (2026-10-01)

The audit has now checked the moment mathematics under its structural roles,
not only under the named profile tuple. `IntegratedMeanBalances` proves actual
radial integral, integration-by-parts, viscosity, pressure, parameter, and
torus-average identities. `StateMomentBalances` identifies correction-state
radial moments with averaged state fields and derives angular, axial, pressure,
and flux balances. `CorrectionInitialization` imports this machinery into the
actual primary construction. This is affirmative evidence of a connected
intermediate moment hierarchy, not merely imported vocabulary.

That finding strengthens, rather than removes, the unresolved endpoint issue.
The inspected production graph still does not contain the completed semantic
identification

\[
\operatorname{Obs}_{\mathrm{paper}}
(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
=(M,I,J,S,C_p)
\]

after the selected Cartesian potential/direct/pressure sums, curl and
localisation, periodisation, averaging, and the final limiting/support
operations. The evidence therefore supports two precise statements at once:
the repair and state-balance machinery is used; the complete paper-to-endpoint
observable correspondence remains `CTR-005: NOT ESTABLISHED`. It does not prove
wholesale bypass or a concrete mismatch.

Evidence:
[`priority_233_moment_hierarchy_semantic_boundary_2026-10-01.md`](../NavierStokesReview/src/audit/priority_233_moment_hierarchy_semantic_boundary_2026-10-01.md)
and its
[machine-readable record](../NavierStokesReview/evidence/priority_233_moment_hierarchy_semantic_boundary_2026-10-01.json).

## Current conditional radial-integral result: Priority 231 (2026-10-01)

The compiled review completion
[`SelectedMixedProductionBarMomentProductRule.lean`](../NavierStokesReview/src/completions/SelectedMixedProductionBarMomentProductRule.lean)
transports the exact three-term selected formula under the weighted radial
integral. Its pointwise composition hypothesis and integration-side
requirements remain explicit, so this result does not silently claim that the
exported endpoint supplies them. It strengthens the value-level audit while
leaving `CTR-005: NOT ESTABLISHED` unchanged.

## Current selected-field composition result: Priority 230 (2026-10-01)

The pinned review completion
[`SelectedMixedProductionFullProductRule.lean`](../NavierStokesReview/src/completions/SelectedMixedProductionFullProductRule.lean)
now composes the actual selected radial scalar into the cutoff-curl term,
the cutoff-gradient commutator, and the separately cut/periodised direct
branch. This is affirmative selected-field composition evidence.

It deliberately stops before assigning a value to the commutator or radial
integral. It therefore does not establish the manuscript's
`(M,I,J,S,C_p)` transport and does not prove a selected mismatch. The current
disposition remains `CTR-005: NOT ESTABLISHED`.

## Current declaration-level dependency ledger: Priority 229 (2026-10-01)

The declaration-level ledger
[`priority_229_manuscript_dependency_declaration_ledger_2026-10-01.md`](../NavierStokesReview/src/audit/priority_229_manuscript_dependency_declaration_ledger_2026-10-01.md)
records the exact production chain from five-row corrections and cycle
invariants to residual rates, flatness, force extension, and
`ActualCandidateAssembly.selected_witness`. This is affirmative evidence
that the repair engine is integrated internally. The stronger statement is now
source-checked in Priority 232: the actual rank-stage lemmas are consumed by
the cycle invariant and then by physical data, residual rates, stage estimates,
and the selected witness. Thus the repair engine was not bypassed wholesale.
This is a positive dependency finding, not a conclusion that the final
manuscript observables have already been transported.

The same ledger records the unresolved edge: no inspected consumed production
declaration identifies the completed selected Cartesian, localised,
periodised, summed, radially integrated, pressure-coupled, residual-defined
fields with the manuscript's `(M,I,J,S,C_p)` observables. The complete
paper-to-endpoint correspondence therefore remains `CTR-005: NOT
ESTABLISHED`. The ledger does not claim a nonzero defect or a false selected
identity.

The distinction is recorded in
[`priority_232_repair_engine_usage_and_observable_boundary_2026-10-01.md`](../NavierStokesReview/src/audit/priority_232_repair_engine_usage_and_observable_boundary_2026-10-01.md)
and its machine-readable evidence
[`priority_232_repair_engine_usage_and_observable_boundary_2026-10-01.json`](../NavierStokesReview/evidence/priority_232_repair_engine_usage_and_observable_boundary_2026-10-01.json):
internal repair use is established; the completed selected-field observable
identity is not established; a selected mismatch is also not established.

## Current coupled-dependency adjudication: Priority 228 (2026-10-01)

The new source adjudication is
[`priority_228_coupled_manuscript_lean_dependency_adjudication_2026-10-01.md`](../NavierStokesReview/src/audit/priority_228_coupled_manuscript_lean_dependency_adjudication_2026-10-01.md),
with evidence in
[`priority_228_coupled_manuscript_lean_dependency_adjudication_2026-10-01.md`](../NavierStokesReview/evidence/priority_228_coupled_manuscript_lean_dependency_adjudication_2026-10-01.md).

It resolves the wording problem in the earlier verdict. The repository does
not merely contain moment code that happens to be reachable: the actual
five-row/rank corrections are consumed by the actual cycle invariant, and the
invariant is consumed by the residual-rate, stage-estimate, flatness, force,
and selected-witness route. The repair engine was therefore **not bypassed
wholesale**.

That positive result is not the same as a completed paper-to-endpoint bridge.
The inspected production source still does not provide a theorem identifying
the internal invariant with the manuscript's named
\((M,I,J,S,C_p)\) observables after the selected Cartesian,
curl/localisation, periodisation, radial, pressure, residual, and force
composition. The correct status is therefore **partially integrated; endpoint
semantic correspondence unresolved**. `CTR-005: NOT ESTABLISHED` remains the
controlled disposition for the complete manuscript claim. This is not a claim
of a nonzero selected defect, force nonsmoothness, literal CMI failure,
compiler escape, or `False`.

## Current selected-support correction: Priority 227 (2026-10-01)

The selected periodic-support gate replay is
[`priority_227_selected_periodic_support_gate_replay_2026-10-01.md`](../NavierStokesReview/src/audit/priority_227_selected_periodic_support_gate_replay_2026-10-01.md),
with evidence in
[`selected_periodic_support_gate_replay_2026-10-01.md`](../NavierStokesReview/evidence/selected_periodic_support_gate_replay_2026-10-01.md).
It verifies a conditional contradiction for the exact selected periodic radial
pullback. It does not transfer compact R3 support to the periodised field and
does not yet prove a nonzero value for the exact pullback. The scientific
disposition remains `CTR-005: NOT ESTABLISHED`.

## Current release correction: Priority 226 (2026-10-01)

The verified private/public release state is
[`priority_226_release_state_2026-10-01.md`](../NavierStokesReview/src/audit/priority_226_release_state_2026-10-01.md).
It is a dated release snapshot; the scientific disposition is unchanged.

## Current evidence correction: Priority 225 (2026-10-01)

The latest selected-field gate is
[`selected_mixed_barmoment_shell_gate_2026-10-01.md`](../NavierStokesReview/evidence/selected_mixed_barmoment_shell_gate_2026-10-01.md).
It proves finite-prefix and conditional `barMoment` branch facts, but leaves
the final selected support/integrability hypotheses explicit. It does not
change the active disposition: `CTR-005: NOT ESTABLISHED`.

## Current control correction: Priority 224 (2026-10-01)

The current corpus re-grounding is
[`priority_224_workspace_corpus_regrounding_2026-10-01.md`](../NavierStokesReview/src/audit/priority_224_workspace_corpus_regrounding_2026-10-01.md).
It supersedes older navigation pointers only. The latest selected-path source
records are Priorities 218, 221, and 223. The active disposition remains
`CTR-005: NOT ESTABLISHED`: the selected route is substantive, but complete
manuscript-to-selected-field identification of `(M,I,J,S,C_p)` is not located.

## Current control correction: Priority 214 (2026-09-30)

The current bookkeeping evidence is
`../NavierStokesReview/evidence/tree_reconciliation_current_2026-09-30.md`.
It records 49 tree entries, 47 file entries, 3,466 checkout files, 47 explicit
tree-relative resolutions, 0 missing entries, and 0 ambiguities. The
older reconciliation report remains historical evidence. The live private
checkout intentionally retains two untracked rows: protected OpenAI source
`NavierStokes/R3/TestPressure.lean` and the local raw environment-closure JSON.
Neither is staged or edited. This bookkeeping correction leaves the scientific
status at `CTR-005: NOT ESTABLISHED`.

## Document control and current evidence

This reader-facing paper is controlled by
[`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md) and
[`DOCUMENTATION_RECONCILIATION_2026-09-30.md`](DOCUMENTATION_RECONCILIATION_2026-09-30.md).
The current evidence boundary is recorded in the Priority 186–204 source
reviews under `NavierStokesReview/src/audit/` and their matching JSON records
under `NavierStokesReview/evidence/`. The paper is not a chronological log and
must not be updated from a historical register count. Priority 204 is scope
control only and does not change the scientific disposition. Its 29-row
disposition ledger is historical review-artifact state, not a claim that 29
files are currently untracked. The current Git state has two intentional
untracked rows, as recorded in document control: the protected author-side
source file and the local generated 366 MB environment-closure JSON excluded
from the public release.

Priority 209 is now the current scope and index authority. It records 2,797
current Lean files, 588 modules in the selected endpoint closure, 2,209 rows
outside that closure, 817 files under `NavierStokes/`, and 137 review-side
Lean files. Earlier register counts remain historical evidence. The current
scientific finding remains `CTR-005: NOT ESTABLISHED`.

The latest cross-file trace confirms that the actual cycle carries two
preserved mean-mass identities and three residual-debt classes which feed the
physical-data, residual-rate, force-extension, and blow-up route. The remaining
`CTR-005` question is whether a production theorem identifies that internal
invariant with the manuscript's named `(M,I,J,S,C_p)` observables after the
final Cartesian, periodic, localised, summed, radial, and force transformations.
Evidence: `NavierStokesReview/src/audit/priority_203_internal_to_endpoint_crossfile_trace_2026-09-30.md`.

**Independent source-level review and formal audit**
**Jexposition, 26 September 2026**

## How to read this document

This file contains a research paper followed by its preserved source-audit
dossier. The paper is the argument; the dossier is the provenance record. The
dossier is retained in full so that a mathematician can inspect the source
declarations, theorem signatures, endpoint traces, counter-probes, and later
corrections without treating a chronological work log as the paper's logical
order.

### Companion review and control documents

- [Companion peer review](OpenAI_NavierStokes_Peer_Review_v1.md)
- [CMI first-review plan](OpenAI_NavierStokes_CMI_First_Review_Plan.md)
- [Workspace goal and control rules](REVIEW_AUDIT_WORKSPACE_GOAL.md)
- [Semantic correspondence map](SEMANTIC_CORRESPONDENCE_MAP.md)

### Main manuscript route

Read the following sections in order for the publication-level argument:

1. [Executive verdict](#executive-verdict)
2. [Abstract](#abstract)
3. [Review question and standard](#1-review-question-and-standard)
4. [Source and method](#2-source-and-method)
5. [What the formal endpoint does establish](#3-what-the-formal-endpoint-does-establish)
6. [Force construction and the smoothness attack](#4-force-construction-and-the-smoothness-attack)
7. [The five-moment correspondence objection](#6-the-five-moment-correspondence-objection)
8. [Pressure and localisation](#7-pressure-and-localisation)
9. [External-force causality](#10-external-force-causality)
10. [Verdict](#11-verdict)
11. [References and evidence](#references-and-evidence)
12. [Technical appendices](#appendix-a-technical-findings-supporting-the-verdict)

The detailed material after the appendices is explicitly labelled [Evidence
dossier](#evidence-dossier). It supports, qualifies, or records revisions to
the main argument; it is not a second chronological manuscript and it does not
silently change the verdict.

### Claim-status discipline

The paper preserves the following distinctions throughout:

| Layer | Established by the current record | Not established by the current record |
|---|---|---|
| CMI wording | The forced alternatives are existential mathematical targets, with Fefferman's forward Cauchy framing as part of their interpretation. | A provenance objection alone is not a kernel-level contradiction of an existential proposition. |
| Lean endpoint | The inspected endpoint has a substantial forced candidate, comparison machinery, and standard foundational dependencies. | Kernel checking alone does not prove that the endpoint is the paper's advertised construction. |
| Upstream mechanism | Genuine reduced-profile, rank, moment, curl, localisation, pressure, and energy results occur in the source tree. | Reachability or local certificates do not by themselves prove final selected-field transport. |
| Selected-field correspondence | Raw source tracing now establishes an active profile-moment/rank-repair → coefficient-matching → finite-Cartesian-residual → selected-physical-data chain. The paper's five quantities are used as reduced-profile invariants and their consequences feed the construction. | The public `Witness` does not re-export a named five-tuple certificate, and the audit has not yet established that every paper-level narrative assertion is semantically identical to the CMI endpoint. Tuple absence is not, by itself, a failed proof or a refutation. |
| Force and pressure semantics | Residual provenance and absolute-pressure representation are material semantic audit questions. | Neither is promoted to an unconditional formal refutation without a direct theorem establishing that stronger claim. |

This is a source-grounded audit, not a compiler-status report. Numerical
experiments, plots, and interface countermodels are used as diagnostics and
never substituted for a theorem about the concrete selected field.

### Current source adjudication (2026-09-29)

The earlier formulation of CTR-005 as “the five-moment restoration is missing
from the selected proof” is withdrawn. Direct inspection of the raw Lean chain
shows that the reduced-profile moment and rank machinery is consumed in
coefficient matching, that the resulting `BaseResidual.FiniteIdentities` feed
the residual and all-order-flatness estimates, and that those estimates enter
the selected physical-data and candidate construction. The separate
axis-asymptotic proof of velocity growth is only one conjunct; it does not
show that the repair chain is dispensable from the full candidate.

The remaining question is narrower and must be tested against the exact CMI
and paper statements: whether every advertised consequence has the required
scope for the final selected fields, pressure, force, support, and global
interpretation. The current record contains no proved nonzero moment defect,
impossibility theorem, or kernel-level `False`.

The 2026-09-30 endpoint axiom replay is recorded in
[`selected_endpoint_compile_boundary_reaudit_2026-09-29.md`](../NavierStokesReview/evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md).
It reports only `propext`, `Classical.choice`, and `Quot.sound` for the
queried endpoints. That narrows the axiom-integrity question; it does not
close the separate selected-field moment correspondence.


## Executive verdict

OpenAI's published claim is **not yet established as an exact CMI/paper
correspondence**, but the reason must be stated correctly. The repository
contains a substantial Lean endpoint with a forced whole-space breakdown
proposition, and the inspected endpoint has standard foundational axiom
dependencies. Raw source tracing also shows that the five-moment and rank
repair machinery is used internally to obtain coefficient matching, finite
Cartesian residual identities, residual estimates, selected physical data,
and candidate properties.

The remaining issue is not that the repair engine is absent or wholly
bypassed. The exported
`selected_witness` does not expose a separate named theorem identifying the
paper's five cumulative quantities

$$
(M,I,J,S,C_p)
$$

with the final Cartesian velocity, pressure, residual, and force used by the
whole-space endpoint. The source positively shows internal integration of the
repair engine into residual estimates and candidate data, but the final
semantic identification remains unlocated. This is therefore a
correspondence question at the selected-field boundary, not a claim that the
engine was bypassed or that the selected field is wrong. It is adverse to the
advertised complete paper-to-code claim because the manuscript's downstream
five-observable conclusions have not been shown to apply to the exported
fields.
It is distinct from a kernel-level refutation: the review has not proved
`False` from the selected endpoint and does not describe the literal
existential C/D proposition as formally refuted.

This omission matters because the paper does not use the five quantities as
decorative profile labels. It uses their matching to preserve the heat
exterior, remove integrated pressure and stress tails, restore the profiles
after modulation, and close the later five-equation correction cycle. The
formal record therefore fails to establish the downstream conclusions for the
exported fields, while still falling short of a proof that those conclusions
are mathematically false.

## Abstract

OpenAI presents its paper and public announcement as a solution of the
Navier–Stokes existence and smoothness problem by claiming the forced
alternatives in Charles Fefferman's Clay Mathematics Institute formulation.
This paper audits that claim at three levels: Lean-kernel validity, the exact
proposition exported by the repository, and semantic correspondence between
that proposition and the construction described in the paper.

The source contains genuine five-coordinate repair mathematics, a selected
forced candidate, whole-space comparison infrastructure, and standard-axiom
dependency reports for the inspected endpoint. The adverse result is more
specific than a compiler objection: the final witness does not expose a
field-level transport theorem carrying the paper's named moments
\((M,I,J,S,C_p)\) through the selected Cartesian fields, residual estimates,
pressure recovery, force extension, and final C/D consequences. Zero-sorry
review probes establish interface non-implication, not emptiness of the
selected witness; the missing result is a concrete selected-path composition
theorem.

The publication-level verdict therefore remains **not yet established as an
exact CMI solution**, but not because raw source shows that the moment/rank
engine is missing. The inspected R³ theorem exports a literal C/D-shaped
proposition and the selected construction uses substantial upstream analytic
machinery. The remaining task is to compare the proposition and its proved
consequences with every load-bearing claim in the paper and with Fefferman's
CMI conditions.

The review also separates objections that do not presently refute the claim.
Residual-defined forcing is a provenance concern, but the formal C/D predicate
contains no independence axiom. The exact Newtonian energy identity and
solenoidal assembly remove broad energy-mismatch and raw-stage-divergence
objections. Compact pressure support alone does not imply pressure or velocity
triviality. The off-axis chart and on-axis limit are both represented, but
their complete transport into the final radial moment remains unproved.

The phrase **not formally refuted** reports only that the review has not yet
derived `False` from the selected Lean endpoint. A formal refutation would
require a zero-sorry contradiction on the selected dependency path or a false
mandatory premise proved for the selected fields. That stronger result remains
a separate research target, and its absence is not affirmative evidence for
the published claim.

### CMI wording and the residual-construction nuance

The official Fefferman statement describes \(f_i(x,t)\) as the components of a
given, externally applied force and imposes global smoothness, spatial decay
or periodicity, and energy conditions on the relevant alternatives. That
language supplies the physical interpretation of the data, but Alternatives
(C) and (D) are existential mathematical propositions. They do not introduce
a formal independence predicate saying that a term called \(f\) may not have
been designed from a selected solution.

This matters because OpenAI's own Navier--Stokes paper explicitly uses the
residual-design route: it chooses a flow and pressure, defines the momentum
residual as the force before the singular time, and makes smooth cancellation
of that residual the central construction problem. Consequently, the review
does not claim that residual-defined forcing is automatically forbidden by the
literal CMI quantifier. The correct audit conclusion is more exact: the
current record does not establish that the selected Lean field is the field
described by the paper, with the five cumulative moments, stage corrections,
pressure construction, localisation, all-order residual cancellation, and
whole-space obstruction transported into the exported witness. This is a
reason to reject the advertised proof claim on the present record, not a
request for OpenAI to repair it. The active research task is to falsify the
construction where possible or independently complete the missing calculation
without treating the claim as provisionally valid.

The same distinction applies to the companion Euler paper. Its parent--child
construction asserts exact smooth stage solutions and a stability-based limit.
Nested time intervals alone do not establish a temporal kink or a Zeno failure;
those must be proved from the actual Lean stage-matching and summability
identities. The source-grounded wording and page-level crosswalk are recorded
in `NavierStokesReview/evidence/paper_nuance_crosswalk_2026-09-27.md`.

### Source-to-claim correspondence map

The accompanying [`SEMANTIC_CORRESPONDENCE_MAP.md`](SEMANTIC_CORRESPONDENCE_MAP.md)
is part of the evidence presentation, not a build-status appendix. It maps the
paper's base profile, pulse/correction mechanism, five moments, pressure,
residual force, localisation, and R3 packaging to the declarations that
construct them. It also states the exact transport obligations required before
the Lean endpoint can be identified with the paper's advertised construction.
The key distinction is between a theorem about an individual stage or finite
prefix and a theorem about the final selected Cartesian field after the actual
`tsum`, curl-cutoff commutator, torus averaging, radial integration, pressure
assembly, and whole-space packaging. The former is positive source evidence;
the latter is the load-bearing correspondence question under CTR-005.

### Burden of proof for the advertised solution

The burden in this review is set by OpenAI's own public claim: the repository
and paper are presented as a solution of the Navier–Stokes problem, not merely
as a collection of compiling experiments or a proposal for future work. The
relevant affirmative proposition is therefore that one selected construction
simultaneously satisfies

$$
\text{equations} + \text{regularity} + \text{force conditions}
  + \text{energy bound} + \text{finite-time breakdown},
$$

and that the construction described in the paper is the construction exported
by the theorem. A repository-wide collection of supporting modules cannot
carry that burden if the final witness does not identify the paper's
load-bearing objects with the selected fields.

Accordingly, the exact CMI/paper correspondence remains not independently
established on the inspected record. This is not because the raw source lacks
the moment/rank engine: the selected construction uses it through coefficient
matching, finite residual identities, residual estimates, and candidate-data
theorems. The remaining question is whether every paper consequence and CMI
condition has the same scope for the final selected fields. A zero-sorry
`False`, a proved selected-field mismatch, or an impossibility theorem would be
a stronger refutation; none has been obtained here. The distinction is
deliberate: absence of a formal refutation is not positive evidence for the
published claim, but tuple omission is not a refutation either.

This is not a review of an optional implementation detail. OpenAI's public
announcement presents the work as a solution of the Navier–Stokes existence
and smoothness problem and expressly says that it establishes alternatives
(C) and (D). The paper's Theorem 1.1 makes the same affirmative claim by
asserting existence of the force and fields, bounded kinetic energy, finite-time
velocity blow-up, and the resulting nonexistence conclusion. The adverse
finding in this paper therefore addresses the claim OpenAI actually published:
the inspected record does not establish that the selected endpoint is the
five-moment Navier–Stokes construction used to support that solution claim.

## Formal obligations and independent analytical context

The remaining correspondence audit is a set of exact selected-path scope tests,
not a presumption that one named theorem is absent.
For the actual exported fields (u,p,f), let

$$
\mathcal M(u,p,f)=(M(u),I(u),J(u),S(u,p,f),C_p(u,p,f)).
$$

The paper's mechanism requires a theorem of the following form, with every
map and domain instantiated rather than left as an interface parameter:

$$
\begin{aligned}
&\mathcal M(u,p,f)(t)=\operatorname{promoteDebt}(d_t),\\
&\operatorname{promoteDebt}(P,J_\theta,J_z)
   =(0,0,-P,-J_\theta,-J_z),\\
&\text{and these equalities are transported through}\quad
\texttt{StateRealization.chartIdentity},\ \texttt{CandidateProperties},\
\text{and the exported }\texttt{selected\_witness}.
\end{aligned}
$$

The inspected source proves substantial upstream algebra, selected stage
invariants, finite residual identities, and candidate consequences. It does
not expose the following stronger observables as one named final-field tuple,
so the remaining audit is about scope and composition rather than an assumed
omission of the underlying mechanism:

| Obligation | Required selected theorem | Current classification |
|---|---|---|
| Five-moment correspondence | Check the exact scope of the profile invariants, finite residual identity, selected fields, and paper consequences | Active semantic crosswalk; tuple absence alone is not CTR-005 refutation |
| Absolute pressure semantics | Establish the selected global Poisson/Leray representative, not only pressure differences | Open comparative audit; not a compact-support contradiction |
| Chart scope | Transport the (r>0) chart identity to the axis limit used by `origin_blowup` | Local identities proved; complete composition open |
| Field-level calculation | Evaluate the actual curl/localisation, torus average, `barMoment`, and infinite `tsum` | Open; CALC-26--36 are partial completions |
| Force provenance | Formalise any stronger independence or forward-data admissibility predicate before using it as a disproof | Provenance objection only; CTR-012 |
| Admission scope | Separate repository-wide `sorry` metadata from the selected endpoint's axiom report | Four challenge-file admissions are outside the inspected endpoint |

This formulation prevents a type-level countermodel from being mistaken for a
counterexample to the concrete selected field. Conversely, it prevents the
existence of upstream modules from being treated as proof that their invariants
reach the exported endpoint.

Independent analytical context is relevant but not dispositive. Constantin,
Ignatova, and Vicol study real-analytic forcing under anisotropic Type II
bounds and exact axisymmetry in the collapsing core. They prove regularity at
the putative singular point in that analytic class and derive that a force
with the OpenAI-type properties, if bounded in local (C^2) up to the
singular time, cannot be real analytic or vanish identically near the point.
This is consistent with a smooth, cutoff-based non-analytic force. It does
not refute the literal smooth-forced C/D alternative, but it places the
construction in a narrow non-analytic forced class. The paper is available at
[arXiv:2609.20803](https://arxiv.org/abs/2609.20803).

## A selected-path obstruction to residual cancellation

The force objection can be made precise without assuming that velocity blow-up
automatically implies force blow-up. The selected witness supplies an interior
identity

$$
\mathcal R(u,p)(t,x)=f(t,x),\qquad 0<t<1,
$$

and the selected schedule supplies unbounded mixed velocity at the origin. The
new zero-sorry probe also proves that the corresponding selected mixed
residual tends to zero at that endpoint. Independently, the candidate
interface identifies its interior Navier–Stokes residual with the force. The
probe proves that these facts contradict any selected-field estimate

$$
c\lVert u(t,0)\rVert\leq\lVert\mathcal R(u,p)(t,0)\rVert
$$

with fixed $c>0$, provided the force is locally bounded near $1$. This is the
correct mathematical target for the force-smoothness attack.

The selected raw residual actually falsifies the proposed lower-bound premise:
its norm tends to zero while the origin speed diverges. A second zero-sorry
probe now composes that result with the final selected force. Late-time
activation is removed, the periodic and original residuals agree at the
origin, and the selected force therefore satisfies

$$
\lVert f(t,0)\rVert\longrightarrow0\qquad(t\to1^-).
$$

This is a formal certificate of residual cancellation, not a proof of force
singularity. It closes the force-explosion route and moves the live audit to
the exact selected-field/CMI semantic crosswalk, including pressure
representation and any paper consequence not proved for the selected fields.
It does not establish that the moment engine is missing.

## 1. Review question and standard

The audit asks three different questions.

1. Does Lean check the proposition written in the theorem declaration?
2. Does the declared proposition encode a valid Navier–Stokes construction?
3. Does that construction match the paper and one of Fefferman's stated CMI
   alternatives?

The first question is answered by kernel checking. The second and third
require inspection of definitions, hypotheses, interfaces, and the
mathematical transport between modules. Compilation alone cannot answer them.

The forced C/D alternatives permit a smooth external force. Therefore the
following proposed conditions are not CMI disproof criteria without extra
hypotheses:

$$
\int_{\mathbb R^3} f(x,t)\,dx=0,
\qquad
\nabla\cdot f=0.
$$

An external body force is not an internal Newtonian stress, and incompressibility
constrains $u$, not automatically $f$. These are physical-provenance tests,
not consequences of the written forced alternatives.

## 2. Source and method

The primary source is the review fork of the public
`NavierStokesAndEuler` development. The upstream source tree is not modified.
All review code is under `NavierStokesReview/src/probes`, and all conclusions
below are tied either to source declarations or to zero-sorry Lean probes.

The audit followed the selected path:

$$
\texttt{ActualCandidateAssembly.selected\_witness}
\to
\texttt{GermCandidateAssembly}
\to
\texttt{CandidateFromLimits}
\to
\texttt{R3CompactCandidate}
\to
\texttt{R3/Theorem}.
$$

The active document map is controlled by
[`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md). The evidence
directory contains the compiler outputs and source ledgers; this paper states
the mathematical conclusions rather than reproducing the audit log.

## 3. What the formal endpoint does establish

`NavierStokes/R3/ProblemStatement.lean` requires, among other properties,
pre-singular smooth velocity and pressure, incompressibility, an explicit
Newtonian residual equation, compact support conditions, zero initial velocity,
and unbounded speed as $t\to1^-$. The comparator theorem then rules out a
global finite-energy solution with the same force under the recorded
comparison hypotheses.

The selected dependency reports for `selected_witness`, the R3 theorem, the
actual physical data, and the residual rate theorem contain only Lean's
standard foundational axioms:

$$
\texttt{propext},\qquad \texttt{Classical.choice},\qquad \texttt{Quot.sound}.
$$

This is positive evidence about kernel provenance. It does not certify that
every analytic premise has the intended physical meaning.

The repository-wide statement that every file is admitted-free is false: the
standalone `ComparatorChallenges` modules contain four `sorry` declarations.
The current dependency audit does not place those declarations on the selected
R3 endpoint. The two facts must not be conflated.

## 4. Force construction and the smoothness attack

The force is residual-driven. Before the singular time,
`CandidateFromLimits.force` agrees with the activated residual

$$
\mathcal R(u,p)=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p.
$$

At the endpoint, a smooth extension is constructed from locally uniform
limits of all residual derivatives. `PositiveTimeForce` applies a genuine
smooth temporal cutoff and remains active through the singular interval; it
does not establish an autonomous collapse.

The proposed attack is mathematically meaningful: if the selected fields
satisfied a positive lower estimate

$$
c\,\lVert u(t,0)\rVert
\leq
\lVert\mathcal R(u,p)(t,0)\rVert,
\qquad c>0,
$$

then residual flatness at $t=1$ would contradict origin blow-up. The
zero-sorry probe
[`SelectedResidualLowerBoundObstructionProbe.lean`](../NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean)
proves exactly this conditional contradiction on the actual one-sided
endpoint filter.

The selected-path extraction and the zero residual limit are recorded in
[`SelectedWitnessEndpointResidualProbe.lean`](../NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean).

The selected source, however, also contains explicit core cancellation:
`FinalSlowBase.stressForce_core_germ` and its jet theorem make the stress-force
part vanish in the core, while the remaining error is controlled by flat jet
estimates. Thus the implication

$$
\lVert u(t,0)\rVert\to\infty
\quad\Longrightarrow\quad
\lVert\mathcal R(u,p)(t,0)\rVert\to\infty
$$

has not been proved and is not a valid inference from norm growth alone. The
force-smoothness attack is closed as a force-explosion argument by the selected
force-origin composition result. A formal refutation now requires a different
incompatible selected-field identity or a false mandatory premise.

## 5. The flat residual is an all-order, debt-blind interface

The source definition of `VanishingJointJets` quantifies over every natural
order of the spacetime Fréchet derivative. Its selected construction is fed by
finite residual-rate estimates derived from the actual cycle invariant, then
passes through the schedule theorem and the mixed residual theorem. It is not
an `H^3` truncation.

The time switch is globally smooth, becomes identically one for
`t\geq3/4`, and has zero positive-order derivatives on that late region. The
spatial periodic and cut residuals agree with the original residual on a
neighbourhood of the origin. The comparison is made with the complete
Navier--Stokes residual, so the temporal derivative, advection, Laplacian, and
pressure-gradient terms are not projected away.

This regularity result does not by itself settle the full paper/CMI semantic
crosswalk. The localisation files do not take the paper tuple as an explicit
parameter or re-export it as a named field equality. That is a scope fact about
the interface, not proof that the localisation or the upstream repair data are
irrelevant to the selected residual construction.

## 6. The five-moment correspondence objection

### Status correction

This section records a live correspondence audit, not a finding that the
five-moment mechanism is absent. Raw source inspection establishes the chain

\[
\text{profile moments/rank repair}
\Rightarrow \text{coefficient matching}
\Rightarrow \text{finite Cartesian residual identity}
\Rightarrow \text{selected residual and candidate data}.
\]

The question is whether any particular paper assertion requires an additional
identity for the completed whole-space field that is not among those proved
consequences. The public `Witness` not repeating a named tuple is not enough to
answer that question adversely. A concrete mismatch, impossibility theorem,
or stronger CMI-semantic failure would be required for escalation.

The upstream five-moment machinery is substantive. In
`PositiveOrderMoments.lean`, the history debt is

$$
\mathrm{Debt}=\mathrm{Fin}(5)\to\mathbb R,
$$

and `rowDensity` contains the five literal rows

$$
\begin{aligned}
&R u_n,\\
&R^2 e_n,\\
&\partial_R p_n,\\
&R^2\,\mathcal C_n(u,e),\\
&R\,\mathcal C_n(u,u)-\tfrac{R^2}{2}\partial_Rp_n.
\end{aligned}
$$

`moments_repair_target` proves exact repair to an arbitrary five-coordinate
target under its explicit radial hypotheses. `GlobalStressSupport` and the
aligned base construction use this machinery.

The runtime rank engine is a different interface. `FiveRowRank` declares

$$
\mathrm{Debt}=\mathrm{Fin}(3)\to\mathbb R,
$$

with coordinates $(P,J_\theta,J_z)$. Its proposition `FiveRows` has two
fixed zero-moment rows and three debt-controlled rows. `MeanRankUpdate.scaleDebt`
uses the coefficients

$$
\bigl(U^2d_0,\;\ell^3U^2d_1,\;\ell^2U^2d_2\bigr).
$$

The direct dimension objection is therefore insufficient. A zero-sorry probe
shows that the positive-order repair reduces to the rank repair under the
promotion

$$
(P,J_\theta,J_z)\longmapsto(0,0,-P,-J_\theta,-J_z).
$$

The actual adverse result is transport, not existence of repair code. The
exported `Witness` contains stage sums, away extensions, force predicates,
residual consequences, decay bounds, and boundary jets, but no equality of the
form

$$
\mathrm{moments}(u,e,p)=(M,I,J,S,C_p)
$$

and no theorem carrying such an equality into `StateRealization.chartIdentity`,
the selected residual, or the force. The source audit has not located that
selected-path theorem.

The zero-sorry probe
[`SelectedWitnessAttackBoundaryProbe.lean`](../NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean)
proves the precise interface statement

$$
\neg\bigl(\mathrm{Witness}\Rightarrow
\forall d:\mathrm{Fin}(5)\to\mathbb R,\ d=0\bigr).
$$

This means the witness envelope cannot certify the paper's five-moment
transport by its type alone. It does not prove that the concrete selected
velocity violates the five integrals. That second statement needs a
field-level computation.

### Why the missing bridge is load-bearing

The issue is not simply that the tuple `(M,I,J,S,C_p)` is absent from the
public proposition. The supplied OpenAI paper uses the five cumulative radial
integrals as premises in several later arguments. In Section 4.2 and Lemma
4.4, matching the five integrals is used to preserve the outer pressure and
velocity fields and to remove integrated stress outside the joining annulus.
Appendix A uses the total moment identities to remove radial stress tails.
Section 5 and Appendix B restore the five integrals after joining and shear
modulation. Section 8 then solves a five-equation correction system: two
equations preserve zero angular-momentum and axial-flux integrals, while
three cancel the defects `(P,J_θ,J_z)`. Section 9 uses those preserved
identities in the residual-improvement cycle. [OpenAI, 2026, Sections 4.2,
5, 8–9 and Appendix A]

This makes CTR-005 a proof-engine correspondence failure, not a missing
explanatory label. If Lean does not prove that the final selected Cartesian
fields carry the required identities, then the formal record does not
establish that the paper's exterior matching, stress-tail cancellation,
modulation repair, or correction-cycle conclusions apply to those fields.
The point is conditional in exactly one direction: absence of the transport
theorem does not prove that the identities are false, but it does prevent the
paper's downstream arguments from being verified for the exported witness.
The current status is therefore **not established**, not `False`.

| Paper dependency | Role of the five moments in the paper | Status at the selected Lean endpoint |
| --- | --- | --- |
| Exterior matching | Preserves the heat-exterior pressure and velocity beyond the joining radius | No selected-field transport theorem established |
| Stress-tail removal | Uses total moment identities to eliminate radial stress tails | Not connected to the exported Cartesian field |
| Modulation repair | Restores all five integrals after high-frequency modulation | Upstream repair algebra exists; final-field application is unproved |
| Correction cycle | Preserves two rows and cancels three defects `(P,J_θ,J_z)` | Runtime three-debt repair is present; its identification with the paper's five selected-field identities is unproved |

Source-level evidence for this distinction is retained in the [selected
endpoint moment transport obstruction](../NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md),
the [selected moment transport source trace](../NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md),
the [full selected transport audit](../NavierStokesReview/evidence/selected_transport_audit_full_2026-09-28.md),
and the [load-bearing paper dependency matrix](../NavierStokesReview/evidence/paper_moment_dependency_matrix_2026-09-29.md).

### The profile-tail collision route and its exact limit

The natural next attack is to calculate one of the selected fields' radial
moments and combine a nonzero remainder with the zero rows of `FiveRows`. The
source audit shows why that route is conditional rather than already a
contradiction. `FiveRows` applies to correction profiles `dv` and `ga`; its
first two equations are

$$
\int R^2\,dv(R)\,dR=0,
\qquad
\int R\,ga(R)\,dR=0.
$$

They are not, by themselves, equations saying that the total Cartesian field,
its kinetic energy, or its five paper moments vanish. The review-side
refutation module proves the complementary fact that a nonzero runtime debt
can coexist with those two zero correction rows. This removes the proposed
type-unification shortcut: no contradiction follows merely from the
three-coordinate debt interface.

The selected cycle does carry a real local two-moment invariant, and the
conditional obstruction is valid: if a selected correction moment is proved
nonzero, `FiveRows` yields `False`. The missing step is a field-level map from
the selected Cartesian `tsum` and pressure to the radial profile/history types
accepted by `barMoment` or `PositiveOrderMoments.moments`. `barMoment` itself
is a function-valued radial/toroidal integral, not a total integral of the
exported `VelocityField`.

Thus the route remains the strongest path toward a kernel contradiction, but
its decisive nonzero-remainder premise has not been established. The current
publication conclusion is unchanged: the paper's five-moment mechanism is
**NOT ESTABLISHED** at the selected endpoint, while a literal selected-path
`False` result remains an open stronger target.

Evidence: `NavierStokesReview/evidence/ctr005_profile_tail_collision_route_2026-09-25.md`.

## 7. Pressure and localisation

The R3 packaging imposes compact support on pre-singular pressure slices.
Pressure-recovery modules prove genuine compact-test comparison identities,
and `StateRealization` supplies local pressure germs and a local residual
identity. These are not empty modules.

They do not, by their inspected interfaces, provide an absolute global
pressure representative satisfying the selected paper's claimed Poisson or
Leray semantics. In particular, the comparison hypotheses can be instantiated
with identical zero velocities and a common smooth pressure. The comparison
chain therefore cannot by its type alone certify the absolute selected
pressure.

Compact support alone is still not a contradiction. The external force is
allowed to absorb the pressure-gradient contribution in the forced residual.
To obtain `False`, the review must first prove a selected-field identity such
as

$$
-\Delta p=\nabla\!\cdot\nabla\!\cdot(u\otimes u-f\otimes I)
$$

with the required domain, normalisation, and decay hypotheses, and then show
that this identity is incompatible with the compact pressure predicate. The
current source does not expose that complete bridge. The pressure route is
therefore an open analytic correspondence objection, not a completed
trivialisation theorem.

## 8. Generic interfaces and countermodels

The generic `StageEstimates` record stores smoothness and finite jet-rate
bounds but no five-moment field integral. A zero-sorry probe inhabits this
record with identically zero velocity and pressure stages and proves that the
record does not determine an arbitrary five-coordinate debt. This refutes the
inference

$$
\texttt{StageEstimates}\Longrightarrow\text{five-moment realisation}.
$$

It does not refute `selected_witness`, which adds actual physical-data,
base-profile, endpoint, and origin-growth premises. Similarly, the generic
filter API permits vacuous statements over `Filter.bot`, but the selected
origin-past filter has been checked non-vacuous. The generic hazard is real;
selected-path exploitation has not been demonstrated.

## 9. Pressure response and the residual equation

The proposed equal-and-opposite pressure argument was tested against the
actual operator rather than treated as a general physical objection. The
residual is

$$
\mathcal R_\nu(u,p)=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p,
$$

and the candidate predicate requires `\mathcal R_\nu(u,p)=f`. The force is
therefore the full residual, not a separate term that the pressure equation
must cancel.

The zero-sorry probe
[`PressureResidualNonCancellationProbe.lean`](../NavierStokesReview/src/probes/PressureResidualNonCancellationProbe.lean)
compiles the exact perturbation identity

$$
\mathcal R(u+e,p+q)-\mathcal R(u,p)
=\partial_te-\Delta e+\nabla q
 +(u\cdot\nabla)e+(e\cdot\nabla)u+(e\cdot\nabla)e.
$$

In particular, for zero velocity,

$$
\mathcal R(0,q)-\mathcal R(0,0)=\nabla q.
$$

Thus a nonzero pressure gradient changes the residual; the formal operator
does not imply an equal-and-opposite cancellation. The pressure-recovery
modules are comparison results: they assume two divergence-free fields with
equal residuals and recover pressure differences through compact tests. They do
not impose an absolute Poisson representative for the selected fields.

For a forced incompressible equation, the divergence identity contains the
force term:

$$
\Delta p=\nabla\!\cdot f-
\nabla\!\cdot\bigl((u\cdot\nabla)u\bigr),
$$

when the required commutations are available. Dropping `\nabla\!\cdot f`
would silently replace the forced problem by an additional divergence-free
force assumption. That assumption is not part of the exported candidate
predicate.

The pressure route therefore yields a precise correspondence objection, not a
formal annihilation theorem: the selected path still lacks an explicit
absolute global pressure-Poisson/normalisation bridge, but the proposed
pressure cancellation has not been proved and is contradicted by the compiled
residual identity.

## 10. External-force causality

The official problem statement describes \(f(x,t)\) as a given, externally
applied force. The repository instead defines the final force from the selected
velocity, pressure, and residual-limit data. This is a real paper-to-code
causality mismatch: the construction is residual-designed, not a forward
initial-value argument in which an independently specified force is held fixed
while the velocity evolves.

The formal consequence must nevertheless be stated precisely. Fefferman's C/D
alternatives quantify over the existence of a smooth force satisfying the
specified decay conditions. They do not state an additional Lean-style
independence predicate forbidding the construction of that force from other
witness components. Once constructed, the residual-defined object is still a
function (f(x,t)). The CMI prize rules do not add such a causal predicate.

Therefore residual feedback is a serious objection to the physical
interpretation and to any claim that the code reproduces a prescribed-force
evolution. It is not, without an additional admissibility theorem or a false
mandatory endpoint predicate, a formal disproof of the literal existential C/D
proposition. The official-source adjudication is recorded in
[`cmi_force_independence_adjudication_2026-09-24.md`](../NavierStokesReview/evidence/cmi_force_independence_adjudication_2026-09-24.md).

The fixed-data test makes this objection mathematically sharper. Let (e) be
an independently chosen smooth perturbation, keep (p) and the spacetime
force (f) fixed, and require both (u) and (u+e) to satisfy the same
residual equation. The compiled theorem
[`IndependentDataPerturbationProbe.lean`](../NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean)
derives the necessary identity

$$
\partial_t e-\Delta e+(u\cdot\nabla)e+(e\cdot\nabla)u+(e\cdot\nabla)e=0.
$$

The extension module packages the stronger local conclusion: whenever this
defect is nonzero at one spacetime point, the perturbed field cannot satisfy
the same fixed force. This formally exposes the dependence of the
residual-designed force on its selected velocity path. It does not, however,
show that the selected existential witness must admit such a perturbation, and
therefore does not by itself derive `False` from the C/D endpoint.

The localisation objection has now been formalised rather than left at the
level of the affine test. `CompactFixedForcePerturbation.lean` constructs a
smooth compactly supported potential, takes its spatial curl, and forms a
time-affine perturbation. The resulting field is divergence-free on every
time slice. At the switch time its spatial value, first derivative, and
Laplacian vanish, while its temporal derivative at the origin is the nonzero
first coordinate vector. The theorem
`compactPerturbation_breaks_any_fixed_force_at_origin` proves that the base and
perturbed fields cannot satisfy the same residual equation with the same force.
This is a genuine localised fixed-data obstruction, but it remains an
operator-level result: the literal endpoint does not assert stability under
perturbation, so this theorem alone does not refute its existential quantifier.

The probe also contains a concrete test field

$$
e_a(t,x)=(t-t_0)a,qquad a\ne0.
$$

It proves this field is globally smooth and spatially divergence-free, and
computes its defect at (t=t_0) as exactly (a). Thus the same fixed force
cannot satisfy both the original and perturbed velocities. The field is not
compactly supported or finite-energy on (mathbb R^3), so this is an exact
operator-level causality obstruction rather than a direct CMI counterexample.

The correct CTR-012 conclusion is consequently two-layered. The construction
is not a forward prescribed-force stability result: changing the velocity
without recomputing the residual generally destroys the force identity. But a
single specially matched smooth triple ((u,p,f)) can still satisfy a literal
existential statement. A formal CMI disproof requires either an independence
condition in the theorem being claimed or a selected-path theorem that supplies
an admissible perturbation with nonzero defect. The exact proof and its limits
are recorded in
[`independent_data_perturbation_2026-09-24.md`](../NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md).

The perturbation test was then strengthened so that it preserves the selected
zero initial datum. The new field is

$$e_{t_0}(t,x)=t(t-t_0)\,\mathrm{curl}A(x).$$

It is smooth, compactly supported on each spatial slice, divergence-free, and
zero at both $t=0$ and $t=t_0$. At $t=t_0$ its spatial derivative and spatial
Laplacian vanish, while its temporal derivative is
$t_0\mathrm{curl}A(x)$. At the origin the selected compact potential
gives a nonzero curl, so the fixed-force residual equation fails at the switch.
This closes the initial-data loophole in the earlier perturbation probe and
strengthens CTR-012 as a forward-data provenance objection. It still does not
negate the literal existential C/D proposition, which does not quantify over
such perturbations or encode force independence.

Evidence:
[`same_datum_fixed_force_obstruction_2026-09-24.md`](../NavierStokesReview/evidence/same_datum_fixed_force_obstruction_2026-09-24.md).

Other proposed objections remain outside the CMI disproof threshold unless a
selected-path theorem supplies their missing premise: active forcing, nonzero
force integral or divergence, non-Newtonian regularisation, pure-axial collapse,
and compact pressure support alone.

## 11. Verdict

The formal review establishes the following.

1. The selected Lean endpoint is a real forced C/D-shaped proposition and is
   standard-axiom-only in the inspected dependency reports.
2. The force is selected from the candidate residual and remains active near
   the singular time.
3. The repository contains genuine five-row and profile-moment repair
   mathematics, and raw source tracing gives positive evidence that it is
   used in the selected production route. `FiveRowRank` and the mass-
   preservation lemmas feed the actual cycle invariant; the connected
   radial/state-moment hierarchy feeds physical data and residual-rate
   estimates; those estimates feed the flatness, force-extension, and
   selected-witness path. The public `Witness` does not repeat the named
   profile tuple as a field, but this is not merely an argument from silence:
   the source trace positively rules out a wholesale bypass of the repair
   engine. It does not, however, prove the separate final-observable
   identity described in item 4.
4. The force-smoothness attack has a proved conditional contradiction, but its
   required selected-field lower bound is missing.
5. The pressure chain has comparison infrastructure, but compact support alone
   does not yield a pressure trivialisation contradiction.

The resulting verdict is:

> **The inspected record does not yet establish exact identity between the
> published paper's full CMI argument and the exported Lean endpoint. The
> endpoint is nevertheless a substantial formally checked forced breakdown
> proposition, and no formal contradiction to its selected witness has yet
> been proved.**

The two clauses have different logical roles. The first is the review verdict:
the exact scope of every paper consequence and CMI condition has not yet been
independently matched to the selected fields. It is not a finding that the
moment/rank mechanism is absent. The second is a narrow statement about the
present refutation programme: no zero-sorry proof of `False`, selected-field
mismatch, or impossibility theorem has yet been derived from the endpoint.

The review must therefore not call the literal existential endpoint formally
refuted merely because its public envelope does not repeat the profile tuple.
The next work is adversarial source analysis: test each paper consequence and
CMI condition on the selected fields, derive a concrete mismatch or
impossibility if one exists, and credit a positive bridge if the raw source
supplies it.

The surviving adverse classification is a scoped correspondence question,
not the earlier claim that selected-path moment restoration is missing. The
review should be upgraded to a formal refutation only after a zero-sorry
theorem derives `False`, proves a false mandatory endpoint predicate, or
establishes a concrete mismatch for the selected field.

## 12. Current closure and remaining counter-arguments

The five-moment objection is not that the repository lacks five-moment
mathematics. A transitive import traversal rooted at
`ActualCandidateAssembly.lean` reaches 507 local modules, including the
positive-order, profile, and rank subsystems. The source contains exact repair
identities and uses rank/debt data upstream of the selected endpoint.

The remaining audit question is about semantic scope, not whether the engine
was used. The public `Witness` proposition exposes the selected schedule, mixed
sums, extensions, force, candidate properties, consequences, blow-up norm,
force decay, and boundary jets. It does not repeat an equality identifying the
final mixed fields with the paper's five quantities

$$
(M,I,J,S,C_p),
$$

as a named public field. That does not show that the equality was needed as a
direct argument at this boundary: upstream theorems can be used to prove the
residual, pressure, force, and all-order jet estimates without being re-exported
as fields. It does show that the public proposition alone is not a convenient
certificate of the paper's named observables.

The paper itself makes this correspondence indispensable. Its notation table
defines $m=(M,I,J,S,C_p)$ as the five cumulative radial integrals preserving
pressure, radial velocity, and stress across profile joins. The construction
then states that vanishing five moments remove the exterior pressure and stress
tails, solves for five correction coefficients, and uses exact matching to
preserve the subsequent outer fields. Appendix A repeats that the moment
matching and the axis pressure datum preserve every subsequent outer field.
Those are load-bearing assertions in the paper, not informal physical
commentary. The decisive audit question is whether the proved reduced-profile
and finite-residual consequences have the same mathematical scope as those
assertions after the selected mixed stages and whole-space packaging. The
public absence of a tuple field does not answer that question either way.
The decisive next step is therefore a source-grounded scope theorem or a
zero-sorry counterexample to one of the concrete equalities.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

### The proposed rank-collision refutation

A stronger proposed refutation was tested: inject a compact perturbation into
the selected witness and use the two zero rows of `FiveRowRank.FiveRows` to
derive an impossible nonzero moment. The source does not support that
inference. The five-row predicate is a proposition about two correction
functions and a three-coordinate debt. Its theorem `five_rows` is inhabited
for arbitrary admissible debt, including nonzero debt. The correction-state
theorems preserve two radial moments, but do not state that those moments are
the selected field's kinetic energy or the paper's complete five-moment tuple.

The endpoint `Witness` contains no rank debt or perturbation parameter. Thus
the compact perturbation theorem cannot be substituted into the endpoint by
type unification, and no `False` theorem follows from the zero rows alone.
This negative result is useful: it removes an attractive but invalid shortcut
and leaves the substantive paper-to-code question in its proper form. The
remaining test is whether the selected-path identities already proved for the
correction state and mixed sums have the same scope as the paper's named
observables in the residual, pressure, and force. Evidence:
`NavierStokesReview/evidence/five_row_collision_boundary_2026-09-24.md`.

The runtime scope is now checked separately. `MeanRankUpdate.scaleDebt` has
three debt coordinates, and `FiveRows` constrains only two radial moments of
the correction functions before applying its three debt equations. A compiled
completion constructs a nonzero debt satisfying the full predicate. Thus the
review does not claim that the runtime rows hard-code total kinetic energy to
zero. The unresolved issue is the exact scope of the selected-path transport
of the internal correction data into the exported field and the paper's five
named moments.
Evidence: `NavierStokesReview/evidence/mean_rank_update_scope_2026-09-24.md`.

### A conditional correction-moment obstruction

The zero rows are not empty syntax. They force two precise radial moments of
the correction increment to vanish. The new Lean completion
`CorrectionInvariantScope.lean` proves the corresponding conditional
refutation: if an increment transported into the rank subsystem has a nonzero
`barMoment 2` angular component or nonzero `barMoment 1` axial component, the
complete `FiveRows` predicate is inconsistent.

This is the strongest result presently available from the rank interface. It
does not, by itself, identify an externally chosen Cartesian perturbation with
the correction increment, nor does it identify the two radial moments with
kinetic energy or the paper's five named moments. The remaining theorem is
therefore concrete rather than rhetorical: transport the perturbation through
the selected stage construction, calculate one of these moments as nonzero,
and apply the conditional obstruction. Until that transport is proved, the
result is a load-bearing route to falsification, not a completed `False`
theorem for `selected_witness`.

### What the two zero rows actually preserve

The rank construction is stronger than a syntactic placeholder, but weaker
than the proposed energy argument. Its first two equations constrain the
increment functions themselves:

\[
\int R^2\,dv(R)=0,\qquad \int R\,ga(R)=0.
\]

The correction-state layer identifies these with two radial moments of the
updated angular and axial mean fields, and the generic rank theorem preserves
them from one rank stage to the next. This is a genuine conditional
obstruction: a correction increment with a nonzero corresponding moment cannot
satisfy the complete five-row system.

It is not, however, an energy identity. The source does not equate these
radial moments with total kinetic energy, the full Cartesian velocity, or the
paper's five quantities `(M,I,J,S,C_p)`. Nor does the selected `Witness`
export those moments. The remaining decisive task is therefore a semantic
transport theorem from the selected perturbation and mixed stage fields into
`rankIncrement`. If that theorem proves a nonzero radial moment, the
conditional `False` result closes the selected path; until then, the formal
finding is a correspondence failure under CTR-005, not a completed
refutation. Evidence:
`NavierStokesReview/evidence/correction_moment_transport_audit_2026-09-24.md`.

### Internal cycle invariant and the remaining endpoint gap

The source contains a further fact that must be distinguished from the
exported theorem interface. `ActualCyclePreservation.Invariant` is a
`CycleAnalyticInvariant` with a `masses` field. Its induction therefore proves
that every actual selected-cycle state has two local radial moments equal to
zero. The separate Lean completion exposes this invariant and proves that a
nonzero value of either corresponding selected-cycle moment is impossible.

This result removes an overly broad version of the “zero rows are ignored”
objection. The correction cycle does preserve the two quantities it names.
What remains unproved is the semantic transport from those internal mean
fields into the mixed velocity and pressure sums consumed by `Witness`, and
then into the five published quantities `(M,I,J,S,C_p)`. The local invariant
also says nothing by itself about total kinetic energy. The counter-paper's
load-bearing claim is consequently precise: the source has an internal
two-moment conservation theorem, but does not display the theorem that makes
it the paper's five-moment endpoint certificate. Evidence:
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.

### Direct endpoint trace

The immediate source path sharpens this conclusion. `ActualCandidateAssembly`
does consume actual cycle data and residual estimates, while
`CorrectionState` proves the rank rows for the constructed correction. The
exported `Witness`, however, contains no equality to
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or the named tuple `(M,I,J,S,C_p)`. The absence is not
evidence that those upstream identities are false; it is the absence of the
transport theorem needed to claim that the selected endpoint is the same
five-moment object described in the paper.

This distinction is recorded in
`NavierStokesReview/evidence/selected_endpoint_direct_source_trace_2026-09-24.md`.

### Temporal stage boundary audit

The indexed stage constructor deserves a separate statement. In
`GermCandidateAssembly.lean`, `initializedSeries` assigns the base plus initial
field to index zero and assigns `stages j` to index `j+1`. This leaves no
adjacent-stage matching condition at the constructor boundary. The finite-prefix
theorems in `ActualCandidateConstruction.lean` are additive identities, not
energy conservation laws and not temporal interpolation statements.

This is not merely a missing annotation. The supplementary theorem
`initialized_series_admits_concrete_boundary_mismatch` constructs a raw family
with zero base and initial fields and a nonzero first stage. It proves that the
indexed selector permits unequal adjacent entries. The construction is still
not a temporal counterexample: the index is a natural number, not time, and the
theorem does not assert the selected `StageEstimates`, support, divergence,
residual, or endpoint conditions.

That observation does not establish a discontinuity in the selected field.
The selected sums have presingular smoothness theorems, the time activation is
globally smooth, and late temporal derivatives agree by local eventual
equality. The correct conclusion is an open interface obligation: the review
has not found a theorem deriving a selected temporal boundary mismatch, so it
cannot call the temporal-patching route a formal refutation.

The exact ledger and zero-sorry probe are in
`NavierStokesReview/evidence/temporal_patching_audit_2026-09-24.md` and
`NavierStokesReview/src/probes/TemporalPatchingDiscontinuityProbe.lean`.

### Source context and causal wording

Fefferman describes the force as given and externally applied, which supports
a provenance objection to choosing a trajectory first and defining its
residual afterwards. OpenAI's own paper nevertheless makes that residual
construction explicit and states that the challenge is to make the residual
smooth through the singular time. The formal review therefore asks for the
missing semantic bridges rather than treating the construction method alone as
a contradiction of the existential C/D statement.

The companion Euler paper uses a parent-child sequence on nested time
intervals. That is useful context for what a genuine temporal induction looks
like, but it does not prove that the Navier--Stokes Lean stage index is a time
partition. The full source-context register is
`docs/OpenAI_NavierStokes_Source_Context_Register.md`.

The official CMI statement is correspondingly important in two ways. It calls
the force given and externally applied, which makes force provenance a serious
mathematical question. It also formulates alternatives C and D existentially,
with smooth force data satisfying the stated decay conditions. A perturbation
test or a sign-reversed force therefore cannot, by itself, refute the selected
existential witness. The decisive formal target remains a false mandatory
premise, a concrete selected-field mismatch, or a proved scope failure in the
transport of the five named moments and pressure semantics into the exported
endpoint.

## References and evidence

1. Charles L. Fefferman, [Existence and Smoothness of the Navier–Stokes
   Equation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
2. Clay Mathematics Institute, [Millennium Prize rules](https://www.claymath.org/millennium-problems/rules/).
3. OpenAI, [NavierStokesAndEuler repository](https://github.com/openai/NavierStokesAndEuler).
4. OpenAI, [Finite Time Blowup for Navier–Stokes](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).
5. OpenAI, [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/).
6. OpenAI, [Finite Time Blowup for the Euler Equation](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf).
7. [`SelectedResidualLowerBoundObstructionProbe.lean`](../NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean).
8. [`SelectedWitnessAttackBoundaryProbe.lean`](../NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean).
9. [`FiveRowPositiveOrderBridgeProbe.lean`](../NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean).
10. [`PressureRecoveryAbsolutePremiseProbe.lean`](../NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean).

## Appendix A. Technical findings supporting the verdict

The selected-force provenance theorem extracts the endpoint identity

$$
f(t,x)=\partial_tu+(u\cdot\nabla)u-\Delta u+\nabla p
$$

for interior times. Together with the compact perturbation theorem, this
proves that the selected trajectory is not stable under arbitrary smooth,
compactly supported, divergence-free perturbations when the force and pressure
are held fixed. This is the formal CTR-012 causality objection. It is not a
contradiction of the literal existential C/D endpoint, which does not include
that stability predicate.

The runtime rank layer is active. `MeanRankUpdate.physical_five_rows` and
`CorrectionState.rank_model_rows` apply the three-coordinate debt repair to
the actual cycle. The first two rows preserve two radial correction moments;
they do not state that total kinetic energy is zero. The exported `Witness`
still exposes no equality identifying those internal quantities with the
paper's $(M,I,J,S,C_p)$ and transporting them into the final mixed fields,
pressure, residual, and force. This is the load-bearing CTR-005
paper-to-endpoint correspondence problem.

The whole-space uniqueness route is also active: the comparison theorem uses
the two residual equations, incompressibility, smoothness, finite-energy
bounds, compact support, and compact-test pressure recovery. Compact pressure
support alone does not imply that pressure or velocity vanishes. The remaining
pressure objection is the absence of an absolute selected pressure
representative in the exported semantic bridge.

The stage-control source contains an empty/nonempty split for `ActivePair`.
The review construction resolves the selected-path inhabitance question. The
partition identity

$$
\sum_k\mathrm{slowMask}_n(k,x)^2=1
$$

implies that at least one grid mask is nonzero at every positive band. The
explicit point $(\sqrt{2a},(0,1))$ lies in the reference annulus, so a label
above the selected threshold can be constructed. The zero-sorry theorems
`selected_primary_label_nonempty` and `selected_active_pair_nonempty` then
inhabit the selected label and active-pair subtypes.

The inhabitability sweep narrows this point. `ActualPrimary.choice_nonempty`
constructs the prepared geometric choice, not a label. Meanwhile,
`ActualInitialMean.covariance_bounds_of_curl` explicitly handles an empty
cycle index, and `ActualParticularStageControls.raw_jets` explicitly handles an
empty active-pair type. These are genuine reachability obligations. They do
not, however, make the diagonal velocity series vacuous: `LocalScheduleWitness`
defines `potentialSum` through `SolenoidalDiagonal.potentialSum`, whose actual
`tsum` is indexed by the natural stage number. The generic empty branch is
therefore not a selected-path empty-limit explanation. The remaining
load-bearing issue is CTR-005: no theorem identifies the selected Cartesian
fields and residual with the paper's complete five-moment tuple.

These results are source-linked and compiled in the evidence files below. The
paper's conclusion remains a correspondence-based counter-claim: the public
paper's five-moment semantics are not yet shown to be the semantics of the
exported selected witness. A kernel-level disproof still requires a false
mandatory endpoint premise or a concrete selected-field contradiction.

Evidence: `selected_residual_provenance_2026-09-24.md`,
`selected_rank_transport_reaudit_2026-09-24.md`,
`whole_space_uniqueness_audit_2026-09-24.md`,
`selected_active_pair_reachability_2026-09-24.md`,
`selected_label_inhabitability_audit_2026-09-24.md`.

## Appendix B. Global germ transport and endpoint contract

The source trace separates two claims that are easy to conflate. The theorem
`CandidateConsequences.mixed_exists_force_with_consequences` at
`CandidateConsequences.lean:185-215` does provide a substantial local-to-global
bundle: a force, the complete `CandidateProperties` record, lifespan and H³
consequences, force-jet decay, and the all-order boundary-jet identity. The
concrete assembly supplies its local inputs through `physicalData`, `estimates`,
and `endpoints` at `ActualCandidateAssembly.lean:1079-1115`, and packages the
result in `Witness` at lines `1121-1151`.

That bundle still does not export an equality identifying the selected fields
with the paper's five named moments. Nor does it require that the force and
pressure remain fixed under a smooth, compactly supported, divergence-free
perturbation that preserves the initial datum. The review-side
`GlobalTransportBridgeProbe.lean` proves the exact boundary: the selected
candidate has the full `Consequences` bundle while
`FixedForceSameDatumStable` fails. A second extension proves the universal
non-implication from `CandidateProperties` to that stability predicate.

This result strengthens the causal and paper-to-endpoint objections without
changing the formal verdict. It is not a proof that the literal existential C/D
proposition is empty, because that proposition quantifies over one admissible
force and one candidate trajectory and does not state the stronger stability or
five-moment transport requirements.

Evidence: `global_germ_transport_audit_2026-09-24.md`,
`endpoint_contract_nonimplication_2026-09-24.md`.


## Evidence and provenance dossier

The complete source-audit dossier, including the preserved chronology, source tranches, declarations, probe results, and corrections, is maintained separately at [research_paper_evidence_dossier_2026-09-30.md](../NavierStokesReview/evidence/research_paper_evidence_dossier_2026-09-30.md).

The dossier is evidence and provenance, not an additional publication claim.
## CMI semantic scope and paper-to-code boundary

The CMI target used in this paper is Fefferman's connected formulation, not a
bare restatement of equations (1)--(3). The source wording is preserved in
`docs/navierstokes.txt:25-81,89-184`. In particular, “we may look for
spatially periodic solutions” selects an alternative branch; “thus, we
assume”, “in place of”, and “we then accept” connect the periodic data and
solution conditions to that branch. “Physically reasonable” and “retaining
the heart of the problem” retain the global smoothness and admissibility
meaning across alternatives C and D.

The exact word-to-condition network and the Lean crosswalk are maintained in
[`CMI_OpenAI_Full_Semantic_Crosswalk.md`](CMI_OpenAI_Full_Semantic_Crosswalk.md)
and
[`priority_193_fefferman_semantic_branch_network_2026-09-30.md`](../NavierStokesReview/src/audit/priority_193_fefferman_semantic_branch_network_2026-09-30.md).

The manuscript's own construction has a second connected dependency: the
residual-defined force must remain smooth even though individual terms may be
singular. The profile moments, stress and pressure tail cancellation, wave
corrections, localisation, summation, and all-order residual estimates belong
to that mechanism. The present review therefore distinguishes the formal
comparator-level C/D proposition from complete selected-field reproduction of
the manuscript mechanism. The latter remains `NOT ESTABLISHED (CTR-005)` until
the selected Cartesian transport and observable identities are proved or
refuted by a direct value-level result.

This status is deliberately not weakened into “the moments are optional”, and
it is not inflated into a literal C/D refutation without a selected failed
condition, mismatch, impossibility theorem, or contradiction.

The corresponding source adjudication is
[`priority_195_four_operation_force_smoothness_adjudication_2026-09-30.md`](../NavierStokesReview/src/audit/priority_195_four_operation_force_smoothness_adjudication_2026-09-30.md).
It records that the five-moment repair is substantive while the manuscript
also describes additional residual-control operations. The missing final
selected-field identification therefore remains a genuine correspondence gap,
but it is not by itself a proof that the selected force is nonsmooth or that a
connected CMI alternative is false.
# Live control checkpoint: 2026-09-30 continuation

The latest connected CMI and manuscript crosswalk is Priority 201:
`../NavierStokesReview/src/audit/priority_201_selected_closure_census_2026-09-30.md`.
It must be read with Priority 200 and the raw CMI, manuscript, and R3
endpoint source ranges listed there.

This paper is a reader-facing synthesis, not a chronological agent log. The
current source-of-truth control is
`REVIEW_DOCUMENT_CONTROL.md`, with the companion peer review in
`OpenAI_NavierStokes_Peer_Review_v1.md` and the current evidence reconciliation
in `../NavierStokesReview/evidence/tree_reconciliation_current_2026-09-30.md`.
The review branch is
`review/cmi-first-navier-stokes-reconciled-2026-09-30`; the separate public
review branch is
`review/cmi-first-navier-stokes-disposition-public-2026-09-30`.

The live scientific conclusion remains deliberately calibrated. The source
tree contains real upstream moment/rank repair, Cartesian residual, pressure,
localisation, summation, and force-regularity machinery. The selected export
does not contain a separate named theorem identifying the final Cartesian
fields with `(M,I,J,S,Cp)`. Therefore complete manuscript-to-selected-endpoint
correspondence remains `CTR-005: NOT ESTABLISHED`. This wording does not claim
that the selected field has a nonzero defect, that the force is nonsmooth, or
that the Lean kernel derives `False`; those stronger propositions require
their own field-level proofs.

Current control evidence:

- `../NavierStokesReview/evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md`
- `../NavierStokesReview/src/audit/priority_198_latest_rebuttal_adjudication_2026-09-30.md`
- `../NavierStokesReview/src/audit/priority_193_fefferman_semantic_branch_network_2026-09-30.md`
- `../NavierStokesReview/evidence/untracked_consolidation_matrix_2026-09-30.md`

Older counts, queued-module totals, and branch names embedded in dated
sections are historical audit snapshots, not current status.
## Live audit result: Priority 201 closure census (2026-09-30)

The source census and review-side compilation record are maintained in
`NavierStokesReview/src/audit/priority_201_selected_closure_census_2026-09-30.md`
and
`NavierStokesReview/evidence/source_tranche_priority_201_selected_closure_census_2026-09-30.json`.
The result preserves the paper's connected five-moment dependency as
load-bearing, but records that the inspected selected endpoint still lacks a
named final moment-identification theorem. This is `CTR-005: NOT ESTABLISHED`
for exact manuscript-to-selected-endpoint correspondence, not a claim that
the selected physical field has a proved nonzero defect.
## Live audit result: Priority 202 actual invariant trace (2026-09-30)

The current positive trace is linked at
`../NavierStokesReview/src/audit/priority_202_actual_moment_invariant_trace_2026-09-30.md`.
It establishes that the actual correction cycle transports two zero mean
masses and carries three residual-debt components. This is genuine internal
moment-related mathematics. The paper-to-endpoint gap remains the missing
explicit identification with `(M,I,J,S,Cp)` for the final Cartesian field,
not the absence of all internal moment machinery.

### Priority 205 source-census correction

The selected-closure census and manual candidate adjudication are recorded in
\`../NavierStokesReview/evidence/source_tranche_priority_205_endpoint_census_and_completion_adjudication_2026-09-30.md\`.
It checked seven production declarations that lexically join endpoint,
field, rate, transformation, or moment vocabulary. These declarations
establish actual schedules, residual-rate bounds, eventual germ equalities,
and the axis blow-up route. They do not state the final observable identity
\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
=(M,I,J,S,C_p).
\]

The review-side \`SelectedBarMomentInterface\` defines a valid identity only
after a caller supplies a pullback and a scalar-profile equality. It therefore
does not close the selected-witness correspondence. The paper should be read
as containing genuine internal moment machinery and an unresolved final
observable identification, not as either empty code or a proven selected-field
defect. The controlled review status remains `CTR-005: NOT ESTABLISHED`.

## Current environment and whole-tree control checkpoint

The live Navier--Stokes closure was rebuilt with the pinned
`leanprover/lean4:v4.34.0-rc2` toolchain. It records 30,919 declarations,
329,127 declaration edges, zero missing names, and zero `sorryAx` nodes for
the six selected Navier--Stokes roots. The raw 366 MB graph is retained by
digest outside the scoped public commit. The source record is
[`priority_212_ns_environment_closure_2026-09-30.md`](../NavierStokesReview/src/audit/priority_212_ns_environment_closure_2026-09-30.md),
with the compact closure summary at
[`lean_environment_closure_ns_3d_2026-09-30_summary.md`](../NavierStokesReview/evidence/lean_environment_closure_ns_3d_2026-09-30_summary.md).

The closure removes the stale-environment qualification for those roots. It
does not establish the missing final observable identity. The controlling
whole-tree declaration census is
[`selected_transport_audit_2026-09-30_review_sources.md`](../NavierStokesReview/evidence/selected_transport_audit_2026-09-30_review_sources.md),
and its source-level interpretation is
[`priority_211_selected_transport_whole_tree_2026-09-30.md`](../NavierStokesReview/src/audit/priority_211_selected_transport_whole_tree_2026-09-30.md).
The production source census found no declaration identifying the completed
selected Cartesian field with `(M,I,J,S,C_p)`; the review-side candidates are
conditional caller-supplied interfaces rather than an instantiation of
`selected_witness`.

The active scientific disposition remains `CTR-005: NOT ESTABLISHED` for
complete manuscript-to-selected-endpoint correspondence. This is not a claim
of a selected nonzero defect, force nonsmoothness, literal CMI failure,
impossibility theorem, compiler escape, or `False`.

## Priority 227 selected-axis result

The selected-field audit adds a narrower result. A zero-sorry completion proves
that the exact first-component radial pullback used by the review-side
periodic-support gate is eventually zero on the axis as `t` approaches `1`.
This follows from the selected origin germ equality and
\[
u(t,0)=c(t)\,e_2,
\]
where the blow-up is in the axial component `e_2`, whereas the pullback
samples component `1`. This does not prove that the off-axis pullback is zero
or nonzero, and it does not replace the missing final five-observable
identification. `CTR-005` therefore remains `NOT ESTABLISHED`.
The route-level audit now supplies a positive qualification to the endpoint finding. `ActualCandidateAssembly.selected_witness` feeds `ActualCandidate.selected_candidate_one_with_initial_rest`, and `R3.Theorem` scales one common tuple `(u,p,f,K)` before the comparator and periodic routes consume it. Thus the review does not claim that the endpoint chooses unrelated fields for velocity, pressure, force, and blow-up. The unresolved issue remains narrower and more exact: no production theorem has been located identifying those final selected fields with the manuscript's five observables \((M,I,J,S,C_p)\), or proving their transport through the complete selected transformation chain. See `NavierStokesReview/evidence/priority_241_selected_route_identity_2026-10-01.md`.
## Comparator boundary and semantic provenance audit update (2026-10-01)

The review now separates the Comparator challenge specification from the submitted solution. The `sorry` bodies in `ComparatorChallenges/NavierStokes.lean` are challenge placeholders; `NavierStokes/ComparatorSolution.lean` imports the solution theorem modules and contains no `sorry` body in the inspected source. This source distinction is not treated as proof of independence by itself. The exact Comparator configuration, elaborated proof-term closure, and recursive axiom traversal remain required.

The audit also adds a proof-relevant totalisation and witness-provenance lane. Conditional fallback definitions, chart representatives, endpoint extensions, `Classical.choice`, totalised integrals or derivatives, and similar constructions are not labelled unsound merely because they are noncomputable. They are traced to the selected (u,p,f,K) and checked for branch validity, coverage, choice-independence, integrability, and domain preservation.

This matters to the paper claim because kernel validity establishes a formal proposition, not automatically the proposition intended by Fefferman or by the manuscript:

\[
\Gamma\vdash T
\quad\not\Rightarrow\quad
T=\text{the intended PDE/CMI statement}.
\]

The current positive finding remains that the B route carries one coherent selected tuple and the same force through the R³ theorem and comparator. The current unresolved findings remain the selected-field observable transport, Fefferman-to-Comparator class variance, proof-term A/B differential, constructor-field provenance, and high-risk limits/interchanges. No challenge-file `sorry`, `noncomputable` definition, or interface omission is treated as a concrete selected-path contradiction without the corresponding dependency evidence.

Evidence: `NavierStokesReview/evidence/priority_242_comparator_boundary_and_totalization_2026-10-01.md`, `NavierStokesReview/evidence/comparator_trust_totalization_audit_2026-10-01.json`, and `NavierStokesReview/src/audit/comparator_trust_and_totalization_audit.py`.

### Fefferman-to-Comparator variance

The nonexistence transfer requires an asymmetric class inclusion, not merely similar theorem syntax:

\[
\text{Fefferman-admissible competitor}
\Longrightarrow
\text{Comparator competitor}.
\]

The current source trace positively establishes an internal adapter from Comparator solutions to the repository's `GlobalFiniteEnergySolution`, including explicit `MemLp` and energy transport (`NavierStokes/R3/ComparatorBridge.lean:48–70`). That is not the critical reverse inclusion. The review therefore keeps finite-energy integral versus `MemLp`, coordinate versus Fréchet derivative bounds, `derivWithin` and endpoint semantics, pressure gauge, spatial decay, viscosity, and same-force identity open until checked in the required direction.

Evidence: `NavierStokesReview/evidence/priority_243_fefferman_comparator_variance_2026-10-01.md`.
## Object identity and class-transfer control update

The selected September 10 route now has positive source evidence for one
coherent tuple \((u,p,f,K)\) through the R3 theorem and the same-force
comparator bridge. The periodic route begins from the R3 tuple and then applies
compression, `beforeOne`, and periodisation through explicit transport lemmas.
This corrects any description of the production route as unrelated existential
pieces.

That positive result must not be overstated. The object ledger records no
production theorem identifying the final transformed fields with

\[
\mathcal M(u,p,f)=(M,I,J,S,C_p).
\]

The remaining review question is therefore an arrow-level correspondence
question, not a claim that the upstream repair engine is dead or bypassed.
The ledger also separates the literal Lean inclusion already visible in
`globalSolutionOfComparator` from the independent semantic question whether
every Fefferman-admissible competitor lies in the Comparator class. The required
direction, not an assumed equivalence, is:

\[
\text{Fefferman competitor}\Rightarrow\text{Comparator competitor}.
\]

The A/B proof-term differential, constructor-field provenance, and targeted
fallback/choice/totalisation checks are now part of the evidence programme.
CUDA-first three-dimensional cutoff/curl plots remain an independent numerical
diagnostic and are not treated as a proof of the final observable identity.

Evidence: `NavierStokesReview/evidence/priority_241_object_identity_ledger_2026-10-01.md`,
`priority_243_fefferman_comparator_variance_2026-10-01.md`, and
`priority_242_comparator_boundary_and_totalization_2026-10-01.md`.
