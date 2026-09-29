import completions.SelectedDirectStageMomentTransport
import completions.SelectedRadialSectionComponent

/-!
# Selected direct radial moment bridge

This module composes two source-backed facts for the selected direct branch:
the first Cartesian component on the positive radial section is the native
angular scalar, and that scalar has zero order-two radial moment.  The result
is deliberately scoped to the direct branch.  It does not identify the curl
generated potential branch, or the mixed endpoint velocity, with this scalar.
-/

noncomputable section

namespace NavierStokesReview.SelectedDirectRadialMomentBridge

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokesReview.SelectedDirectStageMomentTransport
open NavierStokesReview.SelectedRadialSectionComponent

private noncomputable def selectedDirectScalar (j : ℕ) : ActualMeanPhysicalData.Scalar :=
  angularNativeStages ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold j

theorem selected_direct_component_one_eq_native_scalar
    (j : ℕ) (p : DirectAngularDiagonal.CylPoint) (hp : 0 < p.2.1) :
    (selectedDirectStages j (ActualMeanStageData.radialSection p)) 1 =
      meanField ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        (CoordinateAlgebra.A CorrectionInitialization.ActualPrimary.h)
        (selectedDirectScalar j) (ActualMeanStageData.radialSection p) := by
  exact selected_direct_stage_radial_component_one j p hp

theorem selected_direct_native_scalar_barMoment_zero
    (j n : ℕ) {s : PressureStream.Plane}
    (hs : s ∈ ActualInitialization.geometry.region.carrier) :
    DefectIncrementBounds.barMoment 2 (selectedDirectScalar j) n s = 0 := by
  exact selected_angular_native_stage_moment_zero j n hs

theorem selected_direct_native_scalar_radial_integral_zero
    (j n : ℕ) {s : PressureStream.Plane}
    (hs : s ∈ ActualInitialization.geometry.region.carrier) :
    (∫ r, r ^ 2 * PressureStream.torusAverage
      ((selectedDirectScalar j) n) (r, s)) = 0 := by
  rw [← DefectIncrementBounds.barMoment_apply]
  exact selected_direct_native_scalar_barMoment_zero j n hs

end NavierStokesReview.SelectedDirectRadialMomentBridge
