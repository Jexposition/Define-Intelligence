# CMI-first review map: OpenAI Navier–Stokes claim

**Working verdict:** `NOT ESTABLISHED AS A CMI SOLUTION` until the selected endpoint is independently checked. This document is a compact work plan, not the research log. Evidence belongs under `NavierStokesReview/evidence/`; completed arguments belong in the peer review and paper.

## Status key

`[x]` checked and closed as an attack route  ·  `[~]` active review  ·  `[ ]` not yet checked  ·  `[!]` formal failure found

## Base-profile verification board: 2026-09-23

| ID | Question | Status | Evidence / next action |
|---|---|---|---|
| BP-01 | Does `finalPotential` define a genuinely three-component field? | [x] | Reduced `(t, s, z)` profile is embedded in three Cartesian components and spatially curled. |
| BP-02 | Is the base field globally swirl-free? | CORRECTED | Only the radial gauge anchor is zero; no global angular-component-zero theorem was found. |
| BP-03 | Are the paper's five moments transported into the selected endpoint? | [~] | Upstream five-moment machinery exists, but no selected-path transport theorem was found through the generic germ/sum interface. |
| BP-04 | Is smooth forcing derived or injected? | [~] | `force_smooth` consumes residual-jet limits and away extensions; verify those premises for the selected fields. |
| BP-05 | Is `WholeDomain*` dead code? | CORRECTED | Unreachable from `selected_witness`, but reachable through paper-result modules. |
| BP-06 | Has a zero-sorry contradiction been obtained? | [ ] | None yet. Do not label the claim refuted without a selected-path contradiction. |
| BP-07 | Are the local paper fields, selected raw stages, force, and exported R³ candidate identified as one object? | [~] | Local velocity/pressure agreement is present, but force and five-moment transport are not exposed in one theorem. |
| BP-08 | Were prior probes themselves checked for overclaiming? | [x] | The isolation probe was corrected; “PositiveOrderMoments is dead code” is withdrawn. |
| BP-09 | Does compact pressure support force the selected velocity to vanish? | [x] | Rejected as a standalone counterexample; the comparison path derives pressure flux from the residual equation. |
| BP-10 | Is the pressure/rate premise merely injected at the final comparison theorem? | [x] | Rejected for the inspected endpoint; `PressureFlux` and `ComparisonRateBound` construct the constants internally. |

Evidence: `NavierStokesReview/evidence/base_profile_core_asymptotics_audit_2026-09-23.md` and `NavierStokesReview/src/probes/BaseProfileCoreAsymptoticsProbe.lean`.

## 1. Target and admissibility gate

| ID | Question | Status | Evidence / next action |
|---|---|---:|---|
| CMI-01 | Which Fefferman alternative is claimed? | [x] | R³ forced breakdown, matching the repository `CandidateProperties` shape. |
| CMI-02 | Is the force globally smooth, rapidly decaying in time, and supported at positive time? | [~] | `ProblemStatement.lean`, `CandidateFromLimits.lean`; verify selected endpoint predicates. |
| CMI-03 | Is the velocity smooth before the singular time and finite-energy as required? | [~] | Trace `CandidateConsequences` to the selected velocity; audit exact norm statements. |
| CMI-04 | Does the code prove the PDE on the required domain, rather than only define a residual? | [~] | Match `navierStokesResidual = forcing` against the selected candidate fields. |

CMI does not impose the additional conditions `∫ f dx = 0` or `∇ · f = 0` on the external force. Those are possible physical diagnostics, not automatic CMI disproofs. A conservation-law attack becomes decisive only after deriving the relevant identity from the stated hypotheses and showing that the selected force violates it.

## Composition audit added 2026-09-24

The next falsification target is explicit: prove or disprove a selected-path
transport theorem carrying the paper's `(M, I, J, S, C_p)` data and the same
force from `LocalPaperTheorem` through `PaperLocalization` into
`ActualCandidateAssembly.selected_candidate`. The current source establishes
local velocity/pressure agreement, not this complete identity.

