# Remaining priority-72 tranche: cutoff jets, Volterra sums, wave sums, loops, tails, and interactions

**Date:** 2026-09-28
**Scope:** six reachable Lean modules selected from the regenerated semantic-coverage queue.
**Method:** direct declaration-level source inspection.  The findings below do not infer endpoint meaning from filenames or imports.

## Result

This tranche confirms several genuine mechanisms that matter to the paper-to-code audit: literal transported cutoffs, analytic Volterra series, locally finite physical wave sums, angular mean/variance identities, outgoing-energy integrals, and exact support-separated curl-interaction cancellations.  None of the inspected modules states the complete selected Cartesian equality for the five paper observables `(M,I,J,S,C_p)` after the full selected assembly.

The correct classification is therefore **partial upstream or intermediate evidence, with final endpoint transport still unresolved**.  This tranche does not prove `Delta m != 0`, does not prove that transport is impossible, and does not derive Lean `False`.

## Module findings

### `NativeCutoffJets.lean`

The module defines the literal transported native cutoff, proves equality with the reference transport on the analytic patch, core membership, Gaussian-germ behaviour, and uniform local iterated-jet bounds.  This is a local cutoff-jet result.  It does not define a global radial moment functional or show that the selected five observables survive cutoff transport.

**Anchors:** lines 27–39, 51–82, 92–105.

### `NilpotentVolterra.lean`

The module defines weighted means, regular primitives, their continuity, derivative equations, path inverses, coefficient actions, holomorphic path words, analytic layers, locally bounded solution layers, and a `solutionSeries` with summability/derivative/specification theorems.  It also constructs regular solutions and uniqueness statements for the Volterra system.  This is real infinite-series analytic infrastructure, but its observables are path/coefficient fields; no selected Cartesian `barMoment`/`torusAverage` transport theorem is stated.

**Anchors:** lines 36–163, 173–237, 474–708, 796–905, 915–1058.

### `PhysicalWaveSum.lean`

The module constructs physical chart lifts, carrier data, supported dyadic/slow masks, locally finite masked sums, smooth global waves, support geometry, jet bounds, and vector sums.  It contains explicit local-finiteness and finite-sum identities and proves several realised-curl/support facts through the imported wave construction.  These results are materially stronger than a generic rate interface, but they remain local/support and jet statements.  The inspected source does not identify the resulting global physical sum with the paper’s five cumulative radial observables.

**Anchors:** lines 152–187, 227–378, 470–559, 585–720, 731–796, 825–976.

### `SmoothLoop.lean`

The module defines an actual angular mean, proves cosine and exponential tilt mean/variance identities, projection/stress inequalities, smooth periodic families, rephasing identities, and positive circle-density constructions.  It is genuine angular-moment machinery, and it corrects any claim that the code has no moment calculations.  The inspected moments are angular loop quantities, not a theorem transporting the five paper radial quantities through the selected Cartesian `tsum`/localisation/periodisation pipeline.

**Anchors:** lines 31–117, 127–222, 230–350, 360–590.

### `TailEnergyBounds.lean`

The module defines tail energy density and proves positivity, continuity, release/plateau bounds, integrability, split formulas, post-pulse energy bounds, smoothness, and parameter derivative estimates.  This is substantive energy control for the outgoing tail.  It does not provide a five-observable radial moment equality or connect the tail energy integrals to the selected `Witness` boundary.

**Anchors:** lines 22–120, 140–262, 271–410, 424–510, 512–707.

### `WaveInteractionBounds.lean`

The module proves algebraic wave-class closure, mean/wave products, transport-class bounds, harmonic ratios, finite wave sums, support-separated products, exact curl-interaction zero results, Cartesian transport components, and realised seed/stage bounds.  In particular, `curl_transport_zero`, `slot_curl_transport_zero`, and related declarations establish exact cancellation under their explicit support/separation hypotheses.  This is important positive evidence against the blanket assertion that every curl interaction must be nonzero.  It still does not prove the selected global five-observable transport theorem; a support-separated interaction identity is not the same as a complete radial-moment identity for the assembled endpoint.

**Anchors:** lines 148–217, 233–337, 399–500, 629–697, 877–1029, 1035–1183.

## Cross-layer interpretation

1. `NativeCutoffJets` and `FlatDyadicExtension` control local jets, not global moment preservation.
2. `NilpotentVolterra` and `PhysicalWaveSum` provide real summation/finite-locality infrastructure, so the audit must not claim that `tsum` or wave assembly is absent or automatically invalid.
3. `SmoothLoop` proves genuine angular moment identities, so “no moment mathematics exists” is false.
4. `WaveInteractionBounds` proves exact zero interactions in separated-support cases, so “curl commutators are necessarily nonzero” is also false.
5. The unresolved question is narrower and stronger: whether the actual selected Cartesian field, with its complete masks, sums, curls, pressure, and endpoint packaging, is explicitly identified with all five paper observables.

