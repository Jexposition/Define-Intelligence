import NavierStokes.SpatialCurl
import NavierStokes.SmoothCutoffs
import NavierStokes.ResidualCalculus
import NavierStokes.ActualCandidateAssembly
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension

open Set
open NavierStokes ProblemStatement
open NavierStokes.CorrectionInitialization.ActualPrimary
open scoped Topology ContDiff

noncomputable section

def bump : ContDiffBump (0 : Space) where
  rIn := 1 / 2
  rOut := 1
  rIn_pos := by norm_num
  rIn_lt_rOut := by norm_num

def scalarPotential : Space → ℝ := fun x => x 1 * bump x

def compactPotential : Space → Space :=
  fun x => scalarPotential x • coordinateVector 2

theorem scalarPotential_contDiff : ContDiff ℝ ∞ scalarPotential := by
  have hcoord : ContDiff ℝ ∞ (fun x : Space => x 1) := by
    let proj : Space →L[ℝ] ℝ := EuclideanSpace.proj 1
    simpa [proj] using proj.contDiff
  exact hcoord.mul bump.contDiff

theorem compactPotential_contDiff : ContDiff ℝ ∞ compactPotential := by
  exact scalarPotential_contDiff.smul_const (coordinateVector 2)

theorem scalarPotential_hasCompactSupport : HasCompactSupport scalarPotential := by
  exact bump.hasCompactSupport.mul_left

theorem compactPotential_hasCompactSupport : HasCompactSupport compactPotential := by
  change HasCompactSupport (scalarPotential • (fun _ : Space => coordinateVector 2))
  exact scalarPotential_hasCompactSupport.smul_right

theorem bump_one_near_zero : bump =ᶠ[𝓝 (0 : Space)] (fun _ => 1) := by
  apply bump.eventuallyEq_one_of_mem_ball
  simp [bump]

theorem scalarPotential_eq_coordinate_near_zero :
    scalarPotential =ᶠ[𝓝 (0 : Space)] (fun x => x 1) := by
  filter_upwards [bump_one_near_zero] with x hx
  simp [scalarPotential, hx]

theorem compactPotential_eq_linear_near_zero :
      compactPotential =ᶠ[𝓝 (0 : Space)]
      (fun x => (x 1) • coordinateVector 2) := by
  filter_upwards [scalarPotential_eq_coordinate_near_zero] with x hx
  simp [compactPotential, hx]

theorem compactPotential_curl_at_zero :
    SpatialCurl.curl compactPotential 0 = coordinateVector 0 := by
  rw [SpatialCurl.curl_eq_of_eventuallyEq compactPotential_eq_linear_near_zero]
  unfold SpatialCurl.curl SpatialCurl.curlLinear SpatialCurl.derivativeEntry
  let proj : Space →L[ℝ] ℝ := EuclideanSpace.proj 1
  have hcoord : DifferentiableAt ℝ (fun y : Space => y 1) 0 := by
    simpa [proj] using proj.differentiableAt
  have hderiv : fderiv ℝ (fun y : Space => y 1) 0 = proj := by
    simpa [proj] using proj.hasFDerivAt.fderiv
  have hlin :
      fderiv ℝ (fun x : Space => (x 1) • coordinateVector 2) 0 =
        proj.smulRight (coordinateVector 2) := by
    simpa [hderiv] using fderiv_smul_const hcoord (coordinateVector 2)
  rw [hlin]
  simp [coordinateVector, proj]

def compactPotentialField : VelocityField := fun z => compactPotential z.2

def compactCurlField : VelocityField := SpatialCurl.spatialCurl compactPotentialField

def compactPerturbation (t₀ : ℝ) : VelocityField :=
  fun z => (z.1 - t₀) • compactCurlField z

theorem compactPotentialField_contDiff : ContDiff ℝ ∞ compactPotentialField := by
  exact compactPotential_contDiff.comp contDiff_snd

theorem compactCurlField_contDiff : ContDiff ℝ ∞ compactCurlField := by
  exact SpatialCurl.contDiff_spatialCurl compactPotentialField_contDiff (by simp)

theorem compactPerturbation_contDiff (t₀ : ℝ) :
    ContDiff ℝ ∞ (compactPerturbation t₀) := by
  exact (contDiff_fst.sub contDiff_const).smul compactCurlField_contDiff

theorem compactCurlField_divergence_free (t : ℝ) (x : Space) :
    spatialDivergence compactCurlField t x = 0 := by
  unfold compactCurlField
  apply SpatialCurl.spatialDivergence_spatialCurl
  have hs : ContDiff ℝ ∞
      (fun y : Space => compactPotentialField (t, y)) := by
    simpa [compactPotentialField] using compactPotential_contDiff
  exact (hs.of_le (by norm_num)).contDiffAt

