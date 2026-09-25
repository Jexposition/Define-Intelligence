# Selected direct-stage moment transport

Date: 2026-09-25

## Result

`NavierStokesReview/src/completions/SelectedDirectStageMomentTransport.lean`
compiles with no `sorry`, `axiom`, or `unsafe` declaration. The command

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

completed successfully with 3703 jobs.

The theorem
`SelectedDirectStageMomentTransport.selected_angular_native_stage_moment_zero`
proves, for every selected native angular stage `j`, radial index `n`, and
point `s` in the selected region,

```text
barMoment 2 (angularNativeStages selectedBudget selectedThreshold j) n s = 0
```

This is an actual stage-level result. It is not a claim about the final mixed
Cartesian velocity and it does not prove `Delta m ≠ 0` or `False`.

## Source path

| Component | Source | Role |
|---|---|---|
| Stage definition | `NavierStokes/ActualCandidateConstruction.lean:392-394` | Stage 0 is the current mean angular field; successor stages are consecutive state differences. |
| Selected cycle invariant | `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean:20-30` | Every selected cycle state has `ZeroMassesOn`; its angular moment of order 2 is zero. |
| Primitive regularity | `NavierStokes/CorrectionStep.lean:9446-9448` and `NavierStokes/MeanStateRegularity.lean:339-347` | The analytic invariant exports `primitives`; `PrimitiveData.mean` is a `MovingTriple`. |
| Regularity conversion | `NavierStokes/MeanStateRegularity.lean:228-246` | `MovingTriple.regular` supplies the smooth/support data required for moment subtraction. |
| Moment subtraction | `NavierStokes/GaugeDebtIncrement.lean:175-179` | `radialMoment_sub_on` transports the integral through a state difference. |
| New completion | `NavierStokesReview/src/completions/SelectedDirectStageMomentTransport.lean:31-62` | Cases on stage index, applies state zero moments, and closes the difference by arithmetic. |

## Audit consequence

The direct scalar angular branch is not the source of a selected nonzero
order-2 radial remainder. The remaining `CTR-005` calculation must therefore
target the potential/curl branch, the Cartesian-to-radial transport, the
localisation and torus-average boundary terms, or a mismatch between those
objects and the scalar stage profile. This result narrows the live route; it
does not clear the paper-to-endpoint correspondence burden.
