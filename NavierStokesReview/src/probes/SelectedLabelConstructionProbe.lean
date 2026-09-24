import NavierStokes.PrimaryRepresentatives
import NavierStokes.PositiveRepresentatives
import NavierStokes.ActualCandidateAssembly
import NavierStokes.ActualParticularStageControls

noncomputable section

namespace NavierStokesReview.SelectedLabelConstructionProbe

open Set Function Filter
open NavierStokes
open NavierStokes.PrimaryRepresentatives
open NavierStokes.PositiveRepresentatives
open NavierStokes.ActualParticularStageControls
open NavierStokes.CorrectionInitialization

/-!
  A source-level construction of an active label from a point of the active set.

  This is deliberately kept independent of the selected witness.  It records
  the exact amount of inhabitability supplied by the partition-of-unity
  construction: a point in the relevant set, together with positive time for
  the positive branch, is enough to construct a label.
-/

theorem primary_activeLabel_at_band_of_mem {K : Set PrimaryRepresentatives.Slow}
    {p : PrimaryRepresentatives.Slow} (hp : p ∈ K) (n : ℕ) (hn : 1 ≤ n) :
    ∃ A : PrimaryRepresentatives.ActiveLabel K, A.val.1 = n := by
  have hsum := SquaredPartition.slowMask_sum_sq n (PrimaryRepresentatives.position p)
  have hmask : ∃ k : SlotColoring.Grid,
      SquaredPartition.slowMask n k (PrimaryRepresentatives.position p) ≠ 0 := by
    by_contra h
    push_neg at h
    have hz : (∑ᶠ k : SlotColoring.Grid,
        SquaredPartition.slowMask n k (PrimaryRepresentatives.position p) ^ 2) = 0 :=
      finsum_eq_zero_of_forall_eq_zero (fun k => by simp [h k])
    linarith [hsum, hz]
  obtain ⟨k, hk⟩ := hmask
  refine ⟨⟨⟨n, k⟩, hn, ?_⟩, rfl⟩
  refine ⟨p, hp, ?_⟩
  apply subset_closure
  change SquaredPartition.slowMask n k (PrimaryRepresentatives.position p) ≠ 0
  exact hk

theorem primary_activeLabel_nonempty_of_mem {K : Set PrimaryRepresentatives.Slow}
    {p : PrimaryRepresentatives.Slow} (hp : p ∈ K) :
    Nonempty (PrimaryRepresentatives.ActiveLabel K) := by
  obtain ⟨A, _⟩ := primary_activeLabel_at_band_of_mem hp 1 (by norm_num)
  exact ⟨A⟩

theorem positive_activeLabel_nonempty_of_mem
    {K : Set PrimaryRepresentatives.Slow}
    {p : PrimaryRepresentatives.Slow} (hp : p ∈ K)
    (hT : 0 < p.2.2) :
    Nonempty (PositiveRepresentatives.ActiveLabel K) := by
  exact primary_activeLabel_nonempty_of_mem (K := PositiveRepresentatives.positivePart K)
    (p := p) ⟨hp, hT⟩

theorem positive_activeLabel_at_band_of_mem
    {K : Set PrimaryRepresentatives.Slow}
    {p : PrimaryRepresentatives.Slow} (hp : p ∈ K)
    (hT : 0 < p.2.2) (n : ℕ) (hn : 1 ≤ n) :
    ∃ A : PositiveRepresentatives.ActiveLabel K, A.val.1 = n := by
  obtain ⟨A, hA⟩ := primary_activeLabel_at_band_of_mem
    (K := PositiveRepresentatives.positivePart K) (p := p) ⟨hp, hT⟩ n hn
  exact ⟨A, hA⟩

