# Priority 182: Fefferman semantic word-to-condition closure

**Date:** 2026-09-29
**Status:** source-grounded semantic control record; no literal C/D failure inferred

## Purpose

This record closes the specific semantic issue raised by the wording in
Fefferman's first two pages. The audit must not read equations `(1)--(11)` as
independent labels. Fefferman uses connective words to define a connected
class of admissible data and accepted solutions, and then carries that class
into alternatives `(A)--(D)`.

The controlling source is `docs/navierstokes.txt:25-81`, checked against the
supplied CMI text. The OpenAI comparison is
`docs/navier-stokes openai.txt:31-47,109-124,306-321,523-546,695-784`.
The Lean comparison is
`NavierStokes/R3/ProblemStatement.lean:90-153`,
`NavierStokes/CandidateFromLimits.lean:80-214`,
`NavierStokes/ComparatorDefinitions.lean:146-243`, and
`NavierStokes/ComparatorR3Theorem.lean:21-44`.

## 1. The connected Fefferman network

The dependency is:

```text
unknown u,p on R^n x [0,infinity)
  -> incompressible equations (1),(2) and datum (3)
  -> given initial field u^o and given externally applied force f
  -> Newton-law / pressure / viscous-force interpretation
  -> physically reasonable solution class
       -> whole-space control at |x| -> infinity
       -> Hence: data decay (4),(5)
       -> only if: accepted global solution conditions (6),(7)
  -> Alternatively, may look for a periodic branch
       -> Thus: periodic data (8),(9)
       -> In place of (4),(5): branch-specific data substitution
       -> We then accept: periodic solution conditions (10),(11)
  -> such smooth, physically reasonable solutions
  -> alternatives (A)--(D), retaining the heart of global existence/smoothness
```

The arrows are semantic dependencies, not claims that Fefferman wrote a
separate theorem for every arrow.

| Exact connective | Semantic work | Consequence for the audit |
|---|---|---|
| `given` | Places `u^o` and `f` on the data side of the forward initial-value problem. | The force cannot be treated as an irrelevant name after selecting a trajectory. |
| `externally applied` | Gives `f` physical provenance in the Newton-law explanation. | Residual-defined forcing requires a provenance discussion; however, the displayed C/D formulas do not add a separate formal independence predicate. |
| `For physically reasonable solutions` | Introduces the class of solutions that the problem accepts. | It is not a loose adjective and cannot be reduced to satisfying `(1)` alone. |
| `want to make sure` | States the physical reason for controlling spatial growth. | The following decay conditions must be read as the data restrictions serving that stated purpose. |
| `Hence` | Connects the growth concern to `(4),(5)`. | Whole-space C cannot be checked from `(1)--(3)` alone. |
| `only if` | Makes `(6),(7)` necessary conditions for an accepted whole-space solution. | A pre-terminal field or local energy bound is not itself an accepted global solution. |
| `Alternatively` | Opens a second treatment of the infinity problem. | It does not weaken the first branch or waive requirements in the second branch. |
| `may look for` | Gives solvers permission to choose the periodic formulation. | It is branch latitude, not optional periodicity after branch selection. |
| `Thus, we assume` | Carries the periodic choice into `(8),(9)`. | D requires periodic data and time-decay hypotheses. |
| `In place of` | Replaces whole-space data controls `(4),(5)` with periodic controls `(8),(9)`. | It does not replace the PDE, initial condition, global time domain, or smoothness. |
| `We then accept` | Defines the accepted periodic solution class through `(10),(11)`. | D cannot be audited from `(1)--(3)` alone. |
| `such smooth, physically reasonable solutions` | Refers back to the complete preceding network. | A surface existential with matching variable names is not automatically semantic equivalence. |
| `while retaining the heart of the problem` | Limits solver latitude to formulations preserving the global existence/smoothness question. | It does not authorise removal of admissibility conditions. |
| `for which there exist no solutions` | Quantifies over every globally admissible competitor for the fixed selected data. | C/D are not merely claims that the displayed pre-singular trajectory stops. |

## 2. The exact connected targets

For the whole-space branch, the relevant target is:

\[
\begin{aligned}
\mathsf C := \exists u^o,f\;[&\mathsf{SmoothDivFree}(u^o)\land(4)\land(5)\\
&\land\neg\exists p,u\;((1)\land(2)\land(3)\land(6)\land(7))].
\end{aligned}
\]

For the periodic branch:

