import NavierStokes.ComparatorR3Theorem

/-!
# Literal Fefferman Alternative (C) cross-walk

This review-side declaration restates the exact whole-space forced alternative
exported by the repository.  It is deliberately separate from the paper-level
five-moment correspondence audit: the two propositions must not be conflated.
The cross-walk does not claim that the paper's selected-field moment identities
have been exported.  It records only the literal CMI proposition actually
proved by the repository theorem.
-/

noncomputable section

namespace NavierStokesReview

open NavierStokes

/--
The repository's exported forced theorem has the same existential shape as
Fefferman's Alternative (C): positive viscosity, rapidly decaying smooth initial
data and force, and no globally smooth uniformly finite-energy solution for the
same data.  The proof is delegated to the repository theorem, not re-created
by this review probe.
-/
theorem literal_fefferman_alternative_C
    (ν : ℝ) (hν : 0 < ν) :
    ∃ (u₀ : EuclideanSpace ℝ (Fin 3) → EuclideanSpace ℝ (Fin 3))
      (f : EuclideanSpace ℝ (Fin 3) → ℝ → EuclideanSpace ℝ (Fin 3)),
      Comparator.InitialVelocityConditionDecay u₀ ∧
        Comparator.ForceConditionDecay f ∧
        ¬ (∃ v p,
          Comparator.NavierStokesExistenceAndSmoothnessRn ν u₀ f v p) :=
  NavierStokes.ComparatorBridge.navier_stokes_breakdown_R3 ν hν

end NavierStokesReview

#print axioms NavierStokesReview.literal_fefferman_alternative_C
