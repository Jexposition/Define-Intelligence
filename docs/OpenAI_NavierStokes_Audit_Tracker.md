# OpenAI Navier–Stokes Counter-Paper Evidence Tracker

This document is the working ledger for the counter-paper. It records evidence, status, and the next falsification test. It is intentionally a tracker. The argument itself is written in `OpenAI_NavierStokes_Research_Paper.md`.

## Base-profile and core-asymptotics audit: 2026-09-23

`finalPotential` is an axisymmetric profile in reduced coordinates `(t, s, z)`, but its spatial curl has three Cartesian components. The radial-anchor zero is a local gauge identity, not a global zero-swirl result. Genuine five-moment machinery exists upstream; the unresolved issue is the absence of a selected-path theorem transporting the named moments through the generic germ/sum interface. `force_smooth` is conditional on residual-jet limits and away extensions. `WholeDomain*` is disconnected from `selected_witness`, not globally dead.

Evidence: `NavierStokesReview/evidence/base_profile_core_asymptotics_audit_2026-09-23.md`.

**Cleared attack surface:** the pure-axial/pure-swirl collapse hypothesis is
rejected. `finalPotential` has three Cartesian components before spatial curl,
and the selected path has a divergence-free assembled field. The radial-anchor
zero is not a global component-vanishing theorem. The discarded collapse note
is not evidence against the claim.

## Scope

- Upstream source under review: OpenAI Navier–Stokes repository, snapshot recorded as `f9e8bc5`.
- Review branch: `review/cmi-first-navier-stokes-2026-09-22`.
- Formal environment: the repository-declared Lean 4.34.0-rc2 through the local elan installation. The separate V-lab `packages-4.32` cache was not substituted because this fork pins matching 4.34.0-rc2 Mathlib and Comparator revisions.
- Boundary: the OpenAI source tree is not edited. Review probes live under `NavierStokesReview/src/probes`.

## Current position

The repository contains a genuine R³ C/D-shaped endpoint and the headline theorem reports only standard Lean axioms. The strongest adverse result is a cross-layer correspondence gap, not a proof that no five-row repair exists. `FiveProfileMoments` matches the paper-shaped normalisation, `PositiveOrderMoments` proves an exact five-component recursive repair, and `FiveRowRank` supplies a distinct three-debt physical rank interface. A zero-sorry theorem rules out a direct row-by-row bridge between the first and third interfaces, but that probe is not by itself a refutation because the positive-order layer may be an intended intermediate representation. The final theorem is not labelled refuted until a false mandatory premise or an impossible selected-path correspondence is proved.

**Headline load-bearing finding: CTR-005.** The paper's named five-moment
system has not been shown by a selected-path theorem to be the same moment
data transported into the production debt, residual estimates, and public
`selected_witness`. This is the active counter-paper objection. It is a
correspondence failure under review, not yet a kernel-level contradiction.

## Pressure and uniqueness closure audit: 2026-09-24

The compact-pressure trivialisation attack is rejected as a standalone
counterexample, but the earlier wording “pressure chain cleared” was too broad.
`PressureRecovery.gradient_recovery` derives a compact-test identity for the
difference `p - q` under equal-residual comparison hypotheses;
`ActualPressureFlux` transports that difference identity to a cutoff flux;
`PressureFlux` constructs the uniform bound; and `WholeSpaceUniqueness`
consumes that bound in competitor comparison. This is a real comparison chain,
not an absolute verification of the selected pressure's global Poisson
representative or normalisation.

This does not rescue the paper's claim. The selected exported candidate still
has no inspected theorem identifying its fields, residual, and force with the
paper's named moment tuple `(M, I, J, S, C_p)`. That unproved identification is
the load-bearing correspondence failure recorded as CTR-005.

Evidence: `NavierStokesReview/evidence/pressure_uniqueness_closure_audit_2026-09-24.md`,
`NavierStokesReview/src/probes/IntermediateAxiomProbe.lean`, and
`NavierStokesReview/src/probes/R3ComparisonPremiseProbe.lean`.

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

| CTR-036 | The local paper construction, the five named moments, and the exported R³ candidate are one already-identified object. | `LocalResidualFlatness.lean` and `LocalPaperTheorem.lean` use the selected raw stages and a schedule; `ActualCandidateAssembly.selected_witness` exposes an existential schedule/extension/force assembly; `PaperLocalization.lean` proves late local velocity and pressure agreement, but the inspected result does not state force equality or transport `(M, I, J, S, C_p)` into the final comparator. | Semantic transport not established; not a kernel contradiction | Prove or refute one selected-path theorem carrying the named moment tuple and the same force through local construction, localization, and exported `selected_candidate`. |

## 2026-09-23 pressure-chain adjudication

The pressure and comparison audit was completed at source level. The generic `Filter.bot` warning remains real, but the inspected pressure-recovery path does not use an empty-filter shortcut: compact temporal tests are converted to pointwise equality on `Ioo 0 T` by continuity and an integral fundamental lemma. The harmonic-functional step is bounded by an explicit Fourier Sobolev norm before compact harmonicity is extended to the full Schwartz test space.

