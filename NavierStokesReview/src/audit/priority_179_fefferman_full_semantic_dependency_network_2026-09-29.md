# Priority 179: Fefferman's full semantic dependency network

Date: 2026-09-29
Status: source-grounded semantic crosswalk; no isolated-C shortcut

## Purpose

This record answers the specific semantic issue raised by the wording
“Alternatively, to rule out problems at infinity, we may look for spatially
periodic solutions ... Thus, we assume ...”. The word “may” gives latitude to
choose a branch. It does not make the conditions of the chosen branch
optional. The audit therefore follows Fefferman's text as a connected
specification, preserving the source wording and recording the mathematical
dependency carried by each connection.

The controlling source is `docs/navierstokes.txt:25-166`, checked against the
supplied CMI PDF. The OpenAI comparison sources are
`docs/navier-stokes openai.txt:33-43,109-124,252-321,1573-1585,1670-1684`.
The Lean comparison sources are
`NavierStokes/R3/ProblemStatement.lean:90-153`,
`NavierStokes/CandidateFromLimits.lean:80-214`, and
`NavierStokes/ComparatorR3Theorem.lean:21-44`.

## 1. The source network, in order

### F1. Unknowns, domain, and equations

Fefferman first fixes the mathematical object: unknown velocity `u(x,t)`,
pressure `p(x,t)`, space `x in R^n`, forward time `t >= 0`, incompressibility,
viscosity, and equations `(1)`, `(2)`, with initial condition `(3)`. The
equations are not a detached display. They define the fluid initial-value
problem whose accepted solutions are classified later.

**Edge F1 -> F2:** every later data, regularity, energy, periodicity, and
nonexistence clause refers to these same fields and this same forward problem.

### F2. Data and physical interpretation

The text calls `u^o` a “given, C-infinity divergence-free vector field” and
`f_i(x,t)` the components of a “given, externally applied force”. It then
explains equation `(1)` through Newton's law for a fluid element subject to
the external force and pressure/friction forces, and equation `(2)` as
incompressibility.

**Edge F2 -> F3:** the force and initial field are data of the problem, not
unknowns that may be dropped after a trajectory has been selected. This gives
the residual-defined force construction a genuine physical-provenance issue.
The displayed C/D formulas do not add a separately named logical predicate
that says `f` must be independent of a trajectory used to discover it. Thus,
provenance is a material semantic requirement and audit obligation, but the
audit must not invent a formal clause that is absent from the statement.

### F3. “For physically reasonable solutions ... Hence”

The phrase “For physically reasonable solutions” introduces the class of
solutions the problem will accept. The sentence says that the purpose is to
prevent `u(x,t)` becoming large as `|x| -> infinity`. “Hence” connects that
physical concern to the all-order data restrictions `(4)` and `(5)`.

For the whole-space branch, the connection is:

\[
\text{physical control at spatial infinity}
\xRightarrow{\text{Hence}}
\text{all-order decay of }u^o\text{ and }f.
\]

The force condition `(5)` is not just a statement about the force at one
time. It quantifies over every spatial derivative order `alpha`, time order
`m`, and decay order `K`, uniformly on `R^n x [0,infinity)` in the stated
weighted sense.

**Edge F3 -> F4:** equations `(1)-(3)` alone do not define the accepted
whole-space problem. The data class `(4),(5)` is part of the target.

### F4. “We accept ... only if”

Fefferman writes “We accept a solution of `(1),(2),(3)` as physically
reasonable only if it satisfies `(6),(7)`.” “Only if” is a necessary-condition
operator. It makes global smoothness and bounded energy requirements for the
accepted whole-space solution class:

\[
p,u\in C^\infty(\mathbb R^n\times[0,\infty)),
\qquad
\int_{\mathbb R^n}|u(x,t)|^2\,dx<C\quad\text{for every }t\ge 0.
\]

**Edge F4 -> F5:** a field defined only for `t < 1` and becoming unbounded as
`t` approaches `1` is not itself an accepted global solution. In a breakdown
argument it is instead used to exclude every hypothetical global solution
with the same data that would have to satisfy `(6),(7)`.

