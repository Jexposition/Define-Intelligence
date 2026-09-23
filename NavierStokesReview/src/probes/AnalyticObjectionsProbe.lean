import NavierStokes.R3.ActualCandidate
import NavierStokes.R3.ViscousEnergyBalance
import NavierStokes.ActualCandidateAssembly

/-!
# Connected analytic-objection probes

These statements keep three questions separate:

* what the selected endpoint explicitly provides;
* what exact energy identity exists in the repository; and
* whether compact pressure is actually a contradiction to the forced CMI
  formulation.

No proposed implication is accepted merely because it sounds physically
plausible. Every theorem below is connected to the selected witness.
-/

open Set
open scoped ContDiff

namespace NavierStokesR3.AnalyticObjectionsProbe

open NavierStokesR3 ProblemStatement

#check NavierStokesR3.CompactEnergy.energy_balance_viscosity
#check NavierStokesR3.CompactEnergy.hasDerivAt_energy_balance_viscosity
#check NavierStokes.CandidateFromLimits.force_smooth
#check NavierStokes.CandidateFromLimits.force_boundary_jets

theorem selected_endpoint_exposes_pressure_support :
    ∃ u : VelocityField, ∃ p : PressureField, ∃ f : VelocityField,
      ∃ K : Set Space,
        CandidateProperties 1 u p f K ∧
          ∀ t ∈ Ico (0 : ℝ) 1,
            tsupport (fun x : Space => p (t, x)) ⊆ K := by
  obtain ⟨u, p, f, K, hc, _⟩ :=
    NavierStokesR3.ActualCandidate.selected_candidate_one_with_early_zero
  exact ⟨u, p, f, K, hc, hc.pressure_support⟩

theorem selected_endpoint_exposes_energy_bound :
    ∃ u : VelocityField, ∃ p : PressureField, ∃ f : VelocityField,
      ∃ K : Set Space,
        CandidateProperties 1 u p f K ∧
          UniformFiniteEnergy (Ico (0 : ℝ) 1) u := by
  obtain ⟨u, p, f, K, hc, _⟩ :=
    NavierStokesR3.ActualCandidate.selected_candidate_one_with_early_zero
  exact ⟨u, p, f, K, hc, hc.energy_bounded⟩

theorem selected_endpoint_exposes_force_smoothness :
    ∃ u : VelocityField, ∃ p : PressureField, ∃ f : VelocityField,
      ∃ K : Set Space,
        CandidateProperties 1 u p f K ∧ ContDiff ℝ ∞ f := by
  obtain ⟨u, p, f, K, hc, _⟩ :=
    NavierStokesR3.ActualCandidate.selected_candidate_one_with_early_zero
  exact ⟨u, p, f, K, hc, hc.force_smooth⟩

end NavierStokesR3.AnalyticObjectionsProbe
