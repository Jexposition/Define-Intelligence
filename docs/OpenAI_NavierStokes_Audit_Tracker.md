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

The repository contains a genuine R³ C/D-shaped endpoint and the headline theorem reports only standard Lean axioms. The primary adverse result is that the published five-moment/CMI claim is **not established** by the inspected paper-to-endpoint record: the authors have not supplied the selected-field composition theorem that their stronger explanation requires. This is not softened by the fact that a separate zero-sorry attack has not yet derived `False`. `FiveProfileMoments` matches the paper-shaped normalisation, `PositiveOrderMoments` proves an exact five-component recursive repair, and `FiveRowRank` supplies a distinct three-debt physical rank interface. A zero-sorry theorem rules out direct row-by-row identification between the first and third interfaces, while the positive-order layer may be an intended intermediate representation. The literal endpoint is therefore not labelled formally refuted, but the published claim is not accepted pending affirmative proof of the missing transport.

**Headline load-bearing finding: CTR-005.** The paper's named five-moment
system has not been shown by a selected-path theorem to be the same moment
data transported into the production debt, residual estimates, and public
`selected_witness`. This is the active counter-paper objection. It is a
correspondence failure under review, not yet a kernel-level contradiction.

This is a failure to discharge the authors' proof burden, not a presumption
that the missing bridge is true. “Not formally refuted” is a separate,
subordinate status for the narrower question whether the current review has
derived `False` from the selected endpoint. The active review verdict is
negative on the published claim until the selected-path bridge and its
analytic premises are shown. The reviewer is not required to construct the
authors' missing affirmative proof before reaching that conclusion.

## Response-claims clarification: 2026-09-24

The supplied technical summaries are broadly consistent with the source, but
four distinctions are mandatory when quoting them:

