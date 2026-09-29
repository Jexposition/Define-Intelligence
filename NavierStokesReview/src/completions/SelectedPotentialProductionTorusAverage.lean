import completions.SelectedPotentialProductionFinitePrefix

/-!
# Finite-prefix torus-average reduction

The lifted finite-prefix scalar currently factors through `pointToCyl`, which
does not inspect the auxiliary `Plane` coordinate.  The two interval
integrals in `torusAverage` therefore reduce exactly to the same scalar value.
This is a selected finite-prefix identity; it is not yet an evaluation of the
remaining radial integral.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialProductionTorusAverage

open NavierStokes
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedPotentialProductionBarMomentSection
open NavierStokesReview.SelectedPotentialProductionFinitePrefix

theorem torusAverage_selected_potential_partial_production
    (a : ℕ → ℕ) (N n : ℕ) (r : ℝ) (p : Plane) :
    PressureStream.torusAverage
        ((selectedPotentialPartialProductionPointScalar a N) n) (r, p) =
      selectedPotentialPartialProductionScalar a N
        (pointToCyl (r, (p, (0, 0)))) := by
  simp [PressureStream.torusAverage, PressureStream.torusInner,
    selectedPotentialPartialProductionPointScalar, pointToCyl]

theorem finite_prefix_barMoment_radial_reduction
    (a : ℕ → ℕ) (N k n : ℕ) (p : Plane) :
    DefectIncrementBounds.barMoment k
        (selectedPotentialPartialProductionPointScalar a N) n p =
      ∫ r, r ^ k * selectedPotentialPartialProductionScalar a N
        (pointToCyl (r, (p, (0, 0)))) := by
  rw [DefectIncrementBounds.barMoment_apply]
  congr 1
  funext r
  rw [torusAverage_selected_potential_partial_production]

end NavierStokesReview.SelectedPotentialProductionTorusAverage
