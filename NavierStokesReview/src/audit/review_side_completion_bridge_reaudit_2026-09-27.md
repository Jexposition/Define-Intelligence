# Review-side completion bridge re-audit

Date: 2026-09-27
Scope: review-side Lean files already created under `NavierStokesReview/src/completions/`
Purpose: reconcile source inspection with the semantic coverage register.

## Scope boundary

These files are auditor-authored review artefacts. They are not part of the
OpenAI `NavierStokes/` source closure and are not imported by
`NavierStokesR3.theorem_1_1`. Their declarations therefore cannot be counted
as evidence that the upstream endpoint transports the paper's five moments.
This tranche was source-read; no successful Lean build is claimed here.

The authoritative register remains:

- 2,790 indexed Lean modules;
- 588 modules reachable from the explicit `NavierStokes/` source root;
- 170 explicit source-review records;
- 443 reachable source modules still awaiting declaration-level semantic classification.

The 16 files below increase the evidence record but do not reduce the 443
OpenAI-source queue, because their register rows are `reachable: false`.

## Declaration-level results

| Review file | Declarations inspected | Classification | What it establishes | What it does not establish |
|---|---|---|---|---|
| `SelectedBarMomentInterface.lean` | `selectedPotentialComponent`, `pullbackScalar`, `selected_component_barMoment_apply`, `SelectedBarMomentTransportData` | `transport_data_required` | Makes the missing point-map/scalar equality explicit and rewrites a typed `barMoment` expression | It does not show that `selected_witness` supplies the data |
| `SelectedBaseProfileTransport.lean` | `constructed_curl_eq_selected_velocity`, `constructed_curl_axis_tendsto` | `intermediate_positive` | Relates a constructed curl branch to a selected-base branch and records an axis limit | It is not the complete five-observable endpoint bridge |
| `SelectedCutStageCurlScope.lean` | `selected_cut_stage_curl_expansion`, `selected_cut_stage_curl_component_zero` | `commutator_exposed_not_evaluated` | Gives the cutoff-times-curl plus cutoff-gradient commutator expansion | It does not evaluate the global radial integral or prove a nonzero defect |
| `SelectedCylindricalComponentTransport.lean` | frame first-component formula, `velocity_polar_component_one` | `intermediate_positive` | Provides a positive-radius cylindrical component identity | It does not provide global axis, torus, or `barMoment` transport |
| `SelectedDirectRadialMomentBridge.lean` | direct branch/native scalar and order-2 radial identities | `intermediate_positive` | Shows a direct native scalar branch has the stated zero moment | It does not identify that branch with the mixed curl-generated endpoint field |
| `SelectedDirectStageMomentTransport.lean` | `selected_angular_native_stage_moment_zero` | `intermediate_positive` | Carries a cycle zero invariant through direct native stage differences | It does not prove the final Cartesian field equality |
| `SelectedPhysicalComponentTransport.lean` | polar-map first component and scaled chart formulas | `intermediate_positive` | Establishes chart-level component formulas | It stops before global radial evaluation |
| `SelectedPhysicalPointTransport.lean` | physical moment point / `PressureStream` rewrite | `transport_data_required` | Identifies the point representation needed by a moment rewrite | It requires explicit transport data and is not selected-witness evidence |
| `SelectedPotentialProductionRadialScalar.lean` | production scalar, differentiability, cutoff-times-curl product rule | `commutator_exposed_not_evaluated` | Makes the selected production scalar and commutator calculus explicit | It does not prove a global moment value |
| `SelectedPotentialStageChartTransport.lean` | selected potential-stage curl / source-chart `EqOn` relation | `intermediate_positive` | Relates a selected chart branch to source chart data on its stated domain | `EqOn` is not a global integral identity |
| `SelectedStreamCurlChartTransport.lean` | selected stream-stage curl / chart-stream `EqOn` relation | `intermediate_positive` | Relates stream-stage curl components on the chart domain | It does not transport the five moments through localisation and summation |
| `SelectedStreamRankScope.lean` | successor stream assembly and rank premise | `intermediate_positive` | Records temporal/rank assembly scope and its upstream premise | It does not close curl-to-`barMoment` transport |
| `SelectedSupportPredicateScope.lean` | shrinking-support countermodel | `nonimplication_countermodel` | Shows the stated support predicate does not imply the cutoff-plateau axial condition | It is not a countermodel to the concrete selected smooth field |
| `SelectedTorusLiftImageScope.lean` | physical-lift image restriction | `transport_data_required` | Identifies the nonnegative-radius image and an unreachable negative-radius square point | It does not prove a missed nonzero selected moment |
| `SelectedScalarSamplingNonuniqueness.lean` | two scalar families agreeing on sampled physical points | `nonimplication_countermodel` | Shows the raw sampling map is non-injective off the physical image | It does not calculate the selected family or prove `False` |
| `SelectedCycleMomentTransport.lean` | cycle-state zero-mass/zero-row consequences | `intermediate_positive` | Records cycle-local invariant consequences | It does not identify them with the final selected Cartesian observables |

## Audit consequence

The tranche strengthens the map in two directions. First, several
intermediate bridges are real and must not be described as absent. Secondly,
the missing endpoint remains specific: no inspected review-side declaration
proves

```text
barMoment(torusAverage(periodise(curl(tsum(potentialSum)) * cutoff)))
  = (M, I, J, S, C_p)
```

and no inspected declaration proves that the corresponding equality is a
field of `ActualCandidateAssembly.Witness` or a premise of
`selected_witness`. The cutoff-gradient term is exposed, but its selected
global integral has not been evaluated. Therefore this tranche supports
`CTR-005: not established` and does not support a nonzero selected defect,
an impossibility theorem, or a kernel-level `False`.

## Register artefacts

- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`
- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.md`
- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.html`

The plan, workspace goal, and audit tracker must cite this report whenever
they cite the 170-review count.
