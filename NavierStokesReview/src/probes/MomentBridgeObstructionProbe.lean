import NavierStokes.FiveRowRank
import NavierStokes.FiveProfileMoments

/-!
# Obstruction to a direct row-by-row moment bridge

`FiveRowRank` and `FiveProfileMoments` are both used by the repository, but
their source power vectors are different.  This probe records the strongest
claim that follows from that fact without adding assumptions: no direct
row-by-row identification of the two systems can exist.

This is not, by itself, a refutation of the final Navier--Stokes theorem.  A
valid proof could still supply a nontrivial change-of-variables, restrict the
five-dimensional debt to a subspace, or prove that the two systems describe
different stages.  The probe therefore turns the review target into precise
missing-interface obligations rather than treating different declarations as
an automatic theorem-level contradiction.
-/

open NavierStokes.FiveRowRank

structure DirectMomentBridge (lam b : ℝ) : Prop where
  axial_powers_eq : axialPowers lam = NavierStokes.FiveProfileMoments.axialPowers b
  angular_powers_eq : angularPowers lam = NavierStokes.FiveProfileMoments.angularPowers b

theorem no_direct_axial_bridge (lam b : ℝ) :
    axialPowers lam ≠ NavierStokes.FiveProfileMoments.axialPowers b := by
  intro h
  have h0 := congrFun h (0 : Fin 2)
  simp [axialPowers, NavierStokes.FiveProfileMoments.axialPowers] at h0

theorem no_direct_angular_bridge (lam b : ℝ) :
    angularPowers lam ≠ NavierStokes.FiveProfileMoments.angularPowers b := by
  intro h
  have h0 := congrFun h (0 : Fin 3)
  simp [angularPowers, NavierStokes.FiveProfileMoments.angularPowers] at h0
  norm_num at h0

theorem no_direct_moment_bridge (lam b : ℝ) :
    ¬ DirectMomentBridge lam b := by
  intro h
  exact no_direct_axial_bridge lam b h.axial_powers_eq

theorem no_linear_debt_equivalence :
    ¬ Nonempty (NavierStokes.FiveRowRank.Debt ≃ₗ[ℝ]
      NavierStokes.FiveProfileMoments.Debt) := by
  rintro ⟨e⟩
  have h := LinearEquiv.finrank_eq e
  norm_num [NavierStokes.FiveRowRank.Debt,
    NavierStokes.FiveProfileMoments.Debt] at h
