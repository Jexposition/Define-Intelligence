import NavierStokes.ActualCandidateAssembly
import NavierStokes.PositiveOrderMoments

/-!
# Selected physical-data interface

This probe keeps the selected path in view while testing the exact scope of
`ActualCycleResidualBounds.PhysicalData`.  The selected source supplies the
physical-data record used by `ActualCandidateAssembly.estimates`, but that
record has no `PositiveOrderMoments.Debt` parameter or field.  Consequently an
arbitrary five-coordinate payload can be paired with the selected physical
data at the interface level.

This is a formal transport omission, not a theorem that the selected fields
violate the five moments.  The latter would require an equality between the
payload and integrals of the selected fields.
-/

noncomputable section

namespace NavierStokesReview.SelectedPhysicalDataMomentInterfaceProbe

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.PositiveOrderMoments

def ghostDebt : Debt := fun _ => 1

theorem ghostDebt_ne_zero : ghostDebt ≠ 0 := by
  intro h
  have h0 := congrFun h (0 : Fin 5)
  norm_num [ghostDebt] at h0

theorem selected_physical_data_coexists_with_unconstrained_five_debt :
    ∃ d : Debt, d ≠ 0 ∧
      (∀ J, ActualCycleResidualBounds.PhysicalData selectedBudget
        (ActualCandidateConstruction.residualBand selectedBudget selectedThreshold)
        (ActualCandidateConstruction.cycle selectedBudget selectedThreshold J).state
        (MixedDiagonalResidual.uncutVelocity
          (ActualCandidateAssembly.potentialStages selectedBudget selectedThreshold
            selectedThreshold_geometry)
          (ActualCandidateAssembly.directStages selectedBudget selectedThreshold
            selectedThreshold_geometry) J)
        (DiagonalJetBounds.uncutPrefix
          (ActualCandidateAssembly.pressureStages selectedBudget selectedThreshold
            selectedThreshold_geometry) (J + 1))) := by
  refine ⟨ghostDebt, ghostDebt_ne_zero, ?_⟩
  exact ActualCandidateAssembly.physicalData selectedBudget selectedThreshold
    selectedThreshold_geometry

end NavierStokesReview.SelectedPhysicalDataMomentInterfaceProbe
