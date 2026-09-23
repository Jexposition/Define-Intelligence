import NavierStokes.ActualCandidateAssembly
import NavierStokes.PhysicalResidualJetBounds
import NavierStokes.SpatialLocalization
import NavierStokes.R3.ProblemStatement

/-!
# Semantic transport and pressure-support audit

This probe records only facts proved from the source declarations.  It does
not infer a contradiction from the existence of a three-coordinate debt, and
it does not infer that compact pressure support is trivial.  Those two
inferences require additional premises which are not present in the selected
endpoint.
-/

noncomputable section

open Set MeasureTheory
open NavierStokes
open NavierStokes.FiveRowRank

namespace NavierStokesReview.SemanticTransportPressureProbe

theorem five_rows_expose_the_two_fixed_rows
    {V G : ℝ → ℝ} {d : FiveRowRank.Debt} {dv ga : ℝ → ℝ}
    (h : FiveRowRank.FiveRows V G d dv ga) :
    (∫ R, R ^ (2 : ℕ) * dv R) = 0 ∧ (∫ R, R * ga R) = 0 := by
  exact ⟨h.1, h.2.1⟩

theorem five_rows_retain_all_three_debt_coordinates
    {V G : ℝ → ℝ} {d : FiveRowRank.Debt} {dv ga : ℝ → ℝ}
    (h : FiveRowRank.FiveRows V G d dv ga) :
    (∫ R, (2 * V R / R) * dv R) = -(d 0) ∧
      (∫ R, R ^ (2 : ℕ) * (G R * dv R + V R * ga R)) = -(d 1) ∧
      (∫ R, 2 * R * G R * ga R - R * V R * dv R) = -(d 2) := by
  exact ⟨h.2.2.1, h.2.2.2.1, h.2.2.2.2⟩

theorem compact_support_does_not_force_a_pressure_slice_to_zero :
    ¬ (∀ f : NavierStokes.ProblemStatement.Space → ℝ,
        HasCompactSupport f → f = 0) := by
  intro h
  have hc : HasCompactSupport NavierStokes.SpatialLocalization.spatialCutoff :=
    NavierStokes.SpatialLocalization.spatialCutoff_hasCompactSupport
  have hz : NavierStokes.SpatialLocalization.spatialCutoff 0 = 1 := by
    apply NavierStokes.SpatialLocalization.spatialCutoff_eq_one
    exact NavierStokes.SpatialLocalization.zero_mem_plateau
  have hzero := h NavierStokes.SpatialLocalization.spatialCutoff hc
  have := congrFun hzero 0
  rw [hz] at this
  norm_num at this

end NavierStokesReview.SemanticTransportPressureProbe
