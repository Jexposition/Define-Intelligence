import NavierStokes.ActualCandidateAssembly

/-!
# Selected potential chart component

This completion transports the concrete selected positive potential stage to
the production polar chart and exposes one Cartesian component.  It is a
field-level identity needed by the radial calculation.  It is not itself a
`barMoment` identity and does not assert that the displayed component has a
nonzero integral.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialChartComponent

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open Set

private abbrev selectedBudget := ActualCandidateConstruction.selectedBudget
private abbrev selectedThreshold := ActualCandidateConstruction.selectedThreshold
private abbrev selectedGeometry := ActualCandidateConstruction.selectedThreshold_geometry

theorem selected_positive_stage_component_one_on_chart
    (j n : ℕ) {a : ℝ} (ha : 0 < a) (i : PolarCharts.Index)
    (hn : ActualCandidateConstruction.firstBand selectedBudget selectedThreshold ≤ n)
    {w : ProblemStatement.SpaceTime}
    (hw : w ∈ ActualPhysicalPrefixFields.cartesianChartDomain
      (ActualCandidateConstruction.qbig selectedBudget selectedThreshold) n a i) :
    (SpatialCurl.spatialCurl
        (ActualCandidateAssembly.selectedPotentialStages (j + 1)) w) 1 =
      (ActualCandidateConstruction.chartPotentialParts
        selectedBudget selectedThreshold a i n (j + 1) w) 1 := by
  change (SpatialCurl.spatialCurl
      (ActualCandidateAssembly.potentialStages selectedBudget selectedThreshold
        selectedGeometry (j + 1)) w) 1 = _
  rw [ActualCandidateAssembly.potentialStages_succ]
  have h := ActualCandidateAssembly.positivePotential_on_chart
    selectedBudget selectedThreshold selectedGeometry j n hn ha i hw
  exact congrArg (fun v : ProblemStatement.Space => v 1) h

theorem selected_positive_stage_component_one_split
    (j n : ℕ) {a : ℝ} (ha : 0 < a) (i : PolarCharts.Index)
    (hn : ActualCandidateConstruction.firstBand selectedBudget selectedThreshold ≤ n)
    {w : ProblemStatement.SpaceTime}
    (hw : w ∈ ActualPhysicalPrefixFields.cartesianChartDomain
      (ActualCandidateConstruction.qbig selectedBudget selectedThreshold) n a i) :
    (SpatialCurl.spatialCurl
        (ActualCandidateAssembly.selectedPotentialStages (j + 1)) w) 1 =
      (ActualCandidateConstruction.chartWaveParts
        selectedBudget selectedThreshold a i n (j + 1) w) 1 +
      (ActualCandidateConstruction.chartStreamParts
        selectedBudget selectedThreshold a i n (j + 1) w) 1 := by
  rw [selected_positive_stage_component_one_on_chart j n ha i hn hw]
  rw [ActualCandidateConstruction.chartPotentialParts_succ]
  rfl

end NavierStokesReview.SelectedPotentialChartComponent
