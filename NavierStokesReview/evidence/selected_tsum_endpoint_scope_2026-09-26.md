# Selected `potentialSum` endpoint scope

**Date:** 2026-09-26  
**Finding class:** source-backed scope boundary  
**Status:** open calculation, not a contradiction

## Source facts

`NavierStokes/SolenoidalDiagonal.lean:37-42` defines

$$
\operatorname{potentialSum}(x)=\sum'_{j\in\mathbb N}
  \operatorname{scaledCutoff}(a_j,q(x))A_j(x),
$$

with `partialPotential` as the finite `Finset.range N` sum.

The local finite-tail theorem at `:46-67` requires both
`Tendsto a atTop atTop` and a strict positive scale `0 < q x`. Under those
hypotheses it gives a neighbourhood on which the infinite sum equals one
finite prefix. The all-jet version at `:140-147` inherits exactly the same
strict-positive-scale hypothesis.

The selected endpoint completion
`NavierStokesReview/src/completions/SelectedFiniteCutoffEndpoint.lean`
proves only that, for each fixed finite prefix, the selected axis cutoffs are
eventually equal to one as `t → 1⁻`. This uses
`AxisPreservation.physicalQ_origin_tendsto`, so its limit scale is zero rather
than strictly positive.

## Consequence for the audit

The source theorems therefore do not yet supply the missing passage

$$
\text{finite prefix at }q>0
\;\Longrightarrow\;
\text{selected infinite }\operatorname{potentialSum}
\text{ at the axis endpoint}\,.
$$

That is a genuine selected-path transport obligation. It is not evidence that
the infinite sum is undefined, discontinuous, or nonzero, because the CMI
candidate is evaluated on the pre-singular domain and the repository may use a
separate endpoint extension. The required next calculation is to identify the
actual endpoint representative and prove its compatibility with the Cartesian
curl, torus average, and `barMoment`.

## Verification boundary

No `Delta m != 0`, `False`, or selected-field PDE failure is claimed from this
scope fact alone.
