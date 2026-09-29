import completions.SelectedMixedRadialSupportObstruction

/-!
# Selected periodic support-transport gate

This is a hardened conditional contradiction gate for the *actual* selected
mixed radial pullback.  It does not use an external debt variable or a toy
profile.  The two premises are deliberately separated:

* `hsupport` is the missing transport theorem from the selected field's
  Cartesian/whole-space support to `RadialAlias.RadiallySupported`;
* `hnonzero` is the missing field-level non-vanishing witness for the same
  pullback.

The selected pullback is already proved period-one in
`SelectedMixedRadialSupportObstruction`.  Periodicity plus bounded radial
support forces it to vanish identically.  Therefore the two premises cannot
coexist.  This file does **not** assert either premise and does not derive
`False` for the current selected endpoint.

The purpose is anti-blindside control: a later source trace must either
construct the exact support/field-identification bridge, or explicitly record
that this contradiction gate remains open.
-/

noncomputable section

namespace NavierStokesReview.SelectedPeriodicSupportTransportGate

open NavierStokes
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedRadialSupportObstruction

theorem selected_periodic_support_transport_gate
    (a : ℕ → ℕ) {α β : ℝ} (hab : α ≤ β)
    (hsupport : RadialAlias.RadiallySupported α β
      (selectedMixedRadialPullback a))
    (hnonzero : ∃ r : ℝ, ∃ p : PhysicalResidualBridge.Plane,
      selectedMixedRadialPullback a (r, p) ≠ 0) : False := by
  have hzero : ∀ r : ℝ, ∀ p : PhysicalResidualBridge.Plane,
      selectedMixedRadialPullback a (r, p) = 0 :=
    selected_mixed_bounded_radial_support_forces_zero a hab hsupport
  obtain ⟨r, p, hne⟩ := hnonzero
  exact hne (hzero r p)

/-! This second theorem binds the support/nonzero assumptions to the schedule
    extracted from the actual exported `selected_witness`.  The assumptions
    remain deliberately explicit and stronger than the current endpoint
    exposes; this theorem does not manufacture them. -/
theorem selected_witness_schedule_support_gate
    {α β : ℝ} (hab : α ≤ β)
    (hsupport : ∀ a : ℕ → ℕ,
      RadialAlias.RadiallySupported α β (selectedMixedRadialPullback a))
    (hnonzero : ∀ a : ℕ → ℕ,
      ∃ r : ℝ, ∃ p : PhysicalResidualBridge.Plane,
        selectedMixedRadialPullback a (r, p) ≠ 0) : False := by
  obtain ⟨a, _, _, _, _, _, _, _⟩ :=
    NavierStokes.ActualCandidateAssembly.selected_witness
  exact selected_periodic_support_transport_gate a hab (hsupport a) (hnonzero a)

end NavierStokesReview.SelectedPeriodicSupportTransportGate
