# Fefferman–OpenAI Navier–Stokes Semantic Crosswalk

**Status:** living source-control document, first complete structural pass
**Date:** 2026-09-29

## Purpose and standard

This document reconstructs Charles Fefferman’s CMI specification and OpenAI’s manuscript as connected mathematical systems, then compares those systems with the Lean declarations. It records definitions, quantifiers, dependencies, implied conditions, and the boundary between a theorem about the Lean encoding and a theorem about the manuscript.

Existing audit notes are navigation aids only. A statement is marked **established** only when its source wording or declaration has been inspected. A statement is marked **not established** when the required implication, transport theorem, or semantic identification has not been found. A missing theorem is not silently converted into either a contradiction or a completed proof.

Whole-source coverage means that every CMI equation, numbered condition, alternative, quantifier, domain, regularity condition, decay condition, and energy condition is represented; every numbered manuscript section and appendix has a row in the section ledger; and every dependency that can change the CMI claim is traced from profile construction through residual correction, summation, localisation, force extension, energy, and comparison.

The exact words remain in the source files. This document supplies the semantic decomposition and coverage ledger needed to audit them without pretending that a short summary is exhaustive.

## 1. Source control

| Source | Current extraction |
|---|---:|
| docs/navierstokes.txt | 210 lines, 14,511 bytes |
| docs/navier-stokes openai.txt | 8,304 lines, 683,841 bytes |
| docs/navierstokes.pdf | 1,827 extracted lines |
| docs/navier-stokes openai.pdf | 23,541 extracted lines |

Text hashes recorded for this pass:

* docs/navierstokes.txt: 35a2891b60b8ba8a65aaf8e1964e38719168c4add277f271b9c377515c7d0759
* docs/navier-stokes openai.txt: f83414ea543ffd89910b9b8a35d1680a2e3295246c91cbedf54e719a7bc316d0
* docs/navierstokes.pdf: c1b5f27b1a64705cfaf1afceea513db5deedca8a18ca56ab32e7f86445a06d0c
* docs/navier-stokes openai.pdf: 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f

## 2. Fefferman’s specification

### 2.0 Verbatim source control

The following is a source-controlled prose excerpt from
`docs/navierstokes.txt`, lines 8–81. Line wrapping and extracted mathematical
notation are normalised for readability; the words themselves are not being
recast as a stronger or weaker specification. It is source text, not an
editorial rewrite. Line references are retained so that the interpretation
below can be checked against the supplied file. Any sentence outside this
block is an audit interpretation and must not be read as Fefferman's wording.

> The Euler and Navier–Stokes equations describe the motion of a fluid in Rn
> (n = 2 or 3). These equations are to be solved for an unknown velocity vector
> u(x, t) = (ui (x, t))1≤i≤n ∈ Rn and pressure p(x, t) ∈ R, defined for position x ∈ Rn
> and time t ≥ 0. We restrict attention here to incompressible fluids filling all of Rn.
>
> Here, u◦ (x) is a given, C ∞ divergence-free vector field on Rn, fi (x, t) are the components of a given, externally applied force (e.g. gravity), ν is a positive coefficient (the viscosity), and ∆ is the Laplacian in the space variables. The Euler equations are equations (1), (2), (3) with ν set equal to zero.
>
> Equation (1) is just Newton’s law f = ma for a fluid element subject to the external force f = (fi (x, t))1≤i≤n and to the forces arising from pressure and friction. Equation (2) just says that the fluid is incompressible. For physically reasonable solutions, we want to make sure u(x, t) does not grow large as |x| → ∞. Hence, we will restrict attention to forces f and initial conditions u◦ that satisfy (4) and (5).
>
> We accept a solution of (1), (2), (3) as physically reasonable only if it satisfies
>
> (6) p, u ∈ C ∞ (Rn × [0, ∞))
>
> and
>
> (7) ∫Rn |u(x, t)|2 dx < C for all t ≥ 0 (bounded energy).
>
> Alternatively, to rule out problems at infinity, we may look for spatially periodic solutions of (1), (2), (3). Thus, we assume that u◦ (x), f (x, t) satisfy (8). In place of (4) and (5), we assume that u◦ is smooth and that (9) holds. We then accept a solution of (1), (2), (3) as physically reasonable if it satisfies (10) and (11).
>
> A fundamental problem in analysis is to decide whether such smooth, physically reasonable solutions exist for the Navier–Stokes equations. To give reasonable leeway to solvers while retaining the heart of the problem, we ask for a proof of one of the following four statements.
>
> (A) Existence and smoothness of Navier–Stokes solutions on R3.
>
> (B) Existence and smoothness of Navier–Stokes solutions in R3/Z3.
>
> (C) Breakdown of Navier–Stokes solutions on R3. Take ν > 0 and n = 3. Then there exist a smooth, divergence-free vector field u◦ (x) on R3 and a smooth f (x, t) on R3 × [0, ∞), satisfying (4), (5), for which there exist no solutions (p, u) of (1), (2), (3), (6), (7) on R3 × [0, ∞).
>
> (D) Breakdown of Navier–Stokes Solutions on R3/Z3. Take ν > 0 and n = 3. Then there exist a smooth, divergence-free vector field u◦ (x) on R3 and a smooth f (x, t) on R3 × [0, ∞), satisfying (8), (9), for which there exist no solutions (p, u) of (1), (2), (3), (10), (11) on R3 × [0, ∞).

The quotation above is intentionally limited to the exact source wording that
controls the audit. The displayed equations (1)–(11) are transcribed separately
in the next subsections. The audit must never replace “given, externally
applied force (e.g. gravity)” with a stronger claim that Fefferman formally
defines a force-independence predicate, and must never replace “for all t ≥ 0”
with a pre-terminal bound.

### 2.1 Objects and meanings

