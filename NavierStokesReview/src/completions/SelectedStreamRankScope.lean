import NavierStokes.ActualCandidateConstruction

/-!
# Selected stream and rank scope

This file composes the source identities that are actually available on the
selected stream path.  It records that the successor stream is assembled from
the temporal and rank families, and that the rank mass-zero premise is used
upstream when the rank potential is constructed.  It does not identify the
resulting Cartesian curl with a scalar `barMoment` input.
-/

noncomputable section

namespace NavierStokesReview.SelectedStreamRankScope

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokes.CorrectionInitialization.ActualPrimary

theorem selected_stream_successor_temporal_rank
    {B N0 : ℕ} (H : MeanCycleInput B N0) (j : ℕ) :
    streamMeanStages B N0 (j + 1) =
      ((ActualMeanPhysicalData.initialCycleData H).temporalFamily j).angularField +
        ((ActualMeanPhysicalData.initialCycleData H).rankFamily j).angularField := by
  calc
    streamMeanStages B N0 (j + 1) =
        ((ActualMeanPhysicalData.initialCycleData H).streamFamily j).angularField :=
      streamMeanStages_succ H j
    _ = ((ActualMeanPhysicalData.initialCycleData H).temporalFamily j).angularField +
        ((ActualMeanPhysicalData.initialCycleData H).rankFamily j).angularField :=
      (ActualMeanPhysicalData.CycleData.stream_angularField
        (ActualMeanPhysicalData.initialCycleData H) j)

theorem selected_stream_successor_moving
    {B N0 : ℕ} (H : MeanCycleInput B N0) (j : ℕ) :
    GaugeMomentBalances.MovingField
      standardRegion
      commonGauge.radial.inner
      commonGauge.radial.outer
      ((ActualMeanPhysicalData.initialCycleData H).streamFamily j).native := by
  exact ActualMeanPhysicalData.CycleData.stream_moving
    (ActualMeanPhysicalData.initialCycleData H) j

end NavierStokesReview.SelectedStreamRankScope
