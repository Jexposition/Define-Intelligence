# Priority 221: Fefferman comparator crosswalk

Date: 2026-10-01
Scope: Fefferman's text mirror, comparator definitions, the R3 candidate
predicate, and the exported forced-breakdown theorem.

## Source specification

Fefferman's text states that the initial velocity is given and smooth, the
force is a given externally applied force, and the spatial decay conditions
are imposed in conditions (4) and (5) at
`docs/navierstokes.txt:25-40`. It defines physically reasonable global
solutions by smoothness and bounded energy at
`docs/navierstokes.txt:41-47`. Alternative (C) quantifies over a smooth
divergence-free initial field and a smooth decaying force for which no global
solution satisfying those conditions exists at
`docs/navierstokes.txt:74-77`.

## Lean comparator mapping

The comparator layer explicitly encodes those requirements:

| CMI requirement | Lean declaration | Source location |
|---|---|---:|
| Smooth, divergence-free, rapidly decaying initial datum | `InitialVelocityConditionDecay` | `NavierStokes/ComparatorDefinitions.lean:124-130` |
| Smooth force with all-order space-time decay | `ForceConditionDecay` | `NavierStokes/ComparatorDefinitions.lean:149-165` |
| Global smooth Navier--Stokes solution | `NavierStokesExistenceAndSmoothness` | `NavierStokes/ComparatorDefinitions.lean:191-209` |
| Global square-integrability and bounded energy | `NavierStokesExistenceAndSmoothnessRn` | `NavierStokes/ComparatorDefinitions.lean:219-227` |
| Pre-singular candidate properties | `R3.ProblemStatement.CandidateProperties` | `NavierStokes/R3/ProblemStatement.lean:92-109` |
| Exported forced candidate theorem | `NavierStokesR3.theorem_1_1` | `NavierStokes/R3/Theorem.lean:46-49` |
| Comparator Alternative (C) theorem | `navier_stokes_breakdown_R3` | `NavierStokes/ComparatorR3Theorem.lean:37-44` |

## Logical result

The source supports the following formal implication chain:

\[
\texttt{theorem\_1\_1}
\Longrightarrow
\texttt{breakdownStatement}
\Longrightarrow
\texttt{navier\_stokes\_breakdown\_R3},
\]

where the comparator theorem carries explicit force-decay and global-solution
conditions. This is stronger than a bare existential shell.

The distinction is:

\[
\text{formal CMI comparator predicate}
\not\equiv
\text{complete semantic identity with every paper mechanism}.
\]

The comparator does not require a named final equality transporting the
manuscript's `(M,I,J,S,C_p)` observables through the selected Cartesian,
localisation, periodisation, summation, pressure, residual, and force route.
That remains the `CTR-005` correspondence question. The residual-defined
force is also a forward-provenance concern because Fefferman describes the
force as given and externally applied, but the literal CMI quantifier itself
does not add an independence predicate.

## Controlled conclusion

This crosswalk clears two inaccurate attacks: it is not valid to call the
comparator admissibility conditions absent, and it is not valid to infer that
the formal C/D-shaped proposition is false merely from residual force design.
It does not clear the paper-to-selected-field correspondence. The controlled
status remains **`CTR-005: NOT ESTABLISHED`** for complete fidelity to the
published mechanism. No literal CMI failure, nonzero selected defect,
impossibility theorem, or `False` is established here.

Evidence: `NavierStokesReview/evidence/fefferman_comparator_crosswalk_2026-10-01.md`.