This closes the specific claim that the endpoint consumes a free scalar rate bound. The comparison closure constructs it internally, and the pressure-flux constant is constructed upstream from the pressure-recovery hypotheses. The chain remains analytically load-bearing, but no zero-sorry contradiction has yet been found in it.

## Formal artefacts

- `NavierStokesReview/evidence/selected_endpoint_composition_audit_2026-09-24.md`: source map for the local paper schedule, selected raw stages, exported witness, and R³ packaging.
- `NavierStokesReview/src/probes/ActualCandidateAssemblyIsolationProbe.lean`: corrected zero-sorry interface probe; it no longer claims that `PositiveOrderMoments` is dead code.

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
## 2026-09-23 actual-field and filter adjudication

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-025 | `PhysicalFields.velocity_germ` and `pressure_germ`, `StateRealization`, and `StateRealization.chartIdentity` connect the selected residual to the actual local velocity and pressure and reconstruct it in Cartesian coordinates. | Confirmed source path | The paper's updated-field recomputation requirement is represented on the selected path. The stale-background attack is not established. |
| CTR-026 | The selected `JetRate` consumer uses `GlobalBaseError.originPast`, with `originPast_before`, `originPast_tendsto`, and `originPast_q_tendsto_zero`; it is not shown to use `Filter.bot`. | Confirmed path-level result | The generic missing-`NeBot` condition remains an API hazard, but it is not a demonstrated vacuous proof of the selected endpoint. |

These findings narrow the counter-paper. The remaining formal correspondence objection is the absence of a displayed transport theorem from the published five quantities `(M, I, J, S, C_p)` into the selected physical-rank data. That objection is not to be promoted to “formal disproof” unless a zero-sorry contradiction or false mandatory premise is established.

## 2026-09-23 formal adjudication

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-027 | `MomentBridgeObstructionProbe.lean` proves that the paper-shaped exponent vectors cannot be directly identified with `FiveRowRank`, and that the associated debt spaces have no linear equivalence. | Confirmed zero-sorry adverse result | The direct Appendix-A-to-`FiveRowRank` reading is impossible. This is a paper-to-code correspondence failure, not yet a refutation of the exported endpoint. |
| CTR-028 | `PositiveOrderMoments.lean` contains a separate five-dimensional exact repair theorem. | Confirmed positive evidence | The repository has serious five-row machinery, so the correct issue is the missing identification and endpoint-use theorem, not absence of all five-row repair. |
| CTR-029 | The R3 endpoint remains standard-axiom-only in the inspected reports, while the force stays active through the singular interval. | Confirmed | The endpoint is forced and C/D-shaped; it is not established as autonomous or force-free. CMI C/D permits smooth forcing. |

The present review classification is **major revision**. A stronger `[FORMALLY REFUTED]` label is reserved for a zero-sorry contradiction or a false premise proved on the selected endpoint path.

## 2026-09-23 bridge correction

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-030 | `FiveRowPositiveOrderBridgeProbe.lean` proves that `PositiveOrderMoments.repairU` and `repairE` equal `FiveRowRank.gamma` and `deltaV` after promoting debt `(P,Jθ,Jz)` to `(0,0,-P,-Jθ,-Jz)`. | Confirmed zero-sorry constructive bridge | The direct dimension mismatch is not a repair contradiction. The remaining target is the selected-path transport of the paper's named moments into this promoted interface. |

This entry supersedes any interpretation of CTR-027 as a standalone refutation. CTR-027 remains a proof that direct row identification is impossible. CTR-030 proves the natural constrained reduced form. The live falsification threshold is now a false equality or false mandatory premise on the selected endpoint path.

## 2026-09-23 repository-wide admitted-declaration census

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-031 | A source census finds four `sorry` declarations in `ComparatorChallenges`: two in `ComparatorChallenges/NavierStokes.lean` and two in `ComparatorChallenges/Euler.lean`. | Confirmed source fact | Any repository-wide statement that every Lean file is zero-sorry is false. The challenge module header describes these as intentional standalone placeholders. |
| CTR-032 | The inspected dependency reports for `NavierStokes/R3/Theorem.lean`, `theorem_1_1`, the selected witness, and the selected stage estimates contain only `propext`, `Classical.choice`, and `Quot.sound`. | Confirmed endpoint fact | The four challenge-file placeholders are not currently shown to contaminate the exported C/D endpoint. This is a repository-scope defect, not yet an endpoint refutation. |

The counter-paper therefore makes two distinct claims. First, the repository is not globally zero-sorry. Second, the selected endpoint is standard-axiom-only in the inspected dependency reports. Collapsing those claims into either “the whole repository is admitted” or “the whole repository is fully verified” would misstate the evidence.

## 2026-09-23 selected import closure and regularity correction