| Exact source phrase or displayed object | Audit interpretation, not a replacement wording | Dependency |
|---|---|---|
| “unknown velocity vector” \(u(x,t)=(u_i(x,t))\) | The solution variable is an \(n\)-component field. | Later claims concern this field and its derivatives, not a profile or potential alone. |
| “pressure” \(p(x,t)\) | A scalar field entering through \(\nabla p\). | Pressure regularity belongs to the solution predicate. |
| \(x\in\mathbb R^n,\ t\ge0\) | Whole-space spatial domain and forward time half-line. | A field defined only for \(t<1\) is not global. |
| “incompressible” | \(\operatorname{div}u=0\). | It is simultaneous with the momentum equation. |
| “given initial field” \(u^\circ\) | Data supplied before the solution is sought. | The solution must equal it at \(t=0\). |
| “given, externally applied force” \(f\) | A force datum in the stated problem formulation. | It must satisfy the force hypotheses; the prose also gives a forward physical interpretation. |
| “physically reasonable” | A solution class including smoothness and energy, not merely a formal PDE equality. | All linked conditions must be satisfied together. |

### 2.1.1 The connected meaning of “physically reasonable”

The phrase cannot be reduced to a synonym for conditions (6) and (7). The
source connects it to the force ontology, the decay hypotheses, the accepted
solution class, and the four alternatives. The controlling source wording is:

> Equation (1) is just Newton’s law f = ma for a fluid element subject to the external force f = (fi (x, t))1≤i≤n and to the forces arising from pressure and friction. Equation (2) just says that the fluid is incompressible. For physically reasonable solutions, we want to make sure u(x, t) does not grow large as |x| → ∞. Hence, we will restrict attention to forces f and initial conditions u◦ that satisfy (4) and (5).

and later:

> A fundamental problem in analysis is to decide whether such smooth, physically reasonable solutions exist for the Navier–Stokes equations. To give reasonable leeway to solvers while retaining the heart of the problem, we ask for a proof of one of the following four statements.

This creates the following semantic dependency, which the audit must preserve:

