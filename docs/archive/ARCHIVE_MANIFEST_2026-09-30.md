# Archive manifest: research-paper consolidation

**Date:** 2026-09-30
**Operation:** split the publication manuscript from its preserved audit dossier
**Deletion:** none

## Source preservation

The pre-consolidation file was copied byte-for-byte before the working path was
rewritten. The archive copy is the recovery source for every line removed from
the publication path:

| Original path | Archived path | Reason | SHA-256 |
|---|---|---|---|
| `docs/OpenAI_NavierStokes_Research_Paper.md` | `docs/archive/OpenAI_NavierStokes_Research_Paper_with_dossier_2026-09-30.md` | Preserve the complete pre-consolidation manuscript and audit dossier | `427A24E6DCEA70ECA9C1AEA07F008FFA806E5ACB0A6E592F94A04D4012F9EA49` |

The archived source contains 4,923 lines. Its original byte content remains
recoverable and was not deleted.

## Consolidated outputs

| Output | Scope | SHA-256 |
|---|---|---|
| `docs/OpenAI_NavierStokes_Research_Paper.md` | Publication argument, source-grounded findings, references, and appendices | `C0500C06F09FF6DD14FB9FA0182B12A50868AF0436905384BC5E82BA80DEACD0` |
| `NavierStokesReview/evidence/research_paper_evidence_dossier_2026-09-30.md` | Preserved audit-control record and source dossier extracted from the manuscript | `71371134CBC5E47D34EFCE18BAB25D678B48DD6D7149658F8C27840063B39810` |

The formal manuscript retains the publication-level argument only. The evidence
dossier remains active under `NavierStokesReview/evidence`, where its source
reviews and machine-readable ledgers belong. The archive copy is retained for
byte-level recovery and provenance comparison.

## Boundary verification

The archived source was split at two explicit structural boundaries:

- original lines 1--76 and 180--1,320 form the publication argument;
- original lines 77--179 and 1,321--4,923 form the preserved audit dossier.

The current manuscript links the dossier rather than embedding it. No evidence
claim was silently deleted or downgraded. Any future archive move must add a new
manifest entry with the old path, new path, reason, and SHA-256.
