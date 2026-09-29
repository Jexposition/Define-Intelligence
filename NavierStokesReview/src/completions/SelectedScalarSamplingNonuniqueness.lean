import NavierStokes.PhysicalMeanJetBounds
import completions.SelectedTorusLiftImageScope

/-!
# Non-uniqueness of the raw scalar family from the production sampling map

`barMoment` consumes a scalar family on the full physical point type.  The
production field samples that family only through `physicalPoint`.  The
previous image theorem gives an explicit auxiliary point outside that image.
This file records the resulting non-injectivity at the plain scalar-family
level.  It does not assert that the selected family has a nonzero value at the
missed point, and it does not replace the missing regularity/overlap theorem.
-/

noncomputable section

namespace NavierStokesReview.SelectedScalarSamplingNonuniqueness

open NavierStokes
open NavierStokesReview.SelectedTorusLiftImageScope

abbrev ScalarFamily := ℕ → NavierStokes.PhysicalMeanJetBounds.Point → ℝ

noncomputable def offImageFamily : ScalarFamily :=
  fun _ z => if radialCoordinate z.2.2 < 0 then 1 else 0

theorem offImageFamily_sample_eq_zero (h : ℝ) (n : ℕ) (w : GraphSpaceTime) :
    offImageFamily n (NavierStokes.PhysicalMeanJetBounds.physicalPoint h w) = 0 := by
  have hn :=
    NavierStokesReview.SelectedTorusLiftImageScope.physicalPoint_auxiliary_radialCoordinate_nonnegative
      h w
  unfold offImageFamily
  split <;> rename_i hs
  · exact False.elim ((not_lt_of_ge hn) hs)
  · rfl

theorem offImageFamily_at_unreachable_eq_one (n : ℕ) :
    offImageFamily n
        NavierStokesReview.SelectedTorusLiftImageScope.unreachablePhysicalPoint = 1 := by
  have hn :=
    NavierStokesReview.SelectedTorusLiftImageScope.radialCoordinate_unreachableAuxiliary_negative
  unfold offImageFamily
  split <;> rename_i hs
  · rfl
  · exact False.elim (hs (by simpa only
      [NavierStokesReview.SelectedTorusLiftImageScope.unreachablePhysicalPoint] using hn))

theorem physicalPoint_sampling_not_injective :
    ∀ h : ℝ, ∃ f g : ScalarFamily,
      (∀ n w, f n (NavierStokes.PhysicalMeanJetBounds.physicalPoint h w) =
        g n (NavierStokes.PhysicalMeanJetBounds.physicalPoint h w)) ∧
      ∃ n z, f n z ≠ g n z := by
  intro h
  refine ⟨(fun _ _ => 0), offImageFamily, ?_, 0,
    NavierStokesReview.SelectedTorusLiftImageScope.unreachablePhysicalPoint, ?_⟩
  · intro n w
    symm
    exact offImageFamily_sample_eq_zero h n w
  · rw [offImageFamily_at_unreachable_eq_one]
    norm_num

end NavierStokesReview.SelectedScalarSamplingNonuniqueness
