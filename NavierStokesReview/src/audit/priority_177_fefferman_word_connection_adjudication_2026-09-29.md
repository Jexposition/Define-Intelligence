# Priority 177: Fefferman word-level connection adjudication

**Date:** 2026-09-29
**Status:** source-grounded semantic audit
**Primary source:** `docs/navierstokes.txt:25-81`

## Finding

Fefferman's CMI statement is a connected specification. The connective words
are not filler around the numbered equations. They determine which objects are
data, which conditions define admissibility, which conditions define an
accepted solution, and which branch is being selected.

This record does not alter Fefferman's wording. It records the mathematical
dependency carried by each connective phrase so that the audit cannot reduce C
or D to an isolated existential sentence containing only `(1)--(3)`.

## Word-level dependency ledger

| Source wording | Immediate semantic operation | Downstream obligation |
| --- | --- | --- |
| “Here” | Binds the definitions of `u°`, `f`, `ν`, and `Δ` to equations `(1)--(3)` | The initial datum and force are part of the same problem object as the unknown `u,p`. |
| “given” | Places `u°` and `f` on the data side of the initial-value problem | The candidate must use the same data in `(3)` and in the global solution/nonexistence claim. |
| “externally applied force (e.g. gravity)” | Supplies the physical provenance of `f` in the Newton-law interpretation | A posteriori residual design must be audited as a provenance issue, even though C’s displayed quantifier has no separately named independence predicate. |
| “The Euler equations are ... with `ν` set equal to zero” | Reuses the same equations and data structure under a parameter change | Navier–Stokes and Euler branches are related by `ν`, not by changing the meaning of the other clauses. |
| “For physically reasonable solutions” | Introduces a normative solution class, not a new equation | The following growth and regularity restrictions qualify the physical problem. |
| “Hence” | Connects the growth-at-infinity concern to data restrictions `(4),(5)` | Decay of initial data and all force derivatives is part of whole-space admissibility. |
| “only if” | Makes `(6),(7)` necessary acceptance conditions | A global PDE solution failing smoothness or bounded energy is outside the accepted whole-space class. |
| “Alternatively” | Opens a second way to control infinity | The periodic branch is a branch substitution, not permission to omit conditions. |
| “may look for spatially periodic solutions” | Gives solver latitude about the domain-at-infinity model | Once selected, the periodic branch must be audited through `(8)--(11)`. |
| “Thus, we assume” | Draws the periodic data hypotheses from the branch choice | `(8),(9)` are premises for the periodic data, not examples. |
| “In place of” | Replaces whole-space data decay with periodic data and force-time decay | `(8),(9)` occupy the data-admissibility role played by `(4),(5)`. |
| “We then accept” | Defines the accepted periodic solution class | Periodicity `(10)` and smoothness `(11)` are mandatory for the same `u,p`. |
| “such smooth, physically reasonable solutions” | Anaphorically refers to the complete preceding framework | A--D inherit the equations, data, domain, regularity, and energy semantics. |
| “while retaining the heart of the problem” | Limits the permitted solver latitude | The global existence/smoothness versus breakdown question remains intact. |
| “for which there exist no solutions” | Quantifies nonexistence relative to fixed admissible data and an accepted class | A local pre-terminal trajectory is insufficient unless it excludes every global accepted solution for those same data. |

## Connected branch formulas

For C, the source-level target is the conjunction

\[
\exists u^\circ,f\;\Bigl[
  \operatorname{SmoothDivFree}(u^\circ)
  \land (4)\land(5)
  \land \neg\exists(p,u)\,\bigl((1)\land(2)\land(3)\land(6)\land(7)\bigr)
\Bigr]
\]

on \(\mathbb R^3\times[0,\infty)\). For D, the corresponding connected
package is `(8),(9)` for the data and `(1),(2),(3),(10),(11)` for the
periodic accepted solution. The wording “may look” does not turn either
package into a menu of independently selectable clauses.

## Audit consequence for the OpenAI correspondence

The inspected Lean route contains concrete residual-limit, smooth-force,
pre-singular PDE, initial-data, energy, and comparator components. That is
evidence for a substantive formalisation of a forced breakdown proposition.
It is not enough, by itself, to credit the manuscript's complete physical
mechanism to the endpoint. The separate manuscript-to-endpoint obligation is

\[
\text{selected activated fields and force}
\longrightarrow
\text{the manuscript's correction and five-moment consequences}
\longrightarrow
\text{the connected C or D admissibility target}.
\]

The current source record has not located that complete selected-field
transport theorem. Therefore the paper-to-endpoint classification remains
**NOT ESTABLISHED (CTR-005)**. This record does not claim a selected nonzero
defect, nonsmooth force, literal C/D failure, or Lean contradiction. Those
stronger outcomes require their own value-level or impossibility theorem.

## Cross-references

* `docs/navierstokes.txt:25-81`
* `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`
* `NavierStokesReview/src/audit/priority_172_fefferman_semantic_network_2026-09-29.md`
* `NavierStokesReview/src/audit/priority_173_fefferman_c_connected_adjudication_2026-09-29.md`
* `NavierStokes/ComparatorR3Theorem.lean:21-44`
* `NavierStokes/R3/ProblemStatement.lean:90-136`
