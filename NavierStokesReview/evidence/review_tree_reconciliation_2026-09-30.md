# NavierStokesReview tree reconciliation

This is a read-only reconciliation of the four navigation indexes against the
current checkout. It is bookkeeping evidence, not a semantic coverage claim.
The indexes are navigation aids; the dated evidence registers and source
reviews remain authoritative for scientific findings. Generated caches are
excluded from the comparison. The counts below are the pre-disposition
snapshot. After reconciliation, 36 artefacts were moved non-destructively to
parent-folder archives; no file was deleted. See
`evidence/archive/ARCHIVE_MANIFEST_2026-09-30.md` and
`evidence/untracked_disposition_manifest_2026-09-30.json`.

## Snapshot counts

| Area | Current files | Index entries | Current files not represented by index basename | Index basenames absent from current files |
|---|---:|---:|---:|---:|
| `evidence` | 314 | 295 | 25 | 6 |
| `results` | 48 | 47 | 1 | 0 |
| `src` | 309 | 298 | 34 | 23 |
| `src/audit` | 170 | 176 | 17 | 23 |

The apparent overlap between the `src` and `src/audit` rows is expected: the
top-level `src_tree.md` and the nested `audit_tree.md` use different historical
tree snapshots, and the comparison is deliberately basename-based. It must not
be read as a theorem or import-graph result.

## Evidence files not represented in `evidence_tree.md`

These are current files whose basenames were absent from the tree snapshot:

- `evidence/hardened_source_map_2026-09-29.json`
- `evidence/hardened_source_map_2026-09-29.md`
- `evidence/paper_moment_dependency_matrix_2026-09-29.md`
- `evidence/physical_projection_equivalence_adjudication_2026-09-29.md`
- `evidence/profile_moment_selected_path_adjudication_2026-09-29.md`
- `evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md`
- `evidence/selected_field_operator_trace_2026-09-29.md`
- `evidence/source_tranche_barmoment_correction_state_vs_selected_field_2026-09-29.json`
- `evidence/source_tranche_euler_cylinder_dirichlet_endpoint_2026-09-29.json`
- `evidence/source_tranche_euler_cylinder_endpoint_graph_2026-09-29.json`
- `evidence/source_tranche_euler_cylinder_graph_path_support_2026-09-29.json`
- `evidence/source_tranche_euler_cylinder_slow_curl_sobolev_2026-09-29.json`
- `evidence/source_tranche_euler_cylinder_tensor_scalar_2026-09-29.json`
- `evidence/source_tranche_euler_finite_grade_endpoint_2026-09-29.json`
- `evidence/source_tranche_euler_gaussian_gevrey_2026-09-29.json`
- `evidence/source_tranche_euler_mean_development_heat_duhamel_2026-09-29.json`
- `evidence/source_tranche_euler_packet_recursive_2026-09-29.json`
- `evidence/source_tranche_euler_transport_frame_heat_2026-09-29.json`
- `evidence/source_tranche_external_semantic_euler_drift_pressure_2026-09-29.json`
- `evidence/source_tranche_full_cmi_dependency_crosswalk_2026-09-29.json`
- `evidence/source_tranche_priority_185_rebuttal_adjudication_2026-09-30.json`
- `evidence/source_tranche_rebuttal_force_smoothness_moment_boundary_2026-09-29.json`
- `evidence/untracked_consolidation_matrix_2026-09-30.json`
- `evidence/untracked_consolidation_matrix_2026-09-30.md`

`evidence/evidence_tree.md` itself is excluded as the index under test.

## Source and audit review files not represented by the current indexes

The following review records are present under `src/audit` but are absent from
the older source-tree snapshot. They must remain discoverable even though the
tree itself is not the authority:

- `priority_145_euler_cylinder_dirichlet_endpoint_source_review_2026-09-29.md`
- `priority_146_euler_cylinder_endpoint_graph_source_review_2026-09-29.md`
- `priority_147_external_semantic_euler_drift_pressure_source_review_2026-09-29.md`
- `priority_148_euler_cylinder_graph_path_support_source_review_2026-09-29.md`
- `priority_149_euler_cylinder_tensor_scalar_source_review_2026-09-29.md`
- `priority_150_euler_cylinder_slow_curl_sobolev_source_review_2026-09-29.md`
- `priority_151_euler_mean_development_heat_duhamel_source_review_2026-09-29.md`
- `priority_152_euler_packet_recursive_source_review_2026-09-29.md`
- `priority_153_euler_finite_grade_endpoint_source_review_2026-09-29.md`
- `priority_154_euler_transport_frame_heat_source_review_2026-09-29.md`
- `priority_155_euler_gaussian_gevrey_source_review_2026-09-29.md`
- `priority_161_rebuttal_force_smoothness_moment_boundary_adjudication_2026-09-29.md`
- `priority_162_barmoment_correction_state_vs_selected_field_source_review_2026-09-29.md`
- `priority_163_full_cmi_dependency_crosswalk_adjudication_2026-09-29.md`
- `priority_179_fefferman_full_semantic_dependency_network_2026-09-29.md`
- `priority_179_latest_force_smoothness_rebuttal_2026-09-29.md`
- `priority_180_selected_field_boundary_rebuttal_adjudication_2026-09-29.md`
- `priority_181_global_barmoment_integrability_gate_2026-09-29.md`
- `priority_182_fefferman_semantic_word_to_condition_closure_2026-09-29.md`
- `priority_183_force_smoothness_moment_rebuttal_adjudication_2026-09-29.md`
- `priority_184_selected_path_foundation_audit_2026-09-29.md`
- `priority_185_rebuttal_adjudication_2026-09-30.md`
- `priority_186_fefferman_full_word_connection_closure_2026-09-30.md`
- `priority_187_circularity_adjudication_2026-09-30.md`
- `priority_188_connected_cmi_compliance_2026-09-30.md`
- `priority_189_openai_physical_wording_source_check_2026-09-30.md`
- `priority_190_connected_cmi_revalidation_2026-09-30.md`
- `priority_193_fefferman_semantic_branch_network_2026-09-30.md`
- `priority_194_residual_cancellation_and_endpoint_adjudication_2026-09-30.md`
- `priority_195_four_operation_force_smoothness_adjudication_2026-09-30.md`
- `priority_198_latest_rebuttal_adjudication_2026-09-30.md`
- `untracked_consolidation_matrix.py`
- `untracked_content_inventory.py`

The same records are current members of `src/audit`; the nested index is also
behind for the 145–163, 185, and later reconciliation tranche.

## Disposition

1. Keep all current files in place.
2. Treat the four tree files as historical navigation snapshots until a
   deliberate regeneration is reviewed.
3. Use this reconciliation plus the evidence register to prevent a file from
   disappearing from the audit simply because an index was not regenerated.
4. Do not interpret a tree omission as unreachable code, dead code, or absence
   of a theorem. Reachability remains an endpoint-import question and semantic
   transport remains a separate theorem-level question.

Linked control records:

- `docs/DOCUMENTATION_RECONCILIATION_2026-09-30.md`
- `evidence/latest_rebuttal_manual_review_tranche_2026-09-30.md`
- `evidence/untracked_consolidation_matrix_2026-09-30.md`
- `evidence/semantic_coverage_register_full_2026-09-29.json`
