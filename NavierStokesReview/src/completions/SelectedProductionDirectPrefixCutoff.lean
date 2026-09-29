import NavierStokes.SpatialLocalization
import completions.SelectedDirectPrefixField
import NavierStokes.ActualMeanStageData
import completions.SelectedRadialSectionComponent

/-!
# Selected direct prefix after spatial cutoff

The native direct prefix has an order-two zero moment before production
localisation.  The production field instead multiplies each direct stage by
`SpatialLocalization.spatialCutoff`.  This theorem records that operation
exactly for a finite prefix.  It does not infer that the weighted moment is
zero or nonzero.
-/

noncomputable section

namespace NavierStokesReview.SelectedProductionDirectPrefixCutoff

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open ProblemStatement
open scoped BigOperators

theorem selected_cut_direct_prefix_component_one
    (J : ℕ) (w : SpaceTime) :
    (∑ j ∈ Finset.range (J + 1),
        (SpatialLocalization.cutPotential (selectedDirectStages j) w) 1) =
      SpatialLocalization.spatialCutoff w.2 *
        (∑ j ∈ Finset.range (J + 1), (selectedDirectStages j w) 1) := by
  simp only [SpatialLocalization.cutPotential, PiLp.smul_apply, smul_eq_mul]
  rw [Finset.mul_sum]

theorem selected_cut_direct_prefix_radial_component_one
    (J : ℕ) (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1) :
    (∑ j ∈ Finset.range (J + 1),
        (SpatialLocalization.cutPotential (selectedDirectStages j)
          (ActualMeanStageData.radialSection p)) 1) =
      SpatialLocalization.spatialCutoff
          (ActualMeanStageData.radialSection p).2 *
        meanField ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold
          (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
          ((selectedCycle J).state.mean.angular)
          (ActualMeanStageData.radialSection p) := by
  rw [selected_cut_direct_prefix_component_one]
  have hprefix :=
    SelectedDirectPrefixField.selected_direct_prefix_eq_cycle_mean J
  change SpatialLocalization.spatialCutoff
      (ActualMeanStageData.radialSection p).2 *
        (∑ j ∈ Finset.range (J + 1),
          (selectedDirectStages j (ActualMeanStageData.radialSection p)) 1) = _
  rw [show (∑ j ∈ Finset.range (J + 1),
      (selectedDirectStages j (ActualMeanStageData.radialSection p)) 1) =
        (meanAngularField ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold
          (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
          ((selectedCycle J).state.mean.angular)
          (ActualMeanStageData.radialSection p)) 1 by
          simpa [DiagonalJetBounds.uncutPrefix] using
            congrArg (fun f => f (ActualMeanStageData.radialSection p) 1) hprefix]
  rw [SelectedRadialSectionComponent.meanAngularField_radialSection_component_one
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
    ((selectedCycle J).state.mean.angular) p hp]

theorem selected_cut_direct_prefix_shell_defect
    (J : ℕ) (w : SpaceTime) :
    (∑ j ∈ Finset.range (J + 1),
        (SpatialLocalization.cutPotential (selectedDirectStages j) w) 1) -
        (∑ j ∈ Finset.range (J + 1), (selectedDirectStages j w) 1) =
      (SpatialLocalization.spatialCutoff w.2 - 1) *
        (∑ j ∈ Finset.range (J + 1), (selectedDirectStages j w) 1) := by
  rw [selected_cut_direct_prefix_component_one]
  ring

end NavierStokesReview.SelectedProductionDirectPrefixCutoff
