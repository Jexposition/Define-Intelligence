# Selected mixed production `barMoment` transport

## Scope

This record covers the selected mixed endpoint after the first-component
decomposition. It tests whether the actual mixed field can be placed in the
scalar-family domain consumed by `DefectIncrementBounds.barMoment`.

## Source and completion

| Item | Location | Result |
|---|---|---|
| Mixed endpoint component | `NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean:31-46` | The first component of `MixedPeriodicAssembly.periodicVelocity` on `ActualMeanStageData.radialSection` is split into the potential branch plus the periodised, cut direct branch. |
| Mixed scalar pullback | `NavierStokesReview/src/completions/SelectedMixedProductionBarMoment.lean:34-40` | Defines `selectedMixedProductionPointScalar` on `DefectIncrementBounds.Point PhysicalResidualBridge.Plane`. |
| `barMoment` application | `.../SelectedMixedProductionBarMoment.lean:43-49` | Zero-sorry exact reduction to `∫ r, r ^ k * PressureStream.torusAverage ...`. |
| Positive-radius physical pullback | `.../SelectedMixedProductionBarMoment.lean:52-59` | Zero-sorry identity back to the mixed radial section when `0 < p.2.1`. |
| Verification | Focused Lean invocation under Lean 4.34.0-rc2 | Exit code 0; no `sorry` or `axiom` was added. |

## Mathematical status

The completion proves that the selected mixed first component can be given a
well-typed radial moment observable:

$$
\operatorname{barMoment}_k(\widetilde u) (n,p)
=
\int_{\mathbb R} r^k\,
\operatorname{torusAverage}(\widetilde u_n)(r,p)\,dr.
$$

On the positive-radius section, the pullback is the actual selected mixed
component. This closes the typing and coordinate step that was previously
missing for the mixed field. It does **not** prove that the observable equals
the paper's five moments, that the direct cutoff contribution vanishes, that
any moment is nonzero, or that the exported C/D theorem is contradictory.

## Remaining calculation

The next field-level target remains an explicit evaluation of the mixed
integral, including the periodised cutoff direct branch. A contradiction
requires an independently proved value or inequality for that integral and a
reachable theorem identifying it with the selected candidate's required
invariant.
