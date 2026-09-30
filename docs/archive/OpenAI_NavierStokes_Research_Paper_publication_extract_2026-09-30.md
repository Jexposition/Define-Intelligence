# Selected-field correspondence in the OpenAI Navier–Stokes formalisation

**Independent source-level review and formal audit**
**Jexposition, 26 September 2026**

## How to read this document

This file is the publication-level argument. The source-audit dossier is kept
as a separate evidence record so that a mathematician can inspect the source
declarations, theorem signatures, endpoint traces, counter-probes, and later
corrections without turning the paper into a chronological work log.

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

The separate [Evidence dossier](../NavierStokesReview/evidence/research_paper_evidence_dossier_2026-09-30.md)
supports, qualifies, and records revisions to the main argument. The paper
states the argument in manuscript order; the dossier records provenance and
does not silently change the verdict.

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



## Executive verdict

OpenAI's published claim is **not yet established as an exact CMI/paper
correspondence**, but the reason must be stated correctly. The repository
contains a substantial Lean endpoint with a forced whole-space breakdown
proposition, and the inspected endpoint has standard foundational axiom
dependencies. Raw source tracing also shows that the five-moment and rank
repair machinery is used internally to obtain coefficient matching, finite
Cartesian residual identities, residual estimates, selected physical data,
and candidate properties.

The remaining issue is not that the repair engine is absent. The exported
`selected_witness` does not expose a separate named theorem identifying the
paper's five cumulative quantities

$$
(M,I,J,S,C_p)
$$

with the final Cartesian velocity, pressure, residual, and force used by the
whole-space endpoint. That absence is a packaging and correspondence question,
not evidence that the five-moment engine was bypassed. It becomes adverse
only if a specific paper or CMI condition requires a stronger whole-space
identity than the proved finite-residual and candidate consequences provide.
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
require inspection of definit…6115 tokens truncated…The two clauses have different logical roles. The first is the review verdict:
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

## Evidence dossier

The complete provenance record is maintained separately in [research paper evidence dossier](../NavierStokesReview/evidence/research_paper_evidence_dossier_2026-09-30.md). It is not part of the publication argument.


