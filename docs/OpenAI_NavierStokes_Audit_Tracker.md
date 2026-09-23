# OpenAI Navier–Stokes Counter-Paper Evidence Tracker

This document is the working ledger for the counter-paper. It records evidence, status, and the next falsification test. It is intentionally a tracker. The argument itself is written in `OpenAI_NavierStokes_Research_Paper.md`.

## Scope

- Upstream source under review: OpenAI Navier–Stokes repository, snapshot recorded as `f9e8bc5`.
- Review branch: `review/cmi-first-navier-stokes-2026-09-22`.
- Formal environment: the repository-declared Lean 4.34.0-rc2 through the local elan installation. The separate V-lab `packages-4.32` cache was not substituted because this fork pins matching 4.34.0-rc2 Mathlib and Comparator revisions.
- Boundary: the OpenAI source tree is not edited. Review probes live under `NavierStokesReview/src/probes`.

## Current position

The repository contains a genuine R³ C/D-shaped endpoint and the headline theorem reports only standard Lean axioms. The strongest adverse result is a cross-layer correspondence gap, not a proof that no five-row repair exists. `FiveProfileMoments` matches the paper-shaped normalisation, `PositiveOrderMoments` proves an exact five-component recursive repair, and `FiveRowRank` supplies a distinct three-debt physical rank interface. A zero-sorry theorem rules out a direct row-by-row bridge between the first and third interfaces, but that probe is not by itself a refutation because the positive-order layer may be an intended intermediate representation. The final theorem is not labelled refuted until a false mandatory premise or an impossible selected-path correspondence is proved.

## Evidence register

| ID | Claim or question | Evidence | Status | Next action |
| --- | --- | --- | --- | --- |
| CTR-001 | The source is only a periodic toy. | `NavierStokes/R3/ProblemStatement.lean` defines whole-space fields, compact support, finite energy, and unbounded speed. | Closed: objection rejected | Keep the R³ distinction in the paper. |
| CTR-002 | The force is active and residual-defined. | Official paper Section 2 and the R³ force definitions construct the force from the momentum residual through the collapse. | Confirmed semantic criticism, not C/D refutation | Audit smooth extension and decay directly. |
| CTR-003 | The endpoint hides custom axioms. | `MainAxiomProbe.lean` reports `propext`, `Classical.choice`, and `Quot.sound` only. | Closed for the inspected endpoints | Continue premise and correspondence inspection. |
| CTR-004 | Generic `JetRate` can be vacuous. | `JetRateVacuityProbe.lean` proves a `Filter.bot` limit can discharge the generic predicate. | Live hazard, not yet endpoint failure | Trace a non-bottom proof into every selected rate premise. |
| CTR-005 | The complete Lean pipeline is one coherent implementation of the paper's five-moment system. | `FiveProfileMoments.lean` matches the paper-shaped vectors; `PositiveOrderMoments.lean` proves exact five-component repair; `FiveRowRank.lean` declares a distinct three-debt interface. | Cross-layer correspondence not established | Identify the explicit staging maps and verify that the selected witness preserves all five named moments. |
| CTR-006 | The moment interfaces are accidentally being treated as the same object. | `MeanRankUpdate` consumes `FiveRowRank`; `ModulatedHistories` and `ReservedPatches` consume `FiveProfileMoments`; `GlobalSlowProfiles` consumes `PositiveOrderMoments`. | Direct-identification objection supported; endpoint refutation not established | Keep the direct obstruction, but audit the positive-order and nominal-to-physical maps before escalation. |
| CTR-007 | Non-Newtonian regularisation disproves the Newtonian theorem. | The published endpoint is Newtonian and C/D allows smooth force. | Rejected as internal refutation | Retain only as a physical robustness limitation. |
| CTR-008 | The two moment declarations may be treated as the same system by direct identification. | `MomentBridgeObstructionProbe.lean` proves `¬ DirectMomentBridge lam b` for all real `lam` and `b`, by evaluating the first axial coordinate. | Formally disproved at the direct-correspondence level | Require an explicit nontrivial change-of-variables theorem. |
| CTR-009 | The selected witness hides a custom axiom at the stage-estimate interface. | `SelectedDependencyAxiomProbe.lean` reports only `propext`, `Classical.choice`, and `Quot.sound` for `selected_witness`, `physicalData`, `actualStageEstimates`, and `Invariant.residual_jetRate`. | Closed for custom-axiom suspicion | Continue semantic and interface audit; do not treat standard axioms as defects. |
| CTR-010 | The two debt interfaces admit a direct full linear identification. | `MomentBridgeObstructionProbe.lean` proves `¬ Nonempty (FiveRowRank.Debt ≃ₗ[ℝ] FiveProfileMoments.Debt)` by finite-dimensional rank. | Formally disproved for full linear identification | Require an explicit constrained embedding or stage-separation theorem. |
| CTR-011 | The repository lacks an exact five-equation repair. | `PositiveOrderMoments.weighted_moments_exact`, `moments_repair_target`, and `exists_smooth_exact_repair` prove exact five-component repair; `GlobalSlowProfiles.profiles_moments` carries it into the recursive sequence. | Rejected by source inspection | Do not repeat the obsolete “three-equation approximation” claim. Audit cross-layer correspondence instead. |
| CTR-012 | The exported whole-space endpoint is disconnected from the selected construction. | `R3/Theorem.lean` obtains its fields from `ActualCandidateAssembly.selected_witness`, localises them through `R3/ActualCandidate.of_localized_fields`, proves the compact energy estimate, and transports viscosity by `R3/ViscosityScaling`. | Closed as an objection | Treat the R³ endpoint as connected to the selected witness; keep the adverse case focused on the missing moment correspondence. |

