# Selected-field to `barMoment` interface

## Result

The review completion `src/completions/SelectedBarMomentInterface.lean` compiles
without `sorry`, custom axioms, or `unsafe` declarations. It proves the exact
interface identity needed to compare a selected production field with the
radial moment operator.

For a point-to-spacetime map

$$
\phi : \operatorname{Point}(P) \to \operatorname{SpaceTime}
$$

and the scalar pullback

$$
g_j(q) = \bigl(u_j(\phi(q))\bigr)_1,
$$

the completion proves

$$
\operatorname{barMoment}_k(g_j)(n,p)
= \int r^k\,\operatorname{torusAverage}
  \bigl(q\mapsto (u_j(\phi(q)))_1\bigr)(r,p)\,dr.
$$

The proof is a direct expansion of `DefectIncrementBounds.barMoment_apply`.

## Source facts

| Item | Source | Consequence |
|---|---|---|
| Production selected field | `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | Exports a Cartesian `VelocityField` on `SpaceTime`. |
| Selected potential stages | `NavierStokes/ActualCandidateAssembly.lean:1165-1168` | Supplies the stage family used by the production sums. |
| Moment operator | `NavierStokes/DefectIncrementBounds.lean:214-220` | Consumes `ScalarField (Point P)`, not a Cartesian velocity field. |
| Auxiliary average | `NavierStokes/PressureStream.lean:63-72` | Averages the two `Plane` coordinates while retaining the radial and slow parameters. |
| Review completion | `NavierStokesReview/src/completions/SelectedBarMomentInterface.lean:32-42,54-66` | Makes the required pullback and scalar equality explicit. |

## Audit significance

The endpoint `selected_witness` does not export a named point-to-spacetime map,
a scalar radial profile, or a theorem identifying the selected infinite sum with
such a profile after torus averaging. Therefore the published five-moment
construction is not yet transported to the concrete selected field at the
formal interface.

This is a concrete representation and transport defect supporting the verdict
`NOT ESTABLISHED AS A CMI SOLUTION`. It is not, by itself, a proof of a nonzero
remainder and does not justify asserting `False`.

## Next calculation gate

The remaining source-first calculation is to construct or refute the required
map from the selected `polarCoordinates` chart to `PressureStream.Lift P`, then
prove the axis, support, torus-average, and infinite-sum transport identities.
Only an exact selected value or inequality, such as

$$
\Delta m \ne 0,
$$

can promote this interface defect to a kernel contradiction.
