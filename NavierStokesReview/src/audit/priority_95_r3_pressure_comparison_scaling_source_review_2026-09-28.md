# Priority 95 source review: R3 pressure comparison, scaling, and Fourier infrastructure

Date: 2026-09-28

This tranche directly reviews the priority-106 R3 pressure/comparison modules and two adjacent scaling/projection modules. The review is source-based and declaration-level. It records positive mathematical content without treating imported support as endpoint transport.

## Files and findings

| File | Direct source finding | Correspondence boundary |
|---|---|---|
| `NavierStokes/NormalScaling.lean` | Proves tangent-projection and projected-RHS rescaling identities, pressure-coefficient rescaling, and projected-operator rescaling in a finite-dimensional inner-product setting. | Algebraic normal/tangent scaling; no selected field or radial observable. |
| `NavierStokes/R3/ActualPressureFlux.lean` | For comparison hypotheses, proves smoothness and integrability of the pressure-difference flux against a compact cutoff and identifies it with a canonical Riesz pairing. The theorem quantifies over `(u,v,p,q)` and uses `p-q`. | Relative comparison only; no absolute selected-pressure representative. |
| `NavierStokes/R3/ComparisonFourierSetup.lean` | Defines Schwartz complex tests, the Riesz symbol, Riesz test operator, pressure pairing, and Fourier H-norm. | Fourier test vocabulary; no candidate endpoint transport. |
| `NavierStokes/R3/LocalizedTransport.lean` | Proves divergence, derivative integration, transport, and pressure integration identities for compactly weighted difference fields. | Localized difference-energy calculus; not a global pressure-Poisson realization. |
| `NavierStokes/R3/PressureFluxIdentity.lean` | Builds smooth compactly supported cutoff-gradient flux functions, weighted components, canonical pressure linear functionals, and the gradient-identification flux identity. | The compact support belongs to the test/cutoff; the result remains comparative and weakly tested. |
| `NavierStokes/R3/PressureFunctionals.lean` | Defines time-averaged pressure-difference functionals from velocity and tensor coefficients, proves integrability and Fourier-H3 bounds, and exposes a complex-linear pairing. | A bounded functional on compact/Schwartz tests, not an absolute pressure field or selected Cartesian moment theorem. |
| `NavierStokes/R3/PressureRecoveryHelpers.lean` | Defines compact real tests and proves the differentiated pressure-Poisson comparison identity against compact tests. The declaration `gradient_poisson_test` explicitly has `p - q`, `u-v`, equal residual hypotheses, and compact test support. | Direct evidence for relative weak pressure recovery; it does not recover `p` alone on all of `R^3`. |
| `NavierStokes/R3/PressureTemporalIdentity.lean` | Proves temporal integration by parts and pressure-gradient identities against compact spatial and temporal tests supported in the interior time interval. | Distributional/weak comparison identity; no absolute endpoint pressure semantics. |
| `NavierStokes/R3/RieszHeatRepresentation.lean` | Defines heat-weighted second-order Fourier symbols and proves integrability and the integral representation of Riesz tests. | Analytic representation layer; no selected-field moment evaluation. |
| `NavierStokes/R3/RieszL2Bounds.lean` | Proves L2 pairing, `MemLp 2`, and integral-square bounds for Riesz test operators. | Functional estimates only. |
| `NavierStokes/R3/RieszLinearityDecay.lean` | Proves additivity, scalar linearity, finite-sum linearity, and Riemann-Lebesgue decay of Riesz tests. | Test-operator regularity/decay only. |
| `NavierStokes/R3/RieszPairing.lean` | Proves integrability, Fourier pairing, conjugate pairing, and self-adjointness identities for Riesz test operators. | Weak Fourier comparison layer; no absolute pressure representative. |
| `NavierStokes/R3/RieszSymbolRegularity.lean` | Proves boundedness/measurability/integrability and smoothness of Riesz multipliers and tests. | Symbol regularity, not physical-field transport. |
| `NavierStokes/R3/SmoothSobolevL6.lean` | Proves cutoff derivative bounds, Sobolev `L^6` estimates, and smooth `MemLp 6` consequences. | Functional regularity and estimates; no radial moments. |
| `NavierStokes/R3/ViscosityScaling.lean` | Defines velocity/pressure rescaling, proves derivatives, divergence, advection, gradient, Laplacian, residual, speed-unboundedness, candidate, and global-solution scaling identities. | Genuine PDE scaling layer; it transports residual/candidate predicates under scaling, not the five paper observables. |
| `NavierStokes/R3/WholeSpaceComparisonClosure.lean` | `eq_of_pressure_flux_bound` combines compact weighted estimates and a pressure-flux bound to prove equality of two solutions on a closed pre-singular slab. The hypotheses explicitly compare `u,v,p,q` under equal residuals. | Strong relative uniqueness/comparison consequence; not an absolute pressure or moment theorem. |
| `NavierStokes/ScalarParticularSupport.lean` | Defines scalar particular copy data/cells and proves cutoff support, a native-zero alternative, and zero germs. | Support bookkeeping; no selected endpoint transport. |
| `NavierStokes/TangentProjection.lean` | Proves algebraic tangent projection, idempotence, projected balance, pressure cancellation, differentiated tangency, preservation, and coefficient sign facts. | Finite-dimensional constraint algebra; no global field realization. |

## Load-bearing source excerpts

`PressureRecoveryHelpers.gradient_poisson_test` has the comparison form

```lean
(∫ x, spatialPartial k (fun y => (p - q) (t, y)) x * scalarLaplacian ψ x) =
  ∑ i : Fin 3, ∑ j : Fin 3,
    ∫ x, tensorDiff u v t i j x *
      spatialPartial i (spatialPartial j (spatialPartial k ψ)) x
```

with equal-residual and compact-test hypotheses. `ActualPressureFlux.pressure_flux_eq_canonical` then identifies the corresponding compact cutoff flux with a canonical Riesz pairing of `tensorDiff u v`. `WholeSpaceComparisonClosure.eq_of_pressure_flux_bound` concludes `u = v` after assuming a pressure-difference flux bound. These are valid relative comparison statements.

They do not establish any declaration of the form

```text
selected_pressure = global_Poisson(u_selected, f_selected)
```

nor do they establish

```text
barMoment(selected_cartesian_field) = (M, I, J, S, C_p).
```

## Controlled conclusion

This tranche corrects two possible overclaims in opposite directions. It rules out saying that the repository lacks pressure recovery, Riesz analysis, whole-space comparison, or viscosity scaling. It also rules out calling these modules an absolute selected-pressure theorem. The source proves substantial weak/comparative pressure machinery, with compact tests, differences, and equal-residual hypotheses. The five-moment selected-field transport question remains open at this tranche; no nonzero defect, impossibility theorem, or kernel-level `False` is asserted.