### F5. The branch sentence: “Alternatively ... may look ... Thus”

“Alternatively, to rule out problems at infinity, we may look for spatially
periodic solutions” creates a second domain-at-infinity branch. “May look” is
the branch-choice permission. It is not a waiver of the definition of a
physically reasonable solution.

“Thus, we assume” draws the periodic data hypotheses `(8)` from that branch
choice. “In place of `(4)` and `(5)`” explicitly states that `(8),(9)` replace
the whole-space data conditions for the periodic branch. “We then accept”
introduces the periodic accepted-solution conditions `(10),(11)`.

The dependency is therefore:

\[
\begin{aligned}
\text{choose periodic branch}
&\xRightarrow{\text{Thus}} (8),(9)\text{ for the data}\\
&\xRightarrow{\text{In place of}} (4),(5)\text{ in that branch}\\
&\xRightarrow{\text{We then accept}} (10),(11)\text{ for the global solution}.
\end{aligned}
\]

The pressure-periodicity erratum reinforces that the periodic branch is a
complete solution specification, not a velocity-only convenience.

### F6. “such smooth, physically reasonable solutions” and “retaining the heart”

The phrase “such smooth, physically reasonable solutions” is an anaphoric
reference to the whole preceding network: equations, data, selected domain
branch, spatial behaviour, global smoothness, energy, and periodicity where
applicable. It cannot be read as referring to `(1)-(3)` alone.

“To give reasonable leeway to solvers while retaining the heart of the
problem” permits the solver to choose among the four stated alternatives and
the two domain formulations. It preserves the central question: global
existence and smoothness versus breakdown for the physically reasonable class.

**Edge F6 -> F7:** C and D must be audited as connected packages, not as
surface existential formulas stripped of the surrounding definitions.

## 2. The complete C and D targets

The whole-space C target is:

\[
\begin{aligned}
\exists u^o,f\;\Big[&u^o\text{ smooth and divergence-free}\land(4)\land(5)\\
&\land\neg\exists(p,u)\text{ on }\mathbb R^3\times[0,\infty):
(1)\land(2)\land(3)\land(6)\land(7)\Big].
\end{aligned}
\]

The periodic D target is:

\[
\begin{aligned}
\exists u^o,f\;\Big[&u^o\text{ smooth and divergence-free}\land(8)\land(9)\\
&\land\neg\exists(p,u)\text{ on }\mathbb R^3\times[0,\infty):
(1)\land(2)\land(3)\land(10)\land(11)\Big].
\end{aligned}
\]

The words “for which there exist no solutions” bind the nonexistence claim to
the same selected admissible data. They do not merely say that one displayed
candidate stops before time one.

## 3. Crosswalk to OpenAI's manuscript

The OpenAI manuscript explicitly says that the force can be defined as the
momentum residual and immediately states the real challenge: the velocity may
blow up while the total residual and all its derivatives extend smoothly
through the singular time. It then says that the uncorrected background
residual is unbounded, that oscillatory pulses cancel its singular part, and
that further corrections remove remaining singular errors.

This gives the manuscript-level dependency:

\[
\text{selected flow and pressure}
\to \text{residual}
\to \text{pulse/stress/moment corrections}
\to \text{smooth total force}
\to \text{connected C or D admissibility}.
\]

The five moments are load-bearing within that manuscript mechanism. The
manuscript also uses other operations, including wave-flux construction,
cutoffs, pressure reconstruction, covariance correction, time inversion, and
nonlinear estimates. It is therefore incorrect both to call the moments
optional and to say that no other construction stage exists.

## 4. Crosswalk to the inspected Lean endpoint

The Lean record is not an equation-only shell. The inspected path contains:

1. `CandidateProperties` with pre-singular smooth velocity and pressure;
2. compact support conditions;
3. globally smooth force and compact positive-time support;
4. zero initial velocity;
5. divergence-free velocity;
6. residual equality on `0 < t < 1`;
7. uniform finite energy on `0 <= t < 1`; and
8. speed unboundedness at time one.