## 5D target and origin contradiction lane: 2026-09-24

| ID | Task | Status | Decisive test / evidence |
|---|---|---:|---|
| 5D-01 | Extract the five physical row definitions. | [x] | `PositiveOrderMoments.rowDensity`, `moments`, `weightedDensity`, and `FiveProfileMoments.physicalMoments`; evidence `physical_transport_bridge_spec_extraction_2026-09-24.md`. |
| 5D-02 | Extract the runtime three-debt update and fixed rows. | [x] | `FiveRowRank.Debt := Fin 3 → ℝ`; `FiveRows` has two zero rows and three `(P,Jθ,Jz)` rows; `MeanRankUpdate.scaleDebt` transports the three rows. |
| 5D-03 | State the required promotion. | [x] | `promoteDebt d := ![0,0,-(d 0),-(d 1),-(d 2)]`; the zero-sorry probe proves only the algebraic repair equality. |
| 5D-04 | Prove promotion is the selected physical five-moment identity. | [ ] | Required theorem must mention selected stage fields, their integrals, and the selected residual/force. None is exhibited. |
| ORG-01 | Check whether `StateRealization.chartIdentity` reaches the singular origin. | [x] | Zero-sorry probe proves its domain and `graphSourceTZ` exclude radius zero. Evidence `state_realization_axis_scope_audit_2026-09-24.md`. |
| ORG-02 | Connect `GlobalBaseError.originPast` to actual selected fields. | [x] | The selected schedule has a zero-sorry raw-residual limit, and `SelectedForceOriginCompositionProbe.lean` identifies the final force with that residual at the origin. |
| ORG-03 | Derive `False` from selected residual limits and origin blow-up. | [~] | The selected speed diverges while the selected force tends to zero. This refutes any positive velocity-to-residual lower bound, but no such premise is required by the endpoint. Seek a different false selected premise. |

## 2. Selected endpoint trace

| ID | Task | Status | Required result |
|---|---|---:|---|
| END-01 | Trace `selected_witness` into `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`. | [x] | Selected witness consumes actual stage estimates, endpoint extensions, and axis conditions. |
| END-02 | Check whether residual rate bounds are inserted or derived. | [x] | `ActualCycleResidualBounds.native_residual` derives the full residual bound from component estimates. |
| END-03 | Check whether `VanishingJointJets` and `AwayExtensions` are derived on the selected path. | [x] | `StageEstimates.exists_schedule` and `MixedDiagonalResidual.physical_vanishingJointJets` derive the limits; `selected_witness` consumes them. Evidence `selected_residual_endpoint_trace_2026-09-24.md`. |
| END-04 | Run `#print axioms` on the exported R³ endpoint and selected witness. | [x] | Current reports show only `propext`, `Classical.choice`, and `Quot.sound`. |
| END-05 | Audit `selectedBudget = 0` and selected stage aliases. | [x] | Zero is an input parameter; stage families remain indexed by `ℕ`; no `sorry` found. |

## 3. Force and endpoint regularity

| ID | Task | Status | Escalation test |
|---|---|---:|---|
| FORCE-01 | Inspect `PositiveTimeForce.timeCutoff`. | [x] | Smooth bump; active on `[3/8,1]`; no step discontinuity. |
| FORCE-02 | Locate pressure in the force residual. | [x] | Pressure enters `navierStokesResidual` in `CandidateFromLimits`; `PositiveTimeForce.force` is only a wrapper. |
| FORCE-03 | Check residual provenance. | [x] | Before `t=1`, `CandidateFromLimits.force` equals the activated residual; endpoint uses smooth extension. |
| FORCE-04 | Prove or refute selected residual endpoint limits. | [x] | `SelectedWitnessEndpointResidualProbe.lean` proves the selected raw mixed residual tends to zero at the origin, and `SelectedForceOriginCompositionProbe.lean` transports that limit to the final force. |
| FORCE-05 | Prove force-norm divergence, failed support, failed decay, or failed `ContDiff`. | [x] | `SelectedForceOriginCompositionProbe.lean` proves the final selected force also tends to zero at the origin. The force-explosion route is closed. |
| FORCE-06 | Test the selected origin velocity-to-residual lower bound. | [x] | Zero-sorry selected-path probe proves origin speed tends to infinity while the selected raw residual tends to zero; every fixed positive lower bound is impossible. |

