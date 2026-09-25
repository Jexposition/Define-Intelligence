import NavierStokes.ActualCandidateAssembly
import NavierStokes.PositiveOrderMoments

/-!
# Selected-endpoint moment transport obstruction

This extension tests the exported selected endpoint, rather than an abstract
stage interface.  `ActualCandidateAssembly.Witness` is inhabited for the
selected parameters, but its proposition contains no five-coordinate debt,
moment array, or equality connecting the paper tuple to the selected mixed
fields.  Consequently a nonzero five-coordinate payload can coexist with the
selected witness at the type boundary.

The result is deliberately a non-implication theorem.  It does not assert
that the selected velocity has incorrect moments.  It proves that the
exported witness alone cannot certify the paper's five-moment transport; that
requires a further theorem equating the named integrals with the selected
velocity, pressure, residual, and force.
-/

noncomputable section

namespace NavierStokesReview.SelectedEndpointMomentTransportObstruction

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.PositiveOrderMoments

def witnessDebt : Debt := fun _ => 1

theorem witnessDebt_ne_zero : witnessDebt ≠ 0 := by
  intro h
  have h0 := congrFun h (0 : Fin 5)
  norm_num [witnessDebt] at h0

theorem selected_witness_compatible_with_nonzero_five_payload :
    ∃ d : Debt, d ≠ 0 ∧
      Witness selectedBudget selectedThreshold selectedThreshold_geometry := by
  exact ⟨witnessDebt, witnessDebt_ne_zero, selected_witness⟩

theorem selected_witness_does_not_export_five_moment_transport :
    ¬ (Witness selectedBudget selectedThreshold selectedThreshold_geometry →
      ∀ d : Debt, d = 0) := by
  intro h
  have hd : witnessDebt = 0 := h selected_witness witnessDebt
  exact witnessDebt_ne_zero hd

end NavierStokesReview.SelectedEndpointMomentTransportObstruction
