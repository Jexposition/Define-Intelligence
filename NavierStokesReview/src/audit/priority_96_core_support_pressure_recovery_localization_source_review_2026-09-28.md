# Priority-96 Source Review: Core Support, Time Localization, and Comparative Pressure Recovery

Date: 2026-09-28

This review records direct source inspection of the next reachable queue. It separates concrete intermediate construction from endpoint semantic transport. No nonzero defect, impossibility theorem, or kernel-level `False` is inferred merely from an omitted theorem.

## Scope

Reviewed the following source files:

- `NavierStokes/ActualCoreSupport.lean`
- `NavierStokes/ActualSignedUnmaskedBinding.lean`
- `NavierStokes/ActualSignedUnmaskedBounds.lean`
- `NavierStokes/AxisTailRegularity.lean`
- `NavierStokes/GaugeExcludedBounds.lean`
- `NavierStokes/GermEndpointInputs.lean`
- `NavierStokes/HeatSwitchHistoryDerivatives.lean`
- `NavierStokes/MixedDiagonalSchedule.lean`
- `NavierStokes/OffplaneJetExtensions.lean`
- `NavierStokes/OscillatoryCurl.lean`
- `NavierStokes/PhysicalStageSupport.lean`
- `NavierStokes/R3/ConservativeDifference.lean`
- `NavierStokes/R3/PressureFluxTest.lean`
- `NavierStokes/R3/PressureRecovery.lean`
- `NavierStokes/R3/RieszTestOperators.lean`
- `NavierStokes/SchedulePressure.lean`
- `NavierStokes/TailCone.lean`
- `NavierStokes/TimeLocalization.lean`
- `NavierStokes/UniformBlockBounds.lean`

## Direct source findings

### Core, support, and rate layers

`ActualCoreSupport.lean` defines the concrete radial/core carrier used by actual initialisation and proves carrier closure, containment, nonnegative time, continuity, fast bounds, support, zero germs, primary velocity/pressure zero facts, Gaussian support, initial support, and an invariant. This is genuine support geometry. It is not a theorem that the completed Cartesian field has the paper's five radial observables.

`ActualSignedUnmaskedBinding.lean`, `ActualSignedUnmaskedBounds.lean`, `MixedDiagonalSchedule.lean`, `PhysicalStageSupport.lean`, `GermEndpointInputs.lean`, `AxisTailRegularity.lean`, `GaugeExcludedBounds.lean`, `OffplaneJetExtensions.lean`, `OscillatoryCurl.lean`, and `HeatSwitchHistoryDerivatives.lean` provide binding, grid-mask, schedule, support, germ, axis, gauge, off-plane jet, oscillatory-curl, and switched-history estimates. These modules demonstrate substantial intermediate infrastructure. Their reviewed declarations expose rate/support/regularity contracts, not an equality of the final field with `(M, I, J, S, C_p)`.

`UniformBlockBounds.lean` proves uniform reindexing, slicing, pairing, signed/product block, native assembly, and state-reindex bounds for coefficient and pressure/amplitude blocks. Uniform bounds are not value-level radial-moment transport.

`TailCone.lean` supplies reduced tail/cone and release estimates, including angular suppression, energy/mass ratios, and future bounds. These remain upstream asymptotic controls.

### Time localization

`TimeLocalization.lean` defines:

```lean
def activatedVelocity (u : VelocityField) : VelocityField :=
  fun z => timeSwitch z.1 • u z

def activatedPressure (p : PressureField) : PressureField :=
  fun z => timeSwitch z.1 * p z
```

The file proves smoothness, periodicity, zero initial data, divergence preservation, late-time equality, and speed-unboundedness preservation. Its central residual theorem is:

```lean
navierStokesResidual (activatedVelocity u) (activatedPressure p) t x =
  timeSwitch t • navierStokesResidual u p t x + deriv timeSwitch t • u (t, x) +
    (timeSwitch t * timeSwitch t - timeSwitch t) • advection u t x
```

This is a precise switched-residual identity. It confirms that the activation layer has nontrivial residual terms away from the late-time region. The file does not define or transport the five cumulative radial moments.

### Comparative pressure and weak PDE layer

`R3/ConservativeDifference.lean` derives the conservative difference equation, integration-by-parts identities, weak pressure-gradient identities, and `weak_pressure_poisson`. The latter has the comparative form:

```lean
∫ x, (p - q) (t, x) * scalarLaplacian ψ x =
  -(∑ k : Fin 3, ∑ i : Fin 3,
    ∫ x, tensorDiff u v t k i x * spatialPartial i (spatialPartial k ψ) x)
```

The hypotheses compare `u` with `v`, `p` with `q`, and require equal residuals. The test `ψ` is compactly supported. This is not an absolute global Poisson representation for `p` alone.

`R3/PressureRecovery.lean` makes the scope explicit in `structure Hypotheses`: it quantifies two velocities and two pressures and assumes equality of their residuals. `gradient_recovery` and `pressure_gradient_recovery` recover the gradient of `p - q` against compact tests. This is a valid comparative pressure result, not selected-witness absolute pressure semantics.

`R3/PressureFluxTest.lean` constructs compact pressure-flux test functions and proves smoothness, support, Lp, derivative, and cutoff-flux bounds. `R3/RieszTestOperators.lean` supplies Riesz test regularity, Lp/Sobolev estimates, and Laplacian identities. Both are analytic test infrastructure.

`SchedulePressure.lean` defines reduced `axisPressure` from the outgoing angular schedule and proves smoothness, sign, derivative, integrability, and natural-axis facts. This is reduced schedule pressure rather than an absolute whole-space pressure representative.

## Controlled correspondence result

This tranche strengthens the audit in two directions:

1. The repository contains real support, switching, weak-PDE, pressure-comparison, Riesz, and reduced-pressure mathematics.
2. The reviewed declarations still do not prove the missing value-level composition

   `selected Cartesian field -> torus/radial observable -> (M, I, J, S, C_p)`.

The time-switch theorem and pressure-recovery theorems must not be misreported. The former proves a concrete residual formula; the latter proves comparative pressure recovery. Neither is a selected-field five-moment transport theorem.

## Status

- `CTR-005`: remains **not established** at the selected-field correspondence boundary. This is a source-backed transport gap, not a claimed nonzero defect.
- `CTR-012`: the time-localization residual identity is direct evidence about the switched construction; it does not by itself impose a formal force-independence predicate.
- `AX-029/AX-030`: comparative pressure recovery is confirmed; absolute selected-pressure Poisson semantics remain unestablished in the inspected path.
- `FORMALLY REFUTED`: not triggered. No concrete `Δm ≠ 0`, impossibility theorem, or kernel `False` was proved by this tranche.

## Register action

The 19 path-qualified evidence records from this review are added to `semantic_coverage_register.py`. The JSON, Markdown, and HTML registers must be regenerated from `hardened_source_map_2026-09-27.json`, then copied to the public `docs/` mirrors. Counts and the remaining reachable queue must be recorded in the current plan and goal documents.
