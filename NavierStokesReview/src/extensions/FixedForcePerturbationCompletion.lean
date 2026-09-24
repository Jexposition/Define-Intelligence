import NavierStokes.R3.PositiveTimeForce
import NavierStokes.ResidualCalculus

/-!
This extension isolates the exact consequence of treating a residual-designed
force as fixed data.  It does not assert that an arbitrary perturbation is an
admissible selected-path perturbation; it proves the operator-level condition
that such a perturbation would have to satisfy.
-/

noncomputable section

namespace NavierStokesReview.FixedForcePerturbationCompletion

open NavierStokes.ProblemStatement
open NavierStokes.ResidualCalculus

def FixedForceData (u : VelocityField) (p : PressureField) (f : VelocityField) : Prop :=
  ∀ t x, navierStokesResidual u p t x = f (t, x)

theorem fixed_force_perturbation_defect_zero
    (u e : VelocityField) (p : PressureField) (f : VelocityField) (t : ℝ) (x : Space)
    (hut : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t)
    (het : DifferentiableAt ℝ (fun s : ℝ => e (s, x)) t)
    (hu : ContDiff ℝ 2 (fun y : Space => u (t, y)))
    (he : ContDiff ℝ 2 (fun y : Space => e (t, y)))
    (hp : DifferentiableAt ℝ (fun y : Space => p (t, y)) x)
    (hbase : navierStokesResidual u p t x = f (t, x))
    (hpert : navierStokesResidual (fun z => u z + e z) p t x = f (t, x)) :
    temporalDerivative e t x - spatialLaplacian e t x +
        spatialDerivative u t x (e (t, x)) +
        spatialDerivative e t x (u (t, x)) +
        spatialDerivative e t x (e (t, x)) = 0 := by
  have hzero_pressure : DifferentiableAt ℝ (fun _ : Space => (0 : ℝ)) x :=
    differentiableAt_const (c := (0 : ℝ))
  have hidentity := navierStokesResidual_add_sub
    u e p (fun _ => 0) t x hut het hu he hp hzero_pressure
  have hresidual_zero :
      navierStokesResidual (fun z => u z + e z) p t x -
          navierStokesResidual u p t x = 0 := by
    rw [hpert, hbase]
    simp
  calc
    temporalDerivative e t x - spatialLaplacian e t x +
          spatialDerivative u t x (e (t, x)) +
          spatialDerivative e t x (u (t, x)) +
          spatialDerivative e t x (e (t, x)) =
        navierStokesResidual (fun z => u z + e z) p t x -
          navierStokesResidual u p t x := by
            simpa [pressureGradient] using hidentity.symm
    _ = 0 := hresidual_zero

theorem fixed_force_data_perturbation_obstruction
    (u e : VelocityField) (p : PressureField) (f : VelocityField)
    (hbase : FixedForceData u p f)
    (t : ℝ) (x : Space)
    (hut : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t)
    (het : DifferentiableAt ℝ (fun s : ℝ => e (s, x)) t)
    (hu : ContDiff ℝ 2 (fun y : Space => u (t, y)))
    (he : ContDiff ℝ 2 (fun y : Space => e (t, y)))
    (hp : DifferentiableAt ℝ (fun y : Space => p (t, y)) x)
    (hdefect :
      temporalDerivative e t x - spatialLaplacian e t x +
        spatialDerivative u t x (e (t, x)) +
        spatialDerivative e t x (u (t, x)) +
        spatialDerivative e t x (e (t, x)) ≠ 0) :
    ¬ FixedForceData (fun z => u z + e z) p f := by
  intro hpert
  exact hdefect (fixed_force_perturbation_defect_zero u e p f t x hut het hu he hp
    (hbase t x) (hpert t x))

theorem positive_time_force_perturbation_obstruction
    (u e g : VelocityField) (p : PressureField)
    (hbase : ∀ t x, navierStokesResidual u p t x =
      NavierStokesR3.PositiveTimeForce.force g (t, x))
    (t : ℝ) (x : Space)
    (hut : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t)
    (het : DifferentiableAt ℝ (fun s : ℝ => e (s, x)) t)
    (hu : ContDiff ℝ 2 (fun y : Space => u (t, y)))
    (he : ContDiff ℝ 2 (fun y : Space => e (t, y)))
    (hp : DifferentiableAt ℝ (fun y : Space => p (t, y)) x)
    (hdefect :
      temporalDerivative e t x - spatialLaplacian e t x +
        spatialDerivative u t x (e (t, x)) +
        spatialDerivative e t x (u (t, x)) +
        spatialDerivative e t x (e (t, x)) ≠ 0) :
    navierStokesResidual (fun z => u z + e z) p t x ≠
      NavierStokesR3.PositiveTimeForce.force g (t, x) := by
  intro hpert
  exact hdefect (fixed_force_perturbation_defect_zero u e p
    (NavierStokesR3.PositiveTimeForce.force g) t x hut het hu he hp
    (hbase t x) hpert)

end NavierStokesReview.FixedForcePerturbationCompletion
