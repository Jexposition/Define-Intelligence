import completions.SelectedPotentialProductionRadialScalar
import completions.SelectedPhysicalPointTransport

/-!
# Selected potential production: typed `barMoment` section

The production calculation is first available on the positive-radius
cylindrical section.  This file gives that calculation a genuine
`ScalarField (PressureStream.Lift P)` type, so that the source `barMoment`
operator can be applied without inventing an inverse for `physicalPoint`.

The construction is a section of the physical point coordinates.  It is a
transport interface, not yet an equality between the full selected Cartesian
field and this scalar family.  That equality remains a separate obligation.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialProductionBarMomentSection

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ActualMeanPotentialRealization
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokes.PhysicalResidualTZ
open NavierStokes.ProblemStatement
open NavierStokesReview.SelectedPotentialProductionRadialScalar
open scoped BigOperators ContDiff Topology

abbrev MomentPoint := DefectIncrementBounds.Point PhysicalResidualBridge.Plane

noncomputable def pointToCyl (q : MomentPoint) : DirectAngularDiagonal.CylPoint :=
  (1 - q.2.1.1, (q.1, q.2.1.2))

noncomputable def selectedPotentialProductionPointScalar (a : ℕ → ℕ) :
    DefectIncrementBounds.ScalarField MomentPoint :=
  fun _ q => selectedPotentialProductionScalar a (pointToCyl q)

theorem selected_potential_production_point_scalar_apply
    (a : ℕ → ℕ) (n : ℕ) (q : MomentPoint) :
    selectedPotentialProductionPointScalar a n q =
      selectedPotentialProductionScalar a (pointToCyl q) := rfl

theorem selected_potential_production_point_barMoment_apply
    (a : ℕ → ℕ) (k n : ℕ) (p : PhysicalResidualBridge.Plane) :
    DefectIncrementBounds.barMoment k
        (selectedPotentialProductionPointScalar a) n p =
      ∫ r, r ^ k * PressureStream.torusAverage
        ((selectedPotentialProductionPointScalar a) n) (r, p) := by
  exact DefectIncrementBounds.barMoment_apply k
    (selectedPotentialProductionPointScalar a) n p

theorem pointToCyl_physicalPoint_radialSection
    (h : ℝ) {p : DirectAngularDiagonal.CylPoint} (hp : 0 < p.2.1) :
    pointToCyl (PhysicalMeanJetBounds.physicalPoint h
      (ActualMeanStageData.radialSection p)) = p := by
  unfold pointToCyl PhysicalMeanJetBounds.physicalPoint
    ActualMeanStageData.radialSection
  simp only [PhysicalGraphBounds.radialProjection_apply,
    AxisymmetricResidual.pack_zero, AxisymmetricResidual.pack_one,
    AxisymmetricResidual.pack_two, PhysicalClassBounds.cartesianRadius]
  simp [Real.sqrt_sq hp.le]

theorem selected_potential_production_point_scalar_physical_pullback
    (h : ℝ) (a : ℕ → ℕ) {p : DirectAngularDiagonal.CylPoint} (hp : 0 < p.2.1) :
    selectedPotentialProductionPointScalar a 0
        (PhysicalMeanJetBounds.physicalPoint h
          (ActualMeanStageData.radialSection p)) =
      selectedPotentialProductionScalar a p := by
  rw [selected_potential_production_point_scalar_apply,
    pointToCyl_physicalPoint_radialSection h hp]

end NavierStokesReview.SelectedPotentialProductionBarMomentSection
