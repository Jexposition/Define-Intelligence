import NavierStokes.DiagonalResidual

/-!
Specification probe: `JetRate` accepts an arbitrary filter. On the bottom
filter every eventual proposition is true, so a rate can be discharged for an
arbitrary, even nonsmooth, function without any derivative estimate. This is
not a claim that the main construction uses the bottom filter; call sites must
therefore be checked for a nontrivial-domain witness.
-/

open Filter

namespace NavierStokesReview

example {D V : Type*} [NormedAddCommGroup D] [NormedSpace ℝ D]
    [NormedAddCommGroup V] [NormedSpace ℝ V]
    (q : D → ℝ) (f : D → V) (m : ℕ) (r : ℝ) :
    NavierStokes.DiagonalResidual.JetRate (⊥ : Filter D) q f m r := by
  refine ⟨0, le_rfl, ?_⟩
  simp

end NavierStokesReview
