# Load-bearing semantic audit

Date: 2026-09-22  
Source commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`  
Review scope: whole-space R3 route, pressure recovery, comparison closure,
viscosity scaling, force bridge, and endpoint-rate filters.

## Findings

1. **Pressure is not simply assumed away in the inspected R3 path.**
   `PressureRecovery.Hypotheses` receives the residual equation, divergence,
   smoothness, positivity, and uniform finite-energy hypotheses. The proof
   constructs the pressure-gradient distribution, then removes the harmonic
   remainder using the compact-harmonic Fourier argument in
   `HarmonicTestFunctionals`. `ActualPressureFlux` consumes that recovered
   gradient and derives the pressure-flux bound used by comparison closure.

2. **The comparison closure has an explicit analytic interface.**
   `WholeSpaceComparisonClosure.eq_of_pressure_flux_bound` and
   `WholeSpaceEnergyLimit.eq_zero_of_radius_bound` require pressure-flux and
   energy-radius estimates. The source path inspected here derives the former
   from the comparison equations rather than adding global agreement as a
   premise. This is positive source evidence, not independent validation of
   every imported analytic lemma.

3. **The inspected viscosity scaling preserves the stated equation.**
   `ViscosityScaling.rescale_residual` rescales velocity amplitude and space,
   changes viscosity by the square of the amplitude, and leaves time fixed.
   `candidate_at_viscosity` chooses the positive square root of the target
   viscosity. The reviewed equations preserve the classical Laplacian and
   convection signs at this interface. No scaling mismatch was found in this
   pass.

4. **The force bridge matches the forced CMI alternative at the predicate
   level.** `ComparatorBridge.forceConditionDecay_of_compact` derives the
   required mixed derivative decay and future-time support from the compact,
   smooth force. This does not settle whether the constructed force is an
   acceptable mathematical witness until the construction premises receive
   independent PDE review.

5. **The generic rate API has a real but currently non-route-breaking
   weakness.** `DiagonalResidual.JetRate` has no `NeBot` premise, so it is
   vacuous on `⊥`. The selected exact open-past endpoint is separately proved
   `NeBot` by `OpenPastNeBotProbe`. Derived intersections remain unproved as
   nontrivial filters, but the selected residual theorem uses a two-branch
   eventual argument, so this observation alone does not refute the exported
   theorem.

## CMI disposition

This lane found no concrete code-level mismatch with the CMI PDE, force,
energy, or whole-space quantifier interface. It did find one reusable
specification-quality issue, `JetRate`'s arbitrary-filter vacuity, and narrowed
its impact by proving the actual open-past endpoint nontrivial. The unresolved
work is analytic provenance and common-domain coverage, not compilation.

## Source anchors

- `NavierStokes/R3/PressureRecovery.lean:33-44,272-305`
- `NavierStokes/R3/HarmonicTestFunctionals.lean:29-110`
- `NavierStokes/R3/ActualPressureFlux.lean`
- `NavierStokes/R3/WholeSpaceComparisonClosure.lean`
- `NavierStokes/R3/WholeSpaceEnergyLimit.lean:25-85`
- `NavierStokes/R3/ViscosityScaling.lean:118-185`
- `NavierStokes/R3/ComparatorBridge.lean:22-88`
- `NavierStokes/DiagonalResidual.lean:33-35`
- `NavierStokes/SpacetimeEndpoint.lean:24-25`
