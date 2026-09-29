import NavierStokes.CyclePhysicalPrefixes

/-!
# Selected Cartesian component transport

This completion records the exact component-level transport available on the
valid positive-radius polar chart.  It is deliberately narrower than a
Cartesian-to-radial moment theorem: it does not identify a global torus
average, a radial `barMoment`, or a nonzero localisation remainder.
-/

noncomputable section

namespace NavierStokesReview.SelectedCylindricalComponentTransport

open NavierStokes
open NavierStokes.CyclePhysicalPrefixes

theorem frame_component_one (θ : ℝ) (v : ProblemStatement.Space) :
    (CylindricalResidual.frame θ v) 1 =
      Real.sin θ * v 0 + Real.cos θ * v 1 := by
  rw [CylindricalResidual.frame_apply]
  simp only [AxisymmetricResidual.pack_one]

theorem velocity_polar_component_one
    {a : ℝ} (ha : 0 < a) (j : PolarCharts.Index)
    (G : ScaledGraph) (n : ℕ)
    (c : CorrectionState.Context CorrectionStep.CyclePoint)
    (u : CorrectionState.State CorrectionStep.CyclePoint)
    {z : ProblemStatement.SpaceTime}
    (hz : z ∈ PhysicalCurlCovariance.validCylindrical a j) :
    (velocity a j G n c u (z.1, CylindricalResidual.chart z.2)) 1 =
      Real.sin (z.2 1) * (cylindricalVelocity G n c u z) 0 +
        Real.cos (z.2 1) * (cylindricalVelocity G n c u z) 1 := by
  rw [velocity_polar_forward ha j G n c u hz]
  exact frame_component_one _ _

end NavierStokesReview.SelectedCylindricalComponentTransport
