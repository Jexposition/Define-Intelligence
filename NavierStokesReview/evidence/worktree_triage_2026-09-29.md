# Worktree triage and consolidation control

**Date:** 2026-09-29
**Repository:** `Jexposition/Define-Intelligence`
**Branch:** `review/cmi-first-navier-stokes-2026-09-29`

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

## Live worktree refresh (2026-09-29, refreshed)

The current worktree contains a mixed set of tracked documentation/register
changes and untracked evidence, scans, source inputs, and scratch material.
This is not a publication batch.
The tracked modifications are dated evidence bundles and reconciliation maps;
they require content and provenance checks before staging. The untracked set
contains source inputs, review evidence, exploratory numerical outputs, build
logs, tree indexes, scratch material, and one user-owned source file.

The current curated public worktree contains untracked generated tree or
closure indexes. They remain outside the public commit until their generation
inputs and links are verified.

### Duplicate and archive controls

The following exact duplicate groups were identified outside `.lake`, build
artefacts, and the existing archive:

1. `claim_register_2026-09-26.{json,md}` and
   `review_claim_register_2026-09-26.{json,md}` are byte-identical tracked
   pairs. They remain in place because eight current evidence maps refer to
   both names. A canonical-name decision and link migration are required
   before any move.
2. The current semantic-coverage HTML, JSON, and Markdown mirrors in `docs/`
   and `NavierStokesReview/evidence/` are byte-identical. The `docs/` copies
   are the public-facing mirrors; the evidence copies remain uncommitted until
   the evidence-tree links are reconciled.

No duplicate has been deleted or moved in this refresh. The existing local
archive remains the only archive destination, with its manifest controlling
provenance. The next consolidation pass must update references before moving
any historical generated file and must leave `NavierStokes/R3/TestPressure.lean`
and `scratch_space/` untouched.

### Immediate triage order

1. Verify the eight tracked evidence changes against their source snapshot and
   current endpoint counts.
2. Reconcile the evidence tree and document tree with the current semantic
   coverage register.
3. Decide the canonical claim-register names and update all references before
   any archive move.
4. Promote only source-backed evidence ledgers and formally reviewed results
   to a curated commit; keep scans, logs, scratch, and user-owned source out.
