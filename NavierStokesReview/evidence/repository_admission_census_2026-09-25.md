# Repository admission census: 2026-09-25

## Result

The blanket assertion that the released repository contains no `sorry`
admissions is false on the inspected source tree. The duplicated challenge
library contains explicit admitted theorem bodies.

| File | Lines | Declaration | Source fact |
|---|---:|---|---|
| `ComparatorChallenges/NavierStokes.lean` | 273--277 | `navier_stokes_breakdown_R3` | theorem body is `by sorry` |
| `ComparatorChallenges/NavierStokes.lean` | 280--284 | `navier_stokes_breakdown_periodic` | theorem body is `by sorry` |
| `ComparatorChallenges/Euler.lean` | 85--88 | `euler_breakdown_R3` | theorem body is `by sorry` |
| `ComparatorChallenges/Euler.lean` | 181--184 | periodic Euler challenge declaration | theorem body is `by sorry` |

`lakefile.toml` lists `ComparatorChallenges` in `defaultTargets`, so these
files are part of the repository's default build surface. The file itself
labels the declarations as intentional challenge placeholders. That label
does not make them kernel-proved.

## Claim-level disposition

This census establishes a repository-wide admission defect. It does not show
that `NavierStokes/R3/Theorem.lean` uses these declarations, and it does not
by itself refute the selected exported C/D proposition. The selected endpoint
must therefore continue to be assessed separately with `#print axioms` and its
own dependency path.

The finding is nevertheless material to the published release record: a
claim that the repository as a whole is a zero-sorry formal proof is false.
The paper's affirmative solution claim remains **not established** on the
stronger selected-field correspondence finding recorded under CTR-005.

## Build note

A first attempt with Lean 4.32 was invalid for this checkout because the
locked packages report Lean 4.34.0-rc2. The correctly pinned build is being
run separately. The version mismatch must not be reported as a source theorem
failure.
