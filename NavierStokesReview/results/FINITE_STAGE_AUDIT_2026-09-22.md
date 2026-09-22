# Finite-stage and derivative-rate audit

Snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
Date: 2026-09-22

## Question

Does the exported candidate construction obtain the residual estimates it needs from explicit premises, or does it simply assume the desired estimate in a record that is later consumed as if it were proved?

## Trace

1. `NavierStokes/MixedCandidateAssembly.lean:27-65` defines `StageEstimates`. Its fields include raw-family smoothness, gain monotonicity and divergence, raw bounds, finite background jet rates, and finite residual jet rates.
2. `NavierStokes/GluedStageEstimates.lean:681-725` defines `actualStageEstimates`. It consumes run data, coherence, representations, smoothness of the current fields, current bounds, and `PhysicalData`; it fills the residual rate through the component-bound construction.
3. `NavierStokes/ActualCandidateAssembly.lean:1079-1098` supplies `physicalData` and then constructs `estimates` from the actual run, representations, coherence, and physical data.
4. `NavierStokes/ActualCycleResidualBounds.lean:1156-1173` derives the physical residual rate from `StateRealization.chartIdentity`, the selected geometry, the invariant's native residual estimate, and exterior germs.
5. `NavierStokes/PhysicalResidualJetBounds.lean:885-923` shows the premises in `StateRealization`: open domain, nonzero radius, matching, base and increment smoothness, base equation, physical smoothness/differentiability, and velocity/pressure germs.

## Result

No source-level vacuity was found in this chain. The residual rate is a derived field of a concrete record, not a declaration-level `axiom` or `sorry`. This is source evidence only. It does not replace the pending kernel `#print axioms` run or the analytic review of the imported cycle certificates.

## Specification concern

`NavierStokes/DiagonalResidual.lean:33-39` defines `JetRate` as an eventual inequality involving `iteratedFDeriv`. It does not bundle `ContDiff` or differentiability. Therefore `JetRate` alone is not a complete smoothness certificate. The final `StageEstimates` record separately requires `ContDiffOn` for the raw families, which prevents this observation from presently establishing a CMI mismatch. Every consumer that turns a rate into an endpoint extension or a smooth final field remains a follow-up audit target.

## Classification

`AUD-034`: confirmed source-level non-vacuity of the finite-stage record.

`AUD-035`: open formalisation-quality concern about the standalone strength of `JetRate`; not a negative verdict.
