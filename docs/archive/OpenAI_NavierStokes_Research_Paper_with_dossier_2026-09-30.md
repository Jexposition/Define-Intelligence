# Selected-field correspondence in the OpenAI Navier–Stokes formalisation

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

- [Companion peer review](../OpenAI_NavierStokes_Peer_Review_v1.md)
- [CMI first-review plan](../OpenAI_NavierStokes_CMI_First_Review_Plan.md)
- [Workspace goal and control rules](../REVIEW_AUDIT_WORKSPACE_GOAL.md)
- [Semantic correspondence map](../SEMANTIC_CORRESPONDENCE_MAP.md)

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

<details>
<summary>Audit control record and dated evidence updates</summary>

The following material is retained for provenance. It is not part of the
publication argument; read the Executive Verdict below for the paper's actual
line of reasoning.

## Audit status and revision record

The following subsections document the current audit state and dated evidence
updates. They are control information for the paper, not additional arguments.

### Live audit state (2026-09-29)

 The authoritative register currently records 2,794 indexed modules, 588
 modules in the captured Navier–Stokes endpoint closure, 906 evidence-inspected
 rows, 1,881 source-indexed rows still queued for semantic review, 0 missing
 project import edges, 10 source rows containing a `sorry` token, and 86
 supplemental evidence records. “Outside the captured endpoint closure” is a
scope label, not a claim that a module is dead or unreachable in OpenAI’s own
build graph. Earlier addenda retain historical tranche counts. The remaining
selected-field composition and full-repository coverage are not yet closed.

### Audit evidence update: Priority 179 force-smoothness rebuttal

The latest rebuttal was checked against the manuscript's explicit residual and
correction passages and the selected Lean force path. The five-moment equations
are load-bearing in the written profile/correction mechanism, but the source
does not establish that they are the only cancellation operation. Nor does
velocity blow-up alone prove termwise divergence of every residual summand.
The selected Lean route derives `force_smooth` from concrete residual
derivative recurrence and locally uniform endpoint limits. The unresolved
publication-level issue remains the final selected-field identification with
the manuscript observables `(M,I,J,S,C_p)`, so the classification remains
**NOT ESTABLISHED (CTR-005)** without asserting a selected mismatch or force
nonsmoothness.

Evidence: `../NavierStokesReview/src/audit/priority_179_latest_force_smoothness_rebuttal_2026-09-29.md`;
`../NavierStokesReview/evidence/source_tranche_priority_179_latest_force_smoothness_rebuttal_2026-09-29.json`.

### Audit evidence update: Priority 154–155 source tranches (2026-09-29)

The latest source reviews and machine-readable evidence are part of the
paper-to-code record:

- [Priority 154: Euler transport, frame, and heat-source review](../../NavierStokesReview/src/audit/priority_154_euler_transport_frame_heat_source_review_2026-09-29.md)
- [Priority 154 machine-readable evidence](../../NavierStokesReview/evidence/source_tranche_euler_transport_frame_heat_2026-09-29.json)
- [Priority 155: Euler Gaussian and Gevrey review](../../NavierStokesReview/src/audit/priority_155_euler_gaussian_gevrey_source_review_2026-09-29.md)
- [Priority 155 machine-readable evidence](../../NavierStokesReview/evidence/source_tranche_euler_gaussian_gevrey_2026-09-29.json)
- [Current semantic coverage register](../../NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-29.md)

The two tranches add positive evidence for conditional Euler transport,
Gaussian heat, composition, continuation, compactness, and flow/Gevrey bounds.
They do not establish the selected Navier–Stokes endpoint or a final Cartesian
transport theorem for `(M,I,J,S,C_p)`. They do not prove a nonzero moment
defect, impossibility, or kernel `False`; the defensible status remains
`CTR-005`: selected-field paper-to-code correspondence not established.

> Audit addendum (2026-09-28): Priority 84 source review found exact positive-axis, radial-heat, release-moment, and torus-average intermediate theorems in the live source tree. These are not treated as proof of the complete selected Cartesian `(M,I,J,S,C_p)` transport. See `NavierStokesReview/src/audit/priority_84_axis_heat_release_torus_source_review_2026-09-28.md`.

> Audit addendum (Priority 85, 2026-09-28): `RepairConeBounds` contains a genuine reduced-profile five-coordinate moment equality and physical five-row/stock transport under explicit chart hypotheses. The review therefore does not claim that five-moment mathematics is absent repository-wide. The open correspondence question is the final composition into the selected Cartesian field and public `Witness`; see `NavierStokesReview/src/audit/priority_85_signed_geometry_repair_cone_source_review_2026-09-28.md`.

> Audit addendum (Priority 86, 2026-09-28): `BaseRankPatch.five_rows` supplies a direct local `FiveRowRank.FiveRows` theorem for the full final base, with accompanying cycle-induction, rank-state, compensation, and mean-stage results. These local bridges are not treated as the final whole-space selected-Cartesian composition. See `NavierStokesReview/src/audit/priority_86_rank_cycle_compensation_source_review_2026-09-28.md`.

### Historical source-tier snapshot: primary bounds, slow-axis, moving moments, and pressure tests

The next four inspections cover `ActualPrimaryBounds.lean`,
`ActualSlowAxis.lean`, `MovingMomentBounds.lean`, and
`R3/PressureTestBounds.lean`. They add native velocity/pressure jet and
periodised copy-sum bounds, reduced slow-axis and axis-jet identities,
moving-strip pressure-mass/radial-moment class bounds, rank-stage support
closure, and Fourier/H3/Riesz-test estimates for comparative pressure recovery.

These are concrete intermediate results. They do not prove the final selected
Cartesian field's `(M,I,J,S,C_p)` after the complete sum/curl/localisation,
periodisation, torus-average, radial-pullback, support/integrability, and axis
route. Comparative pressure-test estimates are not an absolute selected
pressure-Poisson representative. No impossibility theorem or kernel `False`
was obtained. The live register now contains 93 explicit source reviews and
505 reachable modules awaiting semantic classification.

### Historical source-tier snapshot: R3 breakdown, primary coherence, mean bounds, and signed waves

The next source pass inspected `R3/CandidateBreakdown.lean`,
`ActualPrimaryCoherence.lean`, `MeanMomentBounds.lean`, and
`PhysicalSignedWave.lean`. The R3 module proves the formal no-global-competitor
consequence and a uniform (L^2) square bound. The primary-coherence module
proves positive-radius global potential representations, periodicity,
smoothness, axis-zero germs, and component-level Cartesian-curl identities.
The mean-bound module proves torus-average, radial-weight, pressure-mass, and
radial-moment class identities. The signed-wave module proves concrete
potential, cutoff, pressure, periodicity, smoothness, and Cartesian-curl
identities for wave and primary components.

These are substantive intermediate results. They do not prove the final
selected `ASum`/`BSum`/`PSum` field's `(M,I,J,S,C_p)` after the complete
sum/curl/localisation/periodisation/torus-average/radial-pullback,
support/integrability, and axis route. A cutoff-gradient commutator remains a
term to evaluate, not a proved nonzero defect. No impossibility theorem or
kernel `False` was obtained. The live register now contains 89 explicit source
reviews and 509 reachable modules awaiting semantic classification.

</details>

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

The accompanying [`SEMANTIC_CORRESPONDENCE_MAP.md`](../SEMANTIC_CORRESPONDENCE_MAP.md)
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
[`REVIEW_DOCUMENT_CONTROL.md`](../REVIEW_DOCUMENT_CONTROL.md). The evidence
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
[`SelectedResidualLowerBoundObstructionProbe.lean`](../../NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean)
proves exactly this conditional contradiction on the actual one-sided
endpoint filter.

The selected-path extraction and the zero residual limit are recorded in
[`SelectedWitnessEndpointResidualProbe.lean`](../../NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean).

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
[`SelectedWitnessAttackBoundaryProbe.lean`](../../NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean)
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
endpoint moment transport obstruction](../../NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md),
the [selected moment transport source trace](../../NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md),
the [full selected transport audit](../../NavierStokesReview/evidence/selected_transport_audit_full_2026-09-28.md),
and the [load-bearing paper dependency matrix](../../NavierStokesReview/evidence/paper_moment_dependency_matrix_2026-09-29.md).

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
[`PressureResidualNonCancellationProbe.lean`](../../NavierStokesReview/src/probes/PressureResidualNonCancellationProbe.lean)
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
[`cmi_force_independence_adjudication_2026-09-24.md`](../../NavierStokesReview/evidence/cmi_force_independence_adjudication_2026-09-24.md).

The fixed-data test makes this objection mathematically sharper. Let (e) be
an independently chosen smooth perturbation, keep (p) and the spacetime
force (f) fixed, and require both (u) and (u+e) to satisfy the same
residual equation. The compiled theorem
[`IndependentDataPerturbationProbe.lean`](../../NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean)
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
[`independent_data_perturbation_2026-09-24.md`](../../NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md).

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
[`same_datum_fixed_force_obstruction_2026-09-24.md`](../../NavierStokesReview/evidence/same_datum_fixed_force_obstruction_2026-09-24.md).

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
   mathematics, and raw source tracing shows that it feeds coefficient
   matching, finite Cartesian residual identities, residual estimates, and
   selected candidate data. The public `Witness` does not repeat the named
   profile tuple as a field, but that packaging fact is not evidence that the
   repair engine was bypassed.
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
7. [`SelectedResidualLowerBoundObstructionProbe.lean`](../../NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean).
8. [`SelectedWitnessAttackBoundaryProbe.lean`](../../NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean).
9. [`FiveRowPositiveOrderBridgeProbe.lean`](../../NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean).
10. [`PressureRecoveryAbsolutePremiseProbe.lean`](../../NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean).

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

The material below is a preserved source and audit dossier. It is deliberately
not deleted or compressed: its purpose is to retain the declarations, source
paths, tranche reviews, calculations, probe results, corrections, and unresolved
questions needed for reproducibility. It should be read after the main
manuscript and appendices, not as a chronological substitute for them.

Each dossier section has one of four roles:

- **positive source evidence**, showing what the formalisation genuinely proves;
- **correspondence analysis**, testing whether those results reach the advertised
  selected Cartesian field;
- **semantic analysis**, comparing the endpoint with the CMI and paper-level
  interpretation; or
- **open calculation**, recording a test that has not yet yielded a theorem.

The dossier therefore preserves important work without inflating an open
calculation into a refutation. In particular, the current classification
remains `CTR-005` / selected-field paper-to-code correspondence not
established. A nonzero commutator defect, an impossibility theorem, or a kernel
derivation of `False` would require its own direct evidence and would be
recorded as a status change rather than inferred from this heading.

### Dossier navigation

| Evidence lane | What it is for |
|---|---|
| Global germ and endpoint transport | Records the positive selected-path chain and its exact packaging boundary. |
| Moment, rank, and localisation analyses | Separates reduced-profile certificates from final Cartesian transport. |
| Pressure and force provenance | Separates comparative pressure results and residual-designed forcing from stronger semantic claims. |
| Euler companion audits | Keeps the Euler interval and Gaussian/Gevrey analyses separate from the Navier–Stokes endpoint. |
| Repository coverage and source tranches | Records which source files were inspected, what was found, and what remains open. |

### Figures and tables for the paper version

The publication version should render, rather than merely mention, the
following reader-facing objects. They are explanatory figures, not evidence
seals:

1. **Figure 1: Three-layer correspondence map.** Fefferman's CMI target,
   OpenAI's paper mechanism, and the Lean endpoint, with each claimed bridge
   labelled `proved`, `partially proved`, or `not established`.
2. **Figure 2: Selected-field pipeline.** Reduced profile certificates,
   potential lift, curl, localisation, series summation, periodisation,
   torus-average/radial pullback, and the public `Witness` boundary.
3. **Figure 3: Force provenance.** The forward Cauchy direction
   `(u_0,f) -> (u,p)` beside the residual construction `(u,p) -> f`.
4. **Figure 4: Coverage and evidence map.** Endpoint closure versus the
   repository-wide inventory, without using “unreachable” as a synonym for
   dead code.
5. **Table 1: Claim-status matrix.** CTR-005, CTR-012, pressure semantics,
   axiom hygiene, and the retracted objections.
6. **Table 2: Source-to-claim register.** Each load-bearing paper assertion,
   its Lean declarations, the exact transport theorem required, and its current
   evidence status.

No toy numerical scan is presented as proof of the selected Lean field. Any
future plot must identify its exact field-level input, discretisation,
convergence checks, and the proposition it can and cannot support.

## Global germ transport: what the source does and does not connect

The selected construction contains a genuine transport chain before the final
existential envelope. `ActualCyclePreservation.state_runInvariant`
(`ActualCyclePreservation.lean:826-848`) inducts the actual cycle state;
`state_particularData`, `state_waveData`, and `state_wave_transport`
(`850-912`) provide the analytic and wave data consumed by
`ActualCycleCoherence.mean_input_of_transport`
(`ActualCycleCoherence.lean:803-820`). The native stream, angular, and pressure
stages are defined in `ActualCandidateConstruction.lean:392-404,464-502`, and
the assembly proves local chart equalities in
`ActualCandidateAssembly.lean:392-424`. `physicalData`, `estimates`, and
`endpoints` then consume these actual objects at
`ActualCandidateAssembly.lean:1079-1115`.

That positive chain matters. It prevents a fair review from describing the
formalisation as a collection of unrelated declarations. The unresolved issue
is more exact: the exported `Witness`
(`ActualCandidateAssembly.lean:1121-1151`) does not contain a theorem
identifying its selected mixed velocity, pressure, residual, or force with
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or the paper's $(M,I,J,S,C_p)$ quantities. The source
therefore proves substantial global germ transport while leaving the paper's
semantic five-moment identification unexported.

The review-side theorem in `GlobalTransportBridgeProbe.lean` sharpens the same
boundary. It pairs the selected candidate's full `Consequences` bundle with a
zero-sorry failure of a fixed-force, same-initial-datum perturbation predicate.
This establishes path dependence of the residual-designed trajectory. It is not
a contradiction of the literal C/D existential, which asks for one admissible
force and one trajectory and does not quantify over perturbations.

The endpoint's blow-up conclusion must be stated precisely. The selected proof
does prove a formal blow-up predicate: `GermCandidateAssembly.origin_blowup`
(`GermCandidateAssembly.lean:146-159`) transports the origin asymptotic to the
mixed field, and `FinalSlowBase.axis_tendsto`
(`FinalSlowBase.lean:372-378`) derives the base-axis divergence from the leading
profile. That local axis-limit route does not require its own type to repeat a
five-moment tuple. It does **not** show that the paper's restoration mechanism
can be removed from the selected construction. The full selected proof term
genuinely uses moment and rank machinery upstream through `estimates`,
`physicalData`, profile repair, primitive cancellation, and five-row
constructions. Thus the review is not claiming that the endpoint is empty or
that its blow-up predicate was proved independently of the construction.

The unresolved issue is instead an exact identity question. The current source
record does not expose a theorem identifying the completed selected mixed
Cartesian velocity, pressure, residual, and force with the paper's five global
observables. The endpoint therefore proves a formal C/D-shaped candidate while
leaving the paper's claimed five-moment interpretation unestablished at the
final field boundary. This does not prove that the selected integrals are
false; it means that a concrete field-level mismatch, impossibility theorem, or
false mandatory premise would still be needed for a kernel-level refutation.

The corrected counter-paper conclusion is consequently a failed
paper-to-endpoint identification on the current record, not a claim that the
selected blow-up proposition has no proof. The distinction is documented in
`NavierStokesReview/evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md`.

The direct operator-level source trace is separately recorded in
`NavierStokesReview/evidence/selected_field_operator_trace_2026-09-29.md`.
It confirms the selected sum, curl, cutoff, periodisation, and observable
interfaces without treating the explicit cutoff commutator as a proved global
moment defect.

## Burden of proof and the underclaim finding

The review must distinguish the proposition that the Lean endpoint exports from
the proposition OpenAI's paper asks readers to accept. The endpoint is not an
empty wrapper: `ActualCandidateAssembly.Witness` packages smoothness, support,
zero initial data, incompressibility, residual equality, the relevant energy and
blow-up consequences, and the force-jet extension. The comparator modules carry
those predicates into the formal C/D-shaped conclusions.

The paper, however, gives the five named moments `(M,I,J,S,C_p)` a load-bearing
role in the explanation of the construction. `PositiveOrderMoments` and
`FiveProfileMoments` define genuine five-coordinate objects, while
`FiveRowRank` operates through a constrained three-debt interface. The review
has proved a local promotion theorem for those interfaces, but has not found a
theorem identifying the selected final mixed fields and residual with the
paper's five named quantities. That is the unresolved correspondence required
to support the paper's central solution interpretation.

This places the burden where it belongs. A reviewer need not prove that every
smooth force is harmless, or that the literal existential C/D proposition is
false, before declining to accept a paper whose central construction has not
been transported into its exported endpoint. The primary conclusion is
therefore: the public five-moment solution claim is **not established** by the
source as presently exposed. The literal endpoint is materially populated,
but that narrower fact does not establish the published solution claim. A
`False` theorem would be a separate, stronger
result, not a prerequisite for this conclusion.

