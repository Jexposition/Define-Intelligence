import NavierStokes.SpatialCurl

/-!
# Cutoff--curl commutator

This review-side theorem expands the spatial curl of a scalar-localised
potential.  It records the exact product-rule term that must be controlled
before a radial moment statement can be transported from an uncut profile to
the selected Cartesian field.
-/

noncomputable section

namespace NavierStokesReview.SelectedCutoffCurlCommutator

open NavierStokes ProblemStatement

theorem curl_smul_eq_smul_curl_add_commutator
    {χ : Space → ℝ} {A : Space → Space} {x : Space}
    (hχ : DifferentiableAt ℝ χ x) (hA : DifferentiableAt ℝ A x) :
    SpatialCurl.curl (fun y => χ y • A y) x =
      χ x • SpatialCurl.curl A x +
        SpatialCurl.curlLinear ((fderiv ℝ χ x).smulRight (A x)) := by
  unfold SpatialCurl.curl
  rw [fderiv_fun_smul hχ hA]
  rw [map_add, map_smul]

end NavierStokesReview.SelectedCutoffCurlCommutator
