import NavierStokes.ActualCandidateAssembly

/-!
# Selected-field finite-prefix transport

This completion follows the concrete selected endpoint one step further than
the generic witness theorem.  It records the exact local meaning of the
selected `tsum`: at every preterminal point the selected schedule gives a
finite prefix, uniformly for all derivatives.  It deliberately does not
identify that prefix with a radial `barMoment`; that identification remains a
separate calculation obligation.
-/

noncomputable section

namespace NavierStokesReview.SelectedFieldFinitePrefix

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open Set Filter ProblemStatement
open scoped Topology ContDiff BigOperators

theorem selected_schedule_exists :
    ∃ a : ℕ → ℕ,
      MixedCandidateWitness.SelectedSchedule CorrectionInitialization.ActualPrimary.h
        (ActualCandidateConstruction.qbig ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        selectedPotentialStages selectedDirectStages selectedPressureStages a := by
  rcases ActualCandidateAssembly.selected_witness with
    ⟨a, hschedule, _⟩
  exact ⟨a, hschedule⟩

theorem selected_potential_sum_locally_finite :
    ∃ a : ℕ → ℕ,
      MixedCandidateWitness.SelectedSchedule CorrectionInitialization.ActualPrimary.h
        (ActualCandidateConstruction.qbig ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        selectedPotentialStages selectedDirectStages selectedPressureStages a ∧
      ∀ x : SpaceTime, x ∈ PhysicalWaveSum.preterminal →
        ∃ N : ℕ,
          SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
              (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages =ᶠ[𝓝 x]
            SolenoidalDiagonal.partialPotential (fun j => (a j : ℝ))
              (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages N := by
  rcases selected_schedule_exists with ⟨a, hschedule⟩
  refine ⟨a, hschedule, ?_⟩
  intro x hx
  exact SolenoidalDiagonal.potentialSum_eventuallyEq_partial
    hschedule.2.2.2.2.1
    (PhysicalWaveSum.physicalQ_smoothAt CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hx).continuousAt
    (PhysicalWaveSum.physicalQ_pos CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hx)
    selectedPotentialStages

theorem selected_potential_sum_all_jets_locally_finite :
    ∃ a : ℕ → ℕ,
      MixedCandidateWitness.SelectedSchedule CorrectionInitialization.ActualPrimary.h
        (ActualCandidateConstruction.qbig ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        selectedPotentialStages selectedDirectStages selectedPressureStages a ∧
      ∀ x : SpaceTime, x ∈ PhysicalWaveSum.preterminal →
        ∃ N : ℕ, ∀ k : ℕ,
          iteratedFDeriv ℝ k
              (SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
                (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages) =ᶠ[𝓝 x]
            iteratedFDeriv ℝ k
              (SolenoidalDiagonal.partialPotential (fun j => (a j : ℝ))
                (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages N) := by
  rcases selected_schedule_exists with ⟨a, hschedule⟩
  refine ⟨a, hschedule, ?_⟩
  intro x hx
  exact SolenoidalDiagonal.potentialSum_allJets_eventuallyEq_partial
    hschedule.2.2.2.2.1
    (PhysicalWaveSum.physicalQ_smoothAt CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hx).continuousAt
    (PhysicalWaveSum.physicalQ_pos CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hx)

end NavierStokesReview.SelectedFieldFinitePrefix
