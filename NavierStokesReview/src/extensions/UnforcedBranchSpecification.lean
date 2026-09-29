import NavierStokes.R3.ProblemStatement

/-!
# Independent unforced branch: exact target predicate

This file is deliberately a specification boundary.  It does not reuse the
forced `selected_witness` theorem and it does not assert existence.  The force
is definitionally zero, so any future construction that inhabits
`unforcedCandidateStatement` must prove the unforced residual equation rather
than obtaining it by defining a force from a preselected trajectory.

The file belongs to the review-side `extensions` lane.  It does not modify
the OpenAI source tree.
-/

noncomputable section

open Set
open NavierStokesR3.ProblemStatement

namespace NavierStokesReview.Unforced

/-- The only admissible force in this independent branch. -/
def zeroForce : VelocityField := fun _ => 0

/-- The exact R³ candidate contract with the force fixed to `f ≡ 0`.

No existence theorem is asserted here.  This predicate is the load-bearing
target that a future solenoidal construction must inhabit. -/
def unforcedCandidateStatement (ν : ℝ) : Prop :=
  ∃ (u : VelocityField) (p : PressureField) (K : Set Space),
    CandidateProperties ν u p zeroForce K

/-- Any inhabitant of the independent target satisfies the zero-force PDE. -/
theorem unforced_candidate_has_zero_residual
    {ν : ℝ} {u : VelocityField} {p : PressureField} {K : Set Space}
    (h : CandidateProperties ν u p zeroForce K) :
    ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      navierStokesResidual ν u p t x = 0 := by
  intro t ht x
  simpa [zeroForce] using h.navier_stokes t ht x

end NavierStokesReview.Unforced