\[
\begin{aligned}
&\text{external force in Newton's-law framing}
\longrightarrow \text{force and initial-data decay (4)--(5)}\\
&\longrightarrow \text{physically reasonable accepted solution class (6)--(7)}\\
&\longrightarrow \text{the connected alternatives (A)--(D)}.
\end{aligned}
\]

The wording does not by itself add a separately formal predicate called
`ForceIndependentOfTheSelectedTrajectory`. Therefore the audit must not invent
that predicate and claim that the displayed quantifier in (C) literally
contains it. But the opposite shortcut is also invalid: the existential
quantifier does not erase the surrounding meaning of “given, externally
applied force”, the decay requirements, the smooth solution class, the energy
condition, or the instruction to prove one of the four statements as a
connected CMI target. A residual-defined force must consequently be assessed
at both levels: whether it satisfies the displayed formal clauses and whether
the Lean endpoint faithfully represents the connected physical construction
the manuscript claims to realise.

### 2.1.2 The alternatives cite the connected framework, not isolated equations

The alternatives must be read as applications of the preceding framework. They
do not merely cite the symbols “(1), (2), (3)” in isolation. Alternative (C)
explicitly quantifies a smooth, divergence-free (u^\circ), a smooth force
(f) satisfying (4) and (5), and the non-existence of a solution satisfying
(1), (2), (3), (6), and (7) on the whole space and for all (t\ge0). Thus the
logical target is the conjunction

\[
\begin{aligned}
&u^\circ\text{ smooth and divergence-free},\\
&f\text{ smooth and satisfying the all-order decay condition (5)},\\
&\neg\exists(p,u):[(1)\land(2)\land(3)\land(6)\land(7)]
\text{ on }\mathbb R^3\times[0,\infty).
\end{aligned}
\]

Alternative (D) has the corresponding periodic branch: the data must satisfy
(8) and (9), and the prohibited global solution must satisfy (1), (2), (3),
(10), and (11). The references to (6), (7), (9), (10), and (11) are therefore
not decorative equation labels. They select the admissible data and solution
classes that Fefferman has just called “smooth, physically reasonable”.

The immediately following discussion reinforces this reading. Fefferman says
that, for non-small three-dimensional data, the short-time solution has a
maximum allowable interval whose endpoint is called the “blowup time”, and
that if a finite blowup occurs then the velocity becomes unbounded near that
time. He then turns to weak solutions, explicitly distinguishing the weak
integral identities (12) and (13) from the twice-spatially-differentiable
class required by (1). This matters to the audit: a candidate cannot be
credited merely because a residual identity is available on (t<1), or because
an abstract rate contract has a name. The endpoint must be connected to the
force data class and the accepted global solution class that Fefferman
specified.

This does **not** authorise changing Fefferman's wording into a new axiom. It
does require the review to preserve the implication structure he wrote:

\[
\begin{gathered}
\text{external-force/Newton-law framing}\;+
\text{decay data (4),(5)}\\
\Longrightarrow\text{the physically reasonable whole-space problem}\\
\Longrightarrow\text{the global smooth-energy target (6),(7)}\\
\Longrightarrow\text{the meaning of Alternative (C)},
\end{gathered}
\]

and likewise for the periodic chain (8), (9), (10), and (11). The review must
therefore ask whether the selected construction satisfies this connected
target, not merely whether a Lean declaration with a proposition resembling the
last line of (C) compiles.

OpenAI's manuscript itself makes the same connection rather than treating the
force as a free label. It states that the construction uses a smooth,
compactly supported force, defines the force from the momentum residual, and
identifies the central challenge as choosing a blowing-up flow for which that
residual and all of its derivatives extend smoothly through the singular time.
It then attributes that extension to the pulse and correction mechanism. The
paper therefore makes residual regularity part of the proof of admissibility,
not an optional explanation that can be detached from the CMI claim.

The resulting audit distinction is exact:

| Proposition | Current status |
|---|---|
| The inspected Lean theorem proves a Lean proposition whose declared predicates mirror the displayed C clauses: decaying initial data, decaying smooth force, and no global object satisfying the repository's encoded equations, smoothness, and bounded-energy predicates | Established as a formal Lean proposition on the inspected endpoint, subject to the recorded build and axiom ledger; this is not yet a paper-level finding that the connected physically reasonable construction described by Fefferman and OpenAI has been verified |
| The Lean endpoint proves that the selected field and residual realise the connected moment/correction argument used by the manuscript to obtain the smooth force required by Fefferman's physically reasonable CMI target | Not established on the inspected record |
| The selected field or force is mathematically impossible, or violates (4), (5), (6), or (7) | Not proved by the endpoint-omission finding alone |

The second row is the operative paper-to-code finding. It is not a claim that
the moments are irrelevant, removable from the manuscript, or already
transported under an undiscovered theorem. It is a claim that the current
export does not make the connected dependency creditable as a machine-checked
formalisation of the paper's proof. A stronger claim that Alternative (C)
itself fails requires a direct theorem showing that the selected force or field
does not satisfy one of Fefferman's linked conditions, or that the required
moment-to-residual transport is impossible.

### 2.2 Equations (1)–(3)

Fefferman’s momentum equation is

\[
\partial_tu_i+\sum_{j=1}^n u_j\partial_{x_j}u_i
=\nu\Delta u_i-\partial_{x_i}p+f_i(x,t).
\]

With the residual convention used in the audit,

\[
R(u,p):=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p,
\qquad R(u,p)=f.
\]

The incompressibility equation is

\[
\operatorname{div}u=\sum_{i=1}^n\partial_{x_i}u_i=0.
\]

The initial equation is

\[
u(x,0)=u^\circ(x).
\]

The dependency is conjunctive:

\[
\mathrm{Solution}(u,p;u^\circ,f)
\Rightarrow (1)\land(2)\land(3).
\]

It is not enough that a large norm is obtained and that a force is named afterwards. An inverse construction is admissible only if the resulting force satisfies every force-data condition and the resulting fields satisfy the initial-value problem.

### 2.3 Conditions (4) and (5)

For the whole-space problem Fefferman requires, for every multi-index \(\alpha\) and every \(K\),

\[
|\partial_x^\alpha u^\circ(x)|
\le C_{\alpha K}(1+|x|)^{-K},
\]

and, for every \(\alpha,m,K\),

\[
|\partial_x^\alpha\partial_t^m f(x,t)|
\le C_{\alpha m K}(1+|x|+t)^{-K}.
\]

“For any \(\alpha\), \(m\), and \(K\)” quantifies over all derivative orders and all polynomial decay orders. Compact support is stronger than spatial decay only after smoothness of the full extension and all derivative bounds have been proved. These are explicit premises in (C) and (D), not explanatory decoration.

### 2.4 Conditions (6) and (7)

Fefferman accepts a solution only if

\[
p,u\in C^\infty(\mathbb R^n\times[0,\infty))
\]

and

\[
\int_{\mathbb R^n}|u(x,t)|^2\,dx<C
\quad\text{for all }t\ge0.
\]

The phrase “for all \(t\ge0\)” is global. A bound on every compact interval \(0\le t<T<1\) is not literally the same statement. Such a pre-terminal bound can be sufficient inside a comparison proof showing that a global competitor cannot exist, but that is a distinct proposition from saying that the blow-up field itself belongs to the globally accepted solution class.

### 2.5 Periodic alternative and conditions (8)–(11)

The periodic formulation requires

\[
u^\circ(x+e_j)=u^\circ(x),\qquad f(x+e_j,t)=f(x,t),
\quad 1\le j\le n,
\]

and replaces whole-space spatial decay with

\[
|\partial_x^\alpha\partial_t^m f(x,t)|
\le C_{\alpha mK}(1+|t|)^{-K}.
\]

The accepted periodic solution must remain periodic and satisfy global smoothness. Periodising a local field is therefore not enough: the PDE, initial data, pressure, force, regularity, and solution-class conditions must remain connected.

### 2.6 Alternatives (A)–(D)

Alternative (A) is universal unforced existence on \(\mathbb R^3\):

\[
\forall\nu>0\ \forall u^\circ\text{ satisfying (4)}
\ \exists(p,u)\ \mathrm{GlobalSmoothFiniteEnergyNS}(u,p;u^\circ,0).
\]

Alternative (B) is the corresponding universal unforced periodic claim.

Alternative (C) is the forced breakdown claim:

\[
\exists u^\circ\ \exists f\;
\Big(
\operatorname{div}u^\circ=0
\land \operatorname{Decay}_4(u^\circ)
\land \operatorname{Decay}_5(f)
\land
\neg\exists(p,u)\,
\operatorname{GlobalAcceptedSolution}(p,u;u^\circ,f)
\Big).
\]

Alternative (D) is the periodic forced counterpart.

The existential quantifier means that Fefferman’s displayed formal proposition does not contain a separately named independence predicate for \(f\). It does not erase the force hypotheses, the initial-value relation, the global solution class, or the physical wording “given, externally applied force”. Thus residual-designed forcing is not automatically a kernel-level violation of the displayed quantifier, but it remains a material provenance question.

### 2.7 Surrounding prose

Fefferman’s discussion of two-dimensional regularity, small-data results, local existence, and finite blow-up explains the motivation for the four alternatives. It does not weaken them. A finite-time velocity divergence can obstruct global smoothness, but a proof still needs the exact data and solution predicates of the chosen alternative.

### 2.8 Fefferman’s post-alternative context, weak solutions, and errata

The first audit pass must not stop at Alternative (D). Fefferman continues
with the context that distinguishes the strong global solution target from
weak-solution existence and partial regularity. The following source phrases
are retained because they control what may and may not be inferred from a
finite-time singularity.

> These problems are also open and very important for the Euler equations (ν = 0), although the Euler equation is not on the Clay Institute’s list of prize problems.
>
> In two dimensions, the analogues of assertions (A) and (B) have been known for a long time. This gives no hint about the three-dimensional case, since the main difficulties are absent in two dimensions.
>
> For initial data u◦(x) not assumed to be small, it is known that (A) and (B) hold if the time interval [0, ∞) is replaced by a small time interval [0, T), with T depending on the initial data. For a given initial u◦(x), the maximum allowable T is called the “blowup time.”
>
> Either (A) and (B) hold, or else there is a smooth, divergence-free u◦(x) for which (1), (2), (3) have a solution with a finite blowup time.
>
> For the Navier–Stokes equations (ν > 0), if there is a solution with a finite blowup time T, then the velocity becomes unbounded near the blowup time.
>
> Starting with Leray, important progress has been made in understanding weak solutions of the Navier–Stokes equations. To arrive at the idea of a weak solution of a PDE, one integrates the equation against a test function, and then integrates by parts (formally) to make the derivatives fall on the test function.
>
> Note that (12) makes sense for u ∈ L2, f ∈ L1, p ∈ L1, whereas (1) makes sense only if u(x, t) is twice differentiable in x. A solution of (12), (13) is called a weak solution of the Navier–Stokes equations.
>
> Leray showed that the Navier–Stokes equations (1), (2), (3) in three space dimensions always have a weak solution (p, u) with suitable growth properties. Uniqueness of weak solutions of the Navier–Stokes equation is not known.
>
> The partial regularity theorem concerns a parabolic analogue of the Hausdorff dimension of the singular set of a suitable weak solution of Navier–Stokes.
>
> In particular, the singular set of u cannot contain a spacetime curve of the form {(x, t) ∈ R3 × R : x = φ(t)}. This is the best partial regularity theorem known so far for the Navier–Stokes equation.

These paragraphs have four audit consequences. First, “blowup time” is a
statement about the maximal interval of a solution, not by itself a proof of
the forced CMI alternative. Secondly, Fefferman distinguishes the strong
equations (1)–(3), (6), (7) from the weaker distributional formulation (12),
(13). Thirdly, weak-solution existence cannot be substituted for the smooth
global solution predicate in (C). Fourthly, partial regularity does not
replace global smoothness or bounded energy.

The source also contains an Errata block. It states that pressure periodicity
should be explicit in (8), and gives a correction to the displayed weak-form
equation. Those corrections are part of the source record and are not
optional editorial details. They must be carried into any exact CMI crosswalk;
the Lean audit must therefore check pressure periodicity and the corrected
weak-form signs separately from the strong CMI endpoint.

## 3. OpenAI manuscript architecture

The manuscript is an ordered construction, not one isolated blow-up statement:

\[
\begin{aligned}
&\text{similarity geometry and leading profile}
\to\text{background stress and exterior matching}\\
&\to\text{coefficient induction and finite residual}
\to\text{dyadic/torus wave construction}\\
&\to\text{pressure, mean, and five radial corrections}
\to\text{residual decay under iteration}\\
&\to\text{locally finite tsum and flat residual}
\to\text{localisation}\\
&\to\text{smooth compact force extension and comparison contradiction}.
\end{aligned}
\]

These arrows are mathematical dependencies. A Lean import or local certificate is not automatically a proof of the arrow.

### 3.1 Full section ledger

The ranges in the table below are **PDF extraction line ranges**, not the
shorter page-wrapped `navier-stokes openai.txt` line numbers. The PDF
extraction preserves the manuscript's section boundaries and equation
placement; the plain-text extraction is retained for search and hash control
but contains page-footer and layout collapses. This distinction is explicit so
the ledger cannot falsely claim that the 8,304-line plain-text file has lines
past its end.

| Region | PDF-extraction lines | Semantic role and dependency to audit |
|---|---:|---|
| §1.1 Historical context and previous work | 52–124 | Problem setting, incompressible/inviscid distinction, prior results, and target interpretation. |
| §2.1 Inner core | 125–251 | Concentrating core, axis growth, similarity geometry, and singular path. |
| §2.2 Annulus and pulses | 252–293 | Annular transition, pulse families, stress transfer, and retained errors. |
| §2.3 Exterior flow and localisation | 294–327 | Azimuthal exterior, heat flow, support, and localisation plan. |
| §3.1 Concentrating leading field | 328–469 | \(q,\tau,X,\eta\), leading velocity/pressure, and axis asymptotic. |
| §3.2 Background stress | 470–561 | \(E,U\), stress profile, pressure datum, and matching constraints. |
| §3.3 Oscillations and momentum transport | 562–694 | Phases, amplitudes, covariance, energy transfer, and momentum flux. |
| §3.4 Correction and summation | 695–824 | Four correction operations, five radial equations, residual recomputation, and summation. |
| §3.5 Localisation and completion | 825–873 | Cutoffs, curl-after-cutoff, zero extension, residual force, flatness, energy, and comparison. |
| §3.6 Notation and averages | 874–1250 | Choice order, index distinctions, angular/auxiliary torus averages, and normalisation. |
| §4.1 Similarity variables and radial residual | 1251–1425 | Similarity residual and radial integrated equations. |
| §4.2 Cumulative radial integrals | 1426–1586 | Definitions and uses of \(M,I,J,S,C_p\), stress, pressure, and matching. |
| §4.3 Leading stress cone | 1587–1667 | Cone inequalities and positive stress construction. |
| §4.4 Leading profile properties | 1668–1753 | Simultaneous radial, positivity, support, and matching requirements. |
| §4.5 Construction results | 1754–2034 | Compatibility results used to construct the leading profile. |
| §4.6 Leading profile theorem | 2035–2378 | Profile theorem and background consequences. |
| §5.1 Higher coefficients near axis | 2379–2546 | Higher axis coefficient equations and regularity. |
| §5.2 Total radial residual integrals | 2547–2895 | Order-by-order radial defect cancellation. |
| §5.3 Coefficient induction and finite residual | 2896–2964 | Inductive finite-stage residual bounds. |
| §5.4 Divergence-preserving summation | 2965–3161 | Finite tuple summation, divergence, convergence, and bounds. |
| §5.5 Realised base field | 3162–3294 | Limit/base field, pressure, residual, support, and growth. |
| §6.1 Dyadic charts | 3295–3388 | Charts, phase evaluation, and derivative scaling. |
| §6.2 Slow cutoffs | 3389–3520 | Band supports, cutoffs, overlap, and derivative loss. |
| §6.3 Common torus | 3521–3634 | Common auxiliary torus and periodisation conventions. |
| §6.4 Coefficient bounds | 3635–3845 | Coefficients, logarithmic losses, and uniform estimates. |
| §7.1 Phase and transverse frame | 3846–4050 | Phase construction, frames, regularity, and nondegeneracy. |
| §7.2 Pulse equation | 4051–4279 | Pulse solution, shear amplification, viscosity, and derivative control. |
| §7.3 Covariance | 4280–4482 | Leading-wave covariance, linearisation, and stress cone. |
| §7.4 Exact curls and tails | 4483–4630 | Exact divergence-free curls, tails, and covariance remainder. |
| §8.1 Conservative equations | 4631–4681 | Conservative momentum equations and integral constraints. |
| §8.2 Compact primitive | 4682–4829 | Compact primitives for cylindrical weights. |
| §8.3 Pressure reconstruction | 4830–4898 | Pressure and divergence-free velocity corrections. |
| §8.4 Three compatibility defects | 4899–4986 | \(P,J_\theta,J_z\), radial defects, and integrated equations. |
| §8.5 Auxiliary-time inversion | 4987–5053 | Zero-mean inversion and reconstruction remainder. |
| §8.6 Five-dimensional correction | 5054–5208 | Two preserved integrals plus three compatibility corrections. |
| §8.7 Recomputation | 5209–5276 | Full recomputation and compatibility across charts. |
| §9.1 Curl residual estimates | 5277–5374 | Residual estimates for curl-constructed velocities. |
| §9.2 Sources and retained errors | 5375–5520 | Full residual, nonlinear interactions, curl/cutoff errors. |
| §9.3 Full correction cycle | 5521–5803 | Initialisation, iteration, decay exponent, preserved integrals, and summation. |
| §9.4 Common domain | 5804–5937 | Uniform physical derivative estimates and common domains. |
| §9.5 Local field realisation | 5938–6073 | Finite partial sums, local field, smoothness, residual flatness, and growth. |
| §10.1 Localisation | 6074–6139 | Spatial/time cutoffs, curl, support, and zero extension. |
| §10.2 Force derivatives | 6140–6281 | Force before \(t=1\), derivative limits, smooth extension, and support. |
| §10.3 Energy and comparison | 6282–6430 | Energy, dissipation, uniqueness/comparison, and global contradiction. |
| §10.4 Growth, lifespan, viscosity | 6431–6496 | Combines force, energy, growth, and viscosity. |
| §10.5 Periodic equations | 6497–6576 | Periodic equations and periodic interpretation. |
| Appendix A.1–A.7 | 6577–7569 | Finite moment adjustment, outer profile, pressure datum, cone, heat exterior, and exterior stress. |
| Appendix B.1–B.9 | 7574–8268 | Axis data, analytic coefficient space, continuation, stress, choice order, and exact five-moment matching. |
| Appendix C.1–C.3 | 8269–end of appendix | Prescribed mean, radial modulation, exact restoration, and edge completion. |
| References | 8641–end | Prior literature and attribution. |

The appendix headings were found in the extracted source. Final publication citations should use PDF page and equation numbers as well as this text ledger.

## 4. Five cumulative moments and the connected mathematics

The manuscript introduces the radial quantities in §4.2 and uses them in §5.2, §8.6, §9.2–§9.5, and Appendices A–C. In the audit notation:

\[
M=\int_0^XU\,dx,\quad
I=\int_0^XH\,dx,\quad
J=\int_0^XUH\,dx,
\]

\[
S=\int_0^X\left(U^2-\frac{E^2}{2}\right)\,dx,\quad
C_p=\int_0^X\frac{E^2}{2x}\,dx,\quad
H=\sqrt{2X}\,E.
\]

The exact weights and pressure normalisation must always be taken from §4.2 and Appendix A, not reconstructed from memory.

Their connected roles are:

1. \(U,E,\Pi\) determine background stress and axis pressure data.
2. Profile joining and exterior matching use cumulative quantities.
3. Oscillation and correction steps alter finite-dimensional defects.
4. The five-equation correction restores specified quantities and handles three compatibility defects while preserving two invariants.
5. Later residual estimates concern the corrected field.
6. Summation, localisation, and force extension must preserve the identities or replace them with a proved equivalent set of field-level estimates.

The following implication is therefore not free:

\[
\text{profile moments}=0
\Longrightarrow
\text{final Cartesian field moments}=0.
\]

It requires transport through coordinate change, vector-potential lift, curl, cutoffs, periodisation, summation, pressure, force, and endpoint limits.

## 5. Lean crosswalk

### 5.1 Encoded C-shaped proposition

The repository contains a real formal proposition:

\[
\exists u^\circ,f\;
\big[
\operatorname{Decay}(u^\circ)
\land\operatorname{Decay}(f)
\land\neg\exists(v,p)\,
\operatorname{GlobalAcceptedSolution}(v,p;u^\circ,f)
\big].
\]

Relevant declarations:

| Declaration | Role |
|---|---|
| NavierStokes.R3.Theorem.theorem_1_1 | Selected breakdown statement. |
| NavierStokes.ComparatorR3Theorem.navier_stokes_breakdown_R3 | C-shaped comparator quantifiers. |
| ActualCandidateAssembly.Witness | Selected schedules, potential sums, extensions, candidate properties, force regularity, consequences, blow-up, limits. |
| GluedStageEstimates.actualStageEstimates | Concrete stage estimates from physical-cycle data. |
| ActualCycleResidualBounds.finite_residual_rates | Residual rates from actual invariants and PhysicalData. |
| StageEstimates.exists_schedule | Schedules and vanishing joint residual jets. |
| JointResidualLimits.extendedResidual_smooth | Smooth residual extension. |
| CandidateFromLimits.force_smooth | Force smoothness from residual recurrence and compatible limits. |
| MixedPeriodicAssembly.exists_candidate_force | Candidate force and candidate properties. |

The fresh completion at NavierStokesReview/src/completions/SelectedFeffermanAlternativeCProof.lean compiles the encoded C implication with the reported standard axioms propext, Classical.choice, and Quot.sound, subject to the separate whole-repository build caveat caused by the user-owned NavierStokes/R3/TestPressure.lean syntax error.

This is a genuine proof of the **encoded Lean proposition**. It is not automatically a proof that the entire manuscript has been formalised faithfully.

### 5.2 Upstream machinery is real

Earlier wording that the moments were simply dropped or bypassed was too broad. The source shows:

* PositiveOrderMoments.Debt := Fin 5 → ℝ and exact repair identities;
* CorrectionState and FiveRowRank finite-dimensional correction data;
* CycleAnalyticInvariant debt, zero-mass preservation, residual, reconstructed state, waves, pressure, and flatness fields;
* ActualCyclePreservation.state_runInvariant induction of the actual cycle state;
* ActualCycleResidualBounds.Invariant.residual_jetRate consuming actual invariants and actual PhysicalData;
* GluedStageEstimates.actualStageEstimates consuming actual estimates.

The accurate statement is:

> The selected construction uses real physical-cycle and correction data to derive residual-rate and flatness contracts, but the exported Witness does not expose a theorem identifying the final activated Cartesian velocity, pressure, residual, and force with the manuscript’s five cumulative radial observables.

### 5.3 Endpoint omission

ActualCandidateAssembly.Witness around lines 1121–1151 contains the selected schedule, ASum, BSum, PSum, extensions, forcing, CandidateProperties, force regularity, CandidateConsequences, axis blow-up, force derivative decay, and boundary limits. It does not contain an explicit theorem of the form

\[
\operatorname{Moments}(u_{\rm selected},p_{\rm selected},f_{\rm selected})
=(M,I,J,S,C_p),
\]

or an inspected equivalent theorem whose arguments are the final selected Cartesian fields.

This proves only:

* the endpoint proposition does not itself certify that named five-observable equality;
* the selected field has not thereby been shown to have a nonzero defect;
* upstream debt and correction data remain real and are used;
* the complete value-level transport theorem remains unlocated or unproved in this audit.

### 5.4 Force smoothness does not settle manuscript fidelity

The actual Lean route has the structure

\[
\mathrm{PhysicalData}+\mathrm{Invariant}
\to\mathrm{finite\_residual\_rates}
\to\mathrm{StageEstimates}
\to\mathrm{VanishingJointJets}
\to\mathrm{extendedResidual\_smooth}
\to f\in C^\infty.
\]

This defeats the claim that force_smooth is a bare assumption. It does not establish the stronger implication

\[
\text{paper five-moment conditions}
\Longrightarrow
\text{the exact selected VanishingJointJets conditions}
\]

for the final field after all transformations. A rate theorem can be sufficient for force smoothness while remaining semantically insufficient to prove that the manuscript’s advertised five-moment mechanism is what produced that rate theorem.

### 5.5 What the interface probes prove

The StageEstimatesMomentBlindnessProbe and selected-witness obstruction probes prove type-level non-entailment for an abstract five-debt payload. They do not prove that the concrete selected physical field has arbitrary nonzero debt. They prove that the endpoint contract does not force a named five-coordinate debt field to be zero.

A value-level refutation would require

\[
\Delta m=
\operatorname{Moments}(u_{\rm selected},p_{\rm selected},f_{\rm selected})
-(M,I,J,S,C_p)\ne0.
\]

That theorem is not established in this pass.

## 6. Fefferman–OpenAI–Lean compliance matrix

| Requirement | Fefferman meaning | Manuscript dependency | Lean evidence | Current status |
|---|---|---|---|---|
| Equation (1) | Momentum equation with viscosity, pressure, and force. | Residual, local field, extension. | CandidateProperties.residual_eq and force construction. | Encoded equality exists in its stated scope. |
| Equation (2) | Exact incompressibility. | Potentials, curls, and corrections. | Solenoidal and divergence-free fields. | Substantially represented. |
| Equation (3) | Initial datum. | Zero initial state and comparison. | Candidate initial condition and comparator bridge. | Encoded route represents it. |
| Condition (4) | Rapid decay of every initial-data derivative. | Initial field choice. | InitialVelocityConditionDecay. | Encoded predicate is present. |
| Condition (5) | Rapid decay of every force derivative. | Force extension and flat residual. | ForceConditionDecay, ContDiff, derivative decay. | Encoded route proves the predicate; manuscript mechanism identity remains separate. |
| Condition (6) | Global smooth p,u for t≥0. | Forbidden global competitor class. | NavierStokesExistenceAndSmoothnessRn. | Used in comparator. |
| Condition (7) | Uniform global energy. | Energy and comparison. | Global finite-energy solution predicate and candidate energy. | Must be read with exact comparator scope. |
| C quantifiers | Existential forced breakdown. | Theorem 1.1 and comparator. | navier_stokes_breakdown_R3. | Proved as encoded Lean proposition. |
| External force wording | Given externally applied force. | A posteriori residual design. | Residual force route and fixed-force perturbation probe. | Material provenance mismatch, not by itself kernel False. |
| Five moments | Profile and correction engine. | §§4, 5, 8, 9, Appendices A–C. | Positive-order moments, rank, debt, cycle invariants. | Upstream machinery real; final observable identity not established. |
| Curl/localisation transport | Relevant identities must survive final field operations. | §§3.5, 7.4, 9.5, 10.1. | Spatial localisation, solenoidal diagonal, mixed assembly. | Operations exist; full five-observable transport not established. |
| Terminal force smoothness | Force must extend globally through the terminal time. | §10.2 and flat residual. | force_smooth, VanishingJointJets. | Smoothness chain exists; exact five-moment rationale is not yet connected. |

## 7. Adjudication

### 7.1 What is established

The repository proves a Lean proposition whose declared predicates mirror the
displayed clauses of Fefferman Alternative (C), subject to the build caveat.
That is a source-level fact about the Lean definitions and proof term. It is
not yet a paper-level finding that OpenAI has proved Fefferman's connected
“smooth, physically reasonable” construction, because that stronger claim
requires semantic fidelity between the selected Lean fields, the
residual-designed force, and the manuscript's complete correction mechanism:

\[
\exists u^\circ,f\;
\big[
\text{encoded data decay}
\land
\text{no encoded global accepted solution}
\big].
\]

This is not a compiler cheat merely because the proposition is existential.
It is a genuine Lean term for the declared Lean target. The review must not,
however, promote that fact to the unqualified sentence “Alternative (C) is
proved”. Fefferman does not present C as isolated equation labels: C cites
the force/data hypotheses (4)--(5) and the accepted-solution conditions
(6)--(7), after defining them as the connected meaning of a smooth,
physically reasonable solution. The paper-level question is whether the
selected Lean construction establishes that connected object and the
manuscript's route to it.

### 7.2 What is not established

The same theorem does not, without an additional semantic crosswalk, establish

\[
\text{Lean endpoint}
\equiv
\text{every load-bearing manuscript dependency}
\equiv
\text{Fefferman’s connected physical construction}.
\]

The missing equivalence is substantial. The manuscript’s five-coordinate profile identities pass through finite corrections, vector-potential curls, auxiliary averages, shrinking cutoffs, tsum limits, Cartesian fields, pressure reconstruction, force extension, and comparison. The code contains serious ingredients at these stages, but this audit has not found one theorem proving the complete composition.

### 7.3 Claims that must not be made

Current evidence does not justify saying:

* the selected Cartesian defect is nonzero;
* the force is nonsmooth;
* Alternative (C) is formally false in Lean;
* upstream moment corrections are dead code;
* NativeBounds are assumed without derivation;
* five moments are the only source of every residual bound;
* the C-shaped theorem proves the complete manuscript automatically.

Current evidence does justify saying:

* a genuine encoded C-shaped Lean theorem exists;
* upstream physical-cycle, rank, debt, moment, curl, localisation, pressure, and residual machinery is real;
* the final semantic identification between the manuscript’s cumulative observables and the selected Cartesian endpoint is not established in the inspected record;
* the public claim that Lean machine-checks the manuscript’s complete CMI proof is not established until that bridge is proved;
* the residual-force provenance is a separate material concern.

## 8. Required next proof obligations

1. Compute declaration-level dependency closure for selected_witness, theorem_1_1, actualStageEstimates, finite_residual_rates, and force_smooth.
2. Record every moment, debt, mass, rank, and residual declaration actually occurring in the proof terms.
3. Define the exact selected mixed field and the paper observables in one compatible coordinate system.
4. Prove or disprove the composition through finite prefix, tsum, curl, cutoffs, periodisation, pressure, and force extension.
5. Prove the moment-to-jet theorem connecting the concrete five-coordinate corrections to the exact VanishingJointJets used by the selected force route.
6. Recheck the full CMI conjunction: data decay, force smoothness/decay, initial condition, PDE, incompressibility, comparator class, and energy semantics.
7. Change status only when the bridge is proved or a concrete mismatch is proved.

## 9. Evidence index

* NavierStokesReview/evidence/priority_163_direct_cmi_dependency_crosswalk_2026-09-29.md
* NavierStokesReview/evidence/priority_164_direct_cmi_alternative_c_proof_2026-09-29.md
* NavierStokesReview/evidence/selected_physical_data_moment_interface_2026-09-24.md
* NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md
* NavierStokesReview/src/completions/SelectedMixedMomentResidualDecomposition.lean
* NavierStokesReview/src/completions/SelectedProductionDirectCutoff.lean
* NavierStokesReview/src/completions/SelectedPotentialStagewiseCurlOnPhysicalDomain.lean
* NavierStokesReview/src/completions/SelectedFeffermanAlternativeCProof.lean
* docs/OpenAI_NavierStokes_Peer_Review_v1.md
* docs/OpenAI_NavierStokes_Research_Paper.md

## 10. Priority 167 selected-field composition trace

The subsequent declaration-level trace confirms that the selected endpoint is
a genuine composition. Concrete stage data feed `StageEstimates`; the schedule
theorem derives vanishing joint residual jets; the selected fields are formed
by locally finite `potentialSum` terms; mixed curl, cutoff, periodisation, and
time activation are applied; and smooth force data are obtained by residual
extension. The trace does not locate a theorem identifying the completed
Cartesian fields with

\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
 =(M,I,J,S,C_p).
\]