| CTR-016 | The whole-space comparison theorem imports an unproved scalar rate bound as an endpoint premise. | `R3/WholeSpaceComparisonClosure.lean` constructs the rate bound internally through `ComparisonRateBound.exists_uniform_rate_bound`. `R3/WholeSpaceUniqueness.lean` constructs the pressure-flux estimate through `PressureFlux.exists_uniform_actual_pressure_flux_bound`. `R3ComparisonPremiseProbe.lean` records the internal rate-bound construction. | Withdrawn as stated | The rate-bound interface is not an external premise. The remaining audit target is whether the pressure-recovery and localised PDE estimates prove their stated hypotheses with the intended whole-space meaning. |

| CTR-017 | The pressure/uniqueness chain may hide a vacuous or imported comparison premise. | `PressureRecovery.gradient_recovery_complex` uses explicit compact temporal tests; `HarmonicTestFunctionals.eq_zero_of_compact_harmonic` uses a Fourier Sobolev bound; `WholeSpaceComparisonClosure` constructs the scalar rate bound; selected-path axiom probes report only standard axioms. | Not substantiated in the inspected path | Preserve the pressure chain as a live mathematical audit target, but do not call it a formal failure without a concrete false identity or mandatory unprovable premise. |

## 2026-09-23 pressure-chain adjudication

The pressure and comparison audit was completed at source level. The generic `Filter.bot` warning remains real, but the inspected pressure-recovery path does not use an empty-filter shortcut: compact temporal tests are converted to pointwise equality on `Ioo 0 T` by continuity and an integral fundamental lemma. The harmonic-functional step is bounded by an explicit Fourier Sobolev norm before compact harmonicity is extended to the full Schwartz test space.

This closes the specific claim that the endpoint consumes a free scalar rate bound. The comparison closure constructs it internally, and the pressure-flux constant is constructed upstream from the pressure-recovery hypotheses. The chain remains analytically load-bearing, but no zero-sorry contradiction has yet been found in it.

## Formal artefacts

