# Priority 89 source review: moment repair, stress algebra, aliases, and physical curl covariance

## Scope

This tranche reviews eleven reachable modules in the reduced-profile, moment-repair, stress, torus-alias, gauge-preservation, and Cartesian-curl layers. The review is source-grounded and records what the declarations establish; it does not infer an endpoint theorem from imports or names.

## Module findings

| Module | What the source establishes | Boundary that remains open |
|---|---|---|
| `JetBounds.lean` | Generic finite/all-order Fréchet jet bounds, derivative/addition/bilinear/multiplication/transport/perturbation estimates, and rate combinators. | These are regularity/rate contracts, not radial moment observables. |
| `LocalizedMomentRepair.lean` | Smooth compactly supported bump repairs, nonsingular generalised-power moment matrices, exact Lebesgue moment identities, support/linearity, and derivative bounds. | Exact reduced repair is not a theorem about the selected Cartesian `Witness`. |
| `MomentRepair.lean` | Abstract finite-dimensional repair synthesis, exact matching, uniqueness, idempotence, support, and contraction-side facts. | The generic repair object is not identified with the final assembled field or five paper observables. |
| `SmoothFamilyTorusInverse.lean` | Smooth parameterised torus families, means, Fourier inverse, zero-mean solvability, support preservation, multiplier bounds, jets, and non-bar decomposition. | No theorem here identifies the public selected field with the five cumulative radial observables. |
| `StressAlgebra.lean` | Angular/axial radial sources and primitives, derivative and integrated identities, lags, logarithmic terms, and stress-free identities under explicit moment/pressure hypotheses. | This is reduced stress calculus; its hypotheses are not shown here to be transported through the complete endpoint assembly. |
| `UniformFourierAlias.lean` | Exact compact transport aliases, source/alias jet bounds, radial-slice and torus-mean identities, real-centred/inverse constructions, support, finite-jet, mean-class, and superflat estimates. | Alias/mean transport is genuine, but no public selected Cartesian five-observable equality is exported. |
| `ZerothStressIdentity.lean` | Leading angular/axial coefficients, weighted stresses, axis regularity, leading density, scheme germs, raw stress identities, and equality of extended stress slots with leading stress. | This is a reduced leading-stress bridge, not final endpoint transport. |
| `AxisHolomorphicJoint.lean` | Joint parameter smoothness, compact-family derivative estimates, real agreement, common extensions, and uniform mean-value remainder control. | Analytic parameter regularity does not provide selected-field radial moment equality. |
| `AxisProfile.lean` | Radial operator/inverse coefficients, low-order profile expansions, coefficient inversion, and leading axial derivative identities. | Local axis algebra is not a global selected-field observable theorem. |
| `GaugeMassPreservation.lean` | Moving-gauge stream identities, torus-average congruence, zero radial moments for temporal increments, angular/axial torus-mean preservation, and local `ZeroMassesOn` preservation on a valid slow region. | This is a genuine local conservation result. It is not a global theorem transporting all five paper observables to `selected_witness`. |
| `PhysicalCurlCovariance.lean` | Cylindrical/Cartesian curl covariance, moving-frame terms, pullback/cutoff identities, scaled-graph curl, Cartesian potential overlap/germ compatibility, global Cartesian potential/velocity smoothness, divergence freedom, axis zero, and constructed-wave curl identities. | This is a strong physical curl bridge, but it does not prove preservation of the five radial observables through the full `tsum`/localisation/periodisation endpoint. |

## Controlled conclusion

This tranche corrects two opposite errors. First, it rules out the claim that the repository contains no real moment, stress, alias, gauge, or Cartesian-curl mathematics. Second, it does not promote these local or reduced theorems into the missing endpoint correspondence theorem.

The evidence now supports the narrower statement:

\[
\text{reduced repair/stress identities}
\;\longrightarrow\;
\text{local mean and curl transport}
\;\not\Rightarrow\;
\text{five-observable equality for the public selected Cartesian field}.
\]

`GaugeMassPreservation` supplies local mass preservation, and `PhysicalCurlCovariance` supplies a substantial geometric lift. Neither declaration, as reviewed here, proves the full composition through infinite stage assembly, spacetime localisation, periodisation, torus averaging, radial pullback, and `ActualCandidateAssembly.Witness`.

No nonzero defect \(\Delta m\), impossibility theorem, or kernel-level `False` is established by this tranche. The correct status remains a selected-path correspondence question until the concrete endpoint composition is either proved or contradicted.

## Register action

The eleven modules are recorded as `evidence_inspected` in `semantic_coverage_register_full_2026-09-27.json` and its Markdown/HTML mirrors after regeneration. Their findings must remain distinct from the unresolved reachable queue.
