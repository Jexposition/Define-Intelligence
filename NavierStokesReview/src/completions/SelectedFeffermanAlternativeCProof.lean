import NavierStokes.R3.Theorem
import NavierStokes.R3.ComparatorBridge

/-!
# Direct proof of the forced CMI Alternative (C) route

This completion records the positive theorem separately from the adverse
paper-to-endpoint correspondence audit.  It proves the exact comparator
proposition by destructuring the repository's whole-space candidate theorem:

* `theorem_1_1` supplies the same velocity, pressure, force, support, and
  `CandidateProperties` package for every positive viscosity;
* the same theorem supplies the nonexistence of a global smooth finite-energy
  solution for that force;
* `comparator_of_breakdown` maps those facts to Fefferman's Alternative (C)
  quantifiers, using zero initial data and the compact-force decay theorem.

This is a positive proof of the formal CMI (C) proposition.  It does not claim
that the public endpoint exports a separate final-Cartesian equality for every
five-moment consequence in the manuscript.  That is a distinct correspondence
claim and is audited separately.
-/

noncomputable section

namespace NavierStokesReview.SelectedFeffermanAlternativeCProof

open NavierStokes
open NavierStokesR3
open NavierStokesR3.ProblemStatement
open NavierStokes.ComparatorBridge

/-- The selected R³ construction supplies the complete internal candidate
package required by the repository's forced breakdown statement. -/
theorem selected_candidate_has_forced_breakdown
    (ν : ℝ) (hν : 0 < ν) :
    ∃ u : VelocityField, ∃ p : PressureField, ∃ f : VelocityField,
      ∃ K : Set Space,
        CandidateProperties ν u p f K ∧
          ¬ Nonempty (GlobalFiniteEnergySolution ν f) := by
  exact NavierStokesR3.theorem_1_1 ν hν

/-- Direct proof of Fefferman's forced Alternative (C) in the repository's
whole-space comparator formalisation. -/
theorem selected_proves_literal_fefferman_alternative_C
    (ν : ℝ) (hν : 0 < ν) :
    ∃ (u₀ : EuclideanSpace ℝ (Fin 3) → EuclideanSpace ℝ (Fin 3))
      (f : EuclideanSpace ℝ (Fin 3) → ℝ → EuclideanSpace ℝ (Fin 3)),
      Comparator.InitialVelocityConditionDecay u₀ ∧
        Comparator.ForceConditionDecay f ∧
        ¬ (∃ v p,
          Comparator.NavierStokesExistenceAndSmoothnessRn ν u₀ f v p) := by
  obtain ⟨u, p, f, K, hCandidate, hNoGlobal⟩ :=
    selected_candidate_has_forced_breakdown ν hν
  exact NavierStokesR3.comparator_of_breakdown hCandidate hNoGlobal

end NavierStokesReview.SelectedFeffermanAlternativeCProof

#print axioms NavierStokesReview.SelectedFeffermanAlternativeCProof.selected_proves_literal_fefferman_alternative_C
