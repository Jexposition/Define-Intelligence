# Source review: residual stability, copies, time extension, axis geometry, graphs, and primary pulses

Date: 2026-09-28

This tranche records direct source inspection of six reachable modules. It is an evidence update, not a completeness claim and not a proof that the selected field has a nonzero moment defect.

## ResidualStability.lean

`ResidualStability.lean` contains substantive nonlinear residual algebra. The theorem `residual_add_sub_on` (lines 355--373) expands the residual of `(u+w,p+r)` relative to `(u,p)` into the temporal derivative, Laplacian, pressure-gradient, and cross-advection terms. `residualDifference` and `allJetsFlat_residualDifference` (375--389) transfer all-jets flatness from a smooth perturbation to the residual difference. `residualJetExpression` and `residualDifference_eq_jetExpression` (573--610) expose the exact local jet expression and quantitative derivative bounds. `scaleFilter` and `residualDifference_flat_at_scale` (687--712) establish scale-level flatness under the stated positivity, growth, and flatness hypotheses.

Finding: this is real residual-stability and flatness machinery. It does not state or prove that the final selected Cartesian field transports `(M,I,J,S,Cp)`.

## ParticularCopyBounds.lean

`ParticularCopyBounds.lean` defines `ModalControl` (28--71), including neighbourhood, cell, interval, bridge, smoothness, slot, rate, envelope, error-rate, energy, and input-jet controls. The finite-copy smoothness and local-jet interface appears at 82--100. Pressure coefficients and projected pressure are handled at 185--228, with coefficient and pressure jet bounds at 244--279. The later deck declarations provide copy, velocity, pressure, coefficient, source, synthesis, and forcing jet controls (563--660).

Finding: the module supplies genuine finite-stage modal and localised jet control. The inspected declarations do not export a final-field equality for the five paper observables.

## PastExtension.lean

`PastExtension.lean` constructs zero-before-time velocity and pressure extensions (112--153), then proves zero-germ, negative-time, periodicity, eventual equality, late equality, divergence-free preservation, and preservation of speed unboundedness (155--208). It defines the corresponding past residual and proves smoothness, periodicity, zero past, nonnegative-time equality, and late equality (217--264). The derivative recurrence and locally uniform endpoint-limit transfer are recorded at 266--334.

Finding: this is a real time-extension and endpoint adapter. It does not contain radial-moment transport.

## LocalAxisymmetricResidual.lean

`LocalAxisymmetricResidual.lean` derives local Cartesian derivatives of the axisymmetric velocity, advection, divergence, spatial Laplacian, pressure gradient, and temporal derivative (228--343). `navierStokesResidual_velocity` (345--368) gives the exact local viscosity-one residual in terms of radial, angular, and axial profile components; subsequent declarations derive the local zero-residual consequence under profile equations.

Finding: the local axisymmetric PDE correspondence is substantive. It is not a global integration theorem and does not establish the final five-observable transport bridge.

## PhysicalGraphBounds.lean

`PhysicalGraphBounds.lean` defines the native graph, scaled radial variables, and normalisation identities (113--160), together with compact axis-free annular geometry (161--176). The declarations at 298--318 establish differentiability, nonzero-radius conditions, and uniform dyadic-band native-graph jet bounds. Later sections provide physical chart/lift maps and bounds (388 onward, 1017 onward, and 1398 onward), with explicit positive-radius/axis-free hypotheses.

Finding: this is concrete physical graph and chart geometry. The axis exclusion and jet estimates do not imply global preservation of radial moments.

## PrimaryPulseBounds.lean

`PrimaryPulseBounds.lean` gives an exact primary curl-remainder wave class and cumulative budget (992--1026), local radial and tangential profiles and cutoff identities (1699--1739), phase-chart and curl-remainder bounds (1750--1795), and the canonical primary path/pulse with profile, integrand, covariance, and off-slot identities (1828--1947). The uncut normalised pulse and its projected equation appear at 1955--2025.

Finding: this module contains substantive pulse, curl, profile, and covariance mathematics. The inspected declarations do not transport the final activated Cartesian field to `(M,I,J,S,Cp)`.

## Cross-module audit classification

| Module | What is established | What remains unestablished |
|---|---|---|
| `ResidualStability.lean` | Residual difference identities, flatness, and jet bounds | Selected-field global moment transport |
| `ParticularCopyBounds.lean` | Finite-copy modal, pressure, and jet decks | Endpoint five-observable equality |
| `PastExtension.lean` | Smooth past extension and endpoint residual adapter | Radial-moment transport through extension |
| `LocalAxisymmetricResidual.lean` | Local Cartesian/profile residual identity | Global integration and selected endpoint bridge |
| `PhysicalGraphBounds.lean` | Axis-free chart and native graph bounds | On-axis/global moment correspondence |
| `PrimaryPulseBounds.lean` | Local pulse/curl/profile/covariance identities | Final Cartesian `(M,I,J,S,Cp)` transport |

The six modules strengthen the evidence that the repository contains substantial local PDE, geometry, jet, and pulse machinery. They do not close the endpoint correspondence question and do not justify a nonzero-defect or kernel-`False` claim.