| ID | New result | Status | Interpretation |
| --- | --- | --- | --- |
| CTR-033 | `SelectedImportClosureProbe.lean`, importing `NavierStokes.R3.Theorem`, resolves both `PositiveOrderMoments.Debt` and `FiveRowRank.Debt`. | Confirmed zero-sorry probe | The selected theorem's import closure contains both moment layers. Module availability is not evidence that the paper's five named moments are identified with the endpoint's debt or consumed by its residual estimates. |
| CTR-034 | Direct inspection of `ActualCandidateAssembly.selected_witness` shows the endpoint is assembled through the actual stage-estimate and germ-witness chain, but no named theorem was found there equating `(M,I,J,S,Cp)` with the promoted debt and carrying that equality into `CandidateProperties`. | Open load-bearing correspondence obligation | The correct criticism is missing endpoint transport, not absence of five-moment code. A contradiction has not been proved. |
| CTR-039 | The pressure comparison chain itself verifies absolute selected-pressure semantics. | `PressureRecoveryAbsolutePremiseProbe.lean` compiles with no `sorry`: identical zero velocities and any common smooth pressure satisfy `PressureRecovery.Hypotheses`. | Comparison limitation confirmed; selected-path contradiction not yet proved | Trace `pressure_germ` and `base_equation` into an absolute global Poisson/normalisation theorem, or derive a contradiction from the actual selected residual limits. |
| CTR-040 | The selected residual-limit route is independent of the paper's five named moments. | `selected_residual_endpoint_trace_2026-09-24.md` traces `StageEstimates.exists_schedule`, `physical_vanishingJointJets`, `GermCandidateAssembly`, and `selected_witness`; none exposes a five-moment realisation field. | Selected-path transport remains unestablished; no contradiction yet | Attempt a zero-sorry theorem connecting the named moments to `VanishingJointJets`, `haxis`, and `StateRealization.chartIdentity`, or exhibit a false selected premise. |
| CTR-035 | The proposed initial-face smoothness counterexample is invalid. `preSingularDomain = Ico 0 1 × univ` includes `t = 0`, and `ContDiffOn` is relative to that half-domain. | Withdrawn | The review must not claim that the formal candidate is only smooth for `0 < t < 1`; the source explicitly includes relative right-smoothness at the initial face. |

The active falsification lane therefore remains the semantic transport from the paper's moment names to the selected residual construction. The import probe strengthens the audit map but does not turn an unproved bridge into a contradiction.

## 2026-09-23 selected construction-interface adjudication

### Question

Does the selected endpoint obtain its convergence, residual flattening, localisation, and cone-preservation properties from proved source-linked premises, or does a final interface silently assume those properties?

### Evidence

The answer is source-backed on the inspected path. `MixedCandidateAssembly.StageEstimates` stores finite-prefix smoothness and jet-rate estimates. `ActualCycleResidualBounds.finite_residual_rates` derives the residual rates from the actual cycle invariant and `PhysicalData`. `StageEstimates.exists_schedule` derives the scale schedule and `VanishingJointJets`. `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` and `CandidateConsequences.mixed_exists_force_with_consequences` then construct the force and derive the candidate consequences.

The whole-space localisation is also not an arbitrary velocity cutoff: `SpatialLocalization.localizedVelocity_divergence_free` proves the curl-generated localisation is divergence-free, and `R3CompactCandidate` uses local residual equality. The modulated repair path derives coefficient bounds before invoking `ModulatedCone.profiles_trueCone`.

### Decision

The proposed “final theorem assumes convergence”, “cutoff destroys incompressibility”, and “cone preservation lacks quantitative smallness” objections are **not supported** by the selected source. No zero-sorry contradiction was obtained. The live criticism is narrower: the paper still needs a source-linked exposition theorem identifying its named moments with the promoted physical debt used by the endpoint, and the repository-wide zero-sorry claim remains false because of the four standalone challenge placeholders.

### Current counter-paper verdict

The research has established concrete overclaims about repository scope and paper-to-code documentation. It has not yet falsified the selected forced C/D proposition. The escalation rule remains unchanged: promote to formal disproof only after proving a contradiction or a false mandatory premise on the selected witness dependency path.

## 2026-09-23 final review correction

### Question

Are there any remaining hidden truncations in the time-localization of the blowup, vacuous active-pair statements, or hidden transport theorems that save the mathematical claim?

### Evidence

1. **Time Localization:** \CandidateProperties\ and \	imeSwitch\ (in \TimeLocalization.lean\ and \SmoothCutoffs.lean\) are mathematically sound. The cutoff equals 1 near the singular time =1$, perfectly preserving the ^\infty$ \SpeedUnboundedAtOne\ blowup without artificial truncation.
2. **Active Pair:** \ActualParticularStageControls.raw_jets\ handles the empty subtype correctly by deriving \False\ from a patch-membership hypothesis rather than a generic contradiction. It is safe from vacuous limits.
3. **Transport Theorem Absence:** A full repository \grep\ confirms that \RankGeometry.fiveRows\ (and the physical-rank interface) is entirely disconnected from \PositiveOrderMoments\ or any theorem equating them with the paper's 5 moments on the selected path.

