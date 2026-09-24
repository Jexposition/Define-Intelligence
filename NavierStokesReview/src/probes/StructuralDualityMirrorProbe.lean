import NavierStokes.R3.ProblemStatement
import Mathlib.Analysis.Calculus.ContDiff.Operations

/-!
This probe records the exact mirror identities and their logical boundary.
Negating a smooth force preserves admissibility as a field, and `f + (-f)` is
zero pointwise.  Neither fact supplies a solution for the negated forcing
problem or reverses the nonlinear evolution of the original witness.
-/

noncomputable section

namespace NavierStokesReview.StructuralDualityMirrorProbe

open NavierStokesR3.ProblemStatement
open scoped ContDiff InnerProductSpace

def mirrorForce (f : VelocityField) : VelocityField := fun z => -f z

theorem mirrorForce_smooth {f : VelocityField}
    (hf : ContDiff ℝ ∞ f) : ContDiff ℝ ∞ (mirrorForce f) := by
  change ContDiff ℝ ∞ (fun z => -f z)
  exact hf.neg

theorem mirrorForce_work_neg (f u : VelocityField) (z : SpaceTime) :
    ⟪mirrorForce f z, u z⟫_ℝ = - ⟪f z, u z⟫_ℝ := by
  simp [mirrorForce]

theorem force_plus_mirror_zero (f : VelocityField) (z : SpaceTime) :
    f z + mirrorForce f z = 0 := by
  simp [mirrorForce]

theorem same_fields_for_both_forces_force_zero
    {ν : ℝ} {u : VelocityField} {p : PressureField} {f : VelocityField}
    {t : ℝ} {x : Space}
    (hplus : navierStokesResidual ν u p t x = f (t, x))
    (hminus : navierStokesResidual ν u p t x = mirrorForce f (t, x)) :
    f (t, x) = 0 := by
  have hself : f (t, x) = -f (t, x) := hplus.symm.trans (by
    simpa [mirrorForce] using hminus)
  have hadd : f (t, x) + f (t, x) = 0 := eq_neg_iff_add_eq_zero.mp hself
  have htwo : (2 : ℝ) • f (t, x) = 0 := by
    simpa [two_smul] using hadd
  exact (smul_eq_zero.mp htwo).resolve_left (by norm_num)

theorem mirror_is_different_forcing_problem
    {ν : ℝ} {u : VelocityField} {p : PressureField} {f : VelocityField}
    {t : ℝ} {x : Space}
    (hplus : navierStokesResidual ν u p t x = f (t, x))
    (hnonzero : f (t, x) ≠ 0) :
    navierStokesResidual ν u p t x ≠ mirrorForce f (t, x) := by
  intro hminus
  exact hnonzero (same_fields_for_both_forces_force_zero hplus hminus)

end NavierStokesReview.StructuralDualityMirrorProbe
