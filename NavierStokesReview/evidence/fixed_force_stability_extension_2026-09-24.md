# Fixed-force stability extension

Date: 2026-09-24

## Question

Does the selected candidate remain a solution of the same residual equation
after an admissible smooth, compactly supported, divergence-free perturbation
of its velocity field, while the force and pressure are held fixed?

## Formal construction

`NavierStokesReview/src/external_semantic/FixedForcePerturbationStability.lean`
defines:

- `AdmissiblePerturbation`, requiring global smoothness, compact spatial
  support on every time slice, and spatial divergence zero;
- `FixedForceStable`, requiring the same force equation for every such
  perturbation;
- `selected_candidate_fails_fixed_force_stability`, which instantiates the
  compact perturbation at `t₀ = 1/2` and the origin.

The proof uses the existing zero-sorry theorem
`selected_candidate_fixed_force_obstruction`. At `(t,x)=(1/2,0)`, the
perturbed residual differs from the fixed force by the nonzero vector
`coordinateVector 0`. Hence the selected candidate does not satisfy the
added `FixedForceStable` predicate.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

Result: `Build completed successfully (3686 jobs).`

The theorem is in the review-side `NavierStokesReview` library. A source scan
of the new file found no `sorry`, `axiom`, or `unsafe` declaration.

## Scope boundary

This is a formal result about an explicitly strengthened forward-data
predicate. It is not a proof of `False` from the literal C/D endpoint. The
exported endpoint asks for one force and one candidate and does not quantify
over perturbations or include force independence as a Lean premise. The result
therefore establishes a selected-path provenance/stability defect under the
stronger interpretation, while the literal existential proposition remains a
separate question.
