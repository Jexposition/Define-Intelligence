import NavierStokes.ComparatorSolution

/-!
# Independent CMI quantifier probe

This file does not re-prove the OpenAI result and contains no placeholders. It
re-states the exported whole-space and periodic propositions as local aliases,
then applies the exported declarations to those aliases. Its purpose is to
make the CMI-facing quantifiers visible in the review checkout without editing
the upstream source.
-/

namespace NavierStokesReview

local notation "ℝ³" => EuclideanSpace ℝ (Fin 3)

def cmiCStatement : Prop :=
  ∀ (ν : ℝ), 0 < ν →
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
      NavierStokes.Comparator.InitialVelocityConditionDecay u₀ ∧
      NavierStokes.Comparator.ForceConditionDecay f ∧
      ¬ (∃ v p,
        NavierStokes.Comparator.NavierStokesExistenceAndSmoothnessRn
          ν u₀ f v p)

def cmiDStatement : Prop :=
  ∀ (ν : ℝ), 0 < ν →
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
      NavierStokes.Comparator.InitialVelocityConditionPeriodic u₀ ∧
      NavierStokes.Comparator.ForceConditionPeriodic f ∧
      ¬ (∃ v p,
        NavierStokes.Comparator.NavierStokesExistenceAndSmoothnessPeriodic
          ν u₀ f v p)

example : cmiCStatement := by
  intro ν hν
  exact NavierStokes.Comparator.navier_stokes_breakdown_R3 ν hν

example : cmiDStatement := by
  intro ν hν
  exact NavierStokes.Comparator.navier_stokes_breakdown_periodic ν hν

#check NavierStokes.Comparator.navier_stokes_breakdown_R3
#check NavierStokes.Comparator.navier_stokes_breakdown_periodic

end NavierStokesReview
