import NavierStokes.ActualCandidateAssembly

/-!
# Selected stream-to-curl chart transport

This records the actual scalar mean stream used inside the selected potential
stages and its Cartesian curl on the production chart.  It is a transport
identity for the selected source field; it does not identify that vector field
with the scalar torus-average input of `barMoment`.
-/

noncomputable section

namespace NavierStokesReview.SelectedStreamCurlChartTransport

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open Set

theorem selected_stream_stage_curl_on_chart
    (j n : ℕ) {a : ℝ} (ha : 0 < a) (i : PolarCharts.Index)
    (hn : ActualCandidateConstruction.firstBand
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold ≤ n) :
    EqOn
      (SpatialCurl.spatialCurl
        (ActualCandidateConstruction.streamMeanStages
          ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold j))
      (ActualCandidateConstruction.chartStreamParts
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold a i n j)
      (ActualPhysicalPrefixFields.cartesianChartDomain
        (ActualCandidateConstruction.qbig
          ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold) n a i) := by
  exact ActualCandidateAssembly.stream_on_chart
    (ActualCandidateAssembly.meanCycleInput
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry)
    j n hn ha i

end NavierStokesReview.SelectedStreamCurlChartTransport
