# Priority 186: Fefferman full word-to-condition connection closure

**Date:** 2026-09-30  
**Status:** source-checked semantic closure; selected CMI compliance remains an
open value-level and provenance adjudication

## Purpose

This record closes the recurring ambiguity between Fefferman's displayed
equations and the surrounding words that determine how those equations are to
be read. The source is `docs/navierstokes.txt:25-81`, with the later context
at `:89-184`. The exact source text remains authoritative. The phrases below
are quoted as phrases, not silently rewritten as new formal axioms.

## 1. The semantic dependency network

Fefferman's specification is not the isolated tuple `(1),(2),(3)`. Its
dependency order is:

\[
\begin{aligned}
&\text{unknown fields }(u,p) + \text{given data }(u^\circ,f)
  \xrightarrow{\text{Newton-law/incompressibility framing}}
  \text{Navier--Stokes initial-value problem}\\
&\xrightarrow{\text{“For physically reasonable solutions”}}
  \text{admissible solution class}\\
&\xrightarrow{\text{“Hence”}}
  \text{whole-space data controls }(4),(5)\\
&\xrightarrow{\text{“only if”}}
  \text{whole-space accepted-solution controls }(6),(7)\\
&\xrightarrow{\text{“Alternatively ... may look”}}
  \text{optional periodic branch}\\
&\xrightarrow{\text{“Thus” and “In place of”}}
  (8),(9)\text{ as periodic data controls}\\
&\xrightarrow{\text{“We then accept”}}
  (10),(11)\text{ as periodic solution controls}\\
&\xrightarrow{\text{“such smooth, physically reasonable solutions”}}
  (A)--(D)\text{ as global alternatives}.
\end{aligned}
\]

Removing one edge changes the proposition being audited. In particular, a
Lean theorem that reproduces only the final existential shape is not thereby a
machine-checked reproduction of the connected physical specification.

## 2. Word-level meanings and mathematical force

| Source wording | Meaning fixed by the surrounding text | Audit consequence |
|---|---|---|
| “unknown velocity vector” and “pressure” | These are the fields to be solved for, not profile coefficients or a potential alone. | Any paper-to-code claim must identify the actual selected `u` and `p`. |
| “given” initial field | `u^\circ` is supplied data in the initial-value problem. | The selected solution must satisfy `u(x,0)=u^\circ(x)`. |
| “given, externally applied force (e.g. gravity)” | Fefferman's physical framing treats `f` as force data acting on the fluid. | Residual-defined forcing is a provenance issue that must be audited, even though C/D do not display a separate independence predicate. |
| “Equation (1) is just Newton's law” | The force, pressure, friction, and acceleration terms have a physical interpretation, not only an algebraic rearrangement. | A residual identity alone does not settle the full physical interpretation. |
| “For physically reasonable solutions” | Introduces the admissible class used in the next conditions. | It cannot be reduced to a decorative adjective or to `(1)--(3)` alone. |
| “Hence” | Links the stated concern about growth as `\(|x|\to\infty\)` to data restrictions `(4),(5)`. | Decay conditions are part of the whole-space problem. |
| “We accept ... only if” | Makes `(6),(7)` necessary for an accepted whole-space solution. | Smoothness and global bounded energy are not optional annotations. |
| “Alternatively” | Introduces a different domain treatment, not a relaxation of the problem. | The periodic route must be audited separately. |
| “we may look for spatially periodic solutions” | Gives solvers permission to choose the periodic branch. | “May” is branch latitude; it is not permission to omit periodic hypotheses once chosen. |
| “Thus, we assume” | Binds the periodic data assumptions `(8),(9)` after branch selection. | The periodic data must satisfy spatial periodicity and time-decay of all derivatives. |
| “In place of” | Replaces whole-space decay controls `(4),(5)` with periodic data controls `(8),(9)`. | It does not replace the PDE, initial condition, or accepted-solution requirements. |
| “We then accept” | Binds periodic accepted-solution conditions `(10),(11)`. | Periodicity and global smoothness remain required. |
| “fundamental problem in analysis” | Names the global existence/smoothness problem as the object of inquiry. | It is not merely a local construction problem. |
| “such smooth, physically reasonable solutions” | “Such” refers back to the entire connected class, not only the nearest equation. | A/D/C/D must be read with the linked conditions. |
| “reasonable leeway” | Explains why four formulations are offered. | The alternatives vary domain/forcing/unforced scope but retain the core regularity question. |
| “retaining the heart of the problem” | States that the four alternatives preserve the global smoothness/existence issue. | A formal encoding that weakens those obligations cannot be advertised as the same problem without qualification. |

## 3. The connected predicates

With `Data₄(u^\circ)` denoting smooth divergence-free initial data satisfying
(4), `Data₅(f)` denoting the all-order space-time decay in (5), and
`Accepted₍R³₎(p,u)` denoting equations (1)--(3), (6), and (7) on the global
half-line, Fefferman's whole-space C alternative is:

\[
\exists u^\circ\,\exists f\,
\bigl(
  \operatorname{SmoothDivFree}(u^\circ)\land
  \operatorname{Data}_4(u^\circ)\land
  \operatorname{Smooth}(f)\land\operatorname{Data}_5(f)\land
  \neg\exists(p,u)\,
  \operatorname{Accepted}_{\mathbb R^3}(p,u;u^\circ,f)
\bigr).
\]

The periodic D alternative is the corresponding branch:

