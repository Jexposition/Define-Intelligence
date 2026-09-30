# Hardened selected-endpoint transport audit

This report separates source declaration triage from Lean-environment evidence.
A co-occurrence is not a transport proof. No absence result is promoted to an impossibility theorem.

## Audit contract

A declaration is a transport candidate only when the same declaration binds selected-field terms and moment terms, and also contains an equality/transport conclusion. A full candidate additionally shows the transformation terms (`tsum`, curl/localisation, periodisation/torus averaging, or the axis/chart route) in its body. These are review targets until compiled and manually checked.

- Source declarations indexed: **33986**
- Joint source candidates: **11**
- Full manual candidates: **0**
- Environment closure supplied: **False**
- Environment declarations with endpoint/moment/transform terms in their type: **0**

## Source candidates

| Category | File | Lines | Declaration | Field terms | Moment terms | Transform terms |
|---|---|---:|---|---|---|---|
| moment_field_equality_candidate | `NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean` | 57-76 | `NavierStokesReview.PeriodicGlobalIntegral.selected_mixed_barMoment_zero_of_positive_pullback` | selectedMixedRadialPullback | barMoment |  |
| moment_field_equality_candidate | `NavierStokesReview/src/completions/SelectedBarMomentInterface.lean` | 24-27 | `NavierStokesReview.SelectedBarMomentInterface.selectedPotentialComponent` | selectedPotentialStages | barMoment |  |
| moment_field_equality_candidate | `NavierStokesReview/src/completions/SelectedBarMomentInterface.lean` | 32-45 | `NavierStokesReview.SelectedBarMomentInterface.selected_component_barMoment_apply` | selected_witness | barMoment | torusAverage |
| moment_field_equality_candidate | `NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean` | 30-40 | `NavierStokesReview.SelectedR3PackagingBoundary.selected_r3_candidate_compatible_with_nonzero_five_payload` | VelocityField | Debt |  |
| moment_field_equality_candidate | `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | 37-41 | `NavierStokesReview.SelectedEndpointMomentTransportObstruction.selected_witness_compatible_with_nonzero_five_payload` | selected_witness | Debt |  |
| moment_field_equality_candidate | `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | 42-49 | `NavierStokesReview.SelectedEndpointMomentTransportObstruction.selected_witness_does_not_export_five_moment_transport` | selected_witness | Debt |  |
| moment_field_equality_candidate | `NavierStokesReview/src/probes/ActualCandidateAssemblyIsolationProbe.lean` | 23-36 | `NavierStokesReview.ActualCandidateAssemblyIsolationProbe.selected_candidate_isolation` | selected_witness | PositiveOrderMoments, Debt |  |
| moment_field_equality_candidate | `NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean` | 42-53 | `NavierStokesReview.FiveRowCollisionBoundaryProbe.selected_witness_and_nonzero_rank_debt_coexist` | selected_witness | FiveRows, FiveRowRank |  |
| moment_field_equality_candidate | `NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean` | 32-41 | `NavierStokesReview.SelectedWitnessAttackBoundaryProbe.selected_witness_does_not_entail_zero_five_debt` | selected_witness | Debt |  |
| moment_field_equality_candidate | `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean` | 39-45 | `NavierStokesReview.SelectedWitnessInhabitationProbe.selected_witness_signature_ignores_five_debt` | selected_witness | Debt |  |
| moment_field_equality_candidate | `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean` | 37-49 | `NavierStokesReview.SelectedWitnessPathProbe.selected_r3_envelope_coexists_with_unconstrained_five_debt` | VelocityField | Debt |  |

## Interpretation boundary

`manual_transport_candidate` means only that a declaration deserves direct Lean review. It does not prove that the equality is the paper's equality, that its domain is the selected whole-space field, or that its premises are inhabited. A conditional `False` theorem is not an endpoint contradiction until every hypothesis is derived on the selected branch.

The report therefore cannot by itself justify `FORMALLY REFUTED`, `False`, `Delta m != 0`, or `zero percent formalised`. Those labels require a compiled zero-sorry theorem or a complete source-backed proof with all concrete premises.
