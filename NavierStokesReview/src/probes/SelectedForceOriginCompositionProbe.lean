import NavierStokes.ActualCandidateAssembly
import NavierStokes.LocalScheduleWitness

/-!
# Selected raw-residual to final-force composition

This probe checks whether the selected raw mixed residual is actually carried
into the final force at the singular origin.  It is deliberately separate
from the upstream construction and contains no admitted declarations.
-/

noncomputable section

open Set Filter
open NavierStokes
open NavierStokes.ProblemStatement
open scoped Topology ContDiff

namespace NavierStokesReview.SelectedForceOriginCompositionProbe

theorem periodic_residual_origin
    (A v : VelocityField) (p : PressureField) (t : ℝ) :
    MixedPeriodicAssembly.periodicResidual A v p (t, 0) =
      MixedPeriodicAssembly.originalResidual A v p (t, 0) := by
  have hzinner : (0 : Space) ∈ PeriodicLocalization.innerCube (1 / 4) :=
    SpatialLocalization.plateau_subset_innerCube SpatialLocalization.zero_mem_plateau
  have hcut := MixedPeriodicAssembly.periodicResidual_eventuallyEq_cut A v p
    (z := (t, 0)) hzinner
  have horiginal := MixedPeriodicAssembly.cutResidual_eventuallyEq_original A v p
    (z := (t, 0)) SpatialLocalization.zero_mem_plateau
  have he : MixedPeriodicAssembly.periodicResidual A v p =ᶠ[𝓝 (t, 0)]
      MixedPeriodicAssembly.originalResidual A v p := hcut.trans horiginal
  exact he.self_of_nhds

