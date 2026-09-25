import NavierStokes.ActualCandidateConstruction

/-!
# Selected angular component formula

This completion exposes the scalar coefficient carried by the selected
angular mean field before any radial-moment calculation is attempted.
-/

noncomputable section

namespace NavierStokesReview.SelectedAngularComponentFormula

open NavierStokes
open NavierStokes.ActualCandidateConstruction

theorem meanAngularField_component_one (B N0 : ℕ) (degree : ℝ)
    (f : ActualMeanPhysicalData.Scalar) (w : ProblemStatement.SpaceTime) :
    (meanAngularField B N0 degree f w) 1 =
      meanField B N0 degree f w *
        ((PhysicalGraphBounds.radialProjection w).1 /
          PhysicalClassBounds.cartesianRadius
            (PhysicalGraphBounds.radialProjection w)) := by
  simp only [meanAngularField, PhysicalMeanJetBounds.angularVector,
    PhysicalGraphBounds.radialProjection_apply,
    PhysicalClassBounds.cartesianRadius, smul_add, smul_smul]
  simp [ProblemStatement.coordinateVector]

end NavierStokesReview.SelectedAngularComponentFormula
