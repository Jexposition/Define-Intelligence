# Selected R3 packaging boundary

## Source

`NavierStokesR3.ActualCandidate.selected_candidate_one` exports a whole-space
`CandidateProperties` witness. Its `hc` value comes from
`ActualCandidateAssembly.selected_witness` through
`R3/ActualCandidate.lean:127-153`.

## Zero-sorry completion

`NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean`
compiles without `sorry`, `axiom`, or `unsafe`. It defines a nonzero
`Fin 5 → ℝ` payload and proves that this payload can coexist with the
exported R3 candidate, because the R3 `CandidateProperties` type contains no
five-moment field or equality.

Formally, this is a non-implication result:

$$
\operatorname{CandidateProperties}_{R^3}(u,p,f,K)
\not\Rightarrow
\forall d : (\operatorname{Fin} 5 \to \mathbb R),\ d=0.
$$

It does not assert that the actual selected field has nonzero moments. The
remaining field-level target is to calculate the selected `barMoment` and
transport it through the R3 compactification before claiming `\Delta m \ne 0`
or `False`.

## Verification

Focused command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean
  NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean
```

Result: exit code 0; no output.
