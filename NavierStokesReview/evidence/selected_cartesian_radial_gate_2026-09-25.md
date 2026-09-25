# Selected Cartesian-to-radial gate

The review completion
`NavierStokesReview/src/completions/SelectedCartesianRadialGate.lean` compiles
without `sorry`, custom axioms, or `unsafe` declarations.

It proves the exact positive-radius recovery identity

$$
M_f(w)=u_f(w)_1\,\frac{\rho(w)}{x_1},
$$

where `M_f` is the scalar atlas field, `u_f` is
`meanAngularField`, `rho` is `PhysicalClassBounds.cartesianRadius`, and
`x_1` is the first coordinate of `PhysicalGraphBounds.radialProjection w`.
The theorem assumes `x_1 ≠ 0`; it derives `rho ≠ 0` and therefore does not
claim a value on the axis.

This is a concrete coordinate gate, not the requested radial moment theorem.
It does not identify the selected Cartesian curl or cut-stage sum with a
`ScalarField (Point P)`, does not evaluate `barMoment_apply`, and does not
establish `Delta m ≠ 0` or `False`. The next calculation must carry this
recovered coefficient through the cutoff, curl, torus average, and both radial
boundary terms.

## Source anchors

| Item | Source |
|---|---|
| Angular component formula | `NavierStokesReview/src/completions/SelectedAngularComponentFormula.lean` |
| Angular frame | `NavierStokes/PhysicalMeanJetBounds.lean:518-530` |
| Cartesian radius | `NavierStokes/PhysicalClassBounds.lean:606-610` |
| Selected direct stages | `NavierStokes/ActualCandidateAssembly.lean:553-556`; `NavierStokes/ActualCandidateConstruction.lean:394-401` |
| Curl assembly | `NavierStokes/SolenoidalDiagonal.lean:31-38,182-188` |
| Scalar moment operator | `NavierStokes/DefectIncrementBounds.lean:214-220` |

Build result: `lake build NavierStokesReview` completed successfully with
3698 jobs under Lean `v4.34.0-rc2`.