This keeps `CTR-005` precise. The source record supports a concrete
rate-to-flatness and force-smoothness route, while the complete semantic
transport of the manuscript's five observables remains **NOT ESTABLISHED**.
No selected nonzero defect, force nonsmoothness, or literal Alternative (C)
failure is inferred from this omission.

Evidence: `NavierStokesReview/src/audit/priority_167_selected_field_composition_trace_2026-09-29.md`;
`NavierStokesReview/evidence/source_tranche_selected_field_composition_trace_2026-09-29.json`.

## 11. Current conclusion

The correct whole-picture statement is neither “Lean proved nothing” nor “the C-shaped wrapper proves the paper”.

OpenAI’s repository contains a real selected construction and a real proof of its encoded forced breakdown proposition. The upstream moment and correction machinery is not absent, dead, or fabricated. It contributes to actual cycle invariants and residual-rate derivations. However, the present formal record does not yet establish the complete semantic identity between the manuscript’s five cumulative radial repair quantities and the final activated Cartesian fields and force used by the endpoint. Therefore the claim that the Lean development machine-checks the manuscript’s complete CMI proof remains **not established** until the value-level bridge is proved. This is a correspondence finding, not a fabricated kernel contradiction. Conversely, the missing bridge is not permission to report the paper as verified merely because the encoded existential proposition compiles.
## Connected semantic network: Fefferman's words, conditions, and branches

