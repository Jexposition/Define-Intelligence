# OpenAI Navier–Stokes Counter-Paper Evidence Tracker

## Live register state (2026-09-28)

The authoritative register currently records 2,790 indexed modules, 588
 reachable modules, 613 evidence-inspected modules, 0 reachable modules still
 open, and 0 missing project import edges. Historical tranche counts below are
kept as provenance; they are not the current total.

This document is the working ledger for the counter-paper. It records evidence, status, and the next falsification test. It is intentionally a tracker. The argument itself is written in `OpenAI_NavierStokes_Research_Paper.md`.

## MAP-41: R3 breakdown, primary coherence, mean bounds, and signed-wave tier (2026-09-27)

Four further reachable modules were inspected directly. `R3/CandidateBreakdown.lean`
derives the no-global-competitor consequence from compact support, speed
unboundedness, and whole-space comparison, and derives a uniform (L^2) square
bound from `CandidateProperties`. `ActualPrimaryCoherence.lean` proves
positive-radius global potential representations, periodicity, smoothness,
axis-zero germs, and component-level piece-to-Cartesian curl identities.
`MeanMomentBounds.lean` proves torus-average, radial-weight, pressure-mass, and
radial-moment class identities. `PhysicalSignedWave.lean` proves concrete
signed/primary wave potential, cutoff, pressure, periodicity, and Cartesian-curl
identities.

These results strengthen the positive intermediate source record. They do not
evaluate the final selected `ASum`/`BSum`/`PSum` field through the complete
sum/curl/localisation/periodisation/torus-average/radial-pullback,
support/integrability, and axis route to `(M,I,J,S,C_p)`. No nonzero remainder,
impossibility theorem, or kernel `False` was obtained. The live register now
records 89 explicit source reviews and 509 reachable modules awaiting semantic
classification.

Evidence: `NavierStokesReview/evidence/reachable_r3_primary_mean_wave_tier_2026-09-27.md`.

## MAP-42: Primary bounds, slow-axis, moving moments, and pressure-test tier (2026-09-27)

`ActualPrimaryBounds.lean` proves native velocity/pressure jet bounds,
periodised copy-sum estimates, cutoff-copy identities, and chart-level uniform
wave classes. `ActualSlowAxis.lean` proves reduced slow-axis regularity,
positive-order collar identities, stock-field identities, axis vanishing, and
axis jets. `MovingMomentBounds.lean` proves moving-strip pressure-mass and
radial-moment class bounds, support closure under differential operators, and
rank-stage defect classes under explicit local hypotheses.
`R3/PressureTestBounds.lean` proves Fourier/H3 derivative and Riesz-test bounds
for comparative pressure recovery.

These are additional concrete intermediate results. They do not evaluate the
final selected field through the full five-observable route, and comparative
pressure-test bounds are not an absolute selected-pressure Poisson theorem. No
nonzero remainder, impossibility theorem, or kernel `False` was obtained. The
live register now records 93 explicit source reviews and 505 reachable modules
awaiting semantic classification.

Evidence: `NavierStokesReview/evidence/reachable_primary_axis_moving_pressure_tier_2026-09-27.md`.

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

The repository contains a genuine R³ C/D-shaped endpoint and the headline theorem reports only standard Lean axioms. The primary adverse result is that the published five-moment/CMI solution claim is **not established** by the inspected paper-to-endpoint record: the authors have not supplied the selected-field composition theorem that their advertised solution requires. This is not softened by the fact that a separate zero-sorry attack has not yet derived `False`. `FiveProfileMoments` matches the paper-shaped normalisation, `PositiveOrderMoments` proves an exact five-component recursive repair, and `FiveRowRank` supplies a distinct three-debt physical rank interface. A zero-sorry theorem rules out direct row-by-row identification between the first and third interfaces, while the positive-order layer may be an intended intermediate representation. The literal endpoint is therefore not labelled formally refuted, but the published solution claim is not accepted pending affirmative proof of the missing transport.

This is the claim OpenAI actually published, not a stronger interpretation
invented by the review. The announcement calls the work a solution of the
Navier–Stokes existence and smoothness problem and says it resolves the
problem through alternatives (C) and (D). The paper's Theorem 1.1 makes the
same affirmative construction claim. The missing selected-field transport is
therefore a defect in the proof record for the central published solution,
not a request for optional robustness or physical realism.

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

## CMI and paper-nuance correction: 2026-09-27

Fefferman's statement describes the force as a given externally applied force,
but Alternatives (C) and (D) are existential mathematical statements. The
statement does not provide a syntactic independence predicate that forbids
choosing a flow first and defining a residual force. OpenAI's Navier--Stokes
paper expressly describes that residual-design method and makes smooth
residual cancellation its construction problem.

Accordingly, the tracker does **not** classify residual-defined forcing as an
automatic CMI violation. The live issue is whether the selected Lean endpoint
implements the paper's complete construction: five moments, stage
corrections, pressure, localisation, all-order residual cancellation, and the
whole-space nonexistence argument. The companion Euler paper similarly states
exact smooth parent--child stages and a stability-based limit; nested intervals
alone do not prove a temporal discontinuity or a Zeno failure.

Evidence: `NavierStokesReview/evidence/paper_nuance_crosswalk_2026-09-27.md`.

## Semantic correspondence map: 2026-09-26

The review is now organised around the human-readable
`docs/SEMANTIC_CORRESPONDENCE_MAP.md`. That map is the source-to-claim
explanation layer: it identifies what the paper claims, which Lean declarations
construct the corresponding objects, what the selected endpoint actually
exposes, and which field-level equalities remain unproved. It replaces any
compile-count-only reading of the audit. The current load-bearing question is
not whether the moment files are reachable; it is whether their named
observables survive the actual selected Cartesian `tsum`, curl, localisation,
periodisation, averaging, and R3 packaging.

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

The present publication classification is **do not accept the published CMI-solution claim on the inspected record**. This decision follows from the affirmative burden of proof: the published argument must identify the selected fields and transport the paper's named quantities into the exported endpoint. A `[FORMALLY REFUTED]` label is reserved for a zero-sorry contradiction or a false premise proved on the selected endpoint path; that narrower label is not required to withhold acceptance of an under-supported solution claim.

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

The earlier “absolute structural falsification” wording is withdrawn. The direct transport from the paper's named five moments to the selected endpoint remains a publication-critical obligation, but the existing constrained positive-order bridge prevents treating the type difference alone as a contradiction. The selected-budget issue likewise produces no endpoint refutation. The current evidence therefore supports a negative decision on the published solution claim, while reserving “formally refuted” for a separate selected-path contradiction.

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

Packaging status: review commit `054f407` is pushed to
`review/cmi-first-navier-stokes-2026-09-22`. The two supplied reference PDFs
remain intentionally untracked, and no Lean build artefacts are tracked.

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
published solution claim still requires a selected-field correspondence
theorem for the five named moments.

| Obligation | Source result | Status |
|---|---|---|
| Smooth force, support, zero datum, divergence, residual, energy, and blow-up reach the selected endpoint | `ActualCandidateAssembly.lean:1121-1151`, `1177-1185`; `R3/ProblemStatement.lean:92-109` | Present in the literal endpoint |
| Whole-space and periodic C/D comparator consequences follow | `R3/ComparatorR3Theorem.lean:21-35`; `ComparatorTheorem.lean:25-51` | Present on the inspected path |
| The selected mixed fields equal the paper's `(M,I,J,S,C_p)` moments | No equality in `Witness`; upstream definitions are `PositiveOrderMoments.lean:76-85` and `FiveProfileMoments.lean:473-489` | Not established; headline CTR-005 |
| The three-debt rank repair is the paper's five-moment system | `FiveRowPositiveOrderBridgeProbe.lean` proves only the constrained promotion `(0,0,-P,-Jθ,-Jz)` | Direct identification fails; selected transport remains unproved |
| Residual-designed force satisfies an independently encoded force-data condition | No independence or perturbation-stability field in `CandidateProperties` | Not established as part of the published solution claim |

The proper review conclusion is therefore: the authors have established a
formal C/D-shaped endpoint only if the endpoint source is accepted as given;
they have not yet established that the central five-moment construction in the
paper is the construction exported by that endpoint. The burden to supply that
identification is on the authors. A missing bridge is enough to withhold the
published solution claim, even though it is not itself a proof of `False`.

Evidence: `NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.

## Selected physical-data moment-interface recheck: 2026-09-24

The selected source does construct and consume `PhysicalData`; this is not a
dead-code finding. `ActualCycleResidualBounds.lean:1015-1037` defines the
record with smoothness, germs, and exterior agreement, while
`ActualCycleResidualBounds.lean:1142-1173` abbreviates that record as
`PhysicalData` and uses it to produce residual jet bounds. The record has no
`PositiveOrderMoments.Debt`, `FiveProfileMoments.physicalMoments`, or
paper-level `(M,I,J,S,C_p)` field.

The review-side zero-sorry probe
`SelectedPhysicalDataMomentInterfaceProbe.lean` pairs the actual selected
`physicalData` theorem with an arbitrary nonzero five-coordinate debt. This
proves an interface non-implication: the exported record does not determine a
five-moment payload. It does not prove that the actual selected fields have a
wrong integral. The next affirmative target is a theorem equating the
selected mixed fields to the five named moments, followed by a proof that one
such equality fails or is absent from a mandatory endpoint premise.

Evidence: `NavierStokesReview/evidence/selected_physical_data_moment_interface_2026-09-24.md`.

## Publication-burden reassessment: 2026-09-25

The review decision is now stated consistently across the active corpus:
**do not accept the published CMI-solution claim on the inspected
record**. This is an underclaim finding, not a demand that the reviewer first
derive `False` from the literal existential endpoint. The selected endpoint
may be a genuine formal C/D-shaped object while the published paper-to-code
identification remains unproved.

The load-bearing omission is affirmative. The source does not export the
selected-field theorem identifying the paper's `(M,I,J,S,C_p)` quantities and
transporting them through the correction, germ, residual, and force layers.
The burden to supply that composition theorem remains with the authors. The
status **not formally refuted** is subordinate and records only the separate
state of the kernel-level contradiction search.

Evidence: `NavierStokesReview/evidence/burden_of_proof_underclaim_audit_2026-09-24.md`;
`NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.

## Five-row formula alignment and selected-field transport: 2026-09-25

The review has corrected an important possible underclaim. The positive-order
five-row formulae are not being alleged to disagree with the paper:
`PositiveOrderMoments.rowDensity` and `moments`
(`PositiveOrderMoments.lean:77-85`) match the paper's five order-moment
integrands. The outstanding defect is at the selected composition boundary.
`ActualCandidateAssembly.positivePotential`
(`ActualCandidateAssembly.lean:515-523`) is the particular-plus-signed-plus-
stream field used to form the selected stages, while `Witness`
(`ActualCandidateAssembly.lean:1121-1151`) exports no equality carrying that
mixed field into `PositiveOrderMoments.moments`,
`FiveProfileMoments.physicalMoments`, or the paper tuple `(M,I,J,S,C_p)`.

That omission is load-bearing because the paper uses the five identities to
remove pressure/stress tails and preserve outer fields. The current verdict
therefore addresses the central published solution claim: the source does not
establish that the selected object exported as the solution is the object to
which the paper's five-moment tail-cancellation argument applies. This is an
affirmative failure to discharge the authors' proof burden. It is distinct
from the narrower question whether the selected endpoint alone yields a
kernel-level `False`.

The exact source-backed correction and line ledger are now recorded in
`NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.
It confirms that the five-row formulas and upstream cancellation are active;
the unresolved defect is their transport into the selected mixed field and
the exported solution contract.

## Claim-level reconciliation: 2026-09-25

The R³ theorem path is part of the controlled source record. The selected
periodic witness is localised by `NavierStokes/R3/ActualCandidate.lean`, and
`NavierStokes/R3/Theorem.lean:27-53` exports `breakdownStatement` for every
positive viscosity. The literal C/D target is therefore not being rejected on
the ground that only a generic periodic witness exists.

The residual-defined-force and fixed-force perturbation arguments do not
contradict that existential target. They test stronger provenance or stability
properties unless a selected-field premise is shown false. The official paper
itself presents smooth residual cancellation as the construction method.

CTR-005 remains the publication-level issue because the final `Witness` export
does not expose the equality transporting the paper's five quantities

$$
(M,I,J,S,C_p)
$$

into the selected mixed velocity, pressure, residual, and force. Upstream
five-moment definitions and cancellation theorems are confirmed live. Status:
**publication claim not established at the advertised mechanism level; literal
C/D endpoint not formally refuted by this route**.

Evidence: `NavierStokesReview/evidence/cmi_target_and_claim_level_reconciliation_2026-09-25.md`.

## Repository admission census: 2026-09-25

The source tree contains explicit admitted challenge declarations:
`ComparatorChallenges/NavierStokes.lean:273-284` has two `by sorry` theorem
bodies, and `ComparatorChallenges/Euler.lean:85-88,181-184` has further
admissions. `lakefile.toml` includes `ComparatorChallenges` in
`defaultTargets`. This defeats a blanket repository-wide zero-sorry claim.
The selected `NavierStokes/R3` endpoint is tracked separately; the census does
not claim that these challenge declarations lie on its dependency path. The
publication-level verdict remains **not established**, with CTR-005 as the
load-bearing selected-field correspondence objection. Evidence:
`NavierStokesReview/evidence/repository_admission_census_2026-09-25.md`.

## CTR-042: admitted declarations independently confirmed by `#print axioms`: 2026-09-25

The review-side module
`NavierStokesReview/src/audit/RepositoryAdmissionAudit.lean` imports the
standalone challenge declarations and contains no admitted declaration of its
own. Lean reports `sorryAx` for all four challenge results:

| Declaration | Axiom result | Scope |
|---|---|---|
| `NavierStokes.Comparator.navier_stokes_breakdown_R3` | `propext, sorryAx, Classical.choice, Quot.sound` | standalone challenge module |
| `NavierStokes.Comparator.navier_stokes_breakdown_periodic` | `propext, sorryAx, Classical.choice, Quot.sound` | standalone challenge module |
| `Euler.euler_breakdown_R3` | `propext, sorryAx, Classical.choice, Quot.sound` | standalone challenge module |
| `Euler.exists_compact_smooth_euler_singularity` | `propext, sorryAx, Classical.choice, Quot.sound` | standalone challenge module |

This confirms the release-level admission finding rather than merely counting
the source token. It does not place `ComparatorChallenges` on the selected
`NavierStokes/R3` dependency path; `ComparatorSolution.lean` uses the
independent comparator definitions and bridge. Classification: **confirmed
repository-scope defect; selected-endpoint contamination not shown**.

Evidence: `NavierStokesReview/evidence/repository_admission_axiom_log_2026-09-25.md`.

## CTR-043: selected witness does not export the paper's moment payload

