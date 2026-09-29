# Priority 111: Cycle preservation and particular-realisation source review

Date: 2026-09-28
Scope: direct source review of three reachable Lean modules selected from the live semantic coverage register.
Classification rule: local transport is recorded when present; absence of the final selected-field observable is not treated as proof that all upstream transport is absent.

## Executive result

The reviewed modules contain substantive value-level composition:

\[
\text{cycle state}
\to \text{particular data}
\to \text{curl-corrected field}
\to \text{germ/support/periodicity transport}.
\]

This is stronger than a generic rate-only interface. It does not, in the inspected declarations, close the remaining endpoint question:

\[
\text{selected Cartesian field}
\xrightarrow{\text{torus/radial observable}}
(M,I,J,S,C_p).
\]

No non-zero defect or kernel-level `False` is inferred from this tranche.

## Module findings

### `NavierStokes/ActualCyclePreservation.lean`

The module imports the actual correction, carrier, core-support, wave-regularity, signed-output, particular-cycle, debt-bound, coherence, periodicity, and iteration layers (lines 1–16). It defines a concrete fixed `staticData` record (lines 42–72), cycle-stage state and label preservation (lines 149–159), and current-state rank geometry and debt regularity (lines 89–96).

The source proves genuine stage-level properties:

- primary-field smoothness and periodicity (lines 167–191 and 237–255);
- core/control/support invariants (lines 259–389);
- signed coefficient, pressure, tangent-field smoothness, periodicity, and support (lines 453–526);
- assembly of particular and signed data, including curl and support fields (lines 538–726);
- indexed run invariants and periodicity transport (lines 730–914).

The inspected output is an invariant over cycle states and stage data. It does not state a final `barMoment` evaluation, a `FiveRows` equality for the selected Cartesian field, or an equality with `(M,I,J,S,C_p)`.

### `NavierStokes/ActualParticularRealization.lean`

This module proves local coordinate and differential transport rather than merely naming a curl. The reindexing lemmas `normal_pull`, `curl_pull`, and `realizedCoefficient_pull` occur at lines 36–60; germ transport for the complete curl correction occurs at lines 62–71.

The realization layer then proves:

- cylindrical and Cartesian realization through `SpatialCurl` (lines 432–433 and 523–567);
- `cycle_velocity_realization` (lines 547–565);
- `cycle_pressure_realization` (lines 567–614);
- full-variable curl covariance and differentiated germ transport (lines 616–673);
- smoothness and covariance of lifted coefficients (lines 731–867);
- selected current-input velocity and pressure realization (lines 996–1034);
- cycle-level `EqOn` realization on the prescribed domains (lines 1067–1085).

This is a real local curl/pressure bridge. It is not evidence that the final `tsum`/periodised Cartesian field has been passed through `barMoment` or identified with the five paper moments.

### `NavierStokes/ActualParticularCoherence.lean`

The module transports particular-wave data from current-state germs to the target chart. `TargetChart` is defined at lines 55–75. `corrected_amplitude_chart` and `corrected_eq_band_of_germs` occur at lines 75–146; the latter explicitly propagates agreement through the complete curl correction, including the covariance of the carrier products.

Further declarations prove:

- forward germ transport from current-state comparisons (lines 147–286);
- smooth and supported reference/parameter cutoffs (lines 501–543);
- copy, band, and Gaussian source transport (lines 591–936);
- supported source records and parameterised particular data (lines 816–936).

The module therefore closes a genuine local chart/germ/cutoff route. Its inspected declarations do not define or prove a final Cartesian radial observable, `barMoment` preservation, or `(M,I,J,S,C_p)` equality.

## Correspondence classification

| Layer | Evidence in this tranche | Status |
|---|---|---|
| Cycle-state preservation | `Invariant`, state iteration, debt regularity, smoothness, support, periodicity | Present locally |
| Curl realization | `curl_pull`, `realizedCoefficient_pull`, `cycle_velocity_realization`, `SpatialCurl` | Present locally |
| Pressure realization | `cycle_pressure_realization`, pressure/source transport | Present locally |
| Germ and cutoff transport | `corrected_eq_band_of_germs`, cutoff smoothness/support, source transport | Present locally |
| Selected global `tsum` field | No final radial-observable declaration in these modules | Not established here |
| Five-moment endpoint transport | No inspected declaration asserting selected-field `barMoment = (M,I,J,S,C_p)` | Not established here |

## Audit consequence

This tranche narrows the honest statement of CTR-005. The repository has real local field construction and transport; the unresolved issue is the composition of those results with the final selected global field and the paper-level radial observables. The evidence supports `Not Established` for paper-to-endpoint correspondence, not an unconditional refutation.
