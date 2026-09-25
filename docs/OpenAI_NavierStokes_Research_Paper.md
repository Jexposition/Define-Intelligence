# **DEFINE INTELLIGENCE.**


**Epistemological Vacuity and Structural Instability in Automated Blowup Constructions for the 3D Navier-Stokes Equations**

# Notes on the Logical Inconsistencies in the Formalised Navier-Stokes Blowup Constructon  

**Author:** $JΣXP$   


**Independent research initiative:** Jexposition 
**A keyboard cannot generate intellect exceeding that of its typist.**

**A thousand AI agents have proven to be that of an insufficient sum.**  
**If the objective is to produce works comparable to Shakespeare using only monkeys and typewriters, a vastly greater quantity of both monkeys and typewriters are therefore required.**

## Executive verdict

OpenAI's published claim to have solved the Navier–Stokes problem is **rejected
as unestablished on the inspected record**. This is a paper-level negative
finding, not a request for a compiler error. OpenAI claimed a solution of the
Navier–Stokes problem, so the burden is to exhibit one selected construction
whose equations, regularity, force, and load-bearing five-moment mechanism are
the same object. The source does export an R³ C/D-shaped theorem, but that
export does not identify its selected fields with the construction used in the
paper. That selected-field transport is not exposed. The result is a
publication-blocking failure of the affirmative solution record. The narrower
statement that no kernel-level `False` has yet been derived is only a status of
the review's stronger contradiction search; it is not an acceptance of the
published solution.

## Abstract

OpenAI presents its paper and public announcement as a solution of the
Navier–Stokes existence and smoothness problem, specifically by claiming the
forced alternatives in Charles Fefferman's Clay Mathematics Institute
formulation. This paper therefore evaluates that affirmative solution claim,
not an optional implementation detail. The review separates kernel validity,
the exported endpoint specification, and whether the endpoint is the
five-moment construction used to justify the advertised solution.

The inspected endpoint is not refuted by a compiler error or by the use of an
external force. The repository contains a genuine five-coordinate upstream
moment repair, a selected forced candidate, and a standard-axiom-only
dependency report for the inspected headline declarations. The decisive
adverse result is narrower: the exported `selected_witness` does not expose a
field-level equality identifying the paper's $(M,I,J,S,C_p)$ moments with the
selected velocity, pressure, residual, and force. A zero-sorry probe proves
that the witness type does not entail an arbitrary five-moment certificate.

That is a load-bearing failure of the authors' advertised five-moment proof
record. The publication-level verdict is therefore **the paper's claimed
solution is not established by the exposed selected-field correspondence**.
The inspected R³ theorem is a separate level: it exports a literal C/D-shaped
proposition, but that fact does not establish that the proposition is the
five-moment Navier–Stokes solution described and marketed in the paper. This
paper does not claim that the literal endpoint has already been formally
refuted; it rejects the published solution claim because its affirmative proof
record is incomplete at the load-bearing composition boundary.

The phrase **not formally refuted** reports only that the review has not yet
derived `False` from the selected Lean endpoint; it is not evidence that the
missing bridge is true. A formal refutation would require a zero-sorry
contradiction on the selected dependency path or a false mandatory premise
proved for the selected fields. That stronger result remains a separate
research target.

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

Accordingly, this paper rejects the advertised solution claim on the inspected
record. That conclusion does not depend on first proving a contradiction in
Lean. A zero-sorry `False` theorem would be a stronger disproof of the source
endpoint; it is not a prerequisite for finding that the affirmative paper has
failed to establish its claimed solution. The distinction is deliberate:
absence of a formal refutation is not positive evidence for the published
claim, and the unresolved correspondence remains the authors' burden to
discharge.

This is not a review of an optional implementation detail. OpenAI's public
announcement presents the work as a solution of the Navier–Stokes existence
and smoothness problem and expressly says that it establishes alternatives
(C) and (D). The paper's Theorem 1.1 makes the same affirmative claim by
asserting existence of the force and fields, bounded kinetic energy, finite-time
velocity blow-up, and the resulting nonexistence conclusion. The adverse
finding in this paper therefore addresses the claim OpenAI actually published:
the inspected record does not establish that the selected endpoint is the
five-moment Navier–Stokes construction used to support that solution claim.

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
singularity. It closes the force-explosion route and moves the live
falsification target back to CTR-005: the missing selected-path transport of
the paper's five moments and absolute pressure semantics.

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

This regularity result does not resolve the review's central objection. The
localisation files contain no debt-vector parameter and no equality to the
paper's `(M,I,J,S,C_p)` moments. They provide debt-blind field identities, not
the missing selected moment-realisation theorem.

## 6. The five-moment correspondence objection

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
3. The repository contains genuine five-row repair mathematics, but the
   selected witness does not expose the paper's five-moment transport theorem.
4. The force-smoothness attack has a proved conditional contradiction, but its
   required selected-field lower bound is missing.
5. The pressure chain has comparison infrastructure, but compact support alone
   does not yield a pressure trivialisation contradiction.

The resulting verdict is:

> **The OpenAI claim is not established as a CMI solution by the inspected
> paper-to-code correspondence. A formal contradiction to the selected Lean
> witness has not yet been proved.**

The two clauses have different logical roles. The first is the review verdict:
the authors have not discharged the burden of showing that the exported
candidate is the five-moment construction described in the paper and that the
required analytic premises hold for that same candidate. The second is a
narrow statement about the present refutation programme: no zero-sorry proof of
`False` has yet been derived from the selected endpoint. Absence of that
refutation is not affirmative evidence for the authors' claim, and the review
does not carry an equal burden to manufacture the authors' missing composition
theorem.