\[
\exists u^\circ\,\exists f\,
\bigl(
  \operatorname{SmoothDivFreePeriodic}(u^\circ)\land
  \operatorname{Data}_{8,9}(u^\circ,f)\land
  \neg\exists(p,u)\,
  \operatorname{Accepted}_{\mathbb T^3}(p,u;u^\circ,f)
\bigr),
\]

where the accepted periodic predicate contains `(1)--(3),(10),(11)` and the
erratum's periodic pressure condition. These formulas are audit notation for
the source network; they do not replace Fefferman's wording.

The later source discussion confirms why the global quantifier matters:
Fefferman distinguishes a finite local interval from the global problem,
calls the maximal local interval the “blowup time”, and distinguishes the
twice-spatially-differentiable equation from weak integral identities (12),(13).
Therefore a construction valid only for `t<1` is not itself an accepted global
solution; it can still be used in a comparison argument against a hypothetical
global competitor, but that implication must be proved.

## 4. OpenAI manuscript crosswalk

The manuscript's own introduction states a force in `C_c^∞`, a field and
pressure on `\mathbb R^3\times[0,1)`, pre-terminal bounded energy, and velocity
blow-up, followed by a consequence ruling out a global same-data solution. In
its physical description it explicitly says that the force can be defined as
the residual, that individual residual terms can diverge, and that the total
residual and all derivatives must extend smoothly through the singular time.
The relevant source records are:

* `docs/navier-stokes openai.txt:31-47` for the theorem statement;
* `:109-124` for residual forcing and cancellation;
* `:306-321` for the residual correction architecture;
* `:523-546`, `:695-784`, and `:5944-6506` for profile matching,
  correction, summation, localisation, force extension, and energy.

The five moments are therefore load-bearing within the manuscript's profile
matching and correction mechanism. The manuscript also contains wave
amplitude, covariance, pressure, auxiliary-time, cutoff, summation, and flat
remainder operations. It is not source-grounded to call the five equations
the only operation in the entire residual proof, but it is equally wrong to
call them optional or detachable from the advertised construction.

## 5. Lean crosswalk and the exact boundary

The inspected Lean source provides a substantive formal route:

* `NavierStokes/ComparatorDefinitions.lean:146-243` defines force smoothness
  and decay, whole-space accepted solutions, periodicity, and energy fields.
* `NavierStokes/CandidateFromLimits.lean:80-214` derives the smooth force from
  residual derivative limits, vanishing jets, support, and the activated
  residual agreement. It is not a bare `NativeBounds` premise.
* `NavierStokes/ComparatorR3Theorem.lean:21-44` maps the selected theorem into
  an operational C-shaped proposition.

That establishes a formal route whose predicates resemble the connected C
package. It does not, by itself, establish the stronger claim that the route
is the manuscript's exact physical construction. The unresolved transport
obligation remains:

\[
\begin{aligned}
&\text{profile moments/rank repair}
\to \text{selected coefficient data}
\to \text{Cartesian potential and curl}
\to \text{cutoff/localisation}
\to \text{actual }\operatorname{tsum}
\to \text{periodisation and averaging}\\
&\to \text{global radial observable and axis totalisation}
\to (M,I,J,S,C_p)\text{ for the selected }(u,p,f).
\end{aligned}
\]

No inspected endpoint theorem closes this complete identity. That is
`CTR-005`: complete paper-to-selected-endpoint fidelity is **NOT
ESTABLISHED**. This is not the same statement as “the selected force is
nonsmooth” or “Alternative (C) is false”. Those stronger conclusions require
one of the following source-bound results:

1. a selected-field mismatch or failed Fefferman condition;
2. a theorem that the required transport is impossible;
3. a contradiction in the selected construction; or
4. a valid proof that the Lean endpoint's connected C/D predicates are not
   actually inhabited by the selected fields.

Conversely, a proof of the missing transport identity would remove this
correspondence gap. The semantic reading does not permit either shortcut:
“Lean compiles, therefore the manuscript is verified” and “the endpoint lacks
a named moment tuple, therefore C is false” are both invalid inferences.

## 6. Adjudication status

| Question | Current status |
|---|---|
| Did Fefferman mean only equations `(1)--(3)`? | **No.** The surrounding wording binds the connected whole-space or periodic accepted-solution package. |
| Does “may look for periodic solutions” waive the periodic conditions? | **No.** It selects a branch whose assumptions and accepted-solution conditions follow immediately. |
| Does “physically reasonable” carry force provenance, decay, smoothness, and energy meaning? | **Yes, semantically.** It is not a separately formal independence predicate in displayed C/D. |
| Does OpenAI's manuscript treat the residual/correction mechanism as irrelevant? | **No.** It makes smooth total-residual extension the central challenge. |
| Does the selected Lean path contain a substantive residual/force/blow-up route? | **Yes, on the inspected source path.** |
| Does the inspected export prove the full manuscript mechanism is transported into the selected Cartesian endpoint? | **Not established.** |
| Has this record proved literal C or D failure? | **No.** No selected failed condition, mismatch, impossibility theorem, or contradiction has yet been proved. |

## Evidence

* `docs/navierstokes.txt:25-81,89-184`
* `docs/navier-stokes openai.txt:31-47,109-124,306-321,523-546,695-784`
* `NavierStokes/ComparatorDefinitions.lean:146-243`
* `NavierStokes/CandidateFromLimits.lean:80-214`
* `NavierStokes/ComparatorR3Theorem.lean:21-44`
* `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`
* `NavierStokesReview/evidence/source_tranche_priority_182_fefferman_semantic_word_to_condition_closure_2026-09-29.json`