1. `FiveRowPositiveOrderBridgeProbe.lean` proves an algebraic repair identity
   under the promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)`. It does not prove that
   the selected Cartesian fields realise `(M,I,J,S,C_p)` or that the equality
   survives the selected residual and force pipeline.
2. The residual-defined force is compatible with the repository's formal
   existential predicate. Calling that “CMI compliant” would overstate the
   result: force provenance and the meaning of “given, externally applied” are
   not encoded as an independence axiom in `CandidateProperties`.
3. The origin cancellation result is local. Interior residual equality holds
   for `0 < t < 1`, the endpoint is a smooth extension, and the selected force
   tends to zero at the origin. This is not a global statement that the force
   vanishes or is nonzero at every point at time one.
4. Generic zero-velocity and five-debt probes test interface non-implication;
   they do not show that the selected witness is empty or zero. The selected
   primary label and active pair now have explicit zero-sorry witnesses.

The exact claim-by-claim record is
`NavierStokesReview/evidence/response_claims_adjudication_2026-09-24.md`.

## Build verification: 2026-09-24

The declared toolchain was rerun after the review-document updates:

| Target | Result |
| --- | --- |
| `lake build NavierStokesReview` | 3,688 jobs completed successfully |
| `lake build NavierStokes` | 9,580 jobs completed successfully |
| Exported comparator axiom report | `propext`, `Classical.choice`, `Quot.sound` only |

This verifies compilation and dependency hygiene for the inspected targets. It
does not discharge CTR-005 or convert the endpoint into a proof of the paper's
selected five-moment semantics.

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
| CTR-005 | The complete Lean pipeline is one coherent implementation of the paper's five-moment system. | `FiveProfileMoments.lean` matches the paper-shaped vectors; `PositiveOrderMoments.lean` proves exact five-component repair; `FiveRowRank.lean` declares a distinct three-debt interface. `NavierStokesReview/evidence/mean_rank_update_scope_2026-09-24.md` and `MeanRankUpdateAudit.lean` confirm that the two zero rows constrain `dv` and `ga`, not total energy, while the selected endpoint still exposes no five-moment transport equality. | Cross-layer correspondence not established | Identify the explicit staging maps and verify that the selected witness preserves all five named moments. |
| CTR-006 | The moment interfaces are accidentally being treated as the same object. | `MeanRankUpdate` consumes `FiveRowRank`; `ModulatedHistories` and `ReservedPatches` consume `FiveProfileMoments`; `GlobalSlowProfiles` consumes `PositiveOrderMoments`. | Direct-identification objection supported; endpoint refutation not established | Keep the direct obstruction, but audit the positive-order and nominal-to-physical maps before escalation. |
| CTR-007 | Non-Newtonian regularisation disproves the Newtonian theorem. | The published endpoint is Newtonian and C/D allows smooth force. | Rejected as internal refutation | Retain only as a physical robustness limitation. |
| CTR-008 | The two moment declarations may be treated as the same system by direct identification. | `MomentBridgeObstructionProbe.lean` proves `¬ DirectMomentBridge lam b` for all real `lam` and `b`, by evaluating the first axial coordinate. | Formally disproved at the direct-correspondence level | Require an explicit nontrivial change-of-variables theorem. |
| CTR-009 | The selected witness hides a custom axiom at the stage-estimate interface. | `SelectedDependencyAxiomProbe.lean` reports only `propext`, `Classical.choice`, and `Quot.sound` for `selected_witness`, `physicalData`, `actualStageEstimates`, and `Invariant.residual_jetRate`. | Closed for custom-axiom suspicion | Continue semantic and interface audit; do not treat standard axioms as defects. |
| CTR-010 | The two debt interfaces admit a direct full linear identification. | `MomentBridgeObstructionProbe.lean` proves `¬ Nonempty (FiveRowRank.Debt ≃ₗ[ℝ] FiveProfileMoments.Debt)` by finite-dimensional rank. | Formally disproved for full linear identification | Require an explicit constrained embedding or stage-separation theorem. |
| CTR-011 | The repository lacks an exact five-equation repair. | `PositiveOrderMoments.weighted_moments_exact`, `moments_repair_target`, and `exists_smooth_exact_repair` prove exact five-component repair; `GlobalSlowProfiles.profiles_moments` carries it into the recursive sequence. | Rejected by source inspection | Do not repeat the obsolete “three-equation approximation” claim. Audit cross-layer correspondence instead. |
| CTR-012 | The exported whole-space endpoint is disconnected from the selected construction. | `R3/Theorem.lean` obtains its fields from `ActualCandidateAssembly.selected_witness`, localises them through `R3/ActualCandidate.of_localized_fields`, proves the compact energy estimate, and transports viscosity by `R3/ViscosityScaling`. | Closed as an objection | Treat the R³ endpoint as connected to the selected witness; keep the adverse case focused on the missing moment correspondence. |

| CTR-016 | The whole-space comparison theorem imports an unproved scalar rate bound as an endpoint premise. | `R3/WholeSpaceComparisonClosure.lean` constructs the rate bound internally through `ComparisonRateBound.exists_uniform_rate_bound`. `R3/WholeSpaceUniqueness.lean` constructs the pressure-flux estimate through `PressureFlux.exists_uniform_actual_pressure_flux_bound`. `R3ComparisonPremiseProbe.lean` records the internal rate-bound construction. | Withdrawn as stated | The rate-bound interface is not an external premise. The remaining audit target is whether the pressure-recovery and localised PDE estimates prove their stated hypotheses with the intended whole-space meaning. |

| CTR-017-PRESSURE | The pressure/uniqueness chain may hide a vacuous or imported comparison premise. | `PressureRecovery.gradient_recovery_complex` uses explicit compact temporal tests; `HarmonicTestFunctionals.eq_zero_of_compact_harmonic` uses a Fourier Sobolev bound; `WholeSpaceComparisonClosure` constructs the scalar rate bound; selected-path axiom probes report only standard axioms. | Not substantiated in the inspected path | Preserve the pressure chain as a live mathematical audit target, but do not call it a formal failure without a concrete false identity or mandatory unprovable premise. |

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
| CTR-019-SRC | Direct compilation of `ComparatorChallenges/NavierStokes.lean` emits two `declaration uses sorry` warnings, at its whole-space and periodic challenge theorem declarations. | Confirmed source-tree defect; not on the exported endpoint path | The repository-wide claim “zero admitted gaps in every Lean file” is false. `ComparatorSolution.lean` does not import this challenge module, so the finding does not by itself refute the selected C/D theorem. |
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
| CTR-029 | The R3 endpoint remains standard-axiom-only in the inspected reports, while the force is residual-driven on the interior interval and extended smoothly at the endpoint. | Confirmed with scope | The endpoint is forced and C/D-shaped; this does not establish autonomous or force-free collapse. At the origin the selected force tends to zero, so “active through the singular interval” must not be read as a global pointwise nonzero claim. CMI C/D permits smooth forcing. |

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
3. **Transport Theorem Absence:** The direct residual-bound interface does not
   expose a theorem equating `RankGeometry.fiveRows` or the other physical-rank
   data with the paper's five moments on the selected path. The transitive
   closure does contain both rank and positive-order machinery, so this is a
   missing selected-endpoint transport theorem, not global disconnection.

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

## Selected force-origin composition: 2026-09-24

`SelectedForceOriginCompositionProbe.lean` now compiles with zero errors and no
admitted declarations. It extracts the actual selected witness and proves the
late-time chain

$$
f(t,0)=\mathcal R_{\mathrm{periodic}}(t,0)
       =\mathcal R_{\mathrm{original}}(t,0)
$$

eventually as (t\to1^-). The selected `VanishingJointJets` premise therefore
implies

$$
\lVert f(t,0)\rVert\to0.
$$

This closes the proposed force-explosion route. The selected velocity still
has unbounded origin speed, so a fixed positive lower bound from velocity norm
to residual norm is impossible; however, no such lower bound is a premise of
the exported endpoint. The result is evidence of deliberate residual
cancellation, not a formal disproof.

**Status:** selected force composition confirmed; force-singularity attack
closed; CTR-005 remains the load-bearing moment/pressure transport objection.

Evidence: `NavierStokesReview/evidence/selected_force_origin_composition_2026-09-24.md`.

## Vanishing-jets and localisation trace: 2026-09-24

The selected flat residual is not supplied as a truncated `H^3` assertion.
`JointResidualLimits.VanishingJointJets` quantifies over every natural
derivative order. The selected chain fills its finite residual-rate field from
`ActualCycleResidualBounds.Invariant.residual_jetRate`, passes it through
`finite_residual_rates` and `ActualStageEstimates.stageEstimates_of_representations`,
and invokes `StageEstimates.exists_schedule` to obtain the all-order jet limit
in `MixedDiagonalResidual.exists_physical_schedule_residual_zero`.

The time switch is globally smooth, becomes identically one for `t ≥ 3/4`,
and has zero positive-order derivatives on the late side. The late activation
lemmas prove local spacetime equality. The spatial periodic/cut/original
identities likewise compare the complete Navier–Stokes residual through local
equalities, preserving the time derivative, advection, Laplacian, and pressure
gradient terms. No dropped Cartesian component or off-diagonal advection term
was found.

The localisation layer has no debt-vector parameter and does not mention
`FiveRowRank`, `PositiveOrderMoments`, or `(M,I,J,S,C_p)`. This is a precise
debt-blind interface finding, not a proof that the selected fields violate the
moment equations. It reinforces CTR-005 because the missing selected moment
transport is not supplied by the cutoff identities.

Evidence: `NavierStokesReview/evidence/vanishing_joint_jets_and_localisation_trace_2026-09-24.md`.

## 2026-09-24 pressure and mirror-force adjudication

The proposed equal-and-opposite pressure argument was tested against the
actual residual operator. `CandidateFromLimits.force` and the R3 candidate
predicate use the full residual, including the pressure gradient. The compiled
probe `PressureResidualNonCancellationProbe.lean` proves the perturbation
identity and its zero-velocity special case

$$
\mathcal R(0,q)-\mathcal R(0,0)=\nabla q.
$$

Consequently, a nonzero pressure gradient changes the force residual; the
operator does not force it to cancel. The pressure-recovery chain compares two
fields with equal residuals and does not impose `div f = 0` or an absolute
selected-field Poisson representative. The pressure semantic bridge remains
open, but the proposed annihilation theorem is not supported.

The mirror construction `mirrorForce := fun z => -f z` was also compiled in
`MirrorForceSymmetryProbe.lean`. Negation preserves smoothness, but it defines
a different forced problem. For the same velocity and pressure to satisfy both
the original and mirror equations, the source proves `f = -f` pointwise. The
whole-space uniqueness theorem compares solutions with the same force; it does
not compare the solutions for `f` and `-f`. Therefore mirror forcing supplies
no contradiction to the original existential C/D claim.

Evidence: `NavierStokesReview/evidence/pressure_residual_non_cancellation_2026-09-24.md`,
`NavierStokesReview/evidence/mirror_force_symmetry_2026-09-24.md`.

## 2026-09-24 official force-independence check

The official Fefferman statement describes `f(x,t)` as a given, externally
applied force and requires the stated smoothness and decay bounds. Its C/D
claims nevertheless quantify over the existence of a smooth force; the text
does not add a formal independence predicate forbidding a witness construction
that defines `f` from selected `u` and `p`. The CMI prize rules likewise govern
publication and evaluation procedure, not an additional causal axiom for the
PDE.

The repository therefore has a substantial paper-to-model causality objection:
`CandidateFromLimits.force` is residual-designed rather than an independently
specified forward datum. That can invalidate a claim that the construction
models an independently driven physical experiment, but it is not by itself a
formal contradiction to the literal existential C/D proposition. The decisive
remaining question is whether the selected fields satisfy every stated
predicate and whether the paper's stronger causal interpretation is part of
the theorem being claimed.

Evidence: `NavierStokesReview/evidence/cmi_force_independence_adjudication_2026-09-24.md`.

## CTR-012: fixed-force perturbation and structural duality

The official statement's description of a “given, externally applied force”
supports a causal correspondence objection because the repository constructs
its final force from the selected residual. The zero-sorry
`IndependentDataPerturbationProbe` makes the objection exact: if (p) and (f)
are held fixed after replacing (u) by (u+e), then

$$
\partial_t e-\Delta e+(u\cdot\nabla)e+(e\cdot\nabla)u+(e\cdot\nabla)e=0.
$$

The extension theorem packages the pointwise obstruction for
`PositiveTimeForce.force`. The structural duality probe separately proves that
`-f` is smooth, reverses the local work pairing, and cancels `f` pointwise.

The probe also supplies an explicit field `eₐ(t,x) = (t-t₀) • a`. It proves
`ContDiff ℝ ∞` smoothness, zero spatial divergence, and a fixed-force defect
equal to `a` at `t₀`; hence every nonzero `a` breaks the same-force equation.
This is an operator-level countertest, not yet an admissible finite-energy,
compactly supported perturbation of the selected whole-space witness.

**Status:** [x] operator-level fixed-data and mirror identities proved;
[~] selected schedule fracture and C/D `False` remain unproved. No theorem yet
supplies an admissible perturbation of the selected witness or identifies a
solution for `-f` or zero force with the selected solution.

Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`;
`NavierStokesReview/evidence/mirror_force_symmetry_2026-09-24.md`.

