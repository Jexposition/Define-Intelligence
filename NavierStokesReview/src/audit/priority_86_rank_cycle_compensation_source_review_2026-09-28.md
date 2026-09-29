# Priority 86 source review: rank patches, cycle induction, and terminal compensation

Date: 2026-09-28
Scope: direct source inspection of six reachable `NavierStokes` modules.
Purpose: trace the local rank/cycle correction layer after the reduced five-moment findings in Priority 85.

## Executive result

This tranche finds further genuine correction bridges. In particular, `BaseRankPatch.five_rows` explicitly proves `FiveRowRank.FiveRows` for the full final base on the mean patch, using the actual support radii and similarity scales. `ActualCycleExcluded`, `CorrectionAnalyticStep`, `RankStateBounds`, and `ParametricTerminalCompensation` also carry concrete cycle-state, covariance, three-component debt, and compensation data.

These findings further narrow the unresolved issue. The audit can no longer say that rank or five-row mathematics is absent upstream. The remaining question is whether these local/reduced/base identities are composed with the actual final Cartesian field, global localisation, infinite series, periodisation, force/pressure packaging, and public `selected_witness`/`Witness`. No selected-field `Delta m != 0`, impossibility theorem, or `False` is claimed.

## Source findings

### `ActualCycleExcluded.lean`

This module propagates actual primitive and cumulative data through particular, signed, temporal, and rank stages. It tracks covariance updates and derives all-power bounds for next axisymmetric aliases. The outputs are concrete cycle-state and alias controls, not the final public five-observable equality.

Relevant regions: lines 20-71, 94-130, and 153-210.

### `RankStateBounds.lean`

This module lifts actual three-component slow debt classes, defines normalized rank parameters, transports fixed-shell classes to moving support, and proves variable-gauge rank-increment bounds and support margins. It is direct three-component rank-state evidence. It is not by itself a five-coordinate global observable theorem.

Relevant regions: lines 25-87, 90-139, 143-225, and 252-332.

### `BaseRankPatch.lean`

This module constructs actual final-base angular and axial slices and proves background identities on the mean patch. The key declaration is:

```text
five_rows ... : FiveRowRank.FiveRows (angularSlice ...) (axialSlice ...) debt ...
```

The proof applies `MeanRankUpdate.physical_rows_on_patch` with the actual profile scales and support margins. This is a genuine local physical rank bridge and must be included in any fair source account. It remains a patch/base theorem, not the complete whole-space selected Cartesian assembly theorem.

Relevant regions: lines 24-71, 87-190, 230-289, and 333-358.

### `ParametricTerminalCompensation.lean`

This module proves variable-debt coefficient compensation, derivative and compact-amplitude bounds, radius-ratio scaling, physical three-component debt identities, and existence of physical heat compensation. It supplies actual terminal correction data and parameter regularity rather than an abstract placeholder.

Relevant regions: lines 20-124, 226-347, and 365-471.

### `ActualMeanStageData.lean`

This module builds the actual radial section, coefficient/angular field, shrinking supports, zero germs, initial angular/temporal/rank/stream data, and iterated cycle mean-stage data. It is concrete physical-stage ingestion and support control. No final Cartesian five-observable equality is stated in the inspected declarations.

Relevant regions: lines 22-65, 77-178, 190-281, 296-362, and 368-462.

### `CorrectionAnalyticStep.lean`

This module defines the actual analytic correction step, proves signed and particular zero-germ and covariance-moving inputs, constructs step results, and proves invariant and result iteration preservation. Its outputs are correction invariants and estimates. They do not by themselves identify the public selected Cartesian field with the complete paper tuple.

Relevant regions: lines 25-149, 152-262, 467-632, and 654-690.

## Corrected dependency interpretation

```text
Reduced five rows / local rank patch
        |  RepairConeBounds.actual_moments
        |  BaseRankPatch.five_rows
        v
Actual cycle induction and terminal compensation
        |  ActualCycleExcluded, CorrectionAnalyticStep,
        |  RankStateBounds, ParametricTerminalCompensation
        v
Actual stage data and support/covariance controls
        |  ActualMeanStageData and prior signed geometry layers
        v
Final Cartesian selected endpoint
        |  remaining composition test: curl, localisation, tsum,
        |  periodisation, pressure/force, and public Witness
```

The first two levels are now source-confirmed in multiple independent clusters. The final line remains the load-bearing correspondence test. Import reachability and local theorem existence do not substitute for the value-level composition declaration.

## Audit adjudication

`CTR-005` remains a narrow selected-endpoint correspondence finding, not a repository-wide claim that the moment/rank machinery is absent. The evidence now supports the stronger statement that substantial reduced and local physical transport exists, while the final selected Cartesian export still requires direct declaration-level tracing. No unconditional falsification is recorded.
