import NavierStokes.ResidualCalculus

/-!
This probe records the exact consequence of the residual definition relevant to
the proposed pressure "equal-and-opposite" obstruction.  It is deliberately a
local operator identity: it does not assume a pressure Poisson equation that is
absent from the selected candidate interface.
-/

noncomputable section

namespace NavierStokesReview.PressureResidualNonCancellationProbe

open NavierStokes.ProblemStatement
open NavierStokes.ResidualCalculus

theorem pressure_perturbation_enters_force
    (u e : VelocityField) (p q : PressureField) (t : ℝ) (x : Space)
    (hut : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t)
    (het : DifferentiableAt ℝ (fun s : ℝ => e (s, x)) t)
    (hu : ContDiff ℝ 2 (fun y : Space => u (t, y)))
    (he : ContDiff ℝ 2 (fun y : Space => e (t, y)))
    (hp : DifferentiableAt ℝ (fun y : Space => p (t, y)) x)
    (hq : DifferentiableAt ℝ (fun y : Space => q (t, y)) x) :
    navierStokesResidual (fun z => u z + e z) (fun z => p z + q z) t x -
        navierStokesResidual u p t x =
      temporalDerivative e t x - spatialLaplacian e t x + pressureGradient q t x +
        spatialDerivative u t x (e (t, x)) + spatialDerivative e t x (u (t, x)) +
        spatialDerivative e t x (e (t, x)) := by
  exact navierStokesResidual_add_sub u e p q t x hut het hu he hp hq

theorem zero_velocity_pressure_perturbation
    (q : PressureField) (t : ℝ) (x : Space)
    (_hq : DifferentiableAt ℝ (fun y : Space => q (t, y)) x) :
    navierStokesResidual (fun _ => 0) q t x -
        navierStokesResidual (fun _ => 0) (fun _ => 0) t x =
      pressureGradient q t x := by
  have hzero_time : DifferentiableAt ℝ (fun _ : ℝ => (0 : Space)) t :=
    differentiableAt_const (c := (0 : Space))
  have hzero_space : ContDiff ℝ 2 (fun _ : Space => (0 : Space)) :=
    contDiff_const
  have hzero_pressure : DifferentiableAt ℝ (fun _ : Space => (0 : ℝ)) x :=
    differentiableAt_const (c := (0 : ℝ))
  simpa [temporalDerivative, spatialLaplacian, spatialDerivative, advection,
    navierStokesResidual, pressureGradient] using
    (navierStokesResidual_add_sub
      (fun _ => 0) (fun _ => 0) (fun _ => 0) q t x
      hzero_time hzero_time hzero_space hzero_space hzero_pressure _hq)

theorem nonzero_pressure_gradient_changes_residual
    (q : PressureField) (t : ℝ) (x : Space)
    (hq : DifferentiableAt ℝ (fun y : Space => q (t, y)) x)
    (hgrad : pressureGradient q t x ≠ 0) :
    navierStokesResidual (fun _ => 0) q t x ≠
      navierStokesResidual (fun _ => 0) (fun _ => 0) t x := by
  intro hEq
  have hdiff := zero_velocity_pressure_perturbation q t x hq
  have hgradzero : pressureGradient q t x = 0 := by
    calc
      pressureGradient q t x =
          navierStokesResidual (fun _ => 0) q t x -
            navierStokesResidual (fun _ => 0) (fun _ => 0) t x := hdiff.symm
      _ = 0 := by rw [hEq]; simp
  exact hgrad hgradzero

end NavierStokesReview.PressureResidualNonCancellationProbe
