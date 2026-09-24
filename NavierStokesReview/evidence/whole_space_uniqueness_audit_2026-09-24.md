# Whole-space uniqueness audit

**Scope.** Source tree at the current review branch, with the endpoint traced
from `NavierStokesR3.theorem_1_1` through the whole-space comparison modules.

## Source trace

| Location | Statement | Audit result |
|---|---|---|
| `NavierStokes/R3/ProblemStatement.lean:92-111` | `CandidateProperties` | Requires pre-singular smoothness, compact velocity and pressure slices, smooth compact positive-time force, incompressibility, the residual identity, bounded pre-singular energy, and `SpeedUnboundedAtOne`. |
| `NavierStokes/R3/ProblemStatement.lean:129-137` | `GlobalFiniteEnergySolution` | Requires global half-space smoothness, zero initial data, incompressibility, the same force equation, and uniform square-integrable energy. |
| `NavierStokes/R3/WholeSpaceUniqueness.lean:30-66` | `classical_uniqueness_on_Icc` | Derives equality on a closed interval from the two PDEs, divergence-free conditions, finite energy, compact support of the reference field, and compact-test pressure recovery. |
| `NavierStokes/R3/WholeSpaceUniqueness.lean:104-117` | `candidate_global_agrees_before_one` | Instantiates the comparison theorem with the selected candidate and an arbitrary `GlobalFiniteEnergySolution`. |
| `NavierStokes/R3/CandidateBreakdown.lean:43-51` | `no_global_solution_one` | Converts pre-singular agreement plus compact support and speed blow-up into nonexistence of a global finite-energy competitor. |
| `NavierStokes/R3/Theorem.lean:26-62` | `theorem_1_1` | Exports the full R³ breakdown proposition, not only candidate existence. |
| `NavierStokes/PeriodicPaperTheorem.lean:65-75,155-165` | periodic exclusion and corollary | Separately supplies the periodic C/D branch with velocity and pressure periodicity. |

## Pressure result

`CandidateProperties.pressure_support` is not used as a shortcut to pressure
vanishing in `WholeSpaceUniqueness`. The pressure comparison is derived from
the two residual equations and incompressibility through compact tests:

- `NavierStokes/R3/PressureRecovery.lean:33-46` defines the comparison
  hypotheses;
- `NavierStokes/R3/PressureRecovery.lean:188-229` derives the compact-test
  Poisson identity;
- `NavierStokes/R3/PressureRecovery.lean:388-438` derives the pressure-gradient
  recovery used by the flux estimate;
- `NavierStokes/R3/PressureFlux.lean` instantiates that recovery in
  `classical_uniqueness_on_Icc`.

This is a relative, compact-test pressure argument. It does not establish an
absolute pressure normalisation for the selected candidate. That is a valid
correspondence question, but compact pressure support alone does not produce a
contradiction.

## Kernel and specification result

`NavierStokesReview/src/audit/WholeSpaceAxiomAudit.lean` was checked with the
repository's pinned Lean toolchain. The four queried endpoints depend only on
`propext`, `Classical.choice`, and `Quot.sound`. No `sorry`, custom `axiom`, or
`unsafe` declaration was found in the audited source modules.

The audit therefore does **not** establish `False` for the selected witness.
It does establish two separate review conclusions:

1. The whole-space no-global-solution chain is an active formal component and
   cannot honestly be described as dead code or as a candidate-only theorem.
2. The construction's residual provenance and the paper's language of a
   “given, externally applied force” remain a substantive causal/provenance
   objection. The present Lean endpoint does not encode force independence,
   but that omission is not itself a contradiction of the existential C/D
   proposition.

**Status:** uniqueness route audited; no formal disproof obtained.