### Decision

The earlier “absolute structural falsification” wording is withdrawn. The direct transport from the paper's named five moments to the selected endpoint remains an exposition and reproducibility obligation, but the existing constrained positive-order bridge prevents treating the type difference as a contradiction. The selected-budget issue likewise produces no endpoint refutation. The current evidence supports major revision and continued falsification work, not a formally complete disproof.

## 2026-09-23 selected-parameter audit

`ActualCandidateConstruction.selectedBudget` is definitionally `0`. The same module proves `selectedThreshold_geometry`, and `ActualCandidateAssembly.selected_witness` applies the witness theorem to the selected budget, threshold, and geometric-threshold proof. The three aliases `selectedPotentialStages`, `selectedDirectStages`, and `selectedPressureStages` are ordinary noncomputable definitions whose bodies are the corresponding stage functions.

The zero-sorry `NavierStokesReview/src/probes/SelectedBudgetProbe.lean` compiles these exact facts: the selected budget is zero, it is not positive, and the selected threshold satisfies the geometric admissibility inequality. This is a parameter audit, not a proof of the endpoint.

The value `0` is not a zero-stage truncation. The stage functions remain maps indexed by `j : ℕ`; the budget is passed into the cycle, scale, and band parameters. The source therefore does not support calling these aliases `sorry` cheats. A separate question remains open only if the human paper requires a positive budget and the formal endpoint fails to prove that requirement.

The earlier `agent_transport_obstruction.lean` probe is removed from the evidence set because its theorem was a trivial existential witness and did not express the claimed missing transport. It must not be cited as proof of failure.

## 2026-09-23 selected-stage moment bridge audit

The proposed “hardcoded zero rows” objection was checked against the source and is too strong. `FiveRowRank.FiveRows` is an explicit conjunction of five radial integral equations, including the first two zero-moment equations. `FiveRowRank.five_rows` proves those equations for the constructed repair functions. `CorrectionState.rank_rows_on_patch` and `DefectIncrementBounds.RankGeometry.fiveRows` connect the rows to actual slow base fields and preserve the corresponding masses.

The live issue is endpoint transport. `ActualCandidateAssembly.selected_witness` exposes `Witness` over three raw stage sequences. The selected aliases are ordinary functions indexed by `j : ℕ`; the endpoint result does not contain an equality to `FiveRowRank.FiveRows`, `PositiveOrderMoments.moments`, or the paper tuple `(M, I, J, S, C_p)`. A zero-sorry diagnostic probe records these exact types in `NavierStokesReview/src/probes/SelectedMomentBridgeAudit.lean`.

Status: **ZERO-ROW CHEAT ACCUSATION CLEARED; SELECTED-ENDPOINT MOMENT TRANSPORT NOT EXHIBITED**.

This is a material correspondence and reproducibility defect, not yet a formal contradiction. The next decisive test is to locate a mandatory selected-path theorem identifying the actual fields with the five paper moments, or to construct a countermodel showing that `Witness` can hold without that identity.

## 2026-09-23 residual-invariant trace

The selected residual path was checked beyond the theorem name. `CycleAnalyticInvariant` stores the analytic residual data, including the mean bounds, mean hypotheses, source and coefficient regularity, and the residual decomposition. `ActualCycleResidualBounds.Invariant.native_residual` then derives the native residual estimate by combining `H.mean_native`, the fixed base-error estimate, the axisymmetric-alias estimate, the Gaussian field estimate, the source sum, and `H.fullResidual_decomposition`.

This does not expose a `sorry`-style final premise. The subsequent `residual_jetRate` theorem consumes that derived `NativeBounds` result together with the state-realisation and base-exterior estimates. The result is a cleared suspected loophole, not a certification of the paper's physical interpretation. The live falsification target remains an exact false equality or missing transport theorem between the paper's five named moments and the promoted debt used in this chain.

## 2026-09-23 forcing-cutoff audit

The proposed step-function cutoff objection was tested against the actual R³ files. `PositiveTimeForce.timeCutoff` is a rescaled `SmoothCutoffs.cutoff`, and `timeCutoff_contDiff` proves global `ContDiff ℝ ∞` regularity. The source also proves that the cutoff is one on `[3/8,1]` and supported in `[1/16,21/16]`. The zero-sorry `ForceActivityProbe.lean` proves `timeCutoff 1 = 1`, `force f (1,x) = f (1,x)`, and a finite pointwise limit at one for every smooth `f`.

The cutoff is therefore active at the singular time but not discontinuous there. This is not a C/D failure by itself, because the R³ predicate requires a globally smooth force and only imposes the PDE identity on `0 < t < 1`.