This section makes the connective meaning explicit.  The words “may look for
spatially periodic solutions” introduce an alternative modelling branch.  They
do not make the conditions in that branch optional.  Once the periodic branch
is selected, (8)--(11) replace the whole-space data and acceptance conditions
as a connected package.  Likewise, the phrase “physically reasonable” names
the acceptance class formed by the surrounding definitions; it is not a
decorative adjective that can be removed while retaining the same problem.

### Fefferman dependency graph

```text
unknowns u,p on space-time
        |
        +--> (1) momentum balance
        |       |  contains inertia, viscosity, pressure gradient, and f
        |       |  is interpreted as Newton's law for a fluid element
        |       |
        |       +--> force f is given and externally applied in the stated model
        |
        +--> (2) div u = 0
        |       |  incompressibility constraint on the same u as (1)
        |       |
        +--> (3) u(x,0)=u°(x)
        |       |  couples the unknown trajectory to the prescribed datum
        |
        +--> whole-space branch
        |       +--> (4) rapid decay of every initial-data derivative
        |       +--> (5) rapid decay of every force space-time derivative
        |       +--> (6) global smoothness of p,u
        |       +--> (7) bounded energy for every t >= 0
        |
        +--> periodic branch introduced by “Alternatively ... may look”
                +--> (8) periodic initial data and force
                +--> (9) temporal derivative decay of the force
                +--> (10) periodic solution velocity
                +--> (11) global smoothness of p,u
```

