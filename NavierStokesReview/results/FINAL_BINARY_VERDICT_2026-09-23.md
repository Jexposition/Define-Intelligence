# Final binary verdict: OpenAI Navier–Stokes claim

Date: 2026-09-23  
Audited public source commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`  
Review branch: `review/cmi-first-navier-stokes-2026-09-22`

## Answer

**YES, for the claim OpenAI actually formalised: a forced counterexample to
CMI Alternative C, and likewise Alternative D.**

**NO, for the unforced Navier–Stokes problem in Alternatives A or B.**

This is not a split-the-difference answer. The CMI statement itself permits a
smooth external force in C and D. OpenAI's exported theorem quantifies over a
positive viscosity, produces initial data and a force satisfying the
Comparator decay predicates, and proves that no global smooth finite-energy
solution exists for that same data and force.

## Why the forced verdict is positive

1. `NavierStokes.R3.Theorem.theorem_1_1` produces the candidate fields,
   smooth positive-time force, finite-energy bound, finite-time unbounded speed,
   and negation of the global finite-energy solution predicate.
2. `NavierStokes.ComparatorR3Theorem.navier_stokes_breakdown_R3` maps that
   candidate to the exact whole-space Comparator proposition.
3. `NavierStokes.R3.ComparatorBridge` preserves the viscosity, initial datum,
   force, PDE, divergence-free condition, and energy bound in the
   candidate-to-comparator direction.
4. The independent headline report contains only
   `propext`, `Classical.choice`, and `Quot.sound`; it contains no `sorryAx`,
   native-evaluation axiom, or project-specific axiom.
5. The independent quantifier probe elaborates the exact CMI-facing
   existential and same-force negated-global-solution shape.
6. An independent `ClaySpec`/`Gap`/`Adapter` chain compiles against the
   current source closure and composes the OpenAI exports into independently
   written Clay C and D propositions, with the same standard-only axiom set.

The construction's force is residual-engineered. That is a design choice, not
a CMI violation, because C and D ask for existence of a smooth admissible
force rather than `f = 0`.

## What is not proved

The repository does not establish A or B, which require zero force. It also
does not turn the result into a theorem that arbitrary unforced three-
dimensional data blow up. Critiques aimed at that stronger statement are
correctly scoped as objections to an unforced interpretation, not as
refutations of C or D.

## Adversarial findings

No confirmed formal counterexample was found in the audited bridge, pressure
comparison, viscosity scaling, force-decay map, endpoint filter, or annular
regularity guards. The generic `JetRate` API admits vacuous bottom-filter
proofs, but the selected endpoint used by the audited path was separately
proved nontrivial; this is a specification-quality warning, not a disproof of
the exported theorem.

The independent semantic bridge is now also checked against the current
public source, not only the earlier audit snapshot. Its final adapter proves
the current OpenAI exports imply independently written Clay C and D
statements. See `INDEPENDENT_CLAY_BRIDGE_CURRENT_2026-09-23.txt`.

## CMI status versus theorem status

This report answers whether the formalised mathematical claim is proved in the
repository. CMI prize recognition is a separate institutional process. The
official problem statement identifies C and D as valid alternatives, while
the CMI acceptance process requires publication, rigorous examination, and
general acceptance. That procedural status does not change the theorem-level
answer above.

## Evidence

- `NavierStokes/R3/Theorem.lean`
- `NavierStokes/ComparatorR3Theorem.lean`
- `NavierStokes/R3/ComparatorBridge.lean`
- `NavierStokesReview/results/HEADLINE_AXIOMS_4_34_RC2.txt`
- `NavierStokesReview/results/CMI_QUANTIFIER_PROBE_4_34_RC2.txt`
- `NavierStokesReview/results/OPEN_PAST_NEBOT_4_34_RC2.txt`
- `docs/OpenAI_NavierStokes_Axiom_Ledger.md`