Evidence: `NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.

## Publication decision on the advertised solution claim

The relevant review decision is not a vote on whether Lean can type-check the
exported endpoint. It is whether the inspected record establishes the claim
that OpenAI presents to readers: that the selected five-moment construction is
the construction proving a CMI Navier–Stokes alternative. On that question the
burden is asymmetric. The review may reject the advertised solution claim
because the inspected source record does not establish the selected-field
composition and transport. The reviewer does not have to prove the negation of
the literal existential endpoint before making that adverse finding.

The correct publication conclusion is therefore **do not accept the published
CMI-solution claim on the inspected record**. The reason is affirmative and
source-based: the exported witness does not identify its selected mixed fields
with the paper's $(M,I,J,S,C_p)$ tuple, nor does it expose the theorem carrying
that identity through the correction, germ, residual, and force construction.
The phrase **not formally refuted** remains a narrower statement about the
separate search for a selected-path `False` theorem. It cannot be read as
evidence that the missing composition theorem is true.

## The selected physical-data interface

The selected construction does contain a genuine local-to-global assembly.
`PhysicalData` records the smooth velocity and pressure fields, their germs,
and their exterior agreement; the residual endpoint consumes those data to
obtain the jet estimates used by the force construction. The review therefore
does not treat the upstream five-moment modules as dead code and does not
claim that the exported endpoint is empty.

The unresolved issue is more precise. The selected `PhysicalData` record and
the exported `Witness` do not state that the final mixed fields realise the
five quantities

$$
(M,I,J,S,C_p).
$$

The source defines genuine five-coordinate moments upstream, but the review
has not located a theorem transporting those integrals through the selected
mixed velocity, pressure, residual, and force. The zero-sorry interface probe
shows that the selected physical-data record can coexist with an arbitrary
nonzero abstract five-debt parameter because that parameter is not part of the
record's contract.

This is an affirmative underclaim finding. It is enough to conclude that the
paper's five-moment solution explanation is **NOT ESTABLISHED** by the
exported endpoint. It is not, by itself, a proof that the actual selected
integrals are wrong; that stronger result requires a field-level identity and
then a proved mismatch.

Evidence: `NavierStokesReview/evidence/selected_physical_data_moment_interface_2026-09-24.md`.

### A selected-witness non-implication

The stronger endpoint test has now been made against the actual selected
`Witness`, not only against `PhysicalData`. The extension
`SelectedEndpointMomentTransportObstruction.lean` proves, without an
admission, that

$$
\exists d : \mathrm{Debt}_5,
\quad d \ne 0
\quad\land\quad
\mathrm{Witness}_{\mathrm{selected}}.
$$

Here the nonzero payload is an explicit constant function on `Fin 5`, while
the witness is the repository's own `selected_witness`. The result is not a
claim that this abstract payload equals the selected physical integrals. It
proves the exact limitation of the exported proposition: the witness carries
no five-coordinate payload and therefore cannot, by its type alone, certify
the paper's moment identities.

This matters because the paper treats those identities as part of the
solution mechanism, not as optional explanatory notation. The required
theorem must identify the actual selected mixed velocity and pressure fields,
transport their five integrals through the residual and force construction,
and connect them to the endpoint used to claim breakdown. That theorem is
still absent from the inspected export. The counter-paper therefore rejects
the advertised solution claim as **NOT ESTABLISHED**, while keeping the
separate and narrower statement that no selected-path `False` theorem has yet
been derived.

Evidence: `NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md`.

## The published claim and the selected-field burden

The question under review is the claim that this repository supplies a
solution of the Navier–Stokes problem. It is not enough that the source tree
contains a five-moment library or that an upstream slow-profile theorem
compiles. The paper uses the five quantities
$$
(M,I,J,S,C_p)
$$
to justify tail cancellation and preservation of the exterior field. The
selected candidate must therefore export the identities for the actual mixed
velocity and pressure fields used in the final residual and force.

The source trace establishes the positive part: `PositiveOrderMoments.lean:76-85`
defines the five rows, `GlobalSlowProfiles.lean:1043-1055` proves their
positive-order cancellation, and `AssembledSlowBase.lean:592-617` uses that
result. The unresolved issue is the selected-field transport step. The mixed
fields are assembled at `ActualCandidateAssembly.lean:515-523`, while the
`Witness` export at `1121-1151` contains no equality identifying those fields'
integrals with the paper tuple.

This is a direct burden-of-proof failure in the advertised solution claim.
The appropriate conclusion is **NOT ESTABLISHED**, not because the five-row
library is absent, but because its connection to the claimed final solution is
not stated or proved at the exported endpoint. A separate Lean `False` result
would strengthen the paper; it is not required to reject an affirmative claim
whose load-bearing construction remains unconnected.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.

## Claim-level reconciliation: what the source does and does not establish

The review has now compared the exported R³ theorem with the exact CMI target,
rather than treating the periodic assembly interface as the whole claim. This
changes the wording of the conclusion.

`NavierStokes/R3/ProblemStatement.lean` defines the whole-space candidate with
the relevant requirements: a smooth force of compact positive-time support,
smooth pre-singular velocity and pressure, incompressibility, the residual
equation, zero initial velocity, uniformly bounded kinetic energy, and
unbounded speed near time one. `NavierStokes/R3/Theorem.lean:27-53` then
exports `breakdownStatement` for every positive viscosity. The selected chain
is therefore not merely a type-erased periodic wrapper.

The force-provenance objection must also be stated accurately. The CMI
statement specifies a given externally applied force, but its C/D alternatives
are existential statements about a smooth force satisfying the stated decay
conditions. The published paper itself says that, for a chosen incompressible
flow and pressure, the residual can be called the force, and identifies smooth
extension of that residual as the construction problem. A perturbation or
mirror-force theorem changes the force or the trajectory; it does not
contradict the original existential witness.

The strongest supported conclusion is consequently split:

1. The inspected R³ source does state and prove the literal C/D-shaped theorem,
   with the exported theorem depending only on Lean's standard foundational
   axioms.
2. The paper's five-moment explanation remains under-identified at the final
   interface. The selected export at `ActualCandidateAssembly.lean:1121-1151`
   does not expose an equality transporting the paper tuple
   $$
   (M,I,J,S,C_p)
   $$
   into the final mixed velocity, pressure, residual, and force.
3. That missing composition theorem is a publication-level correspondence
   defect if the five-moment mechanism is presented as the proof's load-bearing
   justification. It is not, by itself, a formal contradiction of the literal
   C/D theorem.

This is the correct burden-of-proof position. OpenAI must make the advertised
paper mechanism traceable to the selected fields. The review must not claim
that the C/D theorem has been falsified unless a concrete selected-field
premise is contradicted or a zero-sorry `False` theorem is obtained.

Evidence: `NavierStokesReview/evidence/cmi_target_and_claim_level_reconciliation_2026-09-25.md`.

## Repository-wide admission census

The release record also does not support a blanket claim that the repository
is zero-sorry. `ComparatorChallenges/NavierStokes.lean:273-284` contains two
Navier–Stokes challenge declarations whose theorem bodies are `by sorry`, and
`ComparatorChallenges/Euler.lean:85-88,181-184` contains further admitted
challenge declarations. `lakefile.toml` includes `ComparatorChallenges` in its
default targets. These admissions are not evidence that the selected
`NavierStokes/R3` endpoint imports them, so they are not being misreported as a
refutation of that endpoint. They are, however, a direct failure of any
repository-wide zero-sorry release claim and a reproducibility defect in the
published proof record. Evidence:
`NavierStokesReview/evidence/repository_admission_census_2026-09-25.md`.

The source census has now been reproduced by Lean rather than inferred only
from text search. A review-side audit module reports `sorryAx` in the axiom
dependencies of all four standalone challenge declarations. This makes the
release-level objection independently reproducible. It does not contaminate
the selected R³ dependency report, which uses the independent comparator
definitions; the paper therefore treats it as a separate integrity defect,
not as a substitute for the unresolved selected-field contradiction.

Evidence: `NavierStokesReview/evidence/repository_admission_axiom_log_2026-09-25.md`.

## Remaining field-level calculation

The next question is not whether the repository contains five-moment
definitions. It does. The question is whether the moments used in the paper are
the moments of the selected fields exported by the theorem.

The selected velocity is assembled as a natural-indexed sum of cut stages. The
source path runs from `SolenoidalDiagonal.potentialSum`, through the spatial
curl and the Cartesian chart construction, into cylindrical components and
finally into the radial/toroidal `barMoment` interface. `FiveRows` then imposes
zero identities on correction profiles. Those are meaningful upstream facts,
but they are not automatically identities for the total selected field.

This leaves a precise possible refutation. One must compute the finite-prefix
and tail contributions, retain derivatives of every localisation mask, account
for axis and far-field boundary terms, and exhibit an exact nonzero remainder
that the selected field is required to have while the correction invariant
requires zero. A symbolic helper has been added for the five profile integrals,
but it is intentionally not treated as proof: it becomes evidence only when a
Lean theorem identifies its input expressions with the selected Cartesian
field. Until that calculation is completed, the five-moment objection is a
failure to establish the advertised mechanism, not an assertion that the
selected physical integral is false.

## Companion Euler interval audit

The companion Euler construction was checked as a separate claim. Its source
proves positive interval widths, controlled contraction, positive common
horizons, and value plus first-derivative matching at the inspected seams. The
source therefore does not support the proposed first-order temporal jump or a
quiet Zeno endpoint. An all-order time-jet matching theorem across every seam
has not been identified and remains a legitimate review question. It should be
resolved by an explicit higher-order mismatch, not inferred from the existence
of discrete parent and child stages.

These two results sharpen the burden of proof. The advertised work is still
**NOT ESTABLISHED** as a complete solution record because the selected-field
five-moment composition is not exposed. The literal whole-space C/D endpoint
is not called formally refuted without a concrete selected-field contradiction.

## Selected-field calculation gate

The source trace has now been pushed to the point where a genuine numerical
objection could be made. The selected stage fields are not empty placeholders:
`ActualCandidateConstruction` supplies the initial and positive fields,
`DirectAngularDiagonal` supplies the cylindrical angular component and its
cutoff multiplication, and `ActualMeanPotentialRealization` supplies the
Cartesian embedding and curl identities. `SolenoidalDiagonal.potentialSum`
then assembles the local finite portions of the cut-stage series.

The remaining calculation is exact rather than rhetorical. The derivatives of
the localisation masks must be retained, the positive-radius chart must be
transported through the curl, and the axis and outer-support terms must be
evaluated before `barMoment_apply` can be used. That operator integrates a
scalar radial profile after torus averaging; it does not itself identify a
Cartesian selected velocity with a radial profile. The inspected source still
contains no theorem performing that identification.

Accordingly, no nonzero selected remainder is asserted here. The symbolic
integral helper is a reproducible calculator for an explicitly supplied
profile, not evidence that the profile came from the selected `tsum`. A
kernel contradiction requires both a Lean equality for the selected field and
a proved value such as `Delta m ≠ 0`. This is the live route for testing the
affirmative paper claim, while the present publication verdict remains
**NOT ESTABLISHED** rather than a fabricated `False` theorem.

The companion Euler interval study remains separate. Positive interval
geometry and value/first-derivative seam matching are source-supported; a
quiet Zeno endpoint and an all-order time-jet mismatch remain unproved.

## Selected series and the remaining moment calculation

The review has now followed the selected potential series into a concrete
finite-prefix theorem. The selected schedule is supplied by
`ActualCandidateAssembly.selected_witness`. At every positive preterminal
point, `SolenoidalDiagonal.potentialSum` is locally equal to a finite sum of
the selected stages, and the same finite sum represents every iterated Frechet
jet. This rules out an empty-limit explanation for the selected field.

The result also makes the unresolved endpoint precise. The selected field is built
as a Cartesian velocity from localised potentials and spatial curls. The
paper's five moments, however, are consumed through a scalar radial profile
and torus average in `DefectIncrementBounds.barMoment`. The nominal profile
module proves an explicit five-coordinate formula for its own ideal profiles;
the source does not identify that formula with the selected Cartesian sum.

The next calculation must therefore retain cutoff derivatives, carry the curl
through the positive-radius cylindrical chart, and evaluate the axis and
outer-support terms before applying `barMoment_apply`. If those exact terms
produce a nonzero selected remainder, it can be combined with the zero-row
correction invariant in a zero-sorry contradiction. At present no such
selected `Delta m` has been proved. The honest conclusion is stronger than a
generic missing-bridge complaint but narrower than a formal disproof: the
published five-moment solution claim remains **NOT ESTABLISHED** until this
selected-field calculation is supplied.

Evidence:
`NavierStokesReview/evidence/selected_field_finite_prefix_transport_2026-09-25.md`.

## A selected-field calculation, not a generic objection

The counter-paper now contains a zero-sorry completion that follows the
actual selected direct fields through one concrete layer of the construction.
`selectedDirectStages` is identified with the source's
`angularMeanStages`, and every uncut finite prefix is identified with the
corresponding selected cycle-state mean angular field. Thus the review does
not rely on the claim that the upstream five-moment machinery is dead code or
that the selected series is an empty limit.

The remaining issue is analytical and exact. The direct field is multiplied
by smooth localisation cutoffs, the meridional pieces are embedded into
Cartesian potentials and curled, and the final endpoint consumes a Cartesian
velocity. The paper's Appendix A moments are instead scalar radial profile
integrals after torus averaging. The inspected source does not provide the
selected equality between these objects. A valid counterexample would now be
a computed nonzero remainder after the cutoff derivatives, curl terms, and
axis and outer-support terms are included. Until that calculation is proved in
Lean, this paper makes no unsupported claim that `Delta m ≠ 0` or that the
selected witness yields `False`.

The source-backed result is therefore a strengthened publication objection:
the advertised solution remains **NOT ESTABLISHED** because the inspected
record does not establish the selected Cartesian-to-radial transport theorem
or its numerical or symbolic consequences. This is an adverse conclusion, not
an invitation to treat the claim as pending repair.

Evidence: `NavierStokesReview/evidence/selected_direct_prefix_field_2026-09-25.md`.

## A necessary correction: stage mass preservation is source-supported

The review has now checked the active selected recurrence against the source's
preservation theorem. `SelectedCycleMasses.lean` proves that every selected
cycle state carries the explicit `ZeroMassesOn` invariant. Thus the claim that
the two zero correction rows automatically create a stage-level mass leak is
not supported by the code and is not used here.

This does not settle the published five-moment claim. The invariant is stated
for the correction state's mean profiles; the exported selected direct prefix
is a Cartesian velocity assembled from a scalar coefficient, angular frame,
localisation, and curl. The paper's Appendix A requires the resulting field
to have the corresponding radial moments. That requires an explicit selected
Cartesian-to-radial calculation, including cutoff derivatives and axis and
tail terms. The advertised solution therefore remains **NOT ESTABLISHED** on
the current record; no `Delta m ≠ 0` or kernel `False` is asserted.

Evidence: `NavierStokesReview/evidence/selected_cycle_mass_preservation_2026-09-25.md`.

## Selected angular component exposed

The review has now exposed component one of the selected angular field as the
physical-atlas scalar coefficient times the corresponding component of the
totalised angular frame. This is a concrete selected-field formula and gives
the radial calculation an actual input expression.

It is not yet a contradiction. The coefficient remains defined through the
atlas and radial projection, and the advertised moment requires the complete
cutoff, curl, torus-average, axis, and tail calculation. The paper's claim is
therefore still **NOT ESTABLISHED** pending that selected transport theorem;
no `Delta m ≠ 0` or kernel `False` is claimed from the component identity
alone.

Evidence: `NavierStokesReview/evidence/selected_angular_component_formula_2026-09-25.md`.

## Selected direct stages are chart-realised off the axis

The source audit now proves that the selected direct stage is not an arbitrary
placeholder. On the explicit positive-radius chart hypotheses,
`selected_direct_stage_eq_chart` identifies it with the source's
`chartDirectStages`. This follows the selected stage through the atlas rather
than relying on the generic existential envelope.

That result also fixes the remaining mathematical burden. The chart identity
does not cross the axis and does not expand the Cartesian curl. The paper's
five cumulative quantities are scalar radial quantities, whereas the exported
selected stage remains a vector field assembled through the angular frame,
localisation, curl, and torus averaging. Until those operations are connected
by an explicit selected theorem, the review cannot claim a numerical remainder
or a contradiction. The published solution claim remains **NOT ESTABLISHED**.

Evidence: `NavierStokesReview/evidence/selected_direct_chart_transport_2026-09-25.md`.

## Positive-radius recovery and the remaining radial calculation

The selected-field audit now proves an exact positive-radius recovery formula:
the atlas scalar coefficient of the selected angular field is recovered from
one Cartesian component after division by the corresponding angular-frame
coordinate. The proof also derives that the Cartesian radius is nonzero under
the chart hypothesis. This makes the remaining calculation concrete and
locates the axis as an explicit boundary, rather than treating the selected
field as a generic existential object.

The result is not itself a refutation. The selected construction still applies
localisation before the natural-indexed sum and then takes a Cartesian spatial
curl. The paper's five quantities are computed by a scalar radial profile after
torus averaging. A complete review therefore has to retain the cutoff
commutator, curl and connection terms, axis and outer-support contributions,
and integrability hypotheses before evaluating `barMoment`. No selected
nonzero remainder or kernel contradiction has yet been proved, so the
published solution claim remains **NOT ESTABLISHED**.

Evidence: `NavierStokesReview/evidence/selected_cartesian_radial_gate_2026-09-25.md`.

## Cutoff derivatives are part of the selected field

The field-level audit now proves an exact identity that the published
five-moment argument must address. If a potential is localised by a smooth
scalar cutoff `χ`, then

$$
\mathrm{curl}(\chi A)
=\chi\mathrm{curl}(A)
+\mathrm{curlLinear}\big((D\chi).\mathrm{smulRight}(A)\big).
$$

The second term is the spatial commutator created by the localisation mask.
It is not removed merely by smoothness, compact support, divergence-freeness,
or local finite-sum reduction. Since the repository cuts stages before
forming the potential sum and curls the resulting sum afterward, the term must
be carried through the positive-radius chart, torus average, axis and
outer-support limits, and finally `barMoment`.

This strengthens the affirmative burden without overstating the result. The
review has not yet proved that the selected commutator has a nonzero radial
moment, so it does not claim `Delta m ≠ 0` or `False`. The published solution
claim remains **NOT ESTABLISHED** on the current formal record because the
complete selected-field calculation is absent from the exported evidence.

Evidence: `NavierStokesReview/evidence/selected_cutoff_curl_commutator_2026-09-25.md`.

The review also records a CUDA refinement calculation on an explicitly
declared three-dimensional diagnostic profile. Its signed defect is stable
over 129/193/257/321-point volumes, whereas the independent finite-difference
curl and divergence errors decrease but remain nonzero. This supports the
existence of a numerical profile-level mechanism only; it is not the selected
Lean `tsum` field and does not establish `Delta m \ne 0` for the endpoint.
Evidence: `NavierStokesReview/evidence/cutoff_commutator_resolution_audit_2026-09-29.md`.

## A precise remaining calculation

The selected support estimates and the spatial cutoff are not interchangeable.
The support estimates constrain a similarity radius by

$$r(w)\leq C\sqrt{q(w)},$$

whereas the cutoff is identically one only under the Cartesian inequalities

$$x_0^2+x_1^2<\frac1{32},\qquad |x_2|<\frac18.$$

The current source record does not transport the former condition into the
latter for the selected production stages. Therefore the published
order-two moment cancellation for the uncut direct profile cannot be used as
the value of the cutoff-weighted production moment. The remaining calculation
must retain the cutoff, its torus average, and its axis and outer-support
terms. This is a concrete CTR-005 burden of proof, not yet a proof that the
weighted moment is nonzero.

Evidence: `NavierStokesReview/evidence/selected_support_plateau_gate_2026-09-25.md`.

## The scalar-moment interface is a separate theorem

The paper's five-moment narrative uses radial scalar profiles, whereas the
selected endpoint exports a Cartesian velocity field assembled from potential
and direct branches. These are not interchangeable by notation alone. The
definition of `barMoment` requires a scalar family on
`PressureStream.Lift P`; it then averages the two auxiliary coordinates before
integrating in the radial variable.

The review completion
`NavierStokesReview/src/completions/SelectedBarMomentInterface.lean` makes the
required transport theorem explicit. Given a map

$$
\phi : \operatorname{Point}(P) \to \operatorname{SpaceTime}
$$

and a scalar identification

$$
g_j(q)=\bigl(u_j(\phi(q))\bigr)_1,
$$

it proves

$$
\operatorname{barMoment}_k(g_j)(n,p)
= \int r^k\,\operatorname{torusAverage}
  \bigl(q\mapsto (u_j(\phi(q)))_1\bigr)(r,p)\,dr.
$$

This is a formal interface expansion, not the missing physical conclusion.
The selected endpoint still needs a source-level identification of `φ`, the
scalar profile, the production `tsum`, the axis and outer-support limits, and
the resulting numerical moment. Until those steps are proved, the published
five-moment solution claim remains **NOT ESTABLISHED**. No nonzero remainder and
no `False` theorem is asserted here.

Evidence: `NavierStokesReview/evidence/selected_barMoment_interface_2026-09-25.md`.

## A selected positive-stage component calculation

The source audit has now transported one component of the actual selected
positive-potential stage into the production chart.  For every valid chart
point of positive radius and every successor stage, the review completion
`SelectedPotentialChartComponent.lean` proves

$$
\bigl(\operatorname{curl}(A_{j+1})\bigr)_1
 = \bigl(\operatorname{chartWaveParts}_{j+1}\bigr)_1
   + \bigl(\operatorname{chartStreamParts}_{j+1}\bigr)_1.
$$

This closes a genuine field-level transport step.  It also narrows the
remaining objection: the selected wave and stream terms are present in the
production component, so the next calculation must carry both terms through
the scalar radial projection, torus average, cutoff commutator, and boundary
limits.  The theorem does not yet evaluate `barMoment`, prove a nonzero
remainder, or derive `False`.

Evidence: `NavierStokesReview/evidence/selected_potential_chart_component_2026-09-25.md`.

The first Cartesian component is also explicit. The commutator contributes

$$
\bigl((\nabla\chi)\times A\bigr)_0
  =(D_1\chi)A_2-(D_2\chi)A_1.
$$

The published construction therefore cannot pass from the cut-stage chart
formula to a scalar radial moment by dropping this term. The present result
identifies the integrand that must be transported; it does not yet establish
its integral's sign or non-vanishing.

## Positive-radius recovery and the axis obligation

The selected angular field can now be followed onto an actual radial section.
For positive radius, the first Cartesian component recovers the scalar
coefficient used in the field construction:

$$
u_1\bigl(t,(r,0,z)\bigr)=a(t,r,z),\qquad r>0.
$$

This is a concrete selected-field identity, but it also fixes the boundary
condition that the paper-to-code calculation must address. The source
totalises the angular frame to zero on the axis, so the positive-radius
formula cannot be extended by division at `r=0`. The complete moment transport
must combine the off-axis recovery with the axis extension, the cutoff-curl
commutator, torus averaging, and the outer support boundary.

The result strengthens the counter-paper's burden-of-proof argument without
claiming a mismatch that has not been calculated. No selected `Delta m ≠ 0`
or `False` theorem follows yet; the published solution claim remains
**NOT ESTABLISHED** pending the complete selected-field integral identity.

Evidence: `NavierStokesReview/evidence/selected_radial_section_component_2026-09-25.md`.

### Axis value of the selected angular branch

The radial calculation now has an exact boundary value. Let (w=(t,x)) be a
space-time point with (x_1=x_2=0). The review-side theorem unfolds the
production angular frame and proves

$$
\bigl(u^{\mathrm{direct}}_j(t,x)\bigr)_1=0
\qquad\text{when }x_1=x_2=0.
$$

For (r>0), the preceding theorem recovers the scalar coefficient instead.
Thus the selected calculation is piecewise in its source representation:
positive-radius coefficient recovery and an explicitly totalised zero axis
branch. A complete counterexample would still require evaluating the
curl-generated mixed field against the radial operator on both branches,
including the cutoff-gradient commutator and boundary terms. The axis theorem
therefore closes a definitional ambiguity but does not itself prove a nonzero
remainder or `False`.

Evidence: `NavierStokesReview/evidence/selected_radial_axis_boundary_2026-09-25.md`.

## Production order of the selected velocity

The field-level calculation requires one further distinction. The source does
not define the selected velocity as a single curl of a combined potential.
`MixedDiagonalResidual.velocity` and its periodic wrapper use the order

$$
u_{\mathrm{selected}}
=\mathrm{curl}\!\left(\sum_j\chi_j A_j\right)
 +\sum_j\chi_j B_j,
$$

where the second term is the direct angular branch. The periodic construction
then localises and periodises the potential and direct branches separately.
Therefore the identity

$$
\nabla\times(\chi A)=\chi(\nabla\times A)+(\nabla\chi)\times A
$$

is load-bearing for the potential branch, but does not automatically describe
the direct branch. Any paper-to-code disproof must calculate both branches
before claiming a nonzero radial remainder. This source result corrects the
stronger one-curl model without weakening the central conclusion: the
published solution claim remains **NOT ESTABLISHED** until the full selected
Cartesian-to-radial transport is supplied.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

## Direct stage moments and the remaining transport problem

A further source-level completion now isolates one part of the selected
construction rather than treating the internal correction invariant as if it
already applied to the exported field. The selected native angular stages are
defined by the initial mean-angular state followed by differences of
successive cycle states. The cycle invariant supplies zero order-2 radial
angular moment for each state, while its primitive mean data supplies the
smoothness and support conditions required to subtract the corresponding
integrals. The resulting Lean theorem proves that every selected native
angular stage has zero order-2 `barMoment` on the selected region.

This is a useful negative result for the proposed remainder calculation. The
direct scalar angular branch cannot, by itself, provide the selected nonzero
order-2 radial defect required for a kernel contradiction. It does not,
however, establish the same statement for the final Cartesian field. The
production endpoint is

$$
u_{\mathrm{selected}}
=\mathrm{curl}\!\left(\sum_j\chi_j A_j\right)
 +\sum_j\chi_j B_j,
$$

so the unresolved calculation must transport the curl-generated potential
branch through localisation, cylindrical components, torus averaging, radial
integration, and boundary terms, and then compare it with the separately
added direct branch. Until that selected-field equality and a proved nonzero
remainder are available, the publication claim remains **NOT ESTABLISHED**,
but a kernel-level `False` has not been obtained.

Evidence: `NavierStokesReview/evidence/selected_direct_stage_moment_transport_2026-09-25.md`.

## Local transport of the selected potential stage

The selected construction now admits a source-level field identity for its
potential branch. For each selected stage index satisfying the construction's
residual-band condition, the spatial curl of the selected potential stage
agrees on the actual Cartesian chart domain with the potential field supplied
by the stage-realisation structure. In symbols, on that chart domain,

$$
\mathrm{curl}(A_{\mathrm{selected},k})
=P_{\mathrm{selected},k}.
$$

This result matters because the published moment argument cannot begin from a
generic potential placeholder; it must first identify the actual selected
field that enters the exported velocity. The identity supplies that local
field correspondence without adding axioms or admitted proof gaps.

It does not, however, complete the claimed five-moment argument. The
production velocity has the form

$$
u_{\mathrm{selected}}
=\mathrm{curl}\!\left(\sum_j \chi_j A_j\right)
 +\sum_j \chi_j B_j,
$$

so the current record lacks transport of the curled potential branch and the
separately added direct branch through the cylindrical component map, torus
average, radial integration, axis treatment, and outer-support boundary. A
local chart equality is not a nonzero selected remainder. No proof of
\(\Delta m\ne 0\) or of a kernel contradiction has been obtained. The review
therefore continues to find the published solution claim **NOT ESTABLISHED**
while preserving the distinction between a missing semantic bridge and a
formal contradiction.

Evidence: `NavierStokesReview/evidence/selected_potential_stage_chart_transport_2026-09-25.md`.

## The selected radial input is a rotated Cartesian component

The source construction does not expose the scalar radial moment directly
from the exported Cartesian field. On the valid positive-radius polar chart,
the frame identity gives

$$
u_1(t,x)=\sin(\theta)u_0^{\mathrm{cyl}}(t,x)
          +\cos(\theta)u_1^{\mathrm{cyl}}(t,x).
$$

The review completion transports this identity through the source
`velocity_polar_forward` theorem. This is a useful narrowing of the remaining
correspondence problem: before `barMoment_apply` can be used, the rotated
Cartesian component must be connected to the torus-averaged scalar profile,
and that connection must survive the cutoff, spatial curl, summation, axis
limit, and outer-support boundary.

The identity itself does not imply a nonzero shell contribution. Symmetry,
boundary terms, or cancellation may still make the selected radial value
zero. Accordingly, this result strengthens the transport specification but
does not establish `Delta m ≠ 0` or `False`. The published solution claim
remains **NOT ESTABLISHED** until OpenAI exhibits the complete selected-field
correspondence required by its paper.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

## Base-profile connection to the selected blow-up branch

The audit does not rely on treating the base potential as an opaque symbol.
The source defines the constructed potential from `TailGaugePotential`, proves
that its Euclidean curl equals the selected slow-base velocity before the
terminal time, and proves that the norm of that velocity tends to infinity on
the spatial axis. The review completion transports this exact identity to the
constructed potential.

In symbols, for (t<1),

$$
\operatorname{curl}(A_{\mathrm{selected}})(t,x)
=u_{\mathrm{slow}}(t,x),
$$

and

$$
\|u_{\mathrm{slow}}(t,0)\|\to\infty
\quad (t\to1^{-}).
$$

This is positive evidence for the selected base branch, not a completion of
the paper's five-moment argument. The unresolved step remains the exact
composition of the full mixed Cartesian field with the torus-average and
radial `barMoment` operator after localisation, curl, summation, and boundary
passage. The present record therefore continues to reject the published
solution claim as **NOT ESTABLISHED**, while not claiming a kernel-level
`False`.

Evidence: `NavierStokesReview/evidence/selected_base_profile_transport_2026-09-25.md`.

## Direct-branch component transport

The selected direct branch can now be followed one component further than the
paper's abstract profile notation.  On a valid polar chart, the source frame
does not identify the Cartesian component with the angular profile by
definition.  It gives

$$
u^{\mathrm{direct}}_{j,1}(w)
=\cos(\theta(w))\,Q_n^{-A(h)}
\,a_j\!\left(\operatorname{swapCylinder}\bigl(G_n(\operatorname{polarCoordinates}(w))\bigr)_1\right),
$$

where $a_j$ is the selected `angularNativeStages` profile.  The `swapCylinder`
reindexing is part of the source implementation; omitting it changes the
profile argument and fails to reproduce the field definition.  This formula
is therefore a concrete requirement on any claimed transport from the
Cartesian endpoint to the scalar radial moments $(M,I,J,S,C_p)$.

The result is positive selected-field evidence, not by itself a refutation.
It closes only the component map for the direct branch.  A proof of the
published construction still has to transport the full two-branch field,

$$
\operatorname{curl}\!\left(\sum_j \chi_j A_j\right)
 +\sum_j \chi_j B_j,
$$

through torus averaging, radial integration, the axis branch, and the outer
support boundary.  No selected nonzero remainder or kernel contradiction is
claimed until that calculation is completed.  Conversely, the paper's
five-moment narrative cannot be accepted as a proof of the exported field
without this composition theorem.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

## Direct-branch radial moment calculation

The direct angular branch can now be followed from its Cartesian component to
the scalar moment system without suppressing the coordinate map.  For a
positive-radius cylindrical point (p), the selected component satisfies

$$
u^{\mathrm{direct}}_{j,1}(\operatorname{radialSection}(p))
=\operatorname{meanField}_{j}(\operatorname{radialSection}(p)).
$$

The corresponding native scalar (a_j) is the selected angular stage.  The
source invariant and the exact definition of `barMoment` give

$$
\operatorname{barMoment}_2(a_j)(n,s)
=\int_{\mathbb R} r^2
\operatorname{torusAverage}(a_j(n))(r,s)\,dr=0
$$

for (s) in the selected carrier.  This is a genuine selected-path result,
not a numerical assertion.  It also narrows the counter-paper's target: the
direct scalar branch does not supply the proposed nonzero remainder under
these hypotheses.  The unresolved issue is the curled potential summand in

$$
u_{\mathrm{selected}}
=\nabla\times A_{\mathrm{sum}}+B_{\mathrm{sum}}.
$$

The paper's solution claim still cannot be accepted without transporting that
potential branch through the same torus average, radial integration, axis and
outer-support limits, and final sum.  No claim of `\Delta m\ne0` or `False` is
made until that selected calculation is completed.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

## The graph-to-torus gap in the selected moment calculation

The source code distinguishes between the physical graph used to construct a
selected mean field and the torus average used by the moment operator. The
radial construction evaluates a coefficient on one positive-radial section,

$$
\operatorname{radialSection}(R,s)=\bigl(t,(R,0,s)\bigr),
$$

and the source proves that this section preserves the selected physical graph.
By contrast, `barMoment_apply` evaluates

$$
\int R^2\operatorname{torusAverage}(f_n)(R,s)\,dR,
$$

where `torusAverage` integrates over all auxiliary coordinates. The direct
native scalar branch has a proved zero order-two moment, but the curled
potential branch has not been identified with the same torus-averaged scalar.
The missing graph-to-torus equality is therefore part of the unresolved
selected-field bridge required before the paper's five-moment narrative can
support the exported endpoint.

This distinction preserves the correct verdict. The repository compiles, and
the direct branch has positive selected-path evidence. The advertised
Navier--Stokes solution remains **NOT ESTABLISHED** because the full mixed
field has not been transported through the moment operator. No kernel-level
`False` is claimed on this evidence alone.

Evidence: `NavierStokesReview/evidence/selected_torus_average_representation_gap_2026-09-25.md`.

## The selected mean stream does enter the curled branch

The audit has now closed one possible overstatement. The actual mean stream
is not dead code: `ActualCandidateAssembly.stream_on_chart`, specialised in
`SelectedStreamCurlChartTransport.lean`, identifies the spatial curl of each
selected `streamMeanStages` field with the corresponding `chartStreamParts`
field on the production chart. In symbols,

$$
\nabla\times \operatorname{streamMeanStages}_j
=\operatorname{chartStreamParts}_j.
$$

This is genuine selected-field transport. It does not, however, identify the
resulting vector field with the scalar `Point → ℝ` function on which
`barMoment_apply` operates. The unresolved endpoint is therefore not
that the mean stream is unused, but that its chart/curl representation is
correctly reduced to the torus-averaged scalar moment, including axis and
outer-support terms. The full advertised five-moment conclusion therefore
remains unestablished on the current record.

Evidence: `NavierStokesReview/evidence/selected_stream_curl_chart_transport_2026-09-25.md`.

## Rank correction is active, but its endpoint moment meaning is unproved

The latest source trace corrects a possible overstatement in this review. The
rank machinery is not disconnected from the selected stream. In
`ActualCandidateConstruction.lean:459-470`, the selected successor stream is
assembled from a temporal potential and a rank potential. The source identity
`streamMeanStages_succ` (`:492-494`) then identifies that field with the
corresponding `CycleData.streamFamily`.

The rank mass constraint is also used rather than merely declared. In
`LocalRankDefect.lean:590-604`, `desired_mass_zero` is consumed by the
construction of `rankPotential`; the fixed-stream form at `:606-618` consumes
the same identity again. Thus the correct criticism is not that the rank
correction is dead code.

The remaining problem is at the exported semantic level. The selected stream
decomposes as

$$
(mathrm{streamFamily}_j)_{mathrm{angular}}
 =(mathrm{temporalFamily}_j)_{mathrm{angular}}
  +(mathrm{rankFamily}_j)_{mathrm{angular}},
$$

and `CycleData.stream_moving` (`ActualMeanPhysicalData.lean:915-917`) exports
only a `MovingField`: smoothness, radial support, and auxiliary-coordinate
periodicity. The selected stream is then transported through a Cartesian curl
on the production chart. By contrast,
`DefectIncrementBounds.barMoment_apply` (`:214-220`) requires a scalar field
whose auxiliary coordinates have first been integrated by
`PressureStream.torusAverage`.

No selected theorem presently identifies the curled, assembled stream with
that scalar torus-average input, including the axis, outer-support, and
summation limits. This is a concrete endpoint correspondence failure under
CTR-005. It is stronger than a generic “missing bridge” description because
the source shows exactly where the rank data enters and exactly where the
exported type stops. It still does not prove a nonzero remainder or Lean
`False`; the next required result is an actual selected value or inequality
for the mixed field's `barMoment`.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

## Selected cutoff--curl calculation

The production potential branch does not curl the uncut profile directly. It
first forms each cut stage and then sums it. The review completion
`selected_cut_stage_curl_expansion` proves the exact local identity

$$
\operatorname{curl}(\chi A)=\chi\operatorname{curl}(A)
 +\operatorname{curlLinear}\bigl((D\chi)\operatorname{smulRight}A\bigr).
$$

Here `χ` is the scaled spatial cutoff and `A` is the selected potential
stage. Thus a radial calculation that replaces the production curl by
cutoff-times-uncut-curl has omitted a source-level term. The commutator must
be transported through the Cartesian-to-radial projection, torus average,
summation, and boundary limits before a five-moment conclusion can be made.

The completion proves the formula only. It does not prove that the selected
commutator has a nonzero radial moment, nor does it establish `Delta m ≠ 0` or
`False`. Those remain the next load-bearing calculations.

Evidence: `NavierStokesReview/evidence/selected_cutoff_curl_commutator_2026-09-25.md`.
## Selected Cartesian-to-radial transport status: 2026-09-25

The review now distinguishes two statements that must not be conflated. The
chart point used by the physical construction is compatible with the
pressure-stream point used by the moment definitions; a raw type-domain
mismatch is therefore not a valid objection.

The unresolved issue is stronger and source-specific. The selected endpoint
exports Cartesian stage sums and residual consequences. `barMoment` consumes a
scalar profile on the pressure-stream lift. The review completion
`SelectedPhysicalPointTransport.lean` proves the exact moment formula after an
explicit point-to-spacetime map and scalar-profile equality are supplied, but
the selected endpoint does not currently export that post-curl, post-`tsum`
identification or its torus-average, axis, and outer-support limits. The
five-moment mechanism is therefore not yet shown to constrain the selected
field claimed by the paper.

This is a material correspondence failure and a publication-level burden of
proof. It is not, by itself, a zero-sorry proof of `False` or of a nonzero
selected remainder. The active verdict remains **NOT ESTABLISHED AS A CMI
SOLUTION** unless the review derives a concrete contradiction or independently
verifies the selected-field transport from the actual source. The current
record is sufficient to reject the advertised paper-to-code claim, but not to
assert that the selected identities are false.

Evidence: `NavierStokesReview/evidence/selected_physical_point_transport_2026-09-25.md`.

## Production localisation changes the moment problem

The selected-field calculation identifies a specific point where the paper's
native moment cancellation cannot be carried across by notation alone. The
native direct profile has a proved zero order-two radial moment. The exported
production field is not that profile: on the fundamental cube it is

$$
u_{\mathrm{prod}}(t,x)=u_{\mathrm{periodic}}(t,x)+\chi(x)v(t,x),
$$

with `χ` the spatial cutoff, followed by periodisation. The zero-sorry
theorem `mixed_periodic_velocity_eq_cut_direct_on_unitCube` in
`NavierStokesReview/src/completions/SelectedProductionDirectCutoff.lean`
proves this exact identity from the production definitions.

Thus the relevant calculation is not the native identity

$$
\operatorname{barMoment}_2(v)=0,
$$

but the cutoff-weighted, post-periodisation quantity. The curl of a cut
potential also contributes the explicit commutator

$$
\operatorname{curl}(\chi A)=\chi\operatorname{curl}(A)
 +(\nabla\chi)\times A.
$$

Until the selected Cartesian field is transported through the scalar radial
profile, torus average, and boundary terms, the claimed five-moment repair has
not been shown for the exported field. This is a source-backed
correspondence failure and a substantive publication-level objection under
CTR-005. It is not, at present, a proved `\Delta m\ne0` or kernel-level
contradiction. The overall review verdict therefore remains NOT ESTABLISHED
AS A CMI SOLUTION.

Evidence: `NavierStokesReview/evidence/selected_production_direct_cutoff_2026-09-25.md`.

## Support control is not cutoff control

The selected support theorem currently available in the source is radial. It
bounds `AnnularEndpoint.radius` by a similarity outer radius, whereas the
spatial cutoff is known to equal one only on the two-coordinate set

$$
\{x:\operatorname{radialSquare}(x)<1/32\ \wedge\ |x_2|<1/8\}.
$$

The review completion `SelectedSupportPredicateScope.lean` makes the gap
explicit at the predicate level: a point on the symmetry axis with axial
coordinate one satisfies the radial support inequality but is outside the
cutoff plateau. This is not a claim about the selected smooth field. It is a
proof that the radial support theorem alone cannot remove the cutoff from the
selected production field.

Accordingly, the relevant five-moment calculation must retain the cutoff,
the curl commutator, the torus average, and the boundary terms. The source
record therefore supports a publication-level correspondence objection under
CTR-005, but not yet a nonzero selected remainder or Lean `False`.

Evidence: `NavierStokesReview/evidence/selected_support_predicate_scope_2026-09-25.md`.
## Auxiliary-domain transport gate

The selected Cartesian-to-radial calculation has a more specific obstruction
than a missing theorem name. `PressureStream.torusAverage` integrates the two
auxiliary coordinates over the full unit square before `barMoment` performs its
radial weighting. The selected physical graph, however, is transported through
`PhysicalResidualBridge.absoluteLift` on the positive-radius chart. Its
auxiliary coordinate has the form

$$Y=a(r)v_r+t v_t,qquad a(r)\ge 0,$$

where

$$v_r=(1,1-sqrt2),qquad v_t=(sqrt2-1,1).$$

The review completion constructs a linear functional $ρ$ satisfying
$ρ(v_r)=1$ and $ρ(v_t)=0$. Hence every positive-radius graph point has
$ρ(Y)\ge0$. The point $Y_0=(0,1/2)$ lies in the unit auxiliary square but
has $ρ(Y_0)<0$, so it is outside that graph image.

This does not by itself prove a nonzero radial remainder. It proves that the
published scalar moment calculation cannot be recovered from the selected
positive-radius graph without an additional global extension or an
auxiliary-coordinate invariance theorem. Until the selected integrand is
defined and evaluated over the complete averaging domain, the five-moment
transport claim remains unverified.

The direct production map is included in this calculation gate. The completion
proves that `PhysicalMeanJetBounds.physicalPoint` misses an explicit auxiliary
point in the unit averaging square. Meanwhile, `ActualMeanPhysicalData.Scalar`
is defined on the full point domain, and `meanField` samples the atlas through
`physicalPoint`. The remaining theorem must therefore compare the raw scalar
family consumed by `barMoment` with the scalar profile represented by the
exported production field. An image miss is a concrete transport obstruction,
but it is not by itself a proof of a nonzero moment or `False`.

### Valid-band observation boundary

The atlas construction does not evaluate an arbitrary native scalar family at
every point. `Atlas.physical` selects a valid chart sample when one exists and
returns zero otherwise. The zero-sorry completion
`SelectedAtlasPhysicalErasure.lean` proves the corresponding congruence: two
families that agree at all valid chart samples yield the same selected
physical field.

This sharpens, but does not complete, the five-moment objection. The native
`barMoment` integral ranges over the full lifted torus-average domain. A
remaining transport theorem must connect that domain to the valid chart
samples, or prove that the omitted values contribute zero. Without that
theorem, no selected `Δm ≠ 0` or kernel `False` has been established.

Evidence: `NavierStokesReview/evidence/selected_atlas_physical_erasure_2026-09-25.md`.

## The atlas boundary in the selected moment pipeline

The source audit now identifies a precise domain boundary in the exported
field. `Atlas.Valid` requires a strictly positive first slow coordinate, while
`Atlas.physical` totalises the atlas by returning zero when no valid sample is
available. The zero-sorry theorem
`SelectedAtlasDomainBoundary.atlas_physical_zero_of_nonpositive_slow_coordinate`
formalises this as

$$z.2.1.1\le0\Longrightarrow
\operatorname{Atlas.physical}(A,U,d,f,z)=0.$$

The point matters because the advertised moment is computed in a different
order. `torusAverage` integrates the native scalar family over its full
auxiliary domain, and `barMoment` then integrates in the radial variable.
The production atlas observes only valid chart samples before it is supplied
to the exported field. Consequently, the paper-to-code proof still requires
an equality between the native scalar consumed by `barMoment` and the
zero-extended scalar represented by the production atlas, or a theorem that
the omitted contribution vanishes.

This is a concrete correspondence and domain obligation under CTR-005. It is
not yet a calculation of a nonzero remainder. In particular, the audit does
not claim `Delta m ≠ 0` or `False` until the selected native scalar and its
torus average have been evaluated on the relevant omitted region.

Evidence: `NavierStokesReview/evidence/selected_atlas_domain_boundary_2026-09-25.md`.

## A concrete production weighting in the direct branch

The selected direct branch supplies a more precise calculation target than the
abstract statement that a transport theorem is missing. The source identifies
`directStages` with the native angular mean stages, but the production assembly
then applies `SpatialLocalization.cutPotential`. The zero-sorry completion
`SelectedProductionDirectScalarGate.lean` proves on a positive radial section
that

$$
\bigl(\operatorname{cutPotential}(D_j)\bigr)_1
=\chi(r,z)m_j(r,z),
\qquad
\chi(r,z)=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z).
$$

The upstream order-two `barMoment` identity concerns the unweighted native
profile $m_j$. It cannot be substituted into the production calculation until
the cutoff-weighted remainder

$$
\int r^2\operatorname{torusAverage}((\chi-1)m_j)(r,p)\,dr
$$

has been evaluated, together with the curled potential branch and the endpoint
terms. This is now a concrete selected-field calculation under CTR-005. The
review does not claim a nonzero remainder until that integral is established.

Evidence: `NavierStokesReview/evidence/selected_production_direct_scalar_gate_2026-09-25.md`.

## Atlas pullback of the selected direct component

The field-level calculation has been sharpened one step further. The selected
direct branch is transported to its native angular stage and then unfolded to
the atlas-backed scalar evaluated at the physical point. Its first Cartesian
component is therefore

$$
D^{\mathrm{dir}}_{j,1}(w)=
A^{\mathrm{phys}}(\operatorname{physicalPoint}(w))
\left(\operatorname{angularVector}(\operatorname{radialProjection}(w))\right)_1.
$$

The production localisation multiplies this by `spatialCutoff`; on the
positive radial section that factor is

$$
\chi(r,z)=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z).
$$

This removes one layer of abstraction from the remaining CTR-005 calculation.
The unresolved question is now whether the atlas-selected, cutoff-weighted
scalar has the required torus average and radial moment after the complete
production assembly. The native unweighted zero is not sufficient, but no
nonzero remainder has yet been proved.

Evidence: `NavierStokesReview/evidence/selected_production_atlas_pullback_2026-09-25.md`.
## Selected potential branch: a finite local curl identity

The latest source-backed completion follows the selected potential branch
through the first nontrivial field operation. The selected preterminal
potential sum is locally a finite prefix, and the spatial-curl operator
preserves that local equality. Thus, for every preterminal point (x), some
finite (N) satisfies

\[
u_{\mathrm{pot}}
  =_{\mathcal N x}
\nabla\times\operatorname{partialPotential}_N.
\]

This is a concrete identity for the selected Cartesian field. It is not an
assumption about an abstract witness. The proof is recorded in
`SelectedPotentialPrefixCurlExpansion.lean` and builds with the review tree.

The identity also fixes the next analytical obligation. The finite curl must
still be expanded into its stage terms, transported through the positive-radius
chart and axis totalisation, and compared with the scalar family consumed by
`torusAverage` and `barMoment`. The cutoff/curl commutator remains explicit;
it has not been set to zero. No nonzero radial remainder or `False` result is
claimed until that selected calculation is completed.

The central conclusion is therefore unchanged. OpenAI's published assertion
of a Navier–Stokes solution remains **not established** by the present proof
record. This completion narrows the unresolved selected-field calculation; it
does not lower the burden of proof or convert an unproved correspondence into
an accepted solution.

Evidence: `NavierStokesReview/evidence/selected_potential_partial_curl_2026-09-25.md`.

## Stagewise curl expansion on the physical domain

The selected potential branch has now been expanded one step further. On the
open physical domain, the selected velocity is eventually equal to a finite
sum of the curls of the cutoff stages. This is proved without `sorry` in
`SelectedPotentialStagewiseCurlOnPhysicalDomain.lean`.

For a cutoff stage `χ A`, the spatial curl has the exact form

\[
\operatorname{curl}(\chi A)
 = \chi\,\operatorname{curl}(A) + (\nabla\chi)\times A.
\]

The second term is not a presentation detail. It is the unresolved selected
remainder that must be transported through the positive-radius chart,
axis/outer limits, `torusAverage`, and `barMoment`. The review records no
nonzero value until that calculation is completed. Thus the result strengthens
the `CTR-005` specification-drift finding without converting it into a kernel
contradiction.

Evidence: `NavierStokesReview/evidence/selected_potential_stagewise_curl_2026-09-25.md`.

## A concrete scalar representative for the direct branch

The direct branch has now been tied to the scalar domain used by the moment
operator. `SelectedDirectAtlasScalarRepresentative.lean` defines the selected
atlas scalar through `Atlas.physical` and the same physical-point map used by
`meanField`. It proves the corresponding pullback identity and expands
`barMoment` into the radial integral of the torus average. On the positive
radius section, the first component of the selected direct stage agrees with
that scalar.

This is a concrete transport result, not a completed disproof. The exported
field still combines the direct and potential branches through cutoffs, curl,
and a natural-number summation. Those terms must be evaluated before a
nonzero remainder or a contradiction can be claimed.

Evidence: `NavierStokesReview/evidence/selected_direct_atlas_scalar_representative_2026-09-25.md`.
## Native direct prefix calculation

The selected native direct scalar can now be calculated exactly at finite
stage depth. If

\[
m_J(z)=\sum_{j=0}^{J} m_j(z),
\]

the Lean completion
`SelectedDirectNativePrefixMoment.lean` proves

\[
m_J=(\texttt{selectedCycle}\ J).\texttt{state.mean.angular}
\quad\text{and}\quad
\operatorname{barMoment}_2(m_J)=0
\]

on the selected carrier. This is a selected source identity, not a claim
about an abstract rate interface.

It does not yet evaluate the scalar consumed by the advertised endpoint. The
production field applies a spatial cutoff to the direct branch and combines it
with a Cartesian curl of cutoff potential stages. In general,

\[
\operatorname{barMoment}_2(\chi m_J)\ne
\operatorname{barMoment}_2(m_J)
\]

unless the weighted integral is separately proved. The curl branch also
contains the product-rule contribution

\[
\nabla\times(\chi A)=\chi(\nabla\times A)+(\nabla\chi)\times A.
\]

The unresolved endpoint is therefore concrete: the current record does not transport these production terms
through the atlas, auxiliary torus average, boundary limits, and final
`tsum`, then evaluate the resulting selected moment. The present completion
proves neither `\Delta m\ne0` nor `False`; it removes the native direct prefix
as the source of an uncomputed remainder.

Evidence: `NavierStokesReview/evidence/selected_direct_native_prefix_moment_2026-09-25.md`.

## Production cutoff and the selected shell remainder

The native direct prefix has an exact order-two zero moment before production
localisation. The exported direct branch is different: each stage is first
multiplied by the spatial cutoff used by the production assembly. The review
completion proves the finite-prefix identity

$$
\sum_{j=0}^{J}(\chi u_j)_1
=\chi\sum_{j=0}^{J}(u_j)_1,
$$

and, on the positive-radius radial section, identifies the uncut sum with the
selected cycle mean field. Consequently the difference between the produced
and native components is exactly

$$
\mathcal{E}_J=(\chi-1)\sum_{j=0}^{J}(u_j)_1.
$$

This is a concrete selected-field remainder, not a generic objection. It is
the term that must be carried through the radial projection, torus average,
and final `tsum` before the paper's five-moment identities can be claimed for
the exported field. The available source proves only positivity and ordering
of the moving annulus radii. It does not yet prove a selected nonzero value of
the weighted integral. Thus the paper's solution claim remains **NOT
ESTABLISHED**, while this result does not yet constitute a kernel
contradiction.

Evidence: `NavierStokesReview/evidence/selected_production_direct_prefix_cutoff_2026-09-25.md`.

## The cutoff commutator in the exported potential field

The production field is obtained after spatial localisation. The review
completion
`NavierStokesReview/src/completions/SelectedPotentialProductionProductRule.lean`
proves the selected identity

$$
V_{\mathrm{prod}}(t,x)=\chi(x)\,\operatorname{curl}A(t,x)
 +\operatorname{curlLinear}\!\left(D\chi(x)\,A(t,x)\right)
$$

on the unit cube, where $A$ is the selected potential sum. The second term is
the commutator created when the spatial curl acts on the cutoff. It must be
transported into any radial moment calculation. The five-moment discussion
cannot be identified with the exported field by silently replacing the
localised curl with the native curl.

This establishes a concrete calculation obligation, not a completed
contradiction. The selected atlas component, torus average, `barMoment`, and
infinite-sum transport are still required before the commutator can be given
a selected value or sign. The paper's claim therefore remains **NOT
ESTABLISHED** under the present audit, without claiming that this identity
alone proves `False`.

Evidence: `NavierStokesReview/evidence/selected_potential_production_product_rule_2026-09-25.md`.

## Positive-radius transport of the selected production field

The next source-level completion transports the selected production identity
to the radial section used by the construction. For the selected schedule and
points in the stated physical domain, the first Cartesian component satisfies

$$
V_{\mathrm{prod},1}(t,r,z)=
\chi(r,z)\,\bigl(\operatorname{curl}A(t,r,0,z)\bigr)_1
 +\bigl(\operatorname{curlLinear}(D\chi(r,z)\,A(t,r,0,z))\bigr)_1.
$$

The completion derives the differentiability required by the product rule from
the repository’s selected schedule and its physical-domain smoothness
lemmas. This makes the cutoff derivative contribution a selected-field fact,
not merely a concern about how localisation might behave.

The result does not yet identify this radial-section component with the scalar
family integrated by `barMoment` over the full lifted averaging domain. That
step requires an explicit graph/image theorem, boundary control, torus-average
transport, and passage through the final `tsum`. No sign or nonzero value of
the commutator has been assumed. The conclusion therefore remains **NOT
ESTABLISHED**, rather than a claimed kernel contradiction.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

## Positive-radius lift: an authenticated local bridge, not the endpoint theorem

The source does contain a legitimate coordinate-type bridge that must be
credited. `PhysicalResidualTZ.Lift` is definitionally the product

$$
R × (Plane × Plane),
$$

which is also the point type used by `PressureStream.Lift` when the slow point
is `PhysicalGraphBounds.Plane`. On the positive-radius region,
`ActualMeanPotentialRealization.physicalPoint_forward` identifies the physical
mean point with `PhysicalResidualTZ.absoluteLiftTZ`. In addition,
`ActualCandidateAssembly.stageRealizations` identifies each selected stage curl
with its chart field on the stated chart domain.

This narrows, rather than removes, the remaining objection. These results are
local and stagewise. They do not supply a theorem that transports the final
localised `tsum`, including its cutoff-gradient term and axis or outer-support
limits, into the scalar family consumed by `DefectIncrementBounds.barMoment`.
The published five-moment conclusion therefore still requires an explicit
selected-field composition theorem and an evaluated weighted integral. No sign
or nonzero remainder is inferred from the type compatibility alone.

Evidence: `NavierStokes/PhysicalResidualTZ.lean:19-21,385-452`,
`NavierStokes/ActualMeanPotentialRealization.lean:20-27,331-358`, and
`NavierStokes/ActualCandidateAssembly.lean:1059-1088`.

## A typed local bridge into the radial moment operator

The selected production calculation can now be stated in the type required by
the source moment operator. Let \(q=(R,(T,Z),Y)\) denote a point in the lifted
physical coordinate space. Define the positive-radial section

$$
\pi(q)=(T,(R,Z)).
$$

For the selected schedule \(a\), the review completion defines

$$
F_a(n,q)=V_{\mathrm{prod}}(a)(n,\pi(q)),
$$

as a genuine `ScalarField` on the point type consumed by `barMoment`.
Thus the source definition gives the exact identity

$$
\operatorname{barMoment}_k(F_a)(n,p)=
\int_{\mathbb R}r^k\,
\operatorname{torusAverage}(F_{a,n})(r,p)\,dr.
$$

On the radial section of the physical chart, the point map agrees with the
source physical-point construction for \(R>0\), so this is a real selected
coordinate compatibility result rather than an abstract type alias.

This result narrows the counter-paper's central objection. The issue is no
longer whether the production component can be assigned a `barMoment` type;
it can. The unresolved question is whether the full exported velocity,

$$
U=\operatorname{curl}(\chi A)+\chi B,
$$

including the term \((\nabla\chi)\times A\), its auxiliary torus average,
axis and outer-support limits, and the final \(\operatorname{tsum}\), is equal
to \(F_a\) or to the five profiles used by the paper. Until that selected
identity and its weighted value are proved, the advertised five-moment
solution remains **NOT ESTABLISHED**. The local bridge supplies no sign for a
remainder and no kernel-level `False`.

Evidence:
`NavierStokesReview/evidence/selected_potential_production_barmoment_section_2026-09-26.md`.

## Finite-prefix production and the remaining numerical gate

The next completion follows the selected field before taking its infinite
series limit. For a finite prefix (N), the review defines the actual partial
potential (A_N), applies the source localisation and curl operators, and
retains the exact commutator

$$
\operatorname{curl}(\chi A_N)=
\chi\operatorname{curl}(A_N)+(\nabla\chi)\times A_N.
$$

The finite production is then represented on the lifted point space accepted
by the source radial-moment operator. Thus the source definition supplies

$$
\operatorname{barMoment}_k(F_{a,N})(n,p)=
\int r^k\,\operatorname{torusAverage}(F_{a,N,n})(r,p)\,dr.
$$

On the positive-radius physical section, the lifted scalar pulls back to the
selected finite-prefix production component. This is a concrete transport
result about the selected construction, not a hypothetical countermodel.

It also identifies the exact unresolved quantity. A refutation would require a
zero-sorry evaluation of the torus average and weighted integral, including
the localisation commutator, axis and outer-support terms, followed by a
proved passage (N\to\infty) to the selected `tsum`. Until that calculation
produces a selected nonzero remainder and its matching selected invariant, the
record remains **NOT ESTABLISHED**, rather than a kernel-level `False`.

Evidence:
`NavierStokesReview/evidence/selected_potential_production_finite_prefix_2026-09-26.md`.

## 2026-09-26: finite-prefix torus-average reduction

The preceding finite-prefix construction can now be reduced through the
repository's actual torus-average definition. The review scalar is lifted to
the point type consumed by `barMoment` through `pointToCyl`. Since this map
ignores the auxiliary `Plane` coordinate, the interval integrations in the
torus average are exact definitional repetitions:

$$
\operatorname{torusAverage}(F_{a,N,n})(r,p)
=F_{a,N,n}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr).
$$

Substitution into the source definition of `barMoment` yields

$$
\operatorname{barMoment}_k(F_{a,N})(n,p)
=\int_{\mathbb R} r^k V_{a,N}
\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr)\,dr.
$$

This is a concrete selected finite-prefix transport identity. It does not
evaluate the weighted integral, prove that its value is nonzero, or establish
that the review scalar is the full mixed Cartesian field in the published
endpoint. The axis and outer-support terms and the passage to the selected
infinite `tsum` remain to be proved. The controlled conclusion therefore
remains **NOT ESTABLISHED**, not a kernel-level contradiction.

Evidence: `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md`.

## Axis scale identity

One previously open coordinate question is settled directly by the source.
`NavierStokes/AxisPreservation.lean:130-148` proves that on the symmetry axis,

$$
q_h(t,0)=1-t,\qquad q_h(t,0)\longrightarrow0\quad(t\to1^-).
$$

This follows from the defining equation for the positive similarity coordinate
after the axial coordinate is set to zero. It is therefore a genuine selected
coordinate identity, not a filter-vacuity argument. It does not calculate the
selected velocity's radial moment. The unresolved endpoint is the absent transport of the
complete Cartesian `tsum` through the cutoff/curl construction and then
evaluate its axis, tail, and weighted `barMoment` contributions.

## Finite-prefix cutoff behaviour at the axis endpoint

The review completion SelectedFiniteCutoffEndpoint.lean pulls the source
finite-cutoff plateau through

$$
q_h(t,0)=1-t\\longrightarrow0\\qquad(t\\to1^-).
$$

For every fixed prefix length N, all cutoffs with j < N are therefore equal
to one on some left neighbourhood of t = 1. This is a concrete endpoint fact
about finite prefixes. It is not uniform in N, and it does not evaluate the
infinite Cartesian sum, its curl, the torus average, or the weighted radial
moment. No nonzero remainder or contradiction is claimed from this fact alone.

Evidence:
NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md.

The corresponding source-scope audit records that the local finite-tail and
all-jet theorems require `0 < q x`, whereas the selected axis limit has
`q → 0`. The infinite `potentialSum` representative and its transport through
curl, torus averaging, and `barMoment` therefore remain to be identified.
This is an explicit proof obligation, not an asserted discontinuity or
nonzero remainder.

Evidence:
NavierStokesReview/evidence/selected_tsum_endpoint_scope_2026-09-26.md.

## Selected mixed velocity: separate finite local representatives

The selected endpoint has now been traced through both summation branches. A
zero-sorry completion proves that, at every point of the source physical
domain, the curl-generated potential branch is eventually equal to a finite
curl prefix and the direct branch is eventually equal to its own finite
potential prefix. The two prefix lengths are independent.

This closes the finite local field representation, but it does not evaluate
the full selected field through `torusAverage` or `barMoment`. In particular,
no common truncation index, endpoint interchange, weighted radial value,
nonzero remainder, or kernel contradiction follows. The selected CMI claim
therefore remains **NOT ESTABLISHED** on the existing correspondence record,
while this result supplies the exact finite object required for the next
calculation.

Evidence:
`NavierStokesReview/evidence/selected_mixed_velocity_finite_prefix_2026-09-26.md`.

## Localisation of the selected infinite sum

A further zero-sorry completion isolates the local meaning of the selected
potential `tsum`. At any point where the source production scale is positive,
and under the source convergence hypothesis on the coefficient sequence, the
all-jet API supplies one finite prefix that agrees locally with the infinite
potential at every derivative order:

$$
\exists N\;\forall k,\qquad
D^k\operatorname{potentialSum}(z)
=D^k\operatorname{partialPotential}_N(z)
\quad\text{eventually near }z.
$$

This is useful positive evidence: the selected `tsum` has a precise local
finite-prefix representative on the stated domain. It is not the missing
selected-field transport theorem. The result does not pass the identity through
the global Cartesian curl, `torusAverage`, `barMoment`, or the weighted radial
integral, and it does not evaluate the axis and tail terms. Consequently it
does not prove a nonzero remainder `Delta m != 0` or a kernel contradiction
`False`; the advertised five-moment solution remains **NOT ESTABLISHED** until
those global identifications are supplied.

Evidence:
`NavierStokesReview/evidence/selected_potential_production_tsum_scope_2026-09-26.md`.

## A conditional periodic-to-radial obstruction

The source construction and the radial moment interface impose different
geometric structures. The selected Cartesian velocity is obtained from a
periodised potential, and the source proves unit spatial periodicity. The
operator `barMoment`, however, is defined on a scalar radial field with bounded
radial support. The review-side theorem
`PeriodicRadialSupportObstruction.lean` establishes

$$
g(r+1,Y)=g(r,Y),qquad
\operatorname{supp}(g)\subseteq [a,b]
\quad\Longrightarrow\quad
g(r,Y)=0.
$$

This result is not a selected-endpoint identification.
It does not prove that the selected Cartesian field has a bounded radial
pullback, nor does it identify that pullback with the scalar consumed by
`barMoment`. It therefore yields no numerical remainder and no kernel
contradiction. It sharpens the adverse finding: on the inspected
record does not transport the periodised Cartesian field into the radial
observable with compatible support, nor does it state and justify a different
scalar extension. The advertised five-moment paper-to-code correspondence is
therefore **NOT ESTABLISHED** on the present formal record.

Evidence:
`NavierStokesReview/evidence/periodic_radial_support_obstruction_2026-09-26.md`.

## Mixed endpoint and radial observables

The selected whole-space velocity is assembled from two branches. The
potential branch is localised, while the direct branch is cut and periodised
separately. A zero-sorry review completion proves the first-component
identity on the radial section

$$
u_{\mathrm{mixed},1}(p)=u_{\mathrm{potential},1}(p)+
\left(\operatorname{periodize}\bigl(\operatorname{cutPotential}
u_{\mathrm{direct}}\bigr)(p)\right)_1.
$$

This is a precise scope result, not an assertion that the direct contribution
is nonzero. It does show that a potential-only scalar calculation cannot be
silently identified with the exported mixed field. A complete paper-to-code
transport theorem would still have to map the direct summand to the scalar
radial observable consumed by `barMoment`, justify the common endpoint and
the axis and tail terms, and evaluate the weighted integral. Until then,
CTR-005 remains a load-bearing correspondence failure; this completion does
not establish `Δm ≠ 0` or a kernel-level `False` theorem.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_radial_component_2026-09-26.md`.

