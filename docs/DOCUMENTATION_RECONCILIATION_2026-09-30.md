# Documentation reconciliation: 2026-09-30

**Status:** active consolidation ledger; disposition executed without deletion

This ledger was created after a source-first read of the controlling documents,
the review paper, the CMI crosswalk, the semantic maps, the bridge audits, the
full register mirrors, the evidence tree, the audit tree, and the latest source
tranches through Priority 198. It is a navigation and state-control document.
It does not replace raw Lean source or the frozen source texts.

## Post-disposition workspace state

The pre-disposition inventory has been reconciled. Thirty-six artefacts were
moved non-destructively to parent-folder archives, with original hashes and
old/new paths recorded in the archive manifests. The disposition ledger has
29 rows, controlled by
`NavierStokesReview/evidence/untracked_disposition_manifest_2026-09-30.json`:
24 retained for scoped staging, 3 archive-confirmed, 1 held for provenance
review, and 1 protected OpenAI-source file. These are ledger rows, not a count
of current Git-untracked paths. Git currently reports one untracked path only:
NavierStokes/R3/TestPressure.lean, which is protected and must not be edited,
staged, moved, or archived. No deletion occurred. The evidence
archive manifest is intentionally ignored by the broad repository ignore rule
and must be force-staged explicitly if included in a scoped documentation
commit.

## Effective authority snapshot

The effective machine-readable register is now:

`NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-30.json`

The matching root mirror is:

`docs/REPOSITORY_SEMANTIC_COVERAGE_REGISTER.json`

The current counts are:

| Metric | Current value | Interpretation |
| --- | ---: | --- |
| Indexed Lean modules | 2,797 | Repository inventory in the current register scope |
| Captured endpoint modules | 588 | Membership in the captured `NavierStokes.R3.Theorem` closure only |
| Rows outside selected closure | 2,209 | Outside the chosen audit roots; not a dead-code claim |
| Evidence-inspected rows | 906 | Register rows with an evidence inspection record |
| Source-indexed rows queued | 1,884 | Rows not yet semantically classified at declaration level |
| Missing project import edges | 0 | Import-resolution diagnostic |
| Supplemental evidence records | 86 | Additional review-side records |
| Source rows containing a `sorry` token | 10 | Register field `source_rows_with_sorry_token` |

The register's nested status field reports seven `source_indexed_sorry_token`
rows while its top-level source-row field reports ten. This is now reconciled:
three of the ten lexical rows are already `evidence_inspected`, so `10 = 7 + 3`.

## Findings that are currently locked

These are the findings supported by the latest source records. They are not
being replaced by older challenge documents or by the absence of a named field
in one proposition.

1. The manuscript treats `(M,I,J,S,C_p)` as substantive profile, matching,
   correction, stress, and pressure data. They are not optional notation.
2. Raw Lean tracing shows that profile/rank machinery feeds coefficient
   matching, finite Cartesian residual identities, residual-rate estimates,
   selected physical data, and the selected residual/force route. The earlier
   blanket statement that moment restoration is absent from the selected proof
   is withdrawn.
3. The inspected `ActualCandidateAssembly.Witness` contract does not export a
   named theorem identifying the completed selected Cartesian fields and their
   pressure/residual data with the manuscript's final five observables. This is
   the current `CTR-005` correspondence gap.
4. The selected force-smoothness route is not currently shown to be an
   arbitrary `NativeBounds` assumption. The source path derives actual residual
   rates, vanishing jets, recurrence/limit data, and a smooth force extension.
5. The abstract non-implication probes show a limitation of the public
   contract. They do not show that the concrete selected field has nonzero
   physical moment debt.
6. The manuscript's four coupled residual-control operations prevent the
   stronger claim that the five equations are the sole cancellation mechanism.
   Likewise, velocity blow-up does not imply termwise divergence of every
   residual summand.
7. The connected comparator path contains a substantive encoded forced CMI
   proposition on the inspected route. Complete manuscript-to-selected-field
   fidelity remains **NOT ESTABLISHED (`CTR-005`)**. No selected mismatch,
   impossibility theorem, failed connected CMI condition, or kernel-level
   `False` is recorded.
