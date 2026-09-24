import NavierStokes.ActualParticularStageControls

/-!
# Selected active-pair reachability

This file isolates the non-vacuity condition used by the actual particular
stage controls.  The source code has an empty `ActivePair` branch, so the
audit must not infer non-vacuity merely from the existence of the surrounding
construction.  Conversely, once an actual selected label is supplied, its
chart-band lower bound gives an active pair at that same band.
-/

noncomputable section

namespace NavierStokesReview.SelectedActivePairReachability

open NavierStokes
open NavierStokes.CorrectionInitialization
open NavierStokes.ActualParticularStageControls

theorem active_pair_of_selected_label (B N0 : ℕ)
    (L : CorrectionInitialization.ActualPrimary.Label B N0) :
    Nonempty (ActivePair B N0) := by
  let l : ActualParticularStageControls.Label B N0 := (0, L)
  let n : ℕ := BaseChartJets.cellBand L
  have hband : 1 ≤ n := by
    dsimp [n]
    have hN : (ActualPrimary.choice B N0).prepared.N ≤ BaseChartJets.cellBand L :=
      L.property
    exact le_trans (by
      have hfour := ActualPrimaryCovariance.chosen_threshold_four B N0
      omega) hN
  refine ⟨⟨(l, n), ?_⟩⟩
  exact ⟨hband, CommonWindow.self_mem n⟩

theorem active_pair_nonempty_if_selected_label_nonempty (B N0 : ℕ)
    [Nonempty (CorrectionInitialization.ActualPrimary.Label B N0)] :
    Nonempty (ActivePair B N0) := by
  let L : CorrectionInitialization.ActualPrimary.Label B N0 :=
    Classical.choice (inferInstance : Nonempty (CorrectionInitialization.ActualPrimary.Label B N0))
  exact active_pair_of_selected_label B N0 L

end NavierStokesReview.SelectedActivePairReachability
