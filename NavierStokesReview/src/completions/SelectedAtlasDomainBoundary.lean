import NavierStokes.ActualMeanPhysicalData

noncomputable section

namespace NavierStokesReview
namespace SelectedAtlasDomainBoundary

open NavierStokes
open NavierStokes.ActualMeanPhysicalData
open NavierStokes.PressureStream

/-!
The production atlas evaluates a native scalar only on valid chart samples.
`Atlas.Valid` requires a strictly positive first slow coordinate.  This file
records the resulting zero-extension fact explicitly, without asserting that
the selected native scalar is nonzero on the omitted region.
-/

theorem atlas_physical_zero_of_nonpositive_slow_coordinate
    {h : ℝ} {N Δ : ℕ} (A : Atlas h N Δ)
    {U : Set PressureStream.Plane} {degree : ℝ} (f : Scalar)
    {z : ActualMeanPhysicalData.Point} (hz : z.2.1.1 ≤ 0) :
    A.physical U degree f z = 0 := by
  classical
  unfold Atlas.physical
  by_cases hvalid : ∃ n, A.Valid U z n
  · rcases hvalid with ⟨n, hn⟩
    exact False.elim ((not_lt_of_ge hz) hn.2.1)
  · simp [hvalid]

end SelectedAtlasDomainBoundary
end NavierStokesReview