8. The CUDA 3D cutoff diagnostic is retained as profile-level numerical
   evidence. It is not evidence about the selected Lean `tsum` field until the
   exact field and observable are bound.
9. `ProblemStatement.CandidateProperties` is a real endpoint contract: it
   includes smooth velocity, pressure, and force, residual equality on
   (0<t<1), incompressibility, support, and speed unboundedness. Therefore
   the audit must not say that the selected blow-up is absent merely because
   the final five-observable identification is absent. The precise finding is
   that this endpoint contract does not identify those proved fields and
   residual data with the manuscript's transported `(M,I,J,S,C_p)` mechanism.
10. The 2026-09-30 replay of `WholeSpaceAxiomAudit.lean` reports only
     `propext`, `Classical.choice`, and `Quot.sound` for the queried whole-space
     and periodic endpoints. This is an axiom-footprint result, not evidence
     that the complete manuscript correspondence is proved.

11. Priority 209 resolves the inventory scope. The current whole-checkout
    register has 2,797 rows, the direct `NavierStokes/` source census has 817
    files, and the review-side Lean census has 137 files. The Priority 201
    `repository_lean_files: 2796` value is retained as a historical snapshot,
    not a current headline count.

## Historical counts and supersession rule

The following are historical snapshots, not current counts:

| Artefact | Historical state | Treatment |
| --- | --- | --- |
| `semantic_coverage_register_full_2026-09-27.*` | 2,790 indexed; 588 captured; 903 inspected; 1,880 queued | Retain as dated evidence |
| `semantic_coverage_register_full_2026-09-28.*` | 2,794 indexed; 588 captured; 757 inspected; 2,030 queued | Retain as dated evidence |
| Older sections of `SEMANTIC_CORRESPONDENCE_MAP.md` | Multiple earlier tranche counts | Retain chronology; do not quote as live state |
| Older sections of `REVIEW_DOCUMENT_CONTROL.md` | 2,792 and earlier states | Retain chronology; current header controls |

Historical material is not deleted. Any future archive move requires a
cross-reference, a parent-folder manifest, the old and new paths, a reason,
and the original SHA-256.

## Historical tree-index drift and current control

The tree files are navigation aids, but they currently omit live files:

- `docs/doc_tree.md` omits current source PDFs/text mirrors, `navierstokes.md`,
  the two tree inventories, and the archive entries.
- `NavierStokesReview/evidence/evidence_tree.md` omits current build logs,
  Priority 185 evidence, several Priority 186–198 JSON records, the selected
  operator trace, and the consolidation ledgers.
- `NavierStokesReview/src/audit/audit_tree.md` omits the Priority 145–163
  source reviews, Priority 185, the direct-closure scripts, and the current
  consolidation utility.

These were index defects in the historical snapshots, not evidence that the
omitted files are dead. Priority 209 patched the current appendices and linked
the regenerated source map/register. The older omission lists remain below as
provenance; the current register and source map, not basename snapshots,
control scope and reachability.

## Remaining reconciliation order

1. Continue document-by-document consolidation and source-first fact-checking
   of the active manuscript, peer review, evidence dossier, and audit records.
2. Keep current tree appendices and generated registers synchronized whenever
   new review artefacts are added.
3. Keep the 2,797/817/137/588 scope table and the ten-versus-seven lexical
   status distinction synchronized with generated outputs.
4. Keep the protected `NavierStokes/R3/TestPressure.lean` outside all commits,
   archive moves, and source edits.
5. Only after the consolidation gate is complete may a further non-destructive
   archive move be considered, with a parent-folder SHA-256 manifest. Never
   stage the entire worktree.

## Historical untracked-file control snapshot: 2026-09-30

The following 61-entry snapshot is retained for provenance and is superseded
by the 29-row disposition matrix described above. It must not be read as the
current Git state.

The pre-disposition private worktree contained 61 untracked path entries. They
were not one commit set:

