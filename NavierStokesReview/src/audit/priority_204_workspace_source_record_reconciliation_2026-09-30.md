# Priority 204: workspace source-record reconciliation

Date: 2026-09-30
Status: control discrepancy recorded; no scientific verdict changed

## Purpose

The current documentation pass found two different inventory figures in the
live review records. They must not be quoted as if they were one measurement.
This note records the scopes before the register or census is regenerated.

## Observed records

| Record | Reported scope | Reported count | Interpretation |
| --- | --- | ---: | --- |
| `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-29.json` | fork register rows | 2,794 | current documentation authority for register status |
| `NavierStokesReview/evidence/selected_endpoint_source_census_2026-09-30.md` | files under `NavierStokes/` | 817 | current direct source-file count; its report states this scope explicitly |
| `NavierStokesReview/evidence/source_tranche_priority_201_selected_closure_census_2026-09-30.json` | field `repository_lean_files` | 2,796 | scope is not defined sufficiently to reconcile it with the two records above |
| `source_tranche_priority_201...json` | selected endpoint closure | 588 | agrees with the direct endpoint closure record |

An independent live count gives 817 files under `NavierStokes/`, 1,839 under
`Euler/`, and 2 under `ComparatorChallenges/`. The effective register rows
also include review-side and root mirror rows. These are not interchangeable
with the `NavierStokes/`-only census.

The root-explicit replay of
`NavierStokesReview/src/audit/selected_endpoint_source_census.py` was run with
`--source-root NavierStokes` and returned 817 files, 429,297 source lines,
35,430 parsed declarations, 588 reachable endpoint modules, 380,791 active
closure lines, and zero missing local imports. This confirms the 817-file
scope; it does not regenerate the full 2,794-row register.

## Scientific disposition

This is an inventory-scope discrepancy, not evidence for or against the
Navier--Stokes construction. It does not alter the source-backed findings:

- the actual selected cycle has two preserved mean-mass identities and three
  residual-debt classes;
- those data feed physical data, residual-rate, force-extension, and blow-up
  declarations;
- the inspected selected closure still has no located production theorem
  identifying the completed selected Cartesian construction with the
  manuscript tuple `(M,I,J,S,C_p)`;
- `CTR-005` remains `NOT ESTABLISHED` for complete paper-to-endpoint fidelity;
- no selected nonzero defect, force nonsmoothness, literal CMI failure,
  impossibility theorem, compiler escape, or `False` is inferred.

## Required correction

Before quoting repository totals again, rerun the register and the endpoint
census from explicitly declared roots, then publish one scope table covering:

1. `NavierStokes/` source files;
2. the full fork register roots;
3. the selected endpoint import closure; and
4. review-side Lean files.

Until that rerun, the documentation authority remains the 2,794-row register
for register metrics, and the 817-file count remains the direct
`NavierStokes/` source census. The 2,796 value is retained as an unresolved
historical/source-tranche field, not a live headline count.

## Evidence

- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-29.json`
- `NavierStokesReview/evidence/selected_endpoint_source_census_2026-09-30.md`
- `NavierStokesReview/evidence/source_tranche_priority_201_selected_closure_census_2026-09-30.json`
- `NavierStokesReview/src/audit/selected_endpoint_source_census.py`
