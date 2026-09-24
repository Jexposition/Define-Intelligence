# Stage-estimate interface countermodel

## Finding

The generic `MixedCandidateAssembly.StageEstimates` interface is insufficient
to certify either the paper's five named moments or finite-time blow-up.

This is now machine-checked by
`NavierStokesReview/src/probes/StageEstimatesMomentBlindnessProbe.lean`.

## Formal result

The probe proves, with no `sorry`:

```text
Nonempty (StageEstimates (1 / 4) 1 zeroVelocityStages
  zeroVelocityStages zeroPressureStages)
```

where every velocity and pressure stage is identically zero, every loss and
constant is zero, the gain is `j ↦ (j : ℝ)`, and the finite background and
finite residual rate obligations are satisfied. It also proves:

```text
¬ SpeedUnboundedAtOne (fun _ => 0)
```

The residual-rate contracts therefore admit a completely static zero-field
model. They cannot, by themselves, imply a nonzero angular profile, any
five-coordinate moment identity, or the claimed blow-up.

## Scope

This is a genuine countermodel to the generic interface implication
`StageEstimates → blow-up/moment realisation`. It is not by itself a
countermodel to `ActualCandidateAssembly.selected_witness`, because the
selected endpoint supplies additional hypotheses, including the actual base
construction, physical data, axis preservation, and an origin blow-up theorem.

The load-bearing audit consequence is narrower and decisive: any claim that
the `StageEstimates` fields are themselves the formal verification of the
paper's five-moment physical repair is false. The selected endpoint still
requires a separate theorem transporting those moments into the selected
velocity, pressure, and residual fields. No such transport theorem has been
located.

## Source anchors

- `NavierStokes/MixedCandidateAssembly.lean:29-65`: exact fields of
  `StageEstimates`; no moment tuple or moment equality occurs in the structure.
- `NavierStokes/MixedCandidateAssembly.lean:67-91`: generic schedule theorem
  consumes only those analytic fields and rate contracts.
- `NavierStokes/ActualCandidateAssembly.lean:1165-1185`: selected aliases and
  witness export; no named five-moment transport appears in the endpoint type.
- `NavierStokesReview/src/probes/StageEstimatesMomentBlindnessProbe.lean`: the
  zero-sorry countermodel and non-blow-up result.

## Verdict

**Confirmed interface-level failure; not a complete selected-endpoint
refutation.** The paper's physical moment claim is not established by the
generic stage-estimate interface.

## Five-debt non-determination theorem

The same probe now contains the zero-sorry theorem
`interface_does_not_determine_five_debt`. It proves

```text
¬ (∀ E : StageEstimates ..., ∀ d : PositiveOrderMoments.Debt, d = 0)
```

by instantiating the generic interface with the zero-stage witness and then
choosing the constant-one five-coordinate debt. The theorem is deliberately
about the information content of `StageEstimates`; it does not claim that the
selected physical construction has constant-one debt. Its consequence is
that a selected-path transport theorem must add field-level moment equations
or derive them from the actual selected fields. The promotion map in the
separate five-row probe is algebraically valid, but it is not that transport
theorem.

**Disposition:** confirmed interface obstruction; selected-witness
contradiction still open.

## Reproducibility run

On 2026-09-24 the pinned Lean command
`elan run leanprover/lean4:v4.34.0-rc2 lake env lean` was run against this
probe and the four companion probes for the five-row bridge, axis scope,
pressure premises, and base-profile asymptotics. All five invocations exited
successfully with no errors or `sorry` diagnostics. The stage probe retains
only existing linter warnings about unused simplification arguments; these do
not affect the theorem result.
