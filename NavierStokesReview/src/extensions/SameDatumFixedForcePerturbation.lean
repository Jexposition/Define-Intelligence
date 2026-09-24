import external_semantic.FixedForcePerturbationStability

noncomputable section

namespace NavierStokesReview.SameDatumFixedForcePerturbation

open Set
open NavierStokes ProblemStatement
open NavierStokesReview.FixedForcePerturbationStability
open scoped Topology ContDiff

/-!
# Same-datum fixed-force obstruction

The earlier fixed-force perturbation changes the value at time zero.  This
extension removes that ambiguity.  The perturbation below vanishes at both
time zero and an interior switch time `t₀`, while its time derivative at the
switch is nonzero.  It is smooth, spatially compact on every slice, and
divergence-free.  Thus it tests fixed-force compatibility without changing
the zero initial datum.
-/

def sameDatumCompactPerturbation (t₀ : ℝ) : VelocityField :=
  fun z => (z.1 * (z.1 - t₀)) • compactCurlField z

theorem sameDatumCompactPerturbation_contDiff (t₀ : ℝ) :
    ContDiff ℝ ∞ (sameDatumCompactPerturbation t₀) := by
  exact (contDiff_fst.mul (contDiff_fst.sub contDiff_const)).smul
    compactCurlField_contDiff

theorem sameDatumCompactPerturbation_slice_hasCompactSupport (t₀ t : ℝ) :
    HasCompactSupport
      (fun x : Space => sameDatumCompactPerturbation t₀ (t, x)) := by
  change HasCompactSupport
    ((fun _ : Space => t * (t - t₀)) • (fun x : Space => compactCurlField (t, x)))
  exact (compactCurlField_slice_hasCompactSupport t).smul_left

theorem sameDatumCompactPerturbation_zero_initial (t₀ : ℝ) (x : Space) :
    sameDatumCompactPerturbation t₀ (0, x) = 0 := by
  simp [sameDatumCompactPerturbation]

theorem sameDatumCompactPerturbation_divergence_free (t₀ t : ℝ) (x : Space) :
    spatialDivergence (sameDatumCompactPerturbation t₀) t x = 0 := by
  have hslice : DifferentiableAt ℝ
      (fun y : Space => compactCurlField (t, y)) x := by
    have hglobal : ContDiffOn ℝ ∞ compactCurlField
        ((Set.univ : Set ℝ) ×ˢ (Set.univ : Set Space)) :=
      compactCurlField_contDiff.contDiffOn
    have hs2 : ContDiff ℝ 2 (fun y : Space => compactCurlField (t, y)) :=
      (SpatialCurl.contDiff_spatialSlice hglobal (by simp)).of_le (by norm_num)
    exact hs2.contDiffAt.differentiableAt (by norm_num)
  change spatialDivergence
    (fun z => (t * (t - t₀)) • compactCurlField z) t x = 0
  rw [NavierStokes.ResidualCalculus.spatialDivergence_const_smul
    compactCurlField t x (t * (t - t₀)) hslice]
  rw [compactCurlField_divergence_free, mul_zero]

theorem sameDatumCompactPerturbation_value_at_switch (t₀ : ℝ) (x : Space) :
    sameDatumCompactPerturbation t₀ (t₀, x) = 0 := by
  simp [sameDatumCompactPerturbation]

theorem sameDatumCompactPerturbation_spatialDerivative_at_switch
    (t₀ : ℝ) (x : Space) :
    spatialDerivative (sameDatumCompactPerturbation t₀) t₀ x = 0 := by
  unfold spatialDerivative sameDatumCompactPerturbation
  simp

theorem sameDatumCompactPerturbation_spatialLaplacian_at_switch
    (t₀ : ℝ) (x : Space) :
    spatialLaplacian (sameDatumCompactPerturbation t₀) t₀ x = 0 := by
  unfold spatialLaplacian spatialDerivative sameDatumCompactPerturbation
  simp

