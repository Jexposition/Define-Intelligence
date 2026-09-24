import NavierStokes.ActualCandidateAssembly
import NavierStokes.ActualCandidateConstruction
import NavierStokes.PositiveOrderMoments

/-!
# Selected-witness inhabitation boundary

This is an adversarial interface probe.  It does not claim that the selected
velocity violates the five physical moments.  It proves the stronger type-level
fact that the exported `Witness` proposition carries no `PositiveOrderMoments`
debt payload, so an arbitrary five-coordinate debt can coexist with an
inhabited witness unless an additional transport theorem is supplied.
-/

noncomputable section

namespace NavierStokesReview.SelectedWitnessInhabitationProbe

open NavierStokes.ActualCandidateAssembly
open NavierStokes.PositiveOrderMoments

def ghostDebt : Debt := fun _ => 1

theorem ghostDebt_is_nonzero : ghostDebt ≠ 0 := by
  intro h
  have h0 := congrFun h (0 : Fin 5)
  norm_num [ghostDebt] at h0

/-- The selected witness can be paired with a nonzero five-coordinate debt
    because the exported witness type contains no debt field or equality. -/
theorem selected_witness_coexists_with_unconstrained_ghost_debt :
    ∃ w : Witness NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry,
      ghostDebt ≠ 0 := by
  exact ⟨selected_witness, ghostDebt_is_nonzero⟩

/-- The same observation holds for every debt, not only the named ghost. -/
theorem selected_witness_signature_ignores_five_debt (d : Debt) :
    ∃ w : Witness NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry, d = d := by
  exact ⟨selected_witness, rfl⟩

end NavierStokesReview.SelectedWitnessInhabitationProbe