### Mixed endpoint observable

The selected endpoint is not merely a potential-only field. The review-side
completion `SelectedMixedProductionBarMoment.lean` defines the first Cartesian
component of the actual mixed periodic velocity on the scalar-family domain
used by the repository's radial observable and proves

$$
\operatorname{barMoment}_k(\widetilde u)(n,p)
=
\int_{\mathbb R} r^k\,
\operatorname{torusAverage}(\widetilde u_n)(r,p)\,dr.
$$

On the positive-radius physical section, this scalar is exactly the selected
mixed component. The theorem therefore closes a real domain and coordinate
transport step. It does not evaluate the integral, prove a nonzero remainder,
or identify the result with the five paper moments. The remaining issue is the
value-level calculation for the cut, periodised direct branch together with
the axis, tail, and infinite-sum limits.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

### Conditional linearity of the mixed radial observable

The review-side completion `SelectedMixedProductionBarMomentLinearity.lean`
also proves the exact pointwise decomposition of the selected scalar family
into its potential and direct branches. Under explicit common `Shell`
hypotheses, the source linearity theorem gives

$$
\operatorname{barMoment}_k(\widetilde u)
= \operatorname{barMoment}_k(\widetilde u_{\mathrm{potential}})
+ \operatorname{barMoment}_k(\widetilde u_{\mathrm{direct}}).
$$

