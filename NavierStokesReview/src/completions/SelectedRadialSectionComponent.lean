import completions.SelectedDirectPrefixField
import NavierStokes.ActualMeanStageData

/-!
# Selected radial-section component

This completion records the scalar coefficient carried by the selected
angular field on the positive radial half-plane.  It is the concrete
coordinate input needed before applying a radial moment operator; it does not
assert that the full mixed Cartesian velocity has the same moment.
-/

noncomputable section

namespace NavierStokesReview.SelectedRadialSectionComponent

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokesReview.SelectedDirectPrefixField

theorem meanAngularField_radialSection_component_one
    (B N0 : ℕ) (degree : ℝ) (f : ActualMeanPhysicalData.Scalar)
    (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1) :
    (meanAngularField B N0 degree f
      (ActualMeanStageData.radialSection p)) 1 =
      meanField B N0 degree f (ActualMeanStageData.radialSection p) := by
  unfold meanAngularField PhysicalMeanJetBounds.angularVector
  simp only [ActualMeanStageData.radialSection,
    PhysicalGraphBounds.radialProjection_apply,
    AxisymmetricResidual.pack_zero, AxisymmetricResidual.pack_one,
    PhysicalClassBounds.cartesianRadius, smul_add, smul_smul]
  have hs : Real.sqrt (p.2.1 ^ 2 + 0 ^ 2) = p.2.1 := by
    simpa using (Real.sqrt_sq hp.le)
  rw [hs]
  simp [ProblemStatement.coordinateVector, hp.ne']

theorem selected_direct_stage_radial_component_one
    (j : ℕ) (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1) :
    (selectedDirectStages j (ActualMeanStageData.radialSection p)) 1 =
      meanField ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
        (angularNativeStages ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold j)
        (ActualMeanStageData.radialSection p) := by
  rw [selected_direct_stages_eq_angular_mean]
  exact meanAngularField_radialSection_component_one
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
    (angularNativeStages ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold j) p hp

end NavierStokesReview.SelectedRadialSectionComponent