theorem compactCurlField_slice_hasCompactSupport (t : ℝ) :
    HasCompactSupport (fun x : Space => compactCurlField (t, x)) := by
  change HasCompactSupport (SpatialCurl.curl compactPotential)
  exact SpatialCurl.hasCompactSupport_curl compactPotential_hasCompactSupport

theorem compactPerturbation_slice_hasCompactSupport (t₀ t : ℝ) :
    HasCompactSupport (fun x : Space => compactPerturbation t₀ (t, x)) := by
  change HasCompactSupport
    ((fun _ : Space => (t - t₀)) • (fun x : Space => compactCurlField (t, x)))
  exact (compactCurlField_slice_hasCompactSupport t).smul_left

theorem compactPerturbation_divergence_free (t₀ t : ℝ) (x : Space) :
    spatialDivergence (compactPerturbation t₀) t x = 0 := by
  have hslice : DifferentiableAt ℝ
      (fun y : Space => compactCurlField (t, y)) x := by
    have hglobal : ContDiffOn ℝ ∞ compactCurlField
        ((Set.univ : Set ℝ) ×ˢ (Set.univ : Set Space)) :=
      compactCurlField_contDiff.contDiffOn
    have hs2 : ContDiff ℝ 2 (fun y : Space => compactCurlField (t, y)) :=
      (SpatialCurl.contDiff_spatialSlice hglobal (by simp)).of_le (by norm_num)
    exact (hs2.contDiffAt.differentiableAt (by norm_num))
  change spatialDivergence
    (fun z => (t - t₀) • compactCurlField z) t x = 0
  rw [NavierStokes.ResidualCalculus.spatialDivergence_const_smul
    compactCurlField t x (t - t₀) hslice]
  rw [compactCurlField_divergence_free, mul_zero]

theorem compactPerturbation_temporalDerivative_at_switch (t₀ : ℝ) (x : Space) :
    temporalDerivative (compactPerturbation t₀) t₀ x = compactCurlField (t₀, x) := by
  unfold temporalDerivative compactPerturbation
  change fderiv ℝ (fun s : ℝ =>
    (s - t₀) • compactCurlField (t₀, x)) t₀ 1 = _
  have h := (((hasDerivAt_id t₀).sub_const t₀).smul_const
    (compactCurlField (t₀, x))).hasFDerivAt.fderiv
  have h1 := congrArg (fun L => L (1 : ℝ)) h
  simpa only [id_eq, one_smul, ContinuousLinearMap.toSpanSingleton_apply] using h1

theorem compactPerturbation_value_at_switch (t₀ : ℝ) (x : Space) :
    compactPerturbation t₀ (t₀, x) = 0 := by
  simp [compactPerturbation]

theorem compactPerturbation_spatialDerivative_at_switch (t₀ : ℝ) (x : Space) :
    spatialDerivative (compactPerturbation t₀) t₀ x = 0 := by
  unfold spatialDerivative compactPerturbation
  simp

theorem compactPerturbation_spatialLaplacian_at_switch (t₀ : ℝ) (x : Space) :
    spatialLaplacian (compactPerturbation t₀) t₀ x = 0 := by
  unfold spatialLaplacian spatialDerivative compactPerturbation
  simp

theorem compactPerturbation_fixed_force_defect_at_switch
    (u : VelocityField) (t₀ : ℝ) (x : Space) :
    temporalDerivative (compactPerturbation t₀) t₀ x -
        spatialLaplacian (compactPerturbation t₀) t₀ x +
        spatialDerivative u t₀ x (compactPerturbation t₀ (t₀, x)) +
        spatialDerivative (compactPerturbation t₀) t₀ x (u (t₀, x)) +
        spatialDerivative (compactPerturbation t₀) t₀ x
          (compactPerturbation t₀ (t₀, x)) =
      compactCurlField (t₀, x) := by
  rw [compactPerturbation_temporalDerivative_at_switch,
    compactPerturbation_spatialLaplacian_at_switch,
    compactPerturbation_spatialDerivative_at_switch,
    compactPerturbation_value_at_switch]
  simp

theorem coordinateVector_zero_ne_zero :
    coordinateVector (0 : Fin 3) ≠ (0 : Space) := by
  intro h
  have h0 := congrArg (fun v : Space => v (0 : Fin 3)) h
  simp [coordinateVector] at h0

theorem compactCurlField_at_origin (t : ℝ) :
    compactCurlField (t, 0) = coordinateVector 0 := by
  unfold compactCurlField SpatialCurl.spatialCurl compactPotentialField
  exact compactPotential_curl_at_zero

