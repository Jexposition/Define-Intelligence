import NavierStokes.R3.ActualCandidate
import NavierStokes.R3.PositiveTimeForce

/-!
# Positive-time force activity audit

This probe tests the actual cutoff used by the R³ assembly.  It does not try
to prove a norm divergence from an unproved `sorry` proposition.
-/

open Set
open Filter
open scoped Topology ContDiff

namespace NavierStokesR3.ForceActivityProbe

open NavierStokesR3 ProblemStatement PositiveTimeForce

#check PositiveTimeForce.timeCutoff
#check PositiveTimeForce.timeCutoff_contDiff
#check PositiveTimeForce.timeCutoff_eq_one
#check PositiveTimeForce.timeCutoff_eq_zero
#check PositiveTimeForce.force_contDiff
#check PositiveTimeForce.force_eq
#check NavierStokesR3.ActualCandidate.of_localized_fields

theorem cutoff_is_active_at_singular_time :
    PositiveTimeForce.timeCutoff 1 = 1 := by
  apply PositiveTimeForce.timeCutoff_eq_one
  norm_num

theorem force_is_active_at_singular_time {f : VelocityField} (x : Space) :
    PositiveTimeForce.force f (1, x) = f (1, x) := by
  apply PositiveTimeForce.force_eq
  constructor <;> norm_num

theorem smooth_force_has_finite_pointwise_limit {f : VelocityField}
    (hf : ContDiff ℝ ∞ f) (x : Space) :
    Tendsto (fun t : ℝ => PositiveTimeForce.force f (t, x)) (𝓝 1)
      (𝓝 (PositiveTimeForce.force f (1, x))) := by
  have hcont : Continuous (PositiveTimeForce.force f) :=
    (PositiveTimeForce.force_contDiff hf).continuous
  have hcurve : Continuous (fun t : ℝ => PositiveTimeForce.force f (t, x)) :=
    hcont.comp (continuous_id.prodMk continuous_const)
  exact hcurve.continuousAt

end NavierStokesR3.ForceActivityProbe
