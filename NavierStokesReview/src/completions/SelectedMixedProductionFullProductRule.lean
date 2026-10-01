import completions.SelectedPotentialProductionRadialScalar
import completions.SelectedMixedProductionBranchSplit

/-!
# Selected mixed production: full radial product-rule composition

This theorem composes the actual selected potential and direct branches at the
radial section.  It exposes the cutoff-curl term, the cutoff-gradient
commutator, and the direct periodised branch in one identity.  It does not
assign a numerical value to the resulting radial integral and does not claim
the manuscript's five-observable transport theorem.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedProductionFullProductRule

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedProductionBranchSplit
open NavierStokesReview.SelectedPotentialProductionProductRule
open NavierStokesReview.SelectedPotentialProductionRadialScalar
open scoped ContDiff Topology

theorem selected_mixed_production_scalar_full_composition
    (a : ℕ → ℕ) (p : DirectAngularDiagonal.CylPoint)
    (hcoord : ∀ i : Fin 3,
      |(ActualMeanStageData.radialSection p).2 i| ≤ 1 / 2)
    (hA : DifferentiableAt ℝ
      (fun y : ProblemStatement.Space =>
        SelectedPotentialProductionProductRule.selectedPotentialSum a
          ((ActualMeanStageData.radialSection p).1, y))
      (ActualMeanStageData.radialSection p).2) :
    SelectedMixedProductionRadialComponent.selectedMixedProductionScalar a p =
      SpatialLocalization.spatialCutoff
          (ActualMeanStageData.radialSection p).2 *
          (SpatialCurl.spatialCurl
            (SelectedPotentialProductionProductRule.selectedPotentialSum a)
            (ActualMeanStageData.radialSection p)) 1 +
        (SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff
            (ActualMeanStageData.radialSection p).2).smulRight
            (SelectedPotentialProductionProductRule.selectedPotentialSum a
              (ActualMeanStageData.radialSection p)))) 1 +
        (PeriodicLocalization.periodize
          (SpatialLocalization.cutPotential
            (SelectedMixedProductionRadialComponent.selectedDirectSum a))
          (ActualMeanStageData.radialSection p)) 1 := by
  rw [SelectedMixedProductionRadialComponent.selected_mixed_production_scalar_split]
  rw [SelectedPotentialProductionRadialScalar.selected_potential_production_radial_scalar_eq
    a p hcoord hA]

end NavierStokesReview.SelectedMixedProductionFullProductRule
