import completions.SelectedProductionDirectScalarGate

/-!
# Selected direct component and atlas pullback

This completion records the exact scalar used by the selected direct branch
before its production cutoff is applied.  It keeps the atlas selector and the
physical-point pullback visible, so the native radial moment is not silently
identified with the exported Cartesian component.
-/

noncomputable section

namespace NavierStokesReview.SelectedProductionDirectAtlasPullback

open NavierStokes
open NavierStokes.ProblemStatement
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokesReview.SelectedProductionDirectScalarGate

theorem selected_direct_component_atlas_pullback
    (j : ℕ) (w : NavierStokes.ProblemStatement.SpaceTime) :
    (selectedDirectStages j w) 1 =
      (meanAtlas ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold).physical
        CorrectionInitialization.ActualPrimary.standardRegion.carrier
          (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
        (angularNativeStages ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold j)
        (PhysicalMeanJetBounds.physicalPoint
          CorrectionInitialization.ActualPrimary.h w) *
        (PhysicalMeanJetBounds.angularVector
        (PhysicalGraphBounds.radialProjection w)) 1 := by
  change
    (directStages ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry j w) 1 = _
  rw [ActualCandidateAssembly.directStages_eq
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    ActualCandidateConstruction.selectedThreshold_geometry j]
  simp only [ActualCandidateConstruction.angularMeanStages,
    ActualCandidateConstruction.meanAngularField,
    ActualCandidateConstruction.meanField, Function.comp_apply,
    PiLp.smul_apply, smul_eq_mul]

theorem cut_direct_component_atlas_pullback
    (j : ℕ) (w : NavierStokes.ProblemStatement.SpaceTime) :
    (SpatialLocalization.cutPotential (selectedDirectStages j)
      w) 1 =
      SpatialLocalization.spatialCutoff w.2 *
        ((meanAtlas ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold).physical
          CorrectionInitialization.ActualPrimary.standardRegion.carrier
            (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
          (angularNativeStages ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold j)
          (PhysicalMeanJetBounds.physicalPoint
            CorrectionInitialization.ActualPrimary.h w) *
        (PhysicalMeanJetBounds.angularVector
          (PhysicalGraphBounds.radialProjection w)) 1) := by
  unfold SpatialLocalization.cutPotential
  simp only [PiLp.smul_apply, smul_eq_mul]
  rw [selected_direct_component_atlas_pullback]

end NavierStokesReview.SelectedProductionDirectAtlasPullback
