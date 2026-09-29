import NavierStokes.R3.ActualCandidate
import NavierStokes.PositiveOrderMoments

/-!
# R3 selected-witness packaging boundary

The whole-space candidate exports `CandidateProperties`, while the paper's
five-coordinate debt is a separate type.  This completion records the exact
non-implication at the R3 boundary: an arbitrary nonzero five-coordinate
payload can coexist with the exported candidate because no equality to that
payload occurs in the candidate type.

This is not a claim about the numerical moments of the selected field.  A
field-level calculation is still required for `Delta m != 0` or `False`.
-/

noncomputable section

namespace NavierStokesReview.SelectedR3PackagingBoundary

open NavierStokes.PositiveOrderMoments

def witnessDebt : Debt := fun _ => 1

theorem witnessDebt_ne_zero : witnessDebt ≠ 0 := by
  intro h
  have h0 := congrFun h (0 : Fin 5)
  norm_num [witnessDebt] at h0

theorem selected_r3_candidate_compatible_with_nonzero_five_payload :
    ∃ d : Debt, d ≠ 0 ∧
      ∃ (u : NavierStokesR3.ProblemStatement.VelocityField)
        (p : NavierStokesR3.ProblemStatement.PressureField)
        (f : NavierStokesR3.ProblemStatement.VelocityField)
        (K : Set NavierStokesR3.ProblemStatement.Space),
        NavierStokesR3.ProblemStatement.CandidateProperties 1 u p f K := by
  obtain ⟨u, p, f, K, hc⟩ :=
    NavierStokesR3.ActualCandidate.selected_candidate_one
  exact ⟨witnessDebt, witnessDebt_ne_zero, u, p, f, K, hc⟩

theorem selected_r3_candidate_does_not_export_five_payload_zero :
    ¬ (NavierStokesR3.ProblemStatement.candidateStatement 1 →
      ∀ d : Debt, d = 0) := by
  intro h
  have hd : witnessDebt = 0 := h
    NavierStokesR3.ActualCandidate.selected_candidate_one witnessDebt
  exact witnessDebt_ne_zero hd

end NavierStokesReview.SelectedR3PackagingBoundary
