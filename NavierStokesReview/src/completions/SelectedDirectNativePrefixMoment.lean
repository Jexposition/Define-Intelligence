import completions.SelectedDirectStageMomentTransport
import NavierStokes.ActualCandidateConstruction

/-!
# Selected direct native prefix

This file closes the finite-prefix calculation for the selected native direct
scalar.  The prefix telescopes to the corresponding cycle state, so its
order-two `barMoment` is zero on the selected carrier.  The result is scoped
to the native scalar before Cartesian localisation and does not identify that
moment with the exported mixed velocity.
-/

noncomputable section

namespace NavierStokesReview.SelectedDirectNativePrefixMoment

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokesReview.SelectedDirectStageMomentTransport

private abbrev selectedScalar : ℕ → ActualMeanPhysicalData.Scalar :=
  fun j => angularNativeStages selectedBudget selectedThreshold j

theorem selected_direct_native_scalar_prefix_eq_cycle_mean
    (J n : ℕ) :
    (fun z => ∑ j ∈ Finset.range (J + 1), selectedScalar j n z) =
      (selectedCycle J).state.mean.angular n := by
  funext z
  induction J with
  | zero =>
      simp [selectedScalar, angularNativeStages, selectedCycle, cycle_zero]
  | succ J ih =>
      rw [Finset.sum_range_succ, ih]
      change (selectedCycle J).state.mean.angular n z +
        ((selectedCycle (J + 1)).state.mean.angular -
          (selectedCycle J).state.mean.angular) n z = _
      simp only [Pi.sub_apply]
      ring

theorem selected_direct_native_scalar_prefix_barMoment_zero
    (J n : ℕ) {s : PressureStream.Plane}
    (hs : ActualInitialization.geometry.region.carrier s) :
    DefectIncrementBounds.barMoment 2
        (fun m z => ∑ j ∈ Finset.range (J + 1), selectedScalar j m z)
        n s = 0 := by
  have hscalar :
      (fun m z => ∑ j ∈ Finset.range (J + 1), selectedScalar j m z) =
        (selectedCycle J).state.mean.angular := by
    funext m z
    exact congrFun (selected_direct_native_scalar_prefix_eq_cycle_mean J m) z
  rw [hscalar]
  exact SelectedCycleMomentTransport.selected_cycle_mean_angular_barMoment_zero J n hs

end NavierStokesReview.SelectedDirectNativePrefixMoment
