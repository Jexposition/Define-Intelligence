import completions.SelectedMixedRadialSupportObstruction
import completions.SelectedMixedProductionTorusAverage

/-!
# Global Bochner-integral semantics for a periodic radial pullback

The source `barMoment` uses the global Bochner integral over the real radial
coordinate.  This completion records one exact consequence of that choice:
a unit-periodic scalar that is strictly positive on one fundamental interval
cannot be globally integrable, so Mathlib's `integral_undef` evaluates its
global Bochner integral to zero.  The selected-field theorem below is
conditional on the displayed positivity premise; it does not assert that the
selected pullback has that sign.
-/

noncomputable section

open MeasureTheory
open Set
open Filter

namespace NavierStokesReview.PeriodicGlobalIntegral

open NavierStokesReview.SelectedMixedProductionBarMoment
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedMixedProductionTorusAverage
open NavierStokesReview.SelectedMixedRadialPeriodicity
open NavierStokesReview.SelectedMixedRadialSupportObstruction
open NavierStokesReview.SelectedPotentialProductionBarMomentSection

theorem not_integrable_of_periodic_positive_on_fundamental_interval
    {f : ℝ → ℝ}
    (hperiodic : Function.Periodic f 1)
    (hpositive : ∀ x : ℝ, x ∈ Ioo (0 : ℝ) 1 → 0 < f x) :
    ¬ Integrable f := by
  intro hf
  have hperiod_integral : 0 < ∫ x in (0 : ℝ)..1, f x := by
    apply intervalIntegral.intervalIntegral_pos_of_pos_on hf.intervalIntegrable
    · intro x hx
      exact hpositive x hx
    · norm_num
  have hdiv := hperiodic.tendsto_atTop_intervalIntegral_of_pos
    hperiod_integral (by norm_num : (0 : ℝ) < 1)
  have hconv := intervalIntegral_tendsto_integral_Ioi (0 : ℝ)
    hf.integrableOn (tendsto_id : Tendsto (fun x : ℝ => x) atTop atTop)
  exact (not_tendsto_nhds_of_tendsto_atTop hdiv _ hconv)

theorem periodic_global_integral_zero_of_positive_on_fundamental_interval
    {f : ℝ → ℝ}
    (hperiodic : Function.Periodic f 1)
    (hpositive : ∀ x : ℝ, x ∈ Ioo (0 : ℝ) 1 → 0 < f x) :
    ∫ x, f x = 0 := by
  exact MeasureTheory.integral_undef
    (not_integrable_of_periodic_positive_on_fundamental_interval
      hperiodic hpositive)

theorem selected_mixed_barMoment_zero_of_positive_pullback
    (a : ℕ → ℕ) (n : ℕ) (p : NavierStokes.PhysicalResidualBridge.Plane)
    (hpositive : ∀ r : ℝ, r ∈ Ioo (0 : ℝ) 1 →
      0 < selectedMixedRadialPullback a (r, p)) :
    NavierStokes.DefectIncrementBounds.barMoment 0
        (selectedMixedProductionPointScalar a) n p = 0 := by
  rw [selected_mixed_barMoment_radial_reduction]
  have hnonintegrable : ¬ Integrable
      (fun r : ℝ => selectedMixedRadialPullback a (r, p)) :=
    not_integrable_of_periodic_positive_on_fundamental_interval
      (fun r => selected_mixed_radial_pullback_periodic a r p) hpositive
  have hintegrand :
      (fun r : ℝ => r ^ 0 * selectedMixedProductionScalar a
        (pointToCyl (r, (p, (0, 0))))) =
        (fun r : ℝ => selectedMixedRadialPullback a (r, p)) := by
    funext r
    simp [selectedMixedRadialPullback]
  rw [hintegrand, MeasureTheory.integral_undef hnonintegrable]

end NavierStokesReview.PeriodicGlobalIntegral