The substantive force is residual-derived in `CandidateFromLimits.lean`: before one it agrees with the activated Navier–Stokes residual, while `SpacetimeGluing.smoothExtension` supplies the global smooth continuation. The endpoint limits `hlim` and boundary jet `L` are real obligations constructed upstream from `VanishingJointJets` and away-extension data. The present audit found no theorem proving force-norm divergence and no failed smooth-extension obligation. The remaining adverse claim is semantic and mathematical adequacy: residual feedback must be distinguished from a forced C/D predicate, and any refutation now requires a zero-sorry failure of the selected residual limits, smoothness, support, or decay.

Status: **SMOOTH ACTIVE CUTOFF CONFIRMED; RESIDUAL-FEEDBACK CONCERN CONFIRMED; C/D FORCE FAILURE NOT YET PROVED**.

## 2026-09-23 force-conservation proposal

The proposed counter-force test was adjudicated against the actual CMI predicate. Neither zero spatial integral of the external force nor `∇ · f = 0` is required by the forced alternatives. `PositiveTimeForce.force` is only a smooth time-cutoff wrapper; the pressure term enters through `navierStokesResidual` in `CandidateFromLimits`. Therefore a nonzero net external force or nonzero force divergence would not, by itself, refute the formal C/D statement.

The valid remaining test is stricter: prove, on the selected path and without `sorry`, that the residual-derived force fails one of the predicates actually required by the repository: global smoothness, positive-time support, rapid derivative decay, PDE equality, or finite-energy consequences. Evidence: `NavierStokesReview/evidence/force_conservation_obstruction_adjudication_2026-09-23.md`.

## 2026-09-23 external regularity result

Constantin, Ignatova, and Vicol analyse the OpenAI construction's reported anisotropic angular-mean bounds and exact axisymmetric core. Their theorem gives regularity for analytic forcing; their corollary says that, under the same structural properties and a force bounded in local `C²` up to the singular time, the force cannot be analytic or vanish near the singular point. They identify the OpenAI force as smooth but nonanalytic, which is consistent with its compactly supported cutoff.

This is strong independent evidence that the construction occupies a contrived, nonanalytic forced branch. It is not a formal refutation of Alternative C because the CMI statement asks for smooth rapidly decaying forcing, not analytic forcing. The review must cite this as a method limitation and continue the selected-path predicate audit.

## 2026-09-23 analytic objection probes

The counter-paper now tracks three additional source-connected lanes.

**Incompressibility.** `selectedPotentialStages` are intermediate potentials.
The final selected velocity is assembled through the solenoidal construction,
and `SelectedDivergenceAudit.lean` compiles without `sorry` while extracting
`hc.divergence_free` from the selected witness. The raw-stage divergence
objection is therefore closed as a category error.

**Energy.** `R3/ViscousEnergyBalance.lean` contains an exact Newtonian balance
with forcing work and viscous dissipation, and `R3/CompactEnergy.lean` derives
the corresponding time-derivative theorem. The selected endpoint exposes a
uniform finite-energy field. No selected-field energy mismatch has been proved;
the next test must instantiate the identity on the actual endpoint rather than
infer a mismatch from the moment-system narrative.

**Pressure and temporal gluing.** The selected R³ predicate explicitly requires
compact support for each pre-singular pressure slice, and the construction
obtains it through `SpatialLocalization.cutPressure`. This is a serious
modelling and paper-correspondence question, but it is not automatically a CMI
contradiction because the external force is unrestricted by `div f = 0`. The
temporal force interface is constructed by `SpacetimeGluing.smoothExtension`
and exposes all endpoint jets; the live falsification target is whether the
selected path supplies the residual limits consumed by that theorem.

Evidence: `NavierStokesReview/src/probes/AnalyticObjectionsProbe.lean` and
`NavierStokesReview/evidence/selected_divergence_audit_2026-09-23.md`.

## 2026-09-23 filter non-vacuity audit

`DiagonalResidual.JetRate` is a generic existential bound and does not require a `NeBot` instance. That is a legitimate review hazard for lemmas used with arbitrary filters. The selected endpoint, however, uses `nhdsWithin (1, x) (SpacetimeEndpoint.openPast 1)`, and `JointResidualLimits.past_filter_neBot` proves this filter non-vacuous by rewriting it as a one-sided time neighbourhood times a spatial neighbourhood. `FilterNonVacuityAudit.lean` compiles with no `sorry` and instantiates the theorem at the selected origin.

**Finding:** the generic API is under-guarded, but selected-endpoint vacuity is not established. Restricted or comap filters introduced later remain individually auditable.

## 2026-09-23 pressure-support scan

The proposed non-local-pressure objection was checked against the actual source tree. `SpatialLocalization.cutPressure` and `R3CompactCandidate.localized_pressure_tsupport` explicitly impose compact spatial pressure support in the selected construction. However, the repository also contains substantive compact-test pressure identities: `ConservativeDifference.weak_pressure_poisson`, `PressureRecoveryHelpers.gradient_poisson_test`, `PressureRecovery.pressure_gradient_recovery`, and Riesz test-operator identities.

