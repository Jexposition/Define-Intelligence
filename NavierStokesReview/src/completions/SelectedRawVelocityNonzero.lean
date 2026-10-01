import NavierStokes.LocalScheduleWitness

/-!
# Nonzero value on the selected raw mixed velocity

This completion records the strongest nonzero fact currently available without
pretending it is the nonzero premise required by the selected radial
`barMoment` gate.  The selected origin blow-up gives a nonzero value of the
full raw mixed velocity somewhere before time one.  It does not identify the
point, component, or radial pullback used by the periodic-support gate.
-/

noncomputable section

namespace NavierStokesReview.SelectedRawVelocityNonzero

open NavierStokes

theorem selected_witness_raw_velocity_has_nonzero_value :
    ∃ a : ℕ → ℕ,
      LocalScheduleWitness.Selected a ∧
        ∃ t : ℝ, ∃ x : ProblemStatement.Space,
          MixedPeriodicAssembly.velocity
            (LocalScheduleWitness.potentialSum a)
            (LocalScheduleWitness.directSum a) (t, x) ≠ 0 := by
  obtain ⟨a, ha, _, _, _, _, _, _, _⟩ := ActualCandidateAssembly.selected_witness
  have haxis := LocalScheduleWitness.selected_origin_blowup ha
  have hunbounded := NaturalCore.speedUnbounded_of_axis_tendsto haxis
  obtain ⟨t, x, ht, hnear, hlarge⟩ := hunbounded 1 zero_lt_one 1 zero_lt_one
  refine ⟨a, ha, t, x, ?_⟩
  intro hzero
  have hnorm : ‖MixedPeriodicAssembly.velocity
      (LocalScheduleWitness.potentialSum a)
      (LocalScheduleWitness.directSum a) (t, x)‖ = 0 := by
    rw [hzero, norm_zero]
  linarith

end NavierStokesReview.SelectedRawVelocityNonzero
