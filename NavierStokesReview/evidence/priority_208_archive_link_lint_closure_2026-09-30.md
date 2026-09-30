# Priority 208: archive-link and structural-lint closure

Date: 2026-09-30

## Scope

This tranche records the corrected non-mutating documentation-control audit
after two archived manuscript artefacts were found to retain links relative to
their former `docs/` location. It does not make a mathematical claim about the
Navier--Stokes construction and does not alter `CTR-005`.

## Checks and results

| Check | Scope | Result |
| --- | --- | --- |
| Markdown relative-link resolution | `docs/`, `NavierStokesReview/evidence/`, `results/`, and `src/` | 415 Markdown files checked; 0 broken targets |
| Evidence JSON parsing | `NavierStokesReview/evidence/*.json` | 98 files checked; 0 parse failures |
| Archive manifest verification | All 5 manifest rows with archive paths | 0 missing files; 0 SHA-256 mismatches |
| Protected-source boundary | `NavierStokes/R3/TestPressure.lean` | Present and unchanged; excluded from review staging |

The Markdown checker excludes external URLs, mail links, plugin links, and
mathematical bracket notation such as `B_k[g](j,p)`. It resolves every local
relative target against the directory containing the Markdown file. The two
archived manuscript files were repaired by changing only relocation-relative
paths. Their post-repair hashes are recorded in
`docs/archive/ARCHIVE_MANIFEST_2026-09-30.md`.

## Remaining gate

The structural link/lint gate is now closed for this pass. The broader archive
gate remains open because document-by-document consolidation, cross-reference,
and source fact-checking are still required before any further archive move.
No deletion, bulk staging, OpenAI-source edit, or protected-file movement was
performed.

## Scientific disposition

This tranche provides no new theorem. The controlled finding remains
`CTR-005: NOT ESTABLISHED`: the inspected selected production closure contains
real internal invariant, physical-data, residual-rate, force-extension, and
axis blow-up machinery, but no inspected production declaration identifies the
completed selected Cartesian observables with `(M,I,J,S,C_p)`. This remains a
bounded correspondence finding, not a proof of selected mismatch, force
nonsmoothness, literal CMI failure, impossibility, compiler escape, or `False`.