The current result is therefore a live correspondence question, not a formal contradiction. The decisive test is whether those recovery results can be instantiated for the selected candidate, or whether their equal-residual comparison hypotheses are absent from the selected path. Evidence: `NavierStokesReview/results/pressure_support_scan_2026-09-23.txt`.

## 2026-09-23 semantic transport and pressure-slice audit

The production rank path is now mapped more precisely. `FiveRowRank.Debt` is
`Fin 3 → ℝ`, and `FiveRows` fixes two correction moments to zero while the
remaining three rows consume the three defect coordinates. The repository
also contains a genuine `PositiveOrderMoments.Debt := Fin 5 → ℝ` exact repair.
The zero-sorry `FiveRowPositiveOrderBridgeProbe` proves the explicit
promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)` reproduces the three-debt repair.

This corrects the earlier stronger claim that no five-row repair exists. The
remaining adverse finding is narrower and stronger: the source audit has not
located a selected-path theorem identifying the paper's `(M,I,J,S,C_p)` with
the promoted vector and carrying that identity into
`StateRealization.chartIdentity`, `CandidateConsequences`, and the public
`selected_witness`. This is an unresolved load-bearing correspondence, not a
kernel contradiction by dimension alone.

The pressure audit distinguishes support from recovery. `CandidateProperties.pressure_support`
is a support inclusion in whole-space R³, not a pressure-Poisson axiom. The
earlier wording that selected pressure recovery had not been instantiated is
withdrawn: `WholeSpaceUniqueness.classical_uniqueness_on_Icc` constructs
`PressureRecovery.Hypotheses` and calls
`PressureFlux.exists_uniform_actual_pressure_flux_bound`; its
`candidate_unique_on_Icc` wrapper supplies the selected candidate properties.
The zero-sorry `SemanticTransportPressureProbe` still proves that compact
support alone does not force a pressure slice to vanish. No pressure
trivialisation loop has therefore been proved.

Evidence:
`NavierStokesReview/evidence/semantic_transport_pressure_audit_2026-09-23.md`,
`NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean`.
The selected-instantiation correction is recorded in
`NavierStokesReview/evidence/pressure_recovery_selected_instantiation_2026-09-23.md`.

## Axis scope and 5D target extraction: 2026-09-24

The source audit separates three facts:

1. `PositiveOrderMoments` defines genuine five-coordinate radial integrals
   and proves exact one-step repair.
2. `FiveRowRank` defines a separate `Fin 3 → ℝ` debt interface. Its
   `FiveRows` predicate explicitly proves two zero preservation rows and
   three debt rows, rather than hiding those rows in a type alias.
3. The selected endpoint still exposes no theorem identifying either system
   with the selected velocity, pressure, residual, or force.

The exact promotion is recorded in
`physical_transport_bridge_spec_extraction_2026-09-24.md`. Its zero-sorry
probe proves algebraic compatibility of the repair formulas only. It does
not prove selected-field transport.

The axis audit proves that `StateRealization.chartIdentity` requires a
nonzero radius and that `graphSourceTZ` requires positive radius. It therefore
does not itself cover the origin used by `origin_blowup`.
`GlobalBaseError.actual_error_vanishingJointJets` supplies a separate origin
error-limit route, so the axis exclusion is a correspondence gap and not yet
`False`.

**Status:** 5D target extracted; selected transport unresolved; selected-path
contradiction not established.

Evidence: `NavierStokesReview/evidence/state_realization_axis_scope_audit_2026-09-24.md`.

## Document-control audit: 2026-09-23

The active evidence surface is the fork `Define-Intelligence-github/docs`.
Parent-directory copies are archival, and supporting notes are subordinate to the
source-backed corrections recorded here. The disposition table and merge rule
are maintained in [`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md).

The current audit boundary is deliberately narrower than several early notes:
the selected construction has genuine five-moment machinery upstream, but the
generic germ/stage interface does not yet expose a theorem transporting the
paper's named moments into the selected velocity, pressure, residual, and force
endpoint. This remains the principal correspondence objection. It is not yet a
zero-sorry contradiction.

The following prior objections remain quarantined unless new source evidence is
found: global pure-axial collapse, automatic pressure trivialisation from
compact support, selected-path `Filter.bot` vacuity, force nonsmoothness from
residual definition alone, and the claim that all `WholeDomain*` files are
globally dead.

The pure-axial collapse is specifically **cleared/rejected** by the source
definition and `BaseProfileCoreAsymptoticsProbe.lean`: the profile is reduced
in coordinates but the potential has three Cartesian components, and the
final velocity is generated by spatial curl.

## Release-control verification: 2026-09-24

The authority map and tracker are aligned. The six core review documents are
present in the fork `docs/` directory, the three supporting notes are subordinate
supporting material, and no tracked `.olean` or `.lake` artefact is present.
The transitive-import recheck also corrected stale supporting-note language:
`ActualCandidateAssembly` reaches `FiveProfileMoments` and `FiveRowRank` through
`InitialPhysicalData` and `MeanRankUpdate`, and reaches `PositiveOrderMoments`
through the physical-prefix/profile chain. This is a packaging and source-map
correction, not a new mathematical contradiction. `CTR-005` remains open
pending an explicit selected-path moment-realisation theorem.