The selected-endpoint extension
`NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
uses the actual `selected_witness` and proves, without `sorry`, that it is
compatible at the exported type boundary with a nonzero
`PositiveOrderMoments.Debt`. The same module proves that the witness does not
entail `∀ d : Debt, d = 0`.

This is not a claim that the selected integrals are false. It is a direct
non-implication result: `ActualCandidateAssembly.Witness` does not itself
export a debt field, a five-moment array, or an equality identifying the
selected mixed fields with `(M,I,J,S,C_p)`. The upstream five-row formulae
remain active and source-supported. The missing selected-field composition
theorem remains the load-bearing publication objection under CTR-005.

| Check | Result |
|---|---|
| Selected `Witness` is inhabited | Proved by `ActualCandidateAssembly.selected_witness`. |
| Nonzero five-coordinate payload can coexist with that export | Proved by `selected_witness_compatible_with_nonzero_five_payload`. |
| Actual selected moments are disproved | Not claimed; no equality to the selected integrals is exposed. |
| Published five-moment solution claim established | **No; selected-field transport remains unproved.** |

Evidence: `NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md`.

## CTR-044: profile-tail collision route adjudication

The proposed route to a kernel contradiction has been tested against the
actual definitions. `FiveRowRank.FiveRows` constrains correction profiles
`dv` and `ga`; `DefectIncrementBounds.barMoment` returns radial/toroidal
profile moments, not total Cartesian field or kinetic-energy integrals. The
selected cycle carries a genuine local two-moment invariant, but the final
`Witness` does not export a map from its Cartesian `tsum` fields to those
radial profile types.

The review-side module
`NavierStokesReview/src/refutations/CTR005ProfileTailCollisionScope.lean`
proves without admissions that a nonzero runtime debt is compatible with the
two zero correction rows. It also exposes the selected cycle zero-moment fact
and the exact `barMoment` type. Therefore the conditional implication

$$
\text{nonzero selected correction moment} \Longrightarrow \mathrm{False}
$$

remains valid, but its selected-field nonzero premise is not established. The
route strengthens CTR-005 as the main field-level target; it does not yet
produce `False`.

Evidence: `NavierStokesReview/evidence/ctr005_profile_tail_collision_route_2026-09-25.md`.

## CTR-045: selected Cartesian-to-radial remainder search

The source trace follows the actual selected construction rather than assuming
that upstream profile identities apply automatically. The field path is

$$
\texttt{potentialSum}
\longrightarrow \texttt{cutStage/SpatialCurl}
\longrightarrow \text{Cartesian field}
\longrightarrow \text{cylindrical profile}
\longrightarrow \texttt{barMoment}.
$$

`SolenoidalDiagonal.lean:20-39` defines the natural-indexed sum of cut stages.
`ActualCandidateConstruction.lean:509-520,963-966` supplies the charted stage
fields. `ActualMeanPotentialRealization.lean:29-40` and
`DirectAngularDiagonal.lean:65-71,231-237` expose the meridional and angular
Cartesian constructions. `DefectIncrementBounds.lean:214-220` defines the
radial/toroidal `barMoment`, while `FiveRowRank.lean:241+` constrains the
correction profiles `dv` and `ga`.

No selected-field theorem currently evaluates this entire composition. The
remaining test is concrete: calculate finite-prefix and tail contributions,
including derivatives of localisation masks and axis/tail boundary terms, and
search for an exact nonzero remainder. The symbolic helper
`NavierStokesReview/tools/radial_profile_integrals.py` is deliberately only a
calculation aid until such a Lean equality is proved.

| Check | Result |
|---|---|
| `tsum` and local finite-tail behaviour traced | Confirmed |
| Cartesian stage and curl constructions traced | Confirmed |
| `barMoment`/`FiveRows` scope traced | Confirmed; correction-profile scope |
| Exact selected Cartesian-to-radial identity | Open |
| Exact selected nonzero remainder | Open |
| Selected-path `False` | Not derived |

Classification: **live kernel-level falsification target**, not a completed
contradiction. Evidence:
`NavierStokesReview/evidence/selected_field_remainder_trace_2026-09-25.md`.

## CTR-046: Euler parent-child interval audit

The companion Euler source was checked independently. `PacketSourceScaleSequence`
and `PacketSourceScaleGuards` prove positive widths and controlled contraction;
`PacketNestedHorizons` proves positive common horizons and monotone activation;
`IntervalPathConcatenation`, `TimeIntervalGlue`, and the joined-path modules
require and use value plus first-derivative matching at seams. The inspected
source does not establish the proposed quiet Zeno endpoint or a first-order
temporal jump. An all-order jet audit remains open and must be supported by an
explicit unmatched derivative before being called a defect.

Evidence: `docs/Euler_Parent_Child_Interval_Audit.md` and
`NavierStokesReview/evidence/euler_parent_child_interval_audit_2026-09-25.md`.

## CTR-047: selected-field radial remainder calculation gate

The concrete selected-field trace was extended from the stage aliases into
the actual construction. `ActualCandidateConstruction` gives the initial and
positive stage fields, `DirectAngularDiagonal` gives the cylindrical angular
component and cutoff multiplication, `ActualMeanPotentialRealization` gives
the Cartesian embedding and curl identities, and `SolenoidalDiagonal` gives
the locally finite `potentialSum`.

The calculation stops at a specific, testable interface. `barMoment` is
defined for scalar radial-profile fields and `barMoment_apply` evaluates a
torus-averaged radial integral. No source theorem identifies that scalar
profile with the selected Cartesian `VelocityField` after cutoff, curl,
projection, and `tsum`. The first two `FiveRows` identities therefore cannot
yet be applied to the selected field as a matter of type or value.

| Required result | Status | Evidence |
|---|---:|---|
| Expand a concrete selected stage on a positive-radius band | Open | `ActualCandidateConstruction.lean:953-970` |
| Retain cutoff derivative terms | Open | `DirectAngularDiagonal.lean:208-214`; no selected radial identity |
| Transport Cartesian curl to `barMoment` | Open | `ActualMeanPotentialRealization.lean:29-40,300-316`; `DefectIncrementBounds.lean:214-220` |
| Evaluate axis and outer-support terms | Open | Generic support lemmas exist; selected values are not computed |
| Prove a nonzero selected remainder | Open | No source-backed `Δm ≠ 0` has been established |
| Derive selected-path `False` | Open | Requires the preceding selected equality and value |

The symbolic helper `NavierStokesReview/tools/radial_profile_integrals.py`
is a calculator for explicit reviewer-supplied profiles, not a proof that
those profiles are the selected field. The complete source trace is recorded
in `NavierStokesReview/evidence/selected_field_moment_calculation_gate_2026-09-25.md`.

This record also closes three invalid shortcuts: correction zero rows are not
total kinetic-energy identities; smooth localisation is not a discontinuity;
and fixed-force perturbation brittleness is not by itself a contradiction of
the existential C/D proposition. The affirmative five-moment selected-field
transport remains the authors' burden.

## CTR-048: selected finite-prefix transport is non-vacuous

The review-side completion
`NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean` imports
the actual `selected_witness` and proves that the selected potential `tsum` is
eventually equal to a finite prefix at every positive preterminal point. It
also proves that the same finite prefix represents every iterated Frechet jet.
This closes the empty-tail and empty-filter version of the selected-series
objection.

The result sharpens, rather than removes, CTR-005. The selected sum is a real
locally finite Cartesian construction, but the source still provides no
theorem identifying that Cartesian field, after curl and localisation, with
the scalar radial profile consumed by `DefectIncrementBounds.barMoment`. The
nominal five-row formula in `NominalProfile.outgoing_moments_ideal` is not
such an identification. No selected nonzero remainder `Delta m ≠ 0` or
selected path `False` has been established.

Evidence:
`NavierStokesReview/evidence/selected_field_finite_prefix_transport_2026-09-25.md`.

## CTR-049: selected direct-prefix identity

The review-side completion
NavierStokesReview/src/completions/SelectedDirectPrefixField.lean now proves
a concrete identity for the actual selected direct family. Each
selectedDirectStages j is the corresponding angularMeanStages field, and the
uncut prefix through J equals the selected cycle-state mean angular field.
The module compiles without sorry, axiom, or unsafe.

This is stronger than a generic interface observation: it locates an actual
selected field and its finite-stage recurrence. It still does not supply the
next analytical operation required by the paper's argument. The prefix is a
Cartesian VelocityField; barMoment consumes a scalar radial profile after
torus averaging. Cutoff derivatives, positive-radius curl terms, and axis and
outer-support contributions must be transported through that interface before
any selected Delta m ≠ 0 can be stated.

| Check | Result |
|---|---|
| Selected direct stage identity | Proved. |
| Selected finite-prefix field identity | Proved. |
| Cartesian-to-radial barMoment identity | Open. |
| Selected nonzero remainder | Open; not asserted. |
| Selected-path False | Not derived. |

Evidence: NavierStokesReview/evidence/selected_direct_prefix_field_2026-09-25.md.

## CTR-050: selected-cycle zero-moment preservation is proved, but not yet field transport

The review-side completion
`NavierStokesReview/src/completions/SelectedCycleMasses.lean` now checks the
actual selected recurrence against `ActualCyclePreservation.state_invariant`.
It proves, for every selected stage `j`,
`GaugeMassPreservation.ZeroMassesOn ... (selectedCycle j).state`.
The source path is `ActualCandidateConstruction.lean:35-42,212-214`,
`ActualCyclePreservation.lean:149-159,826-838`, and
`CorrectionStep.lean:9408-9449`.

This rules out one proposed attack: the active correction cycle does not
accidentally lose its two preserved mean-state radial moments at a stage
boundary. It does not prove the public paper's Cartesian five-moment claim.
The selected direct prefix is still a Cartesian `VelocityField`, while
`DefectIncrementBounds.barMoment` consumes a scalar radial profile after torus
averaging. The required curl, cutoff, axis, tail, and projection calculation
remains open. No selected `Delta m ≠ 0` and no selected-path `False` is
recorded.

## 2026-09-26: selected finite production prefix expanded

**IDs:** CTR-005, CALC-27
**Status:** finite cutoff/curl/stage algebra proved; scalar transport remains
open.

`SelectedPotentialProductionFinitePrefix.lean` defines the selected partial
potential for an arbitrary finite prefix `N`. It proves both

$$
\operatorname{curl}(\chi A_N)
=\chi\operatorname{curl}(A_N)
 +(\nabla\chi)\times A_N
$$

and the expansion of `curl A_N` into the finite sum of the individual cut
stage curls. This is the exact production object that must be passed through
the chart, auxiliary torus average, boundary limits, and weighted radial
integral.

The result is selected finite-field evidence, not a sign calculation. It
proves neither a nonzero `Delta m` nor `False`.

| Result | Anchor |
|---|---|
| Partial potential | `SelectedPotentialProductionFinitePrefix.lean:22-26` |
| Stage-curl expansion | `:28-40` |
| Cutoff/curl rule | `:42-53` |
| Combined production expansion | `:55-75` |
| Evidence | `NavierStokesReview/evidence/selected_potential_production_finite_prefix_2026-09-26.md` |

Evidence: `NavierStokesReview/evidence/selected_cycle_mass_preservation_2026-09-25.md`.

## CTR-051: selected angular component is now explicit

The review-side completion
`NavierStokesReview/src/completions/SelectedAngularComponentFormula.lean`
proves the component-one identity for `meanAngularField`: it is the atlas
scalar coefficient multiplied by the first Cartesian component of the
totalised angular frame. This is a concrete refinement of the selected direct
prefix, not a generic witness argument.

The identity still stops before `barMoment`. The coefficient remains expressed
through the physical atlas and radial projection, while `barMoment` requires a
scalar radial profile after torus averaging. The next source-level check must
evaluate that coefficient on a positive-radius band and retain cutoff, curl,
axis, and tail terms. No selected `Delta m ≠ 0` or selected-path `False` has
been proved.

Evidence: `NavierStokesReview/evidence/selected_angular_component_formula_2026-09-25.md`.

## CTR-052: selected direct stages have a positive-radius chart identity

The review-side completion
`NavierStokesReview/src/completions/SelectedDirectPrefixField.lean` now proves
`selected_direct_stage_eq_chart`. After specialising the source theorem to the
selected budget and threshold, each selected direct stage agrees with
`chartDirectStages` on an admissible positive-radius chart.

The transport is source-backed by `ActualCandidateAssembly.lean:553-556` and
`ActualCandidateConstruction.lean:561-572`. It is therefore incorrect to say
that the selected direct stage is only an abstract witness or an uninhabited
limit.

The identity still has a strict boundary. It is not a Cartesian curl formula,
does not cross the axis, and does not identify the vector field with the scalar
radial-profile input consumed by `DefectIncrementBounds.barMoment`. The live
CTR-005 calculation remains: expand the selected coefficient, cutoff
derivatives, curl/connection terms, axis and outer-support terms, and only then
evaluate the radial integral. No selected `Delta m ≠ 0` or kernel `False` has
been proved.

Evidence: `NavierStokesReview/evidence/selected_direct_chart_transport_2026-09-25.md`.

## CTR-053: positive-radius Cartesian-to-radial recovery gate

`SelectedCartesianRadialGate.lean` proves the exact algebraic recovery of the
scalar atlas coefficient from component one of the selected angular field,
under the explicit nonzero first-coordinate hypothesis on the radial chart.
The proof also derives nonvanishing of the Cartesian radius. This is the
strongest new coordinate result, but it is not a `barMoment` theorem: the
selected curl, cutoff derivatives, torus average, axis value, and outer-tail
terms remain outside the identity. No selected `Delta m ≠ 0` or `False` is
recorded.

Evidence: `NavierStokesReview/evidence/selected_cartesian_radial_gate_2026-09-25.md`.

## CTR-054: cutoff--curl commutator is explicit, but its radial value is open

`SelectedCutoffCurlCommutator.lean` now proves the exact local product rule
for a scalar-localised potential:

$$
\operatorname{curl}(\chi A)
=\chi\operatorname{curl}(A)
+\operatorname{curlLinear}\big((D\chi).\operatorname{smulRight}(A)\big).
$$

This matters because `SolenoidalDiagonal.cutStage` applies the scaled cutoff
before `potentialSum`, while `velocitySum` applies the spatial curl afterward.
The derivative-of-cutoff term is therefore part of the selected field-level
calculation. Smoothness and compact support do not make it vanish.

The result is a precise calculation obligation under CTR-005, not a proved
leak: no theorem currently evaluates this commutator through the selected
torus average and `barMoment`, and no selected `Delta m ≠ 0` or `False` has
been derived.

Evidence: `NavierStokesReview/evidence/selected_cutoff_curl_commutator_2026-09-25.md`.

## CALC-21: radial support does not imply cutoff plateau

`SublevelShrinkingSupport` is defined by the radial inequality
`radius w ≤ outerRadius h C w` (`NavierStokes/MixedDiagonalExtensions.lean:99-102`).
The cutoff plateau is the stronger Cartesian condition
`radialSquare x < 1 / 32 ∧ |x 2| < 1 / 8`
(`NavierStokes/SpatialLocalization.lean:133-147`).

The zero-sorry completion
`NavierStokesReview/src/completions/SelectedSupportPredicateScope.lean`
constructs an interface witness with radius zero and axial coordinate one. It
satisfies the radial support predicate for every nonnegative outer-radius
constant but is outside the plateau. The review build completed successfully
with 3716 jobs.

Classification: this closes the predicate implication as an interface
question, not as a selected-field nonzero calculation. It proves that the
native uncut `barMoment` zero cannot be substituted for the production branch
without a selected support-to-plateau theorem. No nonzero `Delta m` and no
kernel `False` are claimed.

Evidence: `NavierStokesReview/evidence/selected_support_predicate_scope_2026-09-25.md`.

## CALC-20: selected support versus cutoff plateau

The source definitions distinguish the selected support condition from the
condition needed to remove the production cutoff. `MixedDiagonalExtensions.SublevelShrinkingSupport`
(`NavierStokes/MixedDiagonalExtensions.lean:99-102`) gives the radial bound
`AnnularEndpoint.radius w ≤ AnnularEndpoint.outerRadius h C w` whenever the
field is nonzero. `AnnularEndpoint.outerRadius` (`AnnularEndpoint.lean:46-48`)
is `C * sqrt (physicalQ h w)`. The selected angular stages satisfy this
predicate at `ActualCandidateConstruction.lean:882-885`.

The cutoff plateau is a different Cartesian predicate:
`radialSquare x < 1 / 32 ∧ |x 2| < 1 / 8`, with `spatialCutoff = 1` proved
only on that set (`NavierStokes/SpatialLocalization.lean:133-147`). The
inspected path contains no theorem transporting the selected similarity-radius
support bound into those Cartesian inequalities.

Classification: **open selected-field calculation gate**, tracked as CALC-20
under CTR-005. The native direct `barMoment` zero therefore cannot yet be
substituted for the cutoff-weighted production moment. This entry does not
establish a nonzero remainder or `False`.

Evidence: `NavierStokesReview/evidence/selected_support_plateau_gate_2026-09-25.md`.

## CTR-005 calculation gate: production direct cutoff

**Status:** OPEN; selected source evidence, not `False`.

The native direct scalar carries the proved zero order-two radial moment, but
the exported mixed field inserts `SpatialLocalization.spatialCutoff` before
periodisation. The zero-sorry completion
`SelectedProductionDirectCutoff.lean` proves on the unit cube:

$$
u_{\mathrm{prod}}=u_{\mathrm{periodic}}+\chi v.
$$

The native moment theorem therefore does not establish the production moment.
The required next calculation is the exact scalar pullback, torus average,
cutoff-gradient commutator, and boundary contribution. No nonzero remainder
has yet been proved.

**Evidence:** `NavierStokesReview/evidence/selected_production_direct_cutoff_2026-09-25.md`.
**Verification:** `lake build NavierStokesReview` passed; the completion has no
`sorry`, custom axiom, or `unsafe`.

## 2026-09-25: selected Cartesian field to `barMoment` interface

The completion `NavierStokesReview/src/completions/SelectedBarMomentInterface.lean`
compiles without `sorry`, custom axioms, or `unsafe` declarations. It proves
that a selected Cartesian component can enter `barMoment` only after supplying
an explicit map

```text
φ : Point P → SpaceTime
```

and a scalar-profile equality

```text
scalarProfile n q = selectedPotentialComponent j (φ q).
```

After those data are present, the theorem expands
`DefectIncrementBounds.barMoment_apply` to the expected torus-average integral.
The production `selected_witness` exports a Cartesian `VelocityField`, but the
source trace has not found a named `φ`, a selected scalar profile, or an equality
transporting the selected `tsum` through `torusAverage` and `barMoment`.

This is a concrete selected-field representation gap under CTR-005. It supports
the publication verdict **NOT ESTABLISHED**, but it is not a nonzero remainder
and does not prove `False`.

Evidence: `NavierStokesReview/evidence/selected_barMoment_interface_2026-09-25.md`.

## Selected physical-point compatibility: 2026-09-25

`SelectedPhysicalPointTransport.lean` corrects the domain description used in
earlier review notes. The chart point and the pressure-stream point are
definitionally compatible when the pressure-stream parameter is `Plane`.
Therefore a raw type-disjointness objection is withdrawn.

The substantive objection remains. The selected endpoint exports Cartesian
stage sums and residual consequences, while `barMoment` consumes a scalar
profile on the pressure-stream lift. The completion proves the `barMoment`
identity after an explicit point-to-spacetime map and scalar-profile equality
are supplied. The selected endpoint still does not export that post-curl,
post-`tsum` equality, nor its torus-average and boundary-limit transport.
This strengthens CTR-005 as a selected-field burden-of-proof failure; it does
not establish a nonzero remainder or `False`.

Evidence: `NavierStokesReview/evidence/selected_physical_point_transport_2026-09-25.md`.

## 2026-09-25: selected positive-stage chart component

`SelectedPotentialChartComponent.lean` compiles without `sorry`, a custom
`axiom`, or `unsafe`.  It proves that the first Cartesian component of the
actual selected positive successor stage reaches the production chart and
splits as `chartWaveParts + chartStreamParts` on the valid chart domain.

Classification: positive selected calculation.  It does not yet identify the
scalar `barMoment` input, evaluate the mixed radial integral, prove
`Delta m ≠ 0`, or derive `False`.

Evidence: `NavierStokesReview/evidence/selected_potential_chart_component_2026-09-25.md`.

The selected first-component completion now makes the commutator concrete:
`(D₁χ)A₂ − (D₂χ)A₁`. This is the next expression to transport into
`barMoment`; its integral has not been evaluated.

## CTR-055: positive-radius selected coefficient recovery

`SelectedRadialSectionComponent.lean` proves a concrete selected-field
identity on the radial section: for positive radius, component one of the
actual `meanAngularField` equals its scalar `meanField` coefficient. The
source path is `ActualMeanStageData.radialSection` together with the actual
`PhysicalMeanJetBounds.angularVector` definition.

The strict hypothesis `r > 0` is substantive. At the axis the source
totalises the angular frame to zero, so coefficient recovery cannot be
extended by algebraic division. The result therefore sharpens the axis term
in CTR-005 but does not establish the full Cartesian-to-`barMoment` identity,
a nonzero `Delta m`, or `False`.

Evidence: `NavierStokesReview/evidence/selected_radial_section_component_2026-09-25.md`.

## CTR-056: selected angular axis branch is explicitly zero

`SelectedRadialAxisBoundary.lean` proves that the first Cartesian component of
the actual selected angular field is zero whenever the two radial Cartesian
coordinates vanish. The same identity is transported to every selected direct
stage. This follows from the production `angularVector` definition and its
totalised divisions; it is not an inferred continuity failure.

Together with CTR-055, the selected radial calculation now has two exact
branches: coefficient recovery for `r > 0` and a zero angular-frame component
on the axis. The unresolved calculation is the full mixed field after cutoff,
curl, torus averaging, and `barMoment`. No nonzero `Delta m` or `False` follows
from the axis result alone.

Evidence: `NavierStokesReview/evidence/selected_radial_axis_boundary_2026-09-25.md`.

## CTR-057: selected mixed velocity has two production summands

`SelectedMixedVelocityDecomposition.lean` proves the exact selected-field
order used by the source:

$$
u_{\mathrm{mixed}}
=\operatorname{curl}\!\left(\sum_j\chi_j A_j\right)
 +\sum_j\chi_j B_j.
$$

`MixedDiagonalResidual.lean:26-29` defines this split, while
`MixedPeriodicAssembly.lean:36-38` localises and periodises the two summands
separately. The direct angular summand is therefore not automatically covered
by a curl product rule. The cutoff commutator remains a valid target for the
potential summand only; the direct summand needs its own radial transport.

This corrects the stronger scratch-space model of the whole selected field as
one curl. It narrows the field-level calculation but does not prove a
nonzero `Delta m` or `False`.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

## CTR-058: selected direct angular stages have zero order-2 radial moment

`SelectedDirectStageMomentTransport.lean` now proves the selected native
angular-stage identity

$$
\operatorname{barMoment}_2(\texttt{angularNativeStages}\;j)=0
$$

on the selected region for every stage index. Stage zero uses the selected
cycle `ZeroMassesOn` theorem. A successor stage is a difference of consecutive
cycle mean-angular fields; the cycle `primitives.mean` data supplies the
smoothness and support needed by
`GaugeDebtIncrement.radialMoment_sub_on`, after which the two state moments
cancel.

This is selected-path evidence, not a generic interface countermodel. It
removes the direct scalar angular branch as a source of a selected nonzero
order-2 radial remainder. It does not identify that scalar moment with the
final mixed Cartesian velocity, evaluate the potential/curl branch, prove a
nonzero `Delta m`, or derive `False`.

Source anchors:

- `NavierStokes/ActualCandidateConstruction.lean:392-394`
- `NavierStokes/CorrectionStep.lean:9446-9448`
- `NavierStokes/MeanStateRegularity.lean:228-246, 339-347`
- `NavierStokes/GaugeDebtIncrement.lean:175-179`
- `NavierStokesReview/src/completions/SelectedDirectStageMomentTransport.lean:31-62`

Evidence: `NavierStokesReview/evidence/selected_direct_stage_moment_transport_2026-09-25.md`.

Build: `elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview`;
3703 jobs completed successfully with no new `sorry`, custom axiom, or
`unsafe` declaration.

## CTR-060: selected positive-radius Cartesian component transport

The review completion `SelectedCylindricalComponentTransport.lean` proves the
exact component identity

```text
(frame θ v) 1 = sin θ * v 0 + cos θ * v 1
```

and transports it through `CyclePhysicalPrefixes.velocity_polar_forward` on
the source valid polar chart. This is selected chart evidence. It does not
identify the mixed selected field with the scalar input of `barMoment`, does
not calculate a nonzero commutator moment, and does not derive `False`.

Source anchors: `NavierStokes/CylindricalResidual.lean:42-50`,
`NavierStokes/CyclePhysicalPrefixes.lean:150-200`, and
`NavierStokesReview/src/completions/SelectedCylindricalComponentTransport.lean:19-37`.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

Build: `elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview`;
3705 jobs completed successfully with no new `sorry`, custom axiom, or
`unsafe` declaration.

## CTR-061: selected base-profile transport

### Question

Is the selected base potential merely a formal placeholder, or is its curl
actually connected to the selected singular velocity branch?

### Source result

`TailGaugePotential.constructedPotential_properties` supplies the selected
`EqOn` curl equality. `FinalSlowBase.axis_tendsto` supplies the source-level
axis norm divergence. `SelectedBaseProfileTransport.lean` transports both
facts to the constructed potential with no admitted proof.

### Disposition

`[x]` base-profile connection established. This does not prove the five-moment
Cartesian-to-scalar bridge and does not yield `Delta m != 0` or `False`.

### Evidence

`NavierStokesReview/evidence/selected_base_profile_transport_2026-09-25.md`;
`NavierStokesReview/src/completions/SelectedBaseProfileTransport.lean:18-39`.

Build: `lake build NavierStokesReview` completed successfully with 3,706 jobs
under the manifest-pinned `leanprover/lean4:v4.34.0-rc2` toolchain; the full
`lake build NavierStokes NavierStokesReview` build completed with 9,605 jobs.

## CTR-062: selected direct component transport is now explicit

`SelectedPhysicalComponentTransport.lean` proves the actual first Cartesian
component of the selected direct branch on a valid chart.  The source map is
not just an abstract frame: after the `swapCylinder` reindexing, the component
contains the graph scale and angular native stage:

$$
u^{\mathrm{direct}}_{j,1}(w)
=\cos(\theta(w))\,Q_n^{-A(h)}
\,a_j\!\left(\operatorname{swapCylinder}\bigl(G_n(\operatorname{polarCoordinates}(w))\bigr)_1\right).
$$

This is selected-path positive evidence.  It closes a component transport
step, but it is not a `barMoment` identity and does not produce a nonzero
remainder or `False`.  The scalar radial operator still requires torus
averaging, axis/support limits, and the potential/curl branch.

Source anchors: `NavierStokes/CyclePhysicalPrefixes.lean:32-38, 158-178`,
`NavierStokes/PhysicalCurlCovariance.lean:666-726`,
`NavierStokes/PhysicalResidualTZ.lean:44-51, 385-419`,
`NavierStokes/ActualCandidateConstruction.lean:358-406, 543-566`, and
`NavierStokesReview/src/completions/SelectedPhysicalComponentTransport.lean:20-94`.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

Verification: standalone Lean compilation under the manifest-pinned
`leanprover/lean4:v4.34.0-rc2` exited `0` with no admitted proof. The combined
`lake build NavierStokes NavierStokesReview` also exited `0` after 9,606 jobs;
the endpoint reported only `[propext, Classical.choice, Quot.sound]`.

## CTR-059: selected potential-stage chart transport

`SelectedPotentialStageChartTransport.lean` now proves the selected
potential-stage curl equality on the actual Cartesian chart domain. For every
selected stage index satisfying the source residual-band condition, the curl
of `selectedPotentialStages k` agrees on that domain with the corresponding
`CyclePhysicalPrefixes.potentialParts` field supplied by
`ActualPhysicalPrefixFields.StageRealizations`.

Source anchors:

- `NavierStokes/SolenoidalDiagonal.lean:111-126, 318-327` for the cut
  potential, potential sum, and velocity curl;
- `NavierStokes/ActualCandidateAssembly.lean:531-533` for the selected
  potential-stage definition;
- `NavierStokes/ActualCandidateAssembly.lean:911-938, 1025-1056,
  1059-1082, 1165-1168` for chart potentials, chart transport, and selected
  aliases;
- `NavierStokes/ActualPhysicalPrefixFields.lean:342-356` for the stage
  realization field;
- `NavierStokesReview/src/completions/SelectedPotentialStageChartTransport.lean:21-44`
  for the review theorem.

This is selected-path field evidence. It closes a local chart equality only.
It does not prove that the potential branch has a nonzero radial `barMoment`,
does not supply the torus-average, axis, support, or boundary transport, and
does not establish `Delta m ≠ 0` or `False`.

Evidence: `NavierStokesReview/evidence/selected_potential_stage_chart_transport_2026-09-25.md`.

Build: `elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview`;
3704 jobs completed successfully with no new `sorry`, custom axiom, or
`unsafe` declaration.

## 2026-09-25 selected direct radial moment bridge

`SelectedDirectRadialMomentBridge.lean` composes the selected radial-section
component theorem with the selected cycle moment invariant.  For the actual
selected direct stage, its first Cartesian component on the positive radial
section equals the native angular scalar.  Expanding `barMoment_apply` then
gives the exact identity

$$
\int_{\mathbb R} r^2\operatorname{torusAverage}(a_j(n))(r,s)\,dr=0
$$

on the selected carrier.  This is positive selected-field evidence for the
direct branch.  It is not the moment of the full endpoint, whose production
order remains `curl(potential sum) + direct sum`; the potential/curl branch and
its boundary terms remain the live falsification target.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.
Build: standalone Lean compilation exited `0`; no `sorry`, custom axiom, or
`unsafe` declaration was introduced.

## CTR-063: selected graph value versus torus-average input

The source now fixes the remaining representation question precisely. The
selected radial construction in `ActualMeanStageData.radialSection`
(`NavierStokes/ActualMeanStageData.lean:23-24`) samples one positive-radial
section with the second Cartesian coordinate set to zero. Its transport
lemmas (`:42-63`) prove equality of that graph sample with the corresponding
physical field value.

The moment interface has a different domain. `PressureStream.torusAverage`
(`NavierStokes/PressureStream.lean:66-71`) integrates over both auxiliary
coordinates `Y : Plane`, and `DefectIncrementBounds.barMoment_apply`
(`NavierStokes/DefectIncrementBounds.lean:214-220`) uses that average inside the
radial integral. No selected-path theorem currently identifies the graph
sample with this full auxiliary average for the curled potential branch.

This is a concrete selected-field bridge still required by CTR-005. It is not
evidence that the average is nonzero, and it does not establish `False`.

Evidence: `NavierStokesReview/evidence/selected_torus_average_representation_gap_2026-09-25.md`.

## 2026-09-25 selected stream-to-curl transport

`SelectedStreamCurlChartTransport.lean` specialises
`ActualCandidateAssembly.stream_on_chart` to the selected construction. It
proves that the actual scalar mean stream is transported into the selected
Cartesian potential branch by spatial curl on the production chart. This
closes the source-to-vector step, but not the vector-to-scalar torus-average
step required by `barMoment_apply`.

Evidence: `NavierStokesReview/evidence/selected_stream_curl_chart_transport_2026-09-25.md`.
Verification: standalone Lean compilation exited `0`; no `sorry`, custom
axiom, or `unsafe` declaration.

## 2026-09-25 selected rank/stream moment scope

The selected rank correction is active in the production stream. The source
defines `rankNative` through `VariableGaugeMean.rankPotential`
(`ActualCandidateConstruction.lean:459-462`), adds it to the temporal stream
(`:464-470`), and identifies successor stages with `streamFamily`
(`:492-494`). `LocalRankDefect.desired_mass_zero`
(`LocalRankDefect.lean:590-604`) is consumed by the rank-potential
construction, with the fixed-stream identity at `:606-618`.

The combined stream is exported through `CycleData.stream_moving`
(`ActualMeanPhysicalData.lean:915-917`) as `MovingField`, whose structure is
limited to smoothness, support, and periodicity
(`GaugeMomentBalances.lean:460-466`). The selected curl transport is proved,
but the audited path still contains no identity from that curled mixed field
to the scalar `torusAverage` input used by `barMoment_apply`
(`DefectIncrementBounds.lean:214-220`).

Classification: selected source evidence for CTR-005. The rank route is not
dead code, but its full five-moment meaning is not established at the exported
field. No nonzero remainder and no kernel `False` are claimed.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.
Verification: `lake build NavierStokesReview` completed successfully with
3711 jobs; the new completion contains no `sorry`, custom axiom, or `unsafe`.

## CTR-005 calculation gate: selected cut-stage curl

The production potential branch applies `SolenoidalDiagonal.cutStage`
(`NavierStokes/SolenoidalDiagonal.lean:31-33`) before forming `potentialSum`
(`:37-42`) and before applying `velocitySum` (`:188-190`). The review theorem
`selected_cut_stage_curl_expansion` in
`NavierStokesReview/src/completions/SelectedCutStageCurlScope.lean:21-38`
expands the selected stage as

$$
\operatorname{curl}(\chi A)=\chi\,\operatorname{curl}(A)
 +(\nabla\chi)\times A.
$$

The second term is an explicit cutoff-gradient commutator. It is not removed
by definitional equality. The theorem does not establish that its radial
moment is nonzero, so this entry records a calculation gate, not `Delta m ≠ 0`
and not `False`.

Evidence: `NavierStokesReview/evidence/selected_cutoff_curl_commutator_2026-09-25.md`.
## CALC-22: selected graph image versus auxiliary torus domain

**Date:** 2026-09-25
**Classification:** selected source/interface evidence; not `Δm ≠ 0` and not `False`
**Evidence:** `NavierStokesReview/evidence/selected_torus_lift_image_scope_2026-09-25.md`

`PressureStream.torusAverage` integrates both auxiliary coordinates over
$[0,1]$ (`NavierStokes/PressureStream.lean:66-71`). `barMoment` consumes that
average (`NavierStokes/DefectIncrementBounds.lean:214-220`). The selected
physical graph instead uses `absoluteLift`
(`NavierStokes/PhysicalResidualBridge.lean:645-649`) whose auxiliary component
is a radial-direction term with nonnegative coefficient, plus a time-direction
term. `commonGraph_eq_physicalToChart`
(`NavierStokes/PhysicalResidualBridge.lean:651-654`) applies only on the
positive-radius chart.

The zero-sorry completion
`SelectedTorusLiftImageScope.lean:26-105` constructs a linear functional `ρ`
with `ρ radialDirection = 1` and `ρ timeDirection = 0`. It proves that every
positive-radius `absoluteLift` image has `ρ ≥ 0`, while the point
`(0, 1 / 2)` lies in the auxiliary integration square and has `ρ < 0`.
Consequently the selected graph image does not cover the full auxiliary domain
used by `torusAverage`. The same separation is proved for the actual
production sampling map `PhysicalMeanJetBounds.physicalPoint`, not only for
the lower-level `absoluteLift` representation.

## CALC-23: raw scalar-family sampling is non-injective

`ActualMeanPhysicalData.Scalar` is a family on the full point domain, while
`meanField` samples through `PhysicalMeanJetBounds.physicalPoint`. The new
zero-sorry completion `SelectedScalarSamplingNonuniqueness.lean:22-58`
constructs an off-image family that vanishes on every production sample but is
nonzero at the explicit missed point. Thus the plain sampling map does not
determine the raw scalar family entering `barMoment`.

This is a selected interface result, not a selected nonzero moment. The
remaining question is whether the source proves uniqueness after imposing the
actual smoothness, overlap, support, and validity hypotheses. That question is
tracked as CALC-24.

Evidence: `NavierStokesReview/evidence/selected_scalar_sampling_nonuniqueness_2026-09-25.md`.

## CALC-24: uniqueness in the selected admissible class

The plain `ScalarFamily` counterexample does not by itself satisfy the
selected smoothness, overlap, support, or validity records. The next proof
must either establish that those records determine the scalar family on the
full `barMoment` domain, or construct two admissible selected families with
identical production pullbacks and different moments. Until one of those
results exists, the audit has a concrete interface obstruction but not a
selected `Delta m` inequality or kernel `False`.

**Finding:** an explicit extension or auxiliary-coordinate invariance theorem
is required before the selected physical chart can be identified with the
scalar field integrated by `barMoment`. This is a concrete transport mismatch,
not a proof that the selected weighted moment is nonzero. The interface result
is complete; the selected scalar equality remains open under `CALC-23`.

## CALC-25: valid-band observation boundary

`SelectedAtlasPhysicalErasure.lean` proves, with zero `sorry`, that
`Atlas.physical` is unchanged when two native scalar families agree at every
valid chart sample. This follows directly from the selected map's valid-band
branch and its zero branch when no valid band exists.

This does not imply equality of the native `barMoment`: `barMoment` integrates
the raw scalar family over the full torus-average domain. The remaining
selected obligation is CALC-26: prove coverage or prove that values outside
the valid chart samples contribute zero. No `Δm ≠ 0` or `False` claim is made.

Evidence: `NavierStokesReview/evidence/selected_atlas_physical_erasure_2026-09-25.md`.

## CALC-27: atlas zero-extension at the domain boundary

`SelectedAtlasDomainBoundary.lean` proves the selected atlas fact

$$z.2.1.1\le0\Longrightarrow
\operatorname{Atlas.physical}(A,U,d,f,z)=0.$$

The proof unfolds `Atlas.physical`. Its nonzero branch would provide an index
`n` with `Atlas.Valid U z n`, while `Atlas.Valid` contains the strict premise
`0 < z.2.1.1`. This is a zero-sorry selected-production result, not a generic
countermodel.

The result sharpens the active transport gate. `barMoment` consumes a native
scalar family over the full lifted domain, while the production atlas
zero-extends outside its positive-validity samples. The current evidence does
not prove that the native selected scalar is nonzero on the omitted region or
that the omitted region contributes a nonzero torus average. Therefore this
entry does not establish `Delta m ≠ 0` or `False`.

| Source | Anchor |
|---|---|
| `Atlas.Valid` | `NavierStokes/ActualMeanPhysicalData.lean:96` |
| `Atlas.physical` | `NavierStokes/ActualMeanPhysicalData.lean:125` |
| `physicalPoint` | `NavierStokes/PhysicalMeanJetBounds.lean:24` |
| `torusAverage` | `NavierStokes/PressureStream.lean:70` |
| `barMoment` | `NavierStokes/DefectIncrementBounds.lean:214` |
| Proof and build record | `NavierStokesReview/evidence/selected_atlas_domain_boundary_2026-09-25.md` |

## 2026-09-25 selected direct production scalar gate

The production direct branch has now been reduced to an exact selected
component identity. `ActualCandidateAssembly.directStages` is identified with
the native angular mean stages at `ActualCandidateAssembly.lean:553-556`.
The production field applies `SpatialLocalization.cutPotential`, whose source
definition multiplies by `spatialCutoff` before periodisation
(`SpatialLocalization.lean:164-172`). The zero-sorry completion
`SelectedProductionDirectScalarGate.lean:21-46` proves, on the positive radial
section, that

$$
(\operatorname{cutPotential}(D_j))_1=\chi(r,z)m_j(r,z),
\qquad
\chi(r,z)=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z).
$$

The native order-two `barMoment` zero applies to `m_j` before this weighting.
It does not remove `χ` from the production field and does not establish that
the weighted integral is zero. This is a concrete selected-field calculation
under CTR-005. The unresolved quantity is the selected weighted remainder,
not merely the name of a missing theorem.

Evidence: `NavierStokesReview/evidence/selected_production_direct_scalar_gate_2026-09-25.md`.

Classification: selected source identity; no `Delta m != 0` or `False` claim.

## CTR-063: selected direct atlas pullback

The selected direct component has now been identified beyond the native-stage
name. `ActualCandidateAssembly.directStages_eq` transports it to
`ActualCandidateConstruction.angularMeanStages`; unfolding the latter shows
that its first Cartesian component is the atlas physical value at
`PhysicalMeanJetBounds.physicalPoint`, multiplied by the first component of
the angular frame. Applying `SpatialLocalization.cutPotential` adds the
production factor `spatialCutoff`.

On the radial section this is the concrete expression

$$
\chi(r,z)m_j(r,z),\qquad
\chi(r,z)=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z).
$$

This closes a selected source identity that was previously only described as
a missing bridge. It still does not evaluate the atlas scalar through
`torusAverage` and `barMoment`, and it does not prove a nonzero weighted
remainder or `False`.

| Source | Anchor |
|---|---|
| Direct branch | `NavierStokes/ActualCandidateAssembly.lean:536-538` |
| Direct-to-native equality | `NavierStokes/ActualCandidateAssembly.lean:553-556` |
| Atlas-backed mean field | `NavierStokes/ActualCandidateConstruction.lean:355-366` |
| Production cutoff | `NavierStokes/SpatialLocalization.lean:164-172` |
| Zero-sorry completion | `NavierStokesReview/src/completions/SelectedProductionDirectAtlasPullback.lean:22-68` |
| Evidence | `NavierStokesReview/evidence/selected_production_atlas_pullback_2026-09-25.md` |

Classification: selected source identity; the affirmative calculation remains
open under CTR-005.
## CALC-31: selected potential partial-curl transport

The review completion
`NavierStokesReview/src/completions/SelectedPotentialPrefixCurlExpansion.lean`
proves that the selected potential velocity is locally equal, in the
neighbourhood filter of every preterminal point, to the spatial curl of a
finite partial potential. The proof composes the selected finite-prefix
identity with `SolenoidalDiagonal.spatialCurl_eventuallyEq`.

This is a selected field identity. It does not yet expand the finite curl into
stage curls on the same open set, and it does not identify the resulting field
with a radial scalar consumed by `barMoment`. No nonzero remainder or `False`
claim follows from it.

| Source | Anchor |
|---|---|
| Selected theorem | `NavierStokesReview/src/completions/SelectedPotentialPrefixCurlExpansion.lean:24-48` |
| Finite-prefix input | `NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean:34-55` |
| Curl transport | `NavierStokes/SolenoidalDiagonal.lean:238-244` |
| Build record | `NavierStokesReview/evidence/selected_potential_partial_curl_2026-09-25.md` |

Classification: selected source identity; stagewise radial transport remains
open under CTR-005.

## CALC-32: selected stagewise curl on the physical domain

The new completion
`NavierStokesReview/src/completions/SelectedPotentialStagewiseCurlOnPhysicalDomain.lean`
uses the selected schedule, the open `physicalDomain`, the positive similarity
coordinate, and the exported stage smoothness theorem to prove a concrete
finite stagewise-curl expansion for the selected potential velocity. This is a
selected source identity, not an abstract interface claim.

The corresponding evidence is
`NavierStokesReview/evidence/selected_potential_stagewise_curl_2026-09-25.md`.
The expansion exposes the product-rule term `(∇χ) × A` in every cutoff curl.
No theorem in the selected path currently evaluates that term through
`torusAverage` and `barMoment`, and no nonzero remainder or `False` follows
yet. CALC-32 is therefore `[x]` for the finite field identity and CALC-06/
CALC-07 remain open for the value and contradiction.

## 2026-09-25: selected direct atlas scalar representative

The selected direct branch now has an explicit scalar representative in
`NavierStokesReview/src/completions/SelectedDirectAtlasScalarRepresentative.lean`.
The definition uses `ActualMeanPhysicalData.Atlas.physical` on the lifted point
domain consumed by `DefectIncrementBounds.barMoment`. A zero-sorry completion
proves the pullback identity from `ActualCandidateConstruction.meanField`, the
`barMoment_apply` radial-integral expansion, and equality with component one of
the selected direct stage on the positive-radius radial section.

This closes the exact scalar-definition ambiguity. It does not yet evaluate
the mixed selected field, the cutoff-weighted curl commutator, or the final
`tsum`; consequently it supplies no `Δm ≠ 0` and no `False`.

Evidence: `NavierStokesReview/evidence/selected_direct_atlas_scalar_representative_2026-09-25.md`.
## 2026-09-25: selected direct native finite-prefix moment

`SelectedDirectNativePrefixMoment.lean` closes the finite-prefix calculation
for the selected native direct scalar. The proof telescopes the sum of
`angularNativeStages` to `(selectedCycle J).state.mean.angular n` and then
uses the selected cycle invariant to prove order-two `barMoment = 0` on the
selected carrier.

This is a source-level selected identity, not a generic interface argument.
It is also deliberately scoped before production spatial localisation, the
Cartesian potential/curl branch, auxiliary torus averaging, and the final
`tsum`. Consequently it clears the native direct prefix as a source of a
remainder but does not establish weighted mixed-field moment zero, a nonzero
`Δm`, or `False`.

| Source | Anchor |
|---|---|
| Native stage and successor | `NavierStokes/ActualCandidateConstruction.lean:392-394, 406-411` |
| New completion | `NavierStokesReview/src/completions/SelectedDirectNativePrefixMoment.lean:22-53` |
| Cycle moment transport | `NavierStokesReview/src/completions/SelectedDirectStageMomentTransport.lean:32-54` |
| Evidence | `NavierStokesReview/evidence/selected_direct_native_prefix_moment_2026-09-25.md` |

Build status: focused Lean check exited 0 with no `sorry`, custom axiom, or
`unsafe` declaration in the new review file.

Classification: selected native-prefix identity complete; selected mixed
scalar evaluation remains open under CTR-005.

## 2026-09-25: selected production direct cutoff identity

`SelectedProductionDirectPrefixCutoff.lean` advances the selected-field
calculation past the native direct prefix. For every finite prefix, the
production direct component is exactly the native prefix multiplied by
`SpatialLocalization.spatialCutoff`. On the positive-radius radial section it
therefore equals the selected cycle mean field multiplied by that cutoff.

The same completion proves the exact algebraic shell defect

$$
\sum_{j\leq J}(\chi u_j)_1-\sum_{j\leq J}(u_j)_1
=(\chi-1)\sum_{j\leq J}(u_j)_1.
$$

This is a selected production identity, not a generic cutoff warning. It
shows why the native `barMoment = 0` result cannot be transferred without
evaluating the weighted shell term. The current source trace provides only
positivity and ordering of the moving annulus radii, not an inequality placing
the selected annulus relative to the fixed cutoff and not a selected nonzero
cycle value. Accordingly, no `Δm ≠ 0` or `False` is recorded.

| Source | Anchor |
|---|---|
| New completion | `NavierStokesReview/src/completions/SelectedProductionDirectPrefixCutoff.lean:26-79` |
| Native stages | `NavierStokes/ActualCandidateConstruction.lean:392-401,425-437` |
| Cutoff | `NavierStokes/SpatialLocalization.lean:41-49,165-171` |
| Evidence | `NavierStokesReview/evidence/selected_production_direct_prefix_cutoff_2026-09-25.md` |

Build status: focused Lean check exited `0` with no `sorry`, custom axiom, or
`unsafe` declaration in the new review module.

Classification: selected shell-defect identity complete; selected weighted
radial value and contradiction remain open under CTR-005.

## 2026-09-25: selected potential production product rule

**IDs:** CTR-005, CALC-04, CALC-05
**Status:** selected source identity proved; selected radial sign unresolved.

The zero-sorry completion
`NavierStokesReview/src/completions/SelectedPotentialProductionProductRule.lean`
specialises the production branch on the unit cube. It proves that the
periodised selected potential field is the spatially cut curl plus the exact
cutoff/curl commutator

$$
\operatorname{curl}(\chi A)=\chi\operatorname{curl}(A)
  +\operatorname{curlLinear}(D\chi\,A).
$$

This selected-field result prevents the native curl from being substituted for
the exported field before localisation. The commutator has not been shown to
have a nonzero selected radial integral. The next load-bearing calculation is
its transport through the atlas, torus average, `barMoment`, and final `tsum`.

**Evidence:** `NavierStokesReview/evidence/selected_potential_production_product_rule_2026-09-25.md`.

## 2026-09-25: selected potential production radial scalar

**IDs:** CTR-005, CALC-04, CALC-05
**Status:** selected positive-radius scalar transport proved; full radial
observable remains open.

`SelectedPotentialProductionRadialScalar.lean` extends the preceding product
rule to the actual source radial section. It defines the first component of
the selected localised potential production field and proves

$$
V_{\mathrm{prod},1}=\chi(\operatorname{curl}A)_1
 +\bigl(\operatorname{curlLinear}(D\chi\,A)\bigr)_1.
$$

The differentiability premise is derived from the selected schedule,
`ActualCandidateAssembly.stages_smooth`, and
`SolenoidalDiagonal.potentialSum_contDiffOn` on the selected physical domain.
This closes a concrete local transport gate. It does not provide the
point-to-spacetime map needed by the full `barMoment` domain, nor does it prove
that the commutator has a nonzero weighted radial integral.

| Item | Location |
|---|---|
| Review completion | `NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean:28-136` |
| Radial section | `NavierStokes/ActualMeanStageData.lean:23-24` |
| Product rule | `NavierStokes/SpatialLocalization.lean:200-207` |
| Evidence | `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md` |

Focused Lean check exited `0` with no `sorry`, custom axiom, or `unsafe`
declaration in the new review completion. Classification: selected transport
identity complete; selected `barMoment` value and contradiction remain open.

## 2026-09-25: positive-radius lift compatibility rechecked

**IDs:** CTR-005, CALC-22, CALC-25
**Status:** local type and chart compatibility confirmed; endpoint moment
transport remains open.

The source recheck found an authenticated local bridge. `PhysicalResidualTZ.Lift`
is definitionally `R × (Plane × Plane)`, the same product used by
`PressureStream.Lift PhysicalGraphBounds.Plane`. On positive radius,
`ActualMeanPotentialRealization.physicalPoint_forward` identifies the mean
physical point with `PhysicalResidualTZ.absoluteLiftTZ`, and
`ActualCandidateAssembly.stageRealizations` transports each selected stage curl
to its chart field.

This does not identify the final localised `tsum` with a scalar input to
`DefectIncrementBounds.barMoment`. The cutoff-gradient commutator, torus
average, axis and outer-support terms, and the final weighted value remain
unproved on the selected endpoint. No `Δm ≠ 0` or `False` is recorded.

| Source | Anchor |
|---|---|
| Slow-coordinate lift | `NavierStokes/PhysicalResidualTZ.lean:19-21,385-452` |
| Mean potential point and forward equality | `NavierStokes/ActualMeanPotentialRealization.lean:20-27,331-358` |
| Selected stage chart transport | `NavierStokes/ActualCandidateAssembly.lean:1059-1088` |
| Radial observable | `NavierStokes/DefectIncrementBounds.lean:214-220` |

## 2026-09-26: selected production scalar given the exact `barMoment` type

**IDs:** CTR-005, CALC-26
**Status:** selected local section bridge proved; full mixed endpoint remains
open.

The review completion
`NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean`
defines a section from the physical moment point
`PressureStream.Lift PhysicalResidualBridge.Plane` to the positive-radial
cylindrical coordinates. It lifts the selected potential-production
component into the exact `ScalarField` type consumed by
`DefectIncrementBounds.barMoment`, and proves the literal integral expansion

$$
\operatorname{barMoment}_k(F_a)(n,p)=
\int r^k\,\operatorname{torusAverage}(F_{a,n})(r,p)\,dr.
$$

The file also proves that the section agrees with the source physical-point
map on `ActualMeanStageData.radialSection p` when `0 < p.2.1`. This removes a
type-level ambiguity, but it does not provide a global inverse for
`physicalPoint` and does not identify the full mixed selected Cartesian field
with `F_a`.

| Result | Anchor |
|---|---|
| `MomentPoint` and section | `SelectedPotentialProductionBarMomentSection.lean:31-38` |
| Pointwise and `barMoment` expansions | `:40-49` |
| Physical radial-section compatibility | `:54-63` |
| Pullback to the selected radial scalar | `:65-72` |
| Evidence | `NavierStokesReview/evidence/selected_potential_production_barmoment_section_2026-09-26.md` |

Focused Lean check exited `0`; the review file adds no `sorry`, custom axiom,
or `unsafe` declaration. The selected weighted value, boundary terms, final
`tsum` transport, and any Delta m != 0 remain unproved. CTR-005 therefore
remains the load-bearing publication objection, while no kernel `False` is
recorded.

## 2026-09-26: finite-prefix moment interface extended

**IDs:** CTR-005, CALC-27, CALC-29
**Status:** selected finite-prefix scalar transport proved; endpoint evaluation
remains open.

`SelectedPotentialProductionFinitePrefix.lean` now defines the concrete partial
selected potential for a finite prefix `N`, expands its stage curls, and retains
the cutoff-gradient commutator. It also defines
`selectedPotentialPartialProductionPointScalar a N` on the exact lifted point
type consumed by `DefectIncrementBounds.barMoment`.

The zero-sorry theorems provide the literal `barMoment` integral expansion and
the positive-radius pullback to the selected physical section. This is a
field-level completion of the finite interface, not a generic type critique.
The torus-average value, axis and tail contributions, infinite `tsum` passage,
and selected weighted remainder are not yet evaluated. No `Delta m != 0` and no
kernel `False` is recorded.

| Result | Anchor |
|---|---|
| Partial potential and stage expansion | `SelectedPotentialProductionFinitePrefix.lean:22-75` |
| Finite `barMoment` application | `:77-94` |
| Physical pullback | `:96-108` |
| Finite production formula | `:110-145` |
| Evidence | `NavierStokesReview/evidence/selected_potential_production_finite_prefix_2026-09-26.md` |

## 2026-09-26: finite-prefix torus-average reduction

**ID:** CALC-34
**Related finding:** CTR-005
**Status:** verified local identity; selected endpoint still open

`SelectedPotentialProductionTorusAverage.lean` proves that the lifted
finite-prefix production scalar factors through `pointToCyl`. Since that map
does not inspect the auxiliary `Plane` coordinate, the two interval integrals
in `PressureStream.torusAverage` reduce exactly. The theorem also rewrites
`DefectIncrementBounds.barMoment` as the weighted radial integral of the
finite-prefix production scalar.

| Result | Anchor |
|---|---|
| Torus-average reduction | `SelectedPotentialProductionTorusAverage.lean:22-29` |
| Radial `barMoment` reduction | `SelectedPotentialProductionTorusAverage.lean:31-40` |
| Evidence | `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md` |
| Full build | `lake build NavierStokesReview`, exit `0`, 3732 jobs |

This result concerns the review-side finite-prefix scalar. It does not
identify that scalar with the complete mixed Cartesian field exported by
`selected_witness`, evaluate the remaining radial integral, or prove a
nonzero remainder. No `Delta m != 0` and no kernel `False` is recorded.

## 2026-09-26: source-confirmed axis similarity scale

**ID:** CALC-35
**Related finding:** CTR-005
**Status:** verified source identity; field-level moment consequence open

`NavierStokes/AxisPreservation.lean:130-148` proves, for `0 < h < 1/2` and
`t < 1`,

$$
\operatorname{physicalQ}(h,(t,0))=1-t,
$$

and proves its limit to zero through `physicalQ_origin_tendsto`. The result
comes from the defining `coordinateQ` equation at axial coordinate zero, not
from an empty filter or an endpoint convention.

This closes one axis-coordinate premise. It does not prove that the selected
Cartesian `tsum` has a nonzero value on that axis, nor does it evaluate the
axis or tail terms in `barMoment`. The active calculation therefore remains
the selected Cartesian-to-radial bridge.

## 2026-09-26: finite-cutoff plateau pulled to the axis endpoint

**IDs:** CTR-005, CALC-28, CALC-36
**Status:** verified finite-prefix endpoint identity; infinite-prefix value open

`SelectedFiniteCutoffEndpoint.lean:26-43` composes the source theorem
`AxisPreservation.physicalQ_origin_tendsto` with
`SmoothCutoffs.finite_scaledCutoffs_eventually_one`. For every fixed `N`, it
proves that, on a left neighbourhood of `t = 1`,

$$
\forall j<N,\qquad
\operatorname{scaledCutoff}(a_j,\operatorname{physicalQ}(h,(t,0)))=1.
$$

This is a genuine selected finite-prefix fact. Its neighbourhood depends on
the finite prefix, so it does not establish a uniform statement in `N` and
does not evaluate the selected `tsum`. The Cartesian curl, torus average,
weighted `barMoment`, and any `Delta m != 0` remain open. No `False` follows.

| Result | Anchor |
|---|---|
| Source finite plateau | `NavierStokes/SmoothCutoffs.lean:171-186` |
| Source axis scale | `NavierStokes/AxisPreservation.lean:130-148` |
| Review theorem | `NavierStokesReview/src/completions/SelectedFiniteCutoffEndpoint.lean:26-43` |
| Evidence | `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md` |

## 2026-09-26: infinite-sum endpoint scope

**IDs:** CTR-005, CALC-36
**Status:** open selected transport calculation

`SolenoidalDiagonal.potentialSum_eventuallyEq_partial` and
`potentialSum_allJets_eventuallyEq_partial` require a strict positive scale at
the point under consideration. The new endpoint completion instead proves a
finite-prefix cutoff plateau as the selected axis scale tends to zero. No
theorem yet transports that finite-prefix fact to the infinite `potentialSum`,
the Cartesian curl, the torus average, or `barMoment` at the endpoint.

This is a load-bearing selected-field obligation, not a proof that the sum
fails. The tracker therefore records no nonzero remainder, PDE failure, or
kernel `False` from this fact alone.

| Evidence | `NavierStokesReview/evidence/selected_tsum_endpoint_scope_2026-09-26.md` |

## 2026-09-26 update: selected production `tsum` scope

A zero-sorry review completion,
`SelectedPotentialProductionTsumScope.lean`, specialises the source theorem
`SolenoidalDiagonal.potentialSum_allJets_eventuallyEq_partial` to the actual
selected potential stages. Under the source convergence and positive-scale
hypotheses, one finite prefix represents every derivative locally. This closes
only the local infinite-sum reduction.

It does not supply the global Cartesian-to-scalar transport required by
`torusAverage`/`barMoment`, does not evaluate the axis or tail contribution,
and does not establish `Delta m != 0` or `False`. CTR-005 and CALC-38 remain
open selected-field correspondence obligations.

Evidence:
`NavierStokesReview/evidence/selected_potential_production_tsum_scope_2026-09-26.md`.

### CALC-37 control entry: 2026-09-26

`SelectedMixedVelocityFinitePrefix.lean` compiles without `sorry` or `unsafe`.
It proves that the selected mixed velocity has separate finite local
representatives for its curl-generated potential branch and its direct branch
on the source physical domain. The prefix indices are independent. This
closes the finite local field trace, but not the selected endpoint `tsum`, a
common prefix, the torus average, the weighted radial integral, or five-moment
transport.

This is a stronger selected-path correspondence result, not a nonzero
remainder or a kernel contradiction.

| Evidence | `NavierStokesReview/evidence/selected_mixed_velocity_finite_prefix_2026-09-26.md` |

## CALC-38a: periodic Cartesian field versus bounded radial support

The review completion `PeriodicRadialSupportObstruction.lean` compiles without
`sorry` and proves that unit periodicity in a radial coordinate together with
bounded radial support forces the scalar field to vanish. The pullback theorem
requires the actual Cartesian-to-radial map and an explicit
`RadiallySupported` premise.

This does not establish that the selected field has that support, so it does
not prove a zero selected field, a nonzero `Delta m`, or `False`. It records a
precise transport obligation between the periodised Cartesian construction and
the scalar field consumed by `barMoment`.

Evidence: `NavierStokesReview/evidence/periodic_radial_support_obstruction_2026-09-26.md`.

## 2026-09-26: selected mixed radial component

**IDs:** CTR-005, CALC-38b

`SelectedMixedProductionRadialComponent.lean` compiles without `sorry`,
custom axioms, or `unsafe`. It proves that the first Cartesian component of
the selected mixed periodic velocity splits into the potential production
scalar plus the first component of the periodised, cut direct branch. The
result is a source-level decomposition only. It does not prove that the
direct summand has a nonzero weighted radial integral, nor that either branch
is the scalar input expected by `barMoment`.

**Classification:** verified transport boundary; no selected-field numerical
mismatch and no kernel-level contradiction.

**Evidence:** `NavierStokesReview/evidence/selected_mixed_production_radial_component_2026-09-26.md`.

## CALC-38c: mixed endpoint `barMoment` transport

`SelectedMixedProductionBarMoment.lean:34-59` defines the first Cartesian
component of the actual mixed selected field on the scalar-family domain
consumed by `DefectIncrementBounds.barMoment`. Lean verifies the exact radial
integral reduction and the positive-radius pullback to the physical radial
section. This resolves the domain/typing interface left open by CALC-38b.

It does not evaluate the weighted integral, prove a sign or nonzero value for
the periodised cut direct branch, identify the result with `(M, I, J, S, C_p)`,
or derive `False` against `selected_candidate`.

**Classification:** verified mixed-field observable interface; no numerical
selected-field mismatch and no kernel-level contradiction.

**Evidence:** `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

