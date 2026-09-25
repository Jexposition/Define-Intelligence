import NavierStokes.ActualCandidateAssembly

/-!
# Selected direct-field prefix

This module records a concrete finite-prefix identity for the selected direct
stage family.  It is deliberately a field identity only: it does not identify
the Cartesian field with `DefectIncrementBounds.barMoment` or with the five
quantities `(M, I, J, S, C_p)` from the paper.
-/

noncomputable section

namespace NavierStokesReview.SelectedDirectPrefixField

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open Set Filter ProblemStatement
open scoped Topology ContDiff BigOperators

theorem selected_direct_stages_eq_angular_mean (j : ℕ) :
    selectedDirectStages j =
      angularMeanStages ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold j := by
  exact ActualCandidateAssembly.directStages_eq
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    ActualCandidateConstruction.selectedThreshold_geometry j

theorem selected_direct_prefix_eq_cycle_mean (J : ℕ) :
    DiagonalJetBounds.uncutPrefix selectedDirectStages (J + 1) =
      meanAngularField ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
        (selectedCycle J).state.mean.angular := by
  rw [show selectedDirectStages =
      angularMeanStages ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold by
    funext j
    exact selected_direct_stages_eq_angular_mean j]
  exact angularMeanStages_prefix
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold J

theorem selected_direct_stage_eq_chart
    (j : ℕ) {a : ℝ} (ha : 0 < a) (i : PolarCharts.Index) (n : ℕ)
    (hn : ActualCandidateConstruction.firstBand
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold ≤ n)
    {w : ProblemStatement.SpaceTime}
    (ht : w ∈ PhysicalWaveSum.preterminal)
    (hu : (PhysicalMeanJetBounds.graph CorrectionInitialization.ActualPrimary.h n
      ((meanAtlas ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold).gap n) w).2.1 ∈
      CorrectionInitialization.ActualPrimary.standardRegion.carrier)
    (hw : w ∈ ActualMeanPotentialRealization.cartesianDomain a i) :
    selectedDirectStages j w =
      chartDirectStages ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold a i n j w := by
  rw [selected_direct_stages_eq_angular_mean]
  exact angularMeanStages_on_chart
    (meanCycleInput ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry)
    j ha i n hn ht hu hw

end NavierStokesReview.SelectedDirectPrefixField
