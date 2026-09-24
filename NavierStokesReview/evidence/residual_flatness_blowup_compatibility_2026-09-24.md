# Residual flatness versus velocity blow-up

## Question

Can the selected residual condition `VanishingJointJets` contradict the
origin blow-up condition used by `selected_witness`?

## Source facts

`JointResidualLimits.VanishingJointJets` is a predicate on one function
`f : SpaceTime → Space`. It requires every iterated Frechet derivative of
`f` to tend to zero at the left-hand endpoint `(1, 0)`. It does not quantify
over, or mention, the velocity field `u`.

`SpeedUnboundedAtOne` is a separate predicate on `u`. The selected path
derives it through the base profile and origin agreement. The residual
endpoint is constructed separately and is later used to extend the force.

## Zero-sorry probe

`NavierStokesReview/src/probes/ResidualFlatnessCompatibilityProbe.lean`
compiles with the pinned Lean toolchain and no `sorry`. It proves:

```lean
theorem residual_flatness_does_not_by_itself_exclude_blowup
    (u : VelocityField) (hu : SpeedUnboundedAtOne u) :
    ∃ f : SpaceTime → Space,
      VanishingJointJets f ∧ SpeedUnboundedAtOne u
```

The witness is the identically zero residual. Every iterated derivative of
that residual is zero, so all joint jets vanish, while the assumed velocity
blow-up remains unchanged.

## What this proves

This formally blocks the proposed implication

```text
VanishingJointJets residual → not SpeedUnboundedAtOne velocity.
```

It does not establish that the selected witness exists, and it does not
validate the selected witness. It proves only that a contradiction cannot be
obtained from the two predicates without using their PDE coupling.

## Remaining selected-path target

To refute `selected_witness`, a future probe must use the actual identity

```text
navierStokesResidual selectedVelocity selectedPressure = selectedForce
```

and then prove that the selected velocity, pressure, and force regularity
cannot satisfy the residual endpoint limits simultaneously. No such theorem
has been proved in this run.

## Disposition

Residual-flatness route: **interface incompatibility disproved; selected
endpoint contradiction unresolved**.
