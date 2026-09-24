import NavierStokes.JointResidualLimits
import NavierStokes.ProblemStatement

open Set
open Filter
open scoped ContDiff

namespace NavierStokesReview.ResidualFlatnessCompatibilityProbe

open NavierStokes.ProblemStatement
open NavierStokes.JointResidualLimits

/-! This file is intentionally a semantic probe.  It does not claim that the
selected witness is false.  It tests whether the residual-flatness predicate
alone can contradict an independent velocity blow-up predicate. -/

theorem zero_residual_has_vanishing_joint_jets :
    NavierStokes.JointResidualLimits.VanishingJointJets
      (fun _ : NavierStokes.ProblemStatement.SpaceTime =>
        (0 : NavierStokes.ProblemStatement.Space)) := by
  intro n
  have hz : iteratedFDeriv ℝ n
      (fun _ : NavierStokes.ProblemStatement.SpaceTime =>
        (0 : NavierStokes.ProblemStatement.Space)) =
      (fun _ => 0) := by
    funext z
    simp
  rw [hz]
  exact tendsto_const_nhds

theorem residual_flatness_does_not_by_itself_exclude_blowup
    (u : NavierStokes.ProblemStatement.VelocityField)
    (hu : NavierStokes.ProblemStatement.SpeedUnboundedAtOne u) :
    ∃ f : NavierStokes.ProblemStatement.SpaceTime →
        NavierStokes.ProblemStatement.Space,
      NavierStokes.JointResidualLimits.VanishingJointJets f ∧
        NavierStokes.ProblemStatement.SpeedUnboundedAtOne u := by
  exact ⟨fun _ => 0, zero_residual_has_vanishing_joint_jets, hu⟩

end NavierStokesReview.ResidualFlatnessCompatibilityProbe
