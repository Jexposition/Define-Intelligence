import NavierStokes.ActualParticularStageControls
import NavierStokes.LocalScheduleWitness

noncomputable section

namespace NavierStokesReview.SelectedLabelInhabitabilityProbe

open NavierStokes
open NavierStokes.ActualParticularStageControls
open NavierStokes.CorrectionInitialization

/-!
# Selected-label inhabitability boundary

This probe separates three propositions that are easy to conflate:

* a supplied primary label gives an active pair;
* the active-pair type is itself inhabited;
* the diagonal `potentialSum` is defined.

The first implication is proved below.  The source also has an explicit
empty-index branch in its mean estimates and an empty-active-pair branch in
`ActualParticularStageControls.raw_jets`.  Neither branch, by itself, proves
that the selected candidate is vacuous.  In particular, `potentialSum` is a
`tsum` indexed by `ℕ`, not by `ActivePair`.
-/

theorem active_pair_of_label (B N0 : ℕ)
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

theorem active_pair_nonempty_if_label_nonempty (B N0 : ℕ)
    [Nonempty (CorrectionInitialization.ActualPrimary.Label B N0)] :
    Nonempty (ActivePair B N0) := by
  let L : CorrectionInitialization.ActualPrimary.Label B N0 :=
    Classical.choice (inferInstance :
      Nonempty (CorrectionInitialization.ActualPrimary.Label B N0))
  exact active_pair_of_label B N0 L

theorem empty_active_pair_makes_control_patch_empty {B N0 : ℕ}
    (hne : ¬ Nonempty (ActivePair B N0))
    (l : ActualParticularStageControls.Label B N0) (n : ℕ)
    (k : NavierStokes.TorusInverse.Frequency) :
    controlPatch l n k = ∅ := by
  ext z
  constructor
  · intro hz
    exact (hne ⟨⟨(l, n), hz.1⟩⟩).elim
  · intro hz
    exact hz.elim

/-! `potentialSum` is total at the type level even under the empty-pair branch. -/

theorem potentialSum_total_under_empty_active_pair {B N0 : ℕ}
    (_hne : ¬ Nonempty (ActivePair B N0)) (a : ℕ → ℕ) :
    ∃ v : ProblemStatement.VelocityField, v = LocalScheduleWitness.potentialSum a := by
  exact ⟨LocalScheduleWitness.potentialSum a, rfl⟩

theorem potentialSum_is_nat_indexed (a : ℕ → ℕ) :
    LocalScheduleWitness.potentialSum a =
      SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
        (PhysicalWaveSum.physicalQ ActualPrimary.h) ActualCandidateAssembly.selectedPotentialStages := by
  simp [LocalScheduleWitness.potentialSum]

end NavierStokesReview.SelectedLabelInhabitabilityProbe