## CALC-38e: exact mixed radial reduction

`SelectedMixedProductionBranchSplit.lean:32-48` defines the cut, periodised
direct scalar and proves the pointwise potential-plus-direct split.
`SelectedMixedProductionTorusAverage.lean:25-41` then reduces the auxiliary
torus average and `barMoment` to the literal mixed weighted radial integral.
The result is zero-sorry and source-typed, but its value is not evaluated.

**Classification:** verified radial reduction; no nonzero remainder and no
kernel-level contradiction.

**Evidence:** `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

## CALC-38g: mixed radial periodicity

`SelectedMixedRadialPeriodicity.lean:28-70` proves that the actual mixed
radial pullback entering the exposed `barMoment` integral is unit-periodic.

**Classification:** verified radial periodicity; no numerical selected-field
mismatch and no kernel-level contradiction.

**Evidence:** `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

## SRC-08: selected-witness packaging boundary

Source review confirms Copilot's path correction. `selected_witness` at
`NavierStokes/ActualCandidateAssembly.lean:1177-1185` destructures the
`CandidateProperties` structure as `hc`; `candidateStatement` is the outer
existential definition. The `hc` record exports regularity, support,
divergence, residual equality, energy, and speed-unboundedness, but no named
five-moment or `barMoment` transport field. `R3/ActualCandidate.lean:78-122`
then uses local compactification and the smooth positive-time force cutoff.
This is a selected-path correspondence/provenance boundary, not evidence that
the energy theorem is absent and not a kernel contradiction.

