import NavierStokes.AxisPreservation
import NavierStokes.SmoothCutoffs

/-!
# Finite-prefix cutoff behaviour at the selected axis endpoint

The source cutoff API gives a common neighbourhood on which any fixed finite
set of scaled cutoffs is equal to one near `q = 0`.  The selected axis scale
theorem identifies `physicalQ h (t, 0)` with `1 - t`, so the same statement
pulls back to `t → 1⁻`.

This is a finite-prefix endpoint fact.  It does not evaluate the selected
infinite sum, its spatial curl, or any radial moment.
-/

noncomputable section

namespace NavierStokesReview.SelectedFiniteCutoffEndpoint

open NavierStokes
open NavierStokes.AxisPreservation
open NavierStokes.PhysicalWaveSum
open Filter
open scoped Topology

theorem selected_finite_cutoffs_eventually_one_on_axis
    {h : ℝ} (hh : 0 < h) (hh1 : h < 1 / 2)
    (a : ℕ → ℕ) (N : ℕ) :
    ∀ᶠ t in 𝓝[<] (1 : ℝ),
      ∀ j ∈ Finset.range N,
        SmoothCutoffs.scaledCutoff (a j : ℝ) (physicalQ h (t, 0)) = 1 := by
  have hq :
      Tendsto (fun t : ℝ => physicalQ h (t, 0))
        (𝓝[<] (1 : ℝ)) (𝓝 0) :=
    physicalQ_origin_tendsto hh hh1
  have hfinite :
      ∀ᶠ q in 𝓝 (0 : ℝ),
        ∀ j ∈ Finset.range N,
          SmoothCutoffs.scaledCutoff (a j : ℝ) q = 1 := by
    simpa using
      (SmoothCutoffs.finite_scaledCutoffs_eventually_one
        (Finset.range N) (fun j => (a j : ℝ)))
  exact hq.eventually hfinite

end NavierStokesReview.SelectedFiniteCutoffEndpoint