The graph has two different kinds of edge.  Equations (1)--(3) are the
dynamical and initial-value core.  Conditions (4)--(7), or (8)--(11), are the
admissibility and acceptance envelope.  A CMI alternative quantifies over the
data in one branch and quantifies nonexistence over solutions satisfying the
same connected envelope.  It is therefore not enough for a candidate to obey
(1) locally before its terminal time if the requested conclusion is a global
nonexistence statement against objects satisfying (6)--(7), or (10)--(11).

### Word-level connections that control the mathematics

| Wording | Direct mathematical meaning | Dependency it creates |
|---|---|---|
| “unknown velocity vector” and “pressure” | `u` and `p` are the coupled unknown fields on space-time | The same fields must occur in the momentum equation, incompressibility, initial condition, smoothness, and energy clauses. |
| “given” initial field | `u°` is data, not a quantity selected after the solution is known | (3) and the decay/periodicity conditions constrain the candidate before solving. |
| “given, externally applied force” | `f` is data in the stated physical model and enters the momentum balance | (1), (4)/(5) or (8)/(9), and the global solution question use the same force. Residual design is logically possible for an existential witness, but it is a provenance departure that must be reported. |
| “incompressible fluids filling all of \(\mathbb R^n\)” | The whole-space setting is part of the model before the periodic alternative is introduced | It explains why decay at spatial infinity is imposed in (4) and (5). |
| “physically reasonable” | The surrounding data and solution clauses define the accepted class | It binds the equation to decay or periodicity, smoothness, and energy; it is not an independent soft preference. |
| “Hence” before (4) and (5) | The decay requirements are justified by the preceding physical-reasonableness aim | The force and initial data must be checked together with the solution, not only the local PDE identity. |
| “only if” before (6) and (7) | Smoothness and bounded energy are necessary acceptance conditions | A global solution that fails either condition is not an accepted solution for the alternatives. |
| “Alternatively” | A second domain-at-infinity formulation is offered | It switches the data and solution envelope to (8)--(11); it does not delete admissibility requirements. |
| “Thus, we assume” after the periodic alternative | The selected periodic branch receives its own explicit hypotheses | (8) and (9) are premises for the periodic data, not examples. |
| “We then accept” | (10) and (11) are the periodic acceptance conditions | The periodic branch must prove periodicity and smoothness for the same solution fields. |
| “fundamental problem” | The question is global existence and smoothness in the accepted class | It explains why the alternatives quantify over all future time and not merely a local construction. |
| “reasonable leeway” | Fefferman permits either whole-space or periodic formulations | The leeway is a choice of admissible setting, not permission to omit conditions inside that setting. |
| “retaining the heart of the problem” | The global smoothness/existence-versus-breakdown question remains intact | A proposed proof must preserve the connected equation, data, regularity, and energy semantics. |
| “for which there exist no solutions” in (C)/(D) | Nonexistence is relative to the same prescribed data and accepted solution class | A local singular trajectory is not enough unless it rules out every global accepted solution for the same data. |

