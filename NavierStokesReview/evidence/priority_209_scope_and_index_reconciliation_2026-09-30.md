# Priority 209: scope and index reconciliation

Date: 2026-09-30
Status: current source map and register regenerated; no scientific disposition changed

## Purpose

The previous control record mixed three measurements: the full fork register,
the `NavierStokes/`-only census, and a historical `repository_lean_files`
field from Priority 201. A fresh root-explicit replay was required before
quoting any repository total. This record is the current scope authority.

## Current measurements

| Measurement | Scope | Count | Authority |
| --- | --- | ---: | --- |
| Whole checkout Lean files | all current `.lean` files excluding `.git` and `.lake` | 2,797 | `hardened_source_map_2026-09-30.json` |
| Selected endpoint closure | import closure from the hardened selected roots | 588 | `semantic_coverage_register_full_2026-09-30.json` |
| Outside selected closure | current register rows not in that closure | 2,209 | regenerated register |
| `NavierStokes/` Lean files | direct OpenAI Navier--Stokes source root | 817 | explicit source-root census |
| `NavierStokesReview/` Lean files | review-side Lean sources | 137 | explicit source-root census |
| Current non-`.lean` and Lean files | checkout files excluding `.git` and `.lake` | 3,449 | hardened source map |

The 588-module closure is a bounded import-graph statement. “Outside
selected closure” means outside the chosen roots used for this audit; it does
not mean dead, unreachable in OpenAI's other roots, or semantically irrelevant.
The direct `NavierStokes/` count is a filesystem scope and is not the same
measurement as the full fork register.

## Register drift

The previous register had 2,794 rows and omitted exactly three newer review-side
Lean files:

- `NavierStokesReview/src/completions/SelectedFeffermanAlternativeCProof.lean`
- `NavierStokesReview/src/extensions/CMIAlternativeCLiteralCrosswalk.lean`
- `NavierStokesReview/src/probes/ActualMomentPreservationTrace.lean`

It did include the protected untracked
`NavierStokes/R3/TestPressure.lean`. The register and source map were
regenerated from the current checkout, so the current register now has 2,797
rows and no register-only stale paths.

This resolves the earlier 2,794-versus-current discrepancy as stale register
generation, not a claim about OpenAI's build graph and not a probe failure.

## Ten versus seven `sorry` counts

The regenerated register reports both measures deliberately:

- `source_rows_with_sorry_token = 10` is the lexical source count;
- `status.source_indexed_sorry_token = 7` is the classification count.

The three lexical rows already classified as `evidence_inspected` are
`ComparatorChallenges.Euler`, `ComparatorChallenges.NavierStokes`, and
`NavierStokesReview.src.completions.SelectedSupportPredicateScope`. Therefore
the relationship is `10 = 7 + 3`, not a contradiction. This is a bookkeeping
distinction and does not reclassify any endpoint theorem.

## Current documentation replay

After adding the Priority 209 control artefacts, the live documentation replay
checked 424 Markdown files and 62,736 local Markdown links, with zero broken
targets after excluding external URLs, Windows absolute paths, and mathematical
bracket notation. It parsed 101 evidence JSON files with zero failures. The
archive manifest has five rows covering four unique archive artefacts, and all
current SHA-256 values match.

The earlier Priority 208 values of 415 Markdown files and 98 evidence JSON
files remain valid as that gate-time snapshot. They are not the current corpus
total; this Priority 209 replay is the current count.

## Tree-index correction

The older evidence, audit, and source trees remain useful historical
navigation snapshots, but they are not current file authorities. Their current
appendices now point to this record, the regenerated source map/register, the
three formerly omitted review-side files, and the current Priority 207--208
control records. Generated `__pycache__`/`.pyc` entries are explicitly treated
as excluded build artefacts; no deletion was performed.

## Scientific disposition

This control correction does not change the scientific finding. The selected
cycle has genuine internal invariant, physical-data, residual-rate,
force-extension, and axis blow-up machinery. The bounded selected-closure
search still has no located production declaration identifying the completed
selected Cartesian velocity, pressure, residual, and force with the manuscript
tuple `(M,I,J,S,C_p)`.

The controlled classification remains **`CTR-005: NOT ESTABLISHED`** for
complete manuscript-to-selected-endpoint correspondence. This record does not
prove a selected nonzero defect, force nonsmoothness, literal forced CMI
failure, impossibility, compiler escape, or `False`.

## Reproducibility inputs

- `NavierStokesReview/src/audit/hardened_source_map.py`
- `NavierStokesReview/src/audit/semantic_coverage_register.py`
- `NavierStokesReview/src/audit/selected_endpoint_source_census.py`
- `NavierStokesReview/evidence/hardened_source_map_2026-09-30.json`
- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-30.json`
- `docs/REPOSITORY_SEMANTIC_COVERAGE_REGISTER.json`
