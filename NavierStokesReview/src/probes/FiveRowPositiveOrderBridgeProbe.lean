import NavierStokes.FiveRowRank
import NavierStokes.PositiveOrderMoments

/-!
  This probe tests the strongest constructive repair of the earlier
  correspondence objection.  The physical mean-rank debt has three entries
  `(P, Jθ, Jz)`.  The positive-order five-moment debt uses the same two fixed
  zero rows and embeds the three physical targets as `(0, 0, -P, -Jθ, -Jz)`.
  The probe deliberately checks definitions and exact moment identities,
  rather than relying on a type-size or import-graph argument.
-/

noncomputable section

open Set MeasureTheory
open NavierStokes

namespace NavierStokesReview.FiveRowPositiveOrderBridgeProbe

open FiveRowRank PositiveOrderMoments

def promoted (d : FiveRowRank.Debt) : PositiveOrderMoments.Debt :=
  ![0, 0, -(d 0), -(d 1), -(d 2)]

theorem repairU_eq_gamma (lam A a b : ℝ) (d : FiveRowRank.Debt) :
    PositiveOrderMoments.repairU lam A a b (promoted d) =
      FiveRowRank.gamma lam A a b d := by
  funext R
  simp [PositiveOrderMoments.repairU, FiveRowRank.gamma,
    PositiveOrderMoments.axialDebt, FiveRowRank.axialDebt, promoted]

theorem repairE_eq_deltaV (lam A a b : ℝ) (d : FiveRowRank.Debt) :
    PositiveOrderMoments.repairE lam A a b (promoted d) =
      FiveRowRank.deltaV lam A a b d := by
  funext R
  simp [PositiveOrderMoments.repairE, FiveRowRank.deltaV,
    PositiveOrderMoments.angularDebt, FiveRowRank.angularDebt, promoted]

theorem positive_order_exact_for_physical_repair
    (lam A a b : ℝ) (d : FiveRowRank.Debt)
    (hlam : 0 < lam) (hA : A ≠ 0) (ha : 0 < a) (hab : a < b) :
    ∀ i : Fin 5,
      PositiveOrderMoments.positiveIntegral
        (fun R => PositiveOrderMoments.weightedDensity lam A
          (FiveRowRank.gamma lam A a b d)
          (FiveRowRank.deltaV lam A a b d) R i) = promoted d i := by
  intro i
  rw [← repairU_eq_gamma lam A a b d, ← repairE_eq_deltaV lam A a b d]
  simpa only using
    (PositiveOrderMoments.weighted_moments_exact lam A a b (promoted d)
      hlam hA ha hab i)

end NavierStokesReview.FiveRowPositiveOrderBridgeProbe
