import NavierStokes.R3.WholeSpaceUniqueness

/-!
# R³ comparison-premise audit

This probe records the source-level fact that the whole-space comparison
theorem does not accept a rate bound as an external premise.  The closure
module constructs that bound internally from `ComparisonRateBound` after
obtaining the pressure-flux estimate from `PressureFlux`.
-/

noncomputable section

open Set MeasureTheory

namespace NavierStokesReview.R3ComparisonPremise

open NavierStokesR3 Comparison

example {C0 C1 CP : ℝ} (hC0 : 0 ≤ C0) (hC1 : 0 ≤ C1) (hCP : 0 ≤ CP) :
    ∃ D ≥ 0, ∀ R ≥ 1, ∀ A ≥ 0, ∀ B ≥ 0,
      B ≤ 1 * (A + 1 / R) →
      ∀ E E' G : ℝ,
        (1 / 2 : ℝ) * E' + A ^ 2 ≤ G * E + C0 / R ^ 2 +
          C1 / R * B ^ (3 / 2 : ℝ) +
          CP * ((B ^ (1 / 2 : ℝ) + 1) * (A / R + 1 / R ^ 2) +
            R ^ (-7 / 4 : ℝ) * B ^ (3 / 4 : ℝ)) →
        E' ≤ 2 * G * E + D / R := by
  simpa only [one_mul] using
    ComparisonRateBound.exists_uniform_rate_bound (S := (1 : ℝ)) (M := (1 : ℝ))
      hC0 hC1 hCP (by norm_num) (by norm_num)

end NavierStokesReview.R3ComparisonPremise

#print axioms NavierStokesR3.WholeSpaceUniqueness.classical_uniqueness_on_Icc
#print axioms NavierStokesR3.WholeSpaceUniqueness.candidate_global_agrees_before_one
