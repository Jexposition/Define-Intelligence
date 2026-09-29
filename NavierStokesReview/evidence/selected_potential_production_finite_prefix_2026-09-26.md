# Selected potential production finite-prefix expansion

**Date:** 2026-09-26
**Evidence class:** Proven selected finite-prefix identity; no contradiction
**Lean file:** `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean`

## Result

For a selected schedule `a` and finite prefix `N`, the review defines the
actual partial potential used by the source diagonal construction:

$$
A_N=\sum_{j<N}
\operatorname{scaledCutoff}(a_j,q)\,A_j.
$$

The production calculation retains the full product rule

$$
\operatorname{curl}(\chi A_N)
=\chi\,\operatorname{curl}(A_N)
 +(\nabla\chi)\times A_N.
$$

The curl of the partial potential is also expanded into the finite sum of
individual stage curls. This is the exact finite object that must be projected,
averaged, and integrated before passing to the selected `tsum`.

## Source anchors

| Result | Location |
|---|---|
| Selected partial potential | `SelectedPotentialProductionFinitePrefix.lean:22-26` |
| Finite stage-curl expansion | `:28-40` |
| Cutoff/curl product rule | `:42-53` |
| Combined finite production expansion | `:55-75` |
| Source product rule | `NavierStokes/SpatialLocalization.lean:200-207` |
| Source partial-curl expansion | `NavierStokes/SolenoidalDiagonal.lean:242-252` |

## Verification

Command:

```text
cmd /c "C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview"
```

Result: exit code `0`; review library build completed `3731` jobs. The new
review files contain no `sorry`, custom axiom, or `unsafe` declaration.

## Boundary

This result does not evaluate the torus average, radial boundary terms, or the
weighted moment. It therefore proves neither a nonzero `Delta m` nor `False`.
The next task is to apply the scalar section and support facts to this same
finite production object without discarding the commutator.

## Exact moment-interface extension

The completion now also defines
`selectedPotentialPartialProductionPointScalar a N` on the lifted point type
consumed by `DefectIncrementBounds.barMoment`. The zero-sorry theorem
`selected_potential_partial_production_point_barMoment_apply` gives the exact
source expansion

$$
\operatorname{barMoment}_k(F_{a,N})(n,p)=
\int r^k\,\operatorname{torusAverage}(F_{a,N,n})(r,p)\,dr.
$$

The theorem
`selected_potential_partial_production_point_scalar_physical_pullback`
identifies the point section with the selected finite-prefix scalar on the
positive-radius physical section. The theorem
`selected_potential_partial_production_radial_scalar_eq` retains the complete
cutoff/curl commutator for that finite prefix under explicit coordinate and
differentiability hypotheses.

This closes the finite-prefix type and local pullback gates. It still does not
evaluate the integral, prove that the omitted chart region contributes zero,
pass to the infinite `tsum`, or establish a nonzero remainder. No `Delta m ≠ 0`
and no `False` follows.
