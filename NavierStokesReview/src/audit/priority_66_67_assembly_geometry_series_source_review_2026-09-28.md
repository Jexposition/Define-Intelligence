# Source review: primary field assembly, comparison, harmonic interaction, cycle geometry, polar coverage, and axis series

Date: 2026-09-28

This tranche records direct inspection of the next six highest-priority reachable modules. It expands the map of real upstream assembly and analytical machinery without treating reachability as endpoint transport.

## PrimaryFieldAssembly.lean

`PrimaryFieldAssembly.lean` contains finite periodised vector-mode and principal-field construction. It proves compact-support and periodisation identities (60--174), finite principal-field decompositions and component formulas (210--298), corrected-field and covariance expansions (395--478), source/amplitude/velocity identifications (525--702), finite corrected-field and periodic coverage results (723--873), continuity and outer-scale identities (897--1013), and scaled corrected-field decompositions (1037--1081).

Finding: this is genuine Cartesian/periodised field assembly with covariance and torus-average results. The inspected declarations do not identify the final selected field with `(M,I,J,S,Cp)`.

## R3/ComparisonGronwall.lean

`R3/ComparisonGronwall.lean` proves derivative-based exponential comparison bounds (24--118), uniform radius estimates, and zero-from-large-radius consequences (119--163).

Finding: real comparison analysis is present. It is not an endpoint moment-transport theorem.

## UniformHarmonicInteraction.lean

`UniformHarmonicInteraction.lean` establishes uniform harmonic wave bounds, complex scalar multiplication and radius division, stripped transport and divergence estimates, ordered-kernel cancellation, block-amplitude bounds, uniform transport/mixed/square/nonlinear coefficient bounds, and interaction-block structure (28--98, 172--245, 271--376, 420--434).

Finding: this is substantive harmonic interaction and coefficient control. No inspected declaration exports the final global five-observable equality.

## ActualCycleGeometry.lean

`ActualCycleGeometry.lean` identifies actual cycle similarity data with the initialization strip, gauge, region, patch radii, index, slow scale, and temporal operators (18--81). It proves operator compatibility, base bounds, positive radius, and positive strip time (81--111).

Finding: this closes concrete geometry and parameter aliases for the actual cycle. It does not transport radial moments through the assembled selected field.

## ActualPolarCoverage.lean

`ActualPolarCoverage.lean` imports physical residual jet bounds and actual initialisation, then defines the actual physical polar coverage domain and proves inner-radius positivity and coverage/chart conditions (21--298). The coverage layer remains geometric and jet-oriented.

Finding: it supplies axis-aware physical chart coverage, not a global `(M,I,J,S,Cp)` transport theorem.

## AxisSeries.lean

`AxisSeries.lean` defines the Bessel-like axis series and proves summability/tail identities, derivative and ODE identities, profile reconstruction, tail monotonicity and nonnegativity, lower bounds, positivity, and logarithmic-slope estimates (56--210, 220--315, 329--385).

Finding: this is explicit scalar axis-series/profile analysis. It does not establish that the final 3D Cartesian field preserves the paper-level moment tuple.

## Tranche classification

| Module | Directly evidenced | Not established by this tranche |
|---|---|---|
| `PrimaryFieldAssembly.lean` | Periodised vector fields, source identities, covariance, torus averages | Final five-moment field equality |
| `R3/ComparisonGronwall.lean` | Comparison/radius bounds | Selected endpoint transport |
| `UniformHarmonicInteraction.lean` | Uniform harmonic and nonlinear interaction bounds | Paper-to-endpoint moment correspondence |
| `ActualCycleGeometry.lean` | Actual geometry and positive-radius identities | Global radial observables |
| `ActualPolarCoverage.lean` | Axis-aware polar coverage and jet domains | On-axis/global moment bridge |
| `AxisSeries.lean` | Scalar series, ODE, tails, positivity, slope | Final Cartesian five-observable equality |

The result is a stronger, more granular architecture map: real field assembly and scalar/profile analysis are present upstream, while the exact selected-field global transport question remains open until a declaration with that value-level conclusion is found or disproved by a source-complete search.
