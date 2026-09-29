import NavierStokes.ActualCandidateAssembly

/-!
# Selected production direct branch after localisation

The selected direct profile has a native radial `barMoment` statement before
the production assembly.  The exported mixed velocity does not insert that
profile directly: it first multiplies the direct field by `spatialCutoff` and
then periodises it.  This file records the exact source identity on the
fundamental cube.  It is the required starting point for a field-level moment
calculation; it does not assume that the cutoff preserves a radial moment.
-/

noncomputable section

namespace NavierStokesReview.SelectedProductionDirectCutoff

open NavierStokes
open NavierStokes.ProblemStatement
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction

theorem mixed_periodic_velocity_eq_cut_direct_on_unitCube
    (A v : VelocityField) (t : ℝ) {x : Space}
    (hx : ∀ i : Fin 3, |x i| ≤ 1 / 2) :
    MixedPeriodicAssembly.periodicVelocity A v (t, x) =
      SpatialLocalization.periodicVelocity A (t, x) +
        SpatialLocalization.spatialCutoff x • v (t, x) := by
  rw [MixedPeriodicAssembly.periodicVelocity]
  rw [PeriodicLocalization.periodize_eq_on_unitCube
    (SpatialLocalization.cutPotential_supported v)
    (by norm_num : (1 / 4 : ℝ) < 1 / 2) hx t]
  rfl

theorem selected_mixed_velocity_eq_cut_direct_on_unitCube
    (a : ℕ → ℕ) (t : ℝ) {x : Space}
    (hx : ∀ i : Fin 3, |x i| ≤ 1 / 2) :
    MixedPeriodicAssembly.periodicVelocity
        (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedPotentialStages)
        (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedDirectStages) (t, x) =
      SpatialLocalization.periodicVelocity
        (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
          (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
          selectedPotentialStages) (t, x) +
        SpatialLocalization.spatialCutoff x •
          (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
            (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
            selectedDirectStages) (t, x) := by
  exact mixed_periodic_velocity_eq_cut_direct_on_unitCube _ _ t hx

end NavierStokesReview.SelectedProductionDirectCutoff
