import NavierStokes.SpacetimeEndpoint

/-!
The selected diagonal schedule uses the open-past neighbourhood filter at
`(1, 0)`.  This probe checks that the concrete filter is nontrivial, while
`DerivedFilterAudit` records the separate generic `JetRate` hazard.
-/

open Filter Set

namespace NavierStokesReview

example : (nhdsWithin ((1 : ℝ), (0 : NavierStokes.ProblemStatement.Space))
    (NavierStokes.SpacetimeEndpoint.openPast 1)).NeBot := by
  apply nhdsWithin_neBot.mpr
  intro U hU
  obtain ⟨ε, hε, hball⟩ := Metric.mem_nhds_iff.mp hU
  refine ⟨(1 - min (ε / 2) (1 / 2), (0 : NavierStokes.ProblemStatement.Space)), ?_⟩
  constructor
  · exact hball (by
      rw [Metric.mem_ball, Prod.dist_eq]
      simp
      rw [abs_of_nonneg (by positivity)]
      exact lt_of_le_of_lt (min_le_left _ _) (by linarith))
  · exact ⟨sub_lt_self (1 : ℝ) (by positivity), Set.mem_univ _⟩

end NavierStokesReview
