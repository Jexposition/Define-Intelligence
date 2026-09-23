import NavierStokes.CandidateConsequences

/-!
# Force activity before the asserted singular time

This is a zero-sorry semantic probe.  It records the strongest conclusion
available from the repository's own candidate interface: a candidate force
cannot vanish throughout `(0,1)`.  The result is relevant to causal or
autonomous interpretations, but it is not a refutation of Fefferman C/D,
which allow a smooth external force.
-/

namespace NavierStokesReview

open Set
open NavierStokes
open NavierStokes.ProblemStatement

theorem force_nonzero_before_one_probe {u : VelocityField} {p : PressureField} {f : VelocityField}
    (h : CandidateProperties u p f) :
    ∃ t ∈ Ioo (0 : ℝ) 1, ∃ x : Space, f (t, x) ≠ 0 := by
  exact (CandidateConsequences.consequences_of_candidate h).force_nonzero

#print axioms force_nonzero_before_one_probe

end NavierStokesReview
