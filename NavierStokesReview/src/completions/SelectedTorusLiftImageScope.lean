import NavierStokes.PhysicalResidualBridge
import NavierStokes.PhysicalMeanJetBounds

/-!
# Auxiliary image scope of the selected physical graph

`PressureStream.torusAverage` integrates over the full auxiliary `Plane`, while
the selected physical graph is represented by `PhysicalResidualBridge.absoluteLift`.
This file proves an exact image-side fact: a continuous linear coordinate is
nonnegative on every auxiliary point produced by `absoluteLift`, but is negative
at an auxiliary point in the unit integration square.  The result identifies a
transport obligation; it does not assert a nonzero selected moment or a kernel
contradiction.
-/

noncomputable section

namespace NavierStokesReview.SelectedTorusLiftImageScope

open NavierStokes
open NavierStokes.PhysicalGraphBounds
open NavierStokes.PhysicalResidualBridge
open NavierStokes.PhysicalMeanJetBounds

abbrev GraphPlane := NavierStokes.PhysicalGraphBounds.Plane
abbrev GraphSpaceTime := NavierStokes.ProblemStatement.SpaceTime

noncomputable def radialCoordinate : GraphPlane →L[ℝ] ℝ :=
  (1 + (Real.sqrt 2 - 1) ^ 2)⁻¹ •
    (ContinuousLinearMap.fst ℝ ℝ ℝ -
      (Real.sqrt 2 - 1) • ContinuousLinearMap.snd ℝ ℝ ℝ)

theorem radialCoordinate_radial :
    radialCoordinate radialDirection = 1 := by
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) :=
    Real.sq_sqrt (by norm_num)
  change (1 + (Real.sqrt 2 - 1) ^ 2)⁻¹ *
    (1 - (Real.sqrt 2 - 1) * (1 - Real.sqrt 2)) = 1
  field_simp
  nlinarith

theorem radialCoordinate_time :
    radialCoordinate timeDirection = 0 := by
  change (1 + (Real.sqrt 2 - 1) ^ 2)⁻¹ *
    ((Real.sqrt 2 - 1) - (Real.sqrt 2 - 1) * 1) = 0
  ring

theorem absoluteLift_auxiliary_radialCoordinate_nonnegative
    (h : ℝ) (p : GraphSpaceTime) (hr : 0 ≤ p.2 0) :
    0 ≤ radialCoordinate (absoluteLift h p).2.2 := by
  unfold absoluteLift
  rw [map_add, map_smul, map_smul, radialCoordinate_radial,
    radialCoordinate_time]
  simp only [smul_eq_mul, mul_one, mul_zero, add_zero]
  exact Real.rpow_nonneg hr _

noncomputable def unreachableAuxiliary : GraphPlane := (0, (1 / 2 : ℝ))

theorem unreachableAuxiliary_in_unit_square :
    unreachableAuxiliary.1 ∈ Set.Icc (0 : ℝ) 1 ∧
      unreachableAuxiliary.2 ∈ Set.Icc (0 : ℝ) 1 := by
  constructor <;> norm_num [unreachableAuxiliary]

theorem radialCoordinate_unreachableAuxiliary_negative :
    radialCoordinate unreachableAuxiliary < 0 := by
  have hs : 1 < Real.sqrt (2 : ℝ) := by
    have hs0 : 0 ≤ Real.sqrt (2 : ℝ) := Real.sqrt_nonneg _
    have hs2 : (Real.sqrt (2 : ℝ)) ^ 2 = (2 : ℝ) :=
      Real.sq_sqrt (by norm_num)
    nlinarith
  change (1 + (Real.sqrt 2 - 1) ^ 2)⁻¹ *
    (0 - (Real.sqrt 2 - 1) * (1 / 2 : ℝ)) < 0
  have hden : 0 < 1 + (Real.sqrt (2 : ℝ) - 1) ^ 2 := by positivity
  have hnum : 0 - (Real.sqrt 2 - 1) * (1 / 2 : ℝ) < 0 := by
    nlinarith [hs]
  exact mul_neg_of_pos_of_neg (inv_pos.mpr hden) hnum

theorem unreachableAuxiliary_not_in_absoluteLift_image
    (h : ℝ) (p : GraphSpaceTime) (hr : 0 ≤ p.2 0) :
    (absoluteLift h p).2.2 ≠ unreachableAuxiliary := by
  intro heq
  have hcoord := congrArg radialCoordinate heq
  have hnonneg := absoluteLift_auxiliary_radialCoordinate_nonnegative h p
    hr
  rw [hcoord] at hnonneg
  exact (not_lt_of_ge hnonneg) radialCoordinate_unreachableAuxiliary_negative

theorem physicalPoint_auxiliary_radialCoordinate_nonnegative
    (h : ℝ) (w : GraphSpaceTime) :
    0 ≤ radialCoordinate (physicalPoint h w).2.2 := by
  unfold physicalPoint radialProfile
  rw [map_add, map_smul, map_smul, radialCoordinate_radial,
    radialCoordinate_time]
  simp only [smul_eq_mul, mul_one, mul_zero, add_zero]
  exact Real.rpow_nonneg (by positivity) _

noncomputable def unreachablePhysicalPoint :
    NavierStokes.PhysicalMeanJetBounds.Point :=
  (0, ((0, 0), unreachableAuxiliary))

theorem unreachablePhysicalPoint_not_in_physicalPoint_image
    (h : ℝ) (w : GraphSpaceTime) :
    physicalPoint h w ≠ unreachablePhysicalPoint := by
  intro heq
  have hcoord := congrArg (fun z => radialCoordinate z.2.2) heq
  have hnonneg := physicalPoint_auxiliary_radialCoordinate_nonnegative h w
  rw [hcoord] at hnonneg
  exact (not_lt_of_ge hnonneg) radialCoordinate_unreachableAuxiliary_negative

end NavierStokesReview.SelectedTorusLiftImageScope
