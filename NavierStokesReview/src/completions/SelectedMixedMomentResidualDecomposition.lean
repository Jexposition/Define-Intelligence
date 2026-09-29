import completions.SelectedMixedProductionBarMomentLinearity

/-!
# Selected mixed production: explicit residual obligation

The selected mixed radial scalar splits into a potential branch and a direct
branch.  The existing native-stage theorem proves a zero order-two moment for
`angularNativeStages`; it does not, by itself, prove the same statement for
the selected direct production branch
`periodize (cutPotential (selectedDirectSum a))`.

This file therefore records the exact conditional reduction that remains at
the selected-field level.  It is deliberately not a contradiction and does
not identify the direct production branch with the native scalar.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedMomentResidualDecomposition

open NavierStokes
open NavierStokes.DefectIncrementBounds
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedProductionBarMoment
open NavierStokesReview.SelectedMixedProductionBarMomentLinearity
open NavierStokesReview.SelectedMixedProductionBranchSplit
open NavierStokesReview.SelectedPotentialProductionBarMomentSection

abbrev MomentPoint := DefectIncrementBounds.Point PhysicalResidualBridge.Plane

theorem selected_mixed_order_two_minus_potential_eq_direct
    (a : ℕ → ℕ) {α β : ℝ}
    (hPotential : Shell α β (selectedPotentialProductionPointScalar a))
    (hDirect : Shell α β (selectedDirectProductionPointScalar a)) :
    barMoment 2 (selectedMixedProductionPointScalar a) -
        barMoment 2 (selectedPotentialProductionPointScalar a) =
      barMoment 2 (selectedDirectProductionPointScalar a) := by
  rw [selected_mixed_production_barMoment_add a hPotential hDirect 2]
  abel

theorem selected_mixed_order_two_reduces_to_potential_residual
    (a : ℕ → ℕ) {α β : ℝ}
    (hPotential : Shell α β (selectedPotentialProductionPointScalar a))
    (hDirect : Shell α β (selectedDirectProductionPointScalar a))
    (hDirectZero :
      barMoment 2 (selectedDirectProductionPointScalar a) = 0) :
    barMoment 2 (selectedMixedProductionPointScalar a) =
      barMoment 2 (selectedPotentialProductionPointScalar a) := by
  rw [selected_mixed_production_barMoment_add a hPotential hDirect 2]
  rw [hDirectZero, add_zero]

theorem selected_mixed_order_two_zero_iff_potential_zero
    (a : ℕ → ℕ) {α β : ℝ}
    (hPotential : Shell α β (selectedPotentialProductionPointScalar a))
    (hDirect : Shell α β (selectedDirectProductionPointScalar a))
    (hDirectZero :
      barMoment 2 (selectedDirectProductionPointScalar a) = 0) :
    barMoment 2 (selectedMixedProductionPointScalar a) = 0 ↔
      barMoment 2 (selectedPotentialProductionPointScalar a) = 0 := by
  rw [selected_mixed_order_two_reduces_to_potential_residual
    a hPotential hDirect hDirectZero]

end NavierStokesReview.SelectedMixedMomentResidualDecomposition
