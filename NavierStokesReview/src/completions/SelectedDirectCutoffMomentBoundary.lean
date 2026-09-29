import completions.SelectedProductionDirectScalarGate

/-!
# Selected direct branch: cutoff boundary identity

This completion closes a previously exposed inference gap at the selected
field level.  The native angular stage has a zero order-two `barMoment`, but
the production branch is formed after multiplication by the spatial cutoff.
The theorem below records the exact pointwise difference between those two
objects on the positive radial section.

It is not a nonzero-moment theorem.  It does not assume that the cutoff is
nonconstant on the support of the selected native scalar, and it does not
evaluate the periodised tsum.  Its purpose is to prevent the invalid rewrite
from an uncut native moment to the selected production moment.
-/

noncomputable section

namespace NavierStokesReview.SelectedDirectCutoffMomentBoundary

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokesReview.SelectedProductionDirectScalarGate

theorem cut_direct_component_one_radial_minus_native
    (j : ℕ) (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1) :
    (SpatialLocalization.cutPotential (selectedDirectStages j)
      (ActualMeanStageData.radialSection p)) 1 -
        meanField ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold
          (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
          (angularNativeStages ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold j)
          (ActualMeanStageData.radialSection p) =
      (SpatialLocalization.spatialCutoff
          (ActualMeanStageData.radialSection p).2 - 1) *
        meanField ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold
          (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
          (angularNativeStages ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold j)
          (ActualMeanStageData.radialSection p) := by
  rw [cut_direct_component_one_radial j p hp]
  ring

theorem cut_direct_component_one_radial_ne_native_of_cutoff_ne_one
    (j : ℕ) (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1)
    (hcut : SpatialLocalization.spatialCutoff
      (ActualMeanStageData.radialSection p).2 ≠ 1)
    (hnative : meanField ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
      (angularNativeStages ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold j)
      (ActualMeanStageData.radialSection p) ≠ 0) :
    (SpatialLocalization.cutPotential (selectedDirectStages j)
      (ActualMeanStageData.radialSection p)) 1 ≠
      meanField ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
        (angularNativeStages ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold j)
        (ActualMeanStageData.radialSection p) := by
  intro hEq
  have hGap := cut_direct_component_one_radial_minus_native j p hp
  rw [hEq, sub_self, zero_mul] at hGap
  exact hnative (by simpa using hGap)

end NavierStokesReview.SelectedDirectCutoffMomentBoundary
