import NavierStokes.GaugeMomentBalances
import NavierStokes.FiveRowRank
import NavierStokes.MeanStateRegularity

/-!
# Regularity is not the five-row solve

`GaugeMomentBalances.MovingField` records smoothness, radial support, and
periodicity.  It does not itself state any integral moment identity.  This
probe gives a zero-sorry countermodel to the implication from that regularity
interface to `FiveRowRank.FiveRows`: the zero moving field satisfies the former,
while a nonzero debt fails the third row of the latter when both background and
increments are zero.

This is an interface audit, not a refutation of the selected endpoint.  The
selected rank path supplies the stronger `RankGeometry.fiveRows` theorem.  The
probe prevents the review from incorrectly treating generic `MovingField`
premises as if they already carried the physical moment equations.
-/

noncomputable section

open Set Function MeasureTheory
open scoped BigOperators ContDiff Topology Interval

namespace NavierStokesReview

open NavierStokes

theorem movingField_does_not_imply_fiveRows
    {coord : ℝ} (U : LocalSignedRequest.SlowRegion coord) (a b : ℝ) :
    ∃ (f : CorrectionState.ScalarField GaugeMomentBalances.Point),
      GaugeMomentBalances.MovingField U a b f ∧
        ¬ FiveRowRank.FiveRows (fun _ => 0) (fun _ => 0) (fun _ : Fin 3 => 1)
          (fun _ => 0) (fun _ => 0) := by
  refine ⟨0, ?_, ?_⟩
  · exact NavierStokes.MeanStateRegularity.MovingField.zero
  · intro h
    have hthird := h.2.2.1
    norm_num at hthird

end NavierStokesReview