## 4. Moment and physical-correspondence lane

| ID | Task | Status | Required result |
|---|---|---:|---|
| MOM-01 | Inspect `FiveRowRank.FiveRows`. | [x] | Five explicit radial integral rows; first two are proved zero rows, not type axioms. |
| MOM-02 | Inspect `PositiveOrderMoments`. | [x] | Genuine five-coordinate integral repair exists. |
| MOM-03 | Find the transport theorem from `(M,I,J,S,C_p)` to selected physical debt. | [~] | No selected-endpoint theorem exhibited yet; search import closure and theorem applications. |
| MOM-04 | Test whether selected fields can satisfy endpoint claims without that transport. | [~] | Construct a zero-sorry countermodel or locate the missing mandatory premise. |
| MOM-05 | Do not infer a CMI failure from non-Newtonian regularisations. | [x] | Such models are external stability tests, not the classical forced equation. |

## 4a. Incompressibility lane

| ID | Task | Status | Finding |
|---|---|---:|---|
| DIV-01 | Distinguish raw potential stages from the final velocity. | [x] | `selectedPotentialStages` are intermediate potentials, not the field in `CandidateProperties`. |
| DIV-02 | Trace the final velocity divergence theorem. | [x] | `SolenoidalDiagonal.divergence_velocitySum_on` proves the curl-generated velocity is divergence-free under its hypotheses. |
| DIV-03 | Extract the selected endpoint property without `sorry`. | [x] | `SelectedDivergenceAudit.lean` compiles and returns `hc.divergence_free`. |
| DIV-04 | Find a false divergence premise on the selected path. | [ ] | No such failure found; keep endpoint residual and moment audits active. |

## 4b. Energy, pressure, and temporal-gluing lane

| ID | Task | Status | Finding / escalation test |
|---|---|---:|---|
| ENG-01 | Locate the exact Newtonian energy identity. | [x] | `R3/ViscousEnergyBalance.lean` proves forcing work minus viscous dissipation. |
| ENG-02 | Check the selected endpoint exposes finite energy. | [x] | `AnalyticObjectionsProbe.lean` extracts `hc.energy_bounded`. |
| ENG-03 | Prove a selected-field energy mismatch. | [ ] | Requires an exact contradiction, not a scaling suspicion. |
| PRS-01 | Check whether pressure is compactly supported in the selected R³ candidate. | [x] | `CandidateProperties.pressure_support` and `R3CompactCandidate.pressure_supported` make this explicit. |
| PRS-02 | Derive a pressure-tail contradiction from the actual force. | [ ] | Only valid after proving the extra force-divergence or independence premise needed for a force-free Poisson argument. |
| GLU-01 | Trace temporal gluing and endpoint jets. | [x] | `VanishingJointJets` is all-orders; `timeSwitch` is globally smooth and late-time local equality preserves all local jets. The selected residual-limit inputs are source-linked through the actual stage estimates. |

## 4d. Advanced structural lanes

| ID | Task | Status | Decisive evidence |
|---|---|---:|---|
| ADV-01 | Energy-dissipation mismatch | [~] | The exact forced energy identity is present. Instantiate it on the selected fields; do not infer a mismatch from the five-row architecture alone. |
| ADV-02 | Temporal stage-interface regularity | [~] | Smooth gluing and endpoint jets are present. Trace the concrete `hlim`, `L`, and `VanishingJointJets` premises into `selected_witness`. |
| ADV-03 | Pressure support versus whole-space recovery | [~] | Compact pressure support is explicit, while compact-test Poisson/recovery theorems also exist. Determine whether the selected construction invokes the recovery bridge or leaves it unconnected. |

