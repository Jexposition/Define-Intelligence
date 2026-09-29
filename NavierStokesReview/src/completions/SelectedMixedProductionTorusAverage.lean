import completions.SelectedMixedProductionBranchSplit

/-!
# Selected mixed production: exact torus-average reduction

The mixed scalar-family pullback factors through `pointToCyl` and is
independent of the auxiliary torus coordinate.  Consequently the auxiliary
torus average reduces definitionally to the scalar on the radial section.
This exposes the remaining weighted radial integral without asserting its
value.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedProductionTorusAverage

open NavierStokes
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedProductionBarMoment
open NavierStokesReview.SelectedMixedProductionBranchSplit
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedPotentialProductionBarMomentSection
open scoped BigOperators

theorem torusAverage_selected_mixed_production
    (a : ℕ → ℕ) (n : ℕ) (r : ℝ) (p : Plane) :
    PressureStream.torusAverage
        ((selectedMixedProductionPointScalar a) n) (r, p) =
      selectedMixedProductionScalar a
        (pointToCyl (r, (p, (0, 0)))) := by
  simp [PressureStream.torusAverage, PressureStream.torusInner,
    selectedMixedProductionPointScalar, pointToCyl]

theorem selected_mixed_barMoment_radial_reduction
    (a : ℕ → ℕ) (k n : ℕ) (p : Plane) :
    DefectIncrementBounds.barMoment k
        (selectedMixedProductionPointScalar a) n p =
      ∫ r, r ^ k * selectedMixedProductionScalar a
        (pointToCyl (r, (p, (0, 0)))) := by
  rw [DefectIncrementBounds.barMoment_apply]
  congr 1
  funext r
  rw [torusAverage_selected_mixed_production]

end NavierStokesReview.SelectedMixedProductionTorusAverage
