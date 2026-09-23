import NavierStokes.R3.ActualCandidate
import NavierStokes.ActualCandidateAssembly

/-!
# Selected incompressibility audit

`selectedPotentialStages` are potential fields.  They are not the final
velocity field, so the CMI divergence obligation must be tested on the
curl-generated/localised velocity extracted from the selected witness.
-/

open Set

namespace NavierStokesR3.SelectedDivergenceAudit

open NavierStokesR3 ProblemStatement

#check NavierStokes.ActualCandidateAssembly.selectedPotentialStages
#check NavierStokes.SolenoidalDiagonal.divergence_velocitySum_on
#check NavierStokesR3.ActualCandidate.selected_candidate_one_with_early_zero

theorem selected_endpoint_divergence_free :
    ∃ u : VelocityField, ∃ p : PressureField, ∃ f : VelocityField,
      ∃ K : Set Space,
        CandidateProperties 1 u p f K ∧
          ∀ t ∈ Ico (0 : ℝ) 1, ∀ x : Space,
            NavierStokes.ProblemStatement.spatialDivergence u t x = 0 := by
  obtain ⟨u, p, f, K, hc, _⟩ :=
    NavierStokesR3.ActualCandidate.selected_candidate_one_with_early_zero
  exact ⟨u, p, f, K, hc, hc.divergence_free⟩

end NavierStokesR3.SelectedDivergenceAudit