## 4e. Current counter-paper deep dive: transport and pressure

| ID | Bounded action | Status | Acceptance test |
|---|---|---:|---|
| TRN-01 | Record the production debt type and exact five-row equations. | [x] | `FiveRowRank.Debt = Fin 3 → ℝ`; first two rows are explicit zero constraints; last three consume all debt coordinates. |
| TRN-02 | Record the independent positive-order five-moment system. | [x] | `PositiveOrderMoments.Debt = Fin 5 → ℝ`; exact weighted moment theorem compiles. |
| TRN-03 | Verify the explicit promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)`. | [x] | `FiveRowPositiveOrderBridgeProbe.lean` compiles with no `sorry`. |
| TRN-04 | Trace promotion into `StateRealization.chartIdentity`. | [~] | Search for a theorem that identifies paper moments with promoted debt and is consumed by `StateRealization`; current source shows local residual/germ inputs only. |
| TRN-05 | Trace promotion into `CandidateConsequences` and `selected_witness`. | [~] | Public consequence bundle contains no moment-realisation field; prove a selected-path contradiction only if an actual mandatory premise fails. |
| TRN-06 | Extract the exact five-row target specification and runtime update laws. | [x] | `physical_transport_bridge_spec_extraction_2026-09-24.md` records the raw row densities, repair theorems, `scaleDebt`, `next_mean`, and `next_preserve_masses`. |
| TRN-07 | Do not invent a recursive stability theorem in `PositiveOrderMoments`. | [x] | The file proves one exact repair step; recursive cycle induction is elsewhere. The selected-path transport theorem remains absent from the inspected declarations. |
| TRN-08 | Separate the extracted 5D target from the selected residual proof. | [x] | `physical_transport_bridge_spec_extraction_2026-09-24.md` records the target and runtime laws; it is an audit specification, not a theorem supplied by the authors. |
| TRN-09 | Check whether `StateRealization.chartIdentity` reaches the singular origin. | [x] | Zero-sorry probe proves its domain and `graphSourceTZ` are strictly positive-radius; no origin transport theorem is present in the inspected chain. |
| PRS-03 | Keep R³ and periodic-lift domains separate. | [x] | R³ `CandidateProperties` uses Euclidean compact support; periodic endpoint uses lifted periodicity. Do not transfer torus support arguments to R³. |
| PRS-04 | Print the exact meaning of `pressure_support`. | [x] | It is `tsupport(slice p) ⊆ K` with `IsCompact K`, not a pressure-Poisson axiom. |
| PRS-05 | Trace `PressureRecovery` and `ActualPressureFlux`. | [x] | `candidate_unique_on_Icc` supplies the selected candidate; `classical_uniqueness_on_Icc` constructs the recovery hypotheses and pressure-flux bound. |
| PRS-06 | Test the compact-pressure trivialisation inference. | [x] | Zero-sorry probe proves compact support does not imply a scalar slice is zero. |
| PRS-07 | Test whether comparison recovery verifies absolute selected pressure semantics. | [x] | `PressureRecoveryAbsolutePremiseProbe.lean` compiles: identical zero velocities and any common smooth pressure satisfy the comparison record. This exposes a limitation of the comparison interface, not yet a selected-endpoint contradiction. |
| PRS-08 | Seek a genuine selected-path pressure contradiction. | [~] | Must connect the selected `pressure_germ`/`base_equation` to an absolute global Poisson or normalisation theorem, then contradict the selected pressure if possible. |
| PRS-09 | Do not treat the comparison probe as a selected-field refutation. | [x] | The probe proves an interface limitation only. A formal disproof still requires a false selected premise or a contradiction with the selected residual limits. |
| PRS-10 | Connect pressure-germ/base-equation premises to origin limits. | [~] | `StateRealization` is off-axis; `GlobalBaseError.originPast` supplies a separate error-limit route. A full selected pressure/residual identity at the origin remains unproved. |

| GLU-02 | Check whether activation or spatial localisation drops residual terms or debt constraints. | [x] | The localisation theorems preserve the complete residual by neighbourhood equality; they have no debt-vector parameter and supply no five-moment transport theorem. |

Evidence for this block:
`NavierStokesReview/evidence/semantic_transport_pressure_audit_2026-09-23.md`,
`NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean`.

### Advanced-lane rule

These lanes may produce a formal disproof only through a zero-sorry theorem on the selected dependency path. A generic theorem about another pair of fields, an arbitrary pressure-tail intuition, or a physical regularisation outside the stated forced equation is not enough.

## 5. Formal-disproof threshold

Escalate from “correspondence defect” to **formal disproof** only when a zero-sorry Lean artefact proves one of these on the selected dependency path:

1. a required premise is false or inconsistent;
2. the selected force cannot satisfy global smoothness, positive-time support, or rapid derivative decay;
3. the selected velocity/pressure pair fails the stated Navier–Stokes equation or finite-energy predicate;
4. a claimed paper-to-code identity is contradicted for the actual selected fields.

Do not use `sorry`, an arbitrary existential witness, a generic countermodel disconnected from `selected_witness`, or the mere presence of a residual-defined force as a disproof.

## 6. Current work queue

| Priority | Next bounded action | Output |
|---:|---|---|
| 1 | Search for the five-moment transport theorem on the selected import closure. | Theorem citation or exact absence report; use the extracted 5D target as the acceptance specification. |
| 2 | Connect selected pressure-germ/base-equation premises to the final residual and origin limit. | A selected-field theorem, or a zero-sorry contradiction if the premises are incompatible. |
| 3 | Test the strongest actual selected obligation in Lean without `sorry`. | Seek a contradiction between selected moment/pressure semantics and the endpoint, not a generic countermodel. |
| 4 | Update tracker, axiom ledger, synthesis, peer review, and paper. | Human-readable counter-paper prose, not a chronological audit log. |

## External literature lane

| ID | Result | Status | Interpretation |
|---|---|---:|---|
| EXT-01 | Constantin–Ignatova–Vicol, arXiv:2609.20803 | [x] | Analytic forcing plus the reported anisotropic bounds and exact axisymmetric core implies regularity. |
| EXT-02 | Their corollary under bounded `C²` force | [x] | The force cannot both be analytic or vanish near the singular point; this is compatible with a compactly supported smooth nonanalytic force. |
| EXT-03 | Scientific American report | [x] | Independent expert criticism supports “contrived forced branch”, but reporting is not a formal contradiction. |
| EXT-04 | Convert external theorem into a Lean failure | [ ] | Only possible if the repository claims analyticity or a forbidden force property. Current source does not. |

References: [CMI problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf), [Scientific American analysis](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/), [Constantin–Ignatova–Vicol](https://arxiv.org/html/2609.20803v1).

## Evidence index

- `NavierStokesReview/evidence/force_cutoff_activity_audit_2026-09-23.md`
- `NavierStokesReview/evidence/selected_witness_endpoint_residual_probe_2026-09-24.md`
- `NavierStokesReview/evidence/selected_moment_bridge_audit_2026-09-23.md`
- `NavierStokesReview/evidence/force_conservation_obstruction_adjudication_2026-09-23.md`
- `NavierStokesReview/evidence/selected_divergence_audit_2026-09-23.md`
- `NavierStokesReview/src/probes/ForceActivityProbe.lean`
- `NavierStokesReview/src/probes/SelectedMomentBridgeAudit.lean`
- `NavierStokesReview/src/probes/SelectedDivergenceAudit.lean`
- `NavierStokesReview/src/probes/AnalyticObjectionsProbe.lean`
- `NavierStokesReview/results/pressure_support_scan_2026-09-23.txt`
- `NavierStokesReview/src/probes/PressureRecoveryInfrastructureProbe.lean`
- `NavierStokesReview/results/pressure_recovery_infrastructure_probe_2026-09-23.txt`
- `NavierStokesReview/evidence/semantic_transport_pressure_audit_2026-09-23.md`
- `NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean`
- `NavierStokesReview/results/semantic_transport_pressure_probe_2026-09-23.txt`
- `NavierStokesReview/evidence/pressure_recovery_selected_instantiation_2026-09-23.md`

**Last updated:** 2026-09-24
**Owner:** CMI-first formal review

## Current live-chain correction

| ID | Status | Acceptance test |
|---|---:|---|
| 5D-08 | [x] | `SelectedBaseMomentCompatibilityProbe.lean` confirms the live upstream five-moment identity, conservative flux consequences, final finite residual identity, and base origin blow-up. |
| 5D-09 | [ ] | Locate a theorem transporting that base invariant into the final mixed fields consumed by `selected_witness`, or derive a contradiction from the actual endpoint premises. |
| FJ-07 | [~] | The five-moment chain is live upstream; selected-mixed-sum transport into residual, pressure, force, and `VanishingJointJets` remains unresolved. |
## 4c. Analytic-objection adjudication

| Lane | Status | Working conclusion | Next decisive test |
|---|---:|---|---|
| Final incompressibility | [x] | The selected final velocity is divergence-free; raw potential stages are not the endpoint field. | Find a false premise in the selected divergence theorem. |
| Energy balance | [x] | An exact forced Newtonian energy identity and a finite-energy endpoint theorem are present. | Instantiate the identity on the selected fields and compare every hypothesis. |
| Pressure localisation | [~] | Compact pressure support is explicit in the selected construction. It is a serious PDE/paper correspondence question, not by itself a CMI contradiction under arbitrary forcing. | Find a proved pressure Poisson/Leray relation that conflicts with the compact support claim. |
| Temporal gluing | [~] | Smooth extension and endpoint-jet interfaces are explicit. The load-bearing issue is whether the residual-limit inputs are actually derived for the selected fields. | Trace `hlim`, `L`, and `VanishingJointJets` to their concrete premises. |
| Filter non-vacuity | [x] | The generic `JetRate` definition omits a `NeBot` parameter, but the selected endpoint filter has an explicit `past_filter_neBot` theorem and a zero-sorry probe. | Audit any later restriction/comap filters individually. |

Evidence: `NavierStokesReview/evidence/analytic_objections_adjudication_2026-09-23.md`.

## Document control

This fork is the active review corpus. See
[`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md) before using any
parent-directory copy or supporting diagnostic note. A claim enters this plan only
after source inspection or a recorded zero-sorry probe.

