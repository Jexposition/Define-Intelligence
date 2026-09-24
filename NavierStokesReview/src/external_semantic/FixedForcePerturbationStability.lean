import extensions.CompactFixedForcePerturbation

noncomputable section

namespace NavierStokesReview.FixedForcePerturbationStability

open Set
open NavierStokes ProblemStatement
open scoped Topology ContDiff

def AdmissiblePerturbation (e : VelocityField) : Prop :=
  ContDiff ℝ ∞ e ∧
    (∀ t : ℝ, HasCompactSupport (fun x : Space => e (t, x))) ∧
    (∀ t : ℝ, ∀ x : Space, spatialDivergence e t x = 0)

def FixedForceStable (u : VelocityField) (p : PressureField) (f : VelocityField) : Prop :=
  ∀ _t₀ : ℝ, ∀ e : VelocityField, AdmissiblePerturbation e →
    ∀ t : ℝ, ∀ x : Space,
      navierStokesResidual (fun z => u z + e z) p t x = f (t, x)

theorem compactPerturbation_admissible (t₀ : ℝ) :
    AdmissiblePerturbation (compactPerturbation t₀) := by
  refine ⟨compactPerturbation_contDiff t₀, ?_, ?_⟩
  · intro t
    exact compactPerturbation_slice_hasCompactSupport t₀ t
  · intro t x
    exact compactPerturbation_divergence_free t₀ t x

theorem selected_candidate_fails_fixed_force_stability :
    ∃ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f ∧ ¬ FixedForceStable u p f := by
  obtain ⟨u, p, f, hc, hneq⟩ := selected_candidate_fixed_force_obstruction
  refine ⟨u, p, f, hc, ?_⟩
  intro hstable
  have heq := hstable ((1 : ℝ) / 2) (compactPerturbation ((1 : ℝ) / 2))
    (compactPerturbation_admissible ((1 : ℝ) / 2)) ((1 : ℝ) / 2) 0
  exact hneq heq

end NavierStokesReview.FixedForcePerturbationStability
