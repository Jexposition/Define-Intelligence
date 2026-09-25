# Repository admission axiom log

**Date:** 2026-09-25  
**Scope:** source-tree integrity, separate from the selected R³ endpoint  
**Review module:** `NavierStokesReview/src/audit/RepositoryAdmissionAudit.lean`

## Finding

The repository declares `ComparatorChallenges` as a Lake default target. Its
Navier–Stokes challenge file contains two theorem bodies written `by sorry`,
and its Euler challenge file contains two further admitted declarations. This
is a concrete repository-scope defect in any unqualified statement that the
whole release contains no admitted theorem bodies.

The audit module itself contains no `sorry`, `axiom`, or `unsafe` declaration.
It imports the challenge files only to expose their axiom dependencies through
Lean's `#print axioms` command. The selected endpoint is not thereby made to
depend on the challenge module: `NavierStokes/ComparatorSolution.lean` imports
the independent comparator definitions and the project bridge instead.

## Source locations

| File | Lines | Declaration | Source status |
|---|---:|---|---|
| `ComparatorChallenges/NavierStokes.lean` | 273–284 | `navier_stokes_breakdown_R3`, `navier_stokes_breakdown_periodic` | `by sorry` |
| `ComparatorChallenges/Euler.lean` | 85–88 | `euler_breakdown_R3` | `by sorry` |
| `ComparatorChallenges/Euler.lean` | 181–184 | `exists_compact_smooth_euler_singularity` | `by sorry` |
| `lakefile.toml` | 3, 27–28 | `ComparatorChallenges` | included in default targets |

## Machine output

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/audit/RepositoryAdmissionAudit.lean
```

Result:

```text
'NavierStokes.Comparator.navier_stokes_breakdown_R3' depends on axioms:
[propext, sorryAx, Classical.choice, Quot.sound]
'NavierStokes.Comparator.navier_stokes_breakdown_periodic' depends on axioms:
[propext, sorryAx, Classical.choice, Quot.sound]
'Euler.euler_breakdown_R3' depends on axioms:
[propext, sorryAx, Classical.choice, Quot.sound]
'Euler.exists_compact_smooth_euler_singularity' depends on axioms:
[propext, sorryAx, Classical.choice, Quot.sound]
```

The four `sorryAx` results are decisive for the repository-wide statement,
but not for the narrower question whether the exported selected R³ theorem
imports those declarations. The counter-paper therefore reports both facts:
the release is not globally admitted-free, while endpoint contamination has
not been shown by this census.

## Reproducibility

`lake build ComparatorChallenges` completed successfully under Lean
4.34.0-rc2 and emitted the four corresponding `declaration uses sorry`
warnings. The review-side audit module then compiled successfully with the
same toolchain and no admission in its own declarations.
