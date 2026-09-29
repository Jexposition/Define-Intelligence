# Selected direct radial moment bridge

**Date:** 2026-09-25  
**Tree:** review worktree, with upstream `NavierStokes/` unchanged  
**Claim level:** selected-path positive result; not a disproof

## Result

The review completion
`NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean`
compiles without `sorry`, custom axioms, or `unsafe` declarations.

For every selected direct stage `j`, positive-radius cylindrical point `p`,
and selected carrier point `s`, it proves

$$
u^{\mathrm{direct}}_{j,1}(\operatorname{radialSection}(p))
=
\operatorname{meanField}_{j}(\operatorname{radialSection}(p)),
$$

and

$$
\int_{\mathbb R} r^2\,
\operatorname{torusAverage}(\operatorname{angularNativeStage}_j(n))(r,s)\,dr
=0.
$$

The second identity is obtained from `barMoment_apply`, not from a numerical
approximation.

## Exact Lean anchors

| Lines | Result |
|---:|---|
| 24--26 | Defines the selected scalar as `angularNativeStages` on the actual selected parameters. |
| 28--35 | Identifies the first direct Cartesian component on the positive radial section with that scalar field. |
| 37--41 | Transports the selected cycle order-two moment invariant to the selected scalar. |
| 43--49 | Expands `barMoment_apply` into the torus-averaged radial integral and proves it is zero. |

## Interpretation

This closes the direct scalar branch only.  It does not prove that the full
endpoint velocity has the same moment, because the endpoint is assembled as

$$
\nabla\times A_{\mathrm{sum}}+B_{\mathrm{sum}}.
$$

The missing selected theorem remains the transport of the curl-generated
potential summand through the same radial operator, including localisation,
boundary terms, and the final sum.  Therefore this result narrows the
counter-proof target but does not establish a nonzero remainder or `False`.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean
```

Result: exit code `0`.

The complete review library also built successfully:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

Result: `3708` jobs completed successfully.

The combined upstream and review targets also built successfully:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokes NavierStokesReview
```

Result: `9607` jobs completed successfully.  The endpoint reports only
`propext`, `Classical.choice`, and `Quot.sound` among its axioms.
