import NavierStokes.ActualCandidateAssembly
import completions.SelectedCutoffCurlCommutator

/-!
# Selected cut-stage curl scope

The production potential sum applies `SolenoidalDiagonal.cutStage` before the
local `tsum` is formed.  This completion expands the curl of one selected cut
stage.  The second term is the cutoff--curl commutator; its value is not
assumed to vanish.
-/

noncomputable section

namespace NavierStokesReview.SelectedCutStageCurlScope

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open ProblemStatement

theorem selected_cut_stage_curl_expansion
    (a : ℕ → ℕ) (q : SpaceTime → ℝ) (j : ℕ) {z : SpaceTime}
    (hχ : DifferentiableAt ℝ (fun y : Space =>
      SmoothCutoffs.scaledCutoff (a j) (q (z.1, y))) z.2)
    (hA : DifferentiableAt ℝ
      (fun y : Space => selectedPotentialStages j (z.1, y)) z.2) :
    SpatialCurl.spatialCurl
        (SolenoidalDiagonal.cutStage (fun k => (a k : ℝ)) q
          selectedPotentialStages j) z =
      SmoothCutoffs.scaledCutoff (a j) (q z) •
          SpatialCurl.spatialCurl (selectedPotentialStages j) z +
        SpatialCurl.curlLinear
          ((fderiv ℝ (fun y : Space =>
            SmoothCutoffs.scaledCutoff (a j) (q (z.1, y))) z.2).smulRight
            (selectedPotentialStages j z)) := by
    simpa [SolenoidalDiagonal.cutStage, SpatialCurl.spatialCurl] using
      (SelectedCutoffCurlCommutator.curl_smul_eq_smul_curl_add_commutator
        hχ hA)

theorem selected_cut_stage_curl_component_zero
    (a : ℕ → ℕ) (q : SpaceTime → ℝ) (j : ℕ) {z : SpaceTime}
    (hχ : DifferentiableAt ℝ (fun y : Space =>
      SmoothCutoffs.scaledCutoff (a j) (q (z.1, y))) z.2)
    (hA : DifferentiableAt ℝ
      (fun y : Space => selectedPotentialStages j (z.1, y)) z.2) :
    (SpatialCurl.spatialCurl
        (SolenoidalDiagonal.cutStage (fun k => (a k : ℝ)) q
          selectedPotentialStages j) z) 0 =
      SmoothCutoffs.scaledCutoff (a j) (q z) •
          (SpatialCurl.spatialCurl (selectedPotentialStages j) z) 0 +
        ((fderiv ℝ (fun y : Space =>
          SmoothCutoffs.scaledCutoff (a j) (q (z.1, y))) z.2
            (coordinateVector 1)) * (selectedPotentialStages j z) 2 -
          (fderiv ℝ (fun y : Space =>
            SmoothCutoffs.scaledCutoff (a j) (q (z.1, y))) z.2
              (coordinateVector 2)) * (selectedPotentialStages j z) 1) := by
  have h := selected_cut_stage_curl_expansion a q j hχ hA
  have h0 := congrArg (fun v : Space => v 0) h
  simpa [SpatialCurl.curlLinear_apply_zero, ContinuousLinearMap.smulRight_apply,
    smul_eq_mul] using h0

end NavierStokesReview.SelectedCutStageCurlScope
