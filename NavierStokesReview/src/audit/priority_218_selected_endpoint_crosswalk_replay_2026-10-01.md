# Priority 218: selected-endpoint crosswalk replay

Date: 2026-10-01
Scope: live production source under `NavierStokes/`, current selected-path
documents, and the existing whole-tree transport census.

## Purpose

This replay tests the exact distinction that has repeatedly been conflated in
the review:

1. whether the selected construction has a real internal invariant and
   residual-to-force route; and
2. whether the exported selected endpoint identifies its completed Cartesian
   fields with the manuscript's named five observables
   `(M,I,J,S,C_p)`.

The result is not inferred from imports alone and is not an impossibility
claim.

## Positive selected-path chain

The production source contains the following connected route:

| Layer | Source declaration | Current source location | Finding |
|---|---|---:|---|
| Internal five-coordinate repair | `PositiveOrderMoments.moments_repair` and `moments_repair_target` | `NavierStokes/PositiveOrderMoments.lean:251-284` | Genuine profile-level moment repair and target correction. |
| Rank correction | `FiveRowRank.FiveRows` and its construction theorem | `NavierStokes/FiveRowRank.lean:241-253, 318` | Genuine five-row rank/debt algebra. |
| Actual cycle invariant | `ActualCyclePreservation.state_runInvariant` and its projections | `NavierStokes/ActualCyclePreservation.lean:826-911` | Actual cycle data feed analytic, coherent, periodic, particular, and wave-transport data. |
| Physical data | `ActualCandidateAssembly.physicalData` | `NavierStokes/ActualCandidateAssembly.lean:1079-1088` | Actual stage representations produce `PhysicalData`; this is not a free generic shell. |
| Stage estimates | `ActualCandidateAssembly.estimates` | `NavierStokes/ActualCandidateAssembly.lean:1090-1098` | Concrete physical data are supplied to `GluedStageEstimates.actualStageEstimates`. |
| Residual limits and force | `CandidateFromLimits.tracedResidual_smooth`, `force_smooth`, and `force_eq_activated_residual` | `NavierStokes/CandidateFromLimits.lean:39-112` | Force smoothness is derived from actual residual-jet limits and recurrence/extension premises. |
| Blow-up route | `GermCandidateAssembly.origin_blowup` | `NavierStokes/GermCandidateAssembly.lean:146-159` | Axis growth is proved through the base asymptotic for the selected mixed velocity. |

## Export boundary

`ActualCandidateAssembly.Witness` is a proposition whose conjuncts include the
selected schedule, `ASum`, `BSum`, `PSum`, away extensions, forcing,
`CandidateProperties`, smooth force, `CandidateConsequences`, H3 blow-up,
force decay, and boundary limits at
`NavierStokes/ActualCandidateAssembly.lean:1121-1151`.

`selected_witness` is proved from the finite-stage witness at
`NavierStokes/ActualCandidateAssembly.lean:1177-1185`.

The inspected production declaration does not contain a conjunct identifying
the completed selected Cartesian velocity, pressure, residual, or force with
the manuscript's complete `(M,I,J,S,C_p)` composition. This is a contract
correspondence result, not a claim that the upstream moment machinery is
unused and not a physical proof that the selected integrals are nonzero.

## Force-regularity correction

The source does not support the claim that `force_smooth` is simply assumed
from `NativeBounds`. `CandidateFromLimits` declares its inputs as locally
uniform limits of every derivative of the actual Navier--Stokes residual at
`lines 8-14 and 39-41`; `tracedResidual_smooth` consumes the derivative
recurrence and those limits at `lines 45-55`; and `force_smooth` follows from
the smooth extension at `lines 80-87`. The resulting force agrees with the
activated residual before the singular time at `lines 97-112`.

This does not prove the missing paper-to-selected-field five-observable
identification. It does rule out the stronger description that the force
regularity was inserted as an unsupported top-level rate assumption.

## Negative endpoint search

The existing hardened whole-tree census indexed 31,831 declarations and found
zero production positive transport candidates. Its three manual candidates
were review-side, caller-supplied `barMoment` interfaces rather than
instantiations of `selected_witness`. The current source replay also found no
production declaration co-binding the selected endpoint terms
(`activatedVelocity`, `periodicVelocity`, `potentialSum`, `periodicPressure`,
or `selected_witness`) with the named five-moment terms and an equality
conclusion.

The negative result is bounded:

\[
\text{no located consumed production identity}
\not\Rightarrow
\Delta m\ne 0,
\quad
\text{force nonsmoothness},
\quad
\text{or }\bot.
\]

## Controlled conclusion

`CTR-005` remains **NOT ESTABLISHED** for complete manuscript-to-selected-
endpoint correspondence. The correct audit statement is asymmetric:

- the selected construction has a genuine internal invariant, physical-data,
  residual-rate, smooth-force, and blow-up route; and
- the reviewed production endpoint still does not expose a consumed theorem
  identifying that completed construction with the manuscript's full
  five-observable composition.

No claim of a compiler escape, a literal CMI failure, an impossible bridge, a
nonzero selected defect, or `False` is authorised by this replay.

Evidence: `NavierStokesReview/evidence/selected_endpoint_crosswalk_replay_2026-10-01.md`.
