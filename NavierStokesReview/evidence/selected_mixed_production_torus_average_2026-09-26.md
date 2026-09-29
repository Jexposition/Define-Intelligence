# Selected mixed production: radial reduction

## Verified completions

| Item | Location | Result |
|---|---|---|
| Direct branch scalar | `NavierStokesReview/src/completions/SelectedMixedProductionBranchSplit.lean:32-39` | Defines the actual periodised, cut direct contribution on the selected radial section. |
| Branch split | `.../SelectedMixedProductionBranchSplit.lean:42-48` | Zero-sorry pointwise split of the mixed scalar-family pullback into potential plus direct branches. |
| Auxiliary torus average | `NavierStokesReview/src/completions/SelectedMixedProductionTorusAverage.lean:25-31` | Zero-sorry reduction to the value at the zero auxiliary coordinate. |
| Weighted radial reduction | `.../SelectedMixedProductionTorusAverage.lean:34-41` | Zero-sorry identity reducing `barMoment` to the literal mixed radial integral. |
| Verification | Lean 4.34.0-rc2, `lake build NavierStokesReview` | Build completed successfully; no `sorry`, `unsafe`, or custom axiom was added. |

## Exact result

For the scalar-family pullback `ũ` of the actual mixed first component,

$$
\operatorname{barMoment}_k(\widetilde u)(n,p)
=
\int_{\mathbb R} r^k\,
u_{\mathrm{mixed},1}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr)\,dr.
$$

The integrand has the exact pointwise decomposition

$$
u_{\mathrm{mixed},1}=u_{\mathrm{potential},1}
+u_{\mathrm{direct,cut,periodised},1}.
$$

This is the first literal radial integral for the actual mixed endpoint, not
the potential-only surrogate. It is still an identity rather than a value:
the repository and the review completion do not yet prove that the direct
term has a nonzero weighted integral, nor that the integral equals one of the
five named paper moments.
