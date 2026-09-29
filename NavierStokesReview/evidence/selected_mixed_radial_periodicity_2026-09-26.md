# Selected mixed radial periodicity and support obstruction

## Verified source facts

| Item | Location | Result |
|---|---|---|
| Mixed Cartesian periodicity | `NavierStokes/MixedPeriodicAssembly.lean:59-65` | The mixed endpoint satisfies `UnitSpatialPeriodsOn` in every coordinate. |
| Radial pullback periodicity | `NavierStokesReview/src/completions/SelectedMixedRadialPeriodicity.lean:28-60` | Zero-sorry theorem: increasing the cylindrical radial coordinate by one leaves the selected mixed first component unchanged. |
| `barMoment`-integrand periodicity | `.../SelectedMixedRadialPeriodicity.lean:62-70` | The literal radial integrand exposed by the mixed reduction is unit-periodic in its unbounded radial variable. |
| Conditional support obstruction | `NavierStokesReview/src/completions/SelectedMixedRadialSupportObstruction.lean:26-48` | If that pullback is also assumed radially supported in a bounded interval, the repository's generic theorem proves it is identically zero. |
| Verification | Lean 4.34.0-rc2, `lake build NavierStokesReview` | Build completed successfully; no `sorry`, `unsafe`, or custom axiom was added. |

## Mathematical consequence

Let

$$
g_a(r,p)=u_{\mathrm{mixed},1}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr).
$$

The completion proves

$$
g_a(r+1,p)=g_a(r,p).
$$

It also proves the conditional implication

$$
\operatorname{RadiallySupported}_{[\alpha,\beta]}(g_a)
\Longrightarrow
g_a\equiv 0.
$$

This is a genuine selected-field structural constraint, but it is not yet an
unconditional contradiction. The exported `selected_witness` does not provide
the bounded radial-support premise for this periodised mixed pullback, and no
nonzero point of `g_a` has been established here. The result therefore
identifies an exact compatibility obligation: a nontrivial global radial
moment calculation must explain how the unbounded periodic pullback is made
integrable or how the observable is otherwise restricted.
