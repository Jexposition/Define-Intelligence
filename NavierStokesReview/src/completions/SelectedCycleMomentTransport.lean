import NavierStokes.ActualCandidateConstruction
import NavierStokes.ActualCyclePreservation

/-!
# Selected-cycle moment boundary

The production correction cycle does carry a local two-moment invariant inside
`CycleAnalyticInvariant`. This completion exposes that fact at the selected
cycle boundary. It does not identify the invariant with the paper's five
named moments or with the exported `Witness` fields.
-/

noncomputable section

namespace NavierStokesReview.SelectedCycleMomentTransport

open NavierStokes

theorem cycle_eq_preservation_state (B N0 j : ℕ) :
    ActualCandidateConstruction.cycle B N0 j =
      ActualCyclePreservation.state B N0 j := by
  unfold ActualCandidateConstruction.cycle ActualCyclePreservation.state
    ActualCandidateConstruction.parameterSequence
  rfl

theorem cycle_state_zero_masses
    (B N0 j : ℕ)
    (hN : ActualCarrierGeometry.geometricThreshold ≤ N0) :
    GaugeMassPreservation.ZeroMassesOn ActualInitialization.geometry.region.carrier
      (ActualCyclePreservation.state B N0 j).state :=
  (ActualCyclePreservation.state_invariant B N0 hN j).masses

theorem selected_cycle_state_zero_masses (j : ℕ) :
    GaugeMassPreservation.ZeroMassesOn ActualInitialization.geometry.region.carrier
      (ActualCandidateConstruction.selectedCycle j).state := by
  change GaugeMassPreservation.ZeroMassesOn ActualInitialization.geometry.region.carrier
    (ActualCandidateConstruction.cycle ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold j).state
  rw [cycle_eq_preservation_state]
  exact cycle_state_zero_masses ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold j
    ActualCandidateConstruction.selectedThreshold_geometry

theorem selected_cycle_nonzero_angular_moment_impossible
    (j n : ℕ) {s : PressureStream.Plane}
    (hs : s ∈ ActualInitialization.geometry.region.carrier)
    (hshift : CorrectionState.radialMoment 2
      (ActualCandidateConstruction.selectedCycle j).state.mean.angular n s ≠ 0) :
    False := by
  exact hshift ((selected_cycle_state_zero_masses j n s hs).1)

theorem selected_cycle_nonzero_axial_moment_impossible
    (j n : ℕ) {s : PressureStream.Plane}
    (hs : s ∈ ActualInitialization.geometry.region.carrier)
    (hshift : CorrectionState.radialMoment 1
      (ActualCandidateConstruction.selectedCycle j).state.mean.axial n s ≠ 0) :
    False := by
  exact hshift ((selected_cycle_state_zero_masses j n s hs).2)

end NavierStokesReview.SelectedCycleMomentTransport
