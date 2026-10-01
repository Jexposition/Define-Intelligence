import completions.SelectedMixedProductionFullProductRule
import completions.SelectedMixedProductionTorusAverage

/-
# Selected mixed production: conditional radial integral composition

This theorem applies the exact selected mixed product-rule formula under the
weighted radial integral used by barMoment.  The pointwise composition is an
explicit hypothesis because the current production endpoint does not export a
global differentiability/coordinate theorem for every integration radius.
No support, sign, nonzero, or five-observable conclusion is inferred.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedProductionBarMomentProductRule

open NavierStokes
open NavierStokes.DefectIncrementBounds
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedProductionBarMoment
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedMixedProductionTorusAverage
open NavierStokesReview.SelectedPotentialProductionBarMomentSection
open NavierStokesReview.SelectedPotentialProductionProductRule
open MeasureTheory
open scoped BigOperators

theorem selected_mixed_barMoment_product_rule
    (a : ℕ → ℕ) (k n : ℕ) (p : Plane)
    (hcomposition :
      ∀ r : ℝ,
        selectedMixedProductionScalar a
            (pointToCyl (r, (p, (0, 0)))) =
          SpatialLocalization.spatialCutoff
              (ActualMeanStageData.radialSection
                (pointToCyl (r, (p, (0, 0))))).2 *
              (SpatialCurl.spatialCurl
                (SelectedPotentialProductionProductRule.selectedPotentialSum a)
                (ActualMeanStageData.radialSection
                  (pointToCyl (r, (p, (0, 0)))))) 1 +
            (SpatialCurl.curlLinear
              ((fderiv ℝ SpatialLocalization.spatialCutoff
                (ActualMeanStageData.radialSection
                  (pointToCyl (r, (p, (0, 0))))).2).smulRight
                (SelectedPotentialProductionProductRule.selectedPotentialSum a
                  (ActualMeanStageData.radialSection
                    (pointToCyl (r, (p, (0, 0)))))))) 1 +
            (PeriodicLocalization.periodize
              (SpatialLocalization.cutPotential
                (SelectedMixedProductionRadialComponent.selectedDirectSum a))
              (ActualMeanStageData.radialSection
                (pointToCyl (r, (p, (0, 0)))))) 1) :
    barMoment k (selectedMixedProductionPointScalar a) n p =
      ∫ r, r ^ k *
        (SpatialLocalization.spatialCutoff
            (ActualMeanStageData.radialSection
              (pointToCyl (r, (p, (0, 0))))).2 *
            (SpatialCurl.spatialCurl
              (SelectedPotentialProductionProductRule.selectedPotentialSum a)
              (ActualMeanStageData.radialSection
                (pointToCyl (r, (p, (0, 0)))))) 1 +
          (SpatialCurl.curlLinear
            ((fderiv ℝ SpatialLocalization.spatialCutoff
              (ActualMeanStageData.radialSection
                (pointToCyl (r, (p, (0, 0))))).2).smulRight
              (SelectedPotentialProductionProductRule.selectedPotentialSum a
                (ActualMeanStageData.radialSection
                  (pointToCyl (r, (p, (0, 0)))))))) 1 +
          (PeriodicLocalization.periodize
            (SpatialLocalization.cutPotential
              (SelectedMixedProductionRadialComponent.selectedDirectSum a))
            (ActualMeanStageData.radialSection
              (pointToCyl (r, (p, (0, 0)))))) 1) := by
  rw [selected_mixed_barMoment_radial_reduction]
  apply integral_congr_ae
  filter_upwards [] with r
  rw [hcomposition r]

end NavierStokesReview.SelectedMixedProductionBarMomentProductRule
