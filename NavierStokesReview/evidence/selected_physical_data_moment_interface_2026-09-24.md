# Selected physical-data moment-interface recheck

## Result

The selected construction does supply `PhysicalData` for every finite stage,
and that record is consumed by `ActualCandidateAssembly.estimates`. The
record is not, however, a five-moment certificate.

The exact source boundary is:

| Source | Observation |
|---|---|
| `ActualCycleResidualBounds.lean:1015-1037` | `PhysicalFields` contains local smoothness, differentiability, velocity and pressure germs, and exterior equality. It has no `Debt` field. |
| `ActualCycleResidualBounds.lean:1089-1122` | `Invariant.stateRealization` turns those fields into `StateRealization` and `chartIdentity`; the premises are local operator and germ identities. No `PositiveOrderMoments` equality is introduced. |
| `ActualCycleResidualBounds.lean:1142-1143` | `PhysicalData` is only an abbreviation for `PhysicalFields`. |
| `ActualCycleResidualBounds.lean:1156-1173` | `Invariant.residual_jetRate` consumes `PhysicalData` and returns a residual `JetRate`. The conclusion contains no five-coordinate moment payload. |
| `ActualCandidateAssembly.lean:1079-1098` | The selected source constructs `physicalData` and passes it into `estimates`. |
| `ActualCandidateAssembly.lean:1121-1151` | `Witness` exports the schedule, mixed sums, extensions, force, candidate properties, consequences, blow-up, decay, and endpoint jets, but no five-moment equality. |

## Zero-sorry selected-path probe

`src/probes/SelectedPhysicalDataMomentInterfaceProbe.lean` compiles under
Lean 4.34.0-rc2. It instantiates the actual selected `physicalData` theorem
and pairs the resulting record with an arbitrary nonzero
`PositiveOrderMoments.Debt`. This proves the interface-level statement:

$$
\text{selected physical-data record}
\not\Rightarrow
\text{exported five-moment payload}.
$$

It does **not** prove that the actual selected fields have incorrect moments.
To obtain that stronger result, a theorem must equate the five integrals of
the selected mixed fields with the paper tuple and then show one equality is
false.

## Consequence for the counter-paper

This is a selected-path specification failure supporting CTR-005. It is
stronger than an import-graph observation and narrower than a kernel-level
refutation. The affirmative burden remains with the authors: they must expose
the missing field-level transport theorem before the paper's five-moment
mechanism can be treated as established by the exported endpoint.

## Build validation

`lake build NavierStokesReview` completed successfully under Lean
4.34.0-rc2, with 3688 jobs and no `sorry` or `unsafe` additions in the probe.
