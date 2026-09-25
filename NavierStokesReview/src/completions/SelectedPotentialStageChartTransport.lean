import NavierStokes.ActualCandidateAssembly

/-!
# Selected potential-stage chart transport

This completion exposes the potential branch of the actual selected endpoint
on the chart domain used by `ActualPhysicalPrefixFields.StageRealizations`.
It is a field equality, not yet a radial-moment identity: the latter still
requires a proved component, torus-average, axis, and support transport.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialStageChartTransport

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open Set

theorem selected_potential_stage_curl_on_chart
    (k n : ℕ) {a : ℝ} (ha : 0 < a) (i : PolarCharts.Index)
    (hn : ActualCandidateConstruction.residualBand
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold ≤ n) :
    EqOn (SpatialCurl.spatialCurl (selectedPotentialStages k))
      (CyclePhysicalPrefixes.potentialParts
        (ActualCandidateConstruction.parameterSequence
          ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        (CorrectionInitialization.ActualPrimary.commonContext
          ActualCandidateConstruction.selectedBudget)
        (ActualInitialization.initialCycleState
          ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        a i (ActualCandidateConstruction.graph n) n k)
      (ActualPhysicalPrefixFields.cartesianChartDomain
        (ActualCandidateConstruction.qbig
          ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold) n a i) := by
  exact (ActualCandidateAssembly.stageRealizations
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    ActualCandidateConstruction.selectedThreshold_geometry).potential
    n hn a ha i k

end NavierStokesReview.SelectedPotentialStageChartTransport
