import completions.SelectedAngularComponentFormula

/-!
# Selected Cartesian-to-radial gate

This file records the exact positive-radius algebra needed before a selected
Cartesian velocity can be supplied to the scalar `barMoment` operator.  It
does not assert a global radial identity, and it does not manufacture a
nonzero remainder.  The recovered coefficient is only defined where the
angular-frame component used in the division is nonzero.
-/

noncomputable section

namespace NavierStokesReview.SelectedCartesianRadialGate

open NavierStokes
open NavierStokes.ActualCandidateConstruction

theorem meanField_recovered_from_component_one
    (B N0 : ℕ) (degree : ℝ)
    (f : ActualMeanPhysicalData.Scalar) (w : ProblemStatement.SpaceTime)
    (hcomponent :
      (PhysicalGraphBounds.radialProjection w).1 ≠ 0) :
    meanField B N0 degree f w =
      (meanAngularField B N0 degree f w) 1 *
        (PhysicalClassBounds.cartesianRadius
          (PhysicalGraphBounds.radialProjection w) /
          (PhysicalGraphBounds.radialProjection w).1) := by
  have hradius : PhysicalClassBounds.cartesianRadius
      (PhysicalGraphBounds.radialProjection w) ≠ 0 := by
    intro hz
    have hsqrt : Real.sqrt
        ((PhysicalGraphBounds.radialProjection w).1 ^ 2 +
          (PhysicalGraphBounds.radialProjection w).2 ^ 2) = 0 := by
      simpa [PhysicalClassBounds.cartesianRadius] using hz
    have hsum : (PhysicalGraphBounds.radialProjection w).1 ^ 2 +
        (PhysicalGraphBounds.radialProjection w).2 ^ 2 = 0 := by
      nlinarith [Real.sq_sqrt
        (show 0 ≤ (PhysicalGraphBounds.radialProjection w).1 ^ 2 +
          (PhysicalGraphBounds.radialProjection w).2 ^ 2 by positivity)]
    have hfirst : (PhysicalGraphBounds.radialProjection w).1 = 0 := by
      nlinarith [sq_nonneg (PhysicalGraphBounds.radialProjection w).2]
    exact hcomponent hfirst
  rw [SelectedAngularComponentFormula.meanAngularField_component_one]
  field_simp [hcomponent, hradius]

end NavierStokesReview.SelectedCartesianRadialGate
