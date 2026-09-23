import NavierStokes.FiveRowRank

/-!
# Exact structure of the repository's five-row predicate

This probe records what `FiveRowRank.FiveRows` actually says.  The predicate
has a three-coordinate debt.  Its first two rows are fixed zero-moment
conditions and its last three rows use the three debt coordinates.  Thus the
source is not a generic five-target, five-unknown linear solve.

This is a structural correction to the review narrative, not a refutation of
the final C/D endpoint.  The first two rows can be validly enforced as
independent invariants, but any claim that this declaration itself supplies a
full five-dimensional inverse is false.
-/

open NavierStokes.FiveRowRank

theorem fiveRows_has_three_coordinate_debt :
    Debt = (Fin 3 → ℝ) := by
  rfl

theorem fiveRows_rows_are_explicit
    {V G : ℝ → ℝ} {d : Debt} {dv ga : ℝ → ℝ}
    (h : FiveRows V G d dv ga) :
    (∫ R, R ^ (2 : ℕ) * dv R) = 0 ∧
      (∫ R, R * ga R) = 0 ∧
      (∫ R, (2 * V R / R) * dv R) = -(d 0) ∧
      (∫ R, R ^ (2 : ℕ) * (G R * dv R + V R * ga R)) = -(d 1) ∧
      (∫ R, 2 * R * G R * ga R - R * V R * dv R) = -(d 2) := by
  exact h

theorem fiveRows_first_two_do_not_use_debt
    {V G : ℝ → ℝ} {d : Debt} {dv ga : ℝ → ℝ}
    (h : FiveRows V G d dv ga) :
    (∫ R, R ^ (2 : ℕ) * dv R) = 0 ∧
      (∫ R, R * ga R) = 0 := by
  exact ⟨h.1, h.2.1⟩

theorem fiveRows_last_three_use_all_debt_coordinates
    {V G : ℝ → ℝ} {d : Debt} {dv ga : ℝ → ℝ}
    (h : FiveRows V G d dv ga) :
    (∫ R, (2 * V R / R) * dv R) = -(d 0) ∧
      (∫ R, R ^ (2 : ℕ) * (G R * dv R + V R * ga R)) = -(d 1) ∧
      (∫ R, 2 * R * G R * ga R - R * V R * dv R) = -(d 2) := by
  exact ⟨h.2.2.1, h.2.2.2.1, h.2.2.2.2⟩
