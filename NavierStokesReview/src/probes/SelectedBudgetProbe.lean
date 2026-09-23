import NavierStokes.ActualCandidateConstruction

open NavierStokes

/-!
# Selected parameter probe

This probe records the literal selected parameters used by the endpoint.  It
does not claim that `selectedBudget = 0` truncates the stage construction: the
stage functions remain indexed by `j : ℕ`.
-/

theorem selected_budget_is_zero :
    ActualCandidateConstruction.selectedBudget = 0 := by
  rfl

theorem selected_budget_is_not_positive :
    ¬ 0 < ActualCandidateConstruction.selectedBudget := by
  simp [ActualCandidateConstruction.selectedBudget]

theorem selected_threshold_is_geometrically_admissible :
    ActualCarrierGeometry.geometricThreshold ≤
      ActualCandidateConstruction.selectedThreshold :=
  ActualCandidateConstruction.selectedThreshold_geometry
