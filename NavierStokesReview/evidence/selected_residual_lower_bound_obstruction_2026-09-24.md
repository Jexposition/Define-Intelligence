# Selected residual lower-bound obstruction

## Result

`SelectedResidualLowerBoundObstructionProbe.lean` compiles with no `sorry`.
It proves the exact conditional contradiction needed by the force-jet attack:

```text
Vanishing residual norm at the endpoint
+ origin velocity norm tending to infinity
+ c * ‖u‖ ≤ ‖residual‖ for some c > 0
→ False.
```

The probe also transports `VanishingJointJets` at the actual one-sided origin
filter to the residual-norm limit required by that contradiction. The selected
origin filter is nontrivial; this is not a `Filter.bot` result.

## Source audit

- `NavierStokes/JointResidualLimits.lean:84-86` defines the residual predicate
  as convergence of every iterated derivative to zero.
- `NavierStokes/CandidateFromLimits.lean:39-41` consumes locally uniform
  residual limits as the explicit `hlim` premise.
- `NavierStokes/FinalSlowBase.lean:372-378` proves the selected base velocity
  norm tends to `atTop` at the origin.
- `NavierStokes/ActualCycleResidualBounds.lean:1158-1172` proves upper
  `JetRate` bounds for the selected residual; it does not state a positive
  lower bound from velocity to residual.
- `NavierStokes/PhysicalResidualJetBounds.lean:898-966` supplies a local
  residual identity and chart transport, but no such lower estimate.

## Disposition

This is a completed formal target specification, not a refutation of the
selected witness. The selected-force composition probe now shows that the
positive lower-bound premise is incompatible with the actual endpoint
cancellation. A velocity blow-up alone cannot replace that theorem because the
residual can cancel to flat order.

**Status:** force-jet falsification route closed; no selected-witness
contradiction established.
