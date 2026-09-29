# Load-Bearing Five-Moment Dependency Matrix

**Audit date:** 2026-09-29
**Scope:** OpenAI's Navier–Stokes paper versus the current Lean source and the exported selected witness.
**Classification:** CTR-005, selected-field paper-to-code correspondence not established.

## Purpose

This document records why the five cumulative quantities

\[
(M,I,J,S,C_p)
\]

are not a decorative detail in the paper.  The paper uses them as load-bearing
premises for matching, stress-tail removal, modulation repair, and the
inductive correction cycle.  The audit therefore asks a narrower and stronger
question than whether similarly named upstream declarations exist:

> Does the actual selected Cartesian field exported by the Lean endpoint carry
> the same five-moment identities that the paper uses in its proof?

The present answer is **not established**.  This is an adverse finding against
the advertised machine-checked paper claim.  It is not a request that OpenAI
be given an opportunity to repair the claim, and it is not yet a theorem that
the selected field has a nonzero defect or that Lean proves `False`.

## Evidence layers

The matrix separates four propositions that must not be conflated:

1. **Paper dependence:** the published argument actually uses the five moments.
2. **Upstream Lean machinery:** the repository contains real moment and repair
   theorems.
3. **Selected-field transport:** those identities are carried through the
   actual Cartesian production pipeline into the public witness.
4. **Falsification:** a direct field calculation proves a nonzero defect,
   impossibility, or contradiction.

The first two are established by the sources cited below.  The third is not
established by the inspected endpoint declarations.  The fourth remains a
separate research target and must not be silently inferred from the third.

## Dependency matrix

| Paper dependency | What the paper uses | Upstream Lean evidence | Exported selected-path boundary | Audit status |
|---|---|---|---|---|
| Exterior matching | Matching the five cumulative radial integrals preserves the outer pressure, radial velocity, and stress fields. | `NominalProfile.heated_moments_at_match` and `heated_moments` in `NavierStokes/NominalProfile.lean:1970–2019`; `heated_five_moments` at `2108–2145`; `PositiveOrderMoments.pressureHistory_exterior_of_moments` at `510–518` and `fluxHistory_exterior_of_moments` at `602–611`. | `ActualCandidateAssembly.Witness` in `NavierStokes/ActualCandidateAssembly.lean:1121–1151` exports sums, extensions, `CandidateProperties`, force regularity, consequences, blow-up, and boundary limits. Its proposition has no selected-field equality to `(M,I,J,S,C_p)`. | Paper dependence and upstream machinery established; final-field identification not established. |
| Stress-tail removal | The paper uses total moment identities to remove exterior radial stress and pressure tails. | OpenAI paper `docs/navier-stokes openai.txt:1578–1586, 2553–2554, 2572–2581`; `PositiveOrderMoments.pressureHistory_exterior_of_moments` and `fluxHistory_exterior_of_moments`; `GlobalStressSupport.nominal_stresses_exterior` at `NavierStokes/GlobalStressSupport.lean:431–447`. | `CandidateProperties` in `NavierStokes/ProblemStatement.lean:101–123` and `NavierStokes/R3/ProblemStatement.lean:92–109` requires smoothness, support, incompressibility, residual equality, energy, and blow-up, but no paper-moment identity or absolute stress-tail certificate. | The paper's use is load-bearing; the selected endpoint does not expose the required identification. This is a correspondence failure, not yet a computed stress contradiction. |
| High-frequency modulation repair | Modulation changes the radial moments by `O(N⁻¹)`; a separate correction restores all five exactly and preserves the exterior fields. | OpenAI paper `docs/navier-stokes openai.txt:533–546`; `PositiveOrderMoments.moments_repair_target` at `NavierStokes/PositiveOrderMoments.lean:275–285`; `NominalProfile.Witness.five_moments` at `NavierStokes/NominalProfile.lean:2536–2541`. | The endpoint's `StageEstimates` in `NavierStokes/MixedCandidateAssembly.lean:29–65` contains smoothness, rate, raw-stage, background, and residual-rate fields, but no five-moment payload. `GluedStageEstimates.actualStageEstimates` at `NavierStokes/GluedStageEstimates.lean:684–701` converts concrete cycle data into that generic interface. | Concrete upstream repair is real; the generic packaging interface does not certify that the selected Cartesian field retains the paper's repaired tuple. |
| Inductive five-equation correction cycle | Each cycle cancels three defects while preserving two moment constraints; the decay improvement is then used in the final local field. | OpenAI paper `docs/navier-stokes openai.txt:727–731, 5250–5262, 5559–5564`; `MeanRankUpdate.physical_five_rows` at `NavierStokes/MeanRankUpdate.lean:163–174`; `CorrectionState.rank_model_rows` and `rank_rows_on_patch` at `NavierStokes/CorrectionState.lean:449–476`; `ActualCyclePreservation.rank_geometry` at `NavierStokes/ActualCyclePreservation.lean:91–96`. | `selected_witness` at `NavierStokes/ActualCandidateAssembly.lean:1177–1181` is proved through `witness` and the generic estimate route. The public `Witness` type has no field equating the final `ASum/BSum/PSum`-derived Cartesian field to the five paper observables. | Local cycle/rank results are established; their complete transport into the selected whole-space witness is not established. |

