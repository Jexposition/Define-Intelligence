# Priority 203: internal invariant to endpoint cross-file trace

Date: 2026-09-30
Status: source-checked; bounded negative result
Disposition: `CTR-005` remains `NOT ESTABLISHED`

## Purpose

This tranche closes the recovery step that was still open after Priority 202.
It checks whether the actual two-plus-three invariant is merely an upstream
record, or whether a production declaration on the selected closure identifies
it with the manuscript's named `(M,I,J,S,C_p)` observables after the final
field construction.

The search is source-first and bounded by the current selected closure rooted
at `NavierStokes.R3.Theorem` and `NavierStokes.ActualCandidateAssembly`.
It is not a repository-wide impossibility proof and it does not infer a value
from the absence of a lexical match.

## Positive production path

The actual construction contains the following connected route.

1. `CorrectionState.radialMoment` and `CorrectionState.debt` define the
   radial/debt layer (`NavierStokes/CorrectionState.lean:226-250`).
2. `GaugeMassPreservation.ZeroMassesOn` supplies the two preserved mean-mass
   identities (`NavierStokes/GaugeMassPreservation.lean:140-142`).
3. `CorrectionStep.CycleAnalyticInvariant` stores both `debt` and `masses`
   (`NavierStokes/CorrectionStep.lean:9408-9448`).
4. `ActualCyclePreservation.state_runInvariant` and
   `ActualInitialization.initial_invariant` construct that invariant on the
   actual cycle (`NavierStokes/ActualCyclePreservation.lean:826-828`,
   `NavierStokes/ActualInitialization.lean:1427-1458`).
5. `DefectIncrementBounds.preserve_masses`, `zeroMasses`, and
   `rankStage_debt_eq` transport the mass rows and three debt classes through
   the correction step (`NavierStokes/DefectIncrementBounds.lean:714-870`).
6. `ActualCandidateAssembly.physicalData` consumes actual stage realizations
   and produces `PhysicalData` (`ActualCandidateAssembly.lean:1079-1088`).
7. `ActualCandidateAssembly.estimates` passes that physical data to
   `GluedStageEstimates.actualStageEstimates` (`ActualCandidateAssembly.lean:1090-1098`).
8. `ActualCycleResidualBounds.Invariant.residual_jetRate` consumes
   `PhysicalData` and state realisation data to derive the residual rate
   (`ActualCycleResidualBounds.lean:1156-1172`).
9. `CandidateFromLimits.tracedResidual_smooth` and `force_smooth` derive the
   smooth force from residual recurrence, boundary jets, and locally uniform
   limits (`CandidateFromLimits.lean:45-112`).
10. `ActualCandidateAssembly.Witness` packages the selected sums, activated
    velocity and pressure, force, candidate consequences, blow-up limit, and
    force boundary limits (`ActualCandidateAssembly.lean:1121-1151`).

This is a genuine constructional chain. It rules out the earlier description
of the endpoint as a bare or unsupported `NativeBounds` shell.

## Cross-file endpoint test

The selected closure contains the following relevant symbol families:

| Internal mechanism | Final endpoint mechanism |
| --- | --- |
| `radialMoment`, `ZeroMassesOn`, `CorrectionState.debt`, `FiveRows`, `barMoment`, `physicalMoments` | `ASum`, `BSum`, `PSum`, `potentialSum`, `periodicVelocity`, `periodicPressure`, `activatedVelocity`, `activatedPressure`, `selected_witness` |

The production declarations found on the left prove local profile, rank,
mass, debt, pressure, and finite-stage identities. The production declarations
found on the right construct the final mixed sums, localisation, residual
limits, and endpoint proposition. The current selected closure contains no
declaration whose result type simultaneously:

- identifies the internal two-plus-three coordinates with the manuscript's
  named `(M,I,J,S,C_p)` quantities;
- specifies the required coordinate/projection and pressure conventions;
- transports that identification through the activated Cartesian field,
  periodisation, torus average, radial integration, infinite summation, and
  force export; and
- is consumed by `Witness` or `selected_witness` as a final observable
  equality.

This is a bounded source-search result. It is not a claim that no theorem can
exist elsewhere in the repository, nor that the concrete selected integrals
are nonzero or wrong.

## Why the endpoint can still compile

The endpoint does not require the five-observable equality as a field of its
contract. It requires the actual physical data, residual-rate, extension, and
candidate-consequence propositions shown above. In symbols, the current
source proves a route of the form

\[
  \text{cycle invariant}
  \Rightarrow \text{physical data and residual rates}
  \Rightarrow \text{residual limits and smooth force}
  \Rightarrow \text{candidate consequences and blow-up}.
\]

The unresolved stronger statement is

\[
  \text{internal two-plus-three invariant}
  \Rightarrow (M,I,J,S,C_p)
  \Rightarrow \text{final selected Cartesian observable identity}.
\]

The first implication is evidenced internally. The second and third are not
present as a named consumed production theorem in the inspected selected
closure. This explains compilation without declaring the manuscript
mechanism irrelevant: Lean checks the proposition encoded by `Witness`, while
the audit asks whether that proposition is the exact paper-level construction
OpenAI claims it formalises.

## Disposition

The current evidence supports:

- genuine internal moment/debt machinery on the selected path;
- actual physical-data and residual-rate consumption;
- a formally encoded forced endpoint with smooth force and blow-up
  consequences on the inspected route;
- `CTR-005: NOT ESTABLISHED` for complete manuscript-to-selected-endpoint
  correspondence.

The current evidence does **not** support:

- a selected nonzero moment defect;
- force nonsmoothness;
- literal failure of Fefferman's forced alternative;
- a compiler cheat, hidden axiom, or kernel contradiction;
- the claim that the five equations are the sole residual-cancellation
  mechanism.

## Reproducibility anchors

- `NavierStokesReview/src/probes/ActualMomentPreservationTrace.lean`
- `NavierStokesReview/evidence/source_tranche_priority_202_actual_moment_invariant_trace_2026-09-30.json`
- `NavierStokes/ActualCandidateConstruction.lean:238-345,392-502`
- `NavierStokes/ActualPhysicalPrefixFields.lean:340-427`
- `NavierStokes/ActualCandidateAssembly.lean:1079-1151,1177-1185`
- `NavierStokes/ActualCycleResidualBounds.lean:1087-1123,1142-1172`
- `NavierStokes/CandidateFromLimits.lean:45-112`
- `NavierStokes/GermCandidateAssembly.lean:146-271`
