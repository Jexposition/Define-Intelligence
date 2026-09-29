import completions.SelectedMixedVelocityDecomposition
import completions.SelectedPotentialStagewiseCurlOnPhysicalDomain

/-!
# Selected mixed velocity: finite local representatives

The selected endpoint adds the curl of the potential `tsum` to a separate
direct `tsum`.  This theorem records the strongest finite-prefix statement
available on the source physical domain: each branch has its own finite local
representative.  No common cutoff index, endpoint value, radial integral, or
nonzero remainder is inferred.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedVelocityFinitePrefix

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open Set Filter ProblemStatement
open scoped Topology ContDiff BigOperators

theorem selected_mixed_velocity_locally_finite :
    ∃ a : ℕ → ℕ,
      MixedCandidateWitness.SelectedSchedule CorrectionInitialization.ActualPrimary.h
        (ActualCandidateConstruction.qbig ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        selectedPotentialStages selectedDirectStages selectedPressureStages a ∧
      ∀ x : SpaceTime,
        x ∈ ActualCandidateConstruction.physicalDomain
            ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold →
        ∃ Np Nd : ℕ,
          MixedDiagonalResidual.velocity (fun j => (a j : ℝ))
              (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
              selectedPotentialStages selectedDirectStages =ᶠ[𝓝 x]
            (fun w =>
              (∑ j ∈ Finset.range Np,
                SpatialCurl.spatialCurl
                  (SolenoidalDiagonal.cutStage (fun k => (a k : ℝ))
                    (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                    selectedPotentialStages j) w) +
              SolenoidalDiagonal.partialPotential (fun j => (a j : ℝ))
                (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedDirectStages Nd w) := by
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
  have hp := SolenoidalDiagonal.velocitySum_eventuallyEq_sum
    hschedule.2.2.2.2.1 hU hqpos hq hstages.1 hx
  have hd := SolenoidalDiagonal.potentialSum_eventuallyEq_partial
    hschedule.2.2.2.2.1
    (hq.contDiffAt (hU.mem_nhds hx)).continuousAt
    (hqpos x hx) selectedDirectStages
  rcases hp with ⟨Np, hp⟩
  rcases hd with ⟨Nd, hd⟩
  refine ⟨Np, Nd, ?_⟩
  filter_upwards [hp, hd] with w hwp hwd
  rw [NavierStokesReview.SelectedMixedVelocityDecomposition.selected_velocity_decomposition_at]
  simpa only [selectedPotentialStages, selectedDirectStages] using
    congrArg₂ (fun u v : Space => u + v) hwp hwd

end NavierStokesReview.SelectedMixedVelocityFinitePrefix
