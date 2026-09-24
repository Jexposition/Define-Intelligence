import NavierStokes.MeanRankUpdate

/-!
# Runtime rank interface: exact scope of the two zero rows

This file exposes the literal algebra of `MeanRankUpdate` and the scope of
`FiveRowRank.FiveRows`. It is deliberately not a transport theorem to the
exported velocity field.
-/

noncomputable section

namespace NavierStokesReview.MeanRankUpdateAudit

open NavierStokes
open scoped BigOperators

theorem scaleDebt_coordinates (ell U : ℝ) (d : MeanRankUpdate.Debt) :
    MeanRankUpdate.scaleDebt ell U d 0 = U ^ 2 * d 0 ∧
    MeanRankUpdate.scaleDebt ell U d 1 = ell ^ 3 * U ^ 2 * d 1 ∧
    MeanRankUpdate.scaleDebt ell U d 2 = ell ^ 2 * U ^ 2 * d 2 := by
  simp [MeanRankUpdate.scaleDebt]

theorem fiveRows_zero_rows_are_correction_moments
    {V G : ℝ → ℝ} {d : FiveRowRank.Debt} {dv ga : ℝ → ℝ}
    (h : FiveRowRank.FiveRows V G d dv ga) :
    (∫ R, R ^ (2 : ℕ) * dv R) = 0 ∧
      (∫ R, R * ga R) = 0 := by
  rcases h with ⟨h1, h2, _, _, _⟩
  exact ⟨h1, h2⟩

theorem nonzero_debt_is_compatible_with_zero_rows
    (lam C a b : ℝ) (hlam : 0 < lam) (hC : C ≠ 0)
    (ha : 0 < a) (hab : a < b) :
    ∃ (dv ga : ℝ → ℝ),
      FiveRowRank.FiveRows (FiveRowRank.background lam C) (fun _ => 0)
        (![1, 0, 0] : FiveRowRank.Debt) dv ga := by
  exact ⟨FiveRowRank.deltaV lam C a b (![1, 0, 0]),
    FiveRowRank.gamma lam C a b (![1, 0, 0]),
    FiveRowRank.five_rows lam C a b (![1, 0, 0]) hlam hC ha hab⟩

end NavierStokesReview.MeanRankUpdateAudit
