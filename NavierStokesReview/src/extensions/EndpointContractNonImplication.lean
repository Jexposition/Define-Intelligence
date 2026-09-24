import extensions.SameDatumFixedForcePerturbation

noncomputable section

namespace NavierStokesReview.EndpointContractNonImplication

open NavierStokes.ProblemStatement
open NavierStokesReview.SameDatumFixedForcePerturbation

/-!
# What the exported candidate contract does not imply

The selected construction supplies a candidate satisfying `CandidateProperties`,
but the exported contract does not quantify over same-datum perturbations with
the force and pressure held fixed.  The theorem below records that this is a
genuine logical non-implication, using the selected candidate and the
same-datum fixed-force obstruction.
-/

theorem candidateProperties_does_not_imply_fixedForceSameDatumStable :
    ¬ (∀ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f → FixedForceSameDatumStable u p f) := by
  intro h
  obtain ⟨u, p, f, hc, hnot⟩ := selected_candidate_fails_fixed_force_same_datum_stability
  exact hnot (h u p f hc)

end NavierStokesReview.EndpointContractNonImplication