This is a genuine algebraic completion, but the selected endpoint does not
export the required common `Shell` premises for the complete infinite-sum
branches. The result therefore does not evaluate the weighted integral, prove
a nonzero localisation commutator, identify the observable with the five
paper moments, or derive `False`. It narrows CTR-005 to the missing value-level
and selected-path transport obligations.

Evidence: `NavierStokesReview/evidence/selected_mixed_barmoment_linearity_2026-09-26.md`.

### What the selected witness actually exports

The source-path audit corrects a filename ambiguity without weakening the
substantive objection. The current tree has no `SelectedCandidate.lean` file.
The selected witness is `ActualCandidateAssembly.selected_witness` at
`NavierStokes/ActualCandidateAssembly.lean:1177`, and its `hc` component is the
`CandidateProperties` structure consumed by `selected_candidate` at lines
1177--1185. The structure is not itself existential; the surrounding
`candidateStatement` supplies the existential quantifiers.

The exported record genuinely contains smoothness, compact support, the
Navier--Stokes residual equation, divergence-freeness, a uniform finite-energy
bound, and the stated speed blow-up. The R3 construction obtains the energy
field through `CompactEnergy.uniform_finite_energy` and uses a spatially
compactified, smoothly time-cut-off force. The remaining correspondence issue
is narrower and more consequential: no exported field of `hc` identifies the
five paper moments `(M,I,J,S,C_p)` with the final Cartesian field or proves
that the periodic `barMoment` survives the R3 compactification. This is a
load-bearing selected-path transport obligation, not a claim that the energy
theorems are missing and not, by itself, a kernel-level contradiction.

The R3 packaging boundary has also been checked directly. A zero-sorry
completion constructs a nonzero abstract five-coordinate payload alongside
the exported R3 candidate, because `CandidateProperties` contains no such
payload. This proves a limitation of the exported interface, not a numerical
claim about the selected field. The paper therefore keeps the decisive
field-level question open: evaluate the selected `barMoment` after the
periodic-to-whole-space construction, or derive a contradiction from an
explicit equality.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.

## Source-path reconciliation and a conditional integral result

One secondary source report cited a module named `SelectedCandidate.lean`.
That name is not present in the current tree or reachable Git history. The
actual selected path is `ActualCandidateAssembly.selected_witness` and
`ActualCandidateAssembly.selected_candidate` at
`NavierStokes/ActualCandidateAssembly.lean:1177-1184`, followed by the R3
wrappers in `NavierStokes/R3/ActualCandidate.lean:127-151` and the exported
theorems in `NavierStokes/R3/Theorem.lean:26-80`. The energy declarations are
not missing: `uniform_finite_energy` is at
`NavierStokes/R3/CompactEnergy.lean:343`, and
`theorem_1_1_with_dissipation` is at `NavierStokes/R3/Theorem.lean:66`.
Accordingly, a filename error must not be promoted into an energy-proof
objection.

The review also formalises one conditional consequence of the radial integral
definition. If a scalar pullback $g$ is unit-periodic and strictly positive
on a fundamental interval, then $g$ is not globally Bochner-integrable:

$$
g(r+1)=g(r),\quad 0<g(r)\ (0<r<1)
\quad\Longrightarrow\quad
\neg\operatorname{Integrable}(g).
$$

In Lean, `MeasureTheory.integral_undef` consequently gives

$$
\int_{\mathbb R} g(r)\,dr=0
$$

for that non-integrable branch. The theorem is instantiated for the selected
mixed radial pullback only under its positivity premise. The selected source
does not prove that premise, and the result does not evaluate the weighted
cases $r^k g(r)$ for $k>0$. It is therefore an exact semantic branch of
the audit, not a selected-field contradiction.

Evidence:
`NavierStokesReview/evidence/source_path_reconciliation_2026-09-26.md`;
`NavierStokesReview/evidence/periodic_global_integral_semantics_2026-09-26.md`.

The auxiliary torus average of this scalar pullback is independent of the
auxiliary coordinate. Consequently the selected mixed observable is reduced
to the literal radial expression

$$
\operatorname{barMoment}_k(\widetilde u)(n,p)
=
\int_{\mathbb R} r^k\,
u_{\mathrm{mixed},1}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr)\,dr.
$$

The integrand is the sum of the potential component and the cut,
periodised direct component. This is a concrete calculation target, not yet a
computed value: no nonzero remainder or contradiction follows until the
direct term and the endpoint/interchange conditions are evaluated.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

### Periodisation versus radial support

The selected mixed pullback entering the radial observable is unit-periodic in
the integration variable:

$$
g_a(r+1,p)=g_a(r,p).
$$

The review completion also proves the exact conditional implication

$$
\operatorname{RadiallySupported}_{[\alpha,\beta]}(g_a)
\Longrightarrow g_a\equiv 0.
$$

This does not by itself refute the exported theorem, because the selected
`Witness` does not export bounded radial support for the periodised mixed
pullback, and the completion does not prove that the pullback is nonzero. It
does, however, make the remaining field-level defect precise: the inspected
record does not supply a valid support/integrability interpretation for
applying the radial moment machinery to the periodised endpoint, nor does it
evaluate the observable under a different justified restriction.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

### Mixed endpoint observable

The selected endpoint is not merely a potential-only field. The review-side
completion `SelectedMixedProductionBarMoment.lean` defines the first Cartesian
component of the actual mixed periodic velocity on the scalar-family domain
used by the repository's radial observable and proves

$$
\operatorname{barMoment}_k(\widetilde u)(n,p)
=
\int_{\mathbb R} r^k\,
\operatorname{torusAverage}(\widetilde u_n)(r,p)\,dr.
$$

On the positive-radius physical section, this scalar is exactly the selected
mixed component. The theorem therefore closes a real domain and coordinate
transport step. It does not evaluate the integral, prove a nonzero remainder,
or identify the result with the five paper moments. The remaining issue is the
value-level calculation for the cut, periodised direct branch together with
the axis, tail, and infinite-sum limits.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.
## Source authority and endpoint map

The source audit was reconciled against the extracted repository tree and the checked-out Lean files. The current source contains both root-level R3 wrapper modules and detailed modules under `NavierStokes/R3/`. In particular, `NavierStokes/R3/ActualCandidate.lean` packages the selected construction, while `NavierStokes/R3/Theorem.lean` exports the existential endpoint. The root files `NavierStokes/R3.lean`, `NavierStokes/R3PressureFourier.lean`, `NavierStokes/R3EnergyNorms.lean`, and `NavierStokes/R3EnergyBoundary.lean` are also present and must not be conflated with the detailed `R3/` paths.

The exported contract is substantive. `CandidateProperties` requires smoothness, spatial periodicity, zero initial velocity, positive-time force support, incompressibility, the Navier–Stokes residual identity, and unbounded speed. The R3 packaging additionally supplies the finite-energy and dissipation conclusions. The audit therefore does not argue that the endpoint is an empty wrapper or that these files are absent.

The unresolved issue is transport of the paper’s named five moments into that exported field. The upstream moment and rank modules are present, and the review has verified several algebraic and finite-prefix identities. What remains unproved is a single selected-path theorem identifying the complete Cartesian field produced by the infinite assembly with the five radial quantities `(M, I, J, S, C_p)`. This is the precise scope of CTR-005.

The pressure modules require the same calibration. `NavierStokes/R3/PressureRecovery.lean` proves comparison pressure-gradient identities against compact smooth tests under explicit hypotheses on two velocity-pressure pairs. `NavierStokes/R3/ActualPressureFlux.lean` derives a comparison flux identity from that result. These are positive formal results, not absent infrastructure. They do not, without an additional selected-field theorem, establish an absolute global pressure representative or transport the five paper moments into the selected endpoint. The current conclusion is therefore **not established as a CMI solution because the load-bearing cross-layer correspondence remains unproved**, not because the source tree fails to contain R3, energy, or pressure modules.

Source-map evidence: `NavierStokesReview/evidence/source_tree_logic_map_2026-09-26.md` and `source_tree_logic_map_2026-09-26.json`.

## Periodisation and the radial observable

The selected-field calculation contains a domain transition that must be made
explicit. The source first forms a compactly supported cut potential and then
periodises the potential and direct branches. In symbols,

$$
\text{cutPotential}
\;\longrightarrow\;
\text{periodicVelocity}
\;\longrightarrow\;
\text{barMoment}.
$$

The first object has a compact support theorem, but the second is unit-periodic.
The final `barMoment` is a global Bochner integral in the real radial variable.
Consequently, compact support before periodisation does not imply radial support
or integrability of the selected pullback after periodisation. The review has
proved the relevant periodicity and the conditional support obstruction, but it
has not proved the missing support/integrability transport or a nonzero value.
This is a concrete unresolved correspondence failure under CTR-005, not an unconditional
contradiction.
## Reproducible source and dependency mapping

The audit infrastructure now separates four claims that are often conflated. The extracted tree fixes the inventory baseline; the live checkout fixes file contents and hashes; source parsing supplies navigation diagnostics; and the compiled Lean environment supplies the declaration-level dependency closure for `NavierStokesR3.theorem_1_1`. The last layer follows elaborated constants from `ConstantInfo` expressions and is the only layer used for endpoint reachability claims.

The 2026-09-26 run produced 30,721 project declarations and 327,757 compiled-environment edges in the endpoint closure. It also produced 50,191 source declarations and 186,194 token-reference diagnostics after the namespace parser correction. These are different observables. The source-token graph is useful for locating candidates, but cannot establish a kernel dependency. The endpoint closure contained no reachable `sorryAx` users; this does not imply that every repository file is free of `sorry`.

This strengthens the method without changing the mathematical verdict. The exported endpoint’s kernel-level validity remains distinct from the unproved selected-field transport theorem required to identify the complete Cartesian assembly with the paper’s five named moments. The reproducibility procedure is recorded in `NavierStokesReview/evidence/hardened_mapping_method_2026-09-26.md`.

The endpoint route audit corrects an important possible overstatement. `FiveRowRank`, `PositiveOrderMoments`, `MeanRankUpdate`, `MixedPeriodicAssembly`, and `DefectIncrementBounds.barMoment` are reachable in the compiled environment; they are not established as dead or orphaned branches. What remains unproved is the stronger field-level statement: that the values computed by those upstream constructions are equal to the five named moments of the final assembled Cartesian witness after localisation, curl, periodisation, summation, and R³ packaging. The review consequently records a correspondence obligation, not a kernel contradiction.

### Endpoint signature cross-examination

The raw source check adds an important qualification to the preceding finding.
`ActualCandidateAssembly.Witness` (`ActualCandidateAssembly.lean:1121-1151`)
is a proposition-valued definition built from nested existentials and
conjunctions, not a structure with named five-moment fields. Its selected
payload includes a stage schedule, three away extensions, a forcing field,
`CandidateProperties`, `CandidateConsequences`, the H³ blow-up limit, force
jet bounds, and endpoint jet identities. It contains no explicit
`PositiveOrderMoments.Debt`, `FiveRowRank.FiveRows`, `barMoment`, or equality
identifying `(M,I,J,S,C_p)` with the final Cartesian field.

