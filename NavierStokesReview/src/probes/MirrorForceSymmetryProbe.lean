import NavierStokes.R3.ProblemStatement
import Mathlib.Analysis.Calculus.ContDiff.Operations

/-!
The negated force is a legitimate smooth field, but it is a different forcing
problem.  This probe records the exact logical boundary of the mirror-force
proposal without claiming that it disproves an existential candidate.
-/

noncomputable section

namespace NavierStokesReview.MirrorForceSymmetryProbe

open NavierStokesR3.ProblemStatement
open scoped ContDiff

def mirrorForce (f : VelocityField) : VelocityField := fun z => -f z

theorem mirrorForce_smooth {f : VelocityField}
    (hf : ContDiff ℝ ∞ f) : ContDiff ℝ ∞ (mirrorForce f) := by
  change ContDiff ℝ ∞ (fun z => -f z)
  exact hf.neg

theorem same_fields_for_mirror_force_require_self_negation
    {ν : ℝ} {u : VelocityField} {p : PressureField} {f : VelocityField}
    {t : ℝ} {x : Space}
    (h : navierStokesResidual ν u p t x = f (t, x))
    (hm : navierStokesResidual ν u p t x = mirrorForce f (t, x)) :
    f (t, x) = -f (t, x) := by
  exact h.symm.trans (by simpa [mirrorForce] using hm)

theorem nonzero_force_cannot_use_same_fields_for_mirror
    {ν : ℝ} {u : VelocityField} {p : PressureField} {f : VelocityField}
    {t : ℝ} {x : Space}
    (h : navierStokesResidual ν u p t x = f (t, x))
    (hn : f (t, x) ≠ -f (t, x)) :
    navierStokesResidual ν u p t x ≠ mirrorForce f (t, x) := by
  intro hm
  exact hn (same_fields_for_mirror_force_require_self_negation h hm)

end NavierStokesReview.MirrorForceSymmetryProbe