theorem compactPerturbation_fixed_force_defect_nonzero_at_origin
    (u : VelocityField) (t₀ : ℝ) :
    temporalDerivative (compactPerturbation t₀) t₀ 0 -
        spatialLaplacian (compactPerturbation t₀) t₀ 0 +
        spatialDerivative u t₀ 0 (compactPerturbation t₀ (t₀, 0)) +
        spatialDerivative (compactPerturbation t₀) t₀ 0 (u (t₀, 0)) +
        spatialDerivative (compactPerturbation t₀) t₀ 0
          (compactPerturbation t₀ (t₀, 0)) ≠ 0 := by
  rw [compactPerturbation_fixed_force_defect_at_switch]
  rw [compactCurlField_at_origin]
  exact coordinateVector_zero_ne_zero

theorem compactPerturbation_breaks_any_fixed_force_at_origin
    (u : VelocityField) (p : PressureField) (f : VelocityField) (t₀ : ℝ)
    (hbase : ∀ t x, navierStokesResidual u p t x = f (t, x))
    (hut : DifferentiableAt ℝ (fun s : ℝ => u (s, 0)) t₀)
    (hu : ContDiff ℝ 2 (fun y : Space => u (t₀, y)))
    (hp : DifferentiableAt ℝ (fun y : Space => p (t₀, y)) 0) :
    ¬ (∀ t x, navierStokesResidual
      (fun z => u z + compactPerturbation t₀ z) p t x = f (t, x)) := by
  intro hpert
  have hzero_pressure : DifferentiableAt ℝ (fun _ : Space => (0 : ℝ)) 0 :=
    differentiableAt_const (c := (0 : ℝ))
  have hj2 : ContDiff ℝ 2 (compactPerturbation t₀) :=
    (compactPerturbation_contDiff t₀).of_le (by norm_num)
  have ht2 : ContDiff ℝ 2
      (fun s : ℝ => compactPerturbation t₀ (s, 0)) :=
    hj2.comp (contDiff_id.prodMk contDiff_const)
  have hs2 : ContDiff ℝ 2
      (fun y : Space => compactPerturbation t₀ (t₀, y)) :=
    hj2.comp (contDiff_const.prodMk contDiff_id)
  have hidentity := NavierStokes.ResidualCalculus.navierStokesResidual_add_sub
    u (compactPerturbation t₀) p (fun _ => 0) t₀ 0 hut
    (ht2.contDiffAt.differentiableAt (by norm_num)) hu hs2 hp hzero_pressure
  have hresidual_zero :
      navierStokesResidual
          (fun z => u z + compactPerturbation t₀ z) p t₀ 0 -
          navierStokesResidual u p t₀ 0 = 0 := by
    rw [hpert t₀ 0, hbase t₀ 0]
    simp
  have hzero_defect :
      temporalDerivative (compactPerturbation t₀) t₀ 0 -
        spatialLaplacian (compactPerturbation t₀) t₀ 0 +
        spatialDerivative u t₀ 0 (compactPerturbation t₀ (t₀, 0)) +
        spatialDerivative (compactPerturbation t₀) t₀ 0 (u (t₀, 0)) +
        spatialDerivative (compactPerturbation t₀) t₀ 0
          (compactPerturbation t₀ (t₀, 0)) = 0 := by
    calc
      _ = navierStokesResidual
          (fun z => u z + compactPerturbation t₀ z) p t₀ 0 -
            navierStokesResidual u p t₀ 0 := by
          simpa [pressureGradient] using hidentity.symm
      _ = 0 := hresidual_zero
  exact (compactPerturbation_fixed_force_defect_nonzero_at_origin u t₀) hzero_defect

/-!
The same local obstruction can be instantiated at the actual selected witness.
This is deliberately an operator-level result: it proves path dependence of the
fixed-force equation, not stability of the CMI existential quantifier.
-/

