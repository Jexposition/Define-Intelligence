# Selected mixed velocity finite-prefix transport

Date: 2026-09-26

## Result

`NavierStokesReview/src/completions/SelectedMixedVelocityFinitePrefix.lean`
compiles without `sorry` or `unsafe` declarations. Its theorem
`selected_mixed_velocity_locally_finite` proves the following selected-path
fact on the source physical domain. For every selected spacetime point there
are finite indices `Np` and `Nd` such that the mixed velocity is eventually
equal to

$$
\sum_{j<N_p}\operatorname{curl}(\operatorname{cutStage}_j)
  + \operatorname{partialPotential}_{N_d}(\text{direct stages}).
$$

The two indices are deliberately separate. The theorem does not assert a
common truncation index, an endpoint value, convergence uniform in the point,
or equality with the radial `barMoment` scalar.

## Source anchors

| Component | Source | Anchor |
|---|---|---|
| `potentialSum` and `partialPotential` | `NavierStokes/SolenoidalDiagonal.lean` | 37-42 |
| local finite-prefix potential theorem | `NavierStokes/SolenoidalDiagonal.lean` | 58-67 |
| local finite-prefix curl theorem | `NavierStokes/SolenoidalDiagonal.lean` | 257-267 |
| selected per-stage smoothness | `NavierStokes/ActualCandidateAssembly.lean` | 879-887 |
| mixed selected decomposition | `NavierStokesReview/src/completions/SelectedMixedVelocityDecomposition.lean` | 21-48 |
| new mixed finite-prefix theorem | `NavierStokesReview/src/completions/SelectedMixedVelocityFinitePrefix.lean` | 24-91 |

## Interpretation

This closes the finite local representative for both branches of the selected
mixed velocity. It does not close the remaining calculation:

$$
\text{selected mixed field}
\longrightarrow \text{Cartesian-to-radial scalar}
\longrightarrow \operatorname{torusAverage}
\longrightarrow \operatorname{barMoment}.
$$

At the singular axis the source scale satisfies `q → 0`, while the local
finite-prefix theorems require `0 < q`. No uniform-in-prefix endpoint transport
or nonzero moment remainder follows from this result. The evidence therefore
supports the existing **NOT ESTABLISHED / correspondence failure** verdict,
not a kernel-level `False`.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedMixedVelocityFinitePrefix.lean
```

Exit status: `0`.

