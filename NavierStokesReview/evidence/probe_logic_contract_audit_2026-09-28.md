# Adversarial probe-contract audit

This report audits the logical scope of auditor-authored Lean probes. It
does not replace Lean compilation and does not infer mathematical truth
from names or lexical co-occurrence.

## Machine summary

- Declarations reviewed: **262**
- Selected-term declarations: **91**
- Declarations with explicit premise markers: **20**
- Declarations with strong-conclusion markers: **88**
- Unconditional endpoint claims authorised by this instrument: **0**
- Origins: `{'review_probe_or_extension': 155, 'review_completion': 107}`
- Scope classes: `{'requires_manual_scope_review': 122, 'review_completion_identity': 102, 'conditional_conclusion': 10, 'type_boundary_or_ghost_payload': 12, 'fixed_force_path_dependence': 15, 'interface_level': 1}`

## Contract rules

1. A conditional theorem remains conditional until every premise is
   derived from the selected construction.
2. A ghost `Debt` or interface countermodel is not the selected field's
   physical observable.
3. A review completion is not OpenAI source evidence.
4. A pointwise inequality is not a nonzero integrated moment.
5. A finite-prefix identity is not an infinite-`tsum` identity without
   convergence, interchange, and domain proofs.
6. No declaration-level scan authorises `False`, `Delta m != 0`, or
   formal refutation.

## Declaration matrix