| Check | Result |
|---|---|
| `hc` source | `selected_witness` component of `CandidateProperties` |
| Energy source | `R3/CompactEnergy.lean:343`; used at `R3/ActualCandidate.lean:119` |
| Whole-space force | `PositiveTimeForce.force (R3CompactCandidate.compactForce f)` |
| Five-moment export | Not present in `hc` or `CandidateProperties` |
| `False` | Not derived |

## SRC-09: R3 packaging non-implication

`SelectedR3PackagingBoundary.lean` compiles without `sorry`, `axiom`, or
`unsafe`. It proves that the exported R3 `CandidateProperties` witness can
coexist with a nonzero `Fin 5 → ℝ` payload. This is a type-boundary result:
it demonstrates that the R3 predicate does not itself export five-moment
transport. It is not a calculation of the selected field's moments and does
not establish `Delta m != 0` or `False`.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.

## 2026-09-26 source-map reconciliation

The R3 source layout was separately checked after a path error. The root-level
files `NavierStokes/R3.lean`, `R3ActualCandidate.lean`, `R3CompactEnergy.lean`,
`R3PressureFourier.lean`, `R3EnergyNorms.lean`, and `R3EnergyBoundary.lean`
are present. They coexist with detailed implementation files under
`NavierStokes/R3/`. Only the filename `SelectedCandidate.lean` remains absent;
that absence is unrelated to the R3 source itself.

The current tree and reachable Git objects contain no module named
`SelectedCandidate.lean`, `selectedcandidate.lean`, or
`R3/SelectedCandidate.lean`. The active names are
`ActualCandidateAssembly.selected_witness` and
`ActualCandidateAssembly.selected_candidate` at
`NavierStokes/ActualCandidateAssembly.lean:1177-1184`. The R3 wrappers are
`NavierStokes/R3/ActualCandidate.lean:127-151`, with the exported theorem and
dissipation theorem in `NavierStokes/R3/Theorem.lean:26-80`.

This is a filename correction, not a finding that the candidate or energy
theorems are absent. `uniform_finite_energy` is declared at
`NavierStokes/R3/CompactEnergy.lean:343` and is used by the viscosity-one
candidate construction. Current counts are 817 Lean files / 381,843 lines
under `NavierStokes/`, and 2,783 Lean files / 570,520 lines across the
worktree when `.lake/` and `.git/` are excluded. Historical counts must be
labelled with their snapshot.

## CALC-38i: global Bochner-integral branch

`PeriodicGlobalIntegral.lean` compiles without `sorry`, `axiom`, or `unsafe`.
It proves that a unit-periodic scalar strictly positive on `Ioo 0 1` cannot
be globally Bochner-integrable. The global integral is then zero by
`MeasureTheory.integral_undef`. The result is instantiated conditionally for
the selected mixed radial pullback and `barMoment 0`.

The selected source does not prove the positivity premise, and this theorem
does not cover the weighted cases `barMoment k` for `k > 0`. It therefore
clarifies the integral semantics without producing `Delta m != 0` or `False`.

Evidence:
`NavierStokesReview/evidence/source_path_reconciliation_2026-09-26.md`;
`NavierStokesReview/evidence/periodic_global_integral_semantics_2026-09-26.md`.

## CALC-38j: conditional mixed `barMoment` linearity

`SelectedMixedProductionBarMomentLinearity.lean` proves the selected mixed
scalar-family representative is the pointwise sum of its potential and direct
branches. Under explicit common `Shell` hypotheses, the source theorem
`DefectIncrementBounds.barMoment_add` therefore splits the mixed observable
into the sum of the two branch observables.

The selected construction does not export those common shell premises for the
complete mixed infinite-sum representative. This closes an algebraic
linearity step conditionally, but does not evaluate the weighted integral,
prove a nonzero commutator contribution, identify the value with the five
paper moments, or derive `False`.

Evidence: `NavierStokesReview/evidence/selected_mixed_barmoment_linearity_2026-09-26.md`.

## CALC-38h: conditional radial-support obstruction

`SelectedMixedRadialSupportObstruction.lean:26-48` instantiates the generic
periodic-plus-bounded-support theorem: any bounded radial support assertion for
the selected mixed pullback would force it to vanish identically.

The selected witness does not export the bounded radial-support premise, and
the completion does not prove a nonzero point. This is therefore a concrete
support/integrability compatibility objection, not yet `False`.

**Evidence:** `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.
## Source-tree and logic-map reconciliation (2026-09-26)

The extracted tree at `D:/Research Lab/Jexposition/tree-maker/Define inteligence tree.md` has been reconciled against the current checkout. The map records 3,021 extracted file entries, 3,029 current files excluding `.git` and `.lake`, and 2,788 current Lean modules. It confirms both source layers:

- root-level wrappers such as `NavierStokes/R3.lean`, `NavierStokes/R3PressureFourier.lean`, `NavierStokes/R3EnergyNorms.lean`, and `NavierStokes/R3EnergyBoundary.lean`;
- detailed R3 implementation modules such as `NavierStokes/R3/ActualCandidate.lean`, `NavierStokes/R3/Theorem.lean`, `NavierStokes/R3/PressureRecovery.lean`, and `NavierStokes/R3/ActualPressureFlux.lean`.

The selected endpoint route is now recorded as:

```text
ActualCandidateConstruction
  -> ActualCandidateAssembly.selected_witness
  -> R3.ActualCandidate.of_localized_fields
  -> R3.Theorem.theorem_1_1
```

`CandidateProperties` is present and explicit: smoothness, periodicity, initial value, positive-time force support, divergence-freeness, residual equality, and speed unboundedness. The live CTR-005 issue is narrower and stronger than a filename or module-presence objection: no exported theorem has yet been identified that evaluates the complete selected Cartesian field against the paper tuple `(M, I, J, S, C_p)`.

Pressure recovery is also present. `R3/PressureRecovery.lean:388-438` proves comparison pressure-gradient identities under explicit two-solution hypotheses and compact spatial tests. `R3/ActualPressureFlux.lean:36-58` derives the corresponding comparison flux. These facts clear any claim that the pressure infrastructure is absent; they leave open the selected-field absolute semantic transport question only.

Evidence: `NavierStokesReview/evidence/source_tree_logic_map_2026-09-26.md`; machine-readable index: `NavierStokesReview/evidence/source_tree_logic_map_2026-09-26.json`.

## Periodisation-to-radial-support boundary (2026-09-26)

The source trace separates two operations that must not be conflated. `SpatialLocalization.cutPotential`
is supported in the compact cylinder (`SpatialLocalization.lean:164-180`), while
`MixedPeriodicAssembly.periodicVelocity` applies lattice periodisation to the
potential and direct branches (`MixedPeriodicAssembly.lean:36-38`) and proves
unit spatial periodicity (`:59-65`). The `barMoment` operator nevertheless
integrates over the full real radial variable (`DefectIncrementBounds.lean:214-220`).

Therefore the existing support obstruction is conditional: a theorem still has
to transport `RadiallySupported` from the pre-periodised field to the selected
periodised pullback before it can force vanishing. The audit records no such
transport theorem and no selected nonzero radial value. This strengthens the
CTR-005 calculation gate without asserting a numerical remainder or `False`.

## Full dependency-map refresh: 2026-09-26

- [x] Re-run the source parser against `tree-maker/Define inteligence tree.md` at transitive import depth 100.
- [x] Record the current source census and closure with scope labels: 2,790 Lean modules; 507 modules from the single `ActualCandidateAssembly` root; and 588 modules / 1,648 import edges from the seven current audit roots.
- [x] Retain 797 reachable modules / 2,378 edges only as the 2026-09-26 historical parser result; it is not interchangeable with the current source closure.
- [x] Confirm that no reachable `NavierStokes.*` import is absent from the checkout.
- [ ] Interpret the complete selected mixed weighted integral at field level.

Evidence: `NavierStokesReview/evidence/source_tree_full_logic_map_2026-09-26.json`.
## Mapping infrastructure record: 2026-09-26

**MAP-01 — Hardened source/environment separation.** The audit now uses the extracted tree as the inventory baseline, live-file hashes for source identity, source parsing for navigation, and Lean’s compiled environment for elaborated declaration reachability. The endpoint export starts at `NavierStokesR3.theorem_1_1` and records 30,721 project declarations with 327,757 compiled-environment edges and no reachable `sorryAx` users. The corrected source map records 50,191 declarations and 186,194 token edges; those edges are diagnostic and are not evidence of kernel dependency.

**Operational consequence.** Filename presence, raw identifier matches, and upstream module reachability cannot close CTR-005. The remaining selected-field question is still value-level transport from the complete assembled Cartesian field to the paper’s named moments. Any stronger conclusion requires a zero-sorry theorem on the selected path.

**MAP-02 — Exact endpoint routes and parser correction.** The compiled closure reaches `ActualCandidateAssembly.selected_witness`, `FiveRowRank.FiveRows`, `FiveRowRank.Debt`, `PositiveOrderMoments.Debt`, `MeanRankUpdate.scaleDebt`, `MixedPeriodicAssembly.periodicVelocity`, `DefectIncrementBounds.barMoment`, `R3CompactCandidate.velocity`, and `NavierStokesR3.ProblemStatement.CandidateProperties`. The join now reports 22,958 exact source matches, 3 ambiguous matches, 7,760 unmatched environment nodes, and 227,128 joined edges. The earlier lower join counts were produced by a namespace/section parser defect and are superseded. Reachability of these declarations is not the same as a theorem transporting their values into the exported Cartesian witness.

Evidence: `NavierStokesReview/evidence/selected_endpoint_routes_2026-09-26.md`.

**MAP-05 — Current selected-path import cross-check.** The corrected source
parser independently reproduces a 507-module closure from
`ActualCandidateAssembly` and a 588-module / 1,648-edge closure from the
current seven audit roots. `PositiveOrderMoments`, `FiveProfileMoments`,
`FiveRowRank`, and `MeanRankUpdate` are on the selected source-import path.
`LocalPaperTheorem`, `LocalResidualFlatness`, and `PaperLocalization` are real
modules but are not reachable from the endpoint roots. The endpoint therefore
does load the moment/rank machinery, but the source spans at
`ActualCandidateAssembly:1079-1098` and `:1121-1181` still export
`PhysicalData`, `StageEstimates`, Cartesian sums, and `CandidateProperties`,
not a selected-field equality for the five paper observables. This is the
current import-versus-transport boundary, not a dead-code finding.

Evidence: `NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.

## MAP-03 — Reproducible mapping bundle

The review now packages inventory, source identity, compiled reachability, and
workspace state in `hardened_audit_bundle_2026-09-26.json`. The run is green:
3,021 extracted-tree entries; 3,058 current checkout files; 2,790 Lean
modules; 50,191 source declarations; 30,721 compiled declarations; 327,757
compiled edges; 22,958 exact source matches; 3 ambiguous matches; 7,760
unmatched environment nodes; and 0 reachable `sorryAx` users.

The bundle validates the required routes to `selected_witness`, `FiveRows`,
both debt types, `scaleDebt`, `periodicVelocity`, `barMoment`, and the R³
packaging. These are reachability facts. They do not prove that the five named
paper moments are values of the final assembled Cartesian witness.

Method: `docs/REVIEW_MAPPING_METHOD.md`.

## MAP-04 — Inventory reconciliation and bounded declaration queries

The mapping run now reconciles the tree-maker inventory with the live
checkout without trusting rendered indentation. It records 3,021 tree file
entries, 2,997 unique-basename resolutions, 24 ambiguous entries, and zero
missing basenames. Ambiguity is preserved as an explicit uncertainty class.

`mapping_query.py` supplies source spans and exact compiled joins for a named
declaration. The raw compiled graph remains distinct from the source-located
join: 327,757 raw environment edges versus 227,128 joined edges. This improves
audit reproducibility and navigation; it does not prove the selected
Cartesian-to-radial five-moment equality.

Evidence: `NavierStokesReview/evidence/tree_reconciliation_2026-09-26.md` and
`NavierStokesReview/evidence/query_selected_witness_2026-09-26.md`.

## MAP-05 — Claim-register boundary: 2026-09-26

`NavierStokesReview/config/review_claims.json` and
`NavierStokesReview/src/audit/claim_register.py` now provide a
machine-readable control layer over the mapping evidence. The validator
checks source declarations, compiled endpoint routes, and named evidence
files. It does not infer theorem meaning from graph reachability.

Current result: MAP-001 supported; CTR-005 open; CTR-012 conditional; and
CTR-032 supported. This preserves the central burden: a selected-path
value-level theorem must still transport the five named moments through the
assembled Cartesian field.

## MAP-06 — Complete module catalogue and visual map: 2026-09-26

`repository_map.py` now joins the authoritative tree inventory, live source
hashes, namespace-aware declarations, the elaborated endpoint environment, and
the claim register into a complete record for every Lean module. The run
accounts for 2,790/2,790 modules, 50,191 source declarations, 30,721 compiled
project declarations, 227,128 source-located compiled edges, 22,958 exact
source joins, three ambiguous joins, 7,760 unmatched environment nodes, and
zero reachable `sorryAx` users.

Outputs are `hardened_source_map_2026-09-29.json` and `.md`, with the exact
endpoint closure in `NavierStokesReview/evidence/direct_endpoint_closure_validation_2026-09-29.md`.
A source module outside the captured endpoint
environment is not called dead code. The map establishes complete audit
coverage and route reachability; CTR-005 remains open because the selected
field-level five-moment equality is not supplied by reachability alone.

## MAP-07 — Current Lean/source audit: 2026-09-26

Targeted builds of `NavierStokes.R3.Theorem` and `NavierStokesReview` pass.
The aggregate `lake build NavierStokes NavierStokesReview` is blocked by the
untracked scratch module `NavierStokes/R3/TestPressure.lean:6:60`, which Lean
reports as `expected token`. The selected endpoint is unaffected: the
whole-space axiom audit reports only `propext`, `Classical.choice`, and
`Quot.sound`. The source trace also confirms that `StateRealization` is a
structure in `NavierStokes/PhysicalResidualJetBounds.lean:885`, not a separate
module. The complete source/build/document result is recorded in
`NavierStokesReview/evidence/current_lean_docs_audit_2026-09-26.md`.

## MAP-08 — Endpoint claim cross-examination: 2026-09-27

Raw source inspection confirms that `ActualCandidateAssembly.Witness` at
`ActualCandidateAssembly.lean:1121-1151` is a proposition-valued nested
existential definition, not a structure carrying named five-moment fields.
The selected closure nevertheless reaches `FiveRowRank`,
`PositiveOrderMoments`, `FiveProfileMoments`, `MeanRankUpdate`,
`periodicVelocity`, and `barMoment`. The correct finding is therefore a
selected-field value-transport gap, not dead code or absent mathematics.

The same cross-examination narrows the other claims. `StageEstimates` blindness
is an interface countermodel, not a zero-field result for the selected witness.
Pressure recovery is a comparison theorem, not an absolute selected-pressure
Poisson theorem; compact pressure support alone has not been shown to force
triviality. The fixed-force perturbation result is a genuine operator-level
path-dependence theorem, but it is not a contradiction of the existential C/D
statement. The exact ledger is
`NavierStokesReview/evidence/claim_cross_examination_2026-09-27.md`.

## MAP-09 — Post-clean build status and source confirmation: 2026-09-27

A clean rebuild was attempted after incompatible `.olean` headers were found.
The aggregate `NavierStokes NavierStokesReview` command exceeded the 20-minute
execution limit without a Lean error. A second bounded
`NavierStokes.R3.Theorem` build exceeded 10 minutes without a Lean error. The
exact build process trees were terminated; no Lean workers remain. This is an
incomplete post-clean build verification, not a failed theorem and not a
successful fresh build.

The raw-source result is unchanged and independently recorded in
`NavierStokesReview/evidence/fresh_build_status_2026-09-27.md`:
`ActualCandidateAssembly.Witness` is a nested existential proposition at
`ActualCandidateAssembly.lean:1121-1151`, and `selected_witness` is its fixed
instantiation at `:1177-1181`. The selected upstream route genuinely reaches
`FiveRowRank`, `PositiveOrderMoments`, `FiveProfileMoments`,
`MeanRankUpdate`, `periodicVelocity`, and `barMoment`. No exported conjunct
identifies the final assembled Cartesian field with the paper tuple
`(M,I,J,S,C_p)`. CTR-005 therefore remains an affirmative selected-field
transport obligation. No `False` result is claimed.

## MAP-17 — Publication-boundary and generated-artifact census: 2026-09-27

The current branch is local-only for this audit pass: `HEAD` is 67 commits
ahead of `origin/review/cmi-first-navier-stokes-2026-09-22`, and no commit or
push was performed here. The inclusive source census is 2,790 Lean files,
comprising 2,789 tracked files and the untracked review module
`NavierStokes/R3/TestPressure.lean`. The map includes the inclusive file, but
the committed baseline does not.

No `.olean`, `.ilean`, or `.lake` paths are tracked. Ignored generated output
does exist in `.lake/` and in
`NavierStokesReview/src/external-semantic/` (`Adapter.olean`,
`ClaySpec.olean`, `ClaySpec-current.olean`, and `Gap.olean`). This is a
release-control finding, not an endpoint theorem finding. It prevents a claim
that the working tree is clean until the artifacts are removed or quarantined.

## MAP-18 — Untracked TestPressure import-path check: 2026-09-27

