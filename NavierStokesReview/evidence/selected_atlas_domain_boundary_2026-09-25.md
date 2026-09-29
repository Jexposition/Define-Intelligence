# Selected atlas domain boundary

**Date:** 2026-09-25  
**Tree:** current review branch  
**Claim class:** selected interface result

## Result

`NavierStokesReview/src/completions/SelectedAtlasDomainBoundary.lean` proves,
without `sorry`, custom axioms, or `unsafe`, that

$$z.2.1.1 \le 0 \;\Longrightarrow\;
\operatorname{Atlas.physical}(A,U,d,f,z)=0.$$

The proof unfolds `Atlas.physical`. A nonzero branch would require a witness
`n` satisfying `Atlas.Valid U z n`; that predicate contains the strict
condition `0 < z.2.1.1`, contradicting the hypothesis.

## Source anchors

| Definition | File and line | Relevance |
|---|---|---|
| `Atlas.Valid` | `NavierStokes/ActualMeanPhysicalData.lean:96` | Requires `0 < z.2.1.1`. |
| `Atlas.physical` | `NavierStokes/ActualMeanPhysicalData.lean:125` | Returns the valid-chart sample, otherwise `0`. |
| `physicalPoint` | `NavierStokes/PhysicalMeanJetBounds.lean:24` | Supplies points to the production atlas. |
| `torusAverage` | `NavierStokes/PressureStream.lean:70` | Averages the native scalar-family domain. |
| `barMoment` | `NavierStokes/DefectIncrementBounds.lean:214` | Integrates the averaged scalar over the radial variable. |

## Interpretation

This proves a domain boundary in the selected atlas: the production
zero-extension is explicit outside the positive-validity region. It does not
prove that the selected native scalar is nonzero on that region, nor that the
omitted region contributes a nonzero amount to `torusAverage` or `barMoment`.
Accordingly it strengthens the transport obligation but does not establish
`Δm ≠ 0`, `False`, or a completed refutation.

## Reproduction

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean \
  NavierStokesReview/src/completions/SelectedAtlasDomainBoundary.lean
```

Result: exit code `0`; no warnings.
