import NavierStokes.PhysicalResidualJetBounds

/-!
# Off-axis scope of `StateRealization.chartIdentity`

This probe records a scope fact, not a contradiction: the chart identity is
proved only on the positive-radius source.  The singular point used by the
origin blow-up is excluded from that source.
-/

noncomputable section

open Set
open NavierStokes ProblemStatement
open NavierStokes.PhysicalResidualJetBounds
open NavierStokes.PhysicalResidualTZ

namespace NavierStokesReview

theorem state_realization_domain_excludes_axis
    {h : ℝ} {N : ℕ} {gap : ℕ → ℕ} {U : Set PhysicalResidualJetBounds.Cylinder}
    {c : CorrectionState.Context PhysicalResidualJetBounds.Point}
    {s : CorrectionState.State PhysicalResidualJetBounds.Point}
    {p₀ : ℕ → PhysicalResidualJetBounds.Cylinder → ℝ}
    {u : VelocityField} {P : PressureField}
    (r : StateRealization h N gap U c s p₀ u P) :
    ¬ ∃ x : PhysicalResidualJetBounds.Cylinder, x ∈ U ∧ x.1.1 = 0 := by
  rintro ⟨x, hx, hzero⟩
  exact (r.radius_ne x hx) hzero

theorem graph_source_excludes_singular_origin
    {G : PhysicalResidualBridge.ScaledGraph}
    {U : Set PhysicalResidualTZ.Cylinder} :
    ((1 : ℝ), (0 : Space)) ∉ graphSourceTZ G U := by
  intro h
  exact (lt_irrefl (0 : ℝ)) h.1

end NavierStokesReview