## Confirmed interface countermodel: 2026-09-24

`StageEstimates` is now formally shown to be blind to the paper's physical
content. The zero-sorry probe
`NavierStokesReview/src/probes/StageEstimatesMomentBlindnessProbe.lean`
constructs a nonempty `StageEstimates` instance with identically zero velocity
and pressure stages, zero losses and residuals, and a divergent scalar gain. The
same probe proves that the resulting zero velocity is not
`SpeedUnboundedAtOne`.

This confirms an interface-level failure: the generic rate-contract structure
does not encode the five named moments or blow-up. It does not by itself refute
the selected endpoint, because `selected_witness` adds separate physical-data,
base-profile, axis-preservation, and origin-growth premises. The headline
`CTR-005` therefore strengthens from “missing exposed transport” to “the
generic StageEstimates interface admits a machine-checked zero-field
countermodel”; the full selected-path five-moment transport remains
unestablished.

Evidence: `NavierStokesReview/evidence/stage_estimates_moment_blindness_2026-09-24.md`.

## CTR-039: the generic stage contract does not determine five debt

`StageEstimatesMomentBlindnessProbe.interface_does_not_determine_five_debt`
is a zero-sorry theorem showing that the generic stage record cannot determine
an arbitrary `PositiveOrderMoments.Debt`. This formally strengthens CTR-005:
the rate interface carries no five-coordinate payload. It remains an
interface-level result. The selected endpoint can still supply additional
field-level premises, so this theorem alone does not derive `False` from
`selected_witness`.

**Status:** confirmed interface obstruction; selected-path contradiction open.

## Pressure-chain verification: 2026-09-24

The pressure-trivialisation attack remains open and is being strengthened.
`CandidateProperties.pressure_support` is only a compact-support inclusion;
`PressureRecovery` and `ActualPressureFlux` recover comparison identities from
equal-residual hypotheses. No global pressure-Poisson/Leray equation for the
selected fields is exposed in the R3 candidate record. This is not a reason to
clear the attack. It identifies the premise that must be added before the
support/topology contradiction can be proved.

The load-bearing target is explicit: formalise the global pressure identity for
the selected fields and test it against the compact pressure slices and the
selected velocity cross-terms. Until that is done, the pressure route is
unresolved, not rejected.

Evidence: `NavierStokesReview/evidence/pressure_recovery_chain_audit_2026-09-24.md`.

The three-vector adversarial attack is recorded in
`NavierStokesReview/evidence/selected_witness_falsification_attacks_2026-09-24.md`.
The zero-sorry `SelectedWitnessInhabitationProbe.lean` proves the selected
`Witness` envelope can be paired with an arbitrary nonzero five-debt payload
because no such payload occurs in the type. This is the strongest current
type-level inhabitance obstruction; a field-level moment violation remains the
next target.

The new zero-sorry comparison-interface probe changes the pressure conclusion's
scope. `PressureRecoveryAbsolutePremiseProbe.lean` proves that the comparison
record accepts identical zero velocities and any common smooth pressure. Thus
the recovery chain can establish identities for pressure differences without
establishing an absolute global Poisson representative for the selected
pressure. This is a live selected-path limitation, not yet a contradiction,
because the endpoint may supply stronger information through `pressure_germ`,
`base_equation`, and the residual-limit construction. Those links must be
 proved before the pressure chain can be called closed.

Evidence: `NavierStokesReview/evidence/physical_transport_bridge_spec_extraction_2026-09-24.md`,
`NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean`.

The selected residual trace records the complementary endpoint fact:
`StageEstimates.exists_schedule` derives `VanishingJointJets` from rate
estimates, and `selected_witness` consumes that result, but the public chain
does not expose the paper's five named moments as premises of that residual
limit. This strengthens CTR-005 as a selected-path correspondence objection;
it does not permit a formal-contradiction label without a false selected
premise.

Evidence: `NavierStokesReview/evidence/selected_residual_endpoint_trace_2026-09-24.md`.

The selected-path ledger now records the exact projection through
`ActualCandidateAssembly.Witness`, `R3ActualCandidate.selected_compact_candidate`,
`R3/ActualCandidate.of_localized_fields`, and `R3/Theorem`.  The zero-sorry
`SelectedWitnessPathProbe.lean` confirms that this path carries the residual,
support, divergence, energy, and blow-up records but no five-moment equality.
This keeps CTR-005 load-bearing and leaves the force-jet, pressure-Poisson,
and field-level moment attacks active.

Evidence: `NavierStokesReview/evidence/selected_witness_path_ledger_2026-09-24.md`.

## Upstream five-moment chain: corrected finding

