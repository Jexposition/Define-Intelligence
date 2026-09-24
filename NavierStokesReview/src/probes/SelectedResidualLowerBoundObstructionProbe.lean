import NavierStokes.CandidateConsequences

/-!
# Selected residual lower-bound obstruction

This probe formalises the exact theorem required by the proposed force-jet
attack.  Flat residual jets contradict origin velocity blow-up only if there
is a positive lower bound transporting the velocity norm into the residual
norm on the same endpoint filter.  The repository supplies the upper-rate
direction, not this lower-rate direction.
-/

noncomputable section

namespace NavierStokesReview.SelectedResidualLowerBoundObstructionProbe

open Filter NavierStokes NavierStokes.ProblemStatement
open scoped Topology ContDiff

theorem flat_residual_conflicts_with_blowup_under_lower_bound
    {D V : Type*} [NormedAddCommGroup D] [NormedSpace ℝ D]
    [NormedAddCommGroup V] [NormedSpace ℝ V]
    {l : Filter D} [NeBot l] {v r : D → ℝ} {c : ℝ}
    (hc : 0 < c)
    (hv : Tendsto v l atTop)
    (hr : Tendsto r l (𝓝 0))
    (hlower : ∀ᶠ z in l, c * v z ≤ r z) : False := by
  have hv1 : ∀ᶠ z in l, 1 < v z := hv.eventually (eventually_gt_atTop 1)
  have hr1 : ∀ᶠ z in l, r z < c := hr.eventually (Iio_mem_nhds hc)
  have hfalse : ∀ᶠ z in l, False := by
    filter_upwards [hlower, hv1, hr1] with z hz hVz hRz
    nlinarith
  obtain ⟨z, hz⟩ := Filter.Eventually.exists hfalse
  exact hz

theorem selected_origin_lower_bound_is_the_required_missing_step
    {A v : VelocityField} {p : PressureField} {l : Filter SpaceTime} [NeBot l]
    (hres : Tendsto (fun z => ‖MixedPeriodicAssembly.originalResidual A v p z‖)
      l (𝓝 0))
    (hvel : Tendsto (fun z => ‖MixedPeriodicAssembly.velocity A v z‖)
      l atTop)
    {c : ℝ} (hc : 0 < c)
    (htransport : ∀ᶠ z in l,
      c * ‖MixedPeriodicAssembly.velocity A v z‖ ≤
        ‖MixedPeriodicAssembly.originalResidual A v p z‖) : False := by
  exact flat_residual_conflicts_with_blowup_under_lower_bound
    (D := SpaceTime) (V := ℝ)
    (v := fun z => ‖MixedPeriodicAssembly.velocity A v z‖)
    (r := fun z => ‖MixedPeriodicAssembly.originalResidual A v p z‖)
    hc hvel hres htransport

theorem selected_time_lower_bound_conflicts_with_the_actual_flatness_contract
    {A v : VelocityField} {p : PressureField}
    (hz : JointResidualLimits.VanishingJointJets
      (MixedPeriodicAssembly.originalResidual A v p))
    (haxis : Tendsto (fun t : ℝ =>
      ‖MixedPeriodicAssembly.velocity A v (t, 0)‖)
      (𝓝[<] (1 : ℝ)) atTop)
    {c : ℝ} (hc : 0 < c)
    (htransport : ∀ᶠ t in 𝓝[<] (1 : ℝ),
      c * ‖MixedPeriodicAssembly.velocity A v (t, 0)‖ ≤
        ‖MixedPeriodicAssembly.originalResidual A v p (t, 0)‖) : False := by
  have hpath : Tendsto (fun t : ℝ => (t, (0 : Space)))
      (𝓝[<] (1 : ℝ))
      (𝓝[SpacetimeEndpoint.openPast 1] ((1 : ℝ), (0 : Space))) := by
    rw [JointResidualLimits.past_filter]
    exact tendsto_id.prodMk tendsto_const_nhds
  have hres0 := hz 0
  have hres : Tendsto (fun t : ℝ =>
      ‖MixedPeriodicAssembly.originalResidual A v p (t, 0)‖)
      (𝓝[<] (1 : ℝ)) (𝓝 0) := by
    have hcomp := hres0.comp hpath
    simpa only [Function.comp_apply, norm_iteratedFDeriv_zero, norm_zero] using hcomp.norm
  exact flat_residual_conflicts_with_blowup_under_lower_bound
    (D := ℝ) (V := ℝ)
    (v := fun t => ‖MixedPeriodicAssembly.velocity A v (t, 0)‖)
    (r := fun t => ‖MixedPeriodicAssembly.originalResidual A v p (t, 0)‖)
    hc haxis hres htransport

end NavierStokesReview.SelectedResidualLowerBoundObstructionProbe
