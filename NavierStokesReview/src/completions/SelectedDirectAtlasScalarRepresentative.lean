import completions.SelectedRadialSectionComponent

/-!
# Selected direct atlas scalar

The direct production field evaluates `Atlas.physical` after composing it with
`PhysicalMeanJetBounds.physicalPoint`.  This file names the scalar family on
the domain consumed by `barMoment` and proves the corresponding composition
identity.  It is a transport result only: it does not identify this scalar
with the curled potential branch and does not assert a nonzero remainder.
-/

noncomputable section

namespace NavierStokesReview.SelectedDirectAtlasScalarRepresentative

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokes.DefectIncrementBounds
open NavierStokes.PressureStream

private abbrev selectedBudget := ActualCandidateConstruction.selectedBudget
private abbrev selectedThreshold := ActualCandidateConstruction.selectedThreshold
private abbrev selectedDegree :=
  CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h

noncomputable def selectedDirectAtlasScalar (j : ℕ) :
    ScalarField (Point Plane) :=
  fun _ z =>
    (ActualCandidateConstruction.meanAtlas selectedBudget selectedThreshold).physical
      CorrectionInitialization.ActualPrimary.standardRegion.carrier selectedDegree
      (ActualCandidateConstruction.angularNativeStages selectedBudget selectedThreshold j) z

theorem meanField_eq_selectedDirectAtlasScalar_pullback
    (j n : ℕ) (w : ProblemStatement.SpaceTime) :
    ActualCandidateConstruction.meanField selectedBudget selectedThreshold
        selectedDegree
        (ActualCandidateConstruction.angularNativeStages selectedBudget selectedThreshold j) w =
      selectedDirectAtlasScalar j n
        (PhysicalMeanJetBounds.physicalPoint
          CorrectionInitialization.ActualPrimary.h w) := by
  rfl

theorem selected_direct_atlas_scalar_barMoment_apply
    (j k n : ℕ) (p : Plane) :
    barMoment k (selectedDirectAtlasScalar j) n p =
      ∫ r, r ^ k * PressureStream.torusAverage
        ((selectedDirectAtlasScalar j) n) (r, p) := by
  exact barMoment_apply k (selectedDirectAtlasScalar j) n p

theorem selected_direct_radial_component_eq_atlas_scalar
    (j : ℕ) (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1) :
    (ActualCandidateAssembly.selectedDirectStages j
        (ActualMeanStageData.radialSection p)) 1 =
      selectedDirectAtlasScalar j 0
        (PhysicalMeanJetBounds.physicalPoint
          CorrectionInitialization.ActualPrimary.h
          (ActualMeanStageData.radialSection p)) := by
  rw [SelectedRadialSectionComponent.selected_direct_stage_radial_component_one j p hp]
  exact meanField_eq_selectedDirectAtlasScalar_pullback j 0
    (ActualMeanStageData.radialSection p)

end NavierStokesReview.SelectedDirectAtlasScalarRepresentative