theorem selected_force_tends_to_zero_at_origin :
    ∃ (a : ℕ → ℕ) (forcing : VelocityField),
      NavierStokes.LocalScheduleWitness.Selected a ∧
      CandidateProperties
        (TimeLocalization.activatedVelocity
          (MixedPeriodicAssembly.periodicVelocity
            (NavierStokes.LocalScheduleWitness.potentialSum a)
            (NavierStokes.LocalScheduleWitness.directSum a)))
        (TimeLocalization.activatedPressure
          (SpatialLocalization.periodicPressure
            (NavierStokes.LocalScheduleWitness.pressureSum a))) forcing ∧
      Tendsto (fun t : ℝ => ‖forcing (t, 0)‖)
        (𝓝[<] (1 : ℝ)) (𝓝 0) := by
  obtain ⟨a, ha, _, _, _, forcing, hc, _, _, _, _, _⟩ :=
    NavierStokes.ActualCandidateAssembly.selected_witness
  have ha' : NavierStokes.LocalScheduleWitness.Selected a := by
    change NavierStokes.MixedCandidateWitness.SelectedSchedule
      NavierStokes.CorrectionInitialization.ActualPrimary.h
      (NavierStokes.ActualCandidateConstruction.qbig
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold)
      (NavierStokes.ActualCandidateAssembly.potentialStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry)
      (NavierStokes.ActualCandidateAssembly.directStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry)
      (NavierStokes.ActualCandidateAssembly.pressureStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry) a
    exact ha
  have hc' : CandidateProperties
      (TimeLocalization.activatedVelocity
        (MixedPeriodicAssembly.periodicVelocity
          (NavierStokes.LocalScheduleWitness.potentialSum a)
          (NavierStokes.LocalScheduleWitness.directSum a)))
      (TimeLocalization.activatedPressure
        (SpatialLocalization.periodicPressure
          (NavierStokes.LocalScheduleWitness.pressureSum a))) forcing := by
    simpa only [NavierStokes.LocalScheduleWitness.potentialSum,
      NavierStokes.LocalScheduleWitness.directSum,
      NavierStokes.LocalScheduleWitness.pressureSum,
      NavierStokes.ActualCandidateAssembly.selectedPotentialStages,
      NavierStokes.ActualCandidateAssembly.selectedDirectStages,
      NavierStokes.ActualCandidateAssembly.selectedPressureStages] using hc
  have hkeep := ha'
  obtain ⟨_, _, _, _, _, _, _, hz⟩ := ha'
  have hpath : Tendsto (fun t : ℝ => (t, (0 : Space)))
      (𝓝[<] (1 : ℝ))
      (𝓝[NavierStokes.SpacetimeEndpoint.openPast 1] ((1 : ℝ), (0 : Space))) := by
    rw [NavierStokes.JointResidualLimits.past_filter]
    exact tendsto_id.prodMk tendsto_const_nhds
  have hres : Tendsto (fun t : ℝ => ‖MixedPeriodicAssembly.originalResidual
      (NavierStokes.LocalScheduleWitness.potentialSum a)
      (NavierStokes.LocalScheduleWitness.directSum a)
      (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0)‖)
      (𝓝[<] (1 : ℝ)) (𝓝 0) := by
    have hcomp := (hz 0).comp hpath
    simpa only [MixedDiagonalResidual.residual_eq_originalResidual,
      NavierStokes.LocalScheduleWitness.potentialSum,
      NavierStokes.LocalScheduleWitness.directSum,
      NavierStokes.LocalScheduleWitness.pressureSum,
      Function.comp_apply, norm_iteratedFDeriv_zero, norm_zero] using hcomp.norm
  have hforce_raw : ∀ᶠ t in 𝓝[<] (1 : ℝ),
      forcing (t, 0) = MixedPeriodicAssembly.originalResidual
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a)
        (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0) := by
    filter_upwards [self_mem_nhdsWithin,
      mem_nhdsWithin_of_mem_nhds
        (Ioi_mem_nhds (show (3 / 4 : ℝ) < 1 by norm_num))] with t ht hlate
    change t ∈ Iio (1 : ℝ) at ht
    change (3 / 4 : ℝ) < t at hlate
    have hvel := TimeLocalization.activatedVelocity_eventuallyEq_late
      (MixedPeriodicAssembly.periodicVelocity
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a)) hlate 0
    have hpre := TimeLocalization.activatedPressure_eventuallyEq_late
      (SpatialLocalization.periodicPressure
        (NavierStokes.LocalScheduleWitness.pressureSum a)) hlate 0
    have hresEq := ResidualRegularity.residual_eventuallyEq hvel hpre
    calc
      forcing (t, 0) = navierStokesResidual
          (TimeLocalization.activatedVelocity
            (MixedPeriodicAssembly.periodicVelocity
              (NavierStokes.LocalScheduleWitness.potentialSum a)
              (NavierStokes.LocalScheduleWitness.directSum a)))
          (TimeLocalization.activatedPressure
            (SpatialLocalization.periodicPressure
              (NavierStokes.LocalScheduleWitness.pressureSum a))) t 0 :=
          (hc'.navier_stokes t ⟨by linarith, ht⟩ 0).symm
      _ = MixedPeriodicAssembly.periodicResidual
          (NavierStokes.LocalScheduleWitness.potentialSum a)
          (NavierStokes.LocalScheduleWitness.directSum a)
          (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0) := by
        have hp := hresEq.self_of_nhds
        simpa only [MixedPeriodicAssembly.periodicResidual] using hp
      _ = MixedPeriodicAssembly.originalResidual
          (NavierStokes.LocalScheduleWitness.potentialSum a)
          (NavierStokes.LocalScheduleWitness.directSum a)
          (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0) :=
        periodic_residual_origin _ _ _ _
  have hnorm : (fun t : ℝ => ‖MixedPeriodicAssembly.originalResidual
      (NavierStokes.LocalScheduleWitness.potentialSum a)
      (NavierStokes.LocalScheduleWitness.directSum a)
      (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0)‖) =ᶠ[𝓝[<] (1 : ℝ)]
      (fun t : ℝ => ‖forcing (t, 0)‖) :=
    hforce_raw.mono (fun t ht => (congrArg norm ht).symm)
  exact ⟨a, forcing, hkeep, hc', hres.congr' hnorm⟩

end NavierStokesReview.SelectedForceOriginCompositionProbe
