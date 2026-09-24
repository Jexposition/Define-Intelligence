import NavierStokes.ActualCandidateAssembly
import NavierStokes.LocalScheduleWitness

/-!
# Selected-witness endpoint residual probe

This probe isolates the exact missing implication in the proposed force
attack.  The selected witness does identify the interior residual with the
force.  A contradiction additionally needs a positive residual lower bound
along the same blow-up path; smoothness and speed blow-up alone do not supply
that lower bound.
-/

noncomputable section

open Set Filter
open scoped Topology ContDiff

namespace NavierStokesReview.SelectedWitnessEndpointResidualProbe

open NavierStokes.ProblemStatement

theorem selected_origin_speed_tendsto :
    ∃ a : ℕ → ℕ,
      NavierStokes.MixedCandidateWitness.SelectedSchedule
        NavierStokes.CorrectionInitialization.ActualPrimary.h
        (NavierStokes.ActualCandidateConstruction.qbig
          NavierStokes.ActualCandidateConstruction.selectedBudget
          NavierStokes.ActualCandidateConstruction.selectedThreshold)
        NavierStokes.ActualCandidateAssembly.selectedPotentialStages
        NavierStokes.ActualCandidateAssembly.selectedDirectStages
        NavierStokes.ActualCandidateAssembly.selectedPressureStages a ∧
      Tendsto (fun t : ℝ => ‖NavierStokes.MixedPeriodicAssembly.velocity
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a) (t, 0)‖)
        (𝓝[<] (1 : ℝ)) atTop := by
  obtain ⟨a, ha, _, _, _, _, _, _, _⟩ :=
    NavierStokes.ActualCandidateAssembly.selected_witness
  have ha' : NavierStokes.LocalScheduleWitness.Selected a := by
    change NavierStokes.MixedCandidateWitness.SelectedSchedule
      NavierStokes.CorrectionInitialization.ActualPrimary.h
      (NavierStokes.ActualCandidateConstruction.qbig
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold)
      (NavierStokes.ActualCandidateAssembly.potentialStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry)
      (NavierStokes.ActualCandidateAssembly.directStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry)
      (NavierStokes.ActualCandidateAssembly.pressureStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry) a
    exact ha
  exact ⟨a, ha', NavierStokes.LocalScheduleWitness.selected_origin_blowup ha'⟩

theorem selected_origin_residual_tends_zero :
    ∃ a : ℕ → ℕ,
      NavierStokes.LocalScheduleWitness.Selected a ∧
      Tendsto (fun t : ℝ => ‖NavierStokes.MixedPeriodicAssembly.originalResidual
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a)
        (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0)‖)
        (𝓝[<] (1 : ℝ)) (𝓝 0) := by
  obtain ⟨a, ha, _, _, _, _, _, _, _⟩ :=
    NavierStokes.ActualCandidateAssembly.selected_witness
  have ha' : NavierStokes.LocalScheduleWitness.Selected a := by
    change NavierStokes.MixedCandidateWitness.SelectedSchedule
      NavierStokes.CorrectionInitialization.ActualPrimary.h
      (NavierStokes.ActualCandidateConstruction.qbig
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold)
      (NavierStokes.ActualCandidateAssembly.potentialStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry)
      (NavierStokes.ActualCandidateAssembly.directStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry)
      (NavierStokes.ActualCandidateAssembly.pressureStages
        NavierStokes.ActualCandidateConstruction.selectedBudget
        NavierStokes.ActualCandidateConstruction.selectedThreshold
        NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry) a
    exact ha
  have hkeep := ha'
  obtain ⟨_, _, _, _, _, _, _, hz⟩ := ha'
  have hres0 := hz 0
  have hpath : Tendsto (fun t : ℝ => (t, (0 : Space)))
      (𝓝[<] (1 : ℝ))
      (𝓝[NavierStokes.SpacetimeEndpoint.openPast 1] ((1 : ℝ), (0 : Space))) := by
    rw [NavierStokes.JointResidualLimits.past_filter]
    exact tendsto_id.prodMk tendsto_const_nhds
  have hres : Tendsto (fun t : ℝ => ‖NavierStokes.MixedPeriodicAssembly.originalResidual
      (NavierStokes.LocalScheduleWitness.potentialSum a)
      (NavierStokes.LocalScheduleWitness.directSum a)
      (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0)‖)
      (𝓝[<] (1 : ℝ)) (𝓝 0) := by
    have hcomp := hres0.comp hpath
    simpa only [NavierStokes.MixedDiagonalResidual.residual_eq_originalResidual,
      NavierStokes.LocalScheduleWitness.potentialSum,
      NavierStokes.LocalScheduleWitness.directSum,
      NavierStokes.LocalScheduleWitness.pressureSum,
      Function.comp_apply, norm_iteratedFDeriv_zero, norm_zero] using hcomp.norm
  exact ⟨a, hkeep, hres⟩