### Compact perturbation closure

`NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` now
supplies the missing localisation for the fixed-force test. The source defines
a compactly supported smooth potential and its curl at lines 12--72, proves
slice compact support at lines 96--105, and proves exact divergence freedom at
lines 107--121. At the switch time, the perturbation's temporal derivative is
the curl field while its value, spatial derivative, and spatial Laplacian
vanish (lines 123--160). The origin curl is the nonzero first coordinate vector
(lines 162--183).

The theorem `compactPerturbation_breaks_any_fixed_force_at_origin` (lines
185--226) proves that a base identity `navierStokesResidual u p = f` cannot
also hold for the perturbed velocity with the same pressure and force. This is
a zero-sorry operator-level fixed-data obstruction with spatial localisation.
It does not prove that the original existential C/D witness is impossible,
because the endpoint theorem does not quantify over perturbations.

**Status:** [x] compact, smooth, divergence-free fixed-force obstruction;
[~] selected-witness contradiction and schedule failure remain open.

Evidence: `NavierStokesReview/evidence/compact_fixed_force_perturbation_2026-09-24.md`.

### Compilation coordinates

The current `IndependentDataPerturbationProbe.lean` source records smoothness
and divergence freedom at lines 26--34, the exact residual identity at
36--66, the general impossibility theorem at 68--84, the corrected derivative
calculation at 96--99, and the concrete fixed-force failure at 111--150. These
coordinates supersede earlier shorthand line references after the derivative
proof was repaired. The compact localised theorem compiles separately in
`CompactFixedForcePerturbation.lean`, with its final obstruction at lines
185--226.