| ID | Control task | Status | Decisive condition |
|---|---|---:|---|
| DOC-01 | Quarantine stale parent verdicts and unsupported pure-axial claims | [x] | The control map identifies active, supporting, archival, and rejected notes. |
| DOC-02 | Reconcile supporting notes with current source paths | [x] | `finalPotential`, selected imports, force gluing, and pressure support are corrected in the active corpus. |
| DOC-03 | Maintain one human-readable peer review and one research paper | [x] | Narrative documents point to tracker/evidence rather than functioning as logs. |
| DOC-04 | Resolve the selected five-moment transport objection | [ ] | Find or refute the theorem transporting the named moments through the selected endpoint. |
| DOC-05 | Verify final authority-map packaging | [x] | Control map, tracker, six core documents, and supporting-note dispositions agree; no tracked build artefacts. |

## New formal countermodel

| ID | Target | Status | Result |
|---|---|---:|---|
| CTR-037 | `MixedCandidateAssembly.StageEstimates` physical content | [x] | Zero-sorry probe constructs the interface with zero velocity/pressure stages and proves zero velocity is not blow-up. |
| CTR-038 | Selected-path five-moment transport | [ ] | The generic interface failure does not yet refute the additional selected physical-data and origin-growth premises. |

Evidence: `NavierStokesReview/evidence/stage_estimates_moment_blindness_2026-09-24.md`.

