import NavierStokes.R3.PressureRecovery

/-!
# Absolute-pressure premise probe

`PressureRecovery.Hypotheses` is a comparison interface.  This probe records
the exact logical limitation that matters for the review: it accepts two
identical zero velocity fields and any pressure field smooth on the comparison
slab, with the same pressure supplied on both sides.  All residual and
divergence obligations then close by reflexivity or zero calculation.

This does not refute the selected endpoint.  It does refute the stronger
review wording that the pressure-recovery chain, by itself, verifies an
absolute pressure Poisson equation for the selected pressure.
-/

noncomputable section

open Set
open scoped ContDiff
open NavierStokes
open NavierStokesR3
open NavierStokesR3.ProblemStatement
open NavierStokesR3.PressureRecovery

namespace NavierStokesReview.PressureRecoveryAbsolutePremiseProbe

theorem comparison_hypotheses_accept_identical_zero_velocity
    {T : ℝ} (hT : 0 < T) {p : PressureField}
    (hp : ContDiffOn ℝ ∞ p (Comparison.slab 0 T)) :
    PressureRecovery.Hypotheses T (fun _ => 0) (fun _ => 0) p p := by
  refine {
    positive := hT
    smooth_u := contDiff_const.contDiffOn
    smooth_v := contDiff_const.contDiffOn
    smooth_p := hp
    smooth_q := hp
    div_u := ?_
    div_v := ?_
    equation := ?_
    energy_u := ?_
    energy_v := ?_
  }
  · intro t ht x
    simp [NavierStokes.ProblemStatement.spatialDivergence,
      NavierStokes.ProblemStatement.spatialDerivative]
  · intro t ht x
    simp [NavierStokes.ProblemStatement.spatialDivergence,
      NavierStokes.ProblemStatement.spatialDerivative]
  · intro t ht x
    simp [NavierStokes.ProblemStatement.navierStokesResidual,
      NavierStokes.ProblemStatement.temporalDerivative,
      NavierStokes.ProblemStatement.advection,
      NavierStokes.ProblemStatement.spatialLaplacian,
      NavierStokes.ProblemStatement.spatialDerivative,
      NavierStokes.ProblemStatement.pressureGradient]
  · refine ⟨0, le_rfl, ?_⟩
    intro t ht
    constructor
    · simp [SquareIntegrableAtTime]
    · simp [kineticEnergy]
  · refine ⟨0, le_rfl, ?_⟩
    intro t ht
    constructor
    · simp [SquareIntegrableAtTime]
    · simp [kineticEnergy]

end NavierStokesReview.PressureRecoveryAbsolutePremiseProbe
