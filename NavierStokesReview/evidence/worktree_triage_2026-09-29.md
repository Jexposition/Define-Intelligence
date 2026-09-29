# Worktree triage and consolidation control

**Date:** 2026-09-29
**Repository:** `Jexposition/Define-Intelligence`
**Branch:** `review/cmi-first-navier-stokes-2026-09-22`

## Purpose

This register prevents bulk staging and prevents evidence loss while the
review workspace is consolidated. It is a control record, not a claim that
any file is disposable. No file is deleted or moved by this triage entry.

## Current classification

| Class | Current material | Treatment |
|---|---|---|
| Curated control documents | `docs/OpenAI_NavierStokes_CMI_First_Review_Plan.md`, `docs/REVIEW_AUDIT_WORKSPACE_GOAL.md`, `docs/REVIEW_DOCUMENT_CONTROL.md` | Review diff, then commit with the current closure evidence. |
| Current generated registers | `semantic_coverage_register_full_2026-09-29.*`, `hardened_source_map_2026-09-29.*`, and their deliberate `docs/` mirrors | Retain only after count, header, and mirror checks agree. |
| Endpoint evidence | `direct_endpoint_closure_validation_2026-09-29.md` and the selected-transport audit ledgers | Retain, cross-link, and cite as scope/evidence records. |
| Manuscript and review | `docs/OpenAI_NavierStokes_Research_Paper.md`, `docs/OpenAI_NavierStokes_Peer_Review_v1.md` | Keep readable and academic; do not turn the manuscript into a chronological log. |
| Exploratory numerical scans | `cutoff_commutator_*` CSV/JSON/PNG/MD outputs | Hold outside the curated publication tranche. They are model/scanner evidence, not proof about the selected Lean field. Promote only after source alignment and methodological review. |
| Historical generated maps/registers | Dated `2026-09-26` and `2026-09-27` maps, bundles, registers, and graphs | Do not archive until hashes, provenance, and references have been checked against the current 2026-09-29 artefacts. Archive only by moving to `NavierStokesReview/evidence/archive/`, with a manifest. |
| Build logs | `controlled_build_*`, `environment_build_*`, and fresh replay reports | Retain only when linked to a reproducible claim; otherwise hold for later evidence consolidation. Never use an unlinked log as a theorem. |
| Source inputs and trees | PDFs, extracted text, `docs/*_tree.md`, and review tree files | Preserve. Reconcile their links before any archive move. Do not modify OpenAI source folders. |
| User-owned source | `NavierStokes/R3/TestPressure.lean` | Leave untouched and unstaged. |
| Scratch and ignored artefacts | `scratch_space/` and `__pycache__/` | Do not commit. Do not delete during this pass. |

## Publication gate

Only the first four classes, plus explicitly reviewed evidence ledgers, may
enter a curated commit. A clean commit must not include scratch material,
ignored bytecode, user-owned source, exploratory plots, or an unreviewed bulk
of historical generated files. Publication to the review branch is deferred
until this gate is satisfied and the resulting commit is independently
verified.

## Adjudication boundary

The selected-field five-moment correspondence remains **not established on
the current record**. This is an adverse finding against the advertised
paper-to-Lean claim. It is not a repair request, and it is not by itself a
proof of a nonzero defect, impossibility, or `False`.
