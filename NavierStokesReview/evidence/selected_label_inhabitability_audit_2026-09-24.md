# Selected-label inhabitability audit

## Result

The selected-label inhabitability objection remains open as an interface
obligation, not a proved selected-path vacuity. The source has a genuine empty
branch, but the review probe does not turn that branch into `False`.

The new zero-sorry probe
`NavierStokesReview/src/probes/SelectedLabelInhabitabilityProbe.lean`
compiles with Lean 4.34.0-rc2. The corrected companion audit
`NavierStokesReview/src/audit/SelectedActivePairReachability.lean` also
compiles. Neither file uses `sorry`, `axiom`, or `unsafe`.

## Flat source ledger

| Location | Definition or theorem | What it establishes | Status |
|---|---|---|---|
| `NavierStokes/CorrectionInitialization.lean:3923-3929` | `ActualPrimary.choice_nonempty`, `ActualPrimary.choice` | A `Choice` record is selected noncomputably. | Does not establish `Nonempty (ActualPrimary.Label B N0)`. |
| `NavierStokes/CorrectionInitialization.lean:3931` | `ActualPrimary.Label` | The label is `PrimaryGeometryAssembly.Index nominal prepared.N`. | The label is a subtype whose inhabitance must be proved separately. |
| `NavierStokes/BaseChartJets.lean:824-827` | `CellIndex` | A positive active label together with `N ≤ L.val.1`. | Supplies a label property after a label exists; it is not a constructor for one. |
| `NavierStokes/ActualParticularStageControls.lean:442-445` | `Active`, `ActivePair` | An active pair is a stage label/band pair satisfying `1 ≤ n` and the level-window predicate. | The type is permitted to be empty. |
| `NavierStokes/ActualParticularStageControls.lean:941-976` | `raw_jets`, nonempty branch | Uses a surjection `ℕ → ActivePair B N0` only after assuming `Nonempty (ActivePair B N0)`. | Conditional, not selected-path inhabitance. |
| `NavierStokes/ActualParticularStageControls.lean:977-987` | `raw_jets`, empty branch | Derives all local support obligations from `¬ Nonempty (ActivePair B N0)` because membership supplies an active pair. | A real vacuous branch. |
| `NavierStokes/ActualInitialMean.lean:25` | `ActualInitialMean.Index` | Defines the cycle index as `ActualPrimary.Label B N0 × Fin 2`. | No `Nonempty` instance is exported here. |
| `NavierStokes/ActualInitialMean.lean:318-341` | `covariance_bounds_of_curl` | Explicitly splits `isEmpty_or_nonempty (Index B N0)` and proves the empty case by zero sums. | Confirms that upstream estimates tolerate an empty index. |
| `NavierStokes/LocalScheduleWitness.lean:21-34` | `potentialSum`, `directSum`, `pressureSum` | Builds each sum from `SolenoidalDiagonal.potentialSum` over `j : ℕ`. | The sum is not indexed by `ActivePair`. |
| `NavierStokes/SolenoidalDiagonal.lean:35-38` | `potentialSum` | Defines an actual `tsum` of `cutStage` terms over natural stage indices. | Type-level totality does not prove a nonzero term or physical non-vacuity. |
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` | Quantifies a natural schedule, three `AwayExtensions`, a force, and endpoint consequences. | Contains no `Nonempty (ActualPrimary.Label ...)`, `Nonempty (ActivePair ...)`, or five-moment field equality. |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1185` | `selected_witness`, `selected_candidate` | Exports the selected existential witness and C/D candidate. | Does not export an active-pair inhabitant theorem. |

## Zero-sorry probe results

`active_pair_of_label` proves the valid conditional implication. It constructs
the stage label `(0, L)`, takes `n = BaseChartJets.cellBand L`, uses the label
property to obtain the lower-band bound, and applies `CommonWindow.self_mem n`.

`empty_active_pair_makes_control_patch_empty` reproduces the source-level
empty-branch mechanism: any point in `controlPatch l n k` would carry an
`Active l n` proof and therefore inhabit `ActivePair`.

`potentialSum_total_under_empty_active_pair` proves only that the output
`VelocityField` has a term-level value even when an empty active-pair
hypothesis is supplied. `potentialSum_is_nat_indexed` unfolds the definition
to the natural-indexed `SolenoidalDiagonal.potentialSum`. This rules out the
more specific claim that the diagonal `tsum` is vacuous merely because the
active-pair subtype might be empty.

## Audit disposition

CTR-019 is a live reachability obligation:

1. The empty branch is real and upstream estimates explicitly tolerate an
   empty index.
2. The selected witness does not export the missing label or active-pair
   inhabitant theorem.
3. The diagonal series is nevertheless total over `ℕ`; empty active pairs do
   not, by themselves, make its limit an empty-set limit.
4. A formal contradiction still requires either a proof that the selected
   label subtype is empty together with a selected mandatory non-vacuity
   consequence, or a separate false field-level endpoint identity.
