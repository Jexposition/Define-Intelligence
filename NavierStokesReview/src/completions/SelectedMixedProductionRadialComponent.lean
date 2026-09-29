import completions.SelectedMixedVelocityDecomposition
import completions.SelectedPotentialProductionRadialScalar

/-!
# Selected mixed production radial component

The exported endpoint uses a mixed periodic velocity: the potential branch is
localised and the direct branch is cut and periodised separately.  This file
records that decomposition after taking the first Cartesian component on the
radial section.  It does not identify the mixed component with the scalar
`barMoment` representative and does not assert a nonzero moment.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedProductionRadialComponent

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ProblemStatement
open NavierStokesReview.SelectedMixedVelocityDecomposition
open NavierStokesReview.SelectedPotentialProductionProductRule
open NavierStokesReview.SelectedPotentialProductionRadialScalar

noncomputable def selectedDirectSum (a : ℕ → ℕ) :=
  SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
    (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
    selectedDirectStages

noncomputable def selectedMixedProductionScalar (a : ℕ → ℕ)
    (p : DirectAngularDiagonal.CylPoint) : ℝ :=
  (MixedPeriodicAssembly.periodicVelocity
      (selectedPotentialSum a) (selectedDirectSum a)
      (ActualMeanStageData.radialSection p)) 1

theorem selected_mixed_production_scalar_split
    (a : ℕ → ℕ) (p : DirectAngularDiagonal.CylPoint) :
    selectedMixedProductionScalar a p =
      selectedPotentialProductionScalar a p +
        (PeriodicLocalization.periodize
          (SpatialLocalization.cutPotential (selectedDirectSum a))
          (ActualMeanStageData.radialSection p)) 1 := by
  unfold selectedMixedProductionScalar selectedDirectSum selectedPotentialSum
  rw [selected_periodic_velocity_decomposition]
  rfl

end NavierStokesReview.SelectedMixedProductionRadialComponent
