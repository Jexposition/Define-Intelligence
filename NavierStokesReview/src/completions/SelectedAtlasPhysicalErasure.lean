import NavierStokes.ActualCandidateConstruction

/-!
# Valid-band erasure in the selected physical map

`Atlas.physical` evaluates a scalar family only at a valid chart sample.  This
completion records the exact congruence principle used by that definition.
It is deliberately weaker than a moment contradiction: `barMoment` consumes
the native scalar family, so a separate theorem is still required to transport
this congruence through the full torus average.
-/

noncomputable section

namespace NavierStokesReview.SelectedAtlasPhysicalErasure

open NavierStokes
open NavierStokes.ActualMeanPhysicalData

theorem atlas_physical_congr_of_valid
    {h : ℝ} {N Δ : ℕ} (A : Atlas h N Δ)
    {U : Set PressureStream.Plane} {degree : ℝ}
    {f g : Scalar}
    (hfg : ∀ n z, A.Valid U z n → f n (A.chart n z) = g n (A.chart n z))
    (z : Point) :
    A.physical U degree f z = A.physical U degree g z := by
  classical
  by_cases hz : ∃ n, A.Valid U z n
  · unfold Atlas.physical
    simp only [dite_eq_left hz]
    rw [hfg (Classical.choose hz) z
      (Classical.choose_spec hz)]
  · unfold Atlas.physical
    simp only [dite_eq_right hz]

end NavierStokesReview.SelectedAtlasPhysicalErasure