## Current proof board: 2026-09-24

| ID | Target | Status | Decisive evidence |
|---|---|---:|---|
| CTR-037 | Generic `StageEstimates` encodes physical blow-up | [x] | Zero-sorry zero-field countermodel; interface is insufficient. |
| CTR-038 | Selected five-moment transport into residual endpoint | [ ] | Locate a theorem linking `(M,I,J,S,C_p)` to selected fields, `chartIdentity`, and `VanishingJointJets`, or prove a contradiction from its premises. |
| CTR-039 | Generic stage interface determines the paper's five-debt payload | [x] | `interface_does_not_determine_five_debt` is a zero-sorry countertheorem: `StageEstimates` alone cannot determine an arbitrary `PositiveOrderMoments.Debt`. This is an interface obstruction, not yet a selected-witness refutation. |
| PRS-08 | Compact pressure support forces trivialisation | [~] | No contradiction has been proved. Add the global Poisson/Leray premises and test the selected pressure and velocity, rather than treating compact support alone as decisive. |
| PRS-09 | Selected pressure has the paper's global semantics | [~] | The comparison interface has no absolute pressure-Poisson premise; selected local `pressure_germ` and `base_equation` still need to be connected to a global pressure theorem. |
| PRS-10 | Pressure comparison chain was over-cleared | [x] | Corrected: the chain is real for differences and flux bounds, but cannot be cited as an absolute selected-pressure verification. |
| CTR-012 | Residual-designed force versus given external datum | [x]/[~] | Official-source check confirms a real causal/paper correspondence objection, but no separate formal independence predicate was found in the C/D statement. |

