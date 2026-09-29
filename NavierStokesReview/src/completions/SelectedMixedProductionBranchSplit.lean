import completions.SelectedMixedProductionBarMoment

/-!
# Selected mixed production: branch split on the `barMoment` domain

The mixed scalar-family pullback is decomposed into the already defined
potential branch and the separately cut, periodised direct branch.  This is a
pointwise algebraic identity.  It deliberately stops before any integral
linearity, support cancellation, or numerical sign claim.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedProductionBranchSplit

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ActualMeanStageData
open NavierStokes.DefectIncrementBounds
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokes.ProblemStatement
open NavierStokesReview.SelectedMixedProductionBarMoment
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedPotentialProductionBarMomentSection
open NavierStokesReview.SelectedPotentialProductionRadialScalar
open scoped BigOperators

abbrev MomentPoint := DefectIncrementBounds.Point PhysicalResidualBridge.Plane

noncomputable def selectedDirectProductionScalar (a : ℕ → ℕ)
    (p : DirectAngularDiagonal.CylPoint) : ℝ :=
  (PeriodicLocalization.periodize
    (SpatialLocalization.cutPotential (selectedDirectSum a))
    (ActualMeanStageData.radialSection p)) 1

noncomputable def selectedDirectProductionPointScalar (a : ℕ → ℕ) :
    DefectIncrementBounds.ScalarField MomentPoint :=
  fun _ q => selectedDirectProductionScalar a (pointToCyl q)

theorem selected_mixed_production_point_scalar_branch_split
    (a : ℕ → ℕ) (n : ℕ) (q : MomentPoint) :
    selectedMixedProductionPointScalar a n q =
      selectedPotentialProductionPointScalar a n q +
        selectedDirectProductionPointScalar a n q := by
  rw [selected_mixed_production_point_scalar_apply,
    selected_potential_production_point_scalar_apply]
  exact selected_mixed_production_scalar_split a (pointToCyl q)

end NavierStokesReview.SelectedMixedProductionBranchSplit
