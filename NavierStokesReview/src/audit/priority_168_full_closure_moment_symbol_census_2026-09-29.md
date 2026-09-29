# Priority 168: full endpoint-closure moment-symbol census

**Date:** 2026-09-29
**Status:** source-traced and import-closure checked; declaration-level selected-witness transport remains unresolved.

## Decision

The earlier wording that the endpoint closure contains no five-moment machinery
was too narrow and must not be repeated. A direct closure run rooted at
`NavierStokes.R3.Theorem` found 588 project modules and completed with exit
code 0. A source census found 32 of those modules containing exact symbols
from `FiveProfileMoments`, `PositiveOrderMoments`, `FiveRowRank`,
`physicalMoments`, or `barMoment`.

This establishes genuine import reachability and substantial upstream use. It
does not establish that the selected theorem's proof term transports the
paper's five observables through the final activated Cartesian fields.

The correct distinction is therefore:

```text
repository source/import closure       = moment machinery is genuinely present
selected declaration contract          = no final five-observable equality exported
selected proof-term transport          = requires declaration-level tracing
```

## Evidence from the full closure

The direct closure command was:

```text
direct_lean_closure.py NavierStokes.R3.Theorem --workers 4
```

It reported 588 project modules, all cached or compiled successfully. The
exact-symbol census identified these load-bearing declarations, among others:

| Module | Declaration and line | What it establishes |
|---|---:|---|
| `FiveProfileMoments.lean` | `physicalMoments_eq`:637; `local_profile_moments`:1136 | profile-level physical moment identities |
| `PositiveOrderMoments.lean` | `moments_repair_target`:276; `exists_parameterized_exact_repair`:916 | exact reduced-profile repair |
| `GlobalStressSupport.lean` | `moments_zero`:146 | upstream stress-support moment cancellation |
| `NominalProfile.lean` | `corrected_moments`:288 | corrected nominal-profile moments |
| `ModulatedHistories.lean` | `actual_histories_restored`:987 | restored profile history identities |
| `MeanRankUpdate.lean` | `physical_five_rows`:163 | physical three-coordinate row update |
| `DefectIncrementBounds.lean` | `fiveRows_preserve_masses`:634; `fiveRows`:775 | rank/debt correction identities |
| `StateMomentBalances.lean` | `axial_flux_pressure_moment`:955 | state-level pressure/moment balance |
| `TerminalCompensation.lean` | `physicalMoments_eq`:540; `physicalMoments_cancel`:570 | terminal compensation identities |

The shortest import paths from `NavierStokes.R3.Theorem` reach these modules
through `ActualCandidateAssembly`, `InitialPhysicalData`,
`ActualPhysicalPrefixFields`, `CorrectionInitialization`,
`AssembledSlowBase`, `GlobalSlowProfiles`, and the cycle/correction modules.
Consequently, it is incorrect to describe these modules as unreachable,
dead, or unrelated to the endpoint repository.

## What the census does not prove

Import reachability is not declaration-level proof-term reachability. The
direct source of `ActualCandidateAssembly.Witness` still packages:

- the selected schedule;
- the three potential sums;
- extensions and forcing;
- `CandidateProperties` and `CandidateConsequences`;
- residual/force regularity, energy, support, and blow-up conclusions.

At `ActualCandidateAssembly.lean:1121-1151`, it does not visibly require an
equality of the form

\[
\operatorname{Moments}(u_{\rm selected},p_{\rm selected},f_{\rm selected})
  =(M,I,J,S,C_p).
\]

The file's direct references include `StageEstimates`, `physicalData`,
`GluedStageEstimates.actualStageEstimates`, `NativeBounds`-style rate data,
and the selected witness, but no direct reference to the five observable
symbols. That observation is only about the exported declaration and does not
show that upstream moment identities are unused in the definitions supplied
to it.

## Required next audit

The next task is not another import scan. It is a declaration-level transport
trace:

1. identify the exact declarations used by `InitialPhysicalData`,
   `ActualCandidateConstruction`, `ActualCyclePreservation.state_coherent`,
   `ActualCandidateAssembly.estimates`, and `GermCandidateAssembly.witness`;
2. record whether each declaration consumes a moment/rank theorem as a proof
   argument or merely imports a module containing one;
3. follow the resulting objects into `StageEstimates`, `VanishingJointJets`,
   `potentialSum`, `periodicVelocity`, and the activated field;
4. search for an equality or equivalence that identifies the completed field's
   observables with the paper's five quantities.

Until that declaration-level trace finds such an identity, the accurate status
is `CTR-005: final selected-field five-observable correspondence not
established`. This is not a claim of nonzero defect, force nonsmoothness, or
failure of the literal existential endpoint.

## Source locations

- `NavierStokes/ActualCandidateAssembly.lean:1079-1151`
- `NavierStokes/ActualCandidateConstruction.lean:1-9`
- `NavierStokes/ActualCyclePreservation.lean:840-912`
- `NavierStokes/CorrectionStep.lean:9408-9461`
- `NavierStokes/FiveProfileMoments.lean:637-655,1136-1180`
- `NavierStokes/PositiveOrderMoments.lean:171-286,916`
- `NavierStokes/MeanRankUpdate.lean:135-193`
- `NavierStokes/TerminalCompensation.lean:540-570`
