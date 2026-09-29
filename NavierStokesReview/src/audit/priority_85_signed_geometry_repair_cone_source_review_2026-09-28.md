# Priority 85 source review: signed geometry, heat switch, repair cone, and label sums

Date: 2026-09-28
Scope: direct source inspection of six reachable `NavierStokes` modules.
Purpose: test whether the next geometry/correction tier contains a differently named five-moment bridge.

## Executive result

This tranche materially strengthens the positive record. Most importantly, `RepairConeBounds.lean` contains an actual five-coordinate reduced-profile theorem, not merely a generic interface:

```text
actual_moments
    normalized reduced fields -> freeRows : Fin 5 -> ℝ
physical_rows
    reduced primitive -> scaled freeRows
physical_stock_values / physical_transport / physical_lags / physical_stocks
    physical chart fields and stocks -> the corresponding reduced controls
```

That finding corrects any blanket statement that five-moment transport is absent throughout the repository. The exact scope is still decisive: these declarations use reduced profiles, chart coordinates, stock/history objects, and explicit local hypotheses. This tranche does not show that the final whole-space Cartesian field exported by `ActualCandidateAssembly.selected_witness`, after its actual curl/localisation/series/periodisation route, is identified with the paper tuple at the public `Witness` boundary.

No nonzero selected-field defect, impossibility theorem, or kernel `False` is claimed.

## Source findings

### `LabelSumBounds.lean`

This module proves finite active-label sum jet bounds, support-window consequences, covariance support, and harmonic covariance class transport for assembled oscillations. It is concrete finite-sum and covariance infrastructure and is relevant to the assembled wave layer, but its declared outputs do not identify the public selected field with the five paper observables.

Relevant regions: lines 157-372, 499-624, 745-818, and 1004-1085.

### `CommonCoverClass.lean`

This module defines actual common-cover paths, affine argument maps, band ratios, chart costs, class/jet transport, profile slow strips, and radial/temporal native bases. It establishes geometric transport over overlapping bands and preserves weighted classes under those maps. It is not a final radial-observable evaluator.

Relevant regions: lines 180-354, 414-565, 633-715, 857-971, 1016-1137, and 1273-1300.

### `HeatSwitchCone.lean`

This module constructs the compensated heat switch and proves smooth history identities, exact pressure/future-integral relations, strict true-cone preservation, uniform compensation thresholds, and exact change-row integral relations. It shows that the heat-switch layer has substantive compensated cone and moment-related mathematics. The theorem `changeRow_prefix_eq_neg_future_heat` is an exact finite-prefix/future-tail relation, not a final Cartesian endpoint statement.

Relevant regions: lines 7-25, 67-175, 365-447, 616-768, 805-831, 1008-1092, and 1104-1248.

### `ActualSignedGeometry.lean`

This module defines the actual signed pulse geometry, common-cover charts, active-pair indexing, phase cells, support cutoffs, and phase-normal/copy identities. It connects actual profile labels and geometry to signed stage coordinates and establishes support and local smoothness control. It does not state the final radial observable transport theorem.

Relevant regions: lines 30-219, 249-372, 461-588, 806-946, 1143-1239, and 1265-1433.

### `ActualSignedStageControls.lean`

This module instantiates actual signed correction-stage parameters, derives requests from current residuals or invariants, and proves native geometry/cutoff, uniform cell-jet, covariance, pulse, and normal-control results. It is a concrete stage-data layer, not merely a blank rate interface. It does not export the complete selected Cartesian five-observable equality.

Relevant regions: lines 1-199, 203-385, 444-525, 543-680, 704-777, 814-1010, and 1042-1185.

### `RepairConeBounds.lean`

This is the key positive finding in the tranche.

- `freeM`, `freeI`, `freeJ`, `freeS`, and `freePi` define the five reduced control rows (lines 110-124).
- `outgoing_moments_log` identifies outgoing reduced moments with the log-row representation (lines 328-377).
- `actual_moments` (lines 491-525) proves that normalized profile moments equal `freeRows : Fin 5 → ℝ` under the separation, parameter, window, and small-debt hypotheses.
- `physical_rows` (lines 804-822) transports the reduced primitive to scaled physical rows.
- `physical_stock_values` (lines 824-866) gives the five physical stock values `(M,I,J,S,pressure)` at the chart point.
- `physical_transport`, `physical_lags`, and `physical_stocks` (lines 946-993) continue the transport to physical control quantities.
- `physical_field_radials` and related declarations (lines 1026-1163) connect field/radial values and parameters under the explicit chart hypotheses.

This is not an interface-level countermodel. It is a real reduced/profile five-row transport theorem. The remaining audit question is whether these values are then composed with the final Cartesian potential/curl fields, localisation, `tsum`, periodisation, pressure/force packaging, and `ActualCandidateAssembly.Witness` so that the public selected field satisfies the paper's advertised observables. The source reviewed here does not establish that final composition.

## Corrected correspondence map

```text
Five reduced moments / rows
        |  RepairConeBounds.actual_moments
        v
Physical chart rows and stock values
        |  physical_rows, physical_stock_values, physical_transport
        v
Signed geometry / heat switch / finite sums / covariance
        |  ActualSignedGeometry, HeatSwitchCone, LabelSumBounds,
        |  ActualSignedStageControls, CommonCoverClass
        v
Final Cartesian selected field and public Witness
        |  full curl + localisation + tsum + periodisation + endpoint
        |  composition still requires direct source proof
```

## Audit adjudication

`CTR-005` must be stated narrowly: the complete selected Cartesian endpoint correspondence remains unestablished on the reviewed evidence. It must not be stated as “no five-moment theorem exists in the repository”.

The tranche also does not establish that curls or cutoffs necessarily create a nonzero defect. It establishes that a real reduced five-row bridge exists and that the final composition still needs to be traced without substituting reduced/profile equality for Cartesian endpoint equality.