theorem selected_candidate_fixed_force_obstruction :
    ∃ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f ∧
      navierStokesResidual
          (fun z => u z + compactPerturbation ((1 : ℝ) / 2) z) p
          ((1 : ℝ) / 2) 0 ≠ f (((1 : ℝ) / 2), 0) := by
  obtain ⟨a, _, ea, eb, ep, forcing, hc, _⟩ :=
    NavierStokes.ActualCandidateAssembly.selected_witness
  let ASum := SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
      (PhysicalWaveSum.physicalQ h)
      (NavierStokes.ActualCandidateAssembly.potentialStages
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        ActualCandidateConstruction.selectedThreshold_geometry)
  let BSum := SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
      (PhysicalWaveSum.physicalQ h)
      (NavierStokes.ActualCandidateAssembly.directStages
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        ActualCandidateConstruction.selectedThreshold_geometry)
  let PSum := SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
      (PhysicalWaveSum.physicalQ h)
      (NavierStokes.ActualCandidateAssembly.pressureStages
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        ActualCandidateConstruction.selectedThreshold_geometry)
  let u : VelocityField :=
    TimeLocalization.activatedVelocity
      (MixedPeriodicAssembly.periodicVelocity ASum BSum)
  let p : PressureField :=
    TimeLocalization.activatedPressure
      (SpatialLocalization.periodicPressure PSum)
  have hc' : CandidateProperties u p forcing := by
    simpa [u, p, ASum, BSum, PSum] using hc
  refine ⟨u, p, forcing, hc', ?_⟩
  have ht : ((1 : ℝ) / 2) ∈ Ioo (0 : ℝ) 1 := by norm_num
  have htu : DifferentiableAt ℝ (fun s : ℝ => u (s, (0 : Space)))
      ((1 : ℝ) / 2) := by
    have hjoint := ProblemStatement.smooth_at_interior hc'.velocity_smooth ht 0
    exact (hjoint.comp ((1 : ℝ) / 2)
      (contDiffAt_id.prodMk contDiffAt_const)).differentiableAt (by simp)
  have hu : ContDiff ℝ 2 (fun y : Space => u (((1 : ℝ) / 2, y))) := by
    exact (TimeLocalization.spatial_smooth_including_initial _ hc'.velocity_smooth
      ((1 : ℝ) / 2) ⟨by norm_num, by norm_num⟩).of_le (by norm_num)
  have hp : DifferentiableAt ℝ (fun y : Space => p (((1 : ℝ) / 2, y))) 0 := by
    exact ((TimeLocalization.spatial_smooth_including_initial _ hc'.pressure_smooth
      ((1 : ℝ) / 2) ⟨by norm_num, by norm_num⟩).differentiable (by simp) 0)
  intro hpert
  have hzero_pressure : DifferentiableAt ℝ (fun _ : Space => (0 : ℝ)) 0 :=
    differentiableAt_const (c := (0 : ℝ))
  have hj2 : ContDiff ℝ 2 (compactPerturbation ((1 : ℝ) / 2)) :=
    (compactPerturbation_contDiff ((1 : ℝ) / 2)).of_le (by norm_num)
  have ht2 : ContDiff ℝ 2
      (fun s : ℝ => compactPerturbation ((1 : ℝ) / 2) (s, 0)) :=
    hj2.comp (contDiff_id.prodMk contDiff_const)
  have hs2 : ContDiff ℝ 2
      (fun y : Space => compactPerturbation ((1 : ℝ) / 2) ((1 : ℝ) / 2, y)) :=
    hj2.comp (contDiff_const.prodMk contDiff_id)
  have hidentity := NavierStokes.ResidualCalculus.navierStokesResidual_add_sub
    u (compactPerturbation ((1 : ℝ) / 2)) p (fun _ => 0) ((1 : ℝ) / 2) 0 htu
    ((ht2.contDiffAt.differentiableAt (by norm_num))) hu hs2 hp hzero_pressure
  have hresidual_zero :
      navierStokesResidual
          (fun z => u z + compactPerturbation ((1 : ℝ) / 2) z) p
            ((1 : ℝ) / 2) 0 -
          navierStokesResidual u p ((1 : ℝ) / 2) 0 = 0 := by
    rw [hpert, hc'.navier_stokes ((1 : ℝ) / 2) ht 0]
    simp
  have hzero_defect :
      temporalDerivative (compactPerturbation ((1 : ℝ) / 2)) ((1 : ℝ) / 2) 0 -
        spatialLaplacian (compactPerturbation ((1 : ℝ) / 2)) ((1 : ℝ) / 2) 0 +
        spatialDerivative u ((1 : ℝ) / 2) 0
          (compactPerturbation ((1 : ℝ) / 2) (((1 : ℝ) / 2), 0)) +
        spatialDerivative (compactPerturbation ((1 : ℝ) / 2)) ((1 : ℝ) / 2) 0
          (u (((1 : ℝ) / 2), 0)) +
        spatialDerivative (compactPerturbation ((1 : ℝ) / 2)) ((1 : ℝ) / 2) 0
          (compactPerturbation ((1 : ℝ) / 2) (((1 : ℝ) / 2), 0)) = 0 := by
    calc
      _ = navierStokesResidual
          (fun z => u z + compactPerturbation ((1 : ℝ) / 2) z) p
            ((1 : ℝ) / 2) 0 -
            navierStokesResidual u p ((1 : ℝ) / 2) 0 := by
          simpa [pressureGradient] using hidentity.symm
      _ = 0 := hresidual_zero
  exact (compactPerturbation_fixed_force_defect_nonzero_at_origin u
    ((1 : ℝ) / 2)) hzero_defect
