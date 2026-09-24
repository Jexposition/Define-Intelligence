import NavierStokes.FiveRowRank
import NavierStokes.ActualCandidateAssembly

/-!
# Boundary of the proposed five-row collision

The first two conjuncts of `FiveRowRank.FiveRows` are zero constraints on the
two correction functions.  They are not equations asserting that the selected
velocity has zero mass or zero angular momentum.  The remaining three rows
carry the arbitrary three-coordinate debt.

This probe records that distinction directly in Lean.  It is deliberately a
countercheck against an invalid route to `False`: the rank predicate is
inhabited for a nonzero debt, and the selected witness can be paired with a
nonzero three-coordinate rank debt because its exported type has no such
payload.
-/

noncomputable section

namespace NavierStokesReview.FiveRowCollisionBoundaryProbe

open NavierStokes
open NavierStokes.FiveRowRank
open NavierStokes.ActualCandidateAssembly

def nonzeroThreeDebt : FiveRowRank.Debt := fun _ => 1

theorem nonzeroThreeDebt_ne_zero : nonzeroThreeDebt ≠ 0 := by
  intro h
  have h0 := congrFun h (0 : Fin 3)
  norm_num [nonzeroThreeDebt] at h0

theorem fiveRows_admits_nonzero_debt :
    FiveRowRank.FiveRows (FiveRowRank.background 1 1) (fun _ => 0)
      nonzeroThreeDebt
      (FiveRowRank.deltaV 1 1 1 2 nonzeroThreeDebt)
      (FiveRowRank.gamma 1 1 1 2 nonzeroThreeDebt) := by
  exact FiveRowRank.five_rows 1 1 1 2 nonzeroThreeDebt
    (by norm_num) (by norm_num) (by norm_num) (by norm_num)

theorem selected_witness_and_nonzero_rank_debt_coexist :
    ∃ _w : Witness ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        ActualCandidateConstruction.selectedThreshold_geometry,
      FiveRowRank.FiveRows (FiveRowRank.background 1 1) (fun _ => 0)
        nonzeroThreeDebt
        (FiveRowRank.deltaV 1 1 1 2 nonzeroThreeDebt)
        (FiveRowRank.gamma 1 1 1 2 nonzeroThreeDebt) ∧
      nonzeroThreeDebt ≠ 0 := by
  exact ⟨selected_witness, fiveRows_admits_nonzero_debt, nonzeroThreeDebt_ne_zero⟩

end NavierStokesReview.FiveRowCollisionBoundaryProbe
