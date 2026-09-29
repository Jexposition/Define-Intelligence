# Selected stream-to-curl chart transport

Status: compiled selected-path transport result; no contradiction.

## Source result

`NavierStokesReview/src/completions/SelectedStreamCurlChartTransport.lean`
proves, for the selected budget and threshold, that each actual stream stage
has the chart identity

$$
\nabla\times \operatorname{streamMeanStages}_j
=\operatorname{chartStreamParts}_j
$$

on the exact `ActualPhysicalPrefixFields.cartesianChartDomain`, under the
source hypothesis that the chart band is at least the first residual band.
The theorem is a direct specialization of
`ActualCandidateAssembly.stream_on_chart`.

## Interpretation

This closes one source-to-field step that was previously only listed in the
plan: the scalar mean stream is not merely an unused upstream object; its curl
is transported into the selected chart potential branch. It still does not
produce the moment identity needed for a contradiction. The remaining map is

$$
\operatorname{chartStreamParts}_j
\longrightarrow
\operatorname{torusAverage}(\text{scalar family})
\longrightarrow
\operatorname{barMoment}.
$$

The current theorem is local to the production chart and vector-valued. It
does not establish equality between the selected curl field and the scalar
`Point → ℝ` input used by `barMoment_apply`, nor does it evaluate an axis or
outer-support remainder.

## Verification

Standalone command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedStreamCurlChartTransport.lean
```

Result: exit code `0`; no `sorry`, custom `axiom`, or `unsafe` declaration.