| Class | Count | Control decision |
|---|---:|---|
| `NavierStokesReview/evidence/` | 54 | Retain for evidence triage; do not bulk-stage. Current registers and source tranches require separate review from diagnostic scans and build logs. |
| `docs/` | 5 | Review against this reconciliation and the document-control map before any commit or archive move. The quarantined final-falsification draft is historical intake only. |
| Protected OpenAI tree | 1 | `NavierStokes/R3/TestPressure.lean`; do not edit, stage, move, or archive. |
| Other/root entries | 2 | Hold outside the formal commit until their exact paths and provenance are verified. |

The untracked set therefore remains intentionally uncommitted. A quoted path
reported by Git required exact filename verification before any filesystem
operation. The later disposition moved 36 artefacts without deletion; the
current worktree has only the protected `NavierStokes/R3/TestPressure.lean`
row untracked.

## Historical manual tranche update: CUDA diagnostics and controlled build records

The manual-review ledger now covers 35 of the 61 held entries, leaving 26
entries for the next tranche. The newly reviewed build pair records a
successful 9,350-job build ending at
`NavierStokes.R3.Theorem`; the paired error stream is empty. This confirms a
successful build record, not complete correspondence with the manuscript.

The newly reviewed `cutoff_commutator_debug`, `debug2`, and `debug3` families
are retained as CUDA-backed 3D profile diagnostics. Their source bindings
reconstruct the declared `SpatialLocalization` cutoff and Cartesian curl, and
their plots show a resolved annular commutator for the declared diagnostic
profile. Their own JSON validation records `selected_delta_m_proved: false`
and `selected_field_bound: false`. They therefore cannot be promoted to a
selected-field mismatch, a formal nonzero \(\Delta m\), or a CMI failure.

The follow-up tranche also reviewed the resolved `deep` sweep, the lower-
resolution `deep_test`, the high-resolution profile scan, and the full-source
route scan. The numerical records still have `selected_delta_m_proved: false`
or `selected_field_bound: false`; the source scan is lexical triage, not a
transport theorem. Evidence and hashes are recorded in
`NavierStokesReview/evidence/latest_rebuttal_manual_review_tranche_2026-09-30.md`.
At that historical checkpoint, all 61 entries remained
`HOLD_NO_STAGE_NO_MOVE`; the manual content-review gate had 0 remaining
entries. The later disposition matrix supersedes that hold without deleting
any artefact.

## Source anchors

- `docs/REVIEW_DOCUMENT_CONTROL.md`
- `docs/REVIEW_AUDIT_WORKSPACE_GOAL.md`
- `docs/OpenAI_NavierStokes_CMI_First_Review_Plan.md`
- `docs/OpenAI_NavierStokes_Peer_Review_v1.md`
- `docs/OpenAI_NavierStokes_Research_Paper.md`
- `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`
- `NavierStokesReview/src/audit/priority_186_fefferman_full_word_connection_closure_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_187_circularity_adjudication_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_188_connected_cmi_compliance_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_189_openai_physical_wording_source_check_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_194_residual_cancellation_and_endpoint_adjudication_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_195_four_operation_force_smoothness_adjudication_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_198_latest_rebuttal_adjudication_2026-09-30.md`
- `NavierStokesReview/evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md`
- `NavierStokesReview/src/audit/priority_199_selected_endpoint_declaration_crosscheck_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_200_connected_cmi_manuscript_crosswalk_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_201_selected_closure_census_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_202_actual_moment_invariant_trace_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_203_internal_to_endpoint_crossfile_trace_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_204_workspace_source_record_reconciliation_2026-09-30.md`
- `NavierStokesReview/evidence/latest_rebuttal_manual_review_tranche_2026-09-30.md`

## Authoritative workspace checkpoint: 2026-09-30 continuation

This checkpoint records the full documentation pass across `docs/`, the CMI
and manuscript source mirrors, the review evidence and results trees, the
audit/source indexes, the probe, completion, extension, refutation, and
external-semantic folders, and `scratch_space/notes3.md` and
`scratch_space/notes4.md`. The scratch notes are historical task-intake
material. They do not override raw Lean source or the current Priority
198--204 source adjudications. Their CUDA/3D diagnostics remain
declared-profile evidence, not selected-field theorems.

