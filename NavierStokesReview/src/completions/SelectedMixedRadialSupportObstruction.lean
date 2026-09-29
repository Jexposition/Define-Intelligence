import completions.PeriodicRadialSupportObstruction
import completions.SelectedMixedRadialPeriodicity

/-!
# Selected mixed production: support/periodicity obstruction

The five-moment radial machinery uses bounded radial support, while the
selected mixed endpoint is built from a unit-periodic Cartesian velocity.  The
following theorem instantiates the repository's generic obstruction for the
actual selected mixed pullback.  It is conditional: the selected witness does
not currently export the required `RadiallySupported` premise.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedRadialSupportObstruction

open NavierStokes
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedProductionBarMoment
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedMixedRadialPeriodicity
open NavierStokesReview.SelectedPotentialProductionBarMomentSection

noncomputable def selectedMixedRadialPullback (a : ℕ → ℕ) :
    ℝ × PhysicalResidualBridge.Plane → ℝ :=
  fun q => selectedMixedProductionScalar a
    (pointToCyl (q.1, (q.2, (0, 0))))

theorem selected_mixed_radial_pullback_periodic
    (a : ℕ → ℕ) (r : ℝ) (p : PhysicalResidualBridge.Plane) :
    selectedMixedRadialPullback a (r + 1, p) =
      selectedMixedRadialPullback a (r, p) := by
  simpa [selectedMixedRadialPullback] using
    selected_mixed_barMoment_integrand_periodic a p r

theorem selected_mixed_bounded_radial_support_forces_zero
    (a : ℕ → ℕ) {α β : ℝ} (hab : α ≤ β)
    (hsupport : RadialAlias.RadiallySupported α β
      (selectedMixedRadialPullback a)) :
    ∀ r : ℝ, ∀ p : PhysicalResidualBridge.Plane,
      selectedMixedRadialPullback a (r, p) = 0 := by
  apply NavierStokesReview.PeriodicRadialSupportObstruction.periodic_radiallySupported_eq_zero
    hab (selectedMixedRadialPullback a)
  · exact selected_mixed_radial_pullback_periodic a
  · exact hsupport

end NavierStokesReview.SelectedMixedRadialSupportObstruction