theorem sameDatumCompactPerturbation_temporalDerivative_at_switch
    (t₀ : ℝ) (x : Space) :
    temporalDerivative (sameDatumCompactPerturbation t₀) t₀ x =
      t₀ • compactCurlField (t₀, x) := by
  unfold temporalDerivative sameDatumCompactPerturbation
  change fderiv ℝ (fun s : ℝ => (s * (s - t₀)) • compactCurlField (t₀, x)) t₀ 1 = _
  have hpoly : HasDerivAt (fun s : ℝ => s * (s - t₀)) t₀ t₀ := by
    change HasDerivAt (id * (fun s : ℝ => s - t₀)) t₀ t₀
    simpa [id_eq, sub_self] using
      ((hasDerivAt_id t₀).mul ((hasDerivAt_id t₀).sub_const t₀))
  have h := (hpoly.smul_const (compactCurlField (t₀, x))).hasFDerivAt.fderiv
  have h1 := congrArg (fun L => L (1 : ℝ)) h
  simpa only [id_eq, one_smul, ContinuousLinearMap.toSpanSingleton_apply,
    smul_eq_mul] using h1

theorem sameDatumCompactPerturbation_fixed_force_defect_at_switch
    (u : VelocityField) (t₀ : ℝ) (x : Space) :
    temporalDerivative (sameDatumCompactPerturbation t₀) t₀ x -
        spatialLaplacian (sameDatumCompactPerturbation t₀) t₀ x +
        spatialDerivative u t₀ x
          (sameDatumCompactPerturbation t₀ (t₀, x)) +
        spatialDerivative (sameDatumCompactPerturbation t₀) t₀ x
          (u (t₀, x)) +
        spatialDerivative (sameDatumCompactPerturbation t₀) t₀ x
          (sameDatumCompactPerturbation t₀ (t₀, x)) =
      t₀ • compactCurlField (t₀, x) := by
  rw [sameDatumCompactPerturbation_temporalDerivative_at_switch,
    sameDatumCompactPerturbation_spatialLaplacian_at_switch,
    sameDatumCompactPerturbation_spatialDerivative_at_switch,
    sameDatumCompactPerturbation_value_at_switch]
  simp

theorem sameDatumCompactPerturbation_fixed_force_defect_nonzero_at_origin
    (u : VelocityField) {t₀ : ℝ} (ht₀ : t₀ ≠ 0) :
    temporalDerivative (sameDatumCompactPerturbation t₀) t₀ 0 -
        spatialLaplacian (sameDatumCompactPerturbation t₀) t₀ 0 +
        spatialDerivative u t₀ 0
          (sameDatumCompactPerturbation t₀ (t₀, 0)) +
        spatialDerivative (sameDatumCompactPerturbation t₀) t₀ 0
          (u (t₀, 0)) +
        spatialDerivative (sameDatumCompactPerturbation t₀) t₀ 0
          (sameDatumCompactPerturbation t₀ (t₀, 0)) ≠ 0 := by
  rw [sameDatumCompactPerturbation_fixed_force_defect_at_switch,
    compactCurlField_at_origin]
  intro h
  exact smul_ne_zero ht₀ coordinateVector_zero_ne_zero h

def SameDatumAdmissiblePerturbation (e : VelocityField) : Prop :=
  NavierStokesReview.FixedForcePerturbationStability.AdmissiblePerturbation e ∧
    ∀ x : Space, e (0, x) = 0

def FixedForceSameDatumStable (u : VelocityField) (p : PressureField)
    (f : VelocityField) : Prop :=
  ∀ e : VelocityField, SameDatumAdmissiblePerturbation e →
    ∀ t : ℝ, ∀ x : Space,
      navierStokesResidual (fun z => u z + e z) p t x = f (t, x)

theorem sameDatumCompactPerturbation_admissible (t₀ : ℝ) :
    SameDatumAdmissiblePerturbation (sameDatumCompactPerturbation t₀) := by
  refine ⟨?_, ?_⟩
  · refine ⟨sameDatumCompactPerturbation_contDiff t₀, ?_, ?_⟩
    · intro t
      exact sameDatumCompactPerturbation_slice_hasCompactSupport t₀ t
    · intro t x
      exact sameDatumCompactPerturbation_divergence_free t₀ t x
  · exact sameDatumCompactPerturbation_zero_initial t₀