Evidence: `NavierStokesReview/evidence/pressure_recovery_chain_audit_2026-09-24.md`,
`NavierStokesReview/evidence/physical_transport_bridge_spec_extraction_2026-09-24.md`,
and `NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean`.

## 5D target and contradiction lane

| ID | Task | Status | Acceptance test |
|---|---|---:|---|
| 5D-01 | Extract literal `PositiveOrderMoments` rows, integrals, and repair lemmas | [x] | `physical_transport_bridge_spec_extraction_2026-09-24.md` records `rowDensity`, `positiveIntegral`, `moments`, `moments_repair`, and `exists_smooth_exact_repair`. |
| 5D-02 | Extract the runtime three-debt update and five-row promotion | [x] | Record `FiveRowRank.Debt`, `scaleDebt`, `FiveRows`, and the existing promotion `(0,0,-P,-Jθ,-Jz)` with source anchors. |
| 5D-03 | Prove generic interface non-determination | [x] | `StageEstimatesMomentBlindnessProbe.interface_does_not_determine_five_debt` compiles without `sorry`. |
| 5D-04 | Transport the five moments into the selected endpoint | [~] | The new attack-boundary probe confirms the `Witness` type does not entail a five-debt certificate; a field-level transport or violation theorem is still required. |
| 5D-05 | Derive contradiction from selected residual limits and origin blow-up | [~] | The scalar endpoint predicates are compatible. A zero-sorry `False` now requires a selected-field PDE lower bound or an incompatible pressure/moment identity. |
| 5D-06 | Inhabit the selected witness with an unconstrained five-debt payload | [x] | `SelectedWitnessInhabitationProbe.lean` compiles without `sorry`: the `Witness` envelope contains no `PositiveOrderMoments.Debt` field or equality. |
| 5D-07 | Derive an actual selected-field five-moment violation | [ ] | Add field-level moments to the selected path and prove their failure or contradiction with the selected residual and pressure premises. |
| FJ-01 | Force-jet breakdown at the singular interface | [x]/[~] | The selected raw residual and final force are composed at the origin and tend to zero; the explosion route is closed. A contradiction still requires a separate selected PDE lower bound. |
| FJ-02 | Pressure-Poisson/support contradiction | [~] | The R3 candidate record has compact pressure support but no explicit global pressure-Poisson field. Add the missing identity and test the selected fields. |
| FJ-04 | Selected-path transport closure | [~] | Trace `ActualCandidateAssembly.Witness` through `R3ActualCandidate.selected_compact_candidate`, `R3/ActualCandidate.of_localized_fields`, and `R3/Theorem`; prove whether any five-moment equality is consumed. |
| FJ-05 | Selected origin residual contradiction | [x]/[~] | The selected force composition proves the origin force tends to zero. A generic residual-flatness incompatibility remains insufficient without a selected PDE lower bound. |
| FJ-08 | Exact residual lower-bound obstruction | [x]/[~] | The zero-sorry probe proves that `c * ‖u‖ ≤ ‖residual‖` with `c > 0` would contradict the selected flat residual and origin blow-up. The companion scalar countermodel proves that blow-up alone does not supply this bound. |
| FJ-06 | Selected pressure semantics | [~] | Add a selected-field global Poisson/Leray premise and test it against compact pressure localisation; compact support alone is not the contradiction. |
| PRS-11 | Pressure absolute-semantics check | [~] | The absolute selected-field Poisson/Leray bridge remains open. The equal-and-opposite cancellation proposal is ruled out by the compiled residual perturbation identity. |

