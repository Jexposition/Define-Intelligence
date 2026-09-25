import completions.SelectedDirectPrefixField

/-!
# Selected angular field at the radial axis

The positive-radius component theorem has a separate boundary branch.  The
source definition totalises the angular frame by Lean's total division, so
when both radial Cartesian coordinates vanish the selected angular field is
zero.  This records the exact axis value; it does not infer a discontinuity
or a nonzero radial moment.
-/

noncomputable section

namespace NavierStokesReview.SelectedRadialAxisBoundary

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokesReview.SelectedDirectPrefixField

theorem meanAngularField_axis_component_one
    (B N0 : ℕ) (degree : ℝ) (f : ActualMeanPhysicalData.Scalar)
    {w : ProblemStatement.SpaceTime}
    (h0 : w.2 0 = 0) (h1 : w.2 1 = 0) :
    (meanAngularField B N0 degree f w) 1 = 0 := by
  unfold meanAngularField PhysicalMeanJetBounds.angularVector
  simp only [PhysicalGraphBounds.radialProjection_apply,
    smul_add, smul_smul, ProblemStatement.coordinateVector]
  simp [h0, h1]

theorem selected_direct_stage_axis_component_one
    (j : ℕ) {w : ProblemStatement.SpaceTime}
    (h0 : w.2 0 = 0) (h1 : w.2 1 = 0) :
    (selectedDirectStages j w) 1 = 0 := by
  rw [selected_direct_stages_eq_angular_mean]
  exact meanAngularField_axis_component_one
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
    (angularNativeStages ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold j) h0 h1

end NavierStokesReview.SelectedRadialAxisBoundary
