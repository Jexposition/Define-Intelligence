# Selected production direct branch after spatial localisation

**Status:** selected source evidence; not a contradiction by itself.

## Result

The native direct-profile result and the exported production field are not the
same expression.  The native result proves

$$
\operatorname{barMoment}_2(\text{selected direct scalar})=0.
$$

The production assembly instead uses

$$
u_{\mathrm{prod}}=\mathrm{periodicVelocity}(A,v),
$$

and on the unit cube the source identity is

$$
\mathrm{periodicVelocity}(A,v)(t,x)
=\mathrm{periodicVelocity}(A)(t,x)
  +\chi(x)\,v(t,x),
$$

where `χ` is `SpatialLocalization.spatialCutoff`.  Therefore the native
zero-moment theorem cannot be substituted for the production-field moment
without evaluating the cutoff-weighted profile and the periodisation/boundary
terms.

## Source anchors

| Item | Source | Lines | Meaning |
|---|---|---:|---|
| Mixed production definition | `NavierStokes/MixedPeriodicAssembly.lean` | 36--38 | Direct field is periodised after `cutPotential`. |
| Cutoff definition | `NavierStokes/SpatialLocalization.lean` | 165--166 | `cutPotential v z = spatialCutoff z.2 • v z`. |
| Periodisation identity | `NavierStokes/PeriodicLocalization.lean` | 272--278 | Supported fields equal their periodisation on the unit cube. |
| Native zero moment | `NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean` | 37--49 | Zero applies to the uncut selected scalar profile. |
| Compiled selected identity | `NavierStokesReview/src/completions/SelectedProductionDirectCutoff.lean` | 23--32 | Exact cutoff-weighted production identity. |
| Selected specialisation | `NavierStokesReview/src/completions/SelectedProductionDirectCutoff.lean` | 35--53 | Same identity for the selected stage sums. |

## Interpretation

This is a concrete implementation mismatch between the paper-level native
profile invariant and the expression entering the production field.  It is a
load-bearing calculation gate for CTR-005.  It does **not** yet prove that the
cutoff-weighted radial integral is nonzero: the sign, support, torus average,
and boundary terms still have to be calculated.  Accordingly it supports
`NOT ESTABLISHED AS A CMI SOLUTION`, not Lean `False`.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

Result: `Build completed successfully (3715 jobs)`; the new completion contains
no `sorry`, `axiom`, or `unsafe` declaration.