### Release verification record: 2026-09-24

The current review branch is synchronised at `d2e6be7`, with `967da70` as the
immediate parent containing the earlier affine-time theorem. The current
`IndependentDataPerturbationProbe.lean` compile completed with Lean 4.34.0-rc2
at exit code 0. The review-module scan found no `sorry`, `axiom`, or `unsafe`
declarations; the tracked-artifact scan found no `.olean`, `.ilean`, or `.lake`
files. `git diff --check` also passed.

The historical references to lines 25, 30, 85, 96, and 121 are preserved for
traceability only. The authoritative current ranges are 26--34, 36--66,
68--84, 86--109, and 111--151. The compact localised theorem's final
obstruction is at lines 185--226 of
`NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean`.

This evidence establishes a fixed-data operator obstruction. It does not, by
itself, prove that the literal existential C/D proposition is contradictory:
the selected endpoint does not quantify over the perturbation used by the
probe. CTR-005 therefore remains the principal selected-endpoint
correspondence objection, while CTR-012 records the independently verified
path-dependence result.

## 2026-09-24 selected-closure moment census

The dependency audit was rerun from `NavierStokes/ActualCandidateAssembly.lean`.
The local `NavierStokes.*` import closure contains 507 reachable modules, with
literal occurrence counts of 154 for `PositiveOrderMoments`, 146 for
`FiveProfileMoments`, 104 for `FiveRowRank`, 44 for `FiveRows`, 42 for
`physicalMoments`, and 44 for `CorrectionState.debt`.

This corrects the broad claim that the five-moment branch is dead or absent.
The live upstream chain includes `MeanRankUpdate.physical_five_rows`,
`CorrectionState.rank_model_rows`, `rank_rows_on_patch`, and
`ActualStageEstimates.RunData.rank_class`. The surviving CTR-005 objection is
more precise: `ActualCandidateAssembly.Witness` (lines 1121–1151) and
`selected_witness` (lines 1177–1180) expose no equality transporting the
paper tuple `(M, I, J, S, C_p)` into the selected mixed sums, residual, force,
or `VanishingJointJets` premises.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## 2026-09-24 proposed five-row collision test

The proposed inference that a compact perturbation must collide with the two
zero rows of `FiveRowRank.FiveRows` was tested directly. The zero-sorry
`FiveRowCollisionBoundaryProbe.lean` compiles `FiveRowRank.five_rows` for a
nonzero `Debt := Fin 3 → ℝ` and separately pairs `selected_witness` with that
nonzero debt. This is possible because `FiveRows` constrains the correction
functions `dv` and `ga`, while `Witness` contains no debt field, perturbation
field, `physicalMoments`, or `FiveRows` equality.

`DefectIncrementBounds.fiveRows_preserve_masses` and `zeroMasses` do prove
preservation of two radial correction-state moments. They do not identify
those moments with kinetic energy or with the selected Cartesian velocity.
Consequently the proposed type-level collision does not derive `False`.

**Status:** [x] direct collision route tested and rejected as stated; [~]
selected five-moment transport remains the CTR-005 load-bearing objection.

Evidence: `NavierStokesReview/evidence/five_row_collision_boundary_2026-09-24.md`.

## 2026-09-24 correction-invariant scope theorem

The follow-up theorem isolates the strongest valid consequence of the two zero
rows. `CorrectionInvariantScope.lean` proves, with no `sorry`, `axiom`, or
`unsafe`, that a correction increment satisfying the complete `FiveRows`
predicate must have