### The two alternative branches are not interchangeable

For the whole-space branch, the connected target is:

\[
\begin{aligned}
\mathrm{Admissible}_{\mathbb R^3}(u^\circ,f)&:
  (4)\land(5),\\
\mathrm{Accepted}_{\mathbb R^3}(p,u;u^\circ,f)&:
  (1)\land(2)\land(3)\land(6)\land(7).
\end{aligned}
\]

For the periodic branch, the connected target is:

\[
\begin{aligned}
\mathrm{Admissible}_{\mathbb T^3}(u^\circ,f)&:
  (8)\land(9),\\
\mathrm{Accepted}_{\mathbb T^3}(p,u;u^\circ,f)&:
  (1)\land(2)\land(3)\land(10)\land(11).
\end{aligned}
\]

The CMI-shaped breakdown claims are consequently:

\[
\exists u^\circ,f\;\Bigl[
  \mathrm{Admissible}_{\mathbb R^3}(u^\circ,f)\land
  \neg\exists p,u\;\mathrm{Accepted}_{\mathbb R^3}(p,u;u^\circ,f)
\Bigr]
\]

for (C), and the analogous periodic statement for (D).  This formalisation is
useful for the audit because it prevents a common category error: proving a
local residual identity or a pre-terminal field property does not by itself
prove the connected global nonexistence claim.