`CandidateFromLimits.force_smooth` is derived from a traced residual,
locally-uniform derivative limits, and a smooth extension. It is not correct
to infer that every individual residual summand must diverge merely because
the velocity norm diverges; cancellation is precisely what the construction
claims to arrange.

`ComparatorR3Theorem.navier_stokes_breakdown_R3` then converts the selected
candidate into the connected C-shaped existential target and excludes a
global smooth finite-energy competitor with the same force and initial datum.

The separate correspondence question remains exact: the inspected public
endpoint does not expose a theorem identifying the completed selected
Cartesian velocity, pressure, residual, and force with all manuscript-level
five-moment consequences. This is **NOT ESTABLISHED (CTR-005)** for
paper-to-endpoint fidelity. It is not, without a further selected-field
theorem, proof of a nonzero defect, a nonsmooth force, literal C/D failure, or
`False`.

## 5. Adjudication rules applied from this network

| Question | Required reading | Current result |
| --- | --- | --- |
| Does “may look” make periodic conditions optional? | No. It permits branch selection; the selected branch is then bound by `(8)-(11)`. | Confirmed from source wording. |
| Can C be reduced to `(1)-(3)`? | No. Whole-space C carries data `(4),(5)` and accepted-solution `(6),(7)`. | Confirmed from source and comparator crosswalk. |
| Does “physically reasonable” matter? | Yes. It names the accepted class and connects to decay, smoothness, and energy. | Confirmed. |
| Does “externally applied” itself create a formal independence axiom? | No explicit predicate is stated in the displayed alternatives. It remains a physical provenance obligation. | Provenance mismatch remains an open semantic audit issue, not an invented theorem. |
| Does Lean establish a connected formal C-shaped route? | Yes, on the inspected path, subject to recorded build and source scope. | Established. |
| Does Lean establish the manuscript's complete five-moment mechanism at the selected endpoint? | Only if a selected-field transport theorem is found or proved. | **NOT ESTABLISHED (CTR-005).** |

## Evidence and cross-references

- Fefferman source: `docs/navierstokes.txt:25-166` and `docs/navierstokes.pdf`.
- OpenAI manuscript extraction: `docs/navier-stokes openai.txt:33-43,109-124,252-321,1573-1585,1670-1684`.
- Existing semantic records: `priority_172_fefferman_semantic_network_2026-09-29.md`,
  `priority_173_fefferman_c_connected_adjudication_2026-09-29.md`, and
  `priority_177_fefferman_word_connection_adjudication_2026-09-29.md`.
- Lean endpoint: `NavierStokes/R3/ProblemStatement.lean:90-153`,
  `NavierStokes/CandidateFromLimits.lean:80-214`, and
  `NavierStokes/ComparatorR3Theorem.lean:21-44`.
- Controlling crosswalk: `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`.

## Priority 180: connected admissibility graph, not isolated citations

The supplied Fefferman text makes the dependency structure explicit. The
following graph is the controlling interpretation for the audit:

```text
unknown u,p on R^n x [0,infinity)
  -> incompressible Navier--Stokes system (1),(2),(3)
  -> given initial datum u^o and given externally applied force f
  -> Newton-law / pressure / viscous-force interpretation
  -> physically reasonable solution class
       -> whole-space concern at |x| -> infinity
       -> hence data restrictions (4),(5)
       -> accepted solution only if (6),(7)
  -> alternatively choose the periodic branch
       -> thus periodic data assumptions (8),(9)
       -> in place of (4),(5), not in place of the PDE or time domain
       -> periodic solution accepted only if (10),(11)
  -> such smooth, physically reasonable solutions
  -> alternatives (A)--(D), retaining the heart of the global question
```

The connective words have logical work:

