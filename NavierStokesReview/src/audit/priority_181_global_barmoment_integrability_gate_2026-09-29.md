# Priority 181: global `barMoment` integrability gate

**Date:** 2026-09-29
**Status:** source-checked; semantic gate identified; no contradiction proved

## Finding

The selected mixed radial pullback is proved periodic with period one by
`selected_mixed_radial_pullback_periodic`. The observable used by
`DefectIncrementBounds.barMoment`, however, is a global Bochner integral over
the unbounded real radial coordinate:

\[
  \operatorname{barMoment}(k,f)(n,p)
  =\int_{\mathbb R} r^k\,\operatorname{torusAverage}(f_n)(r,p)\,dr.
\]

This creates a necessary semantic gate. A nonzero periodic scalar cannot be
globally integrable on \(\mathbb R\). The review completion
`PeriodicGlobalIntegral.lean` therefore proves conditionally that strict
positivity on one unit interval implies non-integrability and that
Mathlib's `integral_undef` then returns zero for the global Bochner integral.

The selected-field instance is conditional. The source does not currently
prove that the selected radial pullback is positive on a fundamental interval,
globally integrable, or radially supported. Likewise, the support obstruction
only proves that a periodic radially supported pullback must be identically
zero after its `RadiallySupported` premise is supplied.

## Exact logical consequences

The inspected record supports the following implications:

\[
\begin{aligned}
&\text{periodic} + \text{bounded radial support}
  \Rightarrow \text{radial pullback}=0,\\
&\text{periodic} + \text{strict positivity on }(0,1)
  \Rightarrow \neg\operatorname{Integrable}(f),\\
&\neg\operatorname{Integrable}(f)
  \Rightarrow \int_{\mathbb R} f=0
  \quad\text{by `integral_undef`}.
\end{aligned}
\]

None of these implications proves that the selected field has a nonzero
moment defect. They show instead that a meaningful selected `barMoment`
identity must establish the correct global integration semantics first. A
finite-prefix compact-support fact cannot be silently transferred through
periodisation to global radial support or integrability.

## Audit classification

* selected radial periodicity: **established conditionally on the inspected
  selected construction**;
* global radial support of the selected periodised field: **not established**;
* global integrability of the selected radial pullback: **not established**;
* selected `barMoment` value: **not established**;
* paper five-observable transport: **NOT ESTABLISHED (CTR-005)**;
* selected nonzero defect, impossibility, literal CMI failure, or `False`:
  **not proved**.

This is a semantic safeguard against treating a global integral with
`integral_undef` as a physical moment calculation. It does not by itself
invalidate the selected endpoint.

## Source anchors

* `NavierStokesReview/src/completions/SelectedMixedRadialSupportObstruction.lean:31--45`
* `NavierStokesReview/src/completions/SelectedMixedRadialPeriodicity.lean:31--58`
* `NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean:31--70`
* `NavierStokes/DefectIncrementBounds.lean:214--220`
* `NavierStokes/MixedPeriodicAssembly.lean:36--65`

