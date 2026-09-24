import NavierStokes.ResidualCalculus

/-!
This probe formalises the part of the independent-data objection that is
actually forced by the PDE operator.  If the same pressure and the same fixed
force are retained after perturbing the velocity by `e`, then the complete
linearised-plus-quadratic perturbation defect must vanish.  The force cannot
adapt independently of that defect.

The probe does not claim that the selected construction admits an arbitrary
perturbation.  Establishing that would require a separate perturbation theorem
for the selected schedule.
-/

noncomputable section

namespace NavierStokesReview.IndependentDataPerturbationProbe

open NavierStokes.ProblemStatement
open NavierStokes.ResidualCalculus

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

theorem fixed_force_perturbation_is_impossible_when_defect_nonzero
    (u e : VelocityField) (p : PressureField) (f : VelocityField) (t : ℝ) (x : Space)
    (hut : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t)
    (het : DifferentiableAt ℝ (fun s : ℝ => e (s, x)) t)
    (hu : ContDiff ℝ 2 (fun y : Space => u (t, y)))
    (he : ContDiff ℝ 2 (fun y : Space => e (t, y)))
    (hp : DifferentiableAt ℝ (fun y : Space => p (t, y)) x)
    (hbase : navierStokesResidual u p t x = f (t, x))
    (hdefect :
      temporalDerivative e t x - spatialLaplacian e t x +
        spatialDerivative u t x (e (t, x)) +
        spatialDerivative e t x (u (t, x)) +
        spatialDerivative e t x (e (t, x)) ≠ 0) :
    navierStokesResidual (fun z => u z + e z) p t x ≠ f (t, x) := by
  intro hpert
  exact hdefect (fixed_force_perturbation_defect_zero u e p f t x hut het hu he hp
    hbase hpert)

end NavierStokesReview.IndependentDataPerturbationProbe
