# Selected residual provenance

## Result

`NavierStokesReview/src/extensions/SelectedResidualProvenance.lean` compiles
without `sorry`, `axiom`, or `unsafe` declarations. Its theorem
`selected_candidate_force_is_residual_output` destructs the exported
`ActualCandidateAssembly.selected_candidate` and proves that the selected
force satisfies

$$
f(t,x)=\mathcal R(u,p)(t,x)
$$

for every $0<t<1$ and every spatial point.

## Source path

The construction path is visible in
`NavierStokes/MixedPeriodicAssembly.lean:338-365`: the force witness is
`CandidateFromLimits.force`, and `CandidateFromLimits.force_eq_activated_residual`
identifies it with the activated residual before the singular time. The
exported `CandidateProperties.navier_stokes` field carries the same identity
through `ActualCandidateAssembly.selected_candidate`.

## Interpretation boundary

This is a formal provenance result. It confirms that the published
construction is residual-designed rather than a forward evolution from a
force selected independently of the candidate trajectory. It does not prove
that the literal existential C/D proposition is inconsistent: the exported
predicate contains no force-independence or perturbation-stability field.
The result strengthens CTR-012 and leaves the selected five-moment
transport objection CTR-005 active.

## Reproduction

```text
lake env lean NavierStokesReview/src/extensions/SelectedResidualProvenance.lean
```

The command completed with exit code 0 on 2026-09-24.
