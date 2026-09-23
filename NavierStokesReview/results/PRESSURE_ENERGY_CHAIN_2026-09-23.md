# Pressure and localized-energy chain audit

Snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

This record separates the final uniqueness theorem's explicit premises from the lower-level estimates that discharge them.

## Source chain

1. `NavierStokes/R3/WholeSpaceUniqueness.lean:28-68` receives smooth velocities and pressures, divergence-free equations, equality of residuals, zero initial data, compact support for the reference velocity, and uniform finite energy for the competitor.
2. It builds `PressureRecovery.Hypotheses` and obtains uniform bounds for the difference in `L²`, the reference velocity in `L³`, and the tensor difference in `L¹`.
3. `NavierStokes/R3/PressureFlux.lean:576-604` uses those bounds with pressure recovery to produce one pressure-flux bound uniform in time and cutoff radius.
4. `NavierStokes/R3/WholeSpaceComparisonClosure.lean:32-157` derives the localized difference-energy balance, estimates the transport, Laplacian, Sobolev, and pressure terms, and applies `ComparisonRateBound.exists_uniform_rate_bound`.
5. `NavierStokes/R3/WholeSpaceEnergyLimit.lean:57-69` consumes the resulting rate estimate to prove that the difference vanishes.

## Review result

The final `hrate` is an explicit premise of the scalar limit theorem, but it is not merely postulated at the whole-space uniqueness entry point. The closure constructs it from the balance and pressure-flux estimates. The supplied review drafts therefore overstate the source when they say that the energy identity is independently verified simply because the repository compiles, but the present inspection has not established a missing theorem in this chain.

The remaining load-bearing audit is semantic and analytic: verify that the `GlobalFiniteEnergySolution` and `PressureRecovery.Hypotheses` interfaces impose all regularity, integrability, and equation conditions required by the imported pressure and integration results. A theorem can be kernel-checked while still proving only the proposition represented by an overly weak interface.

## Not established by this chain

- It does not make the force independent of the candidate velocity.
- It does not turn the forced construction into an unforced A/B result.
- It does not validate the absent draft paths `Forcing/Smoothness.lean`, `Pressure/LerayProjection.lean`, `Scaling/SingularLimits.lean`, or `EnergyDefect.lean`.
- It does not establish nonlinear-regularisation stability or a hypo-dissipative result.
