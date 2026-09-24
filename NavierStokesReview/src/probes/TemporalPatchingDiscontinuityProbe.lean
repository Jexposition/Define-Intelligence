import NavierStokes.GermCandidateAssembly
import NavierStokes.LocalPotentialRebundle
import NavierStokes.TimeLocalization

/-!
# Temporal patching boundary probe

This probe separates two mechanisms that are easy to conflate:

* `initializedSeries` selects an indexed base/initial/stage family; it is not
  a piecewise-in-time definition.
* `TimeLocalization` multiplies a spacetime field by a globally smooth switch.

The first theorem records the exact interface obligation left by the indexed
constructor.  The remaining theorems record the smoothness and late-jet facts
that are actually present in the source.  No discontinuity of the selected
field is inferred from the constructor alone.
-/

noncomputable section

namespace NavierStokesReview.TemporalPatchingDiscontinuityProbe

open NavierStokes ProblemStatement
open scoped Topology ContDiff

theorem initialized_series_boundary_is_unconstrained
    (base initial : ProblemStatement.VelocityField)
    (stages : ℕ → ProblemStatement.VelocityField)
    (h : (fun w => base w + initial w) ≠ stages 0) :
    GermCandidateAssembly.initializedSeries base initial stages 0 ≠
      GermCandidateAssembly.initializedSeries base initial stages 1 := by
  simpa only [GermCandidateAssembly.initializedSeries] using h

theorem initialized_series_admits_concrete_boundary_mismatch (w : SpaceTime) :
    let base : VelocityField := fun _ => 0
    let initial : VelocityField := fun _ => 0
    let stages : ℕ → VelocityField := fun j =>
      if j = 0 then fun _ => coordinateVector 0 else fun _ => 0
    GermCandidateAssembly.initializedSeries base initial stages 0 w ≠
      GermCandidateAssembly.initializedSeries base initial stages 1 w := by
  dsimp only
  intro h
  have hcoord : coordinateVector 0 ≠ (0 : Space) := by
    intro hz
    have hzero := congrArg (fun v : Space => v 0) hz
    simp [coordinateVector] at hzero
  apply hcoord
  simpa [GermCandidateAssembly.initializedSeries] using h.symm

theorem uncut_prefix_boundary_is_additive
    (stages : ℕ → ProblemStatement.VelocityField) (N : ℕ) :
    DiagonalJetBounds.uncutPrefix stages (N + 1) =
      DiagonalJetBounds.uncutPrefix stages N + stages N := by
  exact ActualCandidateConstruction.uncutPrefix_succ stages N

theorem activated_velocity_has_global_presingular_smoothness
    (u : ProblemStatement.VelocityField)
    (hu : ContDiffOn ℝ ∞ u ProblemStatement.preSingularDomain) :
    ContDiffOn ℝ ∞ (TimeLocalization.activatedVelocity u)
      ProblemStatement.preSingularDomain := by
  exact TimeLocalization.activatedVelocity_smooth u hu

theorem activated_late_temporal_derivative_agreement
    (u : ProblemStatement.VelocityField) {t : ℝ}
    (ht : 3 / 4 < t) (x : ProblemStatement.Space) :
    temporalDerivative
        (TimeLocalization.activatedVelocity u) t x =
      temporalDerivative u t x := by
  exact TimeLocalization.activated_temporalDerivative_eq_late u ht x

end NavierStokesReview.TemporalPatchingDiscontinuityProbe
