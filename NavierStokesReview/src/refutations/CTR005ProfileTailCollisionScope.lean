import NavierStokes.ActualCandidateAssembly
import NavierStokes.DefectIncrementBounds
import NavierStokes.FiveRowRank
import completions.MeanRankUpdateAudit
import completions.SelectedCycleMomentTransport

/-!
# CTR-005 profile-tail collision scope

This module tests the proposed route from the five-row correction system to a
kernel contradiction.  It records the strongest facts that follow from the
actual definitions and keeps the missing selected-field bridge explicit.

`FiveRows` constrains correction profiles `dv` and `ga`; it does not assert
that a total Cartesian velocity has zero mass, zero energy, or zero global
moment.  The selected cycle does carry a genuine local two-moment invariant,
but the exported `Witness` does not identify that radial profile with its
assembled Cartesian sums.  Thus the route supplies a conditional obstruction,
not yet a selected-path `False` theorem.
-/

noncomputable section

namespace NavierStokesReview.CTR005ProfileTailCollisionScope

open Set MeasureTheory NavierStokes
open NavierStokes.DefectIncrementBounds
open NavierStokes.FiveRowRank
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction

theorem five_rows_are_increment_scoped
    {V G : ℝ → ℝ} {d : FiveRowRank.Debt} {dv ga : ℝ → ℝ}
    (hrows : FiveRowRank.FiveRows V G d dv ga) :
    (∫ R, R ^ (2 : ℕ) * dv R) = 0 ∧
      (∫ R, R * ga R) = 0 := by
  exact ⟨hrows.1, hrows.2.1⟩

theorem nonzero_runtime_debt_compatible_with_zero_correction_rows
    (lam C a b : ℝ) (hlam : 0 < lam) (hC : C ≠ 0)
    (ha : 0 < a) (hab : a < b) :
    ∃ d : FiveRowRank.Debt, d ≠ 0 ∧
      ∃ dv ga : ℝ → ℝ,
        FiveRowRank.FiveRows (FiveRowRank.background lam C) (fun _ => 0)
          d dv ga := by
  obtain ⟨dv, ga, hrows⟩ :=
    MeanRankUpdateAudit.nonzero_debt_is_compatible_with_zero_rows
      lam C a b hlam hC ha hab
  refine ⟨![1, 0, 0], ?_, dv, ga, hrows⟩
  intro h
  have h0 := congrFun h (0 : Fin 3)
  norm_num at h0

theorem selected_cycle_zero_rows_are_not_total_field_moments (j : ℕ) :
    GaugeMassPreservation.ZeroMassesOn
      ActualInitialization.geometry.region.carrier
      (ActualCandidateConstruction.selectedCycle j).state :=
  SelectedCycleMomentTransport.selected_cycle_state_zero_masses j

theorem barMoment_is_radial_profile_quantity
    {P : Type} [NormedAddCommGroup P] [NormedSpace ℝ P]
    {f : DefectIncrementBounds.ScalarField (DefectIncrementBounds.Point P)}
    (k n : ℕ) (p : P) :
      DefectIncrementBounds.barMoment k f n p =
        ∫ r, r ^ k * PressureStream.torusAverage (f n) (r, p) :=
  DefectIncrementBounds.barMoment_apply k f n p

end NavierStokesReview.CTR005ProfileTailCollisionScope
