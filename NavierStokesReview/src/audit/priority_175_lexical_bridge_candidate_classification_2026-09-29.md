# Priority 175: Declaration-level classification of lexical bridge candidates

**Date:** 2026-09-29
**Scope:** the seven active lexical candidates emitted by the selected-endpoint source census
**Status:** source-checked classification; no selected-field mismatch or impossibility theorem claimed

## Finding

The seven census candidates are not seven hidden versions of the missing
paper-to-endpoint transport theorem. Each declaration was inspected at source
level. They classify as rate estimates, local germ identities, axis-growth
results, or schedule/jet packaging. None has an output identifying the final
activated Cartesian velocity, pressure, or force with the manuscript's five
observables

\[
(M,I,J,S,C_p).
\]

This strengthens the earlier lexical census, but it does not prove that the
selected field has a nonzero moment defect. It establishes only that these
seven candidates do not discharge the missing value-level bridge.

## Candidate-by-candidate classification

| Candidate | Source role | Why it is not the missing bridge |
| --- | --- | --- |
| `ActualPhysicalStageBounds.initialDirect_rate` (`ActualPhysicalStageBounds.lean:594--605`) | A `JetRate` estimate for an initial angular/direct field | It proves a decay-rate bound for `MB.family.angularField`; it does not define or identify a five-observable integral of the selected Cartesian field. |
| `ActualPhysicalStageBounds.background_from_representations` (`:724--755`) | A finite-background `JetRate` estimate for `MixedDiagonalResidual.uncutVelocity` | It consumes local representation equalities and returns an uncut finite-stage rate. It does not pass through the completed sums, activation, radial observable, or `barMoment`. |
| `GermCandidateAssembly.potentialSum_eq_base_germ` (`GermCandidateAssembly.lean:75--95`) | A local eventual equality between a potential sum and its base germ | It is a pointwise neighbourhood statement for the potential under vanishing initial/stage germs. It is not an integral identity and does not mention the five paper observables. |
| `InitializedPhysicalBackground.directIncrement_rate` (`InitializedPhysicalBackground.lean:92--103`) | A native initial direct-field `JetRate` estimate | It bounds an angular field at the endpoint. It contains no selected-field moment, pressure, radial-integral, or periodisation statement. |
| `MixedAxisPreservation.origin_blowup_global` (`MixedAxisPreservation.lean:470--487`) | Axis asymptotic transfer from an anchored base to a mixed diagonal field | It proves a norm limit at the axis from `AxisPreservation.origin_blowup` and a base asymptotic. It does not prove moment transport. |
| `MixedCandidateAssembly.StageEstimates.exists_schedule` (`MixedCandidateAssembly.lean:67--91`) | Schedule extraction from `StageEstimates` | Its conclusion is a scale sequence with `ThreeSmoothSums` and `VanishingJointJets`. It does not assert equality between selected-field observables and `(M,I,J,S,C_p)`. |
| `MixedCandidateWitness.SelectedSchedule` (`MixedCandidateWitness.lean:25--31`) | A proposition packaging sequence growth, smooth sums, and vanishing residual jets | It is a schedule predicate. It contains no five-moment payload or final Cartesian integral. |

## Consequence for CTR-005

The inspected candidates show a real connected route into smooth residual jets:

\[
\text{physical estimates}
\to \text{schedule}
\to \text{smooth sums and vanishing residual jets}
\to \text{force extension}.
\]

They do not establish the separate route required to credit the manuscript's
five-observable mechanism to the exported endpoint:

\[
\text{selected activated Cartesian fields}
\to \operatorname{PaperMoments}(u,p)
\stackrel{?}{=}(M,I,J,S,C_p).
\]

The current classification therefore preserves:

* selected residual-jet and smooth-force route: established on the inspected
  path;
* final paper-specific five-observable transport: **NOT ESTABLISHED
  (CTR-005)**;
* selected mismatch, force nonsmoothness, literal CMI failure, and Lean
  contradiction: not proved.

## Evidence boundary

This report is declaration-level source evidence. It does not treat import
reachability, symbol co-occurrence, a local commutator, or a profile-level
numerical result as a selected-field calculation. The next value-level task is
to bind the actual finite `ASum`/`BSum`/`PSum` composition and its observable
domain before testing the infinite sum and axis limits.

## Source anchors

* `NavierStokesReview/evidence/selected_endpoint_source_census_2026-09-27.md`
* `NavierStokes/ActualPhysicalStageBounds.lean:594--605,724--755`
* `NavierStokes/GermCandidateAssembly.lean:75--95`
* `NavierStokes/InitializedPhysicalBackground.lean:92--103`
* `NavierStokes/MixedAxisPreservation.lean:470--487`
* `NavierStokes/MixedCandidateAssembly.lean:67--91`
* `NavierStokes/MixedCandidateWitness.lean:25--31`
