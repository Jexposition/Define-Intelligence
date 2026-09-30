# Latest rebuttal manual-review tranche

Date: 2026-09-30
Status: reviewed; no staging or archive move authorised by this ledger alone

This tranche records source review of the complete 61-entry untracked corpus.
The files remain in place and remain on `HOLD_NO_STAGE_NO_MOVE`; completing
content review does not authorise staging, archiving, moving, or deletion.
All 61 entries are now reviewed, with the document-level cross-reference and
release gate still outstanding.

## Reviewed artefacts

| Artefact | SHA-256 | Review result | Disposition gate |
| --- | --- | --- | --- |
| `evidence/selected_transport_audit_2026-09-28.md` | `c34bb2f8d61372c1e1c7890b71c08e3fd052b3e5ffcaef93e638f869b9a6fec6` | Retain as selected-path audit; correctly distinguishes candidate declarations from a transport proof | `RETAIN_PENDING_FINAL_CROSSREF` |
| `evidence/selected_transport_bridge_inventory_2026-09-27.md` | `bbaf99d854234298242c175318092c597a5a591bea88f78425b9cd550aef0bfd` | Retain as endpoint boundary evidence; supports CTR-005 without proving a mismatch | `RETAIN_PENDING_FINAL_CROSSREF` |
| `evidence/selected_endpoint_source_census_2026-09-27.md` | `6aebb21e85ad42a1c4aa47dfdd02706fed50e422ef6f1218fc3bd9be16d30bec` | Retain as lexical census; its own interpretation boundary correctly rejects lexical co-occurrence as transport proof | `RETAIN_PENDING_FINAL_CROSSREF` |
| `evidence/global_cross_layer_audit_2026-09-27.md` | `dcc6aa215b49ae97f3f27c9d157cf9a86bfee634702325a6398fb91bff16b1d0` | Retain as source-to-claim ledger; endpoint is real but narrower than the full manuscript chain | `RETAIN_PENDING_FINAL_CROSSREF` |
| `evidence/reachable_moment_transport_declarations_2026-09-27.txt` | `e7c8e908f8868adc63ab511f71c515dd6eee349a4aa86786d61475052f92eb3f` | Retain as search output only; declarations require body-level review and do not establish final transport by name | `RETAIN_AS_TRIAGE_ONLY` |
| `evidence/claim_cross_examination_2026-09-27.md` | `4e4245fa076ff0ea6b4547b92573eb28464265939f6b6855cdb843f441f5f46e` | Retain as calibrated cross-examination; rejects both dead-code and concrete-zero-field overclaims | `RETAIN_PENDING_FINAL_CROSSREF` |
| `evidence/cutoff_commutator_deep_2026-09-27.md` | `65232e9179cbdfff92885da415f99a75e814d7e236595be0d6f027697ac4b44b` | Retain as a 3D numerical diagnostic; not evidence about the selected Lean `tsum` field or a formal \(\Delta m\ne0\) theorem | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/hardened_source_map_2026-09-27.md` | `e615f33a63103538cb90735f38f580c7193a38f9437cfa3dd79883b6c467f433` | Retain as closure metadata; source-token edges remain diagnostic until environment declaration closure is independently checked | `RETAIN_PENDING_ENV_CHECK` |
| `docs/OpenAI_NavierStokes_Final_Falsification_Report.md` | `d9fc1cfbe2c6805af13b697e15ca2f71d367f76d83a0972a91800cbf1d3ac813` | Retain as quarantined historical intake only; its header withdraws the blanket “never transported” claim, but the body still repeats that superseded claim and must not be cited as current evidence | `QUARANTINE_NO_STAGE_NO_MOVE` |
| `evidence/controlled_build_Theorem_2026-09-28.log` | `46f8b6c782c67f1bbe8f689e62c5e1dc98858721a5a3076b8689d8b821c263f8` | Successful 9,350-job build log ending at `NavierStokes.R3.Theorem`; confirms compilation only, not manuscript-level correspondence | `RETAIN_BUILD_RECORD_PENDING_FINAL_CROSSREF` |
| `evidence/controlled_build_Theorem_2026-09-28.err.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Empty error stream; useful as a paired build record, not mathematical evidence | `RETAIN_BUILD_RECORD_PENDING_FINAL_CROSSREF` |
| `evidence/cutoff_commutator_debug2_2026-09-27.md` | `3652659307b2ce4ecd2fafaaf40d61a4ef9e511bae5c0f601e2c06e38991ccd8` | CUDA 3D diagnostic reconstructed the source cutoff and reports nonzero profile defect, but explicitly says it is not `selected_witness` evaluation and does not prove selected Δm | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug2_2026-09-27.json` | `4bb6076c97fabaa9ec46107e14f7e034e93f63f9495f5eae32523cc031c898db` | Machine-readable companion to debug2; records `selected_delta_m_proved: false` and GPU provenance | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug2_2026-09-27.png` | `2b528c6fe3e555b9a73c476a8d7164fda7a64a13cacadf6cff1983d26edabd64` | Plot visually confirms the annular commutator pattern for the declared profile; it is not a selected-field proof | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug3_2026-09-27.csv` | `4b8c7a30d393e2186ce6ff8627ccbe8702b88f164288034076f66a5ca549fbef` | Refinement data for the CUDA profile diagnostic; numerical convergence record only | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug3_2026-09-27.json` | `9599b0ab0e3e4ed3f33414d429538c42525ac91c28dcb777972ca6f04ae26988` | Four-resolution companion record; stable profile defect, but selected-field binding and formal Δm remain false | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug3_2026-09-27.md` | `870e5bebc7f624595080862162f181c70082e35e826d3d75cf538938c1c2d9c7` | Higher-resolution CUDA profile diagnostic; source reconstruction is explicit, endpoint transport is explicitly out of scope | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug3_2026-09-27.png` | `8e06b8bf331c96d1f705e469e60e70d2e344f2d9d9b278557df530264623c959` | Plot companion for debug3; visualises the declared cutoff defect, not the selected Lean field | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug_2026-09-27.csv` | `cb2d7dded91df8ab9a740b2d4833fb581d9e9a275df005f4a6d33f73850cb0b5` | Earlier low-resolution refinement data; useful provenance but weaker derivative resolution than debug3/deep | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug_2026-09-27.json` | `d55a056a18b4c76b332b47cc3163ebe3a7626ac04b3ec99590f8c61855e250f1` | Earlier companion record; records large finite-difference errors and no selected-field conclusion | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug_2026-09-27.md` | `e04390654930868b68a35cd6adbfcbcf6d0c4c9dface4688952ede9019ee35dd` | Earlier CUDA profile diagnostic; retained for reproducibility history, not promoted as endpoint evidence | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_debug_2026-09-27.png` | `99c371c42053faeb8fb4087a1cb0e846ed18d2e5008d5c3d90f95b2cf0cb402f` | Earlier plot companion; visual diagnostic only and superseded in resolution by debug3/deep | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_deep_2026-09-27.csv` | `06c5bc489ce8df3030f71ca322291834a05b0c70dd8d00a1df17a3d50ccee615` | Resolution-sweep data for the 3D CUDA profile diagnostic; stable profile behaviour, but no selected-field binding or formal Δm result | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_deep_2026-09-27.json` | `354e4df204eefc8910348af516a62f97095d0b71036b14f1495a89c3283e0f34` | Machine-readable deep-sweep record; explicitly records `selected_delta_m_proved: false` and `selected_field_bound: false` | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_deep_2026-09-27.png` | `a3c4ef623c04aa4bd549a36f1fa41b40d7d69e6e38297e6dc991f1b3d0219073` | Plot companion for the resolved 3D profile diagnostic; visual evidence is confined to the declared source profile and annular commutator | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_deep_test.csv` | `f2448f7634d049bd12e2ac2f42b2b4d95177f752e3bb968c3f57e82f0475569b` | Lower-resolution exploratory CUDA data; retained for reproducibility history because its finite-difference errors are materially larger | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_deep_test.json` | `d1b714ca7a2b562078a9fbef636af53e5d094b131dbc132782c8f08c1bb2668b` | Exploratory companion record; no selected-field binding and no formal transport conclusion | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_deep_test.md` | `111dcbc842264d0bedd1fdcafb2cb07d0ec3a4da95d180ec55e66a2f779556eb` | Exploratory report; useful to explain why the deeper resolved run is preferred over this lower-resolution run | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_deep_test.png` | `cff7e5b4717cb079eb114201ab3bce6c306ac98abec0a2e21c76888e3ef9feec` | Exploratory plot companion; not evidence about the selected Lean field | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_profile_scan_2026-09-27.csv` | `731b6ff6540942c9b01f7b4107b23b2e80c235707d32d179783ef33c6fe8d078` | High-resolution 1D profile-scan data across radii and grid sizes; demonstrates cutoff-tail dependence only for the declared Gaussian profile | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_profile_scan_2026-09-27.json` | `4e6e2eb90a0cc14260346c7a62f55ff3f32055a197b8beda9f7b8beb633b366c` | CPU/GPU and product-rule checks agree numerically, but `selected_field_bound` remains false; not a Lean endpoint result | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_profile_scan_2026-09-27.md` | `fe718cea432181c185df1890985e76efdd281782dce9bd3966d780cdc8a8bc85` | Profile-level report; documents the declared model and explicitly keeps it separate from `selected_witness` | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_profile_2026-09-27.png` | `42ccfc2607b6029d111efa102630535b90cc8b88f66c6c72a9be920d894e033a` | Plot companion for the profile scan; retained as a visual diagnostic, not a selected-field plot | `RETAIN_DIAGNOSTIC_ONLY` |
| `evidence/cutoff_commutator_source_scan_2026-09-27.json` | `9a6479866e680d358fb9c9a1ccba685528b58d6b5e40c0c9e5e0bce240e9d11c` | Full-source lexical census and active-closure route scan; it finds route symbols but no proof of final five-moment transport | `RETAIN_AS_TRIAGE_ONLY` |
| `evidence/cutoff_commutator_source_scan_2026-09-27.md` | `f03ecf85d76f134eaea0f816fd75ff68fc2c0f232eaa53a3c9d9aa1dd64d05d2` | Source-scan interpretation correctly forbids treating lexical route anchors as a transport theorem or numerical selected-field evaluation | `RETAIN_AS_TRIAGE_ONLY` |

## Source conclusion from this tranche

The reviewed artefacts support the following bounded statement:

\[
\text{encoded selected endpoint} \not\Rightarrow
\text{complete final paper-moment identification}.
\]

They do not support the stronger statements

\[
\|u\|_\infty\to\infty\Rightarrow
\text{every residual summand diverges},
\]

or

\[
f\in C^\infty\Longleftrightarrow(M,I,J,S,C_p)=0.
\]

Those stronger claims remain unproven and must not be promoted in the paper,
plan, or public evidence register.

## Completion of the remaining 26-entry review

The second review pass read the remaining source, control, build, census, and
tree artefacts. Large JSON and HTML files were checked by SHA-256, JSON
parsing, schema keys, counts, route fields, status fields, and relevant
interpretation fields rather than by treating generated bulk text as a new
mathematical result.

| Artefact | SHA-256 | Review result | Disposition gate |
| --- | --- | --- | --- |
| `$null` | `f980bfe3123a50d45f43785b8df0180235aa7189bb21f39bef54aa69e5381622` | Accidental command-output artefact containing path-resolution errors; no scientific or Lean evidence. | `HOLD_NO_STAGE_NO_MOVE` |
| `docs/archive/OpenAI_NavierStokes_Research_Paper_publication_extract_2026-09-30.md` | `92dc55e8995fcbae67ea999d3aa57a5f98287e762fa509f6f85a9fe7de990064` | Dated publication extract; useful historical intake, but canonical claims remain in the current paper and evidence dossier. | `HOLD_NO_STAGE_NO_MOVE` |
| `docs/Define inteligence tree.md` | `476cc9257bf6f3a8259fe78110bdcd9df170b8e265dabb6aeb13e850aa522d17` | Historical generated tree inventory. It is navigation evidence, not semantic authority, and has known tree drift. | `HOLD_NO_STAGE_NO_MOVE` |
| `docs/DOCUMENTATION_RECONCILIATION_2026-09-30.md` | `b9f989f3ff7057e9f891f1c749b16f70d9290d2fdb27361d8ac283d58c3cc893` | Current control ledger. It correctly locks the calibrated CTR-005 finding, count discrepancy, tree drift, and no-move rule. | `HOLD_NO_STAGE_NO_MOVE` |
| `docs/navierstokes.md` | `f2bc583b4f8679f118afed712590b2a4948d3d59a8c04d10e64390dc31b4d32f` | CMI source mirror. It preserves the connected problem statement and alternatives; it does not alter the Lean endpoint finding. | `HOLD_NO_STAGE_NO_MOVE` |
| `NavierStokes/R3/TestPressure.lean` | `eb476f81af0eb578cf87600fca94f772687b5aafbd2f2273e7b284a395fcd9bf` | Protected OpenAI source-side test file. It remains outside this review workflow and is not staged or edited. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/agent_log5_cross_exam_2026-09-27.md` | `de52e86ebc9ea6d37c63809ba491384b4f7df23220431d26e5d4afb5f40a293d` | Calibrated cross-examination. It supports upstream reachability plus the unresolved selected-field composition, while rejecting destruction and sole-mechanism overclaims. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/environment_build_Theorem_2026-09-28.log` | `4ea6cbc5248ccd479d84d6311284b730b69ae3ca1a28db247ff4f6c3e5ba4419` | Partial build record with Mathlib failures and exit code `3221225794`; not a successful endpoint build and not a mathematical result. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/fresh_build_status_2026-09-27.md` | `2a487d172488497f5835917f8a16cfb4201fed98dc4f81cdc5c308a0959a706b` | Correctly records timed-out post-clean rebuild attempts as incomplete verification, not Lean failure. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/fresh_environment_replay_2026-09-27.md` | `b71ec494afb91ce099fba1b33797c6886068b7a6e0c85a841127d7103cb25e3d` | Correctly records that a fresh source-to-compiled environment join was not produced; dated source findings remain separate. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/hardened_audit_bundle_2026-09-27.json` | `841c89caf52a84104d493076d77b3b0bbf0c0afa42f3384f6dc73fc0ebe23d19` | Validated historical audit bundle with 2,790-module counts and zero `sorryAx` users in its captured environment; not the current register. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/hardened_audit_bundle_2026-09-27.md` | `e8d1f41d3673df3f6220f826f016466b393c0612cb895b73753c0464c67c5074` | Human-readable companion to the dated bundle. It correctly separates reachability from value-level transport. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/hardened_source_map_2026-09-27.json` | `912759c60887a18cec3b08dd4847461ace7b40f047d4cfe3c85260b82f65ace2` | Large generated source map. Schema and counts parse, but it is a dated inventory and diagnostic declaration graph, not a proof of transport. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/reachable_initial_moment_cluster_2026-09-27.md` | `7d3e8c7ccb57377b1b7533fa9ba7bf5acf2ed6d522ddf6f12761415588b5893b` | Direct cluster review supports genuine profile moment machinery and explicitly leaves the selected Cartesian composition open. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/reachable_primary_axis_moving_pressure_tier_2026-09-27.md` | `b20e0ed1fcb22e72998bdcff7f1475afaf06e1f7f590c04f0f56ef40db33f42f` | Direct tier review supports concrete bounds and pressure/moment classes, without proving a selected-field mismatch or impossibility. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/reachable_r3_primary_mean_wave_tier_2026-09-27.md` | `3debfae81cef79af35356cf147240c276d148b59bd34a4ec8d2bf6a729029b38` | Direct R3 and wave review supports real Cartesian and averaging declarations, while retaining CTR-005 as a correspondence issue. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/selected_endpoint_source_census_2026-09-27.json` | `654b750c180b29815add1481818234ddbd1f27520c69e1a8d9548983973e67b5` | Source-only census. Its seven production bridge candidates are stage, rate, or blow-up declarations, not a final five-observable equality. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/selected_transport_audit_2026-09-28.json` | `5aa1ed5a639eda47d08e68d1f125b0a7caaa0ad8a913eb4b662c1cfe73af28c4` | Conservative review-side audit. Environment rows are empty; 11 source candidates are triage targets, and every verdict flag for proof, defect, impossibility, or `False` is false. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/semantic_coverage_register_2026-09-27.html` | `b49d5e9657e3a2c3e0b230756a3f546f0a0f5e22dd0031b924b8021f8625e89f` | Generated HTML mirror of the dated narrow register; historical navigation only. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/semantic_coverage_register_2026-09-27.json` | `38dcc68cee8ec99edef8153b126f2a095653941829ab47f0927ad371bc723f72` | Dated narrow register with 2,790 modules and 29 captured reachable rows; superseded for current control by the later full register. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/semantic_coverage_register_2026-09-27.md` | `b3b42918bbab24036a2453882a95d9594641a53bf8061b34829639f2b29f13c8` | Human-readable companion to the dated narrow register; its reachability definition is retained as historical context. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/semantic_coverage_register_full_2026-09-27.html` | `8a99564003b75f5fdfbd13101d6faa2593d0a3c8a36de7c393123af8f7f570a8` | Generated HTML mirror of the dated full register; historical navigation only. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/semantic_coverage_register_full_2026-09-27.json` | `5476b9110b7aeab242192dcb3ebc73ce03adbcd1849d9b5cdcdd7499d2f8d88f` | Dated full register with 2,790 modules, 588 captured modules, 75 supplemental records, and 10 source rows containing a `sorry` token; not current authority. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/semantic_coverage_register_full_2026-09-27.md` | `9760b5defa16908792866c473e38c43b54bb85d5c8edcc4287507f590b5f9372` | Human-readable companion to the dated full register; retained as historical evidence and not used to override current counts. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/tree_reconciliation_2026-09-27.json` | `1604df13e28395a00c384c58fcac2166f9d8fcabc42ada8a0940eb8fe41bf72d` | Dated tree reconciliation with no missing entries but 24 ambiguous basename matches; ambiguity is an inventory issue, not theorem absence. | `HOLD_NO_STAGE_NO_MOVE` |
| `evidence/tree_reconciliation_2026-09-27.md` | `8b07387316aa91d404926082b297b44761e221f2d3575773c720e9965eb28385` | Human-readable companion to the dated reconciliation; it supports the navigation-drift finding only. | `HOLD_NO_STAGE_NO_MOVE` |

## Remaining gate

The 61-entry content review is complete. The next gate is document-level
cross-reference, tree-index reconciliation, explicit retain/merge/supersede
decisions, and release validation. No archive move, deletion, or scoped
staging is authorised yet. The protected OpenAI source file remains outside
this workflow.