\[
\begin{aligned}
\mathsf D := \exists u^o,f\;[&\mathsf{SmoothDivFree}(u^o)\land(8)\land(9)\\
&\land\neg\exists p,u\;((1)\land(2)\land(3)\land(10)\land(11))].
\end{aligned}
\]

The constructed blow-up field need not itself be a global accepted solution:
it is the local/pre-terminal trajectory used to show that no global accepted
competitor with the same data can exist. That distinction is mathematically
essential. It does not remove the obligation to prove the selected data,
force, PDE, incompressibility, initial datum, smoothness, decay, periodicity
where relevant, and the nonexistence comparison.

## 3. Crosswalk to OpenAI's manuscript

OpenAI explicitly states that it defines the external force as the residual
for a chosen incompressible flow and pressure, then identifies the actual
challenge as making the total residual smooth while the velocity becomes
unbounded. The manuscript says the background residual is unbounded, then
uses oscillatory pulses, further corrections, pressure reconstruction,
radial moment corrections, shrinking cutoffs, summation, and flatness of the
full residual to obtain a smooth compactly supported force.

The manuscript dependency is therefore:

\[
\text{chosen }(u,p)
\to \mathcal R(u,p)
\to \text{stress/wave/pressure/moment corrections}
\to \text{all-order residual flatness}
\to f\in C^\infty\text{ with decay}
\to \text{connected C or D claim}.
\]

The five radial equations are load-bearing in the written joining and
correction mechanism. They are not optional explanatory decoration. The
source also names other coupled operations, so the record must not replace
the supported claim with the stronger unproved statement that the five
moments are the sole cancellation mechanism.

## 4. Crosswalk to the Lean endpoint

The inspected Lean path contains more than a bare existential shell:

* `CandidateProperties` records pre-singular smooth fields, compact support,
  smooth force, force support, zero initial velocity, incompressibility, the
  Navier--Stokes equation on the pre-singular interval, finite energy there,
  and speed unboundedness;
* `CandidateFromLimits.force_smooth` derives smooth forcing from traced
  residual derivative limits and a smooth extension;
* `ComparatorDefinitions` encodes force smoothness/decay, initial-data
  decay, global smooth solutions, incompressibility, the initial condition,
  and bounded whole-space energy;
* `ComparatorR3Theorem.navier_stokes_breakdown_R3` packages the corresponding
  whole-space C-shaped existential/nonexistence proposition.

This establishes an operational formal C-shaped route on the inspected
source path, subject to the recorded build and axiom evidence. It does not
establish that the selected Lean objects reproduce every manuscript-level
consequence of the five-moment mechanism. The unresolved paper-fidelity
question remains the selected-field transport of the manuscript observables
through the actual sum, curl, localisation, periodisation, averaging,
radial-pullback, pressure, force, support, and endpoint comparison.

## 5. Adjudication rules

1. Do not call Fefferman's conditions optional because the alternatives are
   existential. The data-side and accepted-solution-side conditions remain
   connected requirements of the existential predicate.
2. Do not claim that residual design automatically violates C/D. The source
   gives a physical provenance objection, but the displayed C/D formulas do
   not state a separate trajectory-independence axiom. A literal failure
   requires a failed connected condition or a proved mismatch.
3. Do not claim that the absence of a named final five-tuple proves the
   selected force is nonsmooth. The Lean residual-limit route is substantive.
4. Do not claim complete manuscript verification merely because the
   operational C-shaped proposition is present. The selected-field
   paper-fidelity transport remains `NOT ESTABLISHED (CTR-005)`.

## Current result

The correct conclusion is not “Fefferman only asked for equations” and not
“the formal C-shaped proposition is already disproved”. The source-grounded
result is:

\[
\text{connected C/D admissibility is binding}
\quad\land\quad
\text{operational C route is present}
\quad\land\quad
\text{complete manuscript-to-selected-field fidelity is not established}.
\]

A literal C/D refutation requires a connected failed premise, a selected
value mismatch, an impossibility theorem, or a contradiction. The present
semantic network alone does not supply that stronger result.

## Evidence

* `docs/navierstokes.txt:25-81`
* `docs/navier-stokes openai.txt:31-47,109-124,306-321,523-546,695-784`
* `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`
* `NavierStokes/R3/ProblemStatement.lean:90-153`
* `NavierStokes/CandidateFromLimits.lean:80-214`
* `NavierStokes/ComparatorDefinitions.lean:146-243`
* `NavierStokes/ComparatorR3Theorem.lean:21-44`