## What the endpoint actually proves

The current source inspection establishes the following endpoint shape:

```text
actual cycle data
  -> GluedStageEstimates.actualStageEstimates
  -> generic StageEstimates / NativeBounds obligations
  -> ActualCandidateAssembly.Witness
  -> R3 localization and CandidateProperties
  -> selected_witness / theorem_1_1
```

The `Witness` proposition does carry real objects: potential sums `ASum`,
`BSum`, `PSum`, away extensions, a forcing field, candidate properties,
regularity, consequences, blow-up, force jet rates, and boundary limits.  It
is therefore not a zero-field placeholder.  The precise problem is different:
the proposition does not contain a conjunct identifying the final Cartesian
fields and residual with the paper's five cumulative moments, nor a theorem
composing the reduced-profile certificates with the full lift, curl,
localisation, summation, and periodisation pipeline.

Likewise, the abstract `StageEstimates` interface is moment-blind, but the
concrete `GluedStageEstimates.actualStageEstimates` does ingest actual cycle
data.  The audit therefore does **not** claim that the concrete selected field
is zero or that all upstream moment information is discarded during
construction.  It claims that the public endpoint does not certify the
paper-level identification needed to treat the upstream identities as the
identities of the exported field.

## Consequence for the advertised claim

The missing identification is decisive because the paper uses the moments to
justify later conclusions.  On the current formal record, the chain

\[
\text{five profile identities}
\longrightarrow
\text{selected Cartesian field}
\longrightarrow
\text{stress/pressure cancellation and endpoint blow-up}
\]

is not a machine-checked chain.  The correct present verdict is therefore:

> **Reject the advertised claim of a machine-checked formalisation of the
> paper's five-moment proof on the current record.**

This does not assert that the upstream identities are false, that the selected
field necessarily violates them, or that the literal existential C/D
proposition has already been refuted.  A stronger falsification requires a
direct value-level calculation of the selected field, for example a proved
nonzero moment defect or an incompatibility theorem.  Until such a calculation
exists, the evidence supports **Not Established / CTR-005**, not a completed
kernel-level `False` result.

## Primary source pointers

- OpenAI paper extraction: `docs/navier-stokes openai.txt`.
- Endpoint source: `NavierStokes/ActualCandidateAssembly.lean:1121–1181`.
- Candidate predicates: `NavierStokes/ProblemStatement.lean:101–123` and `NavierStokes/R3/ProblemStatement.lean:92–109`.
- Generic rate interface: `NavierStokes/MixedCandidateAssembly.lean:29–65`.
- Concrete estimate ingestion: `NavierStokes/GluedStageEstimates.lean:684–701`.
- Existing audit evidence: `selected_endpoint_moment_transport_obstruction_2026-09-25.md`, `selected_moment_transport_source_trace_2026-09-25.md`, and `selected_transport_audit_full_2026-09-28.md` in this directory.
