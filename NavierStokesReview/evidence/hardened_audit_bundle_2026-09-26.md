# Hardened audit bundle

This is a reproducibility index for the review-side source and compiled-environment maps.
The layers are deliberately not merged into one claim: filesystem identity, source navigation, and kernel reachability answer different questions.

## Validation

- Bundle validation: **passed**
- Tree SHA-256: `476cc9257bf6f3a8259fe78110bdcd9df170b8e265dabb6aeb13e850aa522d17`
- Reachable compiled declarations using `sorryAx`: `0`
- Git status entries at capture: `16`
- Tree entries without a current basename: `0`
- Tree entries with ambiguous current basenames: `24`

## Counts

| Layer | Count | Meaning |
|---|---:|---|
| Extracted-tree entries | `3021` | inventory snapshot |
| Current checkout files | `3088` | filesystem census |
| Lean modules | `2790` | source module census |
| Source declarations | `50191` | parser diagnostics |
| Diagnostic declaration edges | `186194` | token-based, non-authoritative |
| Compiled environment nodes | `30721` | kernel environment export |
| Compiled environment edges | `227128` | declaration references |
| Exact source matches | `22958` | fully qualified name join |

## Required endpoint routes

- `NavierStokesR3.theorem_1_1`: reachable through `0` compiled edges
- `NavierStokes.ActualCandidateAssembly.selected_witness`: reachable through `3` compiled edges
- `NavierStokes.FiveRowRank.FiveRows`: reachable through `18` compiled edges
- `NavierStokes.PositiveOrderMoments.Debt`: reachable through `11` compiled edges
- `NavierStokes.MeanRankUpdate.scaleDebt`: reachable through `13` compiled edges
- `NavierStokes.DefectIncrementBounds.barMoment`: reachable through `16` compiled edges
- `NavierStokesR3.ProblemStatement.CandidateProperties`: reachable through `1` compiled edges

## Interpretation boundary

The route results show compiled reachability, not the value-level transport of a mathematical invariant. A missing value theorem remains an open correspondence obligation even when every upstream module is reachable.

Tree reconciliation is intentionally reported separately: a missing or ambiguous inventory basename is a snapshot reconciliation issue, not evidence that a Lean module or theorem is absent.

## Reproduction

Run `NavierStokesReview/src/audit/run_hardened_audit.ps1`; it regenerates the source map and compiled environment export before this bundle is rebuilt.
