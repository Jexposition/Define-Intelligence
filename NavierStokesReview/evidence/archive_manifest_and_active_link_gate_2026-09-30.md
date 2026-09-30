# Archive Manifest and Active-Link Gate

## Scope

This record covers the non-destructive documentation gate completed on
2026-09-30. It checks archive-manifest coverage, SHA-256 stability, active
Markdown references, and the protected-worktree boundary. It is a repository
hygiene record, not a new mathematical result.

## Archive inventory

`docs/archive/` contains one manifest and four archived artefacts. The manifest
records the four artefacts and their hashes. The current hashes were recomputed
from the private worktree and agree with the manifest.

No file was deleted or moved during this gate. No further archive movement is
authorised until the full document-by-document consolidation and cross-check
is complete.

## Active Markdown-link check

The current active tree contains 382 Markdown files and 62,677 parsed link
targets when `docs/archive/` and `.lake/` are excluded. The nine stale
`../NavierStokesReview/...` references in
`research_paper_evidence_dossier_2026-09-30.md` were repaired to paths relative
to its actual `NavierStokesReview/evidence/` location. The two remaining
lexical hits in the conservative checker are LaTeX tokens (`j,p` and `t`), not
Markdown links. Four apparent links in the semantic crosswalk use valid
angle-bracket absolute Windows paths; the checker had truncated them at the
space in `D:/Research Lab` and therefore reported false positives.

The resulting manual disposition is: zero confirmed broken active links in
the repaired tranche. This is not a claim that all prose has been semantically
fact-checked; it only establishes the path-integrity gate for the current
active documents.

## Protected source and release state

The only private untracked path remains
`NavierStokes/R3/TestPressure.lean`. It is protected, untouched, unstaged,
unmoved, and excluded from the archive and review commits. No Lean, Lake,
Elan, Git, or dotnet build process was running in the final process check.

Private commit: `2979784` (`Complete archive manifest inventory`).

Public mirror commit: `104b641` (`Complete archive manifest inventory`), pushed
to `review/cmi-first-navier-stokes-disposition-public-2026-09-30`.

## Scientific disposition unchanged

The active audit remains `CTR-005: NOT ESTABLISHED` for complete
paper-to-selected-endpoint correspondence. The source record still supports
genuine internal moment/debt invariants and a connected residual-rate,
force-limit, and axis-blow-up route. It does not establish a final selected
Cartesian identity with `(M,I,J,S,C_p)`, and it does not establish a selected
nonzero defect, force nonsmoothness, literal CMI failure, impossibility,
compiler cheat, or `False`.
