# Priority 173: Fefferman's connected C specification and the meaning of physical reasonableness

Date: 2026-09-29
Status: authoritative semantic adjudication; no physical-provenance waiver and no selected-field refutation claimed

## Scope

This record answers the specific error the audit must avoid: treating
Fefferman's Alternative (C) as a bare existential wrapper while also making
the opposite error of inventing an additional formal independence axiom that
Fefferman does not state.

The controlling CMI text is `docs/navierstokes.txt:25-81`. The connected
semantic network is:

\[
\begin{aligned}
&(1),(2),(3)\quad\text{fluid PDE, incompressibility, initial datum},\\
&\text{given initial field and given externally applied force},\\
&\text{physically reasonable data}\ \xRightarrow{\text{Hence}}\ (4),(5),\\
&\text{accepted whole-space solution}\ \xRightarrow{\text{only if}}\ (6),(7),\\
&\text{Alternative (C)}:\quad \exists u^\circ,f\ \text{with (4),(5)}\ \land\ \\
&\qquad\neg\exists(p,u)\text{ satisfying }(1),(2),(3),(6),(7)\text{ globally}.
\end{aligned}
\]

The periodic sentence is a different branch:

\[
\text{“Alternatively ... may look”}\ \Rightarrow\ (8),(9)\ \Rightarrow\ (10),(11),
\]

and therefore cannot be used to weaken either branch.

## 1. What the connective words do

### “given” and “externally applied”

These words assign a physical role to the initial field and force: they are
data of the Cauchy problem, not unknown solution components. A residual
construction reverses the *construction order* used by an auditor or author:
one first designs a trajectory and then defines a force that makes the
trajectory solve the equation. That is a real force-provenance question.

It is not, however, an explicit formal predicate in the displayed Alternative
(C) saying

\[
f\ \text{must be independent of the selected }(u,p),
\]

or saying that an existentially constructed smooth function ceases to be
“given” once its formula was discovered from a target trajectory. Therefore
residual provenance is not by itself a proof that the formal C proposition is
false. It remains a material physical-interpretation objection.

### “For physically reasonable solutions ... Hence”

“Hence” is not decorative. Fefferman explicitly links the concern about
growth at spatial infinity to the all-order decay requirements (4) and (5).
For C, the force and initial datum must satisfy that whole-space data class.
Checking only equations (1)--(3) is insufficient.

### “only if”

“Only if” makes (6) and (7) necessary for an accepted global whole-space
solution. A pre-singular blow-up candidate is not itself claimed to satisfy
(6) globally. It is used to exclude a hypothetical global competitor that
would have to satisfy (6) and (7).

### “Alternatively ... may look ... Thus”

“May look” gives solvers a choice of domain formulation. It does not say that
periodicity is optional after the periodic branch is selected. “Thus” replaces
the whole-space data class (4),(5) with (8),(9), and the next acceptance
sentence imposes (10),(11). The pressure periodicity erratum reinforces this
point.

### “retaining the heart of the problem”

This phrase carries the preceding network into A--D. The alternatives retain
the global existence/smoothness-versus-breakdown problem, the relevant data
class, the domain branch, and the accepted solution class. It does not mean
that every internal proof device used by a particular solver must appear as a
named field in a final theorem type.

## 2. Whole-space C: complete formal requirement

The CMI target is not merely

\[
\exists u^\circ,f\;\neg\exists(p,u)\;[(1)\land(2)\land(3)].
\]

It is the connected statement

\[
\begin{aligned}
\exists u^\circ,f\;&\bigl[
 u^\circ\text{ smooth and divergence-free}\land
 f\text{ smooth}\land f,u^\circ\text{ satisfy }(4),(5)\\
&\land\neg\exists(p,u)\text{ on }\mathbb R^3\times[0,\infty):
 (1)\land(2)\land(3)\land(6)\land(7)\bigr].
\end{aligned}
\]

The formal Lean route has been checked against these clauses:

