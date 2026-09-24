# Selected-witness fixed-force obstruction

Date: 2026-09-24
Source file: `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean`

## Result

The extension contains the zero-sorry theorem
`selected_candidate_fixed_force_obstruction`. It destructs
`NavierStokes.ActualCandidateAssembly.selected_witness`, binds the selected
mixed velocity and pressure fields, and proves that the compact, divergence-free
perturbation

$$e(t,x)=(t-1/2)\,\operatorname{curl} A(x)$$

cannot satisfy the same fixed-force residual equation at `t = 1/2`, `x = 0`.
The defect is the nonzero vector `coordinateVector 0`.

The proof uses `NavierStokes.ResidualCalculus.navierStokesResidual_add_sub` and
the selected candidate property `hc'.navier_stokes` at the interior time
`1/2`. It does not assume an independent-force predicate that is absent from
`CandidateProperties`.

## Verified proposition

```lean
∃ (u : VelocityField) (p : PressureField) (f : VelocityField),
  CandidateProperties u p f ∧
  navierStokesResidual
      (fun z => u z + compactPerturbation ((1 : ℝ) / 2) z) p
      ((1 : ℝ) / 2) 0 ≠ f (((1 : ℝ) / 2), 0)
```

The result is an operator-level path-dependence theorem. It shows that the
selected residual construction cannot be reused unchanged after this specific
admissible perturbation. It does not show that the original existential C/D
proposition is empty, because that proposition quantifies over one candidate
force and one candidate field, not over all perturbations of that field.

## Reproduction

```text
lake env lean NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean
```

Observed result: exit code `0`; no `sorry`, `axiom`, or `unsafe` declaration was
added by this extension.

## Audit classification

| Item | Classification |
|---|---|
| Selected witness is instantiated | proved |
| Compact perturbation is smooth and divergence-free | proved in the same extension |
| Same fixed force survives the perturbation | disproved at the selected interior point |
| CMI existential endpoint is contradicted | not proved |
| Missing causal/provenance condition in the endpoint | remains a specification objection |

The finding strengthens CTR-012. It does not replace the selected-path
five-moment transport target under CTR-005 and does not justify a global `False`
verdict without an additional premise connecting perturbation admissibility or
force independence to the claimed endpoint.
