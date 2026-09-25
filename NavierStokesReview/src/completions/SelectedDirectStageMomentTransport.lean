import NavierStokes.ActualCandidateConstruction
import NavierStokes.ActualCyclePreservation
import completions.SelectedCycleMomentTransport

/-!
# Direct native-stage moment transport

This file checks the scalar angular branch used by the selected direct stages.
It proves the state-level zero-moment invariant transports through the native
stage differences.  It does not identify that scalar moment with a moment of
the final mixed Cartesian velocity.
-/

noncomputable section

namespace NavierStokesReview.SelectedDirectStageMomentTransport

open NavierStokes
open NavierStokes.ActualCandidateConstruction

private abbrev selectedRegion := ActualInitialization.geometry.region

private theorem selected_patch_inner_pos : 0 < ActualInitialization.geometry.patch.a :=
  ActualInitialization.geometry.patch.a_pos

private theorem selected_patch_inner_lt_outer :
    ActualInitialization.geometry.patch.a < ActualInitialization.geometry.patch.b :=
  ActualInitialization.geometry.patch.a_lt_left.trans
    (ActualInitialization.geometry.patch.left_lt_right.trans
      ActualInitialization.geometry.patch.right_lt_b)

theorem selected_angular_native_stage_moment_zero
    (j n : ℕ) {s : PressureStream.Plane}
    (hs : s ∈ selectedRegion.carrier) :
    DefectIncrementBounds.barMoment 2
        (angularNativeStages selectedBudget selectedThreshold j) n s = 0 := by
  cases j with
  | zero =>
      exact SelectedCycleMomentTransport.selected_cycle_mean_angular_barMoment_zero 0 n hs
  | succ j =>
      have hInv (k : ℕ) := ActualCyclePreservation.state_invariant
        selectedBudget selectedThreshold selectedThreshold_geometry k
      have hReg (k : ℕ) : GaugeDebtIncrement.Regular selectedRegion
          ActualInitialization.geometry.patch.a ActualInitialization.geometry.patch.b
          ((selectedCycle k).state.mean.angular) := by
        exact (hInv k).primitives.mean.regular.angular
      have hsub := GaugeDebtIncrement.radialMoment_sub_on selectedRegion
        selected_patch_inner_pos selected_patch_inner_lt_outer
        (hReg (j + 1)) (hReg j) 2 n hs
      change CorrectionState.radialMoment 2
        ((selectedCycle (j + 1)).state.mean.angular -
          (selectedCycle j).state.mean.angular) n s = 0
      rw [hsub]
      have hz1 : CorrectionState.radialMoment 2
          (selectedCycle (j + 1)).state.mean.angular n s = 0 := by
        exact SelectedCycleMomentTransport.selected_cycle_mean_angular_barMoment_zero
          (j + 1) n hs
      have hz0 : CorrectionState.radialMoment 2
          (selectedCycle j).state.mean.angular n s = 0 := by
        exact SelectedCycleMomentTransport.selected_cycle_mean_angular_barMoment_zero j n hs
      rw [hz1, hz0]
      simp

end NavierStokesReview.SelectedDirectStageMomentTransport
