# Priority 223: source-only selected-transport replay

Date: 2026-10-01
Status: source-checked replay; no scientific verdict escalation

## Reproducible command

```powershell
& 'D:\Research Lab\V-lab-Equipment\.venv\Scripts\python.exe' `
  NavierStokesReview/src/audit/selected_transport_audit.py `
  --repo-root . `
  --source-root NavierStokes `
  --source-root NavierStokesReview/src `
  --json NavierStokesReview/evidence/selected_transport_audit_2026-10-01_source_only.json `
  --markdown NavierStokesReview/evidence/selected_transport_audit_2026-10-01_source_only.md
```

## Result

The replay indexed **31,836 source declarations**, found **11 joint source
candidates**, and found **3 full manual candidates**. All 11 candidates are
review-side declarations. The manual candidates are caller-supplied
`barMoment` interfaces; they are not production instantiations of the final
selected Cartesian field.

The source-only replay found no production declaration that simultaneously
binds the selected endpoint field, the manuscript moment operators, the
required curl/localisation/periodisation/summation transformations, and a
field-level equality or transport conclusion. This is the same bounded result
as the previous source census, with five additional declarations indexed.

## Interpretation boundary

This is declaration-level triage, not a proof by absence. The replay does not
prove that transport is mathematically impossible, that the selected moments
are nonzero, that the force is nonsmooth, or that Fefferman Alternative (C)
is false. It supports the narrower finding:

> `CTR-005: NOT ESTABLISHED` for complete manuscript-to-selected-endpoint
> fidelity.

The source-only run intentionally does not replace the separate Lean
environment closure. The current environment closure is recorded in
`NavierStokesReview/evidence/lean_environment_closure_ns_3d_2026-09-30_summary.md`;
its raw 366 MB export remains local and untracked.

## Evidence

- Machine-readable output:
  `NavierStokesReview/evidence/selected_transport_audit_2026-10-01_source_only.json`
- Human-readable output:
  `NavierStokesReview/evidence/selected_transport_audit_2026-10-01_source_only.md`
- Prior source census:
  `NavierStokesReview/evidence/selected_transport_audit_2026-09-30_review_sources.md`
- Current selected-path source trace:
  `NavierStokesReview/src/audit/priority_218_selected_endpoint_crosswalk_replay_2026-10-01.md`
