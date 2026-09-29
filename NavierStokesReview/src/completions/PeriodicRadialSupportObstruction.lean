import NavierStokes.RadialAlias
import NavierStokes.ProblemStatement

/-!
# Periodic radial support obstruction

`barMoment` is defined for scalar fields with a fixed radial support
interval, whereas the selected Cartesian fields are periodised.  This file
records the exact elementary incompatibility that must be addressed by any
field-level transport theorem: a field that is periodic in its radial
coordinate and supported in a bounded radial interval is zero.

The theorem is deliberately generic.  It does not assert that the selected
field has radial support, and therefore does not by itself refute the
exported witness.
-/

noncomputable section

open Set

namespace NavierStokesReview.PeriodicRadialSupportObstruction

open NavierStokes

theorem periodic_radiallySupported_eq_zero
    {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F]
    {a b : ℝ} (_hab : a ≤ b) (g : ℝ × E → F)
    (hperiod : ∀ r : ℝ, ∀ Y : E, g (r + 1, Y) = g (r, Y))
    (hsupport : RadialAlias.RadiallySupported a b g) :
    ∀ r : ℝ, ∀ Y : E, g (r, Y) = 0 := by
  intro r Y
  by_contra hne
  have hshift : ∀ n : ℕ, g (r + (n : ℝ), Y) = g (r, Y) := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
        calc
          g (r + ((n + 1 : ℕ) : ℝ), Y) =
              g ((r + (n : ℝ)) + 1, Y) := by
                congr 2
                norm_num
                ring
          _ = g (r + (n : ℝ), Y) := hperiod (r + (n : ℝ)) Y
          _ = g (r, Y) := ih
  obtain ⟨n, hn⟩ := exists_nat_gt (b - r)
  have hne_shift : g (r + (n : ℝ), Y) ≠ 0 := by
    rw [hshift n]
    exact hne
  have hsupport_shift : (r + (n : ℝ), Y) ∈ Function.support g := hne_shift
  have hinterval := hsupport hsupport_shift
  exact (not_le_of_gt (by linarith : b < r + (n : ℝ))) hinterval.2

theorem unit_periodic_pullback_radiallySupported_eq_zero
    {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F]
    {times : Set ℝ} {t : ℝ} (ht : t ∈ times)
    (f : NavierStokes.ProblemStatement.SpaceTime → F)
    (hperiod : NavierStokes.ProblemStatement.UnitSpatialPeriodsOn times f)
    (φ : ℝ × E → NavierStokes.ProblemStatement.Space)
    (hφ : ∀ r : ℝ, ∀ Y : E,
      φ (r + 1, Y) = φ (r, Y) + NavierStokes.ProblemStatement.coordinateVector 0)
    {a b : ℝ} (hab : a ≤ b) (hsupport :
      RadialAlias.RadiallySupported a b (fun q => f (t, φ q))) :
    ∀ r : ℝ, ∀ Y : E, f (t, φ (r, Y)) = 0 := by
  apply periodic_radiallySupported_eq_zero (g := fun q => f (t, φ q))
    hab (fun r Y => ?_) hsupport
  have h := hperiod t ht (φ (r, Y)) 0
  rw [hφ r Y]
  exact h

end NavierStokesReview.PeriodicRadialSupportObstruction