- `NavierStokesReview/src/probes/MomentCoordinateMismatchProbe.lean`: zero-sorry vector inequalities.
- `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean`: zero-sorry impossibility of a direct row-by-row bridge.
- `NavierStokesReview/src/probes/MainAxiomProbe.lean`: endpoint axiom report.
- `NavierStokesReview/src/probes/SelectedDependencyAxiomProbe.lean`: selected-path interface axiom report.
- `NavierStokesReview/src/probes/JetRateVacuityProbe.lean`: generic filter-vacuity witness.
- `NavierStokesReview/src/probes/OriginPastNeBotProbe.lean`: non-vacuity of the concrete origin-past filter.
- `NavierStokesReview/src/probes/OpenPastNeBotProbe.lean`: non-vacuity of a concrete open-past filter.
- `NavierStokesReview/src/probes/ForceActivityProbe.lean`: compiled force-activity consequence from `CandidateConsequences.consequences_of_candidate`.
- `NavierStokesReview/src/probes/FiveRowsStructureProbe.lean`: compiled source-structure check for the three-coordinate `FiveRows` debt and its two fixed zero rows.
- `NavierStokesReview/src/probes/MomentInitializationProbe.lean`: compiled zero-sorry check that the selected initial state satisfies the two preserved zero-mass rows.
- `NavierStokesReview/src/probes/R3ComparisonPremiseProbe.lean`: compiled zero-sorry source-level audit showing that the scalar comparison rate is constructed inside the R³ closure rather than passed into the endpoint as an unproved hypothesis; its endpoint `#print axioms` output contains only `propext`, `Classical.choice`, and `Quot.sound`.
- `NavierStokesReview/src/probes/ActivePairEmptyBranchProbe.lean`: compiled zero-sorry proof that the negative `Nonempty (ActivePair)` branch makes each `controlPatch` empty.
- `NavierStokesReview/src/probes/MovingFieldRowNonImplicationProbe.lean`: compiled zero-sorry countermodel showing that generic moving-field regularity does not entail the physical five-row equations.

Positive source evidence audited directly:

- `NavierStokes/PositiveOrderMoments.lean`: exact five-coordinate repair and arbitrary target theorem.
- `NavierStokes/GlobalSlowProfiles.lean`: recursive use of the five-row repair and zero-moment theorem.
- `NavierStokes/R3/Theorem.lean`, `NavierStokes/R3/ActualCandidate.lean`, and `NavierStokes/R3/ViscosityScaling.lean`: selected-witness extraction, compact whole-space closure, and positive-viscosity scaling.

## Decision rule

Use “formal disproof” only for a zero-sorry contradiction or a demonstrated false premise on the selected witness path. Use “correspondence failure” when the code proves a different proposition or leaves a required bridge absent. Use “semantic criticism” for physical objections that are outside the literal C/D statement.

## Current evidence update: 2026-09-23

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-012 | `(CandidateConsequences.consequences_of_candidate h).force_nonzero` yields a time `t ∈ (0,1)` and point `x` with `f (t,x) ≠ 0` for every `CandidateProperties` witness. | Compiled zero-sorry review probe; endpoint interpretation confirmed | The selected construction is continuously forced before the singular time. This is not a C/D refutation because the official C/D alternatives permit smooth forcing. |
| CTR-013 | The earlier suggestion that the repository lacked a periodic D endpoint was checked against `PeriodicPaperTheorem.lean` and withdrawn. | Corrected | The repository exports both whole-space and periodic C/D-shaped endpoints. The review must attack a false premise or correspondence, not a missing filename. |
| CTR-014 | The five-moment criticism was narrowed after inspection of `PositiveOrderMoments.lean`. | Corrected | The repository does contain an exact five-coordinate repair in that layer. The remaining adverse issue is the absence of an explicit bridge among nominal, positive-order, and physical-rank layers. |
| CTR-015 | `FiveRowRank.FiveRows` is a generic five-target, five-unknown solve. | Formally corrected | `FiveRows` has `Debt := Fin 3 → ℝ`; rows 1 and 2 are fixed zero-moment constraints, while rows 3–5 use debt coordinates 0–2. The new zero-sorry probe rules out describing this declaration itself as a full five-dimensional inverse, but does not refute the endpoint because the fixed rows may be valid invariants. |
| CTR-018 | The two fixed physical-rank rows preserve a nonzero initial mass. | Rejected on the selected witness | `ActualInitialization.initial_zeroMasses` proves the selected initial state has the relevant zero masses; the temporal and rank-stage correction interfaces preserve `ZeroMassesOn`. `MomentInitializationProbe.lean` compiles this source theorem without an added assumption. This closes the initialization attack, but not the cross-layer correspondence gap. |

The paper therefore reports two separate conclusions: active residual forcing is a proved property of the selected candidate, while the moment-interface result is a formal correspondence objection. Neither is promoted to a refutation of the final C/D existential theorem without a reachable false premise.

