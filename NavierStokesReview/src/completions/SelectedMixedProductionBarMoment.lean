import completions.SelectedMixedProductionRadialComponent
import completions.SelectedPotentialProductionBarMomentSection

/-!
# Selected mixed production: typed `barMoment` interface

The exported velocity is the mixed periodic field used by `selected_witness`:
it contains both the potential and direct branches.  This file pulls its first
Cartesian component back to the scalar-family domain consumed by `barMoment`.
The result is an exact typing and coordinate-transport theorem.  It does not
assert that the mixed moment is zero or nonzero, and it does not identify the
mixed scalar with either branch separately.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedProductionBarMoment

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ActualMeanPotentialRealization
open NavierStokes.DefectIncrementBounds
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokes.PhysicalResidualTZ
open NavierStokes.PressureStream
open NavierStokes.ProblemStatement
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedPotentialProductionBarMomentSection
open scoped BigOperators ContDiff Topology

abbrev MomentPoint := DefectIncrementBounds.Point PhysicalResidualBridge.Plane

noncomputable def selectedMixedProductionPointScalar (a : ℕ → ℕ) :
    DefectIncrementBounds.ScalarField MomentPoint :=
  fun _ q => selectedMixedProductionScalar a (pointToCyl q)

theorem selected_mixed_production_point_scalar_apply
    (a : ℕ → ℕ) (n : ℕ) (q : MomentPoint) :
    selectedMixedProductionPointScalar a n q =
      selectedMixedProductionScalar a (pointToCyl q) := rfl

theorem selected_mixed_production_point_barMoment_apply
    (a : ℕ → ℕ) (k n : ℕ) (p : PhysicalResidualBridge.Plane) :
    DefectIncrementBounds.barMoment k
        (selectedMixedProductionPointScalar a) n p =
      ∫ r, r ^ k * PressureStream.torusAverage
        ((selectedMixedProductionPointScalar a) n) (r, p) := by
  exact DefectIncrementBounds.barMoment_apply k
    (selectedMixedProductionPointScalar a) n p

theorem selected_mixed_production_point_scalar_physical_pullback
    (h : ℝ) (a : ℕ → ℕ) {p : DirectAngularDiagonal.CylPoint} (hp : 0 < p.2.1) :
    selectedMixedProductionPointScalar a 0
        (PhysicalMeanJetBounds.physicalPoint h
          (ActualMeanStageData.radialSection p)) =
      selectedMixedProductionScalar a p := by
  rw [selected_mixed_production_point_scalar_apply,
    pointToCyl_physicalPoint_radialSection h hp]

end NavierStokesReview.SelectedMixedProductionBarMoment