```text
barMoment 2 h.angular = 0
barMoment 1 h.axial = 0.
```

It therefore derives `False` from either nonzero correction moment. This is a
real conditional obstruction, not a selected-witness contradiction: the
theorem still needs a transport result identifying the injected perturbation
with `h.angular` or `h.axial` and identifying those moments with the selected
field or the paper's five named quantities. No such endpoint transport is
currently present. This sharpens CTR-005 rather than clearing it.

Evidence: `NavierStokesReview/evidence/correction_invariant_scope_2026-09-24.md`.

## Correction-row transport audit: 2026-09-24

The generic rank-stage theorem has now been exposed directly in the review
completion. It preserves `radialMoment 2` of the angular mean and
`radialMoment 1` of the axial mean. These are the exact consequences of the
two zero correction rows in `FiveRows`.

This is narrower than a mass/energy claim. The source does not identify these
moments with kinetic energy, the complete Cartesian velocity, or the paper's
`(M,I,J,S,C_p)`. The selected `Witness` and `RunInvariant` types do not carry
the invariant. A compact perturbation therefore gives `False` only after a
missing selected-path theorem maps it into `rankIncrement` and proves one of
the two exact moments nonzero.

**CTR-005 update:** generic correction preservation is proved; selected
transport remains the load-bearing unresolved objection. The direct claim
that the zero rows freeze total mass or kinetic energy is not supported by
the source.

Evidence: `NavierStokesReview/evidence/correction_moment_transport_audit_2026-09-24.md`.

## Selected-cycle mass invariant refinement: 2026-09-24

The production path does carry a local invariant that was previously described
too narrowly. `ActualCyclePreservation.Invariant` is a
`CycleAnalyticInvariant`, whose `masses` field is propagated by
`state_invariant`. The new zero-sorry completion
`SelectedCycleMomentTransport.lean` exposes this for every selected cycle
stage and derives `False` from either corresponding nonzero radial moment.

This does not close the counter-paper objection. The invariant is stated on
the internal `CycleState` mean fields and only covers two radial moments. The
exported `ActualCandidateAssembly.Witness` contains the mixed sums, pressure,
force, decay, and blow-up consequences, but does not expose an equality from
those internal moments to the mixed endpoint or to `(M,I,J,S,C_p)`. The live
target is now the precise cycle-to-witness and five-moment transport theorem,
not the existence of a local correction invariant.

Evidence: `NavierStokesReview/evidence/correction_moment_transport_audit_2026-09-24.md`;
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.

## CTR-017: temporal patching boundary audit

The requested stage-transition audit is source-complete for the inspected
files. `GermCandidateAssembly.initializedSeries` at lines 52--61 is an indexed
base/initial/stage selector, not a piecewise-in-time definition. Its first
successor is definitionally `stages 0`; the constructor itself imposes no
adjacent-stage matching equation. `ActualCandidateConstruction.uncutPrefix_succ`
at lines 419--423 and `angularMeanStages_prefix` at lines 425--433 instead
describe additive finite prefixes.

The selected spacetime regularity path is different. `LocalPotentialRebundle`
lines 78--119 proves smoothness and local agreement for the selected summed
fields. `TimeLocalization` lines 27--41 proves smoothness of the actual time
activation, while lines 74--96 and 144--164 prove late local field, derivative,
and residual agreement. `MixedPeriodicAssembly` lines 166--177 and 231--238
proves smoothness and transfer of residual jet limits under spatial local
equality.

| Claim | Status | Evidence |
|---|---:|---|
| Raw indexed stages have an adjacent-stage matching premise | [x] | No such premise in `initializedSeries`; `initialized_series_admits_concrete_boundary_mismatch` constructs an unequal raw boundary without asserting selected-path hypotheses. |
| The selected field is proved temporally discontinuous | [ ] | No source theorem or zero-sorry result establishes this. |
| A higher-order kinetic-energy jump is present | [ ] | No energy-gradient identity is attached to the stage prefix boundary. |
| The activation introduces a non-smooth temporal switch | [x] | Rejected: `timeSwitch` is used through `ContDiffOn ℝ ∞`. |
| Late temporal jets agree with the incoming field | [x] | `activated_temporalDerivative_eq_late` and local eventual equality. |

**Classification:** retain `CTR-017 (Temporal Patching Discontinuity)` as an
open interface question, not a proved endpoint defect. A selected-path
contradiction would require a theorem identifying an actual temporal boundary
with a nonzero derivative mismatch. The zero-sorry probe is
`NavierStokesReview/src/probes/TemporalPatchingDiscontinuityProbe.lean` and
the ledger is `NavierStokesReview/evidence/temporal_patching_audit_2026-09-24.md`.

The official-source nuance is recorded separately in
`docs/OpenAI_NavierStokes_Source_Context_Register.md`: Fefferman's “given,
externally applied” wording supports a causal/provenance objection, while the
literal C/D alternatives remain existential and OpenAI's paper explicitly
describes residual construction. That distinction is part of the audit
record, not a concession about the missing selected semantic bridge.

