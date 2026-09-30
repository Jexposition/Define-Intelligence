# Priority 201: selected-endpoint closure census and transport-candidate disposition

Date: 2026-09-30
Status: source-checked and review-side candidates compiled
Controlled finding: `CTR-005: NOT ESTABLISHED` for complete manuscript-to-selected-endpoint correspondence

## Scope

This tranche closes the current source-level census from the two selected
endpoint roots:

- `NavierStokes.R3.Theorem`
- `NavierStokes.ActualCandidateAssembly`

It also compiles the review-side declarations that a lexical audit identified
as possible moment/endpoint candidates. The census is not a substitute for a
Lean proof, and a compiled review-side lemma is not silently promoted to a
production theorem.

## Current closure result

The source census covers 2,796 Lean files, 649,713 source lines, and 50,205
parsed declarations. The selected endpoint closure contains 588 local
modules, 380,791 active source lines, and 2,378 local import edges. It has
zero missing local imports. The full repository contains 209 external Mathlib
roots that are expected dependencies rather than missing local files.

The active closure contains 7 lexical moment/endpoint co-occurrence rows:

| Source declaration | What it actually proves | Disposition |
| --- | --- | --- |
| `ActualPhysicalStageBounds.initialDirect_rate` | A native jet-rate bound for an angular field | rate result; no final moment identity |
| `ActualPhysicalStageBounds.background_from_representations` | Equality of finite background representations on a physical sublevel | local representation result; no five-moment transport |
| `GermCandidateAssembly.potentialSum_eq_base_germ` | Potential-sum agreement with the base germ near a point | germ result; no five-moment transport |
| `InitializedPhysicalBackground.directIncrement_rate` | A native jet-rate bound for the direct increment | rate result; no final moment identity |
| `MixedAxisPreservation.origin_blowup_global` | Axis blow-up for a mixed copy-series under explicit hypotheses | blow-up route; no final moment identity |
| `MixedCandidateAssembly.StageEstimates.exists_schedule` | A schedule with smooth sums and vanishing residual jets | schedule/flatness result; no final moment identity |
| `MixedCandidateWitness.SelectedSchedule` | A proposition packaging schedule and vanishing-jet conditions | contract; no final moment identity |

No active source declaration in this census proves an equality identifying the
final selected Cartesian velocity, pressure, residual, or force with the
paper's five cumulative quantities `(M,I,J,S,Cp)`.

## Review-side candidate checks

The following review-side files compile under the repository's actual pinned
toolchain (`leanprover/lean4:v4.34.0-rc2` via `lake env lean`):

- `completions/SelectedBarMomentInterface.lean`
- `completions/SelectedPhysicalPointTransport.lean`
- `completions/PeriodicGlobalIntegral.lean`
- `completions/SelectedR3PackagingBoundary.lean`
- `probes/FiveRowCollisionBoundaryProbe.lean`

Their results are materially different from a selected-field transport
theorem:

1. `selected_component_barMoment_apply` and
   `selected_component_requires_transport_data` prove an identity only after
   the caller supplies `pointToSpaceTime`, a scalar pullback, and the equality
   relating that pullback to a selected potential component. The production
   `Witness` does not export that data as a named five-moment equality.
2. `barMoment_transport_requires_selected_scalar` confirms the physical point
   type is definitionally compatible with the `PressureStream` point type. It
   does not construct the selected scalar profile or prove the five paper
   integrals for the final field.
3. `selected_mixed_barMoment_zero_of_positive_pullback` is conditional on a
   positivity premise and uses global Bochner non-integrability followed by
   `integral_undef`. It is not a theorem about the selected Cartesian field's
   physical moment values.
4. `selected_r3_candidate_compatible_with_nonzero_five_payload` and
   `selected_witness_and_nonzero_rank_debt_coexist` show that an abstract
   nonzero debt value can coexist with the exported candidate proposition.
   They establish type-level non-entailment, not a numerical or analytic
   nonzero defect of the selected field.

## Disposition

The census and compilations support all of the following simultaneously:

- the selected endpoint is a substantial construction, not an empty generic
  rate shell;
- actual physical data feed residual-rate and force-smoothness constructions;
- the manuscript's five-moment repair is load-bearing in its stated argument;
- the exported `Witness` does not, in the inspected declaration, expose a
  named final five-moment identification theorem;
- the present record has not proved a selected-field defect, force
  nonsmoothness, impossibility, compiler escape, or `False`.

The correct scientific conclusion remains:

> The literal forced CMI-shaped endpoint is present in the Lean source, while
> exact paper-to-selected-field correspondence for the manuscript's full
> five-moment mechanism is not established by the current exported record.

This is a correspondence finding, not a claim that the mathematics works
without the moments and not a claim that the selected field is known to have
the wrong moments.

## Evidence

- `evidence/selected_endpoint_source_census_2026-09-30.json`
- `evidence/selected_endpoint_source_census_2026-09-30.md`
- `evidence/selected_transport_audit_2026-09-30.json`
- `evidence/selected_transport_audit_2026-09-30.md`
- `ActualCandidateAssembly.lean:1079-1098,1121-1151,1177-1185`
- `ActualCycleResidualBounds.lean:1015-1037,1156-1172`
- `CandidateFromLimits.lean:45-112`
- `GermCandidateAssembly.lean:146-271`