### Cross-references to the later Fefferman discussion

The later paragraphs are not detached background.  They explain why the
connected package is difficult:

1. The local-in-time result explains that a solution exists for a short
   interval, so the unresolved issue is continuation to all time.
2. The definition of blow-up time connects failure of continuation to
   unbounded velocity near a finite terminal time for Navier--Stokes.
3. The weak-solution discussion explains that equations (12)--(13) weaken
   differentiability requirements and therefore are not interchangeable with
   the smooth accepted class (6)--(7) or (10)--(11).
4. The partial-regularity discussion explains what is known about weak
   solutions and why a singular set result does not settle global smoothness.
5. The closing statement that standard methods appear inadequate supplies the
   motivation for asking for a proof of one of the four connected alternatives.

These connections matter to the OpenAI audit.  The relevant question is not
whether a Lean declaration can be syntactically mapped to the words “there
exist \(u^\circ,f\)”.  It is whether the selected construction supplies the
same data, equations, global acceptance conditions, and physical mechanism
that the manuscript claims to use to establish the relevant whole-space or
periodic alternative.

### OpenAI crosswalk consequence

The OpenAI manuscript's residual construction can be logically analysed in
the connected CMI envelope.  It must establish, for the selected data, all of
the following together:

\[
\begin{array}{c}
u^\circ\text{ satisfies the chosen data conditions},\\
f\text{ is a globally smooth force satisfying the same data conditions},\\
(u,p)\text{ satisfies (1)--(3) before the terminal time},\\
f=\mathcal R(u,p)\text{ extends smoothly through the terminal time},\\
\text{no global accepted solution for the same }(u^\circ,f)\text{ exists}.
\end{array}
\]

The current Lean source supports a concrete residual-rate and smooth-force
route.  It does not yet expose the complete theorem that the selected
Cartesian fields, after the manuscript's profile corrections, sums, curls,
localisation, periodisation, pressure construction, and endpoint extension,
realise every five-moment identity claimed by the manuscript.  That is the
precise remaining correspondence question.  It must neither be weakened into
“the moments do not matter” nor overstated into “the force is already proved
nonsmooth”.