Direct elaboration of the untracked `NavierStokes/R3/TestPressure.lean` fails
at line 1 because it imports `NavierStokes.R3.PressureRecovery`, for which no
object file exists in the current build environment. The live source naming
uses root-level modules such as `NavierStokes/R3PressureRecovery.lean`, not a
`NavierStokes/R3/PressureRecovery.lean` module path. This is a malformed,
untracked scratch probe and not a failure of the selected endpoint. It must
not be included in a production build or used as endpoint evidence.

## MAP-10 — Fresh source census and admission scan: 2026-09-27

The source-only mapping pass was rerun after the post-clean build attempts. It
accounts for 2,790 current Lean modules and 50,191 parsed declarations. The
tree reconciliation records 3,021 tree file entries, 2,997 unique-basename
resolutions, 24 ambiguities, and no missing basenames. The machine outputs are
`NavierStokesReview/evidence/hardened_source_map_2026-09-29.json` and
`NavierStokesReview/evidence/tree_reconciliation_2026-09-27.json`.

The source flag scan found no `unsafe`, `axiom`, or `admit` declarations. It
found ten literal `sorry` tokens: four actual admitted challenge bodies in
`ComparatorChallenges/NavierStokes.lean` and `ComparatorChallenges/Euler.lean`,
plus six explanatory comments that say `zero-sorry`. The endpoint's last
completed compiled closure remains the 2026-09-26 export; this source refresh
does not establish a fresh build or fresh endpoint axiom result.

This closes the inventory question without changing the mathematical verdict.
The active selected-path question remains whether the complete Cartesian field
after `tsum`, curl, localisation, periodisation, and radial projection has the
paper's five moment values. Reachability and source coverage do not answer that
value-level question.

## MAP-11 — Route-scope correction and global cross-layer audit: 2026-09-27

The current source inspection corrects the scope of the reachable-moment
finding. `PositiveOrderMoments`, `FiveRowRank`, `MeanRankUpdate`, and
`barMoment` are not dead branches: they occur on endpoint-reachable routes.
Their direct consumers establish slow-base/exterior primitive identities or
correction-state/update invariants. The selected packaging boundary at
`ActualCandidateAssembly.lean:1121-1151` and `:1177-1181` still exports no
equality identifying those quantities with the final Cartesian `ASum`, `BSum`,
or `PSum` fields.

This is the operative audit question, not a claim that the upstream moment
mathematics is absent. The next pass must inspect all candidate bridges in the
joined declaration map, including pressure, energy, support, axis-chart,
force-provenance, and Euler parent-child claims. A negative text search is only
screening evidence; the final classification requires declaration-level source
and type inspection.

## MAP-12 — Partial selected-field bridges found: 2026-09-27

The declaration-level inspection corrected the scope of the earlier negative
screening result. Review-side completion modules do contain partial bridges:
finite-prefix curl and cutoff product rules, local radial scalar formulae,
torus-average reductions, typed mixed-field `barMoment` pullbacks, cycle
moment invariants, and base-profile transport. These results are inventoried
with file and line coordinates in
`NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.

## MAP-26 — Local Cartesian coherence: 2026-09-27

`ActualPrimaryCoherence.lean:1866-1940` defines a genuine local Cartesian
potential/velocity layer and proves smoothness, axis-zero behaviour, the
piece-to-Cartesian velocity relation, pressure representation, and
divergence-freeness on the stated domains. This is positive evidence and
removes any claim that the Cartesian layer is absent. The remaining open
question is whether those local identities are composed with the final
`ASum`/`BSum`/`PSum` fields and the five selected-field observables. Evidence:
`NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.

## MAP-25 — Logarithmic profile/history bridge: 2026-09-27

`NominalConeAssembly.lean:366-446` contains chart identities for the outgoing
profile quantities `M` and `J` and the heat-switch quantities `I` and `S`.
`NominalConeAssembly.Witness.log_histories` at lines 452-470 maps those profile
values into outgoing and heat-switch histories. Lines 596-667 transport the
corresponding parameters and derivatives. This is a genuine reachable bridge
and must be credited in the audit.

The inspected declarations do not take the final `ASum`/`BSum`/`PSum`
Cartesian field as input and do not conclude the five-observable equality
after curl, localisation, periodisation, infinite summation, torus averaging,
and radial pullback. CTR-005 therefore remains an endpoint value-level
transport question, not a claim that the profile/history branch is dead.
Evidence: `NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.

## MAP-24 — Finite-modification moment scope: 2026-09-27

`AssembledSlowBase.lean:1514-1529` defines `FiniteModification` with a
single explicit `mass` field, namely equality of `Q.M` and the nominal profile
mass on the selected outer radius. It does not store a five-coordinate
`(M, I, J, S, Cp)` equality. Other local rows are supplied by separate
`EntranceAlignedBase`, `GlobalStressSupport`, profile, and rank theorems.
This narrows rather than changes CTR-005: the finite-modification record is
not itself the final selected-field transport certificate, but the upstream
five-moment machinery is genuine and must not be described as absent.
Evidence: `NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.

## MAP-23 — Final mixed-field assembly boundary: 2026-09-27

**Source trace:**

- `TailGaugePotential.lean:433-450` defines `finalPotential` and proves its
  curl equals `FinalSlowBase.velocity` for `t < 1`.
- `ActualPhysicalStageBounds.lean:616-656` gives the initial-potential curl
  decomposition.
- `ActualCandidateAssembly.lean:205-211` defines the zeroth potential;
  `:531-568` defines the stage families; `:1003-1077` proves stage curl/chart,
  pressure, and `stageRealizations`; `:1125-1151` packages `ASum`, `BSum`, and
  `PSum` and applies the mixed localisation/periodisation/activation route.
- `MixedPeriodicAssembly.lean:20-170` proves field smoothness, periodicity,
  local equality, and divergence transfer for the mixed field.

**Finding:** Cartesian stage realisation is present and reachable. The exact
source search found no endpoint theorem computing the five named paper
observables on the final activated `ASum`/`BSum`/`PSum` output. Existing
`OutgoingSchedule` and `OutgoingTail` identities remain profile/history-level
results.

**Classification:** selected-field value-level transport remains
`NOT_ESTABLISHED`; this is not a dead-code or disconnected-assembly finding.

The unresolved issue is narrower and stronger than a filename-level absence
claim. No inspected declaration exports a value-level equality identifying the
five paper observables \((M,I,J,S,C_p)\) with the fully assembled selected
Cartesian field after `potentialSum`, curl, localisation, periodisation,
`torusAverage`, radial pullback, and `barMoment`, including the axis and
whole-space extension conditions. No nonzero remainder has yet been computed,
so this remains a correspondence obligation rather than a kernel `False`
derivation.

## MAP-13 — Global cross-layer lane audit: 2026-09-27

The source-led audit now checks the principal isolation lanes beyond the
five-moment branch. `PressureRecovery.gradient_recovery` and
`ActualPressureFlux.pressure_flux_eq_canonical` are comparison theorems for
`p - q` under equal-residual hypotheses. `CompactEnergy.energy_balance` and
`CompactEnergy.uniform_finite_energy` are genuine endpoint energy results.
`MixedPeriodicAssembly` proves smooth localisation, periodicity, divergence
freedom, local equality, origin equality, and residual-jet transfer.
`TimeLocalization` proves a smooth activation layer and late equality after
`3/4`. These findings clear the earlier energy and cutoff objections, but do
not supply the missing selected-field five-observable equality.

The force provenance remains explicit in `CandidateFromLimits.lean:80-110`:
the force is a smooth extension of traced residual jets and agrees with the
activated residual for `0 ≤ t < 1`. This supports CTR-012 as a provenance and
path-dependence objection, not as an unconditional endpoint `False` theorem.

The companion `Euler/` tree is audited separately. Its parent, child, and
packet-stage declarations are not evidence about the Navier--Stokes endpoint.
The full lane ledger, with source coordinates and classifications, is
`NavierStokesReview/evidence/global_cross_layer_audit_2026-09-27.md`.

## MAP-15 — Audit-runner timestamp hardening: 2026-09-27

`NavierStokesReview/src/audit/run_hardened_audit.ps1` previously embedded
`2026-09-26` in its output paths. It now accepts an explicit `-Stamp` and
defaults to the current date, so source maps, environment joins, route maps,
claim registers, bundles, and repository maps cannot silently overwrite or
masquerade as an older snapshot. PowerShell parser validation reports zero
syntax errors. This changes the audit tooling only; it does not claim a fresh
Lean build or a new public release.

## MAP-14 — Source-path and publication-control correction: 2026-09-27

The proposed transport search was rerun against the live source tree. The
three external-semantic Lean files `Adapter.lean`, `ClaySpec.lean`, and
`Gap.lean` are present and tracked. A previous discrepancy came from reading a
nested JSON map field incorrectly and is withdrawn.

The filename suggestions also require correction: no standalone
`StateRealization.lean` or `PhysicalFields.lean` exists in the live tree. The
relevant declarations are in `PhysicalResidualJetBounds.lean` and
`ActualPhysicalPrefixFields.lean`. The live source map contains 2,790 Lean
modules and 50,191 source declarations. The dated compiled endpoint join
contains 572 source-joined modules; the other 2,218 modules are source-indexed
but not captured in that endpoint environment. This is a coverage distinction,
not evidence that those modules are dead or semantically irrelevant.

No local work from this audit pass has been pushed. The checkout remains on
`review/cmi-first-navier-stokes-2026-09-22`; the public branch therefore does
not yet show the local evidence changes. The source-path cross-check and the
remaining declaration-level transport work are recorded in
`NavierStokesReview/evidence/global_cross_layer_audit_2026-09-27.md`.

## MAP-16 — Hidden-name bridge screen: 2026-09-27

The 507 source-reachable production modules were screened for direct textual
co-occurrence between the endpoint predicates and the moment interfaces. The
counts were zero for `FiveRows` with `CandidateProperties`, `barMoment` with
`CandidateProperties`, `PositiveOrderMoments` with `CandidateProperties`,
`FiveProfileMoments` with `CandidateProperties`, and `barMoment` with the
endpoint `Witness`. This is a source-text screening result, not a proof that a
differently named theorem cannot exist. Review-side completion modules do
contain partial transport declarations. The remaining question is the exact
selected-field value theorem through the full Cartesian-to-radial pipeline.

## MAP-19 — Proposed transport-cluster declaration check: 2026-09-27

The suggested architectural clusters were checked against their declarations,
not just their filenames. `LocalPaperTheorem.lean:128-176` packages the local
schedule, smooth fields, divergence, residual flatness, exterior zero residual,
and angular growth. `PaperLocalization.lean:28-48` packages local compact
candidate agreement. Neither declaration states the five selected observables
for the final Cartesian field.

The upstream moment and rank results are genuine but scoped:
`EntranceAlignedBase.lean:666-671` proves zero positive-order moments for an
aligned base history; `CorrectionState.lean:449-476` proves `FiveRows` for a
correction state; `DefectIncrementBounds.lean:621-646` and `:775-813` prove
local mass-row preservation and propagation; and
`FinalSlowBase.lean:616-660` constructs profile data without making those
identities a selected whole-space PDE conclusion.

This is not a dead-code finding and not an algebraic contradiction. The open
transport obligation is the value-level composition after `potentialSum`, curl,
localisation, periodisation, `torusAverage`, radial pullback, `barMoment`, and
the off-axis/on-axis and whole-space extensions. No nonzero remainder has been
computed, so the current classification remains correspondence failure rather
than kernel `False`.

## MAP-20 — Positive upstream five-moment route: 2026-09-27

`GlobalSlowProfiles.profiles_moments` (`GlobalSlowProfiles.lean:1043-1060`)
proves all five positive-order rows for the constructed radial profile
sequence. `GlobalStressSupport.moments_zero`
(`GlobalStressSupport.lean:144-157`) transfers them to the axial and angular
histories, and `AssembledSlowBase.lean:592-617` consumes the zero mass row to
prove an exterior primitive vanishes. These are transported local results and
must be counted as such. They still do not identify the final mixed Cartesian
`ASum`/`BSum`/`PSum` fields with the paper tuple after the full assembly and
projection chain. CTR-005 therefore remains a final selected-field transport
obligation, not an absence claim.

## MAP-21 — Fresh compiled-closure replay status: 2026-09-27

The current source census completed with 2,790 Lean modules and 50,191 source
declarations. The environment-export phase stopped because
`.lake/build/lib/lean/NavierStokes/R3/Theorem.olean` is absent. A bounded
five-minute rebuild of `NavierStokes.R3.Theorem` did not produce the object and
was terminated with its child workers. The dated compiled join in the evidence
corpus is therefore a prior snapshot, not a fresh replay of this checkout.
This does not alter the source-level moment/rank or selected-field transport
findings. Evidence:
`NavierStokesReview/evidence/fresh_environment_replay_2026-09-27.md`.

## MAP-22 — Reachable outgoing-profile identities: 2026-09-27

The selected source closure contains a further moment-bearing route:

```text
ActualCandidateAssembly
  -> InitialPhysicalData -> ActualPrimaryBounds -> CorrectionInitialization
  -> MeanRankUpdate -> FiveProfileMoments -> UniformAngularReset
  -> OutgoingTail -> OutgoingSchedule
```

`OutgoingSchedule.lean:739-747` defines the scalar `massMoment` and
`angularMoment` integrals. `OutgoingSchedule.lean:846-927` proves their
endpoint cancellation, and `OutgoingTail.lean:908-923` preserves the two
identities through the extended angular profile. These are reachable,
substantive profile-level results, so the moment branch is not absent or
unused.

