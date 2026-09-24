import NavierStokes.ActualCandidateAssembly

open Set

namespace NavierStokesReview

open NavierStokes
open NavierStokes.ProblemStatement

/-!
This file records the selected-path provenance of the force.  It is an
operator-level fact about the exported witness, not an additional admissibility
condition and not a disproof of the existential C/D proposition.
-/

theorem selected_candidate_force_is_residual_output :
    ∃ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f ∧
        ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
          f (t, x) = navierStokesResidual u p t x := by
  obtain ⟨u, p, f, hc⟩ := NavierStokes.ActualCandidateAssembly.selected_candidate
  refine ⟨u, p, f, hc, ?_⟩
  intro t ht x
  exact (hc.navier_stokes t ht x).symm

end NavierStokesReview