This does not make the upstream moment modules irrelevant or dead. The
selected closure reaches them. It establishes a precise correspondence
failure instead: the exported endpoint does not state or prove the equality
that carries their values through the assembled `tsum`, curl, localisation,
periodisation, and radial observable. The interface-blindness probe only shows
that `StageEstimates` alone cannot determine a five-coordinate debt; it does
not show that the selected physical field is zero. The exact source ledger is
`NavierStokesReview/evidence/claim_cross_examination_2026-09-27.md`.

Evidence: `NavierStokesReview/evidence/selected_endpoint_routes_2026-09-26.md`.

## Reproducibility control for the code audit

The mapping was rebuilt with a four-layer authority model: the extracted tree
is a hashed inventory snapshot; the live checkout supplies file identity;
source parsing supplies navigation; and the compiled Lean environment supplies
elaborated declaration reachability. The validator also checks source-hash
drift and records the workspace state.

The captured run reaches the moment, periodisation, radial-observable, and R³
packaging declarations from `NavierStokesR3.theorem_1_1`. It records 22,958
exact source joins and retains 3 ambiguous and 7,760 unmatched environment
nodes rather than guessing. The endpoint closure has zero reachable `sorryAx`
users. These controls strengthen reproducibility but do not prove the missing
field-level equality between the final Cartesian assembly and the paper's five
named moments.

Method and reproduction: `docs/REVIEW_MAPPING_METHOD.md` and
`NavierStokesReview/src/audit/run_hardened_audit.ps1`.

## Reproducible repository mapping

The audit distinguishes inventory identity, source navigation, and elaborated
dependency. The extracted tree is hashed as an inventory snapshot; the live
checkout supplies file contents and hashes; source parsing supplies namespace-
aware declaration spans and token diagnostics; and the compiled Lean
environment supplies endpoint dependency evidence. The tree reconciliation
layer records 3,021 tree file entries, 3,058 live files, 2,997 unique
basename resolutions, 24 ambiguous entries, and no missing basenames. It
never assigns an ambiguous rendered tree entry to a path by guesswork.

For the selected endpoint, the run records 30,721 compiled declarations,
327,757 raw environment edges, 22,958 exact source-name matches, and 227,128
source-located joined edges, with zero reachable `sorryAx` users. These
measurements establish reproducible navigation and endpoint scope. They do
not establish that the five named paper moments equal the values of the final
assembled Cartesian field after localisation, curl, periodisation, summation,
and radial projection. That remains the load-bearing selected-path theorem.

To make that boundary auditable, the review includes a machine-readable claim
register at `NavierStokesReview/config/review_claims.json`, checked by
`claim_register.py`. The current register marks the endpoint route and axiom
hygiene as supported, force provenance as conditional, and CTR-005 as open. A
green structural register is not evidence that the missing Cartesian-to-radial
value equality has been proved.

## Complete repository map and evidence boundary

The audit now publishes a complete module map rather than relying on filenames
or a partial route list. The 2026-09-26 run accounts for all 2,790 Lean
modules, records 50,191 source declarations and 30,721 compiled project
declarations, and joins 22,958 compiled declarations to source spans exactly.
It retains three ambiguous joins and 7,760 unmatched environment nodes instead
of assigning them by guesswork. The captured endpoint has zero reachable
`sorryAx` users.

The current source map is available as machine-readable JSON and
human-readable Markdown under
`NavierStokesReview/evidence/hardened_source_map_2026-09-29.*`; its authority
order and reproduction command are in `docs/REPOSITORY_MAP_GUIDE.md`. This improves
source accountability and corrects path-level underclaims. It does not prove
that the final Cartesian field has the paper's five named moment values. That
value-level transport theorem remains the load-bearing CTR-005 question.

For human-readable source navigation, use `docs/REPOSITORY_ARCHITECTURE_MAP.html`; for the mathematical notation and endpoint route, use `docs/MATHEMATICAL_SPECIFICATION.md`; and for evidence authority and regeneration rules, use `docs/REPOSITORY_MAP_GUIDE.md` and `docs/REVIEW_DOCUMENT_CONTROL.md`.

## Current verification boundary

The source audit must be read at two levels. First, the repository genuinely
contains substantive five-moment and rank mathematics. `PositiveOrderMoments`
defines a five-coordinate debt and proves exact repair identities;
`FiveRowRank` defines the three-coordinate physical rank interface; and the
selected upstream route reaches both families, `MeanRankUpdate`, the mixed
periodic velocity, and `barMoment`. It is therefore inaccurate to describe the
five-moment branch as absent or dead.

Second, the exported endpoint still does not state the field-level identity
needed by the paper. `ActualCandidateAssembly.Witness` is a nested existential
proposition (`ActualCandidateAssembly.lean:1121-1151`). Its payload contains a
stage schedule, away extensions, forcing, `CandidateProperties`,
`CandidateConsequences`, the H³ limit, force-jet bounds, and endpoint jets. It
does not contain a `Debt`, `FiveRows`, `barMoment`, or an equality of the form

\[
  (M,I,J,S,C_p) = \mathcal{O}(u_{\mathrm{selected}},p_{\mathrm{selected}},f).
\]

The selected theorem at `ActualCandidateAssembly.lean:1177-1181` merely fixes
the construction parameters and invokes `witness`. Thus imports and upstream
repair identities establish reachability, not transport of their values
through the complete `tsum`, curl, localisation, periodisation, and radial
observable. This remains the load-bearing CTR-005 burden of proof.

The post-clean build status is also controlled. An aggregate fresh rebuild and
a bounded `NavierStokes.R3.Theorem` rebuild exceeded their execution limits
without emitting a Lean error. They are recorded as incomplete verification,
not as Lean failures or successes. The last completed compiled closure is the
dated 2026-09-26 export. See
`NavierStokesReview/evidence/fresh_build_status_2026-09-27.md`.

## Current source-coverage boundary: 2026-09-27

A source-only refresh now accounts for 2,790 Lean modules and 50,191 parsed
declarations in the current checkout. It records 3,021 extracted-tree entries,
2,997 unique-basename resolutions, 24 explicit ambiguities, and no missing
basenames. The scan finds no `unsafe`, `axiom`, or `admit` declarations. Four
actual `sorry` bodies remain in the standalone comparator challenge files;
the other six literal-token hits are explanatory comments, not proof holes.

This is repository inventory evidence, not a replacement for the compiled
endpoint closure. The latest completed closure is still dated 2026-09-26, and
the post-clean rebuild is incomplete. The source census therefore strengthens
file accountability without upgrading CTR-005 or converting the selected-field
correspondence gap into a kernel contradiction.

## Current route-scope clarification: 2026-09-27

The audit does not classify the five-moment branch as absent. Direct source
inspection shows that `PositiveOrderMoments` contributes slow-base and exterior
primitive identities, while `FiveRowRank`, `MeanRankUpdate`, and `barMoment`
occur in correction-state and stage-invariant routes reachable from the
selected endpoint. The remaining question is whether a declaration transports
those identities through the actual `potentialSum`, spatial curl,
localisation, periodisation, torus averaging, and final Cartesian packaging.

The endpoint constructor instead passes smoothness, divergence, joint residual
jets, away extensions, and origin blow-up to
`CandidateConsequences.mixed_exists_force_with_consequences`. Its exported
proposition contains no equality identifying the final `ASum`, `BSum`, or
`PSum` fields with `(M,I,J,S,C_p)`. Accordingly, this manuscript treats
CTR-005 as a selected-field transport obligation, not as a claim that the
upstream correction mathematics is dead code.

## Partial bridge inventory: 2026-09-27

The review-side completion layer contains genuine intermediate results that
must be distinguished from the missing endpoint theorem. It proves
finite-prefix curl expansions, the cutoff-gradient commutator, local radial
scalar formulae, torus-average and radial reductions, and typed `barMoment`
pullbacks. It also proves selected cycle/base moment facts. These results do
not, by themselves, evaluate the final infinite mixed Cartesian field or
identify its value with `(M,I,J,S,C_p)`.