theorem selected_candidate_fails_fixed_force_same_datum_stability :
    ∃ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f ∧ ¬ FixedForceSameDatumStable u p f := by
  obtain ⟨u, p, f, hc, _⟩ := selected_candidate_fixed_force_obstruction
  refine ⟨u, p, f, hc, ?_⟩
  intro hstable
  let t₀ : ℝ := 1 / 2
  have ht₀ : t₀ ≠ 0 := by norm_num [t₀]
  have hpert := hstable (sameDatumCompactPerturbation t₀)
    (sameDatumCompactPerturbation_admissible t₀) t₀ 0
  have ht : t₀ ∈ Ioo (0 : ℝ) 1 := by norm_num [t₀]
  have htu : DifferentiableAt ℝ (fun s : ℝ => u (s, (0 : Space))) t₀ := by
    have hjoint := ProblemStatement.smooth_at_interior hc.velocity_smooth ht 0
    exact (hjoint.comp t₀ (contDiffAt_id.prodMk contDiffAt_const)).differentiableAt (by simp)
  have hu : ContDiff ℝ 2 (fun y : Space => u (t₀, y)) := by
    exact (TimeLocalization.spatial_smooth_including_initial _ hc.velocity_smooth t₀
      ⟨by norm_num [t₀], by norm_num [t₀]⟩).of_le (by norm_num)
  have hp : DifferentiableAt ℝ (fun y : Space => p (t₀, y)) 0 := by
    exact ((TimeLocalization.spatial_smooth_including_initial _ hc.pressure_smooth t₀
      ⟨by norm_num [t₀], by norm_num [t₀]⟩).differentiable (by simp) 0)
  have hzero_pressure : DifferentiableAt ℝ (fun _ : Space => (0 : ℝ)) 0 :=
    differentiableAt_const (c := (0 : ℝ))
  have hj2 : ContDiff ℝ 2 (sameDatumCompactPerturbation t₀) :=
    (sameDatumCompactPerturbation_contDiff t₀).of_le (by norm_num)
  have ht2 : ContDiff ℝ 2
      (fun s : ℝ => sameDatumCompactPerturbation t₀ (s, 0)) :=
    hj2.comp (contDiff_id.prodMk contDiff_const)
  have hs2 : ContDiff ℝ 2
      (fun y : Space => sameDatumCompactPerturbation t₀ (t₀, y)) :=
    hj2.comp (contDiff_const.prodMk contDiff_id)
  have hidentity := NavierStokes.ResidualCalculus.navierStokesResidual_add_sub
    u (sameDatumCompactPerturbation t₀) p (fun _ => 0) t₀ 0 htu
    (ht2.contDiffAt.differentiableAt (by norm_num)) hu hs2 hp hzero_pressure
  have hresidual_zero :
      navierStokesResidual
          (fun z => u z + sameDatumCompactPerturbation t₀ z) p t₀ 0 -
          navierStokesResidual u p t₀ 0 = 0 := by
    rw [hpert, hc.navier_stokes t₀ ht 0]
    simp
  have hzero_defect :
      temporalDerivative (sameDatumCompactPerturbation t₀) t₀ 0 -
        spatialLaplacian (sameDatumCompactPerturbation t₀) t₀ 0 +
        spatialDerivative u t₀ 0
          (sameDatumCompactPerturbation t₀ (t₀, 0)) +
        spatialDerivative (sameDatumCompactPerturbation t₀) t₀ 0
          (u (t₀, 0)) +
        spatialDerivative (sameDatumCompactPerturbation t₀) t₀ 0
          (sameDatumCompactPerturbation t₀ (t₀, 0)) = 0 := by
    calc
      _ = navierStokesResidual
          (fun z => u z + sameDatumCompactPerturbation t₀ z) p t₀ 0 -
            navierStokesResidual u p t₀ 0 := by
          simpa [pressureGradient] using hidentity.symm
      _ = 0 := hresidual_zero
  exact (sameDatumCompactPerturbation_fixed_force_defect_nonzero_at_origin u ht₀)
    hzero_defect

end NavierStokesReview.SameDatumFixedForcePerturbation
