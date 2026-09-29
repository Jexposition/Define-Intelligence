# Selected graph image versus auxiliary torus domain

**Date:** 2026-09-25
**Classification:** selected source/interface evidence; not a nonzero-moment or `False` result
**Build:** `lake build NavierStokesReview`
**Result:** 3717 jobs completed successfully; the new completion contains no `sorry`, custom `axiom`, or `unsafe` declaration.

## Question

Does the physical graph used by the selected chart cover the complete auxiliary
domain integrated by `PressureStream.torusAverage` before `barMoment` is applied?

## Source anchors

- `NavierStokes/PressureStream.lean:66-71` defines `torusInner` and
  `torusAverage`; both auxiliary coordinates are integrated over the interval
  $[0,1]$.
- `NavierStokes/DefectIncrementBounds.lean:214-220` defines `barMoment` and
  expands it as the radial integral of `torusAverage`.
- `NavierStokes/PhysicalGraphBounds.lean:32-35` defines the auxiliary plane and
  the independent directions
  $$v_r=(1,1-\sqrt 2),\qquad v_t=(\sqrt 2-1,1).$$
- `NavierStokes/PhysicalGraphBounds.lean:81-82,112-115` constructs the radial
  profile and `nativeGraph` from a nonnegative radial power times $v_r$ plus a
  time-direction term.
- `NavierStokes/PhysicalResidualBridge.lean:645-649` defines `absoluteLift`.
- `NavierStokes/PhysicalResidualBridge.lean:651-654` relates the common graph to
  the physical chart only under the positive-radius hypothesis
  `0 < p.2 0`.

## Zero-sorry completion

`NavierStokesReview/src/completions/SelectedTorusLiftImageScope.lean:26-105`
defines a continuous linear functional $\rho$ with

$$\rho(v_r)=1,\qquad \rho(v_t)=0.$$

For a physical point with `0 ≤ p.2 0`, the completion proves

$$\rho\bigl((\operatorname{absoluteLift}(h,p)).2.2\bigr)\ge 0.$$

It also defines the auxiliary point

$$Y_0=(0,1/2),$$

proves $Y_0\in[0,1]^2$, and proves $\rho(Y_0)<0$. Therefore, for the stated
nonnegative-radius chart domain,

$$Y_0\notin\operatorname{range}
  \bigl(p\mapsto(\operatorname{absoluteLift}(h,p)).2.2\bigr).$$

The same conclusion is proved for the production sampling map
`PhysicalMeanJetBounds.physicalPoint` at lines 84-105. Its auxiliary
coordinate is a nonnegative radial-power multiple of $v_r$ plus a
time-direction term, so the explicitly defined
`unreachablePhysicalPoint` is not in its range.

## Consequence

The selected production field samples its atlas through
`ActualCandidateConstruction.meanField`
(`NavierStokes/ActualCandidateConstruction.lean:358-361`) and
`PhysicalMeanJetBounds.physicalPoint`, whereas the raw
`ActualMeanPhysicalData.Scalar` family is a function on the full
`PressureStream.Lift` domain (`NavierStokes/ActualMeanPhysicalData.lean:24-26`).
The production sampling map therefore does not by itself identify every raw
scalar value entering `torusAverage`. A scalar profile defined only through the
selected graph cannot be substituted into the full auxiliary average without an
additional extension or invariance theorem.

This is a concrete `CALC-22` transport gate. It is not yet a contradiction:
the repository could still supply an independent global scalar extension, or
prove that the selected integrand is invariant in the missed auxiliary region.
Neither fact is supplied by this completion. The selected weighted moment and
the proposed $\Delta m\ne0$ calculation therefore remain open.
