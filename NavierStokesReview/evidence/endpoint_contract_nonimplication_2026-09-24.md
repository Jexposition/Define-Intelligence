# Endpoint contract non-implication

Date: 2026-09-24  
Status: proved contract limitation; not a literal C/D contradiction

## Result

`NavierStokesReview/src/extensions/EndpointContractNonImplication.lean`
proves, without `sorry`, that the exported periodic `CandidateProperties`
record does not imply the stronger predicate
`FixedForceSameDatumStable`.

The theorem is:

```lean
candidateProperties_does_not_imply_fixedForceSameDatumStable :
  ¬ (∀ (u : VelocityField) (p : PressureField) (f : VelocityField),
    CandidateProperties u p f → FixedForceSameDatumStable u p f)
```

It obtains the selected candidate from
`selected_candidate_fails_fixed_force_same_datum_stability` and applies the
purported implication to that candidate. The existing same-datum perturbation
then supplies the contradiction. The proof is at lines 20--25.

## Interpretation

This is the exact logical statement supported by the fixed-force perturbation
work: the endpoint record does not encode stability under independent,
same-datum velocity perturbations while pressure and force remain fixed. It is
stronger than a generic affine test because the perturbation is smooth,
spatially compact on every time slice, divergence-free, and zero at the initial
time.

It does not prove `False` from the repository's literal C/D endpoint. The C/D
proposition quantifies over one candidate force and one candidate velocity; it
does not quantify over perturbations or require the stability predicate above.
The result is therefore a load-bearing endpoint-contract objection under
CTR-012, not a proof that the existential proposition is empty.

## Verification

`lake build NavierStokesReview` completed successfully with Lean
4.34.0-rc2 after adding the extension. `SameDatumAxiomAudit.lean` reports only
`propext`, `Classical.choice`, and `Quot.sound` for both the selected-path
obstruction and this non-implication theorem. No custom axiom, `sorry`, or
`unsafe` declaration was introduced.