## CTR-012 provenance closure: selected force is residual output

The zero-sorry theorem
`SelectedResidualProvenance.selected_candidate_force_is_residual_output`
destructs `ActualCandidateAssembly.selected_candidate` and proves, for the
selected velocity, pressure, and force,

$$
f(t,x)=\operatorname{navierStokesResidual}(u,p,t,x)
$$

for every interior time and spatial point. The source construction reaches the
same conclusion through `MixedPeriodicAssembly.exists_candidate_force` and
`CandidateFromLimits.force_eq_activated_residual`.

**Classification:** [x] residual provenance established on the selected path;
[~] the CMI-level force-independence objection remains a correspondence
question, not a proved `False`, because the exported `CandidateProperties` does
not quantify over perturbations or require an independence predicate.

Evidence: `NavierStokesReview/evidence/selected_residual_provenance_2026-09-24.md`.

## Selected rank transport re-audit: 2026-09-24

The production rank subsystem is live rather than dead code. `FiveRows` is
proved for arbitrary three-coordinate debt by `MeanRankUpdate.physical_five_rows`,
and `CorrectionState.rank_model_rows`/`rank_rows_on_patch` apply the result to
the actual rank increment. The two zero rows constrain correction functions
and preserve two radial correction moments; they do not freeze total mass or
kinetic energy.

`ActualMeanPhysicalData.cycleRank_class` consumes the actual
`CorrectionState.debt`, while `ActualCandidateAssembly.physicalData` and
`estimates` consume actual cycle fields and residual data. The broad claim that
the selected path is insulated from all moment machinery is therefore
withdrawn. The surviving CTR-005 issue is narrower: `Witness` and
`selected_candidate` do not export an equality connecting those internal
moments to the paper's `(M,I,J,S,C_p)` or to the final mixed residual and
force. Evidence:
`NavierStokesReview/evidence/selected_rank_transport_reaudit_2026-09-24.md`.

## 2026-09-24 whole-space uniqueness-chain audit

The selected R³ endpoint was traced through `WholeSpaceUniqueness`.
`classical_uniqueness_on_Icc` derives equality on each closed interval before
time one from the two residual equations, incompressibility, smoothness,
finite-energy bounds, compact reference support, and compact-test pressure
recovery. `candidate_global_agrees_before_one` applies this to a
`GlobalFiniteEnergySolution`; `CandidateProperties.no_global_solution_one`
then uses compact support and the selected speed blow-up.

This corrects two weaker objections. The R³ theorem is not a candidate-only
shell, and compact pressure support is not a hidden premise that pressure or
velocity vanishes. The pressure argument is relative and compact-test based,
so an absolute selected pressure representative remains unexposed, but no
pressure-trivialisation contradiction was found.

`WholeSpaceAxiomAudit.lean` reports only the standard Lean axioms for the
queried R³ and periodic endpoints and uniqueness lemmas. No admitted
declaration was found in this audited path.

**Classification:** uniqueness route formally active; no selected-witness
`False` obtained. CTR-005 remains the load-bearing selected-path
five-moment/pressure correspondence objection.

Evidence: `NavierStokesReview/evidence/whole_space_uniqueness_audit_2026-09-24.md`.

## External-source scope control: 2026-09-24

The companion Euler paper and the public release are tracked as comparison
material only. The release describes the Euler result as unforced and presents
the Navier--Stokes result through the forced C/D alternatives. That distinction
does not supply a temporal-gluing theorem for the Navier--Stokes indexed stages
and does not alter the selected-endpoint transport target. Source register:
`docs/OpenAI_NavierStokes_Source_Context_Register.md`.

Packaging status: `700e39d` is the last confirmed remote baseline; local review
commit `7e6f0c7` is not confirmed pushed because GitHub authentication is
unavailable. The two supplied reference PDFs remain intentionally untracked,
and no Lean build artefacts are tracked.

## Selected endpoint direct-source trace: 2026-09-24

- [x] Rechecked the immediate endpoint path. `physicalData` and `estimates`
  consume actual cycle fields and residual bounds.
- [x] Rechecked the upstream rank path. `FiveRows` and the two internal radial
  invariants are proved for the constructed correction states.
