# Selected potential production product rule

Date: 2026-09-25
Classification: selected-field identity; sign unresolved

## Result

The review completion
`src/completions/SelectedPotentialProductionProductRule.lean` specialises the
repository's spatial product rule to the selected potential sum. For a point in
the unit cube, with differentiability of the time slice, it proves

$$
V_{\mathrm{prod}}(t,x)
= \chi(x)\,\operatorname{curl} A(t,x)
  + \operatorname{curlLinear}\!left(D\chi(x)\,A(t,x)\right),
$$

where $A$ is the selected potential sum and $\chi$ is the repository's spatial
cutoff. The second term is the cutoff/curl commutator. It is part of the
exported production field and cannot be discarded by identifying that field
with the native curl before localisation.

## Source anchors

| Item | Source location |
|---|---|
| Selected potential sum | `ActualCandidateAssembly.lean:531-534` |
| Cutoff and cut velocity | `SpatialLocalization.lean:41-49,165-172` |
| Product rule | `SpatialLocalization.lean:200-207` |
| Local periodisation equality | `SpatialLocalization.lean:266-270` |
| Selected specialisation | `NavierStokesReview/src/completions/SelectedPotentialProductionProductRule.lean:21-55` |

## Interpretation

This is a concrete selected-field identity. It strengthens CTR-005 and CALC-04
by identifying the term that must be transported through the Cartesian-to-radial
map, torus average, and final `tsum` before the paper's five-moment identities
can be attributed to the exported field.

The theorem does not assign a sign to the commutator, prove that its selected
radial integral is nonzero, or derive `False`. The live calculation therefore
remains the selected scalar transport and weighted integral, not a generic
cutoff objection.

## Verification

Focused Lean check and the full `NavierStokesReview` build both exited `0`.
The new module contains no `sorry`, custom axiom, or `unsafe` declaration.
