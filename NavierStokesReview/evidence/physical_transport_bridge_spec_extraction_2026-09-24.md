# Physical transport bridge specification extraction

**Purpose.** This is an audit specification, not an implementation of a
missing theorem. It records the exact objects that a selected-path bridge would
have to connect before the paper's five-moment narrative could be identified
with the exported endpoint.

## 1. Five positive-order rows

| Object | Source | Exact declaration | Meaning in the source |
|---|---|---|---|
| Positive-order debt | `NavierStokes/PositiveOrderMoments.lean:21-23` | `abbrev Debt := Fin 5 → ℝ` | Five real coordinates. |
| Raw row density | `PositiveOrderMoments.lean:76-80` | `![R * u n R, R ^ 2 * e n R, pressureGradient n e omega R, R ^ 2 * cauchy n u e R, R * cauchy n u u R - R ^ 2 / 2 * pressureGradient n e omega R]` | The five integrands, in source order. |
| Positive integral | `PositiveOrderMoments.lean:82` | `positiveIntegral f := ∫ R in Ioi 0, f R` | Integration over positive radius. |
| Five moments | `PositiveOrderMoments.lean:84-85` | `moments n u e omega := fun i => positiveIntegral (fun R => rowDensity n u e omega R i)` | The actual five-coordinate integral vector. |
| Weighted repair density | `PositiveOrderMoments.lean:107-109` | `![R * du R, R ^ 2 * de R, (2*A)*(R^(-2-2*lam)*de R), A*(R^(1-2*lam)*du R), (-A)*(R^(-2*lam)*de R)]` | The five linearised repair rows. |

The separately named paper-shaped `FiveProfileMoments.Debt` is also
`Fin 5 → ℝ` (`NavierStokes/FiveProfileMoments.lean:260-262`), but its raw
coefficient system is a product `(Fin 2 → ℝ) × (Fin 3 → ℝ)` and its exponent
vectors are `axialPowers b := ![0,b+1/2]` and
`angularPowers b := ![1/2,b,b-1]` (`:273-274`). That is not definitionally the
same object as the positive-order row density above.

## 2. What is actually proved about repair stability

The strongest positive-order repair statements are:

- `rowDensity_increment` (`PositiveOrderMoments.lean:92-105`) proves the
  current-order increment is affine, with no quadratic current-order terms
  when `0 < n`.
- `moments_repair` (`:250-273`) proves one exact affine repair step.
- `moments_repair_target` (`:275-285`) chooses the debt
  `target - moments n u e omega` and reaches the requested target.
- `exists_smooth_exact_repair` (`:287-305`) packages smoothness, support, and
  the target equality.

There is no theorem in `PositiveOrderMoments.lean` named as an induction over
all recursive stages proving that the five coordinates remain invariant across
the entire germ series. The recursive selected construction uses separate
cycle induction theorems, for example `ActualCycleResidualBounds.iterate_base_error`
(`:882-895`) and `ActualCycleCoherence.iterate_coherent` (`:836-849`). The
selected-path bridge would have to connect those cycle invariants to the
positive-order `moments` equality; the inspected source does not expose that
single theorem.

## 3. Runtime three-debt engine and the required promotion

`MeanRankUpdate.Debt` is an abbreviation for `FiveRowRank.Debt`, hence
`Fin 3 → ℝ` (`NavierStokes/MeanRankUpdate.lean:24`). The physical five-row
interface is `FiveRowRank.FiveRows` (`NavierStokes/FiveRowRank.lean:240-246`):
the first two rows are explicit zero integrals and the last three are the three
coordinates of the debt.

The runtime scaling laws are not a `j → j+1` update inside `MeanRankUpdate`.
They are the pointwise scale maps:

```lean
scaleDebt ell U d := ![U ^ 2 * d 0,
  ell ^ 3 * U ^ 2 * d 1,
  ell ^ 2 * U ^ 2 * d 2]
```

from `MeanRankUpdate.lean:29-34`, with `fiveRows_scaled` at `:136-151` and
`physical_five_rows` at `:162-174`. The actual cycle update is in
`CorrectionStep.lean`: `next_mean` (`:5115-5122`) gives
`updated (updated u.mean temporalIncrement) rankIncrement`; the two conserved
radial masses are proved by `next_preserve_masses` (`:5320-5342`).

The exact candidate promotion template is therefore only a proposed audit
object, not an existing source theorem:

```lean
def promoteDebt (d : FiveRowRank.Debt) : PositiveOrderMoments.Debt :=
  ![0, 0, -(d 0), -(d 1), -(d 2)]
```

This map is already tested algebraically in
`NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean:22-50`.
That probe proves equality of the local repair profiles and the five weighted
integrals after promotion. It does not prove that the selected cycle's
`debt c u n` is the paper's `(M,I,J,S,C_p)`, nor that the promoted vector is
transported into `StateRealization.chartIdentity` and the final residual.

## 4. Cartesian contact point

The code does have a concrete local contact:

- `CorrectionStep.normalizedRank_angular`, `normalizedRank_desired`, and
  `normalizedRank_potential` (`:1212-1229`) substitute `debt c u n` into the
  rank profiles.
- `normalizedRank_radial` (`:1231-1245`) carries the same debt into the radial
  rank increment.
- `PhysicalResidualJetBounds.StateRealization.chartIdentity`
  (`:927-966`) reconstructs the Cartesian residual from actual `u` and `P`
  using local germs and `base_equation`.

This is a local residual bridge, not yet a theorem equating the five named
paper moments with the debt used by the Cartesian residual. The missing theorem
must quantify the same fields, the same stage index, the same pressure, and the
same force endpoint. A new bridge file should not be treated as a repair of the
authors' proof unless it is proved from the existing definitions without
introducing a stronger, unproved premise.

## 5. Pressure-chain correction

`PressureRecovery.Hypotheses` (`NavierStokes/R3/PressureRecovery.lean:31-44`)
is a comparison record. `weak_pressure_poisson`
(`NavierStokes/R3/ConservativeDifference.lean:428-469`) and
`pressure_gradient_recovery` (`PressureRecovery.lean:419-438`) concern the
difference `p - q` under equal-residual hypotheses. They do not, by themselves,
assert that the selected pressure has an absolute Poisson representative or a
normalisation.

The zero-sorry probe
`NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean`
constructs these comparison hypotheses with identical zero velocities and an
arbitrary common smooth pressure `p`. Thus the comparison interface cannot be
used as evidence that the selected pressure's global semantics have already
been checked. This is a live audit limitation, not yet a refutation of the
selected endpoint.