## Direct selected-witness attacks: 2026-09-24

| ID | Attack | Status | Required zero-sorry result |
|---|---|---:|---|
| SW-01 | Force-jet breakdown | [~] | Derive a positive lower bound from the selected velocity to its residual, then apply `SelectedResidualLowerBoundObstructionProbe`. |
| SW-02 | Pressure-Poisson/support mismatch | [~] | Derive the global selected pressure-Poisson/Leray identity and contradict compact support or endpoint limits. |
| SW-03 | Moment-blind ghost model | [x]/[~] | The witness envelope has no five-debt field; still derive an actual moment violation for the selected sums. |
| SW-04 | Selected-witness contradiction | [ ] | Close one of SW-01 to SW-03 with `False` from the actual selected witness. |
| SW-05 | Mirror-force symmetry | [x]/[~] | Negation preserves force smoothness, but the mirror force is a different existential input. The same fields satisfy both equations only when `f = -f` pointwise. |

Evidence: `NavierStokesReview/evidence/selected_witness_boundary_attack_status_2026-09-24.md`.

## Attack-boundary result

`SelectedWitnessAttackBoundaryProbe.lean` compiles without `sorry`. It proves
that the exported `Witness` proposition does not entail zero for every
five-coordinate debt and that an unbounded scalar endpoint can coexist with a
flat scalar residual. This prevents an invalid automatic `False` inference.

The selected force composition and all-order jet trace now close the force-
explosion route, while CTR-005 and the absolute pressure bridge remain open.
The mirror-force probe records the corresponding symmetry boundary: a smooth
field `-f` exists, but it is not a counterexample to an existential claim about
`f` and it does not reverse the nonlinear solution path.

## CTR-012 independent-data and mirror lane

| ID | Status | Decisive result |
|---|---:|---|
| CTR-012-A | [x] | Fixed-force perturbation identity compiles with no admitted declarations. |
| CTR-012-B | [x] | The obstruction is packaged for `PositiveTimeForce.force`. |
| CTR-012-A2 | [x] | The explicit affine-time perturbation is globally smooth, spatially divergence-free, and has nonzero defect `a` for `a ≠ 0`. |
| CTR-012-C | [x] | Mirror smoothness, work sign reversal, and `f + (-f) = 0` compile. |
| CTR-012-D | [ ] | A selected-path admissible perturbation or force-superposition contradiction remains to be proved. |

The current lane establishes that residual-designed forcing is path-dependent:
holding the force fixed after changing the velocity imposes the full homogeneous
perturbation PDE. The explicit affine-time test field gives a nonzero defect
under this fixed datum. It does not establish that the selected existential witness
must be stable under that perturbation, nor that the nonlinear schedule reverses
under (f\mapsto-f). Those stronger conclusions require additional premises.

Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`;
`NavierStokesReview/evidence/mirror_force_symmetry_2026-09-24.md`.