The burden is asymmetric. OpenAI must establish the central solution claim made in the
paper: that the selected fields are the advertised five-moment construction
and that the analytic premises used by the endpoint hold for those same
fields. The reviewer need not prove the negation of the literal existential
endpoint before concluding that this published claim has not been established.
The missing composition theorem is therefore a substantive negative review
finding, not a neutral request for optional documentation.

The load-bearing objection is CTR-005: the missing selected-path transport of
the paper's five moments into the actual velocity, pressure, residual, and
force. The review should be upgraded to a formal refutation only after a
zero-sorry theorem derives `False` from the selected witness and its actual
premises, or proves a false mandatory endpoint predicate.

## 12. Closure correction and the surviving counter-argument

The five-moment objection is not that the repository lacks five-moment
mathematics. A transitive import traversal rooted at
`ActualCandidateAssembly.lean` reaches 507 local modules, including the
positive-order, profile, and rank subsystems. The source contains exact repair
identities and uses rank/debt data upstream of the selected endpoint.

The counter-argument is instead about semantic transport. The public `Witness`
proposition exposes the selected schedule, mixed sums, extensions, force,
candidate properties, consequences, blow-up norm, force decay, and boundary
jets. It does not expose an equality identifying the final mixed fields with
the paper's five quantities

$$
(M,I,J,S,C_p),
$$

nor a theorem carrying that equality into the residual, pressure, force, and
all-order jet estimates. The direct-germ interface is therefore weaker than
the paper's advertised five-moment semantics even though the upstream repair
system is substantive.

The paper itself makes this correspondence indispensable. Its notation table
defines $m=(M,I,J,S,C_p)$ as the five cumulative radial integrals preserving
pressure, radial velocity, and stress across profile joins. The construction
then states that vanishing five moments remove the exterior pressure and stress
tails, solves for five correction coefficients, and uses exact matching to
preserve the subsequent outer fields. Appendix A repeats that the moment
matching and the axis pressure datum preserve every subsequent outer field.
Those are load-bearing assertions in the proof of the advertised solution,
not informal physical commentary. The selected endpoint must therefore expose
the corresponding identities for the actual selected fields.

This is a genuine paper-to-endpoint correspondence failure and the strongest
current counter-paper result. It is not yet a formal `False` theorem: the
review has not shown that the concrete selected fields violate one of those
integral identities. The decisive next step is a field-level transport theorem
or a zero-sorry counterexample to one of its concrete equalities.

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
missing theorem is a selected-path transport identity from
$(M,I,J,S,C_p)$ through the correction state and mixed sums into the residual,
pressure, and force. Evidence:
`NavierStokesReview/evidence/five_row_collision_boundary_2026-09-24.md`.

The runtime scope is now checked separately. `MeanRankUpdate.scaleDebt` has
three debt coordinates, and `FiveRows` constrains only two radial moments of
the correction functions before applying its three debt equations. A compiled
completion constructs a nonzero debt satisfying the full predicate. Thus the
review does not claim that the runtime rows hard-code total kinetic energy to
zero. The unresolved issue is the selected-path transport of the internal
correction data into the exported field and the paper's five named moments.
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
premise or a missing selected-path identity, especially the transport of the
five named moments and pressure semantics into the exported endpoint.

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
force and one trajectory and does not quantify over perturbations. The
counter-paper's formal conclusion is consequently a failed paper-to-endpoint
identification until the missing selected-field moment theorem is supplied or
one of its concrete premises is proved false.

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
but that narrower fact does not discharge the authors' burden for the published
solution claim. A `False` theorem would be a separate, stronger
result, not a prerequisite for this conclusion.

Evidence: `NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.

## Publication decision on the advertised solution claim

The relevant review decision is not a vote on whether Lean can type-check the
exported endpoint. It is whether the inspected record establishes the claim
that OpenAI presents to readers: that the selected five-moment construction is
the construction proving a CMI Navier–Stokes alternative. On that question the
burden is asymmetric. OpenAI must exhibit the selected-field composition and
transport theorems; the reviewer does not have to prove the negation of the
literal existential endpoint before declining acceptance of the advertised
solution claim.

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
\exists d : \operatorname{Debt}_5,
\quad d \ne 0
\quad\land\quad
\operatorname{Witness}_{\mathrm{selected}}.
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

The result also makes the remaining burden exact. The selected field is built
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

The burden remains with the authors because their published theorem claims
that the selected construction establishes the five-moment cancellation and
the CMI alternatives. The source-backed result is therefore a strengthened
publication objection: the advertised solution remains **NOT ESTABLISHED**
until the selected Cartesian-to-radial transport theorem and its numerical or
symbolic consequences are exhibited.

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
tail terms. Until that calculation is supplied, the advertised solution
remains **NOT ESTABLISHED**; no `Delta m ≠ 0` or kernel `False` is asserted.

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
\operatorname{curl}(\chi A)
=\chi\operatorname{curl}(A)
+\operatorname{curlLinear}\big((D\chi).\operatorname{smulRight}(A)\big).
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
claim remains **NOT ESTABLISHED** until the complete selected-field
calculation is supplied.

Evidence: `NavierStokesReview/evidence/selected_cutoff_curl_commutator_2026-09-25.md`.

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
