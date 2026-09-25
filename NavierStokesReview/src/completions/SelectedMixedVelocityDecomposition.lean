import NavierStokes.ActualCandidateAssembly

/-!
# Selected mixed velocity decomposition

The production endpoint does not form one curl of a combined potential.  It
first curls the potential sum and then adds the direct angular sum.  This
completion records that order for the selected stage aliases so later radial
or commutator calculations cannot silently apply a curl identity to the wrong
summand.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedVelocityDecomposition

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open ProblemStatement
open scoped BigOperators

theorem selected_velocity_decomposition (a : ℕ → ℕ) :
    MixedDiagonalResidual.velocity (fun j => (a j : ℝ))
        (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
        selectedPotentialStages selectedDirectStages =
      fun z =>
        SolenoidalDiagonal.velocitySum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedPotentialStages z +
        SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedDirectStages z := by
  rfl

theorem selected_velocity_decomposition_at (a : ℕ → ℕ) (z : SpaceTime) :
    MixedDiagonalResidual.velocity (fun j => (a j : ℝ))
        (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
        selectedPotentialStages selectedDirectStages z =
      SolenoidalDiagonal.velocitySum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedPotentialStages z +
        SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedDirectStages z := by
  rfl

theorem selected_periodic_velocity_decomposition (a : ℕ → ℕ) :
    MixedPeriodicAssembly.periodicVelocity
        (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedPotentialStages)
        (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedDirectStages) =
      fun z =>
        SpatialLocalization.periodicVelocity
          (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
            (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
            selectedPotentialStages) z +
        PeriodicLocalization.periodize
          (SpatialLocalization.cutPotential
            (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
              (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
              selectedDirectStages)) z := by
  rfl

end NavierStokesReview.SelectedMixedVelocityDecomposition
