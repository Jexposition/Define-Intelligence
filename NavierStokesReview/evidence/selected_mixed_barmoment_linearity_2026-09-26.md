# Conditional selected mixed `barMoment` linearity

`SelectedMixedProductionBarMomentLinearity.lean` proves without `sorry`,
custom axioms, or `unsafe` that the selected mixed scalar-family
representative is the pointwise sum of its potential and direct branches.
Under explicit common `Shell` hypotheses for those branches, the source
`DefectIncrementBounds.barMoment_add` theorem then gives

$$
B_k[g_{\mathrm{mixed}}]
 = B_k[g_{\mathrm{potential}}] + B_k[g_{\mathrm{direct}}].
$$

The selected construction does not currently export those common shell
premises for the complete mixed infinite-sum representative. This completion
therefore exposes the exact remaining obligation; it does not evaluate the
weighted integral, prove a nonzero commutator contribution, identify the
result with the five paper moments, or derive `False`.

Focused command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean
  NavierStokesReview/src/completions/SelectedMixedProductionBarMomentLinearity.lean
```

Result: exit code 0.
