import completions.SelectedRadialSectionComponent
import NavierStokes.SpatialLocalization

/-!
# Selected production direct scalar gate

The native direct radial moment is a statement about the uncut angular mean
profile.  The production field first applies `SpatialLocalization.cutPotential`.
This file records the exact component identity at the positive radial section,
including the cutoff factor.  It is a selected source identity, not a claim
that the resulting weighted moment is nonzero.
-/

noncomputable section

namespace NavierStokesReview.SelectedProductionDirectScalarGate

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokesReview.SelectedRadialSectionComponent

theorem cut_direct_component_one_radial
    (j : ℕ) (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1) :
    (SpatialLocalization.cutPotential (selectedDirectStages j)
      (ActualMeanStageData.radialSection p)) 1 =
      SpatialLocalization.spatialCutoff (ActualMeanStageData.radialSection p).2 *
        meanField ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold
          (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
          (angularNativeStages ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold j)
          (ActualMeanStageData.radialSection p) := by
  unfold SpatialLocalization.cutPotential
  simp only [PiLp.smul_apply, smul_eq_mul]
  rw [selected_direct_stage_radial_component_one j p hp]

theorem spatialCutoff_radialSection
    (p : DirectAngularDiagonal.CylPoint) :
    SpatialLocalization.spatialCutoff (ActualMeanStageData.radialSection p).2 =
      SmoothCutoffs.cutoff (16 * (p.2.1 ^ 2)) *
        SmoothCutoffs.cutoff (4 * p.2.2) := by
  unfold SpatialLocalization.spatialCutoff SpatialLocalization.cutoffProfile
    ActualMeanStageData.radialSection SpatialLocalization.radialSquare
  simp only [AxisymmetricResidual.pack_zero, AxisymmetricResidual.pack_one,
    AxisymmetricResidual.pack_two]
  ring_nf

end NavierStokesReview.SelectedProductionDirectScalarGate