The exact declarations and coordinates are recorded in
`NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.
The required theorem remains a value-level equality after `potentialSum`, curl,
localisation, periodisation, `torusAverage`, radial pullback, `barMoment`, and
axis/whole-space extension. No nonzero remainder has yet been calculated, so
the calibrated conclusion is an open correspondence obligation, not a
 kernel-level contradiction.

## Global cross-layer audit

The review was extended beyond the moment branch. The source proves a forced
whole-space energy identity and a uniform pre-singular finite-energy estimate
(`R3/CompactEnergy.lean:201-377`). It also proves smooth spatial
localisation, periodisation, divergence freedom, local agreement, origin
agreement, and residual-jet transfer (`MixedPeriodicAssembly.lean:51-245`).
The activation layer is smooth and agrees with the underlying field after
time `3/4` (`TimeLocalization.lean:27-160`). These results remove the earlier
energy-missing and cutoff-discontinuity objections.

Pressure recovery has a narrower scope. `PressureRecovery.gradient_recovery`
and `ActualPressureFlux.pressure_flux_eq_canonical` compare pressure
differences under equal-residual hypotheses. They do not, at the inspected
export boundary, provide a standalone absolute Poisson/Leray representation
for the selected pressure. Likewise, `CandidateFromLimits.force` is defined
from traced residual jets and is equal to the activated residual before time
one. This is evidence for force provenance and path dependence, not a literal
kernel contradiction of an existential force statement.

The complete lane-by-lane source ledger is
`NavierStokesReview/evidence/global_cross_layer_audit_2026-09-27.md`.

## Direct check of the proposed moment-transport junctions

The source audit also checked the architectural locations where a differently
named transport theorem would have to occur. The result is mixed, not empty.
`LocalPaperTheorem.lean:128-176` proves the selected local schedule and its
residual/exterior properties, while `PaperLocalization.lean:28-48` packages
local agreement with a compact candidate. `EntranceAlignedBase.lean:666-671`
proves a five-moment identity for the aligned base history. Separately,
`CorrectionState.lean:449-476` and `DefectIncrementBounds.lean:621-646,
775-813` prove `FiveRowRank.FiveRows`, correction-moment vanishing, and
stage-level preservation.

Those are genuine local results. They do not state the missing composition

\[
  (M,I,J,S,C_p)(u_{\mathrm{selected}},p,f)
  = (M,I,J,S,C_p)_{\mathrm{paper}}
\]

for the final field assembled through `potentialSum`, curl, localisation,
periodisation, torus averaging, and radial integration. The endpoint
`ActualCandidateAssembly.Witness` still exports the schedule, assembled sums,
regularity, residual, energy, blow-up, and boundary-jet predicates without
that value-level equality. Thus the audit confirms real upstream mathematics
and a real selected-path correspondence obligation at the same time.

The upstream route is stronger than this short junction list alone.
`GlobalSlowProfiles.profiles_moments`
(`GlobalSlowProfiles.lean:1043-1060`) proves all five rows for the constructed
positive-order profile sequence. `GlobalStressSupport.moments_zero`
(`GlobalStressSupport.lean:144-157`) transfers them to the axial and angular
histories, and `AssembledSlowBase.lean:592-617` uses the zero mass row to
prove an exterior primitive vanishes. These are transported local results;
the unresolved step is their identification with the final mixed Cartesian
fields after the complete assembly and projection chain.

## Current reproducibility boundary

The source census was refreshed on 2026-09-27 and indexed 2,790 Lean modules
and 50,191 declarations. A fresh compiled-environment replay could not yet be
completed because the current `.lake` directory lacks the endpoint object
`NavierStokes/R3/Theorem.olean`; a bounded rebuild attempt timed out. The
earlier compiled dependency join is consequently treated as a dated snapshot,
not as a fresh replay of the current checkout. This affects the status of the
compiler-closure evidence, not the source-level finding that upstream moment
theorems exist while the final selected-field value equality remains
unestablished. Full details are in
`NavierStokesReview/evidence/fresh_environment_replay_2026-09-27.md`.

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
is genuine reachable profile mathematics and must be included in any account
of the construction.

It does not, by itself, close the selected-field correspondence. The cited
identities concern two scalar outgoing-profile quantities used by the
correction/rank route. They do not identify the complete five named
observables with the final `ASum`, `BSum`, and `PSum` Cartesian fields after
curl, localisation, periodisation, infinite summation, torus averaging, and
radial pullback. The publication claim therefore remains **NOT ESTABLISHED**
because that final value-level identification is absent from the current
formal record.

## Endpoint assembly: what is proved and what is not

The source review does not characterise the final construction as disconnected.
`TailGaugePotential.finalPotential` is built from
`FinalSlowBase.vectorPotential`, and `finalPotential_sameCurl` identifies its
curl with `FinalSlowBase.velocity` on the pre-terminal region
(`TailGaugePotential.lean:433-450`). The initial potential is then decomposed
into the slow-base field, initial curl data, and direct angular data
(`ActualPhysicalStageBounds.lean:616-656`).

`ActualCandidateAssembly.lean:205-211` defines the zeroth potential from the
final base plus the initial increment. Its stage family, successor laws,
positive-stage curl/chart equalities, pressure equalities, and
`stageRealizations` are supplied at `:531-568` and `:1003-1077`. The exported
endpoint forms `ASum`, `BSum`, and `PSum` at `:1125-1151`, then applies
localisation, periodisation, and time activation before checking
`CandidateProperties`. `MixedPeriodicAssembly` supplies corresponding field
smoothness, periodicity, local equality, and divergence-transfer results.

The unresolved point is therefore not whether Cartesian fields are assembled.
It is whether the paper's named observables are evaluated on those final fields
after all of those operations. The reachable moment declarations prove
profile/history identities such as `massMoment_endpoint` and
`angularMoment_endpoint` (`OutgoingSchedule.lean:739-950`) and outgoing-tail
preservation (`OutgoingTail.lean:908-923`). The audit has not found a theorem
identifying those scalars with the five named observables of the activated,
periodised `ASum`/`BSum`/`PSum` field. This remains a selected-field
value-level correspondence obligation, not a dead-code claim.

The audit also confirms a genuine logarithmic profile/history bridge.
`NominalConeAssembly.lean:366-446` proves chart identities for the outgoing
quantities \(M,J,I,S\), while `Witness.log_histories`
(`NominalConeAssembly.lean:452-470`) maps them to the outgoing and heat-switch
histories; parameter transport continues at `:596-667`. These results are
part of the actual upstream construction. Their codomain is profile/history
data, however, not the final activated Cartesian `ASum`/`BSum`/`PSum` field.
They therefore strengthen the positive source record without supplying the
remaining endpoint observable calculation.

The scope of the finite-modification record is narrower than the full paper
mechanism. `AssembledSlowBase.FiniteModification`
(`AssembledSlowBase.lean:1514-1529`) stores field and pressure agreement
together with one explicit mass equality. The remaining local profile and
rank identities are supplied by separate theorems. This is not evidence that
the five-moment construction is absent; it is evidence that the record itself
is not the final five-moment certificate for the selected Cartesian field.

## Local Cartesian coherence

The source also contains a genuine local Cartesian realisation layer in
`ActualPrimaryCoherence.lean:1866-1940`. It defines Cartesian potentials and
their spatial curls, and proves smoothness, axis behaviour, the piece-to-
Cartesian velocity relation, the corresponding pressure representation, and
divergence-freeness on the stated domains. The review therefore does not claim
that the Cartesian field layer is absent. The remaining question is whether
the five profile observables are evaluated on the final mixed
`ASum`/`BSum`/`PSum` fields after the complete endpoint composition.

## Paper-grounded significance of the missing selected-field theorem

The paper itself establishes why the remaining transport question is
load-bearing. In Section 4.2, equation (4.15), the authors define the five
cumulative radial quantities \(M,I,J,S,C_p\); Lemma 4.4 says that matching them
at a joining radius preserves the radially integrated exterior pressure, radial
velocity, and stress. Section 5.2, equations (5.10)--(5.11), then uses a
five-equation correction system to remove exterior pressure and stress terms.
The localisation sections further state that spatial cutoffs are applied to
vector potentials before differentiation so incompressibility is retained, and
that the cutoff/curl contributions are included in the full residual.

Accordingly, the audit does not ask for a cosmetic restatement of an upstream
profile lemma. The required selected-path theorem must evaluate the advertised
observables on the final Cartesian field after the concrete sequence

\[
\text{profile stages}\;\longrightarrow\;\texttt{tsum/potentialSum}
\longrightarrow\;\operatorname{curl}
\longrightarrow\text{cutoffs and periodisation}
\longrightarrow\text{torus average and radial pullback}
\longrightarrow\;(M,I,J,S,C_p).
\]

The source contains genuine upstream certificates, rank identities, outgoing
profile identities, and local Cartesian curl constructions. The inspected
endpoint still exposes no theorem with this final input/output relation. This
supports CTR-005 as a failure to establish that the Lean endpoint formalises
the paper's advertised mechanism. It does not, by itself, prove that the
selected field has an incorrect moment, produce a nonzero remainder, or derive
kernel-level `False`. Those stronger conclusions require a completed field-level
calculation or an impossibility theorem.
## Partial bridges found in the review tree do not close the selected-field theorem

The review must distinguish absence of an endpoint theorem from absence of all intermediate work. The source tree contains real partial constructions: a typed selected mixed scalar pullback, an exact auxiliary torus-average reduction, a finite-prefix/`tsum` jet-scope result, a cutoff--curl commutator identity, and a positive-radius Cartesian recovery formula. These results make the remaining obligation more precise; they do not make it disappear.

The outstanding theorem is still the value-level statement for the final activated Cartesian field, with every operation in the paper's route represented:

\[
u_{\mathrm{selected}}
\xrightarrow{\mathrm{component/pullback}}
\operatorname{torusAverage}
\xrightarrow{\mathrm{radial\ integral}}
(M,I,J,S,C_p).
\]

The completion `PeriodicGlobalIntegral.selected_mixed_barMoment_zero_of_positive_pullback` must not be cited as that theorem. It assumes strict positivity of a periodic pullback on a fundamental interval, derives non-integrability, and uses the convention `integral_undef` to return zero. The positivity premise is not proved for the selected field, so the result is a conditional semantic warning about the global Bochner-integral definition, not a physical moment evaluation.

Accordingly, the calibrated conclusion is: upstream moment certificates and review-side partial bridges are genuine, but the paper-to-endpoint transport of the five cumulative moments remains unestablished on the inspected Lean record. This is a correspondence failure, not yet a kernel-level contradiction.

## Source-tier re-audit: profile, rank, localisation, and selected construction

The higher-priority source tier narrows the finding further. `PositiveOrderMoments.lean:21-23,77-84,192-301` defines a genuine five-coordinate debt and proves exact profile-level repair and target-moment identities. Its later pressure and flux theorems require explicit zero-moment hypotheses. `MeanRankUpdate.lean:24-44,137-169,195-200` separately defines the three-coordinate physical debt, scaling, and `FiveRows` for correction increments. These are substantive certificates, not dead imports, but their codomains are profile or correction layers rather than the exported selected Cartesian field.

`ActualCandidateConstruction.lean:205-257,289-345,832-970` constructs the selected cycle, chart velocity and pressure stages, direct and stream mean stages, and potential-stage field equalities. `SpatialLocalization.lean:164-203,209-290,313-340` then proves the actual cutoff-before-curl identity, exposes the cutoff-gradient commutator, periodises the fields, and establishes local equality, periodicity, divergence freedom, and residual equality. These results validate substantial intermediate mathematics and also show why the remaining theorem is nontrivial: the commutator and all subsequent transformations must be included in any moment calculation.

The pressure-side source is similarly substantive but scoped. `GlobalSlowProfiles.lean:167-205,281-334,337-400` proves reduced profile/history and cutoff-lift identities, while `TerminalPressure.lean:39-145,149-239,406-627` proves smoothness, integrability, and derivative identities for a canonical presingular heat-tail pressure on its stated positive-radius domain. Neither inspected path supplies the absolute final-field Poisson/moment identity required to identify the exported whole-space witness with the paper's five observables.

Thus the strengthened conclusion is not that OpenAI lacks the five-moment engine. The source contains real local engines and several transformations. The unresolved burden is the composed selected-path theorem:

\[
\text{profile/correction certificates}
\to \text{selected stages}
\to \texttt{tsum/potentialSum}
\to \operatorname{curl}(\chi A)
\to \text{periodisation}
\to \text{torusAverage/radial pullback}
\to (M,I,J,S,C_p).
\]

Until that value-level statement, or a concrete impossibility theorem for it, is proved, the appropriate classification remains **not established as paper-to-code correspondence**, not unconditional formal refutation.

## Correction and residual tier: what the additional source review establishes

The next source tier does not weaken the audit by revealing empty scaffolding. `InitialPhysicalData.lean:40-114,141-211,258-355,404-488,535-572,589-685` constructs selected physical coefficients, carriers, pressure coefficients, and support/domain facts. `CorrectionStep.lean:66-225,231-342,396-519,611-739,1024-1110,1173-1190` retains the nonlinear covariance, transport, pressure, and residual cross-terms of a correction cycle. `BaseResidual.lean:36-116,611-666,708-739,776-826,842-910,1024-1110` constructs asymptotic slow-base sums, Cartesian prefixes, spatial-curl rate bounds, pressure prefixes, and axis/growth estimates.

These are positive source findings. They show that the correction, physical-data, and residual layers are mathematically populated and feed substantial intermediate constructions. They still do not supply the final value-level equality

\[
  \operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f)
  =(M,I,J,S,C_p)
\]

after the complete `tsum`/`potentialSum`, curl, localisation, periodisation, torus-average, radial-pullback, support/integrability, and axis-extension route. The appropriate conclusion is therefore neither that the mechanism is absent nor that a nonzero defect has been found. The current source record leaves the selected-field transport unestablished; the advertised paper-to-Lean correspondence is rejected on this record unless direct evidence changes it.

## Further source tier: slow residuals, stress primitives, resets, and chart transport

The next five priority-ranked modules were inspected directly. `SlowBorelBase.lean`
constructs smooth slow series with finite-prefix, tail, derivative, and sum-map
bounds, including pressure and stress coefficient data. `SlowResidualMatching.lean`
provides reduced slow residual and stress primitives, radial identities, and
truncation/tail decompositions. `SignedStressPrimitive.lean` constructs compact
signed bumps with exact weighted moment cancellation and proves physical pullback,
torus-support, and chart finite-jet properties. `UniformAngularReset.lean`
proves uniform invertibility and smooth scheduled reset identities for an angular
moment system. `MeanChartCompatibility.lean` proves scaling and pullback/naturality
statements for cutoffs, torus averages, pressure, temporal families, source
moments, and debt/rank data.

These are positive findings: the upstream construction is populated and contains
substantive correction and transport mathematics. They do not, however, evaluate
\((M,I,J,S,C_p)\) on the complete selected `ASum`/`BSum`/`PSum` field after
summation, curl, localisation, periodisation, torus averaging, radial pullback,
support/integrability, and axis extension. The remaining requirement is a
composed selected-field theorem or a concrete calculation proving that the
composition is impossible. This tier supplies neither a nonzero remainder nor
kernel-level `False`.

The R3 packaging layer was checked separately. `R3/ActualCandidate.lean`
genuinely packages localized velocity and pressure fields with a smooth
positive-time force, residual equality, compact support, and finite-energy
bounds. `ActualInitialization.lean` and `FinalSlowBase.lean` supply populated
initial and slow-base data, while `TerminalStress.lean` and `MeanResidual.lean`
provide terminal-stress and angular-mean residual identities. These findings
strengthen the evidence for a real construction. They do not change the
endpoint result: the R3 candidate predicate still does not state that the final
Cartesian field realizes \((M,I,J,S,C_p)\).

The formal contract was also checked at its source definition. `ProblemStatement.lean`
defines the candidate proposition with smoothness, periodicity, support,
divergence, residual, energy, initial-value, and speed conditions, and explicitly
does not assert existence in that module. `PeriodizedWaveBounds.lean` supplies
local-finite copy-sum and jet bounds; `GaugeMomentBalances.lean` supplies
measured moving-gauge pressure moments; `BaseExterior.lean` supplies canonical
heat-exterior identities; and `ActualBaseResidual.lean` supplies fixed-base
chart and residual identities. These are genuine intermediate results. None
changes the fact that the final exported contract does not state the selected
Cartesian equality for the five paper observables.

### Audit calibration after the additional external comments

The latest adversarial comments sharpen the correct research question but also
contain claims that the source does not yet establish. The Lean source has real
profile, correction, Cartesian-curl, localisation, residual, energy, and R3
packaging results. The unresolved issue is narrower and more consequential:
the inspected endpoint does not export a theorem evaluating the final selected
Cartesian field against the five paper observables after the full
`tsum`/`potentialSum`, curl, localisation, periodisation, torus-average,
radial-pullback, support, integrability, and axis route.

The cutoff-gradient commutator is therefore a required term in the calculation,
not yet a proved nonzero defect. Similarly, the moment-blindness of the generic
`StageEstimates` interface does not show that the concrete selected field is
zero or that all upstream moment-dependent estimates are bypassed. These
distinctions keep the paper adversarial without converting an open calculation
into an unsupported kernel refutation. The current classification remains
**not established as a paper-to-code correspondence under CTR-005** until a
concrete remainder, impossibility theorem, or complete positive bridge is
obtained.

### Additional correction/state tier

The subsequent source check found further real intermediate mathematics rather
than empty scaffolding. `CorrectionState.lean` carries concrete radial pressure
moments, reconstructed residuals, and rank-model `FiveRows`; `HeatTailEdit.lean`
proves weighted heat-tail pressure, energy, angular-debt, and jet estimates;
and `ActualMeanPhysicalData.lean` transports atlas, gauge, rank, temporal, and
native-jet data through cycle stages. These results narrow the audit but do not
evaluate the final selected Cartesian field against `(M,I,J,S,C_p)` after the
full sum/curl/localisation/periodisation/radial-observable composition.

## Latest reachable tier: continuation, slow base, rebase, and rank coherence

The next source pass inspected eight additional reachable modules. The results
are substantive and refine the audit boundary:

`OffplaneCorrectionExtensions.lean` extends positive-radius slow pressure and
rank models to supported Cartesian continuation data. `SlowBaseEndpoint.lean`
lifts profile, potential, velocity, and pressure data to smooth away extensions.
`ConstructedSlowBase.lean` constructs an axisymmetric potential and its spatial
curl, then proves finite identities, stress-zero-core statements, jet flatness,
smoothed divergence-free fields, speed growth, and residual identities for
nominal and modified scales. `BasePrefixIdentity.lean` proves finite-prefix
curl/profile, radial-flux, pressure, stress-force, and coefficient-match
identities. `ActualReferenceRebase.lean` proves rebase and pullback identities
for actual stage contexts, residual sources, frames, amplitudes, pressures,
phases, and periodic subcovers. `HarmonicWaveInteraction.lean` proves local
harmonic-block, zero-mode, convolution, nonlinear-interaction, divergence, and
residual-difference identities. `ActualPrimaryDynamics.lean` supplies copied
primary pulse geometry, velocity/pressure germs, cutoff/curl smoothness, and
local residual formulas. `RankStateCoherence.lean` supplies fibre moments,
measured debt, normalised rank stages, and `FiveRows` conclusions for correction
state slices.

This tier rules out another weak description: the repository is not merely a
collection of disconnected profile names. It contains real local bridges from
reduced data to Cartesian fields and correction states. It still does not prove
that the final selected `ASum`/`BSum`/`PSum` field has the paper tuple
\((M,I,J,S,C_p)\) after summation, curl, localisation, periodisation, torus
averaging, radial pullback, support/integrability, and the axis limit. The
cutoff-gradient commutator remains a term that must be evaluated, not a proved
nonzero defect. The current classification therefore remains **not established
as a paper-to-code correspondence under CTR-005**, with no kernel `False`
obtained. The coverage register now contains 85 explicit source reviews and
513 reachable modules awaiting semantic classification.

## Latest source tier: axisymmetric residual and mean-residual routes

Four further reachable modules were inspected after the continuation and rank
tier. `AxisymmetricResidual.lean` proves exact regular-axisymmetric Cartesian
velocity, pressure, divergence, derivative, Laplacian, and Navier--Stokes
residual formulas, including an on-axis route. `PhysicalParticularWave.lean`
proves actual particular-wave carrier, potential, curl, pressure, chart-change,
periodicity, and reference-domain transport identities. `LeadingStress.lean`
proves reduced angular/axial stress divergence, pressure differentiation,
positive-radius radial pullback, and physical residual transport. Finally,
`LiftedMeanResidual.lean` proves smooth angular averaging, periodic invariance,
conservative flux identities, averaged differential operators, and nonlinear
residual lifting.

These are real local bridges and further reject the claim that the repository
contains only disconnected profile names. They still do not evaluate the final
selected Cartesian field against \((M,I,J,S,C_p)\) after the complete
sum/curl/localisation/periodisation/torus-average/radial-pullback,
support/integrability, and axis route. No nonzero remainder, impossibility
theorem, or kernel `False` was found. The register now records 85 explicit
source reviews and 513 reachable modules awaiting semantic classification.

## Latest source tier: wave bounds, signed data, and primary residuals

The latest source pass inspected four reachable modules directly.
`LinearWaveBounds.lean` contains actual wave coefficients, cutoff and curl
corrections, input bounds, wave classes, exact conditions, and coefficient-level
harmonic residual identities. `ActualPhysicalStageBounds.lean` derives
physical-stage smoothness, support, jet, potential, pressure, and gain bounds
from coherent mean and wave inputs. `ActualSignedWaveData.lean` constructs
signed support cells, potential and pressure copy families, carriers, source
amplitudes, frequency identities, and native stage data. `PrimaryResidualClass.lean`
defines primary correction inputs, invariant angular data, curl-corrected wave
classes, exact conditions, divergence, linear residual, field projection, and
smooth primary coefficients.

These declarations are substantive intermediate mathematics. They do not,
on the inspected source, prove the final selected Cartesian field's
`(M,I,J,S,C_p)` after the complete `tsum`/`potentialSum`, curl of the
localised potential, periodisation, torus averaging, radial pullback,
support and integrability, and axis-limit route. In particular, the source
does not justify the stronger claim that a cutoff-gradient commutator is
automatically nonzero. That remains a value-level calculation target. No
zero-sorry nonzero remainder, impossibility theorem, or kernel `False` was
obtained in this tier. The coverage register now contains 85 explicit source
reviews and 513 reachable modules awaiting semantic classification.

## Latest source tier: initial mean, cycle prefixes, and moment resets

The latest source pass inspected four reachable modules directly.
`ActualInitialMeanEquation.lean` proves initialized angular data, local
mean/divergence, periodicity, mean-zero, primary-sum divergence, and
initialized full-divergence identities. `CyclePhysicalPrefixes.lean` defines
cylindrical and local Cartesian velocity/pressure maps, stage updates, finite
prefixes, potential/direct splits, and local residual-prefix identities under
explicit curl-realisation hypotheses. `FiveProfileMoments.lean` contains a
genuine five-coordinate reduced-profile debt map, exact linear moment maps,
continuous-linear equivalence, compact correction families, and jet bounds.
`AngularMomentReset.lean` contains an invertible local angular/pressure reset
with a pressure-neutral branch and exact endpoint adjustment.

These are substantive intermediate certificates. They do not identify their
reduced or local moments with the final selected Cartesian `ASum`/`BSum`/`PSum`
field after `tsum`, curl, localisation, periodisation, torus averaging,
radial pullback, support/integrability, and the axis limit. No nonzero
remainder, impossibility theorem, or kernel `False` was obtained. The live
coverage register now contains 85 explicit source reviews and 513 reachable
modules awaiting semantic classification.
### Latest source tier: graph, interaction, axis, pulse, rebasing, and stress review (2026-09-28)

The source audit additionally inspected `GraphCalculus.lean`, `LocalizedMeanInteraction.lean`, `NaturalAxisRange.lean`, `PulseGrowth.lean`, `TorusMeanRequestRebase.lean`, and `BaseStressClasses.lean`. These files contain real off-axis derivative identities, local interaction/rate classes, axis-root and cutoff parameter results, scalar pulse-growth classification, exact request rebasing, and weighted base-stress estimates. They do not state the final selected-field identity evaluating `(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation/torus-average/radial route. The register now records 335 evidence-inspected reachable modules and 278 reachable modules still open. No nonzero remainder, impossibility theorem, or kernel `False` is claimed.

## Latest source tier: assembly, geometry, and axis-series review (2026-09-28)

The latest direct source pass inspected `PrimaryFieldAssembly.lean`,
`R3/ComparisonGronwall.lean`, `UniformHarmonicInteraction.lean`,
`ActualCycleGeometry.lean`, `ActualPolarCoverage.lean`, and `AxisSeries.lean`.
These files add genuine periodised vector-field assembly, source and covariance
identities, comparison/radius bounds, uniform harmonic interaction estimates,
actual-cycle geometry identifications, axis-aware polar coverage, and explicit
scalar axis-series analysis. They do not provide the final selected-field
identity evaluating `(M,I,J,S,C_p)` after the complete sum/curl/localisation,
periodisation, torus-average, radial-pullback, support/integrability, and axis
route. The current register records 329 evidence-inspected reachable modules
and 284 reachable modules still open. No nonzero remainder, impossibility
theorem, or kernel `False` is claimed from this tier.

### Latest source tier: scales, endpoint coordinates, and R3 comparison estimates (2026-09-28)

The source audit additionally inspected `ChartScales.lean`, `EndpointCoordinates.lean`, `R3/CompactComparisonBounds.lean`, and `R3/ComparisonFiniteEnergy.lean`. These files contain genuine native coefficient/asymptotic bounds, endpoint similarity-coordinate and Cartesian jet agreement, compact comparison estimates, and finite-energy/tensor-difference estimates. They do not state the final selected-field identity evaluating `(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation/torus-average/radial route. The register now records 339 evidence-inspected reachable modules and 274 reachable modules still open. No nonzero remainder, impossibility theorem, or kernel `False` is claimed from this tranche.
### 2026-09-28 priority-69 source tranche: nine modules registered

Direct source review completed for `AnnularEndpoint.lean`, `AxisContraction.lean`, `PhysicalCopyBounds.lean`, `R3/LocalizedFluxEstimates.lean`, `ResetEnergyBounds.lean`, `ScaledActualParticularControl.lean`, `TerminalCone.lean`, `ViscousPropagator.lean`, and `VolterraAnalyticBounds.lean`. These modules add substantive support/germ, periodisation, reduced-axis, tail-energy, cone, coefficient-propagator, and analytic Volterra bounds. They do not state the final selected Cartesian `torusAverage`/`barMoment` transport theorem, and this tranche yields no nonzero defect, impossibility theorem, or kernel `False`.

The regenerated full semantic register now reports **355 evidence-inspected reachable modules** and **258 reachable modules still open**. The authoritative outputs are `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`, `.md`, and `.html`, mirrored under `docs/`. Detailed evidence is in `NavierStokesReview/src/audit/priority_69_annular_axis_copy_flux_reset_cone_propagator_source_review_2026-09-28.md`.

### 2026-09-28 priority-70 source tranche: activation, wave regularity, base context, and copy-solve transport

The source audit additionally inspected `ActivationBounds.lean`, `ActualWaveRegularity.lean`, `CommonBaseContext.lean`, and `CopySolveCompatibility.lean`. These files contain genuine activation-factor bounds, smooth actual-wave/curl/tsum regularity, common base/stress context, and generic copy-solve transport. They do not state the final selected-field identity evaluating `(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation/torus-average/radial route. The register now records 359 evidence-inspected reachable modules and 254 reachable modules still open. No nonzero remainder, impossibility theorem, or kernel `False` is claimed from this tranche.

### 2026-09-28 priority-71 source tranche: curl realization, diagonal extensions, carrier binding, and finite heads

The source audit additionally inspected `LocalizedCurlRealization.lean`, `MixedDiagonalExtensions.lean`, `ActualCarrierTransport.lean`, and `FiniteHeadClass.lean`. These files contain genuine patchwise curl/divergence and germ identities, potential support/extension, canonical carrier binding, and finite-prefix jet-class transfer. They do not state the final selected-field identity evaluating `(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation/torus-average/radial route. The register remains at 359 evidence-inspected reachable modules and 254 reachable modules still open because these rows were previously evidence-classified. No nonzero remainder, impossibility theorem, or kernel `False` is claimed from this tranche.

### 2026-09-28 priority-72 source tranche: pulse, geometry, time averages, and first-order edge

The source audit additionally inspected `CorrectedPulseAmplitude.lean`, `PrimaryGeometryAssembly.lean`, `R3/ComparisonTimeAverages.lean`, and `SlowFirstOrderEdge.lean`. These files contain genuine corrected energy-reset, reduced geometry, finite-energy time-average, and conditional radial-stress results. `SlowFirstOrderEdge` explicitly delegates global moment closure to separate renormalized-moment and slow-order theorems. The tranche does not state the final selected-field identity evaluating `(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation/torus-average/radial route. The register now reports 363 evidence-inspected reachable modules and 250 reachable modules still open. No nonzero remainder, impossibility theorem, or kernel `False` is claimed from this tranche.

### 2026-09-28 priority-73 source tranche: base velocity, representatives, context, and reserved patches

The source audit additionally inspected `ActualBaseVelocityBounds.lean`, `BaseContextAssembly.lean`, `PhaseEstimates.lean`, `PrimaryRepresentatives.lean`, `PositiveRepresentatives.lean`, and `ReservedPatches.lean`. These files contain genuine actual coefficient/support and rate identities, reduced stress realisation, phase and representative geometry, and radial `FiveProfileMoments`/`FiveRowRank` patch identities. They do not state the final selected-field identity evaluating `(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation/torus-average/radial route. The register now reports **369 evidence-inspected reachable modules and 244 reachable modules still open**. No nonzero remainder, impossibility theorem, or kernel `False` is claimed from this tranche.
## Audit coverage note: 2026-09-28

The source audit has now directly classified 375 of 588 reachable modules; 238 remain open in the live register. The latest six-module tranche concerns activation collars, particular controls, smooth extensions, local physical bounds, and moving-frame/modal estimates. It does not establish the selected Cartesian transport of `(M,I,J,S,C_p)`, and it does not establish a nonzero defect or kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_74_activation_control_extension_frame_source_review_2026-09-28.md`.
## Audit coverage note: 2026-09-28 cutoff/Volterra/wave-interaction tranche

The source audit has now directly classified 381 of 588 reachable modules; 232 remain open in the live register. The latest six-module tranche confirms real summation, angular moment, tail-energy, and separated-curl identities. It does not establish the complete selected Cartesian transport of `(M,I,J,S,C_p)`, nor a nonzero defect or kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_75_wave_cutoff_volterra_sum_loop_tail_interaction_source_review_2026-09-28.md`.
## Audit coverage note: 2026-09-28 radial/chart/integral tranche

The source audit has now directly classified 392 of 588 reachable modules; 221 remain open in the live register. The latest eleven-module tranche confirms actual base-radial and radial-integral identities, but does not establish the complete selected Cartesian transport of `(M,I,J,S,C_p)`, a nonzero defect, or a kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_76_radial_chart_jets_extension_rephase_integral_source_review_2026-09-28.md`.

## Audit coverage note: 2026-09-28 axis/dilation/extension/ODE tranche

The source audit has now directly classified 400 of 588 reachable modules; 213 remain open in the live register. `OutgoingDilation.lean` supplies direct reduced-profile `M`, `I`, `J`, `S`, and axis-datum definitions and identities. This positive evidence narrows, rather than closes, the paper-to-code question: no complete selected Cartesian transport theorem, nonzero defect, or kernel contradiction was established in this tranche. Evidence: `NavierStokesReview/src/audit/priority_77_axis_evaluation_resolvent_phase_gaussian_dilation_extension_ode_source_review_2026-09-28.md`.

### 2026-09-28 priority-78 source tranche

The source audit has now directly classified **414 of 588 reachable modules; 199 remain open**. The latest tranche confirms substantive phase-defect and phase-jet identities, axis harmonic algebra, coefficient/radial weight estimates, polar and edge regularity, stress activation, and weighted Volterra integral regularity. These findings strengthen the intermediate mathematical record but do not establish complete selected Cartesian transport of `(M,I,J,S,C_p)`, a nonzero `Delta m`, impossibility, or a kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_78_phase_defect_axis_algebra_weighted_volterra_source_review_2026-09-28.md`.

### 2026-09-28 priority-79 source tranche

The source audit has now directly classified **420 of 588 reachable modules; 193 remain open**. The latest tranche confirms substantive axis-operator, chart/component, matching-cone, physical-coordinate, signed-covariance, and moving-edge extension mathematics. These findings strengthen the intermediate record but do not establish complete selected Cartesian transport of `(M,I,J,S,C_p)`, a nonzero `Delta m`, impossibility, or a kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_79_axis_chart_matching_coordinate_covariance_edge_source_review_2026-09-28.md`.
## Audit update: reduced radial transport evidence (2026-09-28)

The latest source tranche prevents an overstatement in the manuscript. The repository does contain exact reduced radial pullback identities and weighted `MeanClass` transport (`RadialPullback.lean`, `WeightedRadialPrimitive.lean`), and `ReferencePath.histories` explicitly rebuilds reduced pressure/moment data from a reference path. The unresolved claim is narrower and stronger: the reviewed code does not expose a theorem composing those reduced identities with the selected 3D Cartesian curl, localisation, `tsum`, periodisation, and public `Witness` field so as to establish the paper tuple `(M,I,J,S,C_p)` for the selected endpoint. The manuscript should therefore say “selected endpoint correspondence not established”, not “moment machinery is absent”.
## Audit update: concrete R3 and reduced-moment bridges (2026-09-28)

The source review now confirms concrete intermediate bridges that the manuscript must acknowledge. `OutgoingSchedule` proves two exact combined reduced moment cancellations; `GaugeRadialResidualBounds` identifies a pressure defect with the auxiliary-torus-averaged zeroth radial mass; `MixedDiagonalResidual` defines the residual from the actual potential sums and proves physical joint zero jets; and `R3CompactCandidate` transfers periodic local properties to compact whole-space fields. The defensible criticism is therefore not that moment machinery is absent. It is that the full five-observable selected-Cartesian composition and its export through `Witness` remain unestablished.

## Audit update: actual debt, exterior, scaling, and entrance layers (2026-09-28)

The latest source review adds further positive evidence. `ActualIntermediateDebtBounds` derives three-component debt from checked correction-step data; `ActualMeanExterior` proves annular exterior vanishing for actual mean and cycle families; the R³ scaling modules establish exact energy and support transformations; `R3ActualCandidate` wraps the selected witness into a compact whole-space candidate; and `NaturalEntrance` proves exact reduced angular and axial source-flux identities. These results must be included in any fair account of the formalisation. They still do not establish the full selected Cartesian `(M,I,J,S,C_p)` transport theorem, so the manuscript retains the calibrated status “selected endpoint correspondence not established”, not an unconditional `False` claim.

## Audit update: localisation and physical-profile components (2026-09-28)

The next six source reviews add exact squared partition normalisation, actual mixed curl-plus-angular field and divergence identities, Gaussian tail and all-order jet bounds, leading-stress edge/exterior controls, signed torus/radial request identities including zero adjusted moments, and a positive pulse covariance cone. These are substantive components of the construction and must not be reduced to a generic rate-interface description. They still do not supply the complete selected Cartesian `(M,I,J,S,C_p)` transport theorem through curl, localisation, `tsum`, periodisation, and public `Witness`; the calibrated conclusion remains correspondence not established.

## Audit update: residual grouping, diagonal rates, and compact force (2026-09-28)

The latest source tranche records genuine axisymmetric and finite local residual grouping, diagonal stage-to-limit jet/curl estimates, compact temporal and spatial force decay, and a uniform pre-singular \(R^3\) compact-force \(L^2\) bound. These results strengthen the regularity and force-admissibility record. `DiagonalResidual` proves all-order flatness order-by-order with stage choices; it is not a fixed-tail weighted radial-moment theorem. The reviewed tranche still does not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport through `Witness`, and does not establish `Delta m != 0`, impossibility, or a kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_87_residual_grouping_decay_compact_force_source_review_2026-09-28.md`.

## Audit update: profile cones, covers, similarity, and mean updates (2026-09-28)

The latest source tranche confirms actual reduced cone/stress and loop-moment algebra, analytic axis and heat-profile extensions, anisotropic similarity-chart transitions, an explicit Cartesian axisymmetric curl lift with support bounds, periodised-copy solves, and temporal mean updates. These are substantive parts of the formal construction and must be represented as positive intermediate evidence. They still do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through the public `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_88_profile_cone_cover_similarity_mean_source_review_2026-09-28.md`.

## Audit update: moment repair, stress, alias, and curl covariance (priority 89, 2026-09-28)

The latest source tranche confirms compact reduced moment repair, exact abstract repair, torus inverse and alias transport, reduced stress identities, local gauge-mass preservation, and strong cylindrical/Cartesian curl covariance. These are substantive parts of the construction and must not be omitted. The reviewed declarations still do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through the public `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_89_moment_repair_stress_alias_curl_source_review_2026-09-28.md`.

## Audit update: moment matrices, prepared profiles, Gaussian bounds, and smooth repair (priority 90, 2026-09-28)

The latest source tranche confirms nonsingular generalised-power and bump moment matrices, scheduled and prepared outgoing profiles, whole-space Gaussian integrability, and smooth/analytic abstract quadratic repair. These are substantive upstream components and must be represented positively. They still do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through the public `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_90_moment_matrix_prepared_profiles_gaussian_solver_source_review_2026-09-28.md`.

## Audit update: torus inversion and periodic phase assembly (priority 91, 2026-09-28)

## Audit update: R3 energy, force, polar graph, and uniform curl layers (priority 92, 2026-09-28)

The next direct source tranche confirms genuine R3 force-norm and viscous-dissipation accounting, smooth positive-time force support, an off-axis physical polar-graph reconstruction, scalar forced Gronwall estimates, and broad uniform primary/curl rate propagation. These results correct any suggestion that the R3 energy or temporal-cutoff machinery is merely absent. They remain intermediate correspondence evidence: they do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_92_r3_energy_force_polar_graph_uniform_weights_source_review_2026-09-28.md`.

The latest direct source review confirms a substantive parametric torus-inverse layer and a substantive periodic-phase assembly layer. These modules prove smooth parameter/torus regularity, zero-mean and periodicity properties, Fourier inverse and multiplier estimates, rapid decay, finite-jet bounds, compact clock windows, locally finite tsum periodisation, phase/angular-lift identities, geometry transport, and carrier-adapter germ/jet facts. They strengthen the positive construction record. They do not, by themselves, expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_91_parametric_inverse_periodic_phase_source_review_2026-09-28.md`.

## Audit update: limits, debt matching, lifespan, reindexing, pulse history, and radial flux (priority 93, 2026-09-28)

The latest direct source tranche confirms genuine joint boundary-limit and flat-residual extensions, reduced five-coordinate matching/debt bounds, relative maximal-lifespan consequences, exact reindexing of mean and residual rate classes, explicit pulse energy-history bounds, and an off-axis radial-flux residual identity. These are substantive intermediate components and must not be omitted. They still do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_93_limits_debt_lifespan_reindex_pulse_flux_source_review_2026-09-28.md`.
## Audit update: limits, debt matching, lifespan, reindexing, pulse history, and radial flux (priority 93, 2026-09-28)

The latest direct source tranche confirms genuine joint boundary-limit and flat-residual extensions, reduced five-coordinate matching/debt bounds, relative maximal-lifespan consequences, exact reindexing of mean and residual rate classes, explicit pulse energy-history bounds, and an off-axis radial-flux residual identity. These are substantive intermediate components and must not be omitted. They still do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_93_limits_debt_lifespan_reindex_pulse_flux_source_review_2026-09-28.md`.
## Audit update: histories, initial means, harmonic support, exterior prefixes, and signed families (priority 94, 2026-09-28)

The latest direct source tranche confirms genuine reduced history/repair identities, initial mean/covariance/rank data, harmonic coefficient/support calculus, exterior prefix and germ agreement, a local particular-mean covariance gain, and signed potential/pressure support. These are substantive intermediate components and must not be omitted. They still do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_94_histories_means_harmonic_exterior_source_review_2026-09-28.md`.

## Audit update: core support, time localization, comparative pressure, and uniform bounds (priority 96, 2026-09-28)

The latest direct source tranche confirms concrete core/support geometry, signed unmasked and uniform block bounds, off-plane and oscillatory-curl estimates, smooth time localization with an explicit switched residual formula, comparative weak pressure/Poisson identities, compact pressure-flux tests, Riesz test regularity, reduced schedule pressure, and tail/cone control. These are substantive intermediate components and must not be omitted. They still do not expose an absolute selected pressure representative or the complete selected Cartesian `(M,I,J,S,C_p)` equality through `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_96_core_support_pressure_recovery_localization_source_review_2026-09-28.md`.

## Audit update: local curl and reduced moment bridges (priority 97, 2026-09-28)

The latest direct review identifies genuine local Cartesian-curl and potential-to-velocity identities in `ActualMeanPotentialRealization.lean` and `TailGaugePotential.lean`, together with genuine reduced/chart moment identities in `NominalConeAssembly.lean`. The correct remaining claim is therefore compositional: the source record still does not expose a theorem carrying those identities through the selected global sums, localisation, periodisation, and public `Witness` observables to the final Cartesian `(M,I,J,S,C_p)` equality. No `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_97_local_curl_profile_moment_bridge_source_review_2026-09-28.md`.

## Audit update: signed regularity, gauge/copy transport, support, and axis data (priority 98, 2026-09-28)

The latest direct review confirms signed native regularity, exponent/rate arithmetic, gauge and alias coherence, interval-copy and tangent transport, support preservation, reduced exterior matching, axis pressure data, positive-time signed wave data, and reduced pressure-kernel bounds. These are substantive intermediate components. They still do not expose the complete selected Cartesian `(M,I,J,S,C_p)` equality through `Witness`; no `Delta m != 0`, impossibility theorem, or kernel contradiction is asserted. Evidence: `NavierStokesReview/src/audit/priority_98_signed_gauge_copy_support_axis_transport_source_review_2026-09-28.md`.

## Audit update: carrier, cycle, signed-axis, and pressure-flux review (priority 109, 2026-09-28)

The latest twelve-module review records substantive intermediate transport: current-band support, signed request/amplitude/pressure `tsum` transport, cycle-state coherence, angular curl invariance, dependent-family periodisation, reduced natural-axis bridges, future pressure integrals, physical-stage bounds, and comparative whole-space pressure flux. It does not establish the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` equality, a nonzero defect, an impossibility theorem, or a kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_109_carrier_cycle_signed_axis_pressure_source_review_2026-09-28.md`.

## Audit update: cycle coherence, initial state, particular data, and corrected pressure (priority 110, 2026-09-28)

The latest four-module review records substantive intermediate construction: initialized state and band transport, coherent cycle iteration, particular-cycle native source/pressure/Gaussian data, and reduced corrected-pressure matching and bounds. Priority 111 adds cycle preservation, curl-corrected particular realization, and germ/cutoff transport. Priority 112 adds reduced activation stocks, locally finite diagonal `tsum` jet/tail bounds, and compensated outgoing-profile integral identities. Priority 113 adds heated outgoing reduced-profile identities, mode-solenoidal reindexing, and shaped-wait temporal bounds. These results do not establish the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` equality, a nonzero defect, an impossibility theorem, or a kernel contradiction. Evidence: `NavierStokesReview/src/audit/priority_110_cycle_initial_particular_pressure_source_review_2026-09-28.md`, `NavierStokesReview/src/audit/priority_111_cycle_preservation_particular_realization_source_review_2026-09-28.md`, `NavierStokesReview/src/audit/priority_112_activation_diagonal_extended_heated_source_review_2026-09-28.md`, and `NavierStokesReview/src/audit/priority_113_heated_mode_reindex_shaped_wait_source_review_2026-09-28.md`.

## Adjudication correction: profile moments are active dependencies

The earlier formulation that the five-moment/rank restoration is “missing”, “bypassed”, or wholly outside the selected proof tree is withdrawn. The paper defines `(M,I,J,S,C_p)` as cumulative radial integrals of reduced profile variables used to preserve pressure, radial velocity, stress, and correction-cycle compatibility at profile joins. It does not follow that the public `Witness` must contain a literal final-Cartesian tuple field.

The live source records an active dependency chain from `PositiveOrderMoments.moments_zero` through `GlobalStressSupport.conservative_moments_zero`, `EntranceAlignedBase.aligned_finiteIdentities`, `FinalSlowBase.finiteIdentities`, and `BaseResidual` finite-identity/jet-flatness theorems. These identities are therefore part of the selected construction and cannot be described as dispensable merely because `GermCandidateAssembly.origin_blowup` proves the axis-limit conjunct through `FinalSlowBase.axis_tendsto`.

The remaining adverse question is the complete paper-to-endpoint composition: whether the paper’s reduced-profile identities and their stated consequences are semantically carried through the selected mixed stages, `tsum`, curl, localisation, periodisation, pressure, force, support, and axis/whole-space limits. The review must not infer a nonzero defect, impossibility, or `False` from the absence of a tuple field. Conversely, compilation of the existential endpoint does not by itself establish that complete semantic composition. Evidence: `NavierStokesReview/evidence/selected_profile_moment_dependency_adjudication_2026-09-29.md`.

## Force smoothness and the five-moment correspondence boundary

The raw source resolves an important distinction. The selected Lean route does
not take `NativeBounds` from an empty interface: actual physical data are used
to construct the stage estimates, residual rates are derived, and the force is
made smooth from full residual derivative limits. This positive construction
does not close the separate paper-to-endpoint question. No inspected theorem
identifies those final rate/limit objects with every reduced-profile moment
consequence used in the manuscript after the complete mixed Cartesian,
`tsum`, curl, localisation, periodisation, pressure, and force composition.

The manuscript does contain load-bearing five-moment matching and correction,
but the stronger rebuttal language claiming an explicit
Fredholm-adjoint-Laurent “if and only if” theorem, a sole cancellation route,
or divergence of every individual residual term was not found in the
extracted text. The controlled conclusion is therefore **not established as
complete paper-to-code correspondence**, not a claim that the selected force
is already shown nonsmooth or that the endpoint is formally `False`.

Evidence: `NavierStokesReview/src/audit/priority_161_rebuttal_force_smoothness_moment_boundary_adjudication_2026-09-29.md` and `NavierStokesReview/evidence/source_tranche_rebuttal_force_smoothness_moment_boundary_2026-09-29.json`.

## Audit control: full CMI dependency crosswalk

The paper-to-code review must preserve the relationships among Fefferman's
admissibility conditions, the residual-defined force, the five reduced-profile
moments, and the final Lean endpoint. The current source supports the claim
that the manuscript uses `(M,I,J,S,C_p)` as load-bearing matching and repair
data. It does not support the stronger assertion that velocity blow-up alone
proves every residual summand diverges, or that the extracted paper states a
sole-mechanism Fredholm/adjoint/Laurent “if and only if” theorem.

The Lean route derives a smooth force from concrete physical data, residual
rate bounds, derivative recurrence, locally uniform boundary limits, and smooth
extension. The adverse finding remains that the public `Witness` does not
expose the complete selected-field semantic correspondence to every
paper-level moment consequence. This is **NOT ESTABLISHED** correspondence,
not a proof that the selected force is nonsmooth or that the literal forced
CMI predicate is false.

The required next calculation is the complete selected-field trace through
`tsum`, curl, localisation, periodisation, pressure, force, support, and
endpoint limits. Escalation requires a direct selected mismatch, impossibility
theorem, false mandatory CMI premise, or selected-path `False`.

Evidence: `NavierStokesReview/src/audit/priority_163_full_cmi_dependency_crosswalk_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_full_cmi_dependency_crosswalk_2026-09-29.json`.

## Priority 164: formal CMI Alternative (C) result and manuscript-fidelity boundary

The current Lean record contains a direct zero-sorry proof of a forced
whole-space proposition whose declared predicates mirror the displayed
clauses of Alternative (C). The proof establishes the comparator's declared
smoothness, decay, PDE, initial-data, and global finite-energy competitor
requirements. This is a positive result about the Lean proposition, not a
blanket finding that the paper's complete physically reasonable construction
has been machine-checked.

The manuscript-fidelity question is therefore decisive, not optional. Fefferman
introduces a connected class of smooth, physically reasonable solutions and C
cites that class through (4)--(7); it is not legitimate to reduce C to the
existential symbols or equation labels alone. The paper uses the five moments
as load-bearing profile matching and correction data, while the public
endpoint does not expose a selected-field theorem identifying every
paper-level consequence, including the transport of the corrected moments
through the completed Cartesian construction and residual force. The correct
publication conclusion is consequently: the Lean proposition is proved as
declared, but OpenAI's claim that Lean verifies the manuscript's CMI proof is
**NOT ESTABLISHED** on the current record. A direct proof that the selected
force/data violate (4)--(5), or that the selected field cannot realise the
claimed smooth residual, would escalate this correspondence finding to a
formal CMI failure; that stronger result has not yet been derived.

Evidence: `NavierStokesReview/evidence/priority_164_direct_cmi_alternative_c_proof_2026-09-29.md`;
`NavierStokesReview/evidence/priority_164_direct_cmi_alternative_c_proof_2026-09-29.json`.

The subsequent Priority 162 source review records the correction-state
boundary separately: its `barMoment` and `FiveRows` identities are genuine,
but their identification with the final activated Cartesian field remains
unclosed. Evidence:
`NavierStokesReview/src/audit/priority_162_barmoment_correction_state_vs_selected_field_source_review_2026-09-29.md`
and
`NavierStokesReview/evidence/source_tranche_barmoment_correction_state_vs_selected_field_2026-09-29.json`.

## Source-complete control note: preserve the manuscript's connected logic

The manuscript is not to be reduced to a log of isolated declarations or to
the endpoint's existential wrapper. The complete section and appendix map is
[`CMI_OpenAI_Full_Semantic_Crosswalk.md`](../CMI_OpenAI_Full_Semantic_Crosswalk.md).
It must be read together with Fefferman's complete CMI specification, not as
a substitute for it.

For the audit, the manuscript's five-moment definitions, modulation errors,
correction bumps, matching, pressure/stress consequences, cycle defects,
localisation, and force regularity remain connected claims. The Lean record
shows genuine upstream cycle and rate/flatness machinery, so the review must
not claim that the force route is a bare unsupported NativeBounds premise.
The adverse finding is narrower and stronger than that: the inspected
selected endpoint does not expose the final semantic identity transporting
the manuscript's cumulative observables through the completed Cartesian
construction. Until that selected-field bridge is located or disproved by a
direct calculation, the complete paper-to-code claim is not established; a
compiled C-shaped proposition is not sufficient evidence for the whole
manuscript.

This control note is linked to the source-complete ledger and the evidence
files listed in the peer-review control document. No statement here should be
read as a value-level proof that the selected moments are nonzero or that the
selected force is nonsmooth without a direct theorem.

The subsequent invariant trace corrects the endpoint interpretation. The
`CycleAnalyticInvariant` record contains concrete correction-state obligations,
including a three-component radial defect \((P,J_\theta,J_z)\), two zero-mass
constraints, residual classes, smoothness, support, periodicity, and state
reconstruction. Those data genuinely feed the residual-rate and smooth-force
route. The endpoint therefore cannot fairly be described as deriving force
smoothness from an unsupported `NativeBounds` premise.

The same trace does not locate the different theorem still required for the
paper-level claim: an equality identifying the completed selected Cartesian
field, after `tsum`, curl, localisation, periodisation, pressure, and force
extension, with \((M,I,J,S,C_p)\). The review status consequently remains
**NOT ESTABLISHED AS COMPLETE PAPER-TO-CODE CORRESPONDENCE**, not a claim that
the selected force has already been shown nonsmooth. Evidence:
`NavierStokesReview/src/audit/priority_164_cycle_invariant_residual_jet_trace_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_cycle_invariant_residual_jet_trace_2026-09-29.json`.

## Adjudication of the five-moment smoothness rebuttal

The latest rebuttal is correct that the five cumulative quantities
\((M,I,J,S,C_p)\) are load-bearing in the manuscript's profile matching and
correction architecture. It is not correct to strengthen that observation
into the claim that they are the manuscript's only residual-cancellation
mechanism. The manuscript says that individual residual terms may diverge
while their sum and all derivatives extend smoothly through the singular time
(`docs/navier-stokes openai.txt:108-113`). It then describes pulse-flux
cancellation of the leading singular stress, further correction of remaining
singular errors, heat-exterior localisation, and the five radial moment
equations as connected parts of the construction
(`docs/navier-stokes openai.txt:118-123,287-319,711-735`).

In particular, \(\|u(t)\|_\infty\to\infty\) does not logically imply that each
term in

\[
f=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
\]

diverges. A sum can remain smooth when its summands have cancelling singular
parts. The relevant mathematical question is whether the construction proves
the required cancellations and extension, not whether velocity blow-up by
itself forces termwise divergence.

The adverse paper-to-code finding remains narrower and material. The
inspected `Witness` contract does not expose a theorem identifying the
completed selected Cartesian field and its residual/force construction with
every five-moment consequence used by the manuscript after the actual cycle,
infinite summation, curl, localisation, periodisation, pressure, and endpoint
limits. This leaves the complete manuscript-to-endpoint correspondence
**NOT ESTABLISHED**. It does not prove that the selected force is nonsmooth,
that the selected moments are nonzero, or that the literal forced CMI
proposition is false, because the Lean source also contains a concrete
cycle-invariant and residual-jet route to smooth force data.

This distinction is central to the paper's claim. The audit rejects both
understatements: the moments are not optional bookkeeping, and the compiled
endpoint is not automatically equivalent to the entire manuscript merely
because it contains a C-shaped existential proposition. Evidence:
`NavierStokesReview/evidence/agent_log_rebuttal_adjudication_2026-09-29.md`.

## Selected-field composition trace

The source trace following the latest adjudication confirms the distinction
required by the manuscript audit. The selected Lean construction genuinely
uses concrete cycle data, finite residual rates, locally finite `tsum`s,
Cartesian curl and cutoff operations, periodisation, time activation, and
smooth residual-force extension. The inspected public endpoint nevertheless
does not export the separate semantic theorem transporting the manuscript's
five cumulative observables through that completed composition. The correct
status remains **NOT ESTABLISHED AS COMPLETE PAPER-TO-ENDPOINT
CORRESPONDENCE**, rather than a claim that a selected moment defect or force
nonsmoothness has been proved. Evidence:
`NavierStokesReview/src/audit/priority_167_selected_field_composition_trace_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_selected_field_composition_trace_2026-09-29.json`.

### Correction to the endpoint characterisation

The repository-wide endpoint closure genuinely contains the paper's moment and
rank machinery. A direct 588-module closure census identified 32 modules with
exact moment symbols and representative theorems for profile repair, stress
support, rank updates, state balances, and terminal compensation. The audit
must not call this machinery dead, unreachable, or absent.

The unresolved issue is instead the final semantic identification. The
exported `ActualCandidateAssembly.Witness` packages the selected activated
fields and force consequences but does not visibly state

\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
=(M,I,J,S,C_p).
\]

Thus the current record demonstrates substantial upstream moment mathematics
and a concrete residual-flatness route, while still lacking the explicit
selected-field transport theorem needed to claim that the exported endpoint
is the paper's five-observable construction. This is `CTR-005`, not a claim
that the upstream moment machinery is absent.

Evidence: `NavierStokesReview/src/audit/priority_168_full_closure_moment_symbol_census_2026-09-29.md`.
## Priority 169 source correction: force smoothness and five-moment scope

The audit must not state that the infinity norm blow-up forces every individual
term of

  f = partial_t u + (u dot grad)u - nu Delta u + grad p

to diverge. The manuscript explicitly allows divergent summands with smooth
cancellation of the total residual and its derivatives. It also presents
wave-flux, covariance, auxiliary-time, further-correction, and five-moment
operations as connected parts of the residual construction. The five moments
are load-bearing for profile matching, pressure/stress propagation, modulation
repair, and cycle compatibility, but the source does not support calling them
the sole cancellation mechanism.

The Lean source provides a concrete residual-rate and flatness route: cycle
invariants and physical data feed finite residual rates, those rates feed
vanishing joint jets, and compatible residual limits feed a smooth force
extension. This corrects any description of the endpoint as accepting empty
NativeBounds assumptions.

The remaining adverse conclusion is narrower and still important. The public
selected endpoint does not expose a theorem identifying the completed Cartesian
field and force with every manuscript-level consequence of (M,I,J,S,Cp). The
manuscript-to-endpoint correspondence therefore remains NOT ESTABLISHED under
CTR-005. The current record does not prove a selected nonzero defect, nonsmooth
force, literal CMI failure, or kernel False.

Evidence:
NavierStokesReview/src/audit/priority_169_declaration_level_invariant_force_adjudication_2026-09-29.md;
NavierStokesReview/evidence/source_tranche_priority_169_invariant_force_adjudication_2026-09-29.json.

## Audit boundary update: physical admissibility and endpoint correspondence (2026-09-29)

The manuscript audit now cross-references Fefferman's connected meaning of
“physically reasonable”, including the whole-space and periodic branches and
their global smoothness, decay, periodicity, and energy requirements.  It also
records that the selected Lean force route is derived from concrete physical
cycle data and residual-jet limits.  The remaining open correspondence is the
explicit transport of every paper-level five-moment consequence through the
completed selected Cartesian construction.  This source-bound status is not a
claim that the force is nonsmooth or that the CMI proposition is already
refuted.

See `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md` and
`NavierStokesReview/src/audit/priority_168_fefferman_physical_admissibility_and_force_chain_2026-09-29.md`.

## Audit boundary update: connected CMI endpoint adjudication (2026-09-29)

The current audit treats Fefferman's phrases “physically reasonable” and
“retaining the heart of the problem” as connected semantic requirements, not
as decorative prose. It also records the concrete Lean route that derives
residual flatness and a smooth force from actual cycle data before the
comparison theorem.

The remaining paper-level gap is exact: the endpoint does not expose a
selected-field theorem transporting the manuscript's five radial observables
(M,I,J,S,Cp) through the completed Cartesian, localisation, periodisation,
pressure, and force construction. This sustains CTR-005 for the claim that
the manuscript's complete physical mechanism has been machine-checked.

It does not, by itself, prove that the formal C-shaped proposition is false.
That stronger verdict requires a selected mismatch, an impossibility theorem,
or a failed explicit Fefferman premise. The distinction and the build caveat
are recorded in
NavierStokesReview/src/audit/priority_169_connected_cmi_endpoint_adjudication_2026-09-29.md.

## Audit update: debt-to-force trace and endpoint limitation (2026-09-29)

The source audit traces debt, mass, covariance, and rank data through the
analytic cycle step and invariant propagation into concrete residual-rate
estimates, vanishing residual jets, and a smooth force constructor. The paper's
statement that individual residual terms can diverge while the total residual
extends smoothly is therefore consistent with the selected force route; a
velocity norm blow-up alone is not a proof that every residual summand diverges.

The five-moment system remains a load-bearing part of the manuscript's profile
matching and repair architecture. However, the manuscript also uses pulse
stress covariance, mean and pressure corrections, cutoffs, and recursive
residual improvement. The current Lean endpoint has not been shown to export a
single theorem transporting the manuscript tuple ((M,I,J,S,C_p)) through the
completed Cartesian field construction. The correct status is therefore a
paper-to-endpoint correspondence gap, not a demonstrated nonsmooth force or a
formal contradiction.

## Numerical diagnostic of the spatial curl and cutoff layer

The audit also includes a CUDA-first three-dimensional Cartesian diagnostic of
the source cutoff and vector-potential operation. It reconstructs the cutoff,
forms a nonseparable axisymmetric stream in Cartesian coordinates, evaluates
the analytic curl and cutoff-gradient commutator, independently evaluates the
Cartesian curl by finite differences, measures the divergence residual, and
integrates the full x-y slices. Resolutions 129, 193, and 257 were swept over
three stream scales and two axial modulations on an NVIDIA GeForce RTX 4060 Ti.
The integrated diagnostic defect is stable under refinement while the reported
finite-difference curl and divergence errors decrease.

This is evidence that the cutoff-gradient term can alter radial integration in
an explicit three-dimensional profile. It is not a calculation of the
noncomputable selected `ASum`, `BSum`, or `PSum`, and it does not prove a
nonzero selected-field `(M,I,J,S,C_p)` defect. The source-level transport
obligation therefore remains open rather than being silently promoted from a
diagnostic profile to the exported Lean witness.

Evidence: `NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.md`;
`NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.json`;
`NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.csv`;
`NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.png`.

## Audit update: selected observable type boundary (2026-09-29)

The selected construction is materially present in the Lean source. The
endpoint builds `ASum`, `BSum`, and `PSum` from a locally finite `tsum`, applies
the cutoff-before-curl and periodisation operations, and then time-activates
the mixed fields. The source also proves the cutoff-gradient commutator.

The remaining issue is the observable interface. `barMoment` is defined on a
lifted scalar pressure-stream domain and applies a torus average before radial
integration. It is not definitionally the activated Cartesian velocity supplied
by `Witness`. A source-level theorem must therefore provide the scalar and
component pullback, convergence, support and integrability, and equality with
the completed selected field before the manuscript quantities can be credited
to the endpoint. This sharpens, rather than broadens, CTR-005. No selected
nonzero defect has been established.
## Fefferman's connected specification and the selected formal route

Fefferman's wording is part of the mathematical specification. The phrase
“physically reasonable solutions” is immediately connected by “Hence” to the
all-order spatial and space-time decay conditions (4) and (5). The phrase
“We accept ... only if” then makes global smoothness and bounded energy in
(6) and (7) acceptance conditions for the whole-space solution class. The
word “Alternatively” introduces a different periodic branch, and “Thus” ties
that branch to data conditions (8) and (9) and accepted-solution conditions
(10) and (11). Finally, “retaining the heart of the problem” says that the
four alternatives are meant to preserve this connected PDE, regularity,
decay, energy, and domain structure while allowing different proof targets.

This means that a review cannot establish C merely by matching the surface
quantifiers `exists u0, f`. The whole-space C package is

\[
 (1),(2),(3) + (4),(5) + (6),(7)
\quad\text{on }\mathbb{R}^{3}\times[0,\infty),
\]

while the periodic D package is

\[
 (1),(2),(3) + (8),(9) + (10),(11)
\quad\text{on the periodic domain.}
\]

The current source audit therefore records two separate conclusions. The
inspected Lean path contains a concrete residual-limit and jet-recurrence
route to a smooth force, pre-singular energy control, and a global-comparator
contradiction. It is not an empty proposition or a compiler-shaped shell.
However, the audit has not located a theorem identifying the completed
selected Cartesian velocity, pressure, residual, and force with the
manuscript's five cumulative observables \((M,I,J,S,C_p)\) through the
potential sums, curl, localisation, periodisation, activation, and endpoint
observable maps. The manuscript-specific paper-to-endpoint correspondence is
therefore **NOT ESTABLISHED (CTR-005)**. This is a correspondence finding,
not yet a theorem that the selected field fails C, that the force is not
smooth, or that `False` follows.

The exact wording and node-by-node source graph are preserved in
`docs/navierstokes.txt:25-81` and
`NavierStokesReview/src/audit/priority_172_fefferman_semantic_network_2026-09-29.md`.

## Priority 173: connected CMI compliance versus manuscript mechanism fidelity

Fefferman's “may look for spatially periodic solutions” is a branch choice,
not a relaxation. In the whole-space branch, “physically reasonable”,
“Hence”, and “only if” connect the equations to `(4),(5)` and `(6),(7)`;
“retaining the heart” carries that package into C. The selected Lean path has
explicit smooth-force, decay, pre-singular PDE, initial-data, energy, and
comparator-nonexistence components, so it is not merely a bare existential
shell.

“Given, externally applied” supplies physical force provenance. OpenAI's
manuscript openly uses residual construction, says the background residual is
singular, and then claims pulse fluxes and further corrections make the total
residual smooth. Provenance is therefore a serious physical-model question,
but the displayed C predicate does not add an explicit independence relation.

The five moments remain load-bearing manuscript content. The inspected Lean
endpoint still lacks the theorem transporting every manuscript-level
five-moment consequence through the selected Cartesian construction. Complete
paper-to-endpoint fidelity remains `NOT ESTABLISHED (CTR-005)`; no selected
mismatch or literal C failure has been proved.

Evidence: `NavierStokesReview/src/audit/priority_173_fefferman_c_connected_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_173_fefferman_c_connected_adjudication_2026-09-29.json`.

## Audit update: force-smoothness rebuttal adjudication (2026-09-29)

The source review rejects three overstatements in the supplied rebuttal. First,
`L^\infty` velocity blow-up does not imply that every summand of
`\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p` diverges. Secondly, the
manuscript presents the five radial equations as one correction layer inside a
larger pulse, mean, pressure, auxiliary-time, cutoff, and residual-improvement
architecture. Thirdly, the selected Lean route does not obtain `force_smooth`
from an empty generic rate premise: it extends the traced actual residual after
using the derivative recurrence and locally uniform residual-jet limits.

The remaining adverse finding is narrower but material. The public `Witness`
still does not identify the completed activated Cartesian field's observables
with the manuscript's `(M,I,J,S,C_p)`. The audit therefore keeps
**NOT ESTABLISHED (CTR-005)** for complete paper-to-endpoint fidelity, without
asserting a selected nonzero defect, nonsmooth force, impossibility theorem, or
literal failure of Alternative (C).

Evidence: `NavierStokesReview/src/audit/priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.json`.

### Audit update: declaration-level bridge candidates (2026-09-29)

The seven lexical endpoint candidates have been inspected directly. They
provide rate estimates, local germ equalities, axis-growth transfer, and
schedule/vanishing-jet packaging, but none identifies the final activated
Cartesian velocity, pressure, or force with the manuscript's five observables.
The paper-specific endpoint correspondence therefore remains
**NOT ESTABLISHED (CTR-005)**. This is not a selected-field defect theorem.

Evidence: `NavierStokesReview/src/audit/priority_175_lexical_bridge_candidate_classification_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_175_lexical_bridge_candidate_classification_2026-09-29.json`.

### Audit update: selected-field composition boundary (2026-09-29)

The source trace confirms that the selected sums are genuinely composed into
Cartesian, localised, periodised, time-activated fields and used by the
smooth-force and blow-up endpoint. It does not, however, identify the
pressure-stream `barMoment` domain with the final activated Cartesian
five-observable tuple. The exact paper-to-endpoint correspondence therefore
remains **NOT ESTABLISHED (CTR-005)**, without a claim that the selected field
has a nonzero defect.

Evidence: `NavierStokesReview/src/audit/priority_176_selected_field_composition_domain_trace_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_176_selected_field_composition_domain_trace_2026-09-29.json`.

## Priority 177: Fefferman's connected semantic requirements

The source-level audit now records the mathematical work carried by the words
surrounding Fefferman's equations. “Physically reasonable” is connected by
“Hence” to the whole-space data decay conditions `(4),(5)` and by “only if”
to global smoothness and bounded energy `(6),(7)`. “Alternatively” and “may
look” open the periodic branch; “Thus”, “In place of”, and “We then accept”
make `(8),(9)` and `(10),(11)` the corresponding periodic data and solution
conditions. “Retaining the heart of the problem” carries this full network,
not just `(1)--(3)`, into C and D.

This matters directly to the manuscript audit. The selected Lean route is
substantive and includes a concrete smooth-force and comparison path, but the
inspected endpoint does not yet identify the completed selected Cartesian
construction with every manuscript-level consequence of `(M,I,J,S,C_p)`.
The paper-to-endpoint correspondence therefore remains **NOT ESTABLISHED
(CTR-005)**. This statement is neither a claim that the moments are optional
nor a proof that the selected force fails C; it identifies the unresolved
connected transport obligation.

Evidence:
`NavierStokesReview/src/audit/priority_177_fefferman_word_connection_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_177_fefferman_word_connection_adjudication_2026-09-29.json`.

## Priority 179: source-complete CMI semantic crosswalk

The CMI comparison is not a C-only syntactic test. Fefferman's wording makes
“physically reasonable” a connected solution class. “Hence” connects control
of spatial growth to whole-space data conditions `(4),(5)`; “only if” makes
global smoothness and bounded energy `(6),(7)` necessary. “Alternatively” and
“may look” permit choosing the periodic branch, but “Thus”, “In place of”, and
“We then accept” impose the periodic data and solution conditions `(8),(9)` and
`(10),(11)` once that branch is chosen.

The OpenAI manuscript must therefore be compared with the full connected
package. Its residual, pulse, stress, pressure, localisation, and moment
mechanism is scientifically relevant to that comparison. The Lean endpoint
has a concrete residual-limit and smooth-force route, but the selected-field
transport of the manuscript's complete five-moment consequences remains
`NOT ESTABLISHED (CTR-005)`. This is not a claim that the moments are
optional, nor a claim that literal C/D failure has already been proved.

Full record:
[`priority_179_fefferman_full_semantic_dependency_network_2026-09-29.md`](../../NavierStokesReview/src/audit/priority_179_fefferman_full_semantic_dependency_network_2026-09-29.md).

## Priority 177: Fefferman's connected semantic requirements

The source-level audit now records the mathematical work carried by the words
surrounding Fefferman's equations. “Physically reasonable” is connected by
“Hence” to the whole-space data decay conditions `(4),(5)` and by “only if”
to global smoothness and bounded energy `(6),(7)`. “Alternatively” and “may
look” open the periodic branch; “Thus”, “In place of”, and “We then accept”
make `(8),(9)` and `(10),(11)` the corresponding periodic data and solution
conditions. “Retaining the heart of the problem” carries this full network,
not just `(1)--(3)`, into C and D.

This matters directly to the manuscript audit. The selected Lean route is
substantive and includes a concrete smooth-force and comparison path, but the
inspected endpoint does not yet identify the completed selected Cartesian
construction with every manuscript-level consequence of `(M,I,J,S,C_p)`.
The paper-to-endpoint correspondence therefore remains **NOT ESTABLISHED
(CTR-005)**. This statement is neither a claim that the moments are optional
nor a proof that the selected force fails C; it identifies the unresolved
connected transport obligation.

Evidence:
`NavierStokesReview/src/audit/priority_177_fefferman_word_connection_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_177_fefferman_word_connection_adjudication_2026-09-29.json`.

### Audit update: connected Fefferman specification (2026-09-29)

The CMI source is treated as a connected semantic package. Its data,
force-provenance, domain, smoothness, energy, and nonexistence clauses cannot
be separated without changing the target being audited. The current record
therefore preserves the adverse CTR-005 correspondence finding while leaving
literal C/D failure and selected-field mismatch as unproved stronger claims.

Evidence: `NavierStokesReview/src/audit/priority_177_fefferman_word_connection_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_177_fefferman_word_connection_adjudication_2026-09-29.json`.

## Priority 180: five-moment mechanism and selected-field transport

The manuscript-level conclusion must not be weakened into the claim that the
five cumulative moments are dispensable. They are load-bearing constraints in
the profile matching and correction architecture. The source audit also does
not justify the stronger claim that velocity blow-up forces termwise
divergence of every residual summand, or that the five equations are the only
operation involved in the manuscript's complete cancellation and flatness
argument.

The Lean endpoint has a real conditional smoothness route. Its residual
recurrence, vanishing joint jets, and locally uniform endpoint limits support

\[
  H_{\mathrm{selected}} \Rightarrow J_{\mathrm{flat}}
  \Rightarrow F\in C^\infty,
  \qquad F=\mathcal R(u,p)\text{ before the singular time}.
\]

That implication does not replace the missing paper-to-code identification:

\[
  J_{\mathrm{flat}} \Rightarrow
  \operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}})
  =(M,I,J,S,C_p).
\]

The inspected `ActualCandidateAssembly.Witness` exports no theorem giving that
completed identity after the selected `tsum`, curl, localisation,
periodisation, averaging, and radial/axis constructions. Consequently the
research-paper claim that the exported Lean endpoint machine-checks the
manuscript's five-moment physical mechanism remains **NOT ESTABLISHED
(CTR-005)**. This is a correspondence finding, not a proof that the selected
field has a nonzero defect or that Fefferman's literal C/D proposition has
already been refuted.

Evidence: `NavierStokesReview/src/audit/priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.json`.

### Adjudication correction: operational C versus manuscript fidelity

The connected Fefferman reading must not be used to make the opposite
overclaim. “Physically reasonable” is not an invitation to discard the
conditions surrounding the alternatives, but the displayed whole-space C
predicate is operationally represented by initial-data decay `(4)`, force
smoothness and decay `(5)`, and accepted-solution conditions `(1)--(3),(6),(7)`.
The comparator definitions implement these clauses, and
`NavierStokes.Comparator.navier_stokes_breakdown_R3` proves the corresponding
existential/nonexistence proposition on the inspected route.

The exact logical status is therefore:

\[
\text{Lean proves an inspected operational C-shaped proposition}
\quad\text{but}
\quad
\text{the inspected endpoint does not yet prove identity with every step of
the manuscript's five-moment mechanism}.
\]

The second statement is a paper-to-code fidelity limitation, not a proof that
the operational C-shaped proposition is false. The manuscript itself states that the
force may be defined as the momentum residual and that the total residual can
be made smooth by cancellation, so the mere fact that the force was designed
from the trajectory is not a formal disqualification under Fefferman's
displayed existential C formula. It remains a physical-provenance question
because Fefferman describes the force as “given” and “externally applied”.
That semantic concern must be reported, but it cannot replace a proved failed
condition.

This correction is linked to the source adjudication rather than replacing
the five-moment audit:
`NavierStokesReview/src/audit/priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.md`.

## Selected-field radial observable: integrability gate

The selected-field audit now records a specific analytic issue at the radial
observable boundary. `barMoment` is a global Bochner integral over the real
radial coordinate, while the selected mixed radial pullback is periodic on the
inspected path. Periodicity alone does not define the paper's intended finite
radial moment on the whole line. If a periodic pullback is positive on one
fundamental interval it is not globally integrable; if it is both periodic and
radially supported, it must vanish. Mathlib's `integral_undef` then yields a
zero global integral only after non-integrability has been established, which
is not a physical moment identity.

The current source record does not yet prove the selected support,
integrability, positivity, or a nonzero global value. Accordingly, the
paper-level five-moment transport remains **NOT ESTABLISHED (CTR-005)**. This
does not by itself prove a selected mismatch or literal CMI failure. The next
mathematical obligation is an explicit finite-prefix-to-selected-global
integration theorem with the correct radial domain and hypotheses.

Evidence: `NavierStokesReview/src/audit/priority_181_global_barmoment_integrability_gate_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_181_global_barmoment_integrability_gate_2026-09-29.json`.
## Current semantic control: Fefferman's connected admissibility package

The CMI specification is not being treated as an equation-only shell. The
source-controlled semantic audit maps “given”, “externally applied”, “for
physically reasonable solutions”, “Hence”, “only if”, “Alternatively”, “may
look”, “Thus”, “In place of”, “We then accept”, “such”, “for which”, and
“retaining the heart” to the connected data, branch, global regularity, energy,
periodicity, and nonexistence obligations. The periodic wording gives branch
latitude; it does not make the chosen branch's conditions optional.

This matters to the paper's claim in two directions. The OpenAI manuscript
does contain a substantive residual-cancellation and smooth-force route; the
review therefore does not call its force a compiler trick. At the same time,
the manuscript's five-moment and correction mechanism is not credited as
machine-checked at the final selected Cartesian endpoint until its selected
field, pressure, residual, force, support, and global C/D consequences are
connected by explicit source-level transport results. The current status is
`NOT ESTABLISHED (CTR-005)` for complete manuscript-to-endpoint fidelity,
not a literal C/D refutation.

Evidence: `NavierStokesReview/src/audit/priority_182_fefferman_semantic_word_to_condition_closure_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_priority_182_fefferman_semantic_word_to_condition_closure_2026-09-29.json`.

### Clarification of the periodic-branch wording

The phrase “we may look for spatially periodic solutions” is treated here as
branch latitude, not as permission to omit requirements. “Thus, we assume”
binds (8) and (9) after the periodic branch is selected; “in place of” changes
the whole-space data controls (4) and (5), while “we then accept” binds (10)
and (11). For the whole-space branch used by the C-shaped route, (4), (5),
(6), and (7) remain connected requirements.

This also resolves the apparent force-provenance contradiction. Fefferman's
“given, externally applied” language is a physical forward-problem framing,
but the displayed C and D propositions do not add a separate formal predicate
that a force must be constructed independently of a selected trajectory. The
OpenAI manuscript explicitly defines the force as the residual of a chosen
flow and pressure, then makes smooth extension of the total residual the
central challenge. Therefore the audit must test both levels: the complete
displayed C/D admissibility package and the manuscript's physical construction
correspondence. The operational C route can be formally present while the
selected-field transport of the manuscript's five-moment mechanism remains
unestablished. Neither statement cancels the other.

## Audit dossier update: force smoothness and the five-moment endpoint

The source-controlled review now separates three propositions that had been
blurring together. The manuscript's five-moment system is load-bearing for
profile matching and finite-dimensional correction. The selected Lean route
also contains a concrete residual-jet recurrence, locally uniform endpoint
limits, and a smooth Taylor--Borel force extension that agrees with the
activated residual before the terminal time. Therefore the record does not
support the claim that `force_smooth` is simply assumed from `NativeBounds`.

At the same time, no inspected export theorem identifies the completed
selected Cartesian fields and their residual/force with the manuscript's
`(M,I,J,S,C_p)` observables after the full `tsum`, curl, localisation,
periodisation, torus-average, and radial-integral composition. That is a
substantive paper-to-code correspondence failure, not a claim that the
upstream moment code is dead or that the residual force has already been
proved nonsmooth.

The current scientific classification is consequently **NOT ESTABLISHED
(CTR-005)** for complete manuscript-to-endpoint fidelity. A stronger result
would require a selected value mismatch, an impossibility theorem, or a
connected failed CMI condition. The dossier must not label the manuscript's
literal C/D target false solely from the missing endpoint identity.

Evidence:
`../NavierStokesReview/src/audit/priority_183_force_smoothness_moment_rebuttal_adjudication_2026-09-29.md`;
`../NavierStokesReview/evidence/source_tranche_priority_183_force_smoothness_moment_rebuttal_adjudication_2026-09-29.json`.

### Priority 184 source correction: smooth-force route versus moment transport

The selected Lean construction must not be described as obtaining force
smoothness from a bare generic rate contract. The inspected path constructs
actual residual data, carries vanishing joint jets and boundary limits through
the periodic assembly, and derives `force_smooth` from those premises. The
targeted source modules use standard `noncomputable` definitions and one
standard `Classical.choice` construction; no explicit custom axiom, `sorry`, or
`admit` was found in the inspected selected path.

The paper-to-code correspondence nevertheless remains incomplete at a more
specific point. No selected-endpoint theorem has yet been located that
identifies the completed Cartesian field and force with the paper's five
observables \((M,I,J,S,C_p)\) after `tsum`, curl, localisation, periodisation,
torus averaging, radial integration, and the required integrability/support
arguments. This is the current `CTR-005` finding. It does not prove that the
selected force is nonsmooth or that the selected moments are wrong; those
stronger conclusions require a value-level mismatch or impossibility result.

Evidence:
`../NavierStokesReview/src/audit/priority_184_selected_path_foundation_audit_2026-09-29.md`;
`../NavierStokesReview/evidence/source_tranche_priority_184_selected_path_foundation_audit_2026-09-29.json`.

### Priority 185 source correction: moments, residual cancellation, and force smoothness

The five cumulative moments remain a load-bearing part of the manuscript's
profile matching, modulation restoration, and compatibility correction. The
audit must not understate that dependence. The source also prevents three
stronger claims: \(L^\infty\) velocity blow-up does not by itself imply
termwise divergence of every residual summand; the manuscript does not make
the five equations its only cancellation operation; and the selected Lean
`force_smooth` proof is not a bare `NativeBounds` assumption. The selected
path derives residual rates from actual physical data and invariants, obtains
vanishing joint jets, and constructs a smooth force extension agreeing with
the activated residual before the singular time.

The remaining paper-to-code gap is value-level and specific. The inspected
endpoint still does not prove

\[
J_{\rm flat}\Rightarrow
\operatorname{PaperMoments}(u_{\rm selected},p_{\rm selected})
=(M,I,J,S,C_p)
\]

after the completed series, curl, localisation, periodisation, torus
averaging, radial integration, and global support/integrability arguments.
This leaves complete manuscript fidelity **NOT ESTABLISHED (CTR-005)**. It is
not a proof that the selected force is nonsmooth or that the connected CMI
alternative is false. Those require a selected mismatch, failed condition,
impossibility theorem, or contradiction.

Evidence:
`../NavierStokesReview/src/audit/priority_185_rebuttal_adjudication_2026-09-30.md`;
`../NavierStokesReview/evidence/source_tranche_priority_185_rebuttal_adjudication_2026-09-30.json`.

### Priority 186: source-preserving Fefferman semantic closure

The full word-to-condition network is consolidated in
[`priority_186_fefferman_full_word_connection_closure_2026-09-30.md`](../../NavierStokesReview/src/audit/priority_186_fefferman_full_word_connection_closure_2026-09-30.md)
and its evidence record
[`source_tranche_priority_186_fefferman_full_word_connection_closure_2026-09-30.json`](../../NavierStokesReview/evidence/source_tranche_priority_186_fefferman_full_word_connection_closure_2026-09-30.json).

The audit reads Fefferman's text as a connected mathematical specification.
“May look for” permits a periodic branch; it does not waive that branch's
conditions. “Thus”, “In place of”, and “We then accept” bind `(8),(9)` and
`(10),(11)`. “Physically reasonable” and “retaining the heart of the problem”
carry the global decay, smoothness, energy, force, domain, and existence
meaning into the alternatives. C and D are therefore not assessed from
`(1)--(3)` alone.

The selected Lean path has an operational C-shaped route, but complete
manuscript-to-selected-field fidelity remains **NOT ESTABLISHED (CTR-005)**.
This is a correspondence finding, not a claim that the selected force is
already nonsmooth or that literal C/D failure follows from the absence of a
named moment tuple alone. Such a stronger finding requires a selected failed
condition, value mismatch, impossibility theorem, or contradiction.
## Priority 187: jet-flatness and five-moment correspondence

The current source audit resolves the apparent circularity dispute. The
manuscript's five-moment system is necessary to its stated profile matching
and correction architecture, so the review does not treat it as optional. The
selected Lean route, however, has a separate residual-flatness proof route:

\[
H_{\rm selected}\Rightarrow J_{\rm flat}\Rightarrow F\in C^\infty,
\qquad F=\mathcal R(u_{\rm selected},p_{\rm selected})
\text{ before the singular time}.
\]

That route is built from actual physical data, cycle invariants, finite
residual rates, schedule selection, locally uniform limits, and smooth gluing.
It is therefore inaccurate to call `force_smooth` a free-standing
`NativeBounds` assumption or to infer force nonsmoothness from the absence of
a tuple field.

The unresolved paper-fidelity implication is instead

\[
J_{\rm flat}\Rightarrow
\operatorname{PaperMoments}(u_{\rm selected},p_{\rm selected})
=(M,I,J,S,C_p).
\]

The endpoint `Witness` does not expose this completed selected-field identity,
and the current source trace has not found it elsewhere after the full
Cartesian, sum, curl, localisation, periodisation, torus-average, radial,
support, integrability, and axis construction. The exact manuscript-to-Lean
claim is consequently **NOT ESTABLISHED (CTR-005)**. This is stronger than
saying the moments are unimportant, but weaker and more accurate than claiming
a selected nonzero defect, a nonsmooth force, or literal CMI failure.

Evidence: `NavierStokesReview/src/audit/priority_187_circularity_adjudication_2026-09-30.md`.

## Priority 188: the CMI target is the connected package

The review's CMI conclusion must not be read as though Fefferman asked only
for equations `(1)--(3)`. “May look for” permits choosing the periodic branch;
it does not waive its conditions. “Thus, we assume”, “In place of”, and “We
then accept” bind the periodic data and accepted-solution requirements. The
phrases “physically reasonable” and “retaining the heart of the problem” carry
the connected global smoothness, decay, force, domain, and energy meaning into
C and D.

The Lean comparator source encodes those connected conditions: initial-data
smoothness and divergence freedom, whole-space data decay, force smoothness and
decay, the PDE, incompressibility, initial data, global smoothness, whole-space
energy, and the periodic velocity and pressure conditions. Therefore the
inspected theorem proves the repository's connected formal C/D propositions.
That is a positive formal result, not an equation-only shell.

The adverse finding remains separate. The manuscript's moments are load-bearing
within its construction, but the current endpoint does not expose the
selected-field identity transporting them through the completed Cartesian
construction. Thus `CTR-005` remains **NOT ESTABLISHED** for complete
manuscript-to-selected-endpoint fidelity. This does not, by itself, prove that
the connected formal C/D proposition is false. A literal C/D failure requires a
selected failed condition, selected value mismatch, impossibility theorem, or
contradiction. See
[`CMI_OpenAI_Full_Semantic_Crosswalk.md`](../CMI_OpenAI_Full_Semantic_Crosswalk.md),
Priority 188.

## Priority 189: source correction on physical wording

The OpenAI manuscript was checked directly rather than inferred from a
summary. Its Section 2 calls itself a physical description, defines the force
as the residual, and states that the individual residual terms may diverge
while their sum and all derivatives extend smoothly through the singular time
(`docs/navier-stokes openai.txt:106-124`). It then describes pulses and later
corrections as the cancellation mechanism (`:252-304`). The inspected source
does not say that the construction “would never occur in physical reality”.

The review therefore distinguishes physical framing, Fefferman's displayed
admissibility package, and complete manuscript-mechanism fidelity. The last
remains `CTR-005` until the selected Cartesian field, pressure, residual, and
force are connected to the manuscript's moment and correction identities. The
source correction prevents the review from replacing an unverified transport
finding with an unsupported attribution about what OpenAI's paper says.

Evidence: `NavierStokesReview/src/audit/priority_189_openai_physical_wording_source_check_2026-09-30.md`;
`NavierStokesReview/evidence/source_tranche_priority_189_openai_physical_wording_source_check_2026-09-30.json`.
