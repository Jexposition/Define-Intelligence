# Selected mixed production radial component

**Date:** 2026-09-26
**Classification:** CTR-005 / CALC-38 selected-field transport evidence
**Status:** verified decomposition; no numerical remainder and no kernel contradiction

## Result

`NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean`
compiles without `sorry`, `axiom`, or `unsafe` declarations. Its theorem
`selected_mixed_production_scalar_split` proves, for every schedule `a` and
positive-radial sampling point `p`, the exact first-component decomposition

$$
u_{\mathrm{mixed},1}(p)
=u_{\mathrm{potential},1}(p)
+\left(\operatorname{periodize}
  \bigl(\operatorname{cutPotential}u_{\mathrm{direct}}\bigr)(p)\right)_1.
$$

Here the potential term is the scalar already named
`selectedPotentialProductionScalar`. The second term is the separately
periodised direct branch.

## Source and review anchors

| Item | Location | Finding |
|---|---|---|
| Mixed endpoint definition | `NavierStokes/MixedPeriodicAssembly.lean:35-38` | The endpoint periodises the potential and direct branches separately. |
| Selected endpoint packaging | `NavierStokes/ActualCandidateAssembly.lean:1121-1151, 1177-1185` | `Witness` and `selected_candidate` consume the mixed field, not the potential-only scalar. |
| Potential scalar | `NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean:28-31` | The existing radial observable samples only the potential branch. |
| Mixed decomposition | `NavierStokesReview/src/completions/SelectedMixedVelocityDecomposition.lean:48-60` | The source-level mixed sum is the potential velocity plus the direct sum. |
| New completion | `NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean:23-46` | Zero-sorry first-component split. |

## Interpretation boundary

The theorem establishes a concrete selected-field scope mismatch: the
potential-only radial scalar is not definitionally the first component of the
exported mixed endpoint. It does **not** prove that the direct term is nonzero,
that its weighted radial integral is nonzero, or that it violates a five-moment
identity. A further theorem must transport the direct periodised term through
`torusAverage` and `barMoment`, or prove that it vanishes under the relevant
support and chart hypotheses.

The controlled verdict remains **NOT ESTABLISHED**, not `False`.

## Verification

Focused command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean \
  NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean
```

Result: exit code 0.
