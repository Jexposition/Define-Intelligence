# Periodic global-integral semantics for the selected radial observable

**Date:** 2026-09-26
**Completion:** `NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean`

## Zero-sorry result

The completion compiles with Lean 4.34.0-rc2 and no `sorry`, `axiom`, or
`unsafe` declaration. It proves:

1. A real-valued function with period one that is strictly positive on
   `Ioo 0 1` cannot be globally Bochner-integrable. Its interval integral over
   repeated periods tends to `atTop`, while global integrability gives a finite
   improper-integral limit.
2. By `MeasureTheory.integral_undef`, the global Bochner integral of that
   function is therefore definitionally evaluated as zero.
3. The same conditional statement is instantiated for the selected mixed
   radial pullback and `barMoment 0`.

The relevant selected theorem is
`selected_mixed_barMoment_zero_of_positive_pullback`.

## Scope boundary

The selected source does **not** prove the positivity premise for the mixed
pullback, and the theorem does not evaluate the weighted cases `barMoment k`
for `k > 0`. It therefore supplies a precise integrability branch, not an
unconditional selected-field mismatch and not `False`.

The result also confirms why the radial observable needs an explicit support
or integrability interpretation. The source definition integrates over all
real radial values; interval support lemmas do not automatically apply to the
periodised mixed endpoint.

## Source anchors for the support boundary

The support transition is explicit in the source. `SpatialLocalization.cutPotential`
is the compactly supported field, with `cutPotential_supported` at
`NavierStokes/SpatialLocalization.lean:164-180`. The selected mixed field then
uses `MixedPeriodicAssembly.periodicVelocity`, which combines the periodised
potential branch with the periodised direct branch at
`NavierStokes/MixedPeriodicAssembly.lean:36-38`. Its unit-periodicity theorem
is at `:59-65`.

The radial observable is defined independently as a global real integral:
`DefectIncrementBounds.barMoment` and `barMoment_apply` are at
`NavierStokes/DefectIncrementBounds.lean:214-220`. Thus the source proves

$$
\text{compact support before periodisation}
\not\Rightarrow
\text{bounded radial support after periodisation}.
$$

The review-side obstruction theorem is therefore correctly conditional:
`selected_mixed_bounded_radial_support_forces_zero` may be applied only after a
selected-path theorem supplies `RadiallySupported` for the periodised pullback.
No such theorem, and no selected nonzero value, is currently exported.
