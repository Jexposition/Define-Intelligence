import NavierStokes.ResidualCalculus
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.ContDiff.Operations

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
open scoped ContDiff

theorem affine_time_perturbation_smooth
    (a : Space) (t₀ : ℝ) :
    ContDiff ℝ ∞ (fun z : SpaceTime => (z.1 - t₀) • a) := by
  exact (contDiff_fst.sub contDiff_const).smul_const a

theorem affine_time_perturbation_divergence_free
    (a : Space) (t₀ : ℝ) (t : ℝ) (x : Space) :
    spatialDivergence (fun z : SpaceTime => (z.1 - t₀) • a) t x = 0 := by
  simp [spatialDivergence, spatialDerivative]

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

theorem affine_time_perturbation_defect_eq
    (a : Space) (t₀ : ℝ) (x : Space) :
    temporalDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x -
        spatialLaplacian (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x +
        spatialDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x
          ((t₀ - t₀) • a) +
        spatialDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x
          ((t₀ - t₀) • a) +
        spatialDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x
          ((t₀ - t₀) • a) = a := by
  have hderiv :
      deriv (fun s : ℝ => (s - t₀) • a) t₀ = a := by
    rw [← fderiv_apply_one_eq_deriv]
    have hf :
        fderiv ℝ (fun s : ℝ => (s - t₀) • a) t₀ =
          (fderiv ℝ (fun s : ℝ => s - t₀) t₀).smulRight a := by
      simpa only [id_eq] using
        (fderiv_smul_const (c := fun s : ℝ => s - t₀)
          (differentiableAt_id.sub_const t₀) a)
    rw [hf]
    have hs : deriv (fun s : ℝ => s - t₀) t₀ = 1 := by
      change deriv (fun s : ℝ => id s + (-t₀)) t₀ = 1
      rw [deriv_add_const]
      exact deriv_id t₀
    simp [ContinuousLinearMap.smulRight_apply, hs]
  have hspatial :
      spatialDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x = 0 := by
    simp [spatialDerivative]
  have hspatial_all :
      ∀ y : Space, spatialDerivative
        (fun z : SpaceTime => (z.1 - t₀) • a) t₀ y = 0 := by
    intro y
    simp [spatialDerivative]
  rw [temporalDerivative, fderiv_apply_one_eq_deriv, hderiv]
  simp [spatialLaplacian, hspatial, hspatial_all]

theorem affine_time_perturbation_breaks_fixed_force
    (u : VelocityField) (p : PressureField) (f : VelocityField)
    (a : Space) (t₀ : ℝ) (x : Space)
    (hut : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t₀)
    (hu : ContDiff ℝ 2 (fun y : Space => u (t₀, y)))
    (hp : DifferentiableAt ℝ (fun y : Space => p (t₀, y)) x)
    (ha : a ≠ 0)
    (hbase : navierStokesResidual u p t₀ x = f (t₀, x)) :
    navierStokesResidual
        (fun z => u z + (z.1 - t₀) • a) p t₀ x ≠ f (t₀, x) := by
  intro hpert
  have htemp :
      temporalDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x = a := by
    rw [temporalDerivative, fderiv_apply_one_eq_deriv]
    change deriv (fun s : ℝ => (s - t₀) • a) t₀ = a
    rw [← fderiv_apply_one_eq_deriv]
    have hf :
        fderiv ℝ (fun s : ℝ => (s - t₀) • a) t₀ =
          (fderiv ℝ (fun s : ℝ => s - t₀) t₀).smulRight a := by
      simpa only [id_eq] using
        (fderiv_smul_const (c := fun s : ℝ => s - t₀)
          (differentiableAt_id.sub_const t₀) a)
    rw [hf]
    have hs : deriv (fun s : ℝ => s - t₀) t₀ = 1 := by
      change deriv (fun s : ℝ => id s + (-t₀)) t₀ = 1
      rw [deriv_add_const]
      exact deriv_id t₀
    simp [ContinuousLinearMap.smulRight_apply, hs]
  have hspatial :
      spatialDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x = 0 := by
    simp [spatialDerivative]
  have hlap :
      spatialLaplacian (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x = 0 := by
    simp [spatialLaplacian, spatialDerivative]
  have hdefect :
      temporalDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x -
          spatialLaplacian (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x +
          spatialDerivative u t₀ x ((t₀ - t₀) • a) +
          spatialDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x
            (u (t₀, x)) +
          spatialDerivative (fun z : SpaceTime => (z.1 - t₀) • a) t₀ x
            ((t₀ - t₀) • a) ≠ 0 := by
    rw [htemp, hlap, hspatial]
    simp
    exact ha
  exact hdefect (fixed_force_perturbation_defect_zero u
    (fun z : SpaceTime => (z.1 - t₀) • a) p f t₀ x hut
    (by
      exact (differentiableAt_id.sub_const t₀).smul_const a)
    hu (by
      simpa using (contDiff_const : ContDiff ℝ 2 (fun _ : Space => (0 : Space)))) hp
    hbase hpert)

end NavierStokesReview.IndependentDataPerturbationProbe