| CTR-021 | The `ActualParticularStageControls.raw_jets` empty branch proves arbitrary physical estimates by ex falso on a nonempty domain. | Source inspection: the branch derives `False` only from `z ∈ controlPatch`, whose first component is `Active l n` and therefore constructs an `ActivePair`; the nonempty branch uses an explicit surjection over active pairs. | Local objection not established | Audit whether the selected endpoint requires `Nonempty (ActivePair B N0)` and whether that requirement is proved. Do not call the branch a theorem-level contradiction without that reachability result. |
| CTR-022 | `MeanRankUpdate` implements the paper-shaped `FiveProfileMoments` system because it imports that file. | Source census: the operative interface in `MeanRankUpdate.lean` is exclusively `FiveRowRank.Debt`, `FiveRowRank.FiveRows`, and three-coordinate scaling; no `FiveProfileMoments` symbol is used there. | Import-only bridge not established | Locate a named transport theorem on the selected path, or report the paper-to-physical moment correspondence as unproved. |
| CTR-023 | The selected endpoint closure contains no substantive `FiveProfileMoments` implementation. | Recursive closure census finds nominal-layer uses in `NominalProfile`, `ModulatedHistories`, `ModulatedCone`, `ModulatedProfileAssembly`, `MatchingDebtBounds`, `RepairConeBounds`, and `ReservedPatches`. In `ReservedPatches`, the inspected cross-use proves nominal bump support and `FiveRowRank.background` agreement, not full row transport. | Absence claim rejected; transport gap remains | Locate and inspect a theorem equating the five nominal moment rows with `FiveRowRank.FiveRows` and mapping the debt/coefficient parameters into `MeanRankUpdate`. |

The new `FiveRowsStructureProbe.lean` result narrows the moment objection further. It corrects the review narrative's description of a generic five-by-five solve: the physical-rank file explicitly separates two zero constraints from three debt-controlled rows. The remaining audit target is the proof that those fixed constraints and the three debt rows preserve the paper's five named moments across the selected construction.

## Source-scope correction: 2026-09-23

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-019 | Direct compilation of `ComparatorChallenges/NavierStokes.lean` emits two `declaration uses sorry` warnings, at its whole-space and periodic challenge theorem declarations. | Confirmed source-tree defect; not on the exported endpoint path | The repository-wide claim “zero admitted gaps in every Lean file” is false. `ComparatorSolution.lean` does not import this challenge module, so the finding does not by itself refute the selected C/D theorem. |
| CTR-020 | `ActualCandidateAssembly.selected_witness` feeds `GluedStageEstimates.actualStageEstimates`, which consumes `ActualCycleResidualBounds.PhysicalData`; `ActualPhysicalPrefixFields.physicalFields_all` derives that data from smoothness, local germs, and exterior equality. | Positive provenance evidence | The R³ endpoint is not a disconnected wrapper. The live adverse lane remains the unproved semantic correspondence among the three moment systems. |

The source-scope correction changes the wording of the paper and peer review: the exported path is standard-axiom-only in the inspected reports, but the repository contains an unused challenge module with admitted theorem bodies. The two claims must not be conflated.

## 2026-09-23 regularity-versus-row audit

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-024 | `MovingFieldRowNonImplicationProbe.lean` proves that `GaugeMomentBalances.MovingField` can hold for the zero field while `FiveRowRank.FiveRows` fails for a nonzero debt, because the third row then reduces to `0 = -1`. | Confirmed zero-sorry interface countermodel | Smoothness, support, and periodicity are not themselves the five moment equations. The selected rank path is stronger because `LocalRankDefect.RankGeometry.fiveRows` derives the physical rows from its background, coefficient, length, velocity, and debt hypotheses. This is a proof-obligation distinction, not a refutation of the selected C/D endpoint. |

The review therefore separates two interfaces that had been too easy to conflate. Generic `MovingField` premises preserve analytic regularity and support, while `RankGeometry.fiveRows` is the theorem that supplies the physical moment identities. Any paper-to-code claim must identify where the nominal quantities `(M, I, J, S, C_p)` enter that stronger rank geometry and how their values are preserved. The new probe does not justify calling the selected rank solve absent; it rules out treating regularity alone as evidence of the solve.
