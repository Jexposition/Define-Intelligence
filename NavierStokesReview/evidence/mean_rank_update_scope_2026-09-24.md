# Mean-rank update scope

## Result

The runtime rank interface does not clamp total mass or kinetic energy to zero.
It solves five radial equations for two correction functions while carrying a
three-coordinate debt. The first two equations constrain only those correction
functions. The source also constructs the correction functions for a nonzero
debt, so the zero rows cannot be used as a type-level contradiction by
themselves.

## Flat source ledger

| Source | Lines | Exact role | Review consequence |
|---|---:|---|---|
| `NavierStokes/FiveRowRank.lean` | 21--22 | `Debt := Fin 3 → ℝ` | Runtime debt has three coordinates. |
| `NavierStokes/FiveRowRank.lean` | 241--247 | `FiveRows` starts with `∫ R, R^2 * dv R = 0` and `∫ R, R * ga R = 0`, then has three debt rows. | The zero rows concern `dv` and `ga`, not the exported velocity or kinetic energy. |
| `NavierStokes/FiveRowRank.lean` | 279--284 | `five_rows` supplies correction functions for arbitrary `d : Debt`. | Nonzero debt is compatible with the two zero correction rows. |
| `NavierStokes/MeanRankUpdate.lean` | 24--34 | `scaleDebt` maps `(d 0,d 1,d 2)` to `(U^2 d0, ℓ^3U^2 d1, ℓ^2U^2 d2)`. | Scaling transports the three debts; it does not add the paper's five named moments. |
| `NavierStokes/MeanRankUpdate.lean` | 136--151 | `fiveRows_scaled` preserves the five-row predicate under radial scaling. | This is a local rank-interface theorem, not a selected Cartesian-field theorem. |
| `NavierStokes/MeanRankUpdate.lean` | 153--200 | `angularIncrement`, `desiredAxialIncrement`, and `physical_rows_on_patch`. | The constructed increments satisfy the rank predicate on the patch. |
| `NavierStokes/DefectIncrementBounds.lean` | 799--813 | `RankGeometry.preserve_masses` and `zeroMasses`. | Two internal radial moments are preserved on `CorrectionState`; no kinetic-energy identity is stated. |
| `NavierStokes/ActualCandidateConstruction.lean` | 392--437 | Selected direct stages are cycle-mean increments and finite prefixes reconstruct cycle means. | The missing theorem is transport from those state moments into the exported velocity and paper tuple. |

## Zero-sorry completion

`NavierStokesReview/src/completions/MeanRankUpdateAudit.lean` compiles with no
`sorry`, `axiom`, or `unsafe`. It proves the coordinate formula for
`scaleDebt`, projects the first two `FiveRows` equations, and constructs a
nonzero debt example satisfying the full five-row predicate.

## Status

This sharpens CTR-005. It rejects the overstatement that the runtime rows
hard-code total mass or energy to zero. The live objection is narrower and
stronger: the source has a genuine internal two-moment correction invariant,
but the selected endpoint does not expose its equality with the paper's five
named moments or with the final mixed velocity field.
