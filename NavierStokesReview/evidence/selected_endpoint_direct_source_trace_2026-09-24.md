# Selected endpoint direct-source trace

**Date:** 2026-09-24  
**Scope:** selected Navier–Stokes witness and its immediate construction path

## Finding

The upstream five-moment and rank subsystems are live. The selected endpoint
also consumes real cycle data and residual estimates. The exported endpoint,
however, does not state the theorem that identifies the paper's five named
quantities with the selected mixed velocity, pressure, residual, or force.

This is a source-level correspondence omission. It is not evidence that the
upstream moment construction is dead, and it is not a proof that the selected
fields violate those identities.

## Source ledger

| Location | Direct result |
|---|---|
| `NavierStokes/ActualCandidateAssembly.lean:1079-1098` | `physicalData` and `estimates` are built from actual cycle fields, physical-field representations, and residual-rate bounds. |
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` exports a schedule, three raw stage families, away extensions, force, `CandidateProperties`, endpoint consequences, H³ blow-up, force decay, and boundary jets. |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1185` | `selected_witness` instantiates `Witness`; `selected_candidate` extracts only the candidate fields and force properties. |
| `NavierStokes/ActualStageEstimates.lean:116-123` | The actual run consumes `CorrectionState.debt` through `RunData.rank_class`. |
| `NavierStokes/CorrectionState.lean:449-490` | The rank system proves `FiveRows` for the actual rank construction and transports it to the base patch. |
| `NavierStokes/DefectIncrementBounds.lean:799-813` | The rank stage preserves the two internal radial correction moments. |
| `NavierStokes/PositiveOrderMoments.lean:192-284` | The positive-order subsystem defines genuine five-coordinate integrals and exact repair identities. |
| `NavierStokes/FiveProfileMoments.lean:483-691` | The profile subsystem defines a genuine five-coordinate physical moment map and its integral identity. |

The direct endpoint files `ActualCandidateAssembly.lean`,
`ActualStageEstimates.lean`, `ActualCycleResidualBounds.lean`,
`PhysicalResidualJetBounds.lean`, `GermCandidateAssembly.lean`, and
`MixedCandidateAssembly.lean` contain no direct occurrence of
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or `finiteIdentities` in the exported witness
statement. The transitive closure still reaches those modules upstream.

## Formal status

`SelectedCycleMomentTransport.lean` and the selected-witness path probes
compile without `sorry`, `axiom`, or `unsafe`. They establish the internal
cycle invariant and the endpoint type boundary. They do not prove `False`.

The decisive unresolved theorem remains a selected-field transport identity of
the form

$$
\text{paperMoments}(u,p)
= (M,I,J,S,C_p)
= \text{runtimeMomentData}(\text{selected cycle}),
$$

with that equality carried into the residual, pressure, force, and flat-jet
premises. Until this theorem is supplied or one of its concrete equalities is
refuted, CTR-005 is a correspondence failure rather than a formal
contradiction.
