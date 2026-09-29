import NavierStokes.TailGaugePotential

/-!
# Selected base-profile transport

This completion records what the selected base profile actually provides.  The
gauged potential is not treated as a formal placeholder: its Euclidean curl is
identified with the selected slow-base velocity, and the source-level axis
blow-up is transported through that equality.  This is positive evidence for
the selected base branch, not a proof of the five-moment Cartesian bridge.
-/

noncomputable section

namespace NavierStokesReview.SelectedBaseProfileTransport

open NavierStokes
open Filter
open scoped Topology

theorem constructed_curl_eq_selected_velocity (upper : ℝ) (B : ℕ)
    {w : ProblemStatement.SpaceTime} (ht : w.1 < 1) :
    SpatialCurl.spatialCurl (TailGaugePotential.constructedPotential upper B) w =
      FinalSlowBase.velocity FinalSlowBase.actualProfile.certificate
        FinalSlowBase.actualProfile.modulation upper B w := by
  exact (TailGaugePotential.constructedPotential_properties upper B).2.2 ⟨ht, trivial⟩

theorem constructed_curl_axis_tendsto (upper : ℝ) (B : ℕ) :
    Tendsto
      (fun t : ℝ =>
        ‖SpatialCurl.spatialCurl (TailGaugePotential.constructedPotential upper B) (t, 0)‖)
      (𝓝[<] 1) atTop := by
  have hbase := FinalSlowBase.axis_tendsto
    (H := FinalSlowBase.actualProfile.certificate)
    (v := FinalSlowBase.actualProfile.modulation) upper B
  refine hbase.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with t ht
  have ht' : t < 1 := ht
  rw [constructed_curl_eq_selected_velocity (w := (t, 0)) upper B ht']

end NavierStokesReview.SelectedBaseProfileTransport
