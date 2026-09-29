import completions.SelectedPotentialPrefixCurlExpansion

/-!
# Selected potential: stagewise curl on the physical domain

The selected finite-prefix identity can be expanded into the curls of the
individual cut stages on the open domain on which the source actually exports
per-stage smoothness.  This is the source-backed entry point for the cutoff
commutator calculation.  No radial value or non-vanishing claim is built into
the theorem.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialStagewiseCurlOnPhysicalDomain

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open Set Filter ProblemStatement
open scoped Topology ContDiff BigOperators

theorem selected_potential_velocity_eventuallyEq_stage_curls_on_physicalDomain :
    ∃ a : ℕ → ℕ,
      MixedCandidateWitness.SelectedSchedule CorrectionInitialization.ActualPrimary.h
        (ActualCandidateConstruction.qbig ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        selectedPotentialStages selectedDirectStages selectedPressureStages a ∧
      ∀ x : SpaceTime,
        x ∈ ActualCandidateConstruction.physicalDomain
            ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold →
        ∃ N : ℕ,
          SolenoidalDiagonal.velocitySum (fun j => (a j : ℝ))
              (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages =ᶠ[𝓝 x]
            (fun w => ∑ j ∈ Finset.range N,
              SpatialCurl.spatialCurl
                (SolenoidalDiagonal.cutStage (fun k => (a k : ℝ))
                  (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                  selectedPotentialStages j) w) := by
  rcases NavierStokesReview.SelectedFieldFinitePrefix.selected_schedule_exists with
    ⟨a, hschedule⟩
  refine ⟨a, hschedule, ?_⟩
  intro x hx
  have hU : IsOpen
      (ActualCandidateConstruction.physicalDomain
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold) :=
    ActualCandidateConstruction.physicalDomain_open
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
  have hqpos : ∀ z ∈ ActualCandidateConstruction.physicalDomain
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold,
      0 < PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h z := by
    intro z hz
    exact PhysicalWaveSum.physicalQ_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hz.1
  have hq : ContDiffOn ℝ ∞
      (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
      (ActualCandidateConstruction.physicalDomain
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold) := by
    intro z hz
    exact (PhysicalWaveSum.physicalQ_smoothAt
      CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hz.1).contDiffWithinAt
  have hstages := ActualCandidateAssembly.stages_smooth
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    ActualCandidateConstruction.selectedThreshold_geometry
  exact SolenoidalDiagonal.velocitySum_eventuallyEq_sum
    hschedule.2.2.2.2.1 hU hqpos hq hstages.1 hx

end NavierStokesReview.SelectedPotentialStagewiseCurlOnPhysicalDomain
