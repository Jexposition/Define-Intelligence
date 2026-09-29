# Priority 113 source review: heated outgoing profiles, mode reindexing, and shaped waits

Date: 2026-09-28
Scope: direct source review of three reachable modules in `NavierStokes/`.

## `NavierStokes/HeatedOutgoing.lean`

This module defines the physical-band outgoing heat profile, compensation patch, reduced pressure kernel, energy density, and reduced moment functions. It proves smoothness, support and positivity, heat/patch decompositions, integrability, and exact three-row compensation cancellation. It also packages a reduced `Specification` with pressure-canonical, energy, mass, angular, and renormalised identities.

Evidence anchors: lines 1–56, 57–162, 167–286, 300–390, 472–508, and 793–862.

Boundary: these are genuine reduced-profile moment and pressure results in `(X, eta)` variables. The reviewed declarations do not identify the final selected Cartesian field with a global `barMoment` tuple.

## `NavierStokes/ModeSolenoidalReindex.lean`

This module proves linear-equivalence pullback identities for harmonic amplitudes, single modes, lift and angular directions, cylindrical divergence, and the `ModeSolenoidal` property. It is a real mode-level geometry bridge: reindexing preserves the stated cylindrical divergence-free structure.

Evidence anchors: lines 1–20, 22–63, and 92–97.

Boundary: the result is local mode/reindex transport. It is not a theorem about the assembled global `tsum`, spatial localisation, torus/radial averaging, or the selected five-observable endpoint.

## `NavierStokes/ShapedWaitBounds.lean`

This module proves shaped temporal hold/wait formulas and bounds for pressure sources, axial and angular lag, initial energy and axial constants, derivative control, smoothness, and exponential-to-power decay. It provides temporal/reduced estimate infrastructure used to make the profile schedule quantitatively small.

Evidence anchors: lines 1–43, 45–168, 188–313, 354–423, 432–575, 582–800, 839–915, 980–1038, 1072–1304.

Boundary: no Cartesian curl, `barMoment`, five-observable tuple, or endpoint packaging theorem is present in the reviewed declarations.

## Cross-module result

The tranche adds positive intermediate evidence in three distinct layers: reduced outgoing compensation, local mode geometry, and temporal smallness. It does not resolve the final selected-field composition. No nonzero defect, impossibility theorem, or kernel `False` is inferred.