| Source wording | What it does | What cannot be inferred |
|---|---|---|
| “Here” | Assigns the status of (u^o), (f), ν, and Δ before the equations are used. | The force is not merely an arbitrary post hoc symbol in the physical reading. |
| “given” | Places (u^o) and (f) on the datum side of the forward problem. | It does not by itself create a formal independence axiom. |
| “externally applied” | Gives (f) physical provenance in the Newton-law explanation. | It cannot be erased when assessing physical meaning. |
| “For physically reasonable solutions” | Introduces a class of solutions, not a loose adjective. | It cannot be reduced to satisfying (1) alone. |
| “Hence” | Connects the stated growth concern to the all-order decay conditions (4),(5). | Conditions (4),(5) are not optional decoration for the whole-space branch. |
| “only if” | Makes (6),(7) necessary for an accepted whole-space solution. | A pre-singular or merely local bound is not the same as (7), which quantifies all (t\ge0). |
| “Alternatively” | Opens a second domain-at-infinity branch. | It does not relax the accepted-solution conditions inside the chosen branch. |
| “may look for” | Gives solvers latitude to choose periodic rather than whole-space treatment. | It does not mean periodicity is a suggestion after the periodic branch is chosen. |
| “Thus, we assume” | Carries the branch choice into periodic data assumptions (8),(9). | Conditions (8),(9) cannot be omitted from D. |
| “In place of” | Substitutes periodic data controls for (4),(5). | It does not substitute away (1)--(3), smoothness, or the forward domain. |
| “We then accept” | Defines the accepted periodic solution class by (10),(11). | D cannot be checked from (1)--(3) alone. |
| “such smooth, physically reasonable solutions” | Refers back to the complete connected class. | A bare existential with matching variable names is not automatically semantic equivalence. |
| “while retaining the heart” | Limits solver flexibility to formulations preserving global existence/smoothness. | It does not authorise removal of the admissibility package. |
| “for which there exist no solutions” | Quantifies nonexistence of any globally admissible competitor for the fixed data. | It is not merely nonexistence of the displayed constructed trajectory. |

For audit notation only, the connected target predicates are:

\[
\begin{aligned}
\mathsf{Data}_{\mathbb R^3}(u^o,f) &:= \mathsf{SmoothDivFree}(u^o)\land(4)\land(5),\\
\mathsf{Accept}_{\mathbb R^3}(p,u;u^o,f) &:= (1)\land(2)\land(3)\land(6)\land(7),\\
\mathsf C &:= \exists u^o,f\;[\mathsf{Data}_{\mathbb R^3}(u^o,f)\land
\neg\exists p,u\;\mathsf{Accept}_{\mathbb R^3}(p,u;u^o,f)].
\end{aligned}
\]

For the periodic branch:

\[
\begin{aligned}
\mathsf{Data}_{\mathbb T^3}(u^o,f) &:= \mathsf{SmoothDivFree}(u^o)\land(8)\land(9),\\
\mathsf{Accept}_{\mathbb T^3}(p,u;u^o,f) &:= (1)\land(2)\land(3)\land(10)\land(11),\\
\mathsf D &:= \exists u^o,f\;[\mathsf{Data}_{\mathbb T^3}(u^o,f)\land
\neg\exists p,u\;\mathsf{Accept}_{\mathbb T^3}(p,u;u^o,f)].
\end{aligned}
\]

This yields two separate audit questions. First, does the Lean proposition
itself encode the complete connected Fefferman package? Secondly, does the
selected Lean construction prove the same force, field, pressure, localisation,
moment, residual, smoothness, and energy mechanism described by the OpenAI
manuscript? The current record gives a positive answer to the first question
for the inspected formal C-shaped endpoint, subject to its build and axiom
ledger. It does not yet give a positive answer to the second. The missing
selected-field theorem is therefore material to the advertised paper-to-code
claim. This is the precise scope of CTR-005. It is not a claim that Fefferman's
conditions are optional, and it is not by itself a proof that the selected
fields fail them.

Evidence:

- `docs/navierstokes.txt:25-81`
- `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`
- `NavierStokesReview/evidence/source_tranche_priority_179_fefferman_full_semantic_dependency_network_2026-09-29.json`
