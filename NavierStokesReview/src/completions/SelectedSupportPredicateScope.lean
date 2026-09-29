import NavierStokes.AnnularEndpoint
import NavierStokes.SpatialLocalization

/-!
# Scope of the shrinking-support predicate

`ShrinkingSupport` controls the distance to the symmetry axis.  The cutoff
plateau also imposes an axial-coordinate bound.  This file gives a concrete
zero-sorry interface countermodel showing that the former does not imply the
latter.  The model is deliberately not presented as the selected smooth
velocity field; it isolates the missing logical implication at the support
interface.
-/

noncomputable section

namespace NavierStokesReview.SelectedSupportPredicateScope

open NavierStokes ProblemStatement

noncomputable def axialWitness : Space :=
  coordinateVector (2 : Fin 3)

noncomputable def axialPoint : SpaceTime := (0, axialWitness)

noncomputable def axialSpike (w : SpaceTime) : ℝ :=
  if w = axialPoint then 1 else 0

theorem axialWitness_radius_zero : AnnularEndpoint.radius axialPoint = 0 := by
  simp [axialPoint, axialWitness, AnnularEndpoint.radius,
    PhysicalGraphBounds.radialProjection_apply, PolarCharts.radius,
    coordinateVector]

theorem axialSpike_shrinkingSupport {h C : ℝ} (hC : 0 ≤ C) :
    AnnularEndpoint.ShrinkingSupport h C axialSpike := by
  intro w ht hw
  have hw0 : w = axialPoint := by
    by_contra hne
    simp [axialSpike, hne] at hw
  subst w
  rw [axialWitness_radius_zero]
  exact mul_nonneg hC (Real.sqrt_nonneg _)

theorem axialWitness_not_plateau :
    axialWitness ∉ SpatialLocalization.plateau := by
  simp [axialWitness, SpatialLocalization.plateau,
    SpatialLocalization.radialSquare, coordinateVector]
  norm_num

end NavierStokesReview.SelectedSupportPredicateScope
