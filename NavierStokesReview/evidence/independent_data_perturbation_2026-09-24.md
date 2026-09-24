# Fixed-force perturbation result

## Scope

This note tests the causal reading of the residual-designed force. It treats
the force as a fixed spacetime function while replacing a velocity field (u)
by (u+e), with the pressure held fixed. The test is an operator identity; it
does not assume that the selected construction admits an arbitrary perturbation
or that a new perturbation schedule has already been built.

## Source facts

- `NavierStokes/CandidateFromLimits.lean:82-112` defines the final force from
  the traced residual and proves agreement with the activated residual before
  the singular time.
- `NavierStokes/R3/PositiveTimeForce.lean:46-55` defines the positive-time
  wrapper as `timeCutoff z.1 • f z`; it does not create an independent PDE
  evolution.
- `NavierStokes/ResidualCalculus.lean` supplies the exact residual
  add/subtract identity used by the extension.

## Zero-sorry theorem

`NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean:22-52`
proves that if both (u) and (u+e) satisfy the same residual equation with
the same (p) and (f), then

$$
\partial_t e-\Delta e+(u\cdot\nabla)e+(e\cdot\nabla)u+(e\cdot\nabla)e=0.
$$

At `:54-69`, a nonzero value of this defect proves that the perturbed field
cannot satisfy the same fixed-force equation.

The probe now includes the explicit test field

$$
e_a(t,x)=(t-t_0)a,qquad a\ne0.
$$

`affine_time_perturbation_smooth`, lines 25-28, proves that this field is
globally `ContDiff ℝ ∞`; `affine_time_perturbation_divergence_free`, lines
30-33, proves that its spatial divergence is zero. The theorem
`affine_time_perturbation_defect_eq`, lines 85-119, computes its defect at
`t=t₀` exactly as `a`. `affine_time_perturbation_breaks_fixed_force`, lines
121-172, therefore proves that no nonzero `a` can preserve the same fixed
force at that point.

This is an operator-level causality test. The particular perturbation is not
compactly supported or finite-energy on `ℝ³`, so it is not itself an admissible
CMI witness perturbation. A compactly supported divergence-free version would
be a stronger, separate theorem.

The reusable version is
`NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean`:

- `FixedForceData`, lines 18-19, packages a force as a fixed spacetime datum;
- `fixed_force_perturbation_defect_zero`, lines 21-51, proves the defect
  identity;
- `fixed_force_data_perturbation_obstruction`, lines 53-70, gives the global
  fixed-datum obstruction;
- `positive_time_force_perturbation_obstruction`, lines 72-91, instantiates it
  for `NavierStokesR3.PositiveTimeForce.force`.

## Compilation

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean
```

Result: exit code 0, no `sorry`, no custom axiom, and no compiler diagnostic.
The standalone probe also compiled with exit code 0.

## What this proves

The force cannot adapt to this perturbation while remaining the same fixed datum:
the cross terms and the quadratic perturbation term must be cancelled by the
perturbation itself. This is a formal obstruction to describing a
residual-designed construction as a forward evolution robust under independent
velocity perturbations. This is stronger than an interface-only observation:
the kernel computes a nonzero defect for a concrete smooth divergence-free
test field.

## What this does not prove

It does not prove that the literal existential C/D proposition is false. The
existential witness may consist of one specially matched pair `(u,p,f)`, and
the source does not state a perturbation-stability premise for that witness.
No theorem in this result proves that `StageEstimates.exists_schedule` fails
for an arbitrary (e). The next decisive formal target is a selected-path
theorem producing one admissible perturbation with a nonzero defect, or an
independent-data requirement stated as part of the claimed theorem.