The current scientific record is two-sided. The actual selected cycle has two
preserved mean-mass identities and three residual-debt classes. Those data
feed physical data, residual-rate estimates, residual limits, force extension,
candidate consequences, and the axis blow-up route. The inspected selected
closure still has no located production declaration identifying the completed
Cartesian, localised, periodised, summed fields, pressure, residual, and force
with the manuscript's named `(M,I,J,S,C_p)` observables. The controlled status
remains `CTR-005: NOT ESTABLISHED` for complete
manuscript-to-selected-endpoint correspondence. This does not prove a
selected nonzero defect, force nonsmoothness, literal forced-CMI failure,
impossibility theorem, compiler escape, or `False`.

The live Git state is explicit. The private branch is
`review/cmi-first-navier-stokes-reconciled-2026-09-30`; its local tip is
verified by Git, but its push was not confirmed after two timed-out attempts.
The public
mirror branch is
`review/cmi-first-navier-stokes-disposition-public-2026-09-30`; its remote tip
is verified by Git and its push is confirmed. The private worktree contains exactly one
untracked protected file, `NavierStokes/R3/TestPressure.lean`; it has not been
edited or staged. No OpenAI source file is part of the review tranche.

The next gates are ordered: record or resolve the private push state; complete
the live cross-reference and structural-lint pass; prepare only a scoped
review commit; and only then consider further archive moves. Any archive move
must be non-destructive and manifested with old path, new path, reason, and
SHA-256. No deletion is permitted.

## Live untracked-state reconciliation: 2026-09-30

The regenerated read-only inventory and consolidation matrix now describe the
current private worktree, not the historical review tranche. They contain one
live untracked path: the protected `NavierStokes/R3/TestPressure.lean` file.
Its hash is current and verified. The 29-row disposition manifest and the
older 61-entry hold remain historical content-addressed records of earlier
review states; neither is a count of the current worktree and neither
authorises staging, movement, or deletion.

Current generated records:

- `NavierStokesReview/evidence/untracked_content_inventory_2026-09-30.json`
- `NavierStokesReview/evidence/untracked_content_inventory_2026-09-30.md`
- `NavierStokesReview/evidence/untracked_consolidation_matrix_2026-09-30.json`
- `NavierStokesReview/evidence/untracked_consolidation_matrix_2026-09-30.md`

The protected file remains outside every review commit and archive operation.

## Scope and tree-index reconciliation: Priority 209 (2026-09-30)

The current source replay resolved the earlier count drift. The regenerated
root-explicit source map and semantic register now report 2,797 Lean files,
588 modules in the selected endpoint closure, and 2,209 rows outside that
closure. A direct `NavierStokes/` census reports 817 files; the review-side
Lean census reports 137 files. These are distinct scopes and must not be
quoted as interchangeable totals.

The prior 2,794-row register omitted exactly three newer review-side Lean
files and included the protected `NavierStokes/R3/TestPressure.lean`. The
current register includes all 2,797 paths. The historical Priority 201 field
`repository_lean_files = 2796` is retained as a snapshot value and is
superseded for current totals by Priority 209.

The lexical ten-versus-seven `sorry_token` discrepancy is also resolved:
ten rows contain the token, seven carry the specific source-indexed status,
and three already have `evidence_inspected` status. Thus `10 = 7 + 3`.

Control records:

- `NavierStokesReview/evidence/source_tranche_priority_209_scope_and_index_reconciliation_2026-09-30.json`
- `NavierStokesReview/evidence/priority_209_scope_and_index_reconciliation_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_209_scope_and_index_reconciliation_2026-09-30.md`
- `NavierStokesReview/evidence/hardened_source_map_2026-09-30.json`

This is a bookkeeping and navigation correction only. `CTR-005` remains
`NOT ESTABLISHED`; no selected defect, force nonsmoothness, literal CMI
failure, impossibility, compiler escape, or `False` is inferred.