| Origin | Scope | File | Lines | Declaration | Premises | Conclusion markers |
|---|---|---|---:|---|---|---|
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/BuiltinRules.lean` | 48-51 | `not_intro` | none | False, not_, ¬ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/BuiltinRules.lean` | 51-54 | `empty_false` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/BuiltinRules.lean` | 54-61 | `pEmpty_false` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Forward/State/UpdateGoal.lean` | 16-29 | `updateForwardState` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/Basic.lean` | 22-32 | `elabBoolLit` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/RuleExpr.lean` | 85-136 | `PhaseName.` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/RuleExpr.lean` | 164-176 | `elabSingleIndexingMode` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/RuleExpr.lean` | 191-240 | `elabTransparency` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/RuleExpr.lean` | 262-393 | `RuleSetName.elab` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/Saturate.lean` | 76-89 | `elabAdditionalForwardRules` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/Saturate.lean` | 96-109 | `elabForwardRuleSet` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/Saturate.lean` | 129-135 | `evalSaturate` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/Saturate.lean` | 135-147 | `evalSaturate` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Frontend/Tactic.lean` | 99-169 | `parse` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Index.lean` | 138-182 | `applicableRules` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/RuleSet.lean` | 514-530 | `applicableForwardRulesWith` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/RuleTac/ElabRuleTerm.lean` | 80-92 | `elabSimpTheorems` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Saturate.lean` | 39-185 | `getSingleGoal` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Tree/ExtractScript.lean` | 39-44 | `lazyStepsToSteps` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/Aesop/Tree/Tracing.lean` | 28-82 | `Goal.traceMetadata` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/18.lean` | 18-33 | `Mem.split` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/207.lean` | 10-36 | `Set` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/27.lean` | 40-54 | `All.split_cons` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/AssumptionTransparency.lean` | 11-44 | `T` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/CasesTransparency.lean` | 14-44 | `T` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/CasesTransparency.lean` | 44-49 | `U` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/CasesTypeSynonym.lean` | 9-64 | `X` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/List.lean` | 21-30 | `IsEmpty.false'` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/List.lean` | 93-97 | `mem_none` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/List.lean` | 156-161 | `Empty` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/NoProgress.lean` | 22-33 | `F` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/NoProgress.lean` | 33-37 | `F'` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/NoProgress.lean` | 37-62 | `F'_def` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/Safe.lean` | 19-22 | `even'_of_false` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/SeqCalcProver.lean` | 26-54 | `Mem.split` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/SeqCalcProver.lean` | 286-397 | `Cal_sound_complete` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/TraceProof.lean` | 24-38 | `F` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/aesop/AesopTest/Unfold.lean` | 47-66 | `Bar` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/importGraph/MainGraph.lean` | 172-204 | `graph` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/LeanSearchClient/LeanSearchClient/Syntax.lean` | 251-453 | `searchTacticSuggestions` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/plausible/Plausible/Testable.lean` | 396-520 | `minimize` | none | False, ≠, ¬ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Component/InteractiveSvg.lean` | 67-132 | `InteractiveSvg.serverRpcMethod` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Component/Panel/Basic.lean` | 48-58 | `withPanelWidgets` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Data/Svg.lean` | 97-142 | `Shape.toHtmlData` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/Euclidean.lean` | 139-180 | `EuclideanDisplay.rpc` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/Euclidean.lean` | 267-307 | `EuclideanConstructions.rpc` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/Graph/Graphviz.lean` | 38-87 | `ClickNodeDemo` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/InteractiveSvg.lean` | 12-47 | `isvg` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/InteractiveSvg.lean` | 52-63 | `init` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/LazyComputation.lean` | 31-70 | `runnerWidget` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/RbTree.lean` | 129-150 | `RBTree.presenter` | none | False, ¬ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/SelectInsertConv.lean` | 125-151 | `ConvSelectionPanel.rpc` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/proofwidgets/ProofWidgets/Demos/Venn.lean` | 89-116 | `VennDisplay.rpc` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/Qq/Qq/Match.lean` | 189-477 | `elabPat` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/Qq/QqTest/clauseConvertProp.lean` | 3-12 | `or1` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/Qq/QqTest/clauseConvertProp.lean` | 12-16 | `or2` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/lean32-preflight/.lake/packages/Qq/QqTest/commandTest.lean` | 54-117 | `assignQ` | none | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/RepositoryAdmissionAudit.lean` | 15-25 | `review_module_is_admission_free` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/SelectedActivePairReachability.lean` | 20-35 | `active_pair_of_selected_label` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/audit/SelectedActivePairReachability.lean` | 35-44 | `active_pair_nonempty_if_selected_label_nonempty` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/CorrectionInvariantScope.lean` | 22-32 | `five_rows_force_zero_correction_moments` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/CorrectionInvariantScope.lean` | 32-42 | `nonzero_angular_shift_cannot_satisfy_five_rows` | none | False, ≠, not_ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/CorrectionInvariantScope.lean` | 42-52 | `nonzero_axial_shift_cannot_satisfy_five_rows` | none | False, ≠, not_ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/CorrectionInvariantScope.lean` | 52-79 | `rank_stage_preserves_designated_moments` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/MeanRankUpdateAudit.lean` | 17-23 | `scaleDebt_coordinates` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/MeanRankUpdateAudit.lean` | 23-31 | `fiveRows_zero_rows_are_correction_moments` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/MeanRankUpdateAudit.lean` | 31-43 | `nonzero_debt_is_compatible_with_zero_rows` | none | ≠ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean` | 30-47 | `not_integrable_of_periodic_positive_on_fundamental_interval` | hpositive, hperiodic | not_, ¬ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean` | 47-56 | `periodic_global_integral_zero_of_positive_on_fundamental_interval` | hpositive, hperiodic | not_ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean` | 56-77 | `selected_mixed_barMoment_zero_of_positive_pullback` | hpositive | not_, ¬ |
| review_completion | conditional_conclusion | `NavierStokesReview/src/completions/PeriodicRadialSupportObstruction.lean` | 25-55 | `periodic_radiallySupported_eq_zero` | hsupport | ≠, not_ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/PeriodicRadialSupportObstruction.lean` | 55-75 | `unit_periodic_pullback_radiallySupported_eq_zero` | hsupport | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedAtlasDomainBoundary.lean` | 11-33 | `atlas_physical_zero_of_nonpositive_slow_coordinate` | none | False, not_ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedBarMomentInterface.lean` | 31-53 | `selected_component_barMoment_apply` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedBarMomentInterface.lean` | 53-68 | `selected_component_requires_transport_data` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedBaseProfileTransport.lean` | 20-27 | `constructed_curl_eq_selected_velocity` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedBaseProfileTransport.lean` | 27-42 | `constructed_curl_axis_tendsto` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCutStageCurlScope.lean` | 20-39 | `selected_cut_stage_curl_expansion` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCutStageCurlScope.lean` | 39-63 | `selected_cut_stage_curl_component_zero` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCycleMasses.lean` | 20-32 | `selected_cycle_zeroMasses` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean` | 32-43 | `selected_cycle_state_zero_masses` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean` | 43-51 | `selected_cycle_nonzero_angular_moment_impossible` | none | False, ≠ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean` | 51-59 | `selected_cycle_nonzero_axial_moment_impossible` | none | False, ≠ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean` | 59-66 | `selected_cycle_mean_angular_barMoment_zero` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean` | 66-75 | `selected_cycle_mean_axial_barMoment_zero` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectAtlasScalarRepresentative.lean` | 33-43 | `meanField_eq_selectedDirectAtlasScalar_pullback` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectAtlasScalarRepresentative.lean` | 43-50 | `selected_direct_atlas_scalar_barMoment_apply` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectAtlasScalarRepresentative.lean` | 50-64 | `selected_direct_radial_component_eq_atlas_scalar` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectCutoffMomentBoundary.lean` | 25-46 | `cut_direct_component_one_radial_minus_native` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectCutoffMomentBoundary.lean` | 46-71 | `cut_direct_component_one_radial_ne_native_of_cutoff_ne_one` | none | ≠ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectNativePrefixMoment.lean` | 24-40 | `selected_direct_native_scalar_prefix_eq_cycle_mean` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectNativePrefixMoment.lean` | 40-56 | `selected_direct_native_scalar_prefix_barMoment_zero` | hscalar | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectPrefixField.lean` | 21-30 | `selected_direct_stages_eq_angular_mean` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectPrefixField.lean` | 30-45 | `selected_direct_prefix_eq_cycle_mean` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectPrefixField.lean` | 45-69 | `selected_direct_stage_eq_chart` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean` | 27-36 | `selected_direct_component_one_eq_native_scalar` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean` | 36-42 | `selected_direct_native_scalar_barMoment_zero` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean` | 42-52 | `selected_direct_native_scalar_radial_integral_zero` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedDirectStageMomentTransport.lean` | 31-65 | `selected_angular_native_stage_moment_zero` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean` | 23-33 | `selected_schedule_exists` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean` | 33-58 | `selected_potential_sum_locally_finite` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean` | 58-86 | `selected_potential_sum_all_jets_locally_finite` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedFiniteCutoffEndpoint.lean` | 25-46 | `selected_finite_cutoffs_eventually_one_on_axis` | hfinite | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedMomentResidualDecomposition.lean` | 30-40 | `selected_mixed_order_two_minus_potential_eq_direct` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedMomentResidualDecomposition.lean` | 40-51 | `selected_mixed_order_two_reduces_to_potential_residual` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedMomentResidualDecomposition.lean` | 51-64 | `selected_mixed_order_two_zero_iff_potential_zero` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionBarMoment.lean` | 37-42 | `selected_mixed_production_point_scalar_apply` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionBarMoment.lean` | 42-51 | `selected_mixed_production_point_barMoment_apply` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionBarMoment.lean` | 51-62 | `selected_mixed_production_point_scalar_physical_pullback` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionBarMomentLinearity.lean` | 26-34 | `selected_mixed_production_point_scalar_eq_branch_sum` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionBarMomentLinearity.lean` | 34-47 | `selected_mixed_production_barMoment_add` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionBranchSplit.lean` | 41-52 | `selected_mixed_production_point_scalar_branch_split` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean` | 36-49 | `selected_mixed_production_scalar_split` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionTorusAverage.lean` | 24-33 | `torusAverage_selected_mixed_production` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedProductionTorusAverage.lean` | 33-46 | `selected_mixed_barMoment_radial_reduction` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedRadialPeriodicity.lean` | 27-61 | `selected_mixed_production_scalar_periodic_radius` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedRadialPeriodicity.lean` | 61-76 | `selected_mixed_barMoment_integrand_periodic` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedRadialSupportObstruction.lean` | 30-37 | `selected_mixed_radial_pullback_periodic` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedRadialSupportObstruction.lean` | 37-50 | `selected_mixed_bounded_radial_support_forces_zero` | hsupport | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedVelocityDecomposition.lean` | 22-35 | `selected_velocity_decomposition` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedVelocityDecomposition.lean` | 35-47 | `selected_velocity_decomposition_at` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedVelocityDecomposition.lean` | 47-69 | `selected_periodic_velocity_decomposition` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedMixedVelocityFinitePrefix.lean` | 23-94 | `selected_mixed_velocity_locally_finite` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPhysicalComponentTransport.lean` | 32-66 | `selected_direct_stage_component_one_on_chart` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPhysicalComponentTransport.lean` | 66-96 | `selected_direct_stage_component_one_scaled` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPhysicalPointTransport.lean` | 24-27 | `physical_moment_point_defeq_pressure_stream_point` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPhysicalPointTransport.lean` | 27-37 | `barMoment_transport_requires_selected_scalar` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialChartComponent.lean` | 25-43 | `selected_positive_stage_component_one_on_chart` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialChartComponent.lean` | 43-61 | `selected_positive_stage_component_one_split` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialPrefixCurlExpansion.lean` | 23-50 | `selected_potential_velocity_eventuallyEq_partial_curl` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean` | 39-44 | `selected_potential_production_point_scalar_apply` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean` | 44-53 | `selected_potential_production_point_barMoment_apply` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean` | 64-75 | `selected_potential_production_point_scalar_physical_pullback` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean` | 33-47 | `selected_potential_partial_curl_eq_stage_sum` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean` | 47-60 | `selected_potential_partial_cut_product_rule` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean` | 60-92 | `selected_potential_partial_production_expansion` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean` | 92-101 | `selected_potential_partial_production_point_barMoment_apply` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean` | 101-116 | `selected_potential_partial_production_point_scalar_physical_pullback` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean` | 116-162 | `selected_potential_partial_production_radial_scalar_eq` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionProductRule.lean` | 27-57 | `selected_potential_periodic_product_rule` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean` | 32-82 | `selected_potential_sum_spatial_differentiableAt` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean` | 82-106 | `selected_potential_production_radial_scalar_eq` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean` | 106-140 | `selected_witness_production_radial_scalar_transport` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionTorusAverage.lean` | 21-30 | `torusAverage_selected_potential_partial_production` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionTorusAverage.lean` | 30-43 | `finite_prefix_barMoment_radial_reduction` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialProductionTsumScope.lean` | 28-49 | `selected_potential_sum_all_jets_eventuallyEq_partial` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialStageChartTransport.lean` | 20-48 | `selected_potential_stage_curl_on_chart` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedPotentialStagewiseCurlOnPhysicalDomain.lean` | 22-78 | `selected_potential_velocity_eventuallyEq_stage_curls_on_physicalDomain` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectAtlasPullback.lean` | 21-47 | `selected_direct_component_atlas_pullback` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectAtlasPullback.lean` | 47-68 | `cut_direct_component_atlas_pullback` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectCutoff.lean` | 22-34 | `mixed_periodic_velocity_eq_cut_direct_on_unitCube` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectCutoff.lean` | 34-56 | `selected_mixed_velocity_eq_cut_direct_on_unitCube` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectPrefixCutoff.lean` | 25-34 | `selected_cut_direct_prefix_component_one` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectPrefixCutoff.lean` | 34-68 | `selected_cut_direct_prefix_radial_component_one` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectPrefixCutoff.lean` | 68-80 | `selected_cut_direct_prefix_shell_defect` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedProductionDirectScalarGate.lean` | 22-37 | `cut_direct_component_one_radial` | none | none |
| review_completion | type_boundary_or_ghost_payload | `NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean` | 22-24 | `witnessDebt` | none | none |
| review_completion | type_boundary_or_ghost_payload | `NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean` | 24-29 | `witnessDebt_ne_zero` | none | ≠ |
| review_completion | type_boundary_or_ghost_payload | `NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean` | 29-40 | `selected_r3_candidate_compatible_with_nonzero_five_payload` | none | ≠ |
| review_completion | type_boundary_or_ghost_payload | `NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean` | 40-50 | `selected_r3_candidate_does_not_export_five_payload_zero` | none | not_, ¬, does_not |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedRadialAxisBoundary.lean` | 31-45 | `selected_direct_stage_axis_component_one` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedRadialSectionComponent.lean` | 37-56 | `selected_direct_stage_radial_component_one` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedScalarSamplingNonuniqueness.lean` | 26-36 | `offImageFamily_sample_eq_zero` | none | False, not_ |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedScalarSamplingNonuniqueness.lean` | 36-47 | `offImageFamily_at_unreachable_eq_one` | none | False |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedStreamCurlChartTransport.lean` | 19-45 | `selected_stream_stage_curl_on_chart` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedStreamRankScope.lean` | 20-34 | `selected_stream_successor_temporal_rank` | none | none |
| review_completion | review_completion_identity | `NavierStokesReview/src/completions/SelectedStreamRankScope.lean` | 34-46 | `selected_stream_successor_moving` | none | none |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` | 148-163 | `compactPerturbation_fixed_force_defect_at_switch` | none | none |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` | 174-186 | `compactPerturbation_fixed_force_defect_nonzero_at_origin` | none | ≠ |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` | 186-229 | `compactPerturbation_breaks_any_fixed_force_at_origin` | hidentity | ¬ |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` | 229-322 | `selected_candidate_fixed_force_obstruction` | hidentity | ≠, obstruction |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/EndpointContractNonImplication.lean` | 9-28 | `candidateProperties_does_not_imply_fixedForceSameDatumStable` | none | not_, ¬, does_not |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean` | 20-52 | `fixed_force_perturbation_defect_zero` | hidentity | none |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean` | 52-71 | `fixed_force_data_perturbation_obstruction` | none | ≠, ¬, obstruction |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean` | 71-95 | `positive_time_force_perturbation_obstruction` | none | ≠, obstruction |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/SameDatumFixedForcePerturbation.lean` | 88-105 | `sameDatumCompactPerturbation_fixed_force_defect_at_switch` | none | none |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/extensions/SameDatumFixedForcePerturbation.lean` | 105-120 | `sameDatumCompactPerturbation_fixed_force_defect_nonzero_at_origin` | none | ≠ |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/extensions/SameDatumFixedForcePerturbation.lean` | 140-199 | `selected_candidate_fails_fixed_force_same_datum_stability` | hidentity | ≠, ¬, obstruction |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | 29-31 | `witnessDebt` | none | none |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | 31-36 | `witnessDebt_ne_zero` | none | ≠ |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | 36-41 | `selected_witness_compatible_with_nonzero_five_payload` | none | ≠ |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | 41-50 | `selected_witness_does_not_export_five_moment_transport` | none | not_, ¬, does_not |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/extensions/SelectedResidualProvenance.lean` | 9-27 | `selected_candidate_force_is_residual_output` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/external-semantic/Adapter.lean` | 16-20 | `openAIComparatorOptionD` | none | none |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/external_semantic/FixedForcePerturbationStability.lean` | 28-40 | `selected_candidate_fails_fixed_force_stability` | none | neq, ¬, obstruction |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/ActualCandidateAssemblyIsolationProbe.lean` | 21-37 | `selected_candidate_isolation` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/agent_moment_bridge.lean` | 14-26 | `dimension_mismatch_obstruction` | none | False, obstruction |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/AnalyticObjectionsProbe.lean` | 30-40 | `selected_endpoint_exposes_pressure_support` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/AnalyticObjectionsProbe.lean` | 40-49 | `selected_endpoint_exposes_energy_bound` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/AnalyticObjectionsProbe.lean` | 49-59 | `selected_endpoint_exposes_force_smoothness` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/CMIQuantifierProbe.lean` | 25-47 | `cmiDStatement` | none | ¬ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FilterNonVacuityAudit.lean` | 14-18 | `selected_endpoint_filter_nontrivial` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FilterNonVacuityAudit.lean` | 18-22 | `selected_endpoint_filter_supports_instance` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean` | 26-28 | `nonzeroThreeDebt` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean` | 28-33 | `nonzeroThreeDebt_ne_zero` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean` | 33-41 | `fiveRows_admits_nonzero_debt` | none | none |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean` | 41-54 | `selected_witness_and_nonzero_rank_debt_coexist` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean` | 21-24 | `promoted` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean` | 24-31 | `repairU_eq_gamma` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean` | 31-38 | `repairE_eq_deltaV` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean` | 38-54 | `positive_order_exact_for_physical_repair` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowsStructureProbe.lean` | 18-22 | `fiveRows_has_three_coordinate_debt` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowsStructureProbe.lean` | 22-32 | `fiveRows_rows_are_explicit` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowsStructureProbe.lean` | 32-39 | `fiveRows_first_two_do_not_use_debt` | none | not_ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/FiveRowsStructureProbe.lean` | 39-47 | `fiveRows_last_three_use_all_debt_coordinates` | none | none |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/probes/GlobalTransportBridgeProbe.lean` | 11-35 | `selected_global_consequences_with_fixed_force_obstruction` | none | ¬, obstruction |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/probes/GlobalTransportBridgeProbe.lean` | 35-46 | `global_consequence_bundle_does_not_imply_fixed_force_stability` | none | not_, ¬, does_not, obstruction |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean` | 35-67 | `fixed_force_perturbation_defect_zero` | hidentity | none |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean` | 67-85 | `fixed_force_perturbation_is_impossible_when_defect_nonzero` | none | ≠ |
| review_probe_or_extension | fixed_force_path_dependence | `NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean` | 110-154 | `affine_time_perturbation_breaks_fixed_force` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/ManifoldDimensionalReductionProbe.lean` | 23-27 | `promoted` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/ManifoldDimensionalReductionProbe.lean` | 27-35 | `spatial_dimension_zero_collapse` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/ManifoldDimensionalReductionProbe.lean` | 35-43 | `spatial_dimension_one_collapse` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/ManifoldDimensionalReductionProbe.lean` | 43-55 | `physical_debts_shifted` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/MirrorForceSymmetryProbe.lean` | 31-42 | `nonzero_force_cannot_use_same_fields_for_mirror` | none | ≠, not_ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean` | 38-43 | `no_direct_moment_bridge` | none | ¬ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean` | 43-51 | `no_linear_debt_equivalence` | none | ¬ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/MomentInitializationProbe.lean` | 10-18 | `selected_initial_masses_are_zero` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/MovingFieldRowNonImplicationProbe.lean` | 29-43 | `movingField_does_not_imply_fiveRows` | none | not_, ¬, does_not |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/PressureResidualNonCancellationProbe.lean` | 49-67 | `nonzero_pressure_gradient_changes_residual` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedBaseMomentCompatibilityProbe.lean` | 26-44 | `modulated_scheme_has_five_moment_identity` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedBudgetProbe.lean` | 4-16 | `selected_budget_is_zero` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedBudgetProbe.lean` | 16-20 | `selected_budget_is_not_positive` | none | not_, ¬ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedBudgetProbe.lean` | 20-25 | `selected_threshold_is_geometrically_admissible` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedDivergenceAudit.lean` | 21-33 | `selected_endpoint_divergence_free` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedForceOriginCompositionProbe.lean` | 20-34 | `periodic_residual_origin` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedForceOriginCompositionProbe.lean` | 34-149 | `selected_force_tends_to_zero_at_origin` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedLabelConstructionProbe.lean` | 109-127 | `selected_primary_label_nonempty` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedLabelConstructionProbe.lean` | 127-143 | `selected_active_pair_nonempty` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedLabelInhabitabilityProbe.lean` | 69-77 | `potentialSum_is_nat_indexed` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedPhysicalDataMomentInterfaceProbe.lean` | 27-29 | `ghostDebt` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedPhysicalDataMomentInterfaceProbe.lean` | 29-34 | `ghostDebt_ne_zero` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedPhysicalDataMomentInterfaceProbe.lean` | 34-53 | `selected_physical_data_coexists_with_unconstrained_five_debt` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean` | 19-35 | `flat_residual_conflicts_with_blowup_under_lower_bound` | none | False |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean` | 35-51 | `selected_origin_lower_bound_is_the_required_missing_step` | htransport | False |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean` | 51-81 | `selected_time_lower_bound_conflicts_with_the_actual_flatness_contract` | htransport | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean` | 29-31 | `nonzeroDebt` | none | none |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean` | 31-41 | `selected_witness_does_not_entail_zero_five_debt` | none | not_, ¬, does_not |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean` | 22-59 | `selected_origin_speed_tendsto` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean` | 59-109 | `selected_origin_residual_tends_zero` | none | none |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean` | 109-156 | `selected_origin_positive_lower_bound_is_impossible` | htransport | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean` | 156-163 | `selected_witness_has_candidate_properties` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean` | 163-170 | `interior_residual_is_the_selected_force` | none | none |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean` | 170-202 | `lower_bound_contradicts_selected_speed` | htransport | False |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean` | 21-23 | `ghostDebt` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean` | 23-28 | `ghostDebt_is_nonzero` | none | ≠ |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean` | 28-37 | `selected_witness_coexists_with_unconstrained_ghost_debt` | none | ≠ |
| review_probe_or_extension | type_boundary_or_ghost_payload | `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean` | 37-46 | `selected_witness_signature_ignores_five_debt` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean` | 21-29 | `selected_periodic_properties_are_exported` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean` | 29-36 | `selected_path_reaches_r3_only_through_localization` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean` | 36-50 | `selected_r3_envelope_coexists_with_unconstrained_five_debt` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean` | 23-29 | `five_rows_expose_the_two_fixed_rows` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean` | 29-37 | `five_rows_retain_all_three_debt_coordinates` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean` | 37-53 | `compact_support_does_not_force_a_pressure_slice_to_zero` | none | not_, ¬, does_not |
| review_probe_or_extension | interface_level | `NavierStokesReview/src/probes/StageEstimatesMomentBlindnessProbe.lean` | 154-174 | `interface_does_not_determine_five_debt` | none | not_, ¬, does_not |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/probes/StructuralDualityMirrorProbe.lean` | 45-56 | `mirror_is_different_forcing_problem` | hnonzero | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/refutations/CTR005ProfileTailCollisionScope.lean` | 31-38 | `five_rows_are_increment_scoped` | none | none |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/refutations/CTR005ProfileTailCollisionScope.lean` | 38-53 | `nonzero_runtime_debt_compatible_with_zero_correction_rows` | none | ≠ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/refutations/CTR005ProfileTailCollisionScope.lean` | 53-59 | `selected_cycle_zero_rows_are_not_total_field_moments` | none | not_ |
| review_probe_or_extension | requires_manual_scope_review | `NavierStokesReview/src/refutations/CTR005ProfileTailCollisionScope.lean` | 59-69 | `barMoment_is_radial_profile_quantity` | none | none |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/refutations/SelectedPeriodicSupportTransportGate.lean` | 33-45 | `selected_periodic_support_transport_gate` | hsupport, hnonzero | False, ≠ |
| review_probe_or_extension | conditional_conclusion | `NavierStokesReview/src/refutations/SelectedPeriodicSupportTransportGate.lean` | 45-62 | `selected_witness_schedule_support_gate` | hsupport, hnonzero | False, ≠ |

## Audit status

This instrument is a blindside detector for the review apparatus. It
does not assert that a hidden source theorem is absent. The selected
field still requires a source-backed, compiled theorem for the exact
Cartesian-to-radial composition and its five observables.