| Connected C clause | Selected Lean record | Adjudication |
|---|---|---|
| \(\nu>0,n=3\) | `navier_stokes_breakdown_R3` | present |
| smooth divergence-free initial datum | zero initial datum and `InitialVelocityConditionDecay` | present |
| smooth force with whole-space decay | global `ContDiff` force, compact support, `ForceConditionDecay` bridge | present on the inspected route |
| (1), (2), (3) for the constructed pre-singular field | residual equality, divergence, zero initial condition on the stated pre-singular domain | present on the inspected route |
| (6), (7) for a prohibited global competitor | `GlobalFiniteEnergySolution` and `Comparator.NavierStokesExistenceAndSmoothnessRn` | present in the contradiction target |
| no such global competitor | comparator bridge and exclusion theorem | present on the inspected route |

The candidate itself is not silently claimed to be a global smooth solution;
its speed is unbounded as \(t\uparrow1\). The contradiction instead says that
any global solution for the same admissible data would agree with the
pre-singular construction and would therefore be impossible. That distinction
is mathematically necessary and is not a loophole.

## 3. What the OpenAI manuscript actually says about the force

The extracted manuscript states that the force may be defined as the momentum
residual and immediately identifies the real challenge: the velocity blows up
while the *total residual and all its derivatives* extend smoothly. It then
states that the background residual is singular, pulse momentum fluxes cancel
its singular part, and further corrections remove the remaining singular
terms. The same manuscript later describes the five cumulative radial profile
integrals as preserving pressure, radial velocity, and stress across profile
joins.

This produces three distinct statements that must not be merged:

1. **Background failure:** the uncorrected background cannot provide the
   required smooth force.
2. **Manuscript mechanism:** pulses, stress matching, further corrections, and
   five-moment profile data are claimed to produce a smooth total residual.
3. **Lean endpoint:** the selected path derives a smooth force through residual
   limits and jet recurrence, but the inspected public endpoint does not export
   a theorem identifying the completed Cartesian field and force with every
   five-moment consequence in the manuscript.

The manuscript therefore does not support the claim that the full construction
“would never occur in physical reality”. The source passage says the
uncorrected background force is unacceptable and then describes corrections
intended to produce the required smooth force. Any stronger attribution needs
an exact source passage and a mathematical check.

## 4. Final adjudication

The audit has two separate verdict layers:

### Formal CMI-shaped proposition

On the inspected Lean path, the whole-space C-shaped proposition is formally
established with the connected decay, smoothness, PDE, initial-data, energy,
and nonexistence predicates. It is not correct to downgrade that result to a
bare `∃u₀,f` wrapper.

### Paper-to-endpoint fidelity

The manuscript's five-moment correction mechanism is load-bearing scientific
content. The inspected endpoint does not expose a theorem transporting the
five reduced-profile observables through the completed selected sums, curl,
localisation, periodisation, pressure, force, and endpoint comparison fields.
Therefore the claim that Lean machine-checked *the manuscript's stated
five-moment mechanism* remains `NOT ESTABLISHED (CTR-005)`.

That is not a claim that the formal C proposition is false, and it is not a
claim that the moments are dispensable in the manuscript. It is a precise
paper-to-code correspondence failure. To escalate beyond CTR-005, the audit
must prove a selected failed CMI premise, a concrete selected moment mismatch,
an impossibility theorem, or a contradiction.

## Evidence

- CMI source: `docs/navierstokes.txt:25-81`.
- OpenAI manuscript: `docs/navier-stokes openai.txt:109-124`, `252-321`,
  and `984-1035`.
- Formal C endpoint: `NavierStokes/ComparatorR3Theorem.lean:21-44`.
- Candidate properties: `NavierStokes/R3/ProblemStatement.lean:90-136`.
- Force bridge: `NavierStokes/R3/ComparatorBridge.lean:22-88`.
- Review probes: `NavierStokesReview/src/probes/CMIQuantifierProbe.lean`,
  `CMIForceBridgeProbe.lean`, and
  `NavierStokesReview/src/extensions/CMIAlternativeCLiteralCrosswalk.lean`.
- Force-smoothness rebuttal adjudication: `NavierStokesReview/src/audit/priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.md` and
  `NavierStokesReview/evidence/source_tranche_priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.json`.
