import completions.SelectedMixedProductionBranchSplit
import NavierStokes.DefectIncrementBounds

/-!
# Selected mixed production: conditional `barMoment` linearity

The selected mixed scalar is the sum of the potential and direct branches.
The source `barMoment_add` theorem applies only to scalar families carrying
the common `Shell` regularity and radial-support hypotheses.  This file
records the exact conditional transport statement and leaves those hypotheses
visible.  It does not assert a numerical value for the selected moment.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedProductionBarMomentLinearity

open NavierStokes
open NavierStokes.DefectIncrementBounds
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedProductionBarMoment
open NavierStokesReview.SelectedMixedProductionBranchSplit
open NavierStokesReview.SelectedPotentialProductionBarMomentSection

abbrev MomentPoint := DefectIncrementBounds.Point PhysicalResidualBridge.Plane

theorem selected_mixed_production_point_scalar_eq_branch_sum
    (a : ℕ → ℕ) :
    selectedMixedProductionPointScalar a =
      selectedPotentialProductionPointScalar a +
        selectedDirectProductionPointScalar a := by
  funext n q
  exact selected_mixed_production_point_scalar_branch_split a n q

theorem selected_mixed_production_barMoment_add
    (a : ℕ → ℕ) {α β : ℝ}
    (hPotential : Shell α β (selectedPotentialProductionPointScalar a))
    (hDirect : Shell α β (selectedDirectProductionPointScalar a))
    (k : ℕ) :
    barMoment k (selectedMixedProductionPointScalar a) =
      barMoment k (selectedPotentialProductionPointScalar a) +
        barMoment k (selectedDirectProductionPointScalar a) := by
  rw [selected_mixed_production_point_scalar_eq_branch_sum]
  exact barMoment_add hPotential hDirect k

end NavierStokesReview.SelectedMixedProductionBarMomentLinearity
