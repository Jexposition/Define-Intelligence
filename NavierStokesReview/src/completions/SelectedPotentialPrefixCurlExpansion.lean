import completions.SelectedFieldFinitePrefix

/-!
# Selected potential prefix and curl transport

This completion applies the selected finite-prefix theorem to the spatial
curl.  It records the exact finite partial-potential representation of the
selected Cartesian velocity on the preterminal domain.  The further
expansion of that partial curl into stage curls still requires a per-stage
smoothness transport theorem on the same open set.  No radial projection or
non-vanishing remainder is asserted here.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialPrefixCurlExpansion

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open Set Filter ProblemStatement
open scoped Topology ContDiff BigOperators

theorem selected_potential_velocity_eventuallyEq_partial_curl :
    ∃ a : ℕ → ℕ,
      MixedCandidateWitness.SelectedSchedule CorrectionInitialization.ActualPrimary.h
        (ActualCandidateConstruction.qbig ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        selectedPotentialStages selectedDirectStages selectedPressureStages a ∧
      ∀ x : SpaceTime, x ∈ PhysicalWaveSum.preterminal →
        ∃ N : ℕ,
          SolenoidalDiagonal.velocitySum (fun j => (a j : ℝ))
              (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages =ᶠ[𝓝 x]
            (SpatialCurl.spatialCurl
              (SolenoidalDiagonal.partialPotential (fun j => (a j : ℝ))
                (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages N)) := by
  rcases NavierStokesReview.SelectedFieldFinitePrefix.selected_potential_sum_locally_finite with
    ⟨a, hschedule, hpartial⟩
  refine ⟨a, hschedule, ?_⟩
  intro x hx
  have hN := hpartial x hx
  rcases hN with ⟨N, hN⟩
  refine ⟨N, ?_⟩
  have hc := SolenoidalDiagonal.spatialCurl_eventuallyEq hN
  simpa only [SolenoidalDiagonal.velocitySum] using hc

end NavierStokesReview.SelectedPotentialPrefixCurlExpansion