theorem selected_origin_positive_lower_bound_is_impossible
    {a : ℕ → ℕ} (ha : NavierStokes.LocalScheduleWitness.Selected a)
    {c : ℝ} (hc : 0 < c)
    (htransport : ∀ᶠ t in 𝓝[<] (1 : ℝ),
      c * ‖NavierStokes.MixedPeriodicAssembly.velocity
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a) (t, 0)‖ ≤
      ‖NavierStokes.MixedPeriodicAssembly.originalResidual
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a)
        (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0)‖) : False := by
  have hspeed := NavierStokes.LocalScheduleWitness.selected_origin_blowup ha
  obtain ⟨_, _, _, _, _, _, _, hz⟩ := ha
  have hpath : Tendsto (fun t : ℝ => (t, (0 : Space)))
      (𝓝[<] (1 : ℝ))
      (𝓝[NavierStokes.SpacetimeEndpoint.openPast 1] ((1 : ℝ), (0 : Space))) := by
    rw [NavierStokes.JointResidualLimits.past_filter]
    exact tendsto_id.prodMk tendsto_const_nhds
  have hres0 := hz 0
  have hres : Tendsto (fun t : ℝ => ‖NavierStokes.MixedPeriodicAssembly.originalResidual
      (NavierStokes.LocalScheduleWitness.potentialSum a)
      (NavierStokes.LocalScheduleWitness.directSum a)
      (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0)‖)
      (𝓝[<] (1 : ℝ)) (𝓝 0) := by
    have hcomp := hres0.comp hpath
    simpa only [NavierStokes.MixedDiagonalResidual.residual_eq_originalResidual,
      NavierStokes.LocalScheduleWitness.potentialSum,
      NavierStokes.LocalScheduleWitness.directSum,
      NavierStokes.LocalScheduleWitness.pressureSum,
      Function.comp_apply, norm_iteratedFDeriv_zero, norm_zero] using hcomp.norm
  have hv : ∀ᶠ t in 𝓝[<] (1 : ℝ), 1 <
      ‖NavierStokes.MixedPeriodicAssembly.velocity
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a) (t, 0)‖ :=
    hspeed.eventually (eventually_gt_atTop 1)
  have hr : ∀ᶠ t in 𝓝[<] (1 : ℝ),
      ‖NavierStokes.MixedPeriodicAssembly.originalResidual
        (NavierStokes.LocalScheduleWitness.potentialSum a)
        (NavierStokes.LocalScheduleWitness.directSum a)
        (NavierStokes.LocalScheduleWitness.pressureSum a) (t, 0)‖ < c :=
    hres.eventually (Iio_mem_nhds hc)
  have hfalse : ∀ᶠ t in 𝓝[<] (1 : ℝ), False := by
    filter_upwards [htransport, hv, hr] with t ht hv htres
    nlinarith
  obtain ⟨t, ht⟩ := Filter.Eventually.exists hfalse
  exact ht

theorem selected_witness_has_candidate_properties :
    ∃ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f := by
  obtain ⟨_, _, _, _, _, forcing, hc, _, _, _, _⟩ :=
    NavierStokes.ActualCandidateAssembly.selected_witness
  exact ⟨_, _, forcing, hc⟩

theorem interior_residual_is_the_selected_force
    {u : VelocityField} {p : PressureField} {f : VelocityField}
    (hc : CandidateProperties u p f) {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1)
    (x : Space) :
    navierStokesResidual u p t x = f (t, x) :=
  hc.navier_stokes t ht x

theorem lower_bound_contradicts_selected_speed
    {u : VelocityField} {p : PressureField} {f : VelocityField}
    (hc : CandidateProperties u p f)
    {c B : ℝ} (hcpos : 0 < c)
    (hspeed : Tendsto (fun t : ℝ => ‖u (t, 0)‖) (𝓝[<] (1 : ℝ)) atTop)
    (hforce : ∀ᶠ t in 𝓝[<] (1 : ℝ), ‖f (t, 0)‖ ≤ B)
    (htransport : ∀ᶠ t in 𝓝[<] (1 : ℝ),
      c * ‖u (t, 0)‖ ≤ ‖navierStokesResidual u p t 0‖) : False := by
  have hspeed : ∀ᶠ t in 𝓝[<] (1 : ℝ),
      B / c + 1 < ‖u (t, 0)‖ := by
    exact hspeed.eventually (eventually_gt_atTop (B / c + 1))
  have hpast : ∀ᶠ t in 𝓝[<] (1 : ℝ), t ∈ Ioo (0 : ℝ) 1 := by
    filter_upwards [self_mem_nhdsWithin,
      (eventually_gt_nhds (show (0 : ℝ) < 1 by norm_num)).filter_mono
        nhdsWithin_le_nhds] with t ht h0
    exact ⟨h0, ht⟩
  have hcontra : ∀ᶠ t in 𝓝[<] (1 : ℝ), False := by
    filter_upwards [hforce, htransport, hspeed, hpast] with t hf ht hs hp
    rw [hc.navier_stokes t hp 0] at ht
    have hB : c * (B / c + 1) < c * ‖u (t, 0)‖ := by
      exact mul_lt_mul_of_pos_left hs hcpos
    have hcalc : c * (B / c + 1) = B + c := by
      calc
        c * (B / c + 1) = c * (B / c) + c := by ring
        _ = B + c := by rw [mul_div_cancel₀ B (ne_of_gt hcpos)]
    have hupper : c * ‖u (t, 0)‖ ≤ B := ht.trans hf
    linarith [hcalc]
  obtain ⟨t, ht⟩ := Filter.Eventually.exists hcontra
  exact ht

end NavierStokesReview.SelectedWitnessEndpointResidualProbe