- [x] Rechecked the exported `Witness`. It contains no equality to
  `PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
  `FiveRowRank.FiveRows`, or `(M,I,J,S,C_p)`.
- [ ] A concrete selected-field violation or zero-sorry `False` theorem has
  not been obtained. CTR-005 remains a selected-endpoint correspondence
  objection, not a dead-code or hardcoded-zero claim.

Evidence: `NavierStokesReview/evidence/selected_endpoint_direct_source_trace_2026-09-24.md`.

## Fixed-force stability extension: 2026-09-24

| ID | Result | Status |
|---|---|---:|
| CTR-012-I | Defined `FixedForceStable` for smooth, compactly supported, divergence-free velocity perturbations with force and pressure held fixed. | [x] |
| CTR-012-J | Proved that the selected candidate fails this strengthened predicate using the compact perturbation at `(1/2, 0)`. | [x] |
| CTR-012-K | Derived a contradiction with the literal C/D existential endpoint. | [ ] |

The new theorem is compiled in
`NavierStokesReview/src/external_semantic/FixedForcePerturbationStability.lean`.
It proves a fixed-force stability failure, not that the literal endpoint is
empty. `CandidateProperties` does not quantify over perturbations or require
force independence. Evidence:
`NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md`.

## Same-datum fixed-force closure: 2026-09-24

The earlier fixed-force perturbation lane did not require the perturbation to
preserve the selected zero initial datum. That limitation is now removed in
`NavierStokesReview/src/extensions/SameDatumFixedForcePerturbation.lean`.
The new field uses the factor `t(t-t₀)` and is globally smooth, compactly
supported on every spatial slice, divergence-free, and zero at `t = 0`. At an
interior switch `t₀`, its value, spatial derivative, and spatial Laplacian
vanish, while its temporal derivative is `t₀ • compactCurlField (t₀, x)`. At
the origin this is nonzero for `t₀ ≠ 0`.

The zero-sorry theorem
`selected_candidate_fails_fixed_force_same_datum_stability` therefore proves
fixed-force path dependence even when the initial datum is held fixed. This
strengthens CTR-012 as a forward-data objection. It still does not make the
literal C/D existential empty, because `CandidateProperties` does not quantify
over perturbations or encode force independence.

Evidence:
`NavierStokesReview/evidence/same_datum_fixed_force_obstruction_2026-09-24.md`.

## Selected active-pair reachability: 2026-09-24

The stage-control source contains an explicit empty/nonempty split for
`ActualParticularStageControls.ActivePair`. A review-side theorem proves the
positive implication that is justified by the source: given a concrete
`ActualPrimary.Label B N0`, its chart-band lower bound makes the same-band
pair active via `CommonWindow.self_mem`.

The selected-path construction is now stronger than this conditional result:
`SelectedLabelConstructionProbe.selected_primary_label_nonempty` constructs a
label above the selected threshold, and
`selected_active_pair_nonempty` turns it into an active pair. The generic
empty branch remains a valid interface branch, but it is not reachable on the
selected path under the proved construction.

Evidence: `NavierStokesReview/evidence/selected_active_pair_reachability_2026-09-24.md`.

## CTR-019: selected-label inhabitability: 2026-09-24

| Check | Source result | Status |
|---|---|---:|
| Primary choice | `ActualPrimary.choice_nonempty` selects the prepared geometric data. A separate review theorem constructs the required label above its selected band floor. | Verified by review theorem |
| Active-pair reachability | `SelectedLabelConstructionProbe.selected_active_pair_nonempty` constructs the stage label `(0,L)` and uses `BaseChartJets.cellBand L` plus `CommonWindow.self_mem`. | Verified on selected path |
| Empty branch | `ActualParticularStageControls.raw_jets` contains an explicit `¬ Nonempty (ActivePair B N0)` branch; `ActualInitialMean.covariance_bounds_of_curl` also splits on an empty cycle index. | Verified source branch |
| Diagonal sum | `LocalScheduleWitness.potentialSum` unfolds to `SolenoidalDiagonal.potentialSum`, a `tsum` over `j : ℕ`, not over `ActivePair`. | Not an empty-set limit |

The selected witness does not itself export these inhabitance theorems, but the
review-side construction now proves both propositions without admitted
declarations. `slowMask_sum_sq = 1` supplies a nonzero mask at every positive
band; the explicit point `(√(2a),(0,1))` lies in the selected reference
annulus. Thus CTR-019 is cleared as a selected-path vacuity route. The generic
empty branches remain real interface behaviour, but they do not apply to the
selected construction.

Evidence: `NavierStokesReview/evidence/selected_label_inhabitability_audit_2026-09-24.md`;
`NavierStokesReview/src/probes/SelectedLabelInhabitabilityProbe.lean`;
`NavierStokesReview/src/probes/SelectedLabelConstructionProbe.lean`.

## External wording and admissibility scope: 2026-09-24

The official problem statement calls the force a given, externally applied
force and imposes smooth decay estimates. OpenAI's release describes a smooth
applied force whose terms cancel while velocity grows. These statements
support a causal/provenance objection to a residual-designed trajectory, but
the exported C/D proposition contains no formal independence predicate. The
review records this as a paper-to-endpoint correspondence issue, not as a
Lean contradiction derived from wording alone.

## Burden of proof and possible underclaim: 2026-09-24

The audit distinguishes a failure to establish the published claim from a
formal refutation of the literal exported proposition. OpenAI bears the burden
of proving the stronger statement it presents to readers. The review does not
have to derive `False` from `selected_witness` before finding that the paper's
CMI-level claim is unsupported by the inspected source.

The unresolved obligations are affirmative requirements on the authors:

1. identify the actual selected velocity and pressure fields with the paper's
   named moments `(M,I,J,S,C_p)`;
2. transport those identities through the correction, germ, residual, and
   force construction;
3. show that the analytic premises consumed by the endpoint hold for that same
   object; and
4. explain why the residual-designed force satisfies the paper's use of
   “given, externally applied force”, rather than only the weaker formal
   `CandidateProperties` predicate.

The current evidence shows that these obligations are not exported as one
selected-field composition theorem. This is therefore a substantive
**not-established** finding, not a presumption that the missing bridge is
true. The narrower status **not formally refuted** records only that the
current zero-sorry attack has not produced `False` from the selected endpoint.

Evidence: `NavierStokesReview/evidence/burden_of_proof_underclaim_audit_2026-09-24.md`.

## CTR-016: global germ-transport validity audit: 2026-09-24

| Source / interface | Exact result | Status |
|---|---|---:|
| `CandidateConsequences.lean:185-215` | `mixed_exists_force_with_consequences` returns the force, `CandidateProperties`, `Consequences`, H³ growth, force-jet decay, and boundary jets from its supplied local data and residual limits. | [x] |
| `ActualCandidateAssembly.lean:1079-1098` | `physicalData` and `estimates` consume actual cycle states, uncut fields, representations, and residual data. | [x] |
| `ActualCandidateAssembly.lean:1100-1115` | `endpoints` supplies germ-stage endpoint data to the finite-stage schedule. | [x] |
| `ActualCandidateAssembly.lean:1121-1151` | `Witness` exports selected sums, away extensions, force predicates, `Consequences`, H³ growth, decay, and boundary jets, but no `(M,I,J,S,C_p)` equality. | [x] |
| `ActualCandidateAssembly.lean:1177-1181` | `selected_witness` instantiates that same bundle without adding a moment-transport or force-independence theorem. | [x] |
| `GlobalTransportBridgeProbe.lean:27-43` | Zero-sorry result: the selected candidate has the global `Consequences` bundle while same-datum fixed-force stability fails. | [x] |

CTR-016 is a global contract mismatch, not a compiler failure. The local-to-
global PDE and jet consequences are present. The missing exported fields are
the selected five-moment identity and force-independence/stability condition.

Evidence: `NavierStokesReview/evidence/global_germ_transport_audit_2026-09-24.md`.

### CTR-016 recheck: actual cycle transport is present, endpoint semantics remain unexported

The source recheck records positive transport evidence before the final
envelope. `ActualCyclePreservation.state_runInvariant` (826-848) and its
particular-data/wave results (850-912) feed
`ActualCycleCoherence.mean_input_of_transport` (803-820). Native stage
definitions and prefix identities occur at
`ActualCandidateConstruction.lean:392-404,464-502`, and actual chart
equalities occur at `ActualCandidateAssembly.lean:392-424`.

This narrows, rather than removes, CTR-016. The source has a genuine local-to-
global construction and the selected endpoint consumes actual cycle data. The
remaining missing theorem is the field-level identification of that data with
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, and the paper tuple `(M,I,J,S,C_p)` inside the selected
mixed velocity, pressure, residual, and force. The classification remains
**open, load-bearing correspondence defect; no `False` theorem**.

## Endpoint contract non-implication: 2026-09-24

`EndpointContractNonImplication.lean:20-25` proves that `CandidateProperties`
does not imply `FixedForceSameDatumStable`. Its axiom audit reports only
`propext`, `Classical.choice`, and `Quot.sound`.

## Official claim transport matrix: 2026-09-24

The source-to-claim matrix records the burden asymmetry precisely. The exported
`Witness` and comparator path contain the literal C/D-shaped predicates, so the
review does not describe the endpoint as a hollow existential shell. The
stronger public paper claim still requires a selected-field correspondence
theorem for the five named moments.

| Obligation | Source result | Status |
|---|---|---|
| Smooth force, support, zero datum, divergence, residual, energy, and blow-up reach the selected endpoint | `ActualCandidateAssembly.lean:1121-1151`, `1177-1185`; `R3/ProblemStatement.lean:92-109` | Present in the literal endpoint |
| Whole-space and periodic C/D comparator consequences follow | `R3/ComparatorR3Theorem.lean:21-35`; `ComparatorTheorem.lean:25-51` | Present on the inspected path |
| The selected mixed fields equal the paper's `(M,I,J,S,C_p)` moments | No equality in `Witness`; upstream definitions are `PositiveOrderMoments.lean:76-85` and `FiveProfileMoments.lean:473-489` | Not established; headline CTR-005 |
| The three-debt rank repair is the paper's five-moment system | `FiveRowPositiveOrderBridgeProbe.lean` proves only the constrained promotion `(0,0,-P,-Jθ,-Jz)` | Direct identification fails; selected transport remains unproved |
| Residual-designed force satisfies an independently encoded force-data condition | No independence or perturbation-stability field in `CandidateProperties` | Not established as the stronger semantic reading |

The proper review conclusion is therefore: the authors have established a
formal C/D-shaped endpoint only if the endpoint source is accepted as given;
they have not yet established that the central five-moment construction in the
paper is the construction exported by that endpoint. The burden to supply that
identification is on the authors. A missing bridge is enough to withhold the
stronger claim, even though it is not itself a proof of `False`.

Evidence: `NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.
