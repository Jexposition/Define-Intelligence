# Selected finite-cutoff endpoint

**Date:** 2026-09-26  
**Classification:** source-backed finite-prefix identity; not a selected-field contradiction  
**Finding IDs:** CTR-005, CALC-28, CALC-36

## Result

The review completion
`NavierStokesReview/src/completions/SelectedFiniteCutoffEndpoint.lean:26-43`
proves the following statement. For `0 < h < 1/2`, every fixed finite prefix
of the selected scale sequence has a common left neighbourhood of `t = 1` on
which its cutoffs are all equal to one:

$$
\forall N\;\exists\,\text{a left neighbourhood of }1\;\forall j<N,
\quad \operatorname{scaledCutoff}(a_j,q_h(t,0))=1.
$$

The proof composes the author-source identity
`NavierStokes.AxisPreservation.physicalQ_origin_tendsto` with the source
finite-family plateau theorem
`NavierStokes.SmoothCutoffs.finite_scaledCutoffs_eventually_one`.

## Source anchors

| Fact | Source |
|---|---|
| `scaledCutoff_eventually_one_at_zero` | `NavierStokes/SmoothCutoffs.lean:171-173` |
| finite common plateau | `NavierStokes/SmoothCutoffs.lean:175-186` |
| axis scale identity and limit | `NavierStokes/AxisPreservation.lean:130-148` |
| selected pullback theorem | `NavierStokesReview/src/completions/SelectedFiniteCutoffEndpoint.lean:26-43` |

## Audit meaning

This closes a real endpoint fact for every fixed finite prefix. It does not
show that the infinite `tsum` has a nonzero or divergent value, because the
neighbourhood depends on the finite set of indices. It also does not evaluate
the Cartesian curl, `torusAverage`, `barMoment`, or a selected remainder.
Consequently it does not prove `Delta m != 0`, `False`, or a temporal
discontinuity. The remaining load-bearing task is uniform control of the
prefix-to-`tsum` passage and the resulting weighted radial integral.

## Verification

Focused command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean \
  NavierStokesReview/src/completions/SelectedFiniteCutoffEndpoint.lean
```

Exit status: `0`. The completion introduces no `sorry`, custom `axiom`, or
`unsafe` declaration.
