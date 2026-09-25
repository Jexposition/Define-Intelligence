import NavierStokes.ActualCandidateConstruction
import NavierStokes.ActualCyclePreservation

/-!
# Selected cycle mass preservation

This completion checks whether the mass invariant proved by the actual cycle
preservation theorem applies to the selected recurrence used by the exported
stage aliases.  It is deliberately a source-level identity, not an inference
from the paper's five-moment discussion.
-/

noncomputable section

namespace NavierStokesReview.SelectedCycleMasses

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ActualCyclePreservation

theorem selected_cycle_zeroMasses (j : ℕ) :
    GaugeMassPreservation.ZeroMassesOn
      ActualInitialization.geometry.region.carrier
      (selectedCycle j).state := by
  change GaugeMassPreservation.ZeroMassesOn
    ActualInitialization.geometry.region.carrier
    (ActualCyclePreservation.state selectedBudget selectedThreshold j).state
  exact (ActualCyclePreservation.state_invariant selectedBudget selectedThreshold
    selectedThreshold_geometry j).masses

end NavierStokesReview.SelectedCycleMasses
