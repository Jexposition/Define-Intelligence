# Priority 63-66 source review: profile bounds, axis geometry, and physical localisation

Date: 2026-09-27
Scope: ten directly inspected reachable source modules.
Method: source-first review of definitions and theorem statements at the cited ranges.

## Executive result

This tranche supplies substantial profile and geometry evidence. It contains
actual covariance determinant/inverse bounds, spatial Taylor-Borel extension,
true-cone speed and variance correction, Bochner transport primitives,
Gaussian support and zero-germ coverage, physical polar-chart identities,
axis-preservation and origin blow-up, natural-axis reference positivity,
implicit heat-coordinate identities, and positive-time signed-mask bounds.

The axis layer is especially important: `AxisPreservation` explicitly proves
local finite-sum collapse near the preterminal axis and isolates the first
potential/curl while stating that no uniform stage radius or final-velocity
estimate is assumed. This is real origin-path infrastructure, not a proof of a
global five-observable equality.

## Module findings

### `PrimaryCovarianceBounds.lean`

Defines the actual normalised-slot covariance and proves compact cone margins,
chart scale bounds, determinant/inverse-weight bounds, and positive primary
weights (`PrimaryCovarianceBounds.lean:30-49, :89-181, :337-389`). It is a
zeroth-order covariance estimate and has no radial moment observable.

### `SpatialBorelExtension.lean`

Constructs spatial bump/localisation terms, jointly smooth Taylor-Borel
templates, compact support, derivative bounds, and a scale/doubling schedule
(`SpatialBorelExtension.lean:29-86, :122-211`). It addresses spatial jet
extension, not field-level radial moment transport.

### `TrueConeLoop.lean`

Builds the actual exponential moment inverse, smooth speed correction,
variance root, compact cone margins, and phase change
(`TrueConeLoop.lean:22-170`). Its moment objects are angular exponential-family
moments inherited from `LoopVariance`, not the final whole-space `barMoment`.

### `TransportPrimitive.lean`

Defines translated compact radial integrals and proves Bochner integrability,
parameter smoothness, support truncation, fixed-interval representations, and
derivative retention (`TransportPrimitive.lean:34-100, :112-245`). This is a
real integral transport primitive, but no selected Cartesian field is supplied
to it and no `(M,I,J,S,C_p)` equality is concluded.

### `ActualGaussianCoverage.lean`

Defines actual Gaussian/clock rates and proves uniform envelopes, compact source
and outer cells, source-cell inclusion, time support, and whole-path zero-germ
properties (`ActualGaussianCoverage.lean:25-109, :129-209`). These results
control support of actual Volterra paths; they do not evaluate selected radial
observables.

### `ActualSignedPhysicalGeometry.lean`

Proves annular coverage, chart existence, positive chart radius, physical chart
membership and scale identities, and mapping into the physical polar domain
(`ActualSignedPhysicalGeometry.lean:25-119, :130-184`). This is concrete
preterminal coordinate geometry, not a global moment bridge.

### `AxisPreservation.lean`

Proves actual wave sums vanish near preterminal axis points and their curls
vanish there (`AxisPreservation.lean:20-60`). It then proves potential-sum
collapse to the first stage, velocity-sum collapse, eventual origin equality,
and origin blow-up consequences (`:64-174`). The header explicitly says no
uniform radius in stage number and no final-velocity estimate are assumed.
This is strong local axis evidence, but not a final five-moment evaluation.

### `AxisReference.lean`

Identifies the natural-axis reference with its leading series, proves derivative
and coefficient identities, positivity, logarithmic-slope margins, and scaled
profile stability (`AxisReference.lean:21-154, :168-275`). The series is a
reference profile construction, not the selected whole-space Cartesian field's
radial observable.

### `PhysicalHeatCoordinates.lean`

Proves the actual implicit physical heat-coordinate identities, normalisation,
heat carrier equivalence, and the `q`, `eta`, and `X` normalised-section
formulas (`PhysicalHeatCoordinates.lean:20-111`). These are coordinate/profile
identities for the heat edit and do not export a global field moment theorem.

### `PositiveTimeSignedLocalization.lean`

Defines positive-native-time mask/radius conditions and proves normalised-radius
bounds and mask pullback properties (`PositiveTimeSignedLocalization.lean:25-108`).
Its header explicitly states that no support assertion is made outside the
positive-time domain. No endpoint moment equality is present.

## Cross-layer disposition

| Question | Source-grounded answer |
|---|---|
| Is the axis/origin construction substantive? | Yes. Local finite-sum collapse, curl vanishing, and origin blow-up are explicitly proved under stated hypotheses. |
| Are Gaussian, polar, heat-coordinate, and covariance bounds real? | Yes. |
| Do these results identify the final field's five paper observables? | No. |
| Does the axis theorem itself prove a nonzero moment defect? | No. |
| Does this tranche prove impossibility or `False`? | No. |

## Controlled conclusion

The positive result is not merely “some profiles exist”: the source records
actual local field geometry, axis behaviour, support and Gaussian coverage, and
profile bounds. The unresolved boundary remains the composition from these
local objects to the final selected Cartesian field and its global radial
moment engine. No claim stronger than that is recorded.