The five-moment construction is live upstream, not dead code. A zero-sorry
probe confirms that `GlobalStressSupport.moments_zero` is transported through
`EntranceAlignedBase.aligned_moments_zero`, the modulated finite-identity chain,
and `FinalSlowBase.finiteIdentities`; the same constructed base also supplies
`FinalSlowBase.speedUnbounded`. The earlier “complete disconnection” wording is
withdrawn.

The unresolved CTR-005 objection is more precise: the final mixed sums consumed
by `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` are
accepted through generic `StageEstimates` and local physical-field data, but no
source-linked theorem was located that identifies those mixed fields with the
repaired five rows `(M,I,J,S,C_p)` and carries that equality into the residual,
pressure, and force endpoint. This is an endpoint transport gap, not a claim
that the upstream repair algebra is absent.

Evidence: `NavierStokesReview/evidence/selected_base_moment_chain_reaudit_2026-09-24.md` and
`NavierStokesReview/src/probes/SelectedBaseMomentCompatibilityProbe.lean`.

## Selected residual lower-bound attack: 2026-09-24

The force-smoothness attack now has a zero-sorry formal obstruction theorem.
`NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean`
proves that the selected origin blow-up and flat residual jets are incompatible
with any eventual estimate

$$c\lVert u(t,0)\rVert \leq \lVert \mathcal R(u,p)(t,0)\rVert,$$

for a fixed $c>0$. The source path currently proves upper `JetRate` bounds for
residual derivatives. No field-level positive lower bound has been located in
`ActualCycleResidualBounds`, `PhysicalResidualJetBounds`, or
`CandidateFromLimits`. This leaves FJ-01/FJ-05 open and identifies the exact
theorem still required for a formal refutation.

Evidence: `NavierStokesReview/evidence/selected_residual_lower_bound_obstruction_2026-09-24.md`.

## Direct selected-witness falsification board: 2026-09-24

The three attacks are now tracked against the actual selected endpoint. The
force route has a proved conditional contradiction, not a clearance: a fixed
positive velocity-to-residual lower bound would conflict with residual flatness
and origin blow-up, but the source has not supplied that lower bound. The
pressure route remains open because compact support is not itself a Poisson
contradiction. The moment-blindness result is an interface countermodel only;
it does not yet evaluate the concrete selected fields.

Evidence: `NavierStokesReview/evidence/selected_witness_boundary_attack_status_2026-09-24.md`.

## Selected-witness attack-boundary result: 2026-09-24

`SelectedWitnessAttackBoundaryProbe.lean` compiles without `sorry` and fixes
the logical strength of the current adverse result. It proves

$$
\neg(\texttt{Witness}\Rightarrow
\forall d:\mathrm{Fin}(5)\to\mathbb R,\ d=0),
$$

because the exported witness contains no five-debt field or equality. It also
constructs a scalar endpoint countermodel in which one quantity tends to
infinity while another tends to zero. Therefore the proposed force attack
still requires a selected-field lower bound linking velocity to residual; the
source's velocity blow-up and residual-flatness predicates do not provide that
bound by themselves.

**Status:** confirmed interface obstruction and attack boundary; selected-path
formal contradiction remains open.

Evidence: `NavierStokesReview/evidence/selected_witness_attack_boundary_2026-09-24.md`.

## Selected-witness endpoint residual probe: 2026-09-24

The exact force attack is now formalised against the selected witness rather
than an arbitrary residual. `SelectedWitnessEndpointResidualProbe.lean`
extracts the selected `CandidateProperties`, proves that the interior residual
equals the selected force, and proves `False` from three eventual facts: the
origin speed tends to infinity, the selected force is locally bounded, and a
fixed positive lower bound carries velocity size into residual size.

The first two facts are available from the endpoint interface. The third is
not currently exported by the selected source. `FinalSlowBase` instead
contains a residual decomposition with flat error/core-stress terms, so the
review must determine whether the lower bound is mathematically true or is
destroyed by the construction's cancellation. This is a conditional formal
contradiction, not a clearance and not yet an unconditional refutation.

Evidence: `NavierStokesReview/evidence/selected_witness_endpoint_residual_probe_2026-09-24.md`.

The probe was strengthened after the initial conditional result. It now
extracts the selected schedule itself, proves origin speed blow-up for the
selected mixed velocity, and proves that the corresponding selected mixed
residual tends to zero. Therefore a fixed positive lower bound from velocity
size to that residual is formally impossible. This is evidence of the
construction's cancellation mechanism, not a force-singularity theorem. The
remaining composition question is whether this raw residual is identified
with the final force at the origin, rather than only with the interior force
identity.

The axis-scope audit was independently rechecked. `selected_residual_jetRate`
does not merely juxtapose unrelated estimates: it splits on `w ∈ S`, uses the
off-axis chart bound on `S`, and uses `houtside` plus `base_exterior_jetRate`
on `Sᶜ`. The positive-radius restriction is a scope limitation and a missing
origin semantic bridge, not a proved derivative discontinuity.