The inspected route still does not export an equality identifying those two
scalars, or the complete five named observables, with the final Cartesian
`ASum`/`BSum`/`PSum` fields after curl, localisation, periodisation, infinite
summation, torus averaging, and radial pullback. The result strengthens the
positive upstream record without closing CTR-005. Evidence:
`NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.

## MAP-27 — Paper-grounded status of the selected-field transport obligation: 2026-09-27

The local copy of OpenAI's paper makes the unresolved bridge load-bearing rather
than cosmetic. Section 4.2, equation (4.15), defines the five cumulative radial
quantities \(M,I,J,S,C_p\), and Lemma 4.4 states that matching these cumulative
integrals preserves the radially integrated exterior pressure, radial velocity,
and stress data. Section 5.2, equations (5.10)--(5.11), uses a five-equation
correction solve to remove exterior pressure and stress terms. The later
localisation discussion also says that cutoffs are applied to vector potentials
before taking curls and that the resulting cutoff/curl terms are retained in the
full residual.

This source evidence changes the wording, not the verdict. The required result
is not merely an upstream profile certificate. It is a theorem evaluating the
named observables on the final selected Cartesian field after the actual
`potentialSum`/`tsum`, curl, spatial and temporal localisation, periodisation,
torus averaging, radial pullback, and axis/outer-domain extensions. The source
audit has found real upstream profile, rank, and outgoing-history identities but
has not found that final value-level theorem. The finding is therefore a
load-bearing correspondence failure under CTR-005, not proof that the upstream
five-moment machinery is absent and not a proof of `False`.

The targeted Lean invocation in this checkout did not reach source elaboration:
the cached dependency object
`.lake/build/lib/lean/NavierStokes/ActualCandidateConstruction.olean` was
absent. This is a build-environment freshness limitation, not a theorem failure.
No fresh clean-build or fresh axiom report is claimed until the dependency graph
has been rebuilt.
## MAP-28: Partial selected-field bridge inventory, not endpoint closure (2026-09-27)

The review-side completion layer contains genuine intermediate bridges that must be distinguished from the missing final theorem:

- `SelectedMixedProductionBarMoment.lean:34-59` defines the selected mixed scalar pullback and proves its typed `barMoment` interface.
- `SelectedMixedProductionTorusAverage.lean:25-44` reduces the auxiliary torus average to an explicit radial-section integral.
- `SelectedPotentialProductionTsumScope.lean:29-48` controls an eventual finite-prefix/`tsum` jet scope, while explicitly leaving `torusAverage`, `barMoment`, and radial-integral evaluation separate.
- `SelectedCutoffCurlCommutator.lean:18-23` exposes the cutoff-gradient commutator that a global moment proof must control.
- `SelectedCartesianRadialGate.lean:20-46` is only a positive-radius/nonzero-component recovery formula.

`PeriodicGlobalIntegral.selected_mixed_barMoment_zero_of_positive_pullback` (`PeriodicGlobalIntegral.lean:57-75`) is conditional. It assumes strict positivity on a fundamental interval, proves non-integrability of the periodic pullback, and obtains zero through Mathlib's `integral_undef`. The selected positivity premise is not established there. Therefore this theorem is not the physical value of the selected moment and does not close the endpoint transport burden.

**Classification:** `CTR-005` remains an open selected-field transport/correspondence issue, now with partial bridges explicitly credited. Do not state “no bridge exists”; state that no inspected theorem yet proves the full selected Cartesian field equality through `tsum`, curl, localisation, periodisation, torus averaging, radial pullback, support/integrability, and axis handling.

## MAP-29: High-priority source-tier re-audit (2026-09-27)

The next reachable source tier was inspected directly rather than inferred from
imports:

- `PositiveOrderMoments.lean:21-23,77-84,192-301` defines a real five-coordinate
  debt and proves exact profile repair and target-moment identities, with later
  pressure/flux consequences under explicit zero-moment hypotheses.
- `MeanRankUpdate.lean:24-44,137-169,195-200` defines the distinct
  three-coordinate physical debt, its scaling, and `FiveRows` for correction
  increments. This is correction-layer structure, not a total-moment theorem
  for the exported field.
- `ActualCandidateConstruction.lean:205-257,289-345,832-970` constructs the
  selected cycle, chart stages, direct/stream mean stages, and potential-stage
  field equalities.
- `SpatialLocalization.lean:164-203,209-290,313-340` proves the actual
  cutoff-before-curl identity, exposes the cutoff-gradient commutator, and
  proves periodised local equality, periodicity, divergence freedom, and
  residual transfer.
- `GlobalSlowProfiles.lean:167-205,281-334,337-400` and
  `TerminalPressure.lean:39-145,149-239,406-627` contain genuine reduced
  pressure/profile identities on their stated domains.

These findings rule out the weak allegation that the upstream mechanism is
absent or disconnected. They do not close the selected-field value theorem
through `tsum`, curl, localisation, periodisation, torus averaging, radial
pullback, support/integrability, and axis handling. `CTR-005` therefore remains
the affirmative correspondence burden, without a claim of nonzero remainder or
kernel `False`.

## MAP-30: Correction and local moment tier (2026-09-27)

The next reachable correction tier was inspected directly and added to the semantic coverage register. `CorrectionInitialization.lean:112-270,1153-1234` contains actual cutoff-curl, pressure-mode, support, and local zero-mass consequences. `StateMomentBalances.lean:719-721,767-824,956-1005,1063-1118` contains genuine local radial and pressure moment balances, while explicitly describing its `FluxInputs` premises as pointwise regularity data rather than an averaged moment identity. `IntegratedMeanBalances.lean:24-224,237-330,360-520,581-697` provides the underlying radial moments, torus averages, and integration identities. `PhysicalMeanDomain.lean` supplies local fibre, support, periodicity, and finite-jet transport. `ActualSignedPhysicalData.lean` contains concrete Cartesian carrier, potential, pressure, periodisation, and `tsum` equalities.

These results strengthen the positive source record and narrow the remaining attack surface. They do not yet evaluate the five paper observables on the complete selected `ASum`/`BSum`/`PSum` field after every transformation. The required next result remains either a concrete nonzero remainder, an impossibility theorem, or a positive full transport theorem. The presence of local moment identities must not be promoted to either endpoint transport or `False`.

## MAP-31: Slow-profile, stress, reset, and chart-compatibility tier (2026-09-27)

The next five priority-ranked reachable modules were inspected directly:

- `SlowBorelBase.lean:23-50,72-232,292-375,381-468,810-871,1043-1147` constructs smooth slow series, finite-prefix/tail bounds, derivative and sum-map infrastructure, and coefficient data including pressure and stress.
- `SlowResidualMatching.lean:47-152,175-250,267-333,392-618,833-1144,1204-1381` supplies reduced slow residual/stress primitives, radial identities, and truncation/tail decompositions with explicit stress equalities.
- `SignedStressPrimitive.lean:20-149,159-311,692-804,857-920,1159-1234` constructs compact signed bumps with exact weighted moment cancellation and proves physical pullback, torus-support, and chart finite-jet properties.
- `UniformAngularReset.lean:25-80,142-191,273-364,438-480,922-937,1001-1052,1251-1342` proves uniform invertibility of the two-bump angular moment system, a smooth reset branch, and scheduled damping/endpoint identities.
- `MeanChartCompatibility.lean:22-189,314-414,427-574,609-651,763-900,1209-1338` proves scaling and pullback/naturality identities for cutoffs, torus averages, pressure, temporal families, source moments, and debt/rank data.

This tier materially strengthens the positive source record. It also narrows the remaining test: these declarations operate at slow-profile, correction, physical-pullback, or chart-compatibility layers. The inspected route still does not evaluate the five paper observables on the complete selected `ASum`/`BSum`/`PSum` field after every transformation. No nonzero remainder, impossibility theorem, or kernel `False` has been obtained. `CTR-005` remains open as a selected-field correspondence question, independently of any future author remediation.

## MAP-32: Dynamics, local-rank, terminal compensation, and reindexing tier (2026-09-27)

The next five queue entries were inspected directly:

- `ActualParticularDynamics.lean:26-239,454-573,1462-1481,1509-1534,1547-1625` constructs selected primary carriers, transported coordinates, harmonic residual blocks, divergence-free sums, and common-cover cancellation identities.
- `LocalRankDefect.lean:25-213,430-464,590-608,743-808` proves local-shell/rank smoothness and derives zero `barMoment` rows for local correction increments and updated local means.
- `TerminalCompensation.lean:24-181,217-260,700-760,907-1009` constructs three compact compensation bumps, proves weighted integrability, and identifies physical positive-radius moment cancellation.
- `SlowExpansionResidual.lean:24-246,285-330,769-850,908-995` expands finite slow products and convolutions, exposes finite remainders, proves coefficient cancellation criteria, and reconstructs reduced Cartesian residual components away from the axis.
- `StateReindex.lean:23-175,108-159,500-590,650-727,742-794` proves isometric pullback of fields, derivatives, correction states, residual operators, and auxiliary torus/radial integrals.

These results are substantive but scoped. Local `barMoment` zeros, terminal profile cancellation, reduced residual identities, and reindexing naturality are not the final selected `ASum`/`BSum`/`PSum` five-observable evaluation. No nonzero remainder, impossibility theorem, or kernel `False` has been found. The next unresolved work remains the complete endpoint composition.

## MAP-33: Initialisation, final slow base, R3 packaging, terminal stress, and mean residual (2026-09-27)

The next five priority-ranked modules were inspected directly:

- `ActualInitialization.lean:31-190,1132-1246,1354-1427,1471-1512` builds the actual initial correction state, selected primary pieces, pressure/Gaussian blocks, support facts, mean/debt data, zero-mass and covariance invariants, and initial divergence/residual properties.
- `FinalSlowBase.lean:26-166,223-280,335-380,433-482,495-600,627-639` constructs the aligned slow base, weighted/stress identities, support and exterior vanishing, completed velocity/pressure, and terminal extension.
- `R3/ActualCandidate.lean:24-121,124-153` packages localized fields and the positive-time force into the whole-space candidate properties, including residual, support, finite-energy, and C/D statements.
- `TerminalStress.lean:23-112,147-206,226-268,340-453,640-778,805-945` proves terminal heat-tail, radial residual, boundary, flattening, and stress identities. Its module comment explicitly separates backward stress from the separate global moment condition.
- `MeanResidual.lean:24-229,790-915,1021-1091,1132-1154` defines normalized angular averaging and proves mean balances, Cartesian residual/divergence identities, periodic invariance, and covariance/error retention.

These findings further confirm substantive intermediate mathematics and a real
R3 packaging layer. They do not add the final selected-field five-observable
equality. The endpoint remains a correspondence question until that value-level
composition is located, proved impossible, or computed to have a nonzero defect.

## MAP-34: Formal contract, periodised bounds, gauge moments, exterior, and base residual (2026-09-27)

The next five queue entries were inspected directly:

- `ProblemStatement.lean:42-120,140-159` defines the formal candidate contract and explicitly states that this module asserts no existence. The contract has smoothness, periodicity, support, divergence, residual, energy, initial-value, and speed fields, but no five-moment, absolute-pressure, or force-independence predicate.
- `PeriodizedWaveBounds.lean:30-183,188-289,303-344` proves local-finite support-cell, copy-sum germ, support, jet, and whole-lift bounds, including cutoff derivative/source terms.
- `GaugeMomentBalances.lean:24-102,151-186,184-207` defines measured pressure coefficients as scaled second moments and proves moving-gauge pressure identities, while separating regularity/support/periodicity hypotheses from moment equations.
- `BaseExterior.lean:30-156,164-240,278-314,328-338` proves canonical heat-exterior pressure, smoothness, integrability, residual zero, and exterior stream/velocity/pressure identities.
- `ActualBaseResidual.lean:28-113,116-218,247-317,332-384,479-507` proves residual germ congruence/invariance and defines scaled base pressure, error, velocity, and stress fields with smoothness claims.

This tier confirms the formal endpoint contract and substantial periodised,
gauge, exterior, and base-residual infrastructure. It does not add the final
selected Cartesian five-observable equality or a contradiction. The open test
remains the complete endpoint composition, not the existence of upstream
operators.

## MAP-35: Fact-check of supplied `agent log 5` comments (2026-09-27)

The supplied comments correctly reinforce the need for a complete selected-field
transport audit, but several proposed conclusions exceed the current source
record. `ActualCandidateAssembly.Witness` does not export a final equality for
`(M, I, J, S, C_p)`, while upstream profile, correction, Cartesian-curl,
localisation, residual, energy, and R3 packaging mathematics is genuine and
reachable. The endpoint therefore has a load-bearing correspondence gap, not a
proof that the whole upstream mechanism is absent.

`SpatialLocalization.lean` exposes the cutoff-gradient commutator and proves
local divergence/residual-transfer properties. It does not evaluate the
commutator's global radial integral or prove that it is nonzero. Likewise,
`StageEstimates` is blind to a five-coordinate debt as an interface, but the
concrete selected stage estimates consume physical-data and `NativeBounds`
results. The phrase “only generic rates” is therefore too broad.

The residual-defined force and fixed-force perturbation establish provenance
and trajectory sensitivity. They do not add a formal force-independence
predicate to the existential C/D endpoint, so they are not an unconditional
kernel contradiction. The supplied comments are recorded as adversarial
hypotheses for the next value-level calculation, not as established defects.

Evidence: `NavierStokesReview/evidence/agent_log5_cross_exam_2026-09-27.md`.
The open target remains:

```text
selected Cartesian field -> tsum/potentialSum -> curl/localisation/commutator
-> periodisation -> torus average -> radial pullback -> (M,I,J,S,C_p).
```

Escalation requires a zero-sorry nonzero remainder, a zero-sorry impossibility
theorem, or a positive complete bridge theorem.

## MAP-36: Correction/state and heat-tail tier (2026-09-27)

The next reachable modules were inspected directly. `CorrectionState.lean` uses
concrete state fields, angular covariances, radial pressure moments, reconstructed
radial residuals, and `FiveRows` for rank correction functions. `HeatTailEdit.lean`
proves smooth switch/edit factors, weighted tail integrability, pressure/energy/
angular debt bounds, outgoing factorisation, and jet control. `ActualMeanPhysicalData.lean`
transports atlas/state overlap, gauge/rank/temporal data, pressure identities,
and native-jet estimates through cycle stages.

These findings strengthen the positive source record. They do not establish the
selected Cartesian field's final `(M,I,J,S,C_p)` value after `tsum`, curl,
localisation, periodisation, torus averaging, radial pullback, support,
integrability, and axis limits. No nonzero remainder, impossibility theorem, or
kernel `False` was obtained. At that stage the register recorded 65 explicit
reviews and 533 reachable modules; the later MAP-37 pass updates the current
register to 73 explicit reviews and 525 reachable modules.

## MAP-37: Slow-base, rebase, harmonic, primary-dynamics, and rank-coherence tier (2026-09-27)

The next eight priority-ranked reachable modules were inspected directly:

- `OffplaneCorrectionExtensions.lean:21-203,217-327,339-455,730-812,875-1060`
  extends positive-radius slow pressure/rank models to supported Cartesian
  continuation data and proves smoothness, agreement, support, and shrinking
  support.
- `SlowBaseEndpoint.lean:44-181,226-258,292-356,421-438` lifts profile,
  potential, velocity, and pressure data to smooth away extensions and proves
  germ/extension identities.
- `ConstructedSlowBase.lean:40-53,65-113,145-188,210-329,339-438,616-697,714-770,828-931`
  constructs a genuine axisymmetric potential/curl route and derives finite
  identities, stress-zero-core, jet flatness, smoothness, divergence, growth,
  and residual identities for nominal and modified scales.
- `BasePrefixIdentity.lean:23-157,217-260,270-319,341-383` proves finite-prefix
  curl/profile, radial-flux, pressure, stress-force, and finite-identity
  bridges from coefficient matches.
- `ActualReferenceRebase.lean:77-146,260-336,560-625,787-834,877-932,1062-1091`
  proves rebase/pullback identities for actual stage contexts, residual sources,
  frames, directions, amplitudes, pressures, phases, and periodic subcovers.
- `HarmonicWaveInteraction.lean:107-235,277-386,440-576,605-789,839-880,917-1116`
  formalises harmonic blocks, zero modes, convolution transport, nonlinear
  interaction updates, divergence coefficients, and residual-difference blocks.
- `ActualPrimaryDynamics.lean:57-177,249-343,429-529,963-1144` derives actual
  primary pulse geometry, copied velocity/pressure germs, cutoff/curl
  smoothness, local linear identities, and local residual formulas.
- `RankStateCoherence.lean:26-74,116-225,248-336,364-394,428-452` defines
  fibre moments, measured debt, rank-on predicates, normalised rank stages, and
  `FiveRows` conclusions for correction/rank state slices.

These are additional positive intermediate results. They materially narrow the
possible location of a defect, but none is a theorem whose input is the final
selected `ASum`/`BSum`/`PSum` Cartesian field and whose conclusion evaluates
`(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation,
torus-average, radial-pullback, support, integrability, and axis route. No
nonzero remainder, impossibility theorem, or kernel `False` was obtained. The
generated register now records 73 explicit reviews and 525 reachable modules
still awaiting semantic classification.

## MAP-38: Axisymmetric residual, particular-wave, leading-stress, and mean-residual tier (2026-09-27)

Four further priority-ranked reachable modules were inspected directly:

- `AxisymmetricResidual.lean:155-264,274-350,366-408,417-432` defines regular
  axisymmetric Cartesian velocity/pressure lifts and proves exact advection,
  derivative, Laplacian, pressure-gradient, divergence, and residual formulas,
  including an on-axis route.
- `PhysicalParticularWave.lean:31-120,246-300,367-443,519-697` builds actual
  particular-wave carriers, potentials, curls, pressures, chart changes,
  periodicity, smoothness, and reference-domain transport identities.
- `LeadingStress.lean:33-224,258-309,363-421,458-519` derives angular and axial
  stress divergences, pressure derivatives, radial pullbacks, physical stress
  scaling, and residual transport on regular positive-radius profile domains.
- `LiftedMeanResidual.lean:25-113,128-198,201-265,350-431,472-508,625-675`
  defines angular averaging and proves smooth parameter integration, periodic
  invariance, conservative flux, averaged Laplacian/gradient, and nonlinear
  residual-lifting identities.

These are genuine local Cartesian, profile-to-residual, stress, and mean
calculus results. They further reduce the space in which a selected-field
bridge or defect could occur, but none evaluates the final selected field's
`(M,I,J,S,C_p)` after the complete sum/curl/localisation/periodisation,
torus-average, radial-pullback, support, integrability, and axis route. No
nonzero remainder, impossibility theorem, or kernel `False` was obtained. The
register now records 77 explicit reviews and 521 reachable modules still
awaiting semantic classification.

## MAP-39: Wave-bound, signed-data, and primary-residual tier (2026-09-27)

The next four reachable modules were inspected directly:

- `LinearWaveBounds.lean:93-184,176-269,270-392,444-556,630-675` defines actual
  wave coefficients, cutoff/curl corrections, input bounds, wave classes, exact
  conditions, and coefficient-level harmonic residual identities.
- `ActualPhysicalStageBounds.lean:24-115,130-158,171-269,274-302` derives
  physical-stage smoothness, support, jet, potential, pressure, and gain bounds
  from coherent mean and wave inputs and packages cycle inputs.
- `ActualSignedWaveData.lean:29-56,119-240,251-365,373-456` builds signed
  support cells, potential/pressure copy families, carriers, source amplitudes,
  frequency identities, and native stage data.
- `PrimaryResidualClass.lean:36-169,173-309,344-419,430-565` defines primary
  correction inputs, invariant angular data, curl-corrected wave classes, exact
  conditions, divergence, linear residual, field projection, and smooth primary
  coefficients.

These are real coefficient, stage, signed-data, and primary-residual results.
They do not evaluate the final selected Cartesian field against `(M,I,J,S,C_p)`
through the complete sum/curl/localisation/periodisation, torus-average,
radial-pullback, support, integrability, and axis route. No nonzero remainder,
impossibility theorem, or kernel `False` was obtained. The register now records
81 explicit reviews and 517 reachable modules still awaiting classification.

## MAP-40: Initial-mean, cycle-prefix, and moment-reset tier (2026-09-27)

Four additional reachable modules were inspected directly. `ActualInitialMeanEquation.lean`
proves initialized angular data, local mean/divergence, periodicity, mean-zero,
primary-sum divergence, and initialized full-divergence identities.
`CyclePhysicalPrefixes.lean` defines cylindrical and local Cartesian
velocity/pressure maps, stage updates, finite prefixes, potential/direct splits,
and local residual-prefix identities under explicit curl-realisation
hypotheses. `FiveProfileMoments.lean` contains a genuine five-coordinate
reduced-profile debt map, integrability, exact linear moment maps, continuous
linear equivalence, compact correction families, and jet bounds.
`AngularMomentReset.lean` contains an invertible two-parameter local
angular/pressure reset with a pressure-neutral branch and exact endpoint
adjustment.

These results strengthen the positive intermediate source record. They do not
identify the reduced-profile or local-reset moments with the final selected
Cartesian `ASum`/`BSum`/`PSum` field after `tsum`, curl, localisation,
periodisation, torus averaging, radial pullback, support/integrability, and
the axis limit. No nonzero remainder, impossibility theorem, or kernel `False`
was obtained. Evidence record:
`NavierStokesReview/evidence/reachable_initial_moment_cluster_2026-09-27.md`.

## MAP-43: Transformation-pipeline evidence control (2026-09-27)

`scratch_space/notes3.md` supplies the declared Gaussian profile calculation
and its cutoff-gradient hypothesis. The implementation
`NavierStokesReview/src/audit/cutoff_commutator_scan.py` now reconstructs the
exact `SpatialLocalization.spatialCutoff` on a full 3D Cartesian volume,
evaluates a nonseparable `S(r,z)` stream, analytic and finite-difference curls,
the `(grad c) x A` commutator, divergence residuals, and full x-y moment
slices. It sweeps resolution/profile scale/modulation and writes plotted
JSON/CSV/Markdown evidence through the CUDA-first V-lab environment. CPU is a
fallback only; CPU/GPU comparison is not the objective. This remains
profile-level diagnostic evidence, not a selected-field result: the notes do
not bind the calculation to OpenAI's `ASum`/`BSum`/`PSum`, `tsum`, curl,
localisation, periodisation, torus averaging, radial pullback, support,
integrability, and axis route.

The product-rule commutator is source-supported. A nonzero radial integral for
the declared profile does not by itself prove a nonzero selected-field
remainder. No `Delta m != 0`, impossibility theorem, or kernel `False` is
recorded by MAP-43.

The whole-tree source instrument
`NavierStokesReview/src/audit/selected_endpoint_source_census.py` covers 2,790
Lean files, 649,366 source lines, 50,191 parsed declarations, and 588 modules
reachable from the two endpoint roots. It reports seven active lexical bridge
candidates and zero missing local imports. These are triage counts only; no
candidate is promoted without exact declaration-level transport evidence.

## MAP-44: CUDA-first 3D cutoff/curl diagnostic (2026-09-27)

The required plot is
`NavierStokesReview/evidence/cutoff_commutator_deep_2026-09-27.png`, with
machine-readable outputs beside it. The calculation is explicitly stronger
than the earlier scalar control: it operates on the three-dimensional
Cartesian volume, reconstructs `A_x=-c*S*y/r^2`, `A_y=c*S*x/r^2`, evaluates
`curl(cA)` and the exact cutoff-gradient term, and independently computes the
Cartesian finite-difference curl. It records `Delta M(z)` from full x-y slice
integrals, off-axis divergence error, curl-discretisation error, and
resolution/profile convergence.

The source formulas are anchored to `SpatialLocalization.lean:41-53`,
`:165-171`, and `:200-208`, with the physical potential route anchored to
`ActualPrimaryCoherence.lean:1633-1871`. The stream remains an explicit
diagnostic profile, not `selected_witness`. No selected `Delta m != 0`,
impossibility theorem, or kernel `False` is recorded by MAP-44.

The completed CUDA run used an RTX 4060 Ti, resolutions 129/193/257, profile
scales 0.5/1/2, modulations 0/0.25, and a fixed trusted radius `r > 0.1` for
finite-difference validation. At the finest resolution the declared profile
produced stable nonzero slice-defect ranges of approximately `0.244--0.364`
in `L∞` and `0.0841--0.1337` in the reported `L1` slice metric. For the
scale-1, zero-modulation control, the trusted divergence and Cartesian curl
errors decreased from the coarser runs to approximately `2.94` and `0.191` at
257 points; the product-rule residual decreased to `0.0449`. These are
numerical convergence diagnostics for the declared profile. They do not bind
the values to the selected `ASum`/`BSum`/`PSum` field and therefore do not
escalate CTR-005.

## MAP-45: Source-bound bridge candidate audit and recovery hand-off (2026-09-27)

The source census was rerun with `NavierStokes/` as its explicit root. It
reports 817 files, 429,297 source lines, 35,430 declarations, 2,940 import
edges, and 588 source-reachable modules. This is distinct from the repository-
wide atlas (2,790 Lean files / 649,366 Lean lines) and the compiled
source-joined selected closure (572 modules).

The seven lexical bridge candidates were inspected directly. They resolve to
rate estimates, base-germ equalities, origin blow-up transfer, schedule
construction, and selected-schedule packaging. None outputs the required
value-level equality between the selected Cartesian `ASum`/`BSum`/`PSum` field
and `(M,I,J,S,C_p)`. The exact trace is:
`NavierStokesReview/src/audit/selected_endpoint_bridge_trace_2026-09-27.md`.

The review-side extension
`NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
is correctly classified as a type-level non-implication: it pairs the
inhabited `Witness` proposition with an arbitrary nonzero five-coordinate
payload. It does not calculate the selected field and does not prove a false
selected premise. A direct Lean run is currently blocked by the absent
compiled object for `NavierStokes.ActualCandidateAssembly`; a timed targeted
build did not finish within 120 seconds. This is a build-state limitation,
not mathematical evidence.

`scratch_space/notes4.md` is now a controlling recovery input. Its unforced
reuse branch is recorded in the plan and goal documents, but remains separate
from the selected-endpoint verdict. No 1D Gaussian toy result is used as
selected-field evidence.
## 2026-09-27 semantic register hardening

The semantic coverage generator was corrected for the current hardened source
map. The full-tree output is generated from
`NavierStokesReview/evidence/hardened_source_map_2026-09-29.json` and is
stored as `semantic_coverage_register_full_2026-09-27.{json,md,html}`.
It records 2,790 indexed modules, 588 reachable modules, 108 explicit source
reviews, and 490 reachable modules awaiting declaration-level classification.

The separate register generated from the current source map covers
only 29 modules on explicitly recorded route paths. It is route evidence, not
the full dependency closure. This correction is methodological and does not
change CTR-005, the current correspondence classification, or the absence of
a selected-field (\Delta m\ne0) theorem.

The independent opportunity branch now has a review-side Lean specification
at `NavierStokesReview/src/extensions/UnforcedBranchSpecification.lean`.
It fixes `zeroForce` to the zero field and derives the zero-residual obligation
from `CandidateProperties`; no unforced existence theorem is claimed yet.

## Current register synchronisation — 2026-09-27

The authoritative current register now records 2,790 indexed modules, 588 reachable modules, 131 explicit source reviews, and 467 reachable modules awaiting declaration-level classification. The latest 23-module source tranche is in `NavierStokesReview/src/audit/unresolved_reachable_module_classification_2026-09-27.md`, with generated navigation views in `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.{json,md,html}`.

## Current register synchronisation: R3 analytical tranche

After the next raw-source tranche, the authoritative current register records **2,790 indexed modules, 588 reachable modules, 155 explicit source reviews, and 443 reachable modules awaiting declaration-level classification**. The 24-module report is `NavierStokesReview/src/audit/r3_analytical_module_classification_2026-09-27.md`. The generated JSON/Markdown/HTML views are the current machine-readable register; older counts above are retained as historical snapshots.

## MAP-46: Review-side bridge/completion register reconciliation (2026-09-27)

The semantic register now includes the 16 auditor-authored
completion/bridge files previously source-read but not reflected in the live
counts. The current full-tree register is 2,790 indexed modules, 588
reachable OpenAI source modules, 170 explicit source reviews, and 443
reachable OpenAI source modules awaiting declaration-level semantic
classification.

The 16-file report is
`NavierStokesReview/src/audit/review_side_completion_bridge_reaudit_2026-09-27.md`.
Those files are outside the OpenAI reachability graph, so the increase from
155 to 170 is evidence coverage, not endpoint closure. They establish
intermediate chart, direct-stage, cycle, and commutator facts, but no
inspected declaration supplies the complete selected-field identity

```text
barMoment(torusAverage(periodise(curl(tsum(potentialSum)) * cutoff)))
  = (M, I, J, S, C_p).
```

The cutoff-gradient term is consequently an open selected-field calculation.
This record does not assert `Delta m != 0`, an impossibility result, or
kernel-level `False`. The generated register views remain the authoritative
machine-readable and navigable outputs.

## MAP-47: Priority 0/1 source tranche register reconciliation (2026-09-27)

The live register now records **2,790 indexed modules, 588 reachable OpenAI
source modules, 199 explicit source-review records, and 414 reachable OpenAI
source modules awaiting declaration-level semantic classification**.

The 29-module source report is
`NavierStokesReview/src/audit/priority_0_1_source_review_2026-09-27.md`.
The generated JSON/Markdown/HTML outputs remain the authoritative register.

This tranche records substantive intermediate results in carrier geometry,
Gaussian/profile construction, covariance, curl geometry, reduced radial flux,
R3 weighted estimates, local series, compatible curl gluing, dyadic coverage,
and wave-state regularity. It does not assert that these results transport the
paper's five observables to `ActualCandidateAssembly.selected_witness`.
No `Delta m != 0`, impossibility theorem, or kernel-level `False` is claimed.
## MAP-48: priority 140-145 source tranche

On 2026-09-27, ten additional endpoint-reachable modules were directly reviewed and entered into the full semantic register. The register is now 2,790 indexed / 588 reachable / 209 evidence-inspected / 404 reachable-not-semantically-inspected. The report `NavierStokesReview/src/audit/priority_140_145_source_review_2026-09-27.md` confirms real reduced radial histories, positive-order five-row stress cancellations, covariance averaging, axis extensions, ODE reconstruction, and three-coordinate debt updates. These are upstream or intermediate results; they do not by themselves establish the final selected Cartesian \((M,I,J,S,C_p)\) transport theorem. No nonzero selected-field remainder or `False` is claimed.

## MAP-49: priority 135-139 source tranche

The full register is now **2,790 indexed / 588 reachable / 219 inspected /
394 reachable-not-semantically-inspected**. The ten-file report is
`NavierStokesReview/src/audit/priority_135_139_source_review_2026-09-27.md`.
It confirms non-vacuous terminal radial and pressure primitives, exact
pressure-mass cancellation, finite-support `tsum` collapse, local
periodised/cylindrical curl transport, harmonic mean-zero reconstruction,
coherent curl jet bounds, and pulse-history estimates. These facts narrow the
remaining semantic boundary but do not prove final selected-field moment
transport, `Delta m != 0`, impossibility, or `False`.

## MAP-50: priority 1-2 source tranche

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 229 inspected / 384 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_1_2_source_review_2026-09-27.md`.
It confirms a real intermediate `crossDefect` path and a later four-stage
result whose zero radial-moment hypotheses are explicit. The tranche does not
establish final selected-field moment transport, `Delta m != 0`, impossibility,
or kernel-level `False`.

## MAP-58: comparator/current-mode/heat-debt/residual-naturality tranche

Direct source review added six reachable modules to the semantic register: `ComparatorBridge`, `CurrentParticularPhysicalCoherence`, `CurrentPhysicalModeGerms`, `ExtendedHeatDebts`, `HarmonicStructurePreservation`, and `PhysicalResidualNaturality`. The report is `NavierStokesReview/src/audit/priority_133_129_132_source_review_2026-09-27.md`.

The regenerated authoritative register records **2,790 indexed / 588 reachable / 305 evidence-inspected / 308 reachable-open**. The tranche confirms real intermediate operator bridges, native-scale cancellations, positive-radius mode germs, scalar heat-debt jets, harmonic solenoidal invariants, and local residual naturality. It does not establish final selected-field `(M,I,J,S,C_p)` transport, a nonzero selected-field defect, impossibility, or `False`.

## MAP-59: initial/comparator/heat-tail/cylindrical tranche

The next six reachable modules are now directly reviewed and registered. The report is `NavierStokesReview/src/audit/priority_132_131_130_source_review_2026-09-27.md`. The tranche confirms real initial/Gaussian field bounds, comparator predicates, heat-tail regularity and limits, a signed mean-gain theorem, off-axis cylindrical residual identities, and outgoing history limits.

The regenerated authoritative register records **2,790 indexed / 588 reachable / 311 evidence-inspected / 302 reachable-open**. These results remain intermediate or coordinate-local. They do not establish selected-field `(M,I,J,S,C_p)` transport, a concrete nonzero defect, impossibility, or `False`.

## MAP-60: residual/rank bridge tranche

The next six modules are directly reviewed in `NavierStokesReview/src/audit/priority_130_129_residual_rank_source_review_2026-09-27.md` and entered into the authoritative register. The tranche confirms local Cartesian/cylindrical residual bridges, coordinate-layout covariance, transition-profile control, cycle mean/divergence propagation, and genuine `FiveRowRank` five-row repair algebra.

The regenerated authoritative register records **2,790 indexed / 588 reachable / 317 evidence-inspected / 296 reachable-open**. `FiveRowRank` is real intermediate repair mathematics, but no inspected declaration transports it into the final selected Cartesian field. No concrete selected-field `Delta m != 0`, impossibility theorem, or `False` is asserted.

## MAP-52: priority 7-61 R3 source tranche

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 249 inspected / 364 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_7_61_r3_source_review_2026-09-27.md`.
It confirms explicit mixed-candidate packaging and real R3 compact-support,
heat-kernel, cutoff-commutator, Fubini, weak-continuity, coordinate, and flat
cutoff results. It does not establish final selected-field moment transport,
`Delta m != 0`, impossibility, or kernel-level `False`.

## MAP-53: priority 61-64 localisation tranche

## MAP-54: priority 63-66 profile/axis source tranche

## MAP-55: priority 133-141 signed-profile and prefix source tranche

## MAP-56: priority 133-135 signed-dynamics source tranche

## MAP-57: priority 133-134 curl/endpoint source tranche

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 299 inspected / 314 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_133_134_curl_endpoint_source_review_2026-09-27.md`.
It confirms finite-label/harmonic bounds, an actual current-band Cartesian
curl bridge, initial native regularity, residual-limit construction, finite
particular assembly, concrete endpoint-input packaging, potential coherence,
and seed periodicity. It does not establish final selected-field moment
transport, `Delta m != 0`, impossibility, or kernel-level `False`.

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 289 inspected / 324 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_133_135_signed_dynamics_source_review_2026-09-27.md`.
It confirms concrete signed common-wave equations, exact exterior zero/support
behaviour, mean-increment residual algebra, temporal-state naturality, current
support/zero lemmas, potential transport, valid-band wave compatibility, and
coefficient deck periodicity. It does not establish final selected-field
moment transport, `Delta m != 0`, impossibility, or kernel-level `False`.

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 279 inspected / 334 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_133_141_source_review_2026-09-27.md`.
It confirms substantive signed profiles, covariance and scale identities,
actual wave/source bounds, periodic same-force uniqueness, physical sum
coherence, cycle periodicity, and finite-prefix Cartesian/polar field
agreement. `ActualPhysicalPrefixFields` supplies a finite-prefix `PhysicalData`
bridge. It does not establish final selected-field moment transport,
`Delta m != 0`, impossibility, or kernel-level `False`.

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 269 inspected / 344 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_63_66_profile_axis_source_review_2026-09-27.md`.
It confirms actual covariance/inverse bounds, spatial Borel extension,
true-cone correction, Bochner transport primitives, Gaussian zero-germ coverage,
physical polar geometry, axis-preservation/origin results, natural-axis
reference positivity, implicit heat coordinates, and positive-time signed
localisation. It does not establish final selected-field moment transport,
`Delta m != 0`, impossibility, or kernel-level `False`.

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 259 inspected / 354 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_61_64_localisation_source_review_2026-09-27.md`.
It confirms genuine curl, copy, cutoff, gluing, zero-mean modulation, tangent
ODE, and primary-copy bridge theorems. It does not establish final selected-
field moment transport, `Delta m != 0`, impossibility, or kernel-level `False`.

## MAP-51: priority 3-6 source tranche

On 2026-09-27, ten additional reachable modules were directly reviewed and
entered into the full semantic register. The register now records **2,790
indexed / 588 reachable / 239 inspected / 374 reachable-not-semantically-
inspected**. The report is
`NavierStokesReview/src/audit/priority_3_6_source_review_2026-09-27.md`.
The tranche confirms an explicit earlier-band cross-defect term and a
conditional prepared-tail cancellation, alongside real torus, parity,
profile-history, support, covariance, and coordinate theorems. It does not
establish final selected-field moment transport, `Delta m != 0`, impossibility,
or kernel-level `False`.
## Evidence update: 2026-09-28

Registered source tranche: `ResidualStability.lean`, `ParticularCopyBounds.lean`, `PastExtension.lean`, `LocalAxisymmetricResidual.lean`, `PhysicalGraphBounds.lean`, and `PrimaryPulseBounds.lean`. The tranche confirms real residual-stability, copy/pressure jet, time-extension, local axisymmetric PDE, physical graph, and primary pulse infrastructure. It does not close CTR-005: no inspected declaration transports the final activated Cartesian field to the paper tuple `(M,I,J,S,Cp)`.

Current register counts: 2,790 indexed; 588 reachable; 323 evidence-inspected; 290 reachable and not semantically inspected; 2,168 source-indexed review queued; 9 source-indexed files with a `sorry` token; 0 missing project import edges. These are coverage counters, not proof claims.
## Evidence update: 2026-09-28 assembly, geometry, and series tranche

Registered: `PrimaryFieldAssembly`, `R3/ComparisonGronwall`, `UniformHarmonicInteraction`, `ActualCycleGeometry`, `ActualPolarCoverage`, and `AxisSeries`. The direct review confirms real periodised field assembly, covariance and torus-average declarations, Gronwall comparison, uniform harmonic interaction, actual geometry identities, axis-aware coverage, and scalar axis-series estimates. No inspected declaration closes the final global five-observable transport bridge.

Register counts: 2,790 indexed; 588 reachable; 329 evidence-inspected; 284 reachable not semantically inspected; 0 missing project import edges. Counts are coverage evidence, not a completion or refutation certificate.

## Evidence update: 2026-09-28 graph, interaction, axis, pulse, rebasing, and stress tranche

Registered: `GraphCalculus`, `LocalizedMeanInteraction`, `NaturalAxisRange`, `PulseGrowth`, `TorusMeanRequestRebase`, and `BaseStressClasses`. The direct review confirms real off-axis graph calculus, local interaction/rate classes, axis-root and smooth-cutoff control, scalar pulse-growth classification, exact request rebasing, and weighted base-stress/jet classes. No inspected declaration closes the final global five-observable transport bridge.

Register counts: 2,790 indexed; 588 reachable; 335 evidence-inspected; 278 reachable not semantically inspected; 0 missing project import edges. Counts are coverage evidence, not a completion or refutation certificate.

## Evidence update: 2026-09-28 scales, coordinates, and comparison tranche

Registered: `ChartScales`, `EndpointCoordinates`, `R3/CompactComparisonBounds`, and `R3/ComparisonFiniteEnergy`. Direct review confirms genuine scale/asymptotic, endpoint-coordinate, compact comparison, finite-energy, and tensor-difference mathematics. No inspected declaration closes the final selected-field five-observable transport bridge, proves a nonzero selected-field defect, or derives `False`.

Register counts: 2,790 indexed; 588 reachable; 339 evidence-inspected; 274 reachable not semantically inspected; 0 missing project import edges. Counts are coverage evidence, not a completion or refutation certificate.

## Evidence update: 2026-09-28 R3 comparison-energy and slot-geometry tranche

Registered: `R3/ComparisonSetup`, `R3/LocalizedDifferenceEnergy`, `R3/LocalizedLaplacian`, `R3/SharpEnergyBound`, `R3/SpatialCauchySchwarz`, `R3/WholeSpaceEnergyLimit`, and `SlotGeometry`. Direct review confirms substantive weighted comparison-energy, localized integration, scalar energy, work, cutoff-limit, and slot-geometry mathematics. No inspected declaration closes the final selected-field five-observable transport bridge, proves a nonzero selected-field defect, or derives `False`.

Register counts: 2,790 indexed; 588 reachable; 346 evidence-inspected; 267 reachable not semantically inspected; 0 missing project import edges. Counts are coverage evidence, not a completion or refutation certificate.
### 2026-09-28 priority-69 source tranche: nine modules registered

Direct source review completed for `AnnularEndpoint.lean`, `AxisContraction.lean`, `PhysicalCopyBounds.lean`, `R3/LocalizedFluxEstimates.lean`, `ResetEnergyBounds.lean`, `ScaledActualParticularControl.lean`, `TerminalCone.lean`, `ViscousPropagator.lean`, and `VolterraAnalyticBounds.lean`. These modules add substantive support/germ, periodisation, reduced-axis, tail-energy, cone, coefficient-propagator, and analytic Volterra bounds. They do not state the final selected Cartesian `torusAverage`/`barMoment` transport theorem, and this tranche yields no nonzero defect, impossibility theorem, or kernel `False`.

The regenerated full semantic register now reports **355 evidence-inspected reachable modules** and **258 reachable modules still open**. The authoritative outputs are `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`, `.md`, and `.html`, mirrored under `docs/`. Detailed evidence is in `NavierStokesReview/src/audit/priority_69_annular_axis_copy_flux_reset_cone_propagator_source_review_2026-09-28.md`.

### 2026-09-28 priority-70 source tranche: four modules registered

Direct source review completed for `ActivationBounds.lean`, `ActualWaveRegularity.lean`, `CommonBaseContext.lean`, and `CopySolveCompatibility.lean`. These modules add substantive activation, wave regularity, base/stress-context, and generic copy-solve transport mathematics. No inspected declaration closes the final selected-field five-observable transport bridge, proves a nonzero selected-field defect, establishes impossibility, or derives `False`.

Register counts: 2,790 indexed; 588 reachable; 359 evidence-inspected; 254 reachable not semantically inspected; 0 missing project import edges. Counts are coverage evidence, not a completion or refutation certificate.

### 2026-09-28 priority-71 source tranche: four modules reviewed

Direct source review completed for `LocalizedCurlRealization.lean`, `MixedDiagonalExtensions.lean`, `ActualCarrierTransport.lean`, and `FiniteHeadClass.lean`. They add substantive local curl/divergence, support/extension, carrier-binding, and finite-head jet-class results. No inspected declaration closes the final selected-field five-observable transport bridge, proves a nonzero selected-field defect, establishes impossibility, or derives `False`.

Register counts remain 2,790 indexed; 588 reachable; 359 evidence-inspected; 254 reachable not semantically inspected; 0 missing project import edges. The rows were already evidence-classified; this tranche adds direct source evidence.

### 2026-09-28 priority-72 source tranche: four modules reviewed

Direct source review completed for `CorrectedPulseAmplitude.lean`, `PrimaryGeometryAssembly.lean`, `R3/ComparisonTimeAverages.lean`, and `SlowFirstOrderEdge.lean`. They add corrected energy-reset, reduced geometry, finite-energy time-average, and conditional radial-stress results. The first-order edge source explicitly refers global moment closure to separate renormalized-moment and slow-order theorems. No inspected declaration in this tranche closes the final selected-field five-observable transport bridge, proves a nonzero selected-field defect, establishes impossibility, or derives `False`.

Register counts are now 2,790 indexed; 588 reachable; 363 evidence-inspected reachable; 250 reachable not semantically inspected; 0 missing project import edges. Detailed evidence: `NavierStokesReview/src/audit/priority_72_pulse_geometry_average_first_order_source_review_2026-09-28.md`.

### 2026-09-28 priority-73 source tranche: six modules reviewed

Direct source review completed for `ActualBaseVelocityBounds.lean`, `BaseContextAssembly.lean`, `PhaseEstimates.lean`, `PrimaryRepresentatives.lean`, `PositiveRepresentatives.lean`, and `ReservedPatches.lean`. They confirm actual coefficient/support and rate identities, reduced stress realisation, phase and representative geometry, and genuine radial `FiveProfileMoments`/`FiveRowRank` patch identities. No inspected declaration in this tranche closes final selected-field five-observable transport, proves a nonzero selected-field defect, establishes impossibility, or derives `False`.

Register counts are now **2,790 indexed; 588 reachable; 369 evidence-inspected reachable; 244 reachable not semantically inspected; 0 missing project import edges**. Detailed evidence: `NavierStokesReview/src/audit/priority_73_base_representative_reserved_source_review_2026-09-28.md`.
## Audit state update: 2026-09-28

Coverage is **375 evidence-inspected of 588 reachable modules**, with **238 reachable modules still open** and **0 missing project import edges**. The latest six-file tranche confirms substantive activation, control, extension, local-field, and frame layers, but supplies no final selected-field five-moment equality. Evidence: `NavierStokesReview/src/audit/priority_74_activation_control_extension_frame_source_review_2026-09-28.md`.
## Audit state update: 2026-09-28 cutoff/Volterra/wave-interaction tranche

Coverage is **381 evidence-inspected of 588 reachable modules**, with **232 reachable modules still open** and **0 missing project import edges**. The tranche confirms exact support-separated curl cancellations and real intermediate moment/sum infrastructure; it does not establish the complete selected-field five-observable equality. Evidence: `NavierStokesReview/src/audit/priority_75_wave_cutoff_volterra_sum_loop_tail_interaction_source_review_2026-09-28.md`.
## Audit state update: 2026-09-28 radial/chart/integral tranche

Coverage is **392 evidence-inspected of 588 reachable modules**, with **221 reachable modules still open** and **0 missing project import edges**. The tranche adds positive base-radial and actual-integral evidence while preserving the distinction between intermediate radial identities and the final selected-field five-observable transport theorem. Evidence: `NavierStokesReview/src/audit/priority_76_radial_chart_jets_extension_rephase_integral_source_review_2026-09-28.md`.

## Audit state update: 2026-09-28 axis/dilation/extension/ODE tranche

Coverage is **400 evidence-inspected of 588 reachable modules**, with **213 reachable modules still open** and **0 missing project import edges**. `OutgoingDilation.lean` provides positive reduced-profile definitions and identities for the moment quantities, while the complete selected Cartesian five-observable transport remains unlocated. Evidence: `NavierStokesReview/src/audit/priority_77_axis_evaluation_resolvent_phase_gaussian_dilation_extension_ode_source_review_2026-09-28.md`.

### 2026-09-28 priority-78 source tranche

Coverage is now **414 evidence-inspected of 588 reachable modules**, with **199 reachable modules still open** and **0 missing project import edges**. Direct review of the phase-defect, axis-algebra, weighted-coefficient, polar-chart, stress-activation, and Volterra-regularity modules found substantive intermediate identities but no complete selected Cartesian `(M,I,J,S,C_p)` transport theorem, nonzero defect proof, impossibility theorem, or kernel `False`. Evidence: `NavierStokesReview/src/audit/priority_78_phase_defect_axis_algebra_weighted_volterra_source_review_2026-09-28.md`.

### 2026-09-28 priority-79 source tranche

Coverage is now **420 evidence-inspected of 588 reachable modules**, with **193 reachable modules still open** and **0 missing project import edges**. Direct review of the axis-operator, chart-jet, matching-cone, physical-coordinate, signed-covariance, and wave-edge modules found substantive intermediate identities but no complete selected Cartesian `(M,I,J,S,C_p)` transport theorem, nonzero defect proof, impossibility theorem, or kernel `False`. Evidence: `NavierStokesReview/src/audit/priority_79_axis_chart_matching_coordinate_covariance_edge_source_review_2026-09-28.md`.
## Priority 80 evidence tranche (2026-09-28)

Report: [`priority_80_axis_endpoint_radial_transport_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_80_axis_endpoint_radial_transport_source_review_2026-09-28.md). Register after regeneration: 2,790 indexed; 588 reachable; 426 evidence-inspected; 187 reachable-not-semantically-inspected; 0 missing project import edges.

Finding: exact reduced radial integral and weighted-mean transport exists in `RadialPullback` and `WeightedRadialPrimitive`, and `ReferencePath.histories` reconstructs reduced pressure/moment state. The missing item remains the selected 3D Cartesian composition and export into `Witness`; this is a correspondence gap, not evidence that upstream moment machinery is absent. No unconditional refutation is recorded.
## Priority 81 evidence tranche (2026-09-28)

Report: [`priority_81_r3_residual_gauge_outgoing_moment_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_81_r3_residual_gauge_outgoing_moment_source_review_2026-09-28.md). Register after regeneration: 2,790 indexed; 588 reachable; 438 evidence-inspected; 175 reachable-not-semantically-inspected; 0 missing project import edges.

Positive findings: two exact outgoing reduced moment cancellations; pressure-defect equals the auxiliary-torus-averaged zeroth radial mass; actual potential-sum residual and physical joint-jet identities; and periodic-to-compact R3 packaging. Corrected classification: upstream/reduced moment bridges are present, while complete five-observable selected-Cartesian transport into `Witness` remains unestablished. No unconditional refutation is recorded.

## Priority 82 evidence tranche (2026-09-28)

Report: [`priority_82_debt_exterior_scaling_entrance_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_82_debt_exterior_scaling_entrance_source_review_2026-09-28.md). The current register is 2,790 indexed; 588 reachable; 444 evidence-inspected; 169 reachable-open; and 0 missing project import edges.

Positive findings are recorded for actual intermediate debt, exterior annular support, exact R³ energy/support scaling, selected-to-compact candidate packaging, and reduced entrance flux identities. These findings narrow the open issue; they do not prove or refute the complete selected Cartesian `(M,I,J,S,C_p)` transport.

## Priority 83 evidence tranche (2026-09-28)

Report: [`priority_83_partition_angular_gaussian_stress_request_covariance_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_83_partition_angular_gaussian_stress_request_covariance_source_review_2026-09-28.md). The current register is 2,790 indexed; 588 reachable; 444 evidence-inspected; 169 reachable-open; and 0 missing project import edges.

Positive findings are recorded for exact squared partition identities, mixed curl-plus-angular field and divergence construction, Gaussian tail/jet control, leading stress edge/exterior bounds, signed torus/radial request identities, and pulse covariance/cone positivity. These are intermediate bridges, not the complete selected Cartesian five-observable theorem.

## Priority 84 evidence tranche (2026-09-28)

Report: [`priority_84_axis_heat_release_torus_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_84_axis_heat_release_torus_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 450 evidence-inspected; 163 reachable-open; and 0 missing project import edges.

Positive findings are recorded for actual positive-axis Volterra profiles, pulse-lag and reset equations, radial heat moment ODEs, renormalised release moments, heated physical axial-viscosity cancellation, and torus/Jacobian/periodisation averages. These findings narrow the remaining question but do not establish the complete selected Cartesian `(M,I,J,S,C_p)` transport, a nonzero selected-field defect, an impossibility theorem, or `False`.

## Priority 85 evidence tranche (2026-09-28)

Report: [`priority_85_signed_geometry_repair_cone_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_85_signed_geometry_repair_cone_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 456 evidence-inspected; 157 reachable-open; and 0 missing project import edges.

## Priority 86 evidence tranche (2026-09-28)

Report: [`priority_86_rank_cycle_compensation_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_86_rank_cycle_compensation_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 462 evidence-inspected; 151 reachable-open; and 0 missing project import edges.

`BaseRankPatch.five_rows` provides a genuine local `FiveRowRank.FiveRows` theorem for the full final base. The same tranche records actual cycle/covariance preservation, rank-state bounds, terminal compensation, and mean-stage support data. These are positive local bridges; the final selected Cartesian composition remains unestablished, and no nonzero defect, impossibility theorem, or `False` is asserted.

Critical correction: `RepairConeBounds.actual_moments` and its `physical_rows`/`physical_stock_values`/`physical_transport` family provide genuine reduced five-coordinate and physical chart transport. The unresolved claim is narrower: the reviewed declarations do not establish composition of those values with the final Cartesian curl/localisation/`tsum`/periodisation/pressure-force selected endpoint and public `Witness`. No selected-field nonzero defect, impossibility theorem, or `False` is asserted.

## Priority 87 evidence tranche (2026-09-28)

Report: [`priority_87_residual_grouping_decay_compact_force_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_87_residual_grouping_decay_compact_force_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 468 evidence-inspected; 145 reachable-open; and 0 missing project import edges.

The tranche records actual axisymmetric/local residual grouping, diagonal residual flatness and curl-rate transfer, compact temporal/spatial force decay, and a uniform \(R^3\) compact-force \(L^2\) bound. These are positive intermediate results. The selected Cartesian five-observable composition remains unestablished; no nonzero defect, impossibility theorem, or `False` is asserted.

## Priority 88 evidence tranche (2026-09-28)

Report: [`priority_88_profile_cone_cover_similarity_mean_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_88_profile_cone_cover_similarity_mean_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 483 evidence-inspected; 130 reachable-open; and 0 missing project import edges.

The tranche records actual reduced cone/stress and loop-moment algebra, analytic axis/heat extensions, similarity-coordinate transitions, Cartesian axisymmetric curl/support identities, periodised-copy solves, and temporal mean updates. These are positive intermediate results. The final selected Cartesian five-observable composition remains unestablished; no nonzero defect, impossibility theorem, or `False` is asserted.

## Priority 89 evidence tranche (2026-09-28)

Report: [`priority_89_moment_repair_stress_alias_curl_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_89_moment_repair_stress_alias_curl_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 494 evidence-inspected; 119 reachable-open; and 0 missing project import edges. The tranche confirms real compact/reduced repair, stress, torus-alias, local gauge-mass, and Cartesian-curl declarations, while leaving the complete public selected-field five-observable composition unresolved.

## Priority 90 evidence tranche (2026-09-28)

Report: [`priority_90_moment_matrix_prepared_profiles_gaussian_solver_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_90_moment_matrix_prepared_profiles_gaussian_solver_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 499 evidence-inspected; 114 reachable-open; and 0 missing project import edges. The tranche confirms general moment-matrix, profile-scheduling, Gaussian-integrability, and abstract quadratic-repair declarations, without promoting them to final selected-field transport.

## Priority 91 evidence tranche (2026-09-28)

## Priority 92 evidence tranche (2026-09-28)

Report: [`priority_92_r3_energy_force_polar_graph_uniform_weights_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_92_r3_energy_force_polar_graph_uniform_weights_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 508 evidence-inspected; 105 reachable-open; and 0 missing project import edges. The tranche records genuine R3 energy/dissipation, smooth force localisation, off-axis polar graph reconstruction, and uniform curl/rate infrastructure. It does not establish the final selected Cartesian moment tuple at `Witness`.

Report: [`priority_91_parametric_inverse_periodic_phase_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_91_parametric_inverse_periodic_phase_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 501 evidence-inspected; 112 reachable-open; and 0 missing project import edges. `ParametricTorusInverse` and `PeriodicPhaseAssembly` provide real torus-inverse, Fourier, phase, periodicity, local-finiteness, geometry-transport, germ, and jet results. They remain intermediate evidence and do not establish the final selected Cartesian moment tuple at `Witness`.
## Priority 93 evidence tranche (2026-09-28)

Report: [`priority_93_limits_debt_lifespan_reindex_pulse_flux_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_93_limits_debt_lifespan_reindex_pulse_flux_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 514 evidence-inspected; 99 reachable-open; and 0 missing project import edges. The tranche records genuine boundary-limit/flat-residual, reduced debt-matching, lifespan, reindexing, pulse-history, and local radial-flux results. It does not establish the final selected Cartesian moment tuple at `Witness`.
## Priority 94 evidence tranche (2026-09-28)

## Priority 95 evidence tranche (2026-09-28)

Report: [`priority_95_r3_pressure_comparison_scaling_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_95_r3_pressure_comparison_scaling_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 539 evidence-inspected; 74 reachable-open; and 0 missing project import edges. The tranche confirms relative pressure recovery, compact-test Poisson identities, Riesz/Fourier estimates, viscosity scaling, and whole-space comparison closure. It does not establish an absolute selected pressure representative or the final selected Cartesian moment tuple at `Witness`.

## Priority 96 evidence tranche (2026-09-28)

Report: [`priority_96_core_support_pressure_recovery_localization_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_96_core_support_pressure_recovery_localization_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 558 evidence-inspected; 55 reachable-open; and 0 missing project import edges. The tranche confirms concrete core/support, switching, comparative weak-pressure, compact-test, Riesz, reduced schedule-pressure, tail/cone, and uniform-rate infrastructure. It does not establish the final selected Cartesian moment tuple at `Witness`.

## Priority 97 evidence tranche (2026-09-28)

Direct source review of eleven modules is recorded in [`priority_97_local_curl_profile_moment_bridge_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_97_local_curl_profile_moment_bridge_source_review_2026-09-28.md). `ActualMeanPotentialRealization` and `TailGaugePotential` provide genuine local Cartesian-curl/potential identities; `NominalConeAssembly` provides genuine reduced/chart moment identities. These positive bridges narrow, rather than close, CTR-005: the composed selected global-sum/localisation/periodisation-to-`Witness` theorem remains unestablished. Register state: 2,790 indexed, 588 reachable, 569 evidence-inspected, 44 reachable-open, and 0 missing project import edges. No `Delta m != 0`, impossibility, or `False` classification is authorised.

## Priority 98 evidence tranche (2026-09-28)

Direct source review of eleven modules is recorded in [`priority_98_signed_gauge_copy_support_axis_transport_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_98_signed_gauge_copy_support_axis_transport_source_review_2026-09-28.md). The tranche adds positive evidence for signed native regularity, gauge/alias decay, copy-path transport, support preservation, reduced exterior matching, axis pressure data, positive-time signed wave data, reduced pressure kernels, and scaled tangent transport. Register state: 2,790 indexed, 588 reachable, 580 evidence-inspected, 33 reachable-open, and 0 missing project import edges. No final selected-field five-observable equality, `Delta m != 0`, impossibility, or `False` classification is authorised.

## Priority 109 evidence tranche (2026-09-28)

Direct source review of twelve modules is recorded in [`priority_109_carrier_cycle_signed_axis_pressure_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_109_carrier_cycle_signed_axis_pressure_source_review_2026-09-28.md). The tranche adds positive carrier support, signed `tsum` amplitude/pressure transport, cycle/copy coherence, angular curl invariance, reduced-axis transport, future pressure integrals, physical-stage rate bounds, and comparative pressure-flux evidence. Register state: 2,790 indexed, 588 reachable, 592 evidence-inspected, 21 reachable-open, and 0 missing project import edges. No final selected-field five-observable equality, nonzero defect, impossibility, or `False` classification is authorised.

## Priority 110 evidence tranche (2026-09-28)

Direct source review of four modules is recorded in [`priority_110_cycle_initial_particular_pressure_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_110_cycle_initial_particular_pressure_source_review_2026-09-28.md). The tranche adds positive initial-state construction, cycle coherence, particular native data, and reduced corrected-pressure bounds. Register state: 2,790 indexed, 588 reachable, 596 evidence-inspected, 17 reachable-open, and 0 missing project import edges. No final selected-field five-observable equality, nonzero defect, impossibility, or `False` classification is authorised.

## Priority 111 evidence tranche (2026-09-28)

The three-module report is [`priority_111_cycle_preservation_particular_realization_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_111_cycle_preservation_particular_realization_source_review_2026-09-28.md). It adds positive source evidence for cycle invariants, curl-corrected velocity and pressure realization, germ/cutoff/support transport, and cycle-domain equality. The final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` composition remains unproved in this tranche. Register state: 2,790 indexed, 588 reachable, 599 evidence-inspected, 14 reachable-open, and 0 missing project import edges.

## Priority 112 evidence tranche (2026-09-28)

Direct source review of `ActivationStocks.lean`, `DiagonalJetBounds.lean`, and `ExtendedHeatedOutgoing.lean` is recorded in [`priority_112_activation_diagonal_extended_heated_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_112_activation_diagonal_extended_heated_source_review_2026-09-28.md). The tranche confirms reduced stock/jet identities, locally finite `tsum` derivative and tail estimates, and substantive reduced-profile compensation and zero-moment identities. It does not establish the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` equality. Register state: 2,790 indexed, 588 reachable, 602 evidence-inspected, 11 reachable-open, and 0 missing project import edges. No nonzero defect, impossibility, or `False` classification is authorised.

## Priority 113 evidence tranche (2026-09-28)

Direct source review of `HeatedOutgoing.lean`, `ModeSolenoidalReindex.lean`, and `ShapedWaitBounds.lean` is recorded in [`priority_113_heated_mode_reindex_shaped_wait_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_113_heated_mode_reindex_shaped_wait_source_review_2026-09-28.md). The tranche confirms reduced compensation rows, local mode-level solenoidal reindexing, and temporal wait/pressure/decay estimates. It does not establish the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` equality. Register state: 2,790 indexed, 588 reachable, 605 evidence-inspected, 8 reachable-open, and 0 missing project import edges. No nonzero defect, impossibility, or `False` classification is authorised.

## Priority 114 evidence tranche (2026-09-28)

The eight-module report is [`priority_114_final_reachable_eight_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_114_final_reachable_eight_source_review_2026-09-28.md). It confirms real reduced radial moment/stress identities, curl-lifted backgrounds, rank/debt regularity, periodic integration/localisation, lattice periodisation, periodic Sobolev consequences, and native copy/jet bounds. Reachable source coverage is now complete: 2,790 indexed; 588 reachable; 613 evidence-inspected; 0 reachable-open; 0 missing project import edges. The final selected Cartesian observable composition remains unproved. No nonzero defect, impossibility, or `False` classification is authorised.

Report: [`priority_94_histories_means_harmonic_exterior_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_94_histories_means_harmonic_exterior_source_review_2026-09-28.md). The regenerated register is 2,790 indexed; 588 reachable; 521 evidence-inspected; 92 reachable-open; and 0 missing project import edges. The tranche records genuine reduced histories/repair, initial means, harmonic support/calculus, exterior prefix agreement, particular-mean covariance gain, and signed potential/pressure support. It does not establish the final selected Cartesian moment tuple at `Witness`.
## 2026-09-28 probe hardening: periodic versus compact selected fields

The latest source review blocks a specific unsafe inference. The compact
whole-space field has support theorems, while the selected mixed radial
observable is built from a periodic velocity branch. The source proves local
eventual equality on an inner cube, not a global equality or a transfer of
bounded radial support. `SelectedPeriodicSupportTransportGate.lean` captures
the exact conditional consequence: periodicity plus bounded radial support
forces the selected pullback to vanish, so a contradiction would require both
the missing support-transport theorem and a nonzero selected-field witness.

Those premises are not currently proved. This is a hardened falsification
target, not a `False` result. Its direct Lean check is also pending because
`completions.SelectedMixedRadialSupportObstruction.olean` is absent after the
previous package rebuild timeout. Until the review package is rebuilt under
`leanprover/lean4:v4.34.0-rc2`, the gate is source-reviewed only.

## 2026-09-28 probe-logic adversarial review

Probe validity is now recorded separately from the mathematical claim that a
probe investigates. The review report is
`NavierStokesReview/src/audit/priority_119_probe_logic_adversarial_review_2026-09-28.md`.
It classifies each probe by concrete expression, domain, hypotheses,
conclusion, and prohibited extrapolations.

The new source completion
`NavierStokesReview/src/completions/SelectedDirectCutoffMomentBoundary.lean`
proves the selected direct-stage identity

\[
u_{\mathrm{cut},1}-u_{\mathrm{native},1}
=(c-1)u_{\mathrm{native},1}.
\]

This identifies the exact cutoff-defect channel in the selected source path.
It does not prove that the final periodised infinite sum has a nonzero
`barMoment`, and it does not prove `False`. The completion remains
source-reviewed rather than compiler-verified while the pinned review package
is incomplete.

Explicit prohibitions are now: native zero moment does not transfer
automatically through cutoffs or periodisation; a commutator does not imply a
nonzero integral; finite-prefix control does not imply `tsum` control; local
equality does not imply global radial equality; interface ghost data does not
describe the selected physical field; and a conditional support/nonvanishing
gate is not an achieved contradiction.

Current register snapshot: 2,792 indexed modules; 588 in the captured
Navier--Stokes endpoint closure; 629 evidence-inspected rows; 2,154
source-indexed review-queued rows; zero missing project import edges; and ten
source rows containing a `sorry` token. These are coverage metrics only.

## 2026-09-28 register correction after Priority 122 Euler tranche

The report
`NavierStokesReview/src/audit/priority_122_euler_operator_projection_source_review_2026-09-28.md`
reviews ten Euler modules covering translation graphs, coefficient paths,
Sobolev/operator bounds, compact curl, parameter integrals, projected Euler
pairings, compact smoothness, and bounded compact-support paths. They are
genuine Euler infrastructure outside the captured Navier--Stokes endpoint
closure. They do not establish the selected Navier--Stokes radial-moment
transport.

The regenerated register reports 2,792 indexed modules; 588 in the captured
Navier--Stokes endpoint closure; 659 evidence-inspected rows; 2,124
source-indexed review-queued rows; zero missing project import edges; and ten
source rows containing a `sorry` token.

## 2026-09-28 Priority 123 selected endpoint-junction review

The source report
`NavierStokesReview/src/audit/priority_123_selected_ns_paper_endpoint_junction_review_2026-09-28.md`
audits eight Navier--Stokes junctions that could conceal a transport theorem:
`PeriodicPaperTheorem`, `PeriodicPaperScalingSupport`,
`WholeDomainPhysicalStageTheorem`, `ActualParticularPhysicalData`,
`MeanStageContinuation`, `CycleContinuationInvariant`,
`SignedRequestContinuation`, and `CorrectionInitializationNoOptions`.

The result is deliberately two-sided. These files contain genuine physical
data, potential/pressure `tsum` and summability identities, support and
periodicity transport, continuation invariants, residual estimates, and a
real periodic C/D packaging theorem. This rules out the overstatement that
the selected path uses only abstract rates or that the upstream machinery is
absent.

At the same time, the inspected declarations do not expose the decisive
field-level equality

\[
\operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p).
\]

No nonzero defect, impossibility theorem, or kernel-level `False` is claimed
from this tranche. The live classification remains **CTR-005: correspondence
not established**, pending declaration-level search over the remaining
source scope. “Outside the captured endpoint closure” remains a scope label,
not a dead-code claim.

Register after Priority 123: **2,792 indexed modules**, **588 captured
endpoint-closure modules**, **677 evidence-inspected rows**, **2,106 queued
rows**, zero missing project import edges, and ten source rows containing a
`sorry` token.

## 2026-09-28 Priority 124 selected dynamics/comparator/appendix review

The source report
`NavierStokesReview/src/audit/priority_124_selected_ns_dynamics_comparator_appendix_review_2026-09-28.md`
reviews ten further endpoint-adjacent modules:
`ActualParticularDynamicsNoOptions`, `AppendixHeatResults`,
`AppendixJoiningResults`, `BaseWitnessClosure`, `CommonCoverWithin`,
`CompactHolomorphicFamily`, `ComparatorR3Bridge`, `ComparatorSolution`,
`EndpointLimits`, and `FlatPrimitivePaper`.

They contain real selected dynamics, profile/joining bounds, finite local
summation, comparator residual packages, endpoint jet hypotheses, and compact
smooth primitives. The review found no declaration proving

\[
\operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p).
\]

The anti-blindside boundaries are explicit: a local heat `moment_zero` use is
not the final field observable; a comparator theorem is not selected-field
transport; finite local sums are not a global radial `tsum`; and a smooth left
endpoint extension does not bridge the off-axis chart to the origin
singularity. No nonzero defect or kernel `False` is claimed.

Register after Priority 124: **2,792 indexed modules**, **588 captured
endpoint-closure modules**, **677 evidence-inspected rows**, **2,106 queued
rows**, zero missing project import edges, and ten source rows containing a
`sorry` token.

## 2026-09-28 register correction after Euler tranche

The source report
`NavierStokesReview/src/audit/priority_120_euler_transport_foundation_source_review_2026-09-28.md`
classifies ten Euler-side foundation/transport/regularity modules. The
regenerated register reports 2,792 indexed modules; 588 in the captured
Navier--Stokes endpoint closure; 639 evidence-inspected rows; 2,144
source-indexed review-queued rows; zero missing project import edges; and ten
source rows containing a `sorry` token. These are coverage metrics, not a
kernel verdict.

## 2026-09-28 register correction after Priority 121 Euler tranche

`NavierStokesReview/src/audit/priority_121_euler_bounded_flow_analytic_source_review_2026-09-28.md`
records declaration-level review of ten Euler bounded-flow and analytic
modules. They are real repository-wide Euler infrastructure outside the
captured Navier--Stokes endpoint closure. This does not classify them as dead
and does not establish the selected Navier--Stokes radial-moment transport.

The regenerated register reports 2,792 indexed modules; 588 in the captured
Navier--Stokes endpoint closure; 649 evidence-inspected rows; 2,134
source-indexed review-queued rows; zero missing project import edges; and ten
source rows containing a `sorry` token. These are coverage metrics only.

## 2026-09-28 Priority 125 probe-logic hardening

The controlling review is
`NavierStokesReview/src/audit/priority_125_probe_logic_hardening_2026-09-28.md`.
The repository-wide instrument is
`NavierStokesReview/src/audit/selected_transport_audit.py`, with outputs
`NavierStokesReview/evidence/selected_transport_audit_full_2026-09-28.md` and
`.json`.

The instrument now strips nested Lean comments before classifying declaration
terms, includes `selectedPotentialComponent` in the field vocabulary, and
separates positive transport-review candidates from conditional gates,
obstructions, interface countermodels, and co-occurrence. This corrects two
detector blindspots before evidence is interpreted.

Repository-wide result: **33,986 declarations**, **11 joint candidates**, and
**3 positive manual-review candidates**. The three are explicit pullback
identities requiring a supplied scalar profile and point-to-space-time map;
they are not proofs that the final activated Cartesian selected field carries
\((M,I,J,S,C_p)\). The historical Lean environment snapshot reports the
selected endpoint types but is not asserted fresh against the current tree.

The regenerated register remains **2,792 indexed modules**, **588 captured
endpoint-closure modules**, **677 inspected Lean-module rows**, **2,106 queued
rows**, zero missing project import edges, ten source rows containing a
`sorry` token, and **19 supplemental audit artifacts**. No selected transport,
nonzero \(\Delta m\), impossibility theorem, or kernel `False` is claimed.

## 2026-09-28 Priority 126: selected finite-prefix and radial transport review

Source report:
`NavierStokesReview/src/audit/priority_126_selected_field_finite_prefix_transport_review_2026-09-28.md`.

This tranche was added to prevent a false negative caused by inspecting only
the exported `Witness` proposition. It verifies source declarations for the
concrete selected path through finite potential prefixes, spatial curls,
cutoff product rules, the mixed direct branch, torus averaging, radial
pullback, and `barMoment`.

The source proves an exact cutoff-gradient commutator and finite-prefix
identities. It does **not** yet prove that the commutator is nonzero, that
the infinite selected `tsum` may be exchanged with the radial integral, or
that the resulting five observables equal `(M, I, J, S, C_p)`. The direct
branch and positive-radius/global-axis scope remain explicit review gates.

Register after regeneration: **2,792 indexed modules**, **588 captured
endpoint-closure modules**, **688 inspected Lean-module rows**, **2,095
queued rows**, zero missing project import edges, ten source rows containing
a `sorry` token, and **23 supplemental audit artifacts**. No selected
transport, nonzero \(\Delta m\), impossibility theorem, or kernel `False` is
claimed.

## 2026-09-28 Priority 127: source provenance and environment-closure integrity

The controlling review is
`NavierStokesReview/src/audit/priority_127_source_provenance_and_environment_integrity_review_2026-09-28.md`.
The hardened detector was run both over the whole workspace and over
`NavierStokes/` alone. The whole-workspace run reports 34,583 declarations
and 11 joint candidates, all with origin `review_completion`; the source-only
run reports 31,472 OpenAI-source declarations, zero joint candidates, and zero
positive manual candidates. The source-only result is a conservative search
boundary, not an absence theorem.

The environment closure is not currently usable as endpoint evidence. The
supplied snapshot is missing the configured selected endpoint roots, and a
fresh `EnvironmentDependencyExport.lean` run failed because
`.lake/build/lib/lean/NavierStokes/R3/Theorem.olean` is absent. A follow-up
`lake build NavierStokes` exceeded the 120-second limit and was stopped with
its Lean children. This timeout is recorded explicitly rather than hidden
behind the old snapshot. The next gate is an exact source build and fresh
dependency export, followed by separate
compilation of the review-side completion probes. No `False`, nonzero
\(\Delta m\), impossibility, or formal-refutation status follows from this
provenance review.

## 2026-09-28 Priority 128: adversarial probe-contract review

Report:
`NavierStokesReview/src/audit/priority_128_probe_logic_adversarial_contracts_2026-09-28.md`.
Instrument:
`NavierStokesReview/src/audit/probe_logic_contract_audit.py`.

The instrument reviewed 262 review-authored declarations. It found 91
selected-term declarations, 20 declarations with explicit conditional-premise
markers, 88 declarations with strong-conclusion markers, and zero
unconditional endpoint claims authorised. The matrix keeps interface
countermodels, ghost/type-boundary payloads, conditional support/nonzero
gates, fixed-force path-dependence tests, and review-completion identities
separate. It is an anti-blindside control, not a theorem and not an absence
proof.

No probe may establish `False`, \(\Delta m\ne0\), or formal refutation without
exact selected-field provenance, all premises derived on the selected branch,
current-environment compilation, and the required `tsum`, integration,
periodisation, axis, and global-domain arguments. The regenerated register is
2,792 indexed modules, 588 captured endpoint-closure modules, 688
evidence-inspected rows, 2,095 queued rows, 26 supplemental audit artifacts,
zero missing project import edges, and ten source rows containing a `sorry`
token. No verdict escalation is recorded.

## Priority 129: external R3 pressure and endpoint-adjacent source review

Report:
`NavierStokesReview/src/audit/priority_129_external_r3_pressure_comparator_source_review_2026-09-28.md`.

This tranche corrects a possible blindside in both directions. It does not
call every pressure, periodisation, or rebundle result irrelevant, and it does
not promote a local identity to the selected global bridge.

| Source result | Actually established | Still unproved |
|---|---|---|
| `PeriodizePDE.navier_stokes_periodize` | Conditional residual covariance for supported fields and `r < 1/2` | Selected five-observable transport, radial/axis limits, and global `tsum` interchange |
| `LocalPotentialRebundle` | Finite-stage and exterior pointwise identities | Global selected-field radial integral and `(M,I,J,S,C_p)` equality |
| `LocalPaperTheorem.Properties` | Smoothness, curl/decomposition, divergence, extensions, jets, residual flatness, exterior behaviour | A selected Cartesian moment observable |
| R3 pressure modules | Majorants, near-kernel estimates, conditional distributional representation | Absolute selected pressure Poisson/Leray semantics |
| Comparator/sharp-bound modules | Conditional C/D packages and stage/rate bounds | Paper-to-endpoint moment transport |

The live register now reports **2,792 indexed**, **588 captured
endpoint-closure modules**, **703 evidence-inspected rows**, **2,080
source-indexed rows queued**, **0 missing project import edges**, **10 source
rows containing a `sorry` token**, and **29 supplemental audit artifacts**.
These are coverage metrics. They do not authorise `False`, `Delta m != 0`, or
formal-refutation claims.

## Priority 130: Euler comparator and cylinder-average source review

Report:
`NavierStokesReview/src/audit/priority_130_euler_comparator_cylinder_average_source_review_2026-09-28.md`.
The source review records genuine external Euler curl, angular-average,
zero-mean, comparator, Dirichlet, and acceleration results. It does not bind
them to the selected Navier--Stokes witness or to the five-observable global
transport theorem.

The live register is **2,792 indexed**, **588 captured endpoint-closure
modules**, **718 evidence-inspected rows**, **2,065 source-indexed rows
queued**, **0 missing project import edges**, **10 source rows containing a
`sorry` token**, and **31 supplemental audit artifacts**. No verdict
escalation is recorded.

## Priority 133: external source profile and NS junction tranche

Evidence:

- NavierStokesReview/src/audit/external_source_profile.py
- NavierStokesReview/evidence/external_source_profile_full_2026-09-28.json
- NavierStokesReview/evidence/external_source_profile_full_2026-09-28.md
- NavierStokesReview/src/audit/priority_132_external_ns_junction_h3_periodic_candidate_review_2026-09-28.md
- NavierStokesReview/evidence/source_tranche_external_ns_junction_2026-09-28.json

The external profile accounts for all **2,204 modules outside the captured
endpoint closure**. It is a structural profile, not a semantic review and
not a dead-code claim. The 15-file Navier--Stokes junction tranche records
genuine conditional candidate, periodic, H3, comparator, localisation, and
lifespan infrastructure. It finds no final selected-field barMoment equality,
no nonzero defect calculation, no impossibility proof, and no kernel
contradiction. CTR-005 remains a correspondence gap pending the full
external and review-side audit.

Current register snapshot after regeneration: **2,792 indexed modules**, **588
captured endpoint-closure modules**, **731 evidence-inspected rows**, **2,052
source-indexed rows queued**, **0 missing project import edges**, **10 source
rows containing a sorry token**, and **36 supplemental audit artifacts**.
These are coverage measurements only.

The consolidation gate remains mandatory: fetch/read/fact-check all current
documents and evidence first; then move only confirmed redundant or superseded
files, never delete them, to scratch_space/archive_preconsolidation/ with a
path/reason/SHA-256 manifest. Commits are local coherent tranches; no push
is authorised without explicit user instruction.

## Priority 131: consolidation, archive, and commit control

The audit must not accumulate an opaque pile of documents or commits. After
the source review is sufficiently consolidated, execute a document-control
pass that fetches and reads every current map, plan, goal, tracker, paper,
peer-review document, register, generated evidence report, probe, and relevant
Lean source file. Cross-check duplicated statements against source and PDF
evidence, keep the narrower claim where evidence conflicts, and preserve the
older wording in audit history.

No deletion is permitted. Only confirmed redundant or superseded material may
be moved to a local archive outside the commit set, with an archive manifest
recording old path, new path, reason, and SHA-256. Commit coherent verified
tranches, stage only files belonging to that tranche, and do not push without
explicit user instruction.

## MAP-59: priority 135 external moment-realisation junctions (2026-09-28)

Evidence:

- `NavierStokesReview/src/audit/priority_135_external_moment_realization_junction_source_review_2026-09-28.md`
- `NavierStokesReview/evidence/source_tranche_external_moment_realization_junction_2026-09-28.json`

This twelve-file tranche records exact reduced-profile moment repair and
restoration in `ModulatedProfileJetRates`, local quadratic correction and
moment-matrix algebra, three-component local rank/debt/remainder bounds,
periodic pressure/primitive continuation, smooth divergence-free Cartesian
realisation, local heat pressure tails, and all-order residual-flatness
results. These are positive intermediate results. They correct any blanket
statement that the five-moment system or Cartesian construction is absent.

The inspected declarations still do not provide the final value-level theorem
connecting the selected global Cartesian field to
\[
\operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p).
\]
The absence claim is bounded to this tranche; it is not a repository-wide
impossibility theorem. CTR-005 therefore remains **not established at the
selected-field boundary**. No nonzero \(\Delta m\), impossibility theorem, or
kernel-level `False` was derived.

The current register is **2,792 indexed**, **588 captured endpoint-closure**,
**745 evidence-inspected**, **2,040 queued**, **0 missing project import
edges**, **10 source rows containing a `sorry` token**, and **40 supplemental
evidence records**.

## Priority 134: comparator admissions and Euler foundation

Evidence:

- `NavierStokesReview/src/audit/priority_134_comparator_eulerproof_source_review_2026-09-28.md`
- `NavierStokesReview/evidence/source_tranche_comparator_eulerproof_2026-09-28.json`

The two standalone `ComparatorChallenges` files contain four intentional
admitted theorem bodies at the recorded source anchors. Their headers state
that they are standalone references and are not imported by the proof root;
the active endpoint contamination question therefore remains an import-closure
question, not an inference from file presence. `Euler/EulerProof.lean` is a
20,755-line, 91-import, 1,202-declaration file with no admitted-token match in
the audited lexical gate. Its reviewed results are real conditional analytic,
Sobolev, pressure, packet, scale, and ODE infrastructure, but this tranche
does not prove a final Euler CMI endpoint or selected Navier--Stokes
five-observable transport.

The register after regeneration is **2,792 indexed**, **588 captured
endpoint-closure**, **734 evidence-inspected**, **2,051 queued**, **0 missing
project import edges**, **10 source rows containing a `sorry` token**, and **38
supplemental evidence records**. This tranche causes no verdict escalation.
