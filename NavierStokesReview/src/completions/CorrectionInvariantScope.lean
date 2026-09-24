import NavierStokes.DefectIncrementBounds

/-!
# Scope of the five-row correction invariant

This file records the strongest contradiction that follows from the two zero
rows without adding an unproved bridge to the exported Cartesian velocity.
The zero rows force two radial moments of the correction increment to vanish.
They do not state that the selected velocity has zero kinetic energy, nor do
they identify either radial moment with a CMI energy quantity.
-/

noncomputable section

namespace NavierStokesReview.CorrectionInvariantScope

open NavierStokes
open NavierStokes.DefectIncrementBounds
open MeanIncrementBounds

variable {P : Type} [NormedAddCommGroup P] [NormedSpace ℝ P]

theorem five_rows_force_zero_correction_moments
    {o : Operators (Point P)} {base m h : Triple (Point P)}
    {W : Fin 3 → Fin 3 → ScalarField (Point P)}
    (hv : IsSlow h.angular) (hg : IsSlow h.axial)
    (hrows : ∀ n p, FiveRowRank.FiveRows (slowSlice base.angular n p)
      (slowSlice base.axial n p) (defects o base m W n p)
      (slowSlice h.angular n p) (slowSlice h.axial n p)) :
    barMoment 2 h.angular = 0 ∧ barMoment 1 h.axial = 0 := by
  exact fiveRows_mass_zero hv hg hrows

theorem nonzero_angular_shift_cannot_satisfy_five_rows
    {o : Operators (Point P)} {base m h : Triple (Point P)}
    {W : Fin 3 → Fin 3 → ScalarField (Point P)}
    (hv : IsSlow h.angular) (hg : IsSlow h.axial)
    (hrows : ∀ n p, FiveRowRank.FiveRows (slowSlice base.angular n p)
      (slowSlice base.axial n p) (defects o base m W n p)
      (slowSlice h.angular n p) (slowSlice h.axial n p))
    (hshift : barMoment 2 h.angular ≠ 0) : False := by
  exact hshift (five_rows_force_zero_correction_moments hv hg hrows).1

theorem nonzero_axial_shift_cannot_satisfy_five_rows
    {o : Operators (Point P)} {base m h : Triple (Point P)}
    {W : Fin 3 → Fin 3 → ScalarField (Point P)}
    (hv : IsSlow h.angular) (hg : IsSlow h.axial)
    (hrows : ∀ n p, FiveRowRank.FiveRows (slowSlice base.angular n p)
      (slowSlice base.axial n p) (defects o base m W n p)
      (slowSlice h.angular n p) (slowSlice h.axial n p))
    (hshift : barMoment 1 h.axial ≠ 0) : False := by
  exact hshift (five_rows_force_zero_correction_moments hv hg hrows).2

end NavierStokesReview.CorrectionInvariantScope
