import NavierStokes.FiveRowRank
import NavierStokes.FiveProfileMoments

/-!
# A small, zero-sorry correspondence test

The repository contains two moment systems.  `FiveProfileMoments` declares
the vectors used by the official paper's Appendix A.1 after setting
`b = -1/2 - λ`.  `FiveRowRank` declares a different pair of vectors and is
used by the physical five-row update.  These lemmas test that the two source
systems are not definitionally the same.

These lemmas do not refute the top-level theorem.  They formally establish
that a bridge between the two source systems cannot be mere definitional
equality.  A theorem identifying their rows, debts, bump coefficients, and
parameter normalisation is required before the two branches can be treated
as one verified moment construction.
-/

open NavierStokes.FiveRowRank

theorem rank_angular_powers_not_profile_powers (lam : ℝ) :
    angularPowers lam ≠
      NavierStokes.FiveProfileMoments.angularPowers (-1 / 2 - lam) := by
  intro h
  have h0 := congrFun h (0 : Fin 3)
  simp [angularPowers, NavierStokes.FiveProfileMoments.angularPowers] at h0
  norm_num at h0

theorem rank_axial_powers_not_profile_powers (lam : ℝ) :
    axialPowers lam ≠
      NavierStokes.FiveProfileMoments.axialPowers (-1 / 2 - lam) := by
  intro h
  have h0 := congrFun h (0 : Fin 2)
  simp [axialPowers, NavierStokes.FiveProfileMoments.axialPowers] at h0
