import NavierStokes.R3ActualCandidate
import NavierStokes.ActualCandidateAssembly
import NavierStokes.PositiveOrderMoments

/-!
# Selected-witness path trace

This probe follows the exported witness into the whole-space wrapper.  It is
deliberately not a claim that the selected velocity violates the five physical
moments.  It records the exact formal boundary: the R3 wrapper transports the
periodic candidate properties, but the resulting proposition still has no
`PositiveOrderMoments.Debt` field or moment equality.
-/

noncomputable section

namespace NavierStokesReview.SelectedWitnessPathProbe

open NavierStokes.ActualCandidateAssembly
open NavierStokes.PositiveOrderMoments

theorem selected_periodic_properties_are_exported :
    ∃ u : NavierStokes.ProblemStatement.VelocityField,
      ∃ p : NavierStokes.ProblemStatement.PressureField,
      ∃ f : NavierStokes.ProblemStatement.VelocityField,
      NavierStokes.ProblemStatement.CandidateProperties u p f := by
  obtain ⟨a, _, ea, eb, ep, forcing, hc, _⟩ := selected_witness
  exact ⟨_, _, forcing, hc⟩

theorem selected_path_reaches_r3_only_through_localization :
    ∃ u : NavierStokes.ProblemStatement.VelocityField,
      ∃ p : NavierStokes.ProblemStatement.PressureField,
      ∃ f : NavierStokes.ProblemStatement.VelocityField,
      NavierStokes.R3CompactCandidate.Properties u p f := by
  exact NavierStokes.R3CompactCandidate.selected_compact_candidate

theorem selected_r3_envelope_coexists_with_unconstrained_five_debt :
    ∃ u : NavierStokes.ProblemStatement.VelocityField,
      ∃ p : NavierStokes.ProblemStatement.PressureField,
      ∃ f : NavierStokes.ProblemStatement.VelocityField,
      ∃ d : Debt, NavierStokes.R3CompactCandidate.Properties u p f ∧ d ≠ 0 := by
  obtain ⟨u, p, f, h⟩ := NavierStokes.R3CompactCandidate.selected_compact_candidate
  let d : Debt := fun _ => 1
  refine ⟨u, p, f, d, h, ?_⟩
  intro hd
  have hd0 := congrFun hd (0 : Fin 5)
  norm_num [d] at hd0

end NavierStokesReview.SelectedWitnessPathProbe