theorem reference_positive_activeLabel_nonempty
    {h a b : ℝ} (hh : 0 < h) (hh1 : h < 1 / 2)
    (ha : 0 < a) (hab : a ≤ b) :
    Nonempty (PositiveRepresentatives.ActiveLabel
      (PrimaryRepresentatives.referenceCompact h a b)) := by
  let p : PrimaryRepresentatives.Slow := (Real.sqrt (2 * a), (0, 1))
  have hp_active : p ∈ PrimaryRepresentatives.activeReference h a b := by
    refine ⟨?_, by norm_num, ?_⟩
    · exact Real.sqrt_nonneg _
    · refine ⟨1, ⟨by norm_num, by norm_num⟩, ?_, ?_⟩
      · simp [p, SimilarityCoordinates.forwardScalar]
      · have hs : (Real.sqrt (2 * a)) ^ 2 = 2 * a := by
          rw [Real.sq_sqrt]
          positivity
        dsimp [p]
        rw [hs]
        constructor <;> nlinarith
  have hp_compact : p ∈ PrimaryRepresentatives.referenceCompact h a b :=
    subset_closure hp_active
  exact positive_activeLabel_nonempty_of_mem hp_compact (by norm_num [p])

theorem reference_positive_activeLabel_at_band
    {h a b : ℝ} (hh : 0 < h) (hh1 : h < 1 / 2)
    (ha : 0 < a) (hab : a ≤ b) (n : ℕ) (hn : 1 ≤ n) :
    ∃ A : PositiveRepresentatives.ActiveLabel
      (PrimaryRepresentatives.referenceCompact h a b), A.val.1 = n := by
  let p : PrimaryRepresentatives.Slow := (Real.sqrt (2 * a), (0, 1))
  have hp_active : p ∈ PrimaryRepresentatives.activeReference h a b := by
    refine ⟨?_, by norm_num, ?_⟩
    · exact Real.sqrt_nonneg _
    · refine ⟨1, ⟨by norm_num, by norm_num⟩, ?_, ?_⟩
      · simp [p, SimilarityCoordinates.forwardScalar]
      · have hs : (Real.sqrt (2 * a)) ^ 2 = 2 * a := by
          rw [Real.sq_sqrt]
          positivity
        dsimp [p]
        rw [hs]
        constructor <;> nlinarith
  have hp_compact : p ∈ PrimaryRepresentatives.referenceCompact h a b :=
    subset_closure hp_active
  exact positive_activeLabel_at_band_of_mem hp_compact (by norm_num [p]) n hn

theorem selected_primary_label_nonempty (B N0 : ℕ) :
    Nonempty (CorrectionInitialization.ActualPrimary.Label B N0) := by
  let n : ℕ := max (CorrectionInitialization.ActualPrimary.choice B N0).prepared.N 1
  obtain ⟨A, hA⟩ := reference_positive_activeLabel_at_band
    (h := CorrectionInitialization.ActualPrimary.h)
    (a := NominalConeAssembly.activeLeft CorrectionInitialization.ActualPrimary.nominal)
    (b := NominalConeAssembly.activeRight CorrectionInitialization.ActualPrimary.nominal)
    CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
    CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half
    (NominalConeAssembly.activeLeft_pos CorrectionInitialization.ActualPrimary.nominal)
    (le_of_lt (PrimaryGeometryAssembly.active_order
      (W := CorrectionInitialization.ActualPrimary.nominal)))
    n (by exact le_max_right _ _)
  refine ⟨⟨A, ?_⟩⟩
  change (CorrectionInitialization.ActualPrimary.choice B N0).prepared.N ≤ A.val.1
  rw [hA]
  exact le_max_left _ _

theorem selected_active_pair_nonempty (B N0 : ℕ) :
    Nonempty (ActualParticularStageControls.ActivePair B N0) := by
  obtain ⟨L⟩ := selected_primary_label_nonempty B N0
  let l : ActualParticularStageControls.Label B N0 := (0, L)
  let n : ℕ := BaseChartJets.cellBand L
  have hband : 1 ≤ n := by
    dsimp [n]
    have hN : (CorrectionInitialization.ActualPrimary.choice B N0).prepared.N ≤
        BaseChartJets.cellBand L := L.property
    exact le_trans (by
      have hfour := NavierStokes.ActualPrimaryCovariance.chosen_threshold_four B N0
      omega) hN
  exact ⟨⟨(l, n), hband, CommonWindow.self_mem n⟩⟩

end NavierStokesReview.SelectedLabelConstructionProbe
