# CMI-first review map: OpenAI Navier–Stokes claim

**Working verdict:** `NOT ESTABLISHED AS A CMI SOLUTION` until the selected endpoint is independently checked. This document is a compact work plan, not the research log. Evidence belongs under `NavierStokesReview/evidence/`; completed arguments belong in the peer review and paper.

## Burden-of-proof gate

The authors must establish the claim they publish. The review need not derive
the negation of the literal existential endpoint before withholding acceptance
of the published paper and its CMI solution claim. Track these as separate outcomes:

| Claim level | Required evidence | Current status |
|---|---|---|
| Lean endpoint | The exported proposition is kernel-checked. | Partly confirmed on the inspected path. |
| Selected construction | The same selected fields satisfy every analytic and PDE premise consumed by the endpoint. | The complete field-level composition remains to be exhibited. |
| Published paper | The selected fields are the advertised five-moment construction. | **Not established; CTR-005 remains open.** |
| CMI solution | The paper construction matches a Fefferman alternative with all required hypotheses. | **Not established.** |

`NOT FORMALLY REFUTED` is only the status of the current Lean contradiction
search. It is not affirmative evidence that an unproved bridge is valid.
Evidence: `NavierStokesReview/evidence/burden_of_proof_underclaim_audit_2026-09-24.md`.

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
| 5D-05 | Test whether the two zero correction rows collide with a nonzero perturbation or selected witness. | [x] | `FiveRowCollisionBoundaryProbe.lean` compiles: `FiveRowRank.five_rows` admits nonzero `Fin 3 → ℝ` debt, while `Witness` contains no rank debt or perturbation field. No `False` follows by type collision. |
| 5D-06 | Prove the strongest conditional contradiction from the zero rows. | [x] | `CorrectionInvariantScope.lean` compiles without `sorry`, `axiom`, or `unsafe`: a nonzero `barMoment 2` angular correction or `barMoment 1` axial correction contradicts `FiveRows`. The missing step is transporting the selected perturbation into that correction increment. |
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
| MOM-06 | Keep the correction-state invariants distinct from selected-field energy. | [x] | `fiveRows_preserve_masses` preserves two radial correction moments; no theorem equates them with selected Cartesian mass or kinetic energy. |

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

## CTR-016 global germ-transport audit: recheck status

| Check | Status | Result |
|---|---:|---|
| Local cycle invariants reach the mean-atlas input | [x] | `state_runInvariant`, `state_particularData`, `state_waveData`, and `state_wave_transport` feed `mean_input_of_transport`. |
| Native stages have actual chart/exterior transport | [x] | Stage definitions, prefix identities, and chart equalities are source-linked in `ActualCandidateConstruction` and `ActualCandidateAssembly`. |
| `physicalData`, `estimates`, and `endpoints` consume actual selected data | [x] | `ActualCandidateAssembly.lean:1079-1115`. |
| Exported `Witness` identifies the selected fields with the paper's five moments | [ ] | No equality to `PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`, `FiveRowRank.FiveRows`, or `(M,I,J,S,C_p)` is exported. |
| Global consequences imply fixed-force same-datum stability | [x] | `GlobalTransportBridgeProbe.lean` proves the selected consequences coexist with failure of the review-side stability predicate. |
| Selected-path `False` | [ ] | Not obtained. The remaining target is a concrete false field-level moment or pressure identity, not a generic interface objection. |

### Fixed-data perturbation closure

| Check | Status | Result |
|---|---:|---|
| Exact residual perturbation identity | [x] | `IndependentDataPerturbationProbe.lean` compiles without `sorry`. |
| Smooth divergence-free localised test field | [x] | `CompactFixedForcePerturbation.lean` constructs a compact spatial curl perturbation. |
| Nonzero switch-time defect | [x] | The defect at the origin is `coordinateVector 0 ≠ 0`. |
| Contradiction with same fixed force | [x] | Base and perturbed fields cannot satisfy the same residual equation under the stated local hypotheses. |
| Contradiction to literal C/D existential endpoint | [~] | Not established: the endpoint does not currently quantify over perturbations. |

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
| BURDEN-01 | Separate non-establishment from formal refutation | [x] | The authors' missing selected-field composition is an affirmative reason not to accept the published CMI claim; a separate zero-sorry `False` theorem is required only for the narrower label `FORMALLY REFUTED`. |
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

## Closure correction: 2026-09-24

| Check | Status | Result |
|---|---:|---|
| Selected import closure | [x] | 507 reachable modules from `ActualCandidateAssembly`; five-moment and rank modules are present upstream. |
| Dead-code allegation | [x] | Withdrawn in its broad form. The active objection is missing selected-endpoint transport, not absent machinery. |
| Endpoint type boundary | [x] | `Witness` contains schedules, fields, force, consequences, jets, and decay, but no named five-moment equality. |
| Selected transport theorem | [~] | Search/construct a theorem identifying the actual mixed sums with `(M,I,J,S,C_p)` and carrying it into residual and force premises. |
| Formal contradiction | [~] | No selected-path `False` theorem yet. Keep the counter-paper verdict at “not established as claimed”. |

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Correction-row transport audit: 2026-09-24

| ID | Task | Status | Acceptance test |
|---|---|---:|---|
| 5D-10 | Prove the exact generic correction-moment invariant. | [x] | `CorrectionInvariantScope.rank_stage_preserves_designated_moments` compiles without admitted declarations. |
| 5D-11 | Transport a selected Cartesian perturbation into `rankIncrement`. | [ ] | A theorem must identify the perturbation with the actual correction field and prove a nonzero `barMoment 2` or `barMoment 1`. |
| 5D-12 | Infer kinetic-energy or full five-moment preservation from the zero rows. | [ ] | No such inference is licensed by the source; `FiveRows` contains radial correction moments, not an energy identity. |
| 5D-13 | Expose the actual selected-cycle local mass invariant. | [x] | `SelectedCycleMomentTransport.lean` compiles: `state_invariant.masses` gives `ZeroMassesOn` for every selected cycle stage. |
| 5D-14 | Transport that local invariant into the exported mixed `Witness`. | [ ] | The `Witness` type must expose the relevant equality and identify it with the paper's five named moments. |
| 5D-15 | Audit the runtime rank scaling and the scope of the two zero rows. | [x] | `MeanRankUpdateAudit.lean` compiles; `scaleDebt` is three-coordinate scaling and `FiveRows` zeroes correction moments, not kinetic energy. |

Evidence: `NavierStokesReview/evidence/correction_moment_transport_audit_2026-09-24.md` and
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`, with
`NavierStokesReview/evidence/mean_rank_update_scope_2026-09-24.md` for the
runtime rank audit.

## Temporal patching and source-context lane: 2026-09-24

| ID | Task | Status | Acceptance test |
|---|---|---:|---|
| CTR-017-01 | Map `initializedSeries`, finite prefixes, and successor stage families. | [x] | Exact source ledger distinguishes indexed stages from temporal intervals. |
| CTR-017-02 | Test for a selected temporal derivative jump. | [x] | Audit complete: the zero-sorry probe constructs an unequal raw indexed boundary, but no theorem identifies the index with time or derives a selected-field derivative mismatch. |
| CTR-017-03 | Verify time activation and late jet agreement. | [x] | `TemporalPatchingDiscontinuityProbe.lean` compiles; `timeSwitch` and late derivative theorems are source-linked. |
| SRC-01 | Reconcile Fefferman's “given external force” wording with C/D existential quantification. | [x] | `OpenAI_NavierStokes_Source_Context_Register.md` records both facts without converting provenance into an unsupported `False`. |
| SRC-02 | Compare the Euler parent-child time iteration with the Navier--Stokes indexed stage constructor. | [x] | The source register records that the comparison does not transfer a temporal-gluing theorem into the Navier--Stokes code. |
| SRC-03 | Keep the five-moment and pressure bridges linked to the final witness. | [ ] | Find a selected-field equality for `(M,I,J,S,C_p)` and the absolute pressure semantics, or prove a false mandatory premise. |

## Selected endpoint direct-source recheck: 2026-09-24

| Task | Status | Acceptance test |
|---|---:|---|
| Recheck actual cycle/rank consumption | [x] | `physicalData`, `RunData.rank_class`, `rank_rows_on_patch`, and `SelectedCycleMomentTransport` are source-linked and compile. |
| Recheck exported five-moment transport | [ ] | No equality from the selected mixed endpoint to `moments`, `physicalMoments`, `FiveRows`, or `(M,I,J,S,C_p)` was found. |
| Escalate CTR-005 to formal disproof | [ ] | Requires a false equality or other contradiction on the selected fields; an omitted export field is not enough. |

Evidence: `NavierStokesReview/evidence/selected_endpoint_direct_source_trace_2026-09-24.md`.

Evidence: `NavierStokesReview/evidence/temporal_patching_audit_2026-09-24.md` and
`docs/OpenAI_NavierStokes_Source_Context_Register.md`.

## Selected-witness fixed-force closure

| ID | Task | Status | Acceptance test |
|---|---|---:|---|
| CTR-012-E | Instantiate the compact fixed-force obstruction on the selected witness. | [x] | `selected_candidate_fixed_force_obstruction` compiles without admitted declarations. |
| CTR-012-F | Convert the selected-path obstruction into a CMI-level contradiction. | [ ] | Add a theorem using a premise actually required by the endpoint, such as force independence or a false selected identity. |

The current result proves path dependence of the selected residual construction,
not emptiness of the endpoint existential.

## Residual provenance closure

| ID | Task | Status | Acceptance test |
|---|---|---:|---|
| CTR-012-G | Extract residual provenance from the exported selected witness. | [x] | `SelectedResidualProvenance.selected_candidate_force_is_residual_output` compiles and proves `f = navierStokesResidual u p` on `0 < t < 1`. |
| CTR-012-H | Convert provenance into a literal C/D contradiction. | [ ] | Requires a force-independence/admissibility premise in the endpoint or a false selected predicate. |

The construction therefore has a proved causal/provenance mismatch with the
forward-data language of the official problem statement, but the literal
existential endpoint is not empty merely because its witness was manufactured
backwards.

## Current formal extension

| Task | Status | Acceptance test |
|---|---:|---|
| Define explicit fixed-force stability predicate | [x] | `FixedForceStable` quantifies over smooth, compactly supported, divergence-free perturbations. |
| Instantiate the selected compact perturbation | [x] | `selected_candidate_fails_fixed_force_stability` compiles with no admitted declarations. |
| Strengthen perturbation to preserve zero initial data | [x] | `selected_candidate_fails_fixed_force_same_datum_stability` compiles with no admitted declarations. |
| Promote this to literal C/D `False` | [ ] | Requires force independence or perturbation stability as an actual endpoint premise, or a false selected identity. |

Interpret the result as a formal provenance/stability objection. Do not write
that the existential C/D proposition has been refuted by this extension alone.

Evidence: `NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md` and
`NavierStokesReview/evidence/same_datum_fixed_force_obstruction_2026-09-24.md`.

## Selected rank transport re-audit: 2026-09-24

| Check | Result | Required follow-up |
|---|---|---|
| Runtime `FiveRows` is active | Confirmed | Keep the selected-cycle rank chain in scope. |
| First two rows freeze total energy | Rejected | Do not use this claim in the paper. |
| Internal radial correction invariant | Confirmed | Treat `ZeroMassesOn` as a local invariant only. |
| Transport into selected mixed endpoint | Unresolved | Identify the paper tuple `(M,I,J,S,C_p)` with the selected fields and residual, or prove a concrete violation. |

Evidence: `NavierStokesReview/evidence/selected_rank_transport_reaudit_2026-09-24.md`.

## Whole-space uniqueness-chain audit: 2026-09-24

| ID | Task | Status | Required follow-up |
|---|---|---:|---|
| UNI-01 | Audit `classical_uniqueness_on_Icc`. | [x] | Preserve its actual hypotheses in the peer review. |
| UNI-02 | Audit selected-candidate instantiation and no-global conclusion. | [x] | Do not describe the R³ theorem as candidate-only or dead code. |
| UNI-03 | Test compact pressure support as a trivialisation premise. | [x] | Keep this route cleared unless a separate absolute Poisson identity is proved. |
| UNI-04 | Check kernel dependencies of R³, uniqueness, and periodic endpoints. | [x] | Standard axioms only; no admitted declaration found in the audited path. |
| UNI-05 | Produce selected-path `False` from this chain. | [ ] | Requires a false mandatory premise; none found in this pass. |

Evidence: `NavierStokesReview/evidence/whole_space_uniqueness_audit_2026-09-24.md`.

## Release-control recheck: 2026-09-24

| Check | Status | Result |
|---|---:|---|
| Selected rank path | [x] | The actual cycle consumes rank/debt data; the two local radial invariants are compiled in `SelectedCycleMomentTransport.lean`. |
| Endpoint transport | [ ] | `Witness` exposes no equality to the five paper moments or to `FiveRowRank.FiveRows`; a concrete selected-field violation remains to be proved. |
| Whole-space audit | [x] | The comparison/uniqueness chain and standard-axiom report are recorded. |
| Release packaging | [x] | Review commit `c9adab3` is pushed to `review/cmi-first-navier-stokes-2026-09-22`. No tracked Lean build artefacts exist. The two supplied PDFs remain intentionally untracked. |

The active route is therefore the selected-field transport theorem, not the
discarded claims that the five-moment branch is dead code, that the first two
rows freeze total kinetic energy, or that compact pressure support alone
trivialises the candidate.

## Reachability and external-data scope

| Task | Status | Acceptance condition |
|---|---:|---|
| Audit the `ActivePair` empty branch | [x] | Source split and branch premises identified. |
| Prove concrete-label reachability | [x] | `active_pair_of_selected_label` compiles without admitted declarations. |
| Prove selected-label inhabitance | [x] | Review theorem constructs `Nonempty (ActualPrimary.Label B N0)` above the selected band floor. |
| Convert the branch into `False` | [ ] | Requires a false selected predicate, not branch inspection alone. |
| Preserve CMI wording distinction | [x] | Causal/provenance criticism separated from literal C/D hypotheses. |

Evidence: `NavierStokesReview/evidence/selected_active_pair_reachability_2026-09-24.md`.

### CTR-019 selected-label inhabitability sweep

| Task | Status | Acceptance condition |
|---|---:|---|
| Recheck the active/nonempty source split | [x] | `raw_jets` and `ActualInitialMean.covariance_bounds_of_curl` both expose explicit empty branches. |
| Repair and compile the reachability theorem | [x] | Stage label `(0,L)` is used at the `ActivePair` boundary; audit and probe compile without admitted declarations. |
| Prove selected label inhabitance | [x] | `SelectedLabelConstructionProbe.selected_primary_label_nonempty` compiles without admitted declarations. |
| Test diagonal-sum vacuity | [x] | `potentialSum` is shown to be a total natural-indexed `tsum`; empty `ActivePair` does not imply an empty-set limit. |
| Update the verdict only from selected-path evidence | [x] | CTR-019 is cleared as a selected-path vacuity route; retain the generic empty-branch fact without overclaiming. |

Evidence: `NavierStokesReview/evidence/selected_label_inhabitability_audit_2026-09-24.md`.

## Global germ-transport validity audit (CTR-016)

| Check | Status | Decisive source / result |
|---|---:|---|
| Identify the local-to-global consequence theorem | [x] | `CandidateConsequences.mixed_exists_force_with_consequences`, lines 185--215. |
| Trace the concrete selected assembly | [x] | `ActualCandidateAssembly.physicalData`, `estimates`, `endpoints`, and `Witness`, lines 1079--1151; `selected_witness`, lines 1177--1181. |
| Test global consequences against fixed-force transport | [x] | `GlobalTransportBridgeProbe.lean` compiles: `Consequences` coexists with failure of `FixedForceSameDatumStable`. |
| Derive literal C/D `False` | [ ] | The endpoint still has no perturbation-stability or five-moment field identity requirement. |

Evidence: `NavierStokesReview/evidence/global_germ_transport_audit_2026-09-24.md`.

## Official claim transport and underclaim gate

| Task | Status | Acceptance condition |
|---|---:|---|
| Map each published Theorem 1.1 obligation to the Lean endpoint | [x] | `official_claim_transport_matrix_2026-09-24.md` records source anchors and endpoint status. |
| Separate literal C/D predicates from the paper's five-moment explanation | [x] | The matrix records the endpoint predicates as present and the selected five-moment identification as unproved. |
| Treat burden of proof asymmetrically | [x] | OpenAI must supply the selected-field transport theorem before the published solution claim is accepted. |
| Prevent underclaiming the review result | [x] | The primary verdict is `NOT ESTABLISHED`; `NOT FORMALLY REFUTED` is only a narrower report about the current `False` search. |
| Promote the correspondence gap to `False` | [ ] | Requires a false equality or false mandatory premise on the selected path. |
| Continue selected-field theorem search | [~] | Locate a theorem identifying the final mixed fields with `(M,I,J,S,C_p)`, or compile a concrete counterexample to that identity. The publication verdict already remains `NOT ESTABLISHED` if the affirmative bridge is absent. |

The active counter-paper target is therefore an underclaim in the published
mathematical correspondence, not a generic objection to compilation.

## Burden-of-proof gate

The publication verdict is controlled asymmetrically. OpenAI must provide the
selected-field composition theorem before the published solution claim is accepted. If
that theorem is absent, the review records **NOT ESTABLISHED** and withholds
acceptance. **NOT FORMALLY REFUTED** remains only a subordinate technical
status reporting that the current Lean attack has not derived `False`; it is
not a presumption that the missing bridge exists. Continue the `False` search
as a separate lane, not as a prerequisite for the publication verdict.

## Selected physical-data moment gate

| Task | Status | Acceptance condition |
|---|---:|---|
| Trace `PhysicalData` into the selected residual-rate endpoint | [x] | `ActualCycleResidualBounds.lean:1015-1037, 1142-1173`; `ActualCandidateAssembly.lean:1079-1098` |
| Test whether the exported record determines a five-moment payload | [x] | `SelectedPhysicalDataMomentInterfaceProbe.lean` compiles with arbitrary nonzero abstract debt |
| Prove the selected mixed fields equal `(M,I,J,S,C_p)` | [~] | A field-level integral identity in the selected `Witness` path; this remains the load-bearing proof obligation for the published claim. |
| Derive a selected-field mismatch | [ ] | A false equality or false mandatory endpoint premise, proved without `sorry` |

The publication gate is already met for the narrower review conclusion:
without the selected-field composition theorem, the published solution claim is
**NOT ESTABLISHED**. The remaining two rows are required only for a stronger
kernel-level refutation. Their absence is already sufficient to withhold the
advertised affirmative paper claim.

**Last updated:** 2026-09-25

## Source-trace correction

The selected closure reaches the five-moment construction. The active task is
therefore not to prove that the formulas are absent. It is to obtain or refute
the selected-field identity linking `PositiveOrderMoments.moments` and the
paper tuple
$$
(M,I,J,S,C_p)
$$
to the mixed fields assembled at `ActualCandidateAssembly.lean:515-523` and
exported by `Witness` at `1121-1151`.

| Check | Status | Evidence |
|---|---:|---|
| Five radial densities exist | [x] | `PositiveOrderMoments.lean:76-85` |
| Five-row cancellation is proved upstream | [x] | `GlobalSlowProfiles.lean:1043-1055`; `AssembledSlowBase.lean:592-617` |
| Selected mixed-field transport into the final residual/force contract | [ ] | No field-level equality found in `Witness` |

Evidence: `NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.

## Claim-level reconciliation: 2026-09-25

| Review level | Current result | Required next action |
|---|---|---|
| Literal R³ C/D proposition | Exported by `NavierStokesR3.theorem_1_1`; force provenance alone does not contradict it | Audit imported analytic lemmas for an actual false premise or invalid operator identity |
| Paper's five-moment mechanism | Upstream construction is live, but selected-field composition into `Witness` is not exposed | Require or derive the equality for the paper tuple $(M,I,J,S,C_p)$ on the final mixed fields |
| Formal refutation | No zero-sorry `False` for the selected endpoint | Do not label the literal theorem refuted without a concrete selected-field contradiction |

The publication-level counterfinding remains valid: the advertised
five-moment explanation is not established by the exported selected-field
interface. The review must not misstate this as proof that the literal C/D
proposition is false.

Evidence: `NavierStokesReview/evidence/cmi_target_and_claim_level_reconciliation_2026-09-25.md`.

## Repository-wide admission census

| Task | Status | Acceptance condition |
|---|---:|---|
| Census every default build target for admitted declarations | [x] | `ComparatorChallenges/NavierStokes.lean:273-284` and `ComparatorChallenges/Euler.lean:85-88,181-184` contain explicit `sorry` bodies. |
| Keep selected endpoint and repository-wide claims separate | [x] | Census does not claim the challenge declarations lie on `NavierStokes/R3`'s dependency path. |
| Record the release-level consequence | [x] | Blanket repository-wide zero-sorry claim is rejected; evidence is `repository_admission_census_2026-09-25.md`. |
| Reproduce the admission result through Lean's axiom report | [x] | `RepositoryAdmissionAudit.lean` compiles and reports `sorryAx` for all four standalone challenge declarations; see `repository_admission_axiom_log_2026-09-25.md`. |

## Selected-endpoint transport obstruction: 2026-09-25

| Task | Status | Acceptance condition |
|---|---:|---|
| Test the actual selected `Witness`, not only a generic stage interface | [x] | Review extension imports `ActualCandidateAssembly` and uses `selected_witness`. |
| Test whether the exported witness determines a five-coordinate payload | [x] | A zero-sorry theorem pairs the inhabited witness with a nonzero `PositiveOrderMoments.Debt`. |
| Claim that the selected physical integrals are false | [ ] | No such claim is made without a field-level integral equality. |
| Prove the paper's five-moment composition theorem | [ ] | Still required from the affirmative solution record. |
| Derive selected-path `False` | [ ] | Continue only through a false selected premise or an exact contradictory identity. |

Evidence: `NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md`.

The active counter-paper conclusion remains **NOT ESTABLISHED** for the
advertised solution claim. The new theorem strengthens CTR-005 as an exported
interface non-implication; it does not convert an absent transport field into
a fabricated contradiction.

## CTR-005 profile-tail collision route: 2026-09-25

| Task | Status | Acceptance condition |
|---|---:|---|
| Confirm the scope of `FiveRows` | [x] | Zero rows are correction-profile identities for `dv` and `ga`, not total-field moments. |
| Test whether nonzero runtime debt is compatible with those rows | [x] | `CTR005ProfileTailCollisionScope.lean` proves compatibility without admissions. |
| Trace the selected cycle invariant | [x] | Selected cycle zero-moment theorem is compiled and source-linked. |
| Map selected Cartesian `tsum` fields to radial `barMoment`/history types | [ ] | Required field-level evaluation bridge is still absent. |
| Prove a selected nonzero remainder | [ ] | No source-backed value or inequality has yet been established. |
| Derive selected-path `False` | [ ] | Remains open; do not infer it from the correction-row interface alone. |

Evidence: `NavierStokesReview/evidence/ctr005_profile_tail_collision_route_2026-09-25.md`.

## Field-level remainder calculation: 2026-09-25

This is the remaining route to a kernel-level contradiction. It must evaluate
the selected fields, not merely restate the missing bridge.

| Work item | Status | Required result |
|---|---:|---|
| Trace `potentialSum` as the actual natural-indexed `tsum` of cut stages | [x] | `SolenoidalDiagonal.lean:20-39`; finite-tail/local-prefix lemmas recorded |
| Trace the Cartesian construction before projection | [x] | `ActualCandidateConstruction.lean:509-520,963-966`; `ActualMeanPotentialRealization.lean:29-40,630-648`; `DirectAngularDiagonal.lean:65-71,231-237` |
| Trace `barMoment` and `FiveRows` after profile formation | [x] | `DefectIncrementBounds.lean:214-220`; `FiveRowRank.lean:241+`; rows constrain `dv` and `ga` |
| Prove a Cartesian-curl to radial-profile identity for the selected `tsum` | [ ] | Explicit theorem with all coordinate changes and endpoint hypotheses |
| Check cutoff-mask derivative terms | [ ] | Evaluate whether derivatives of localization masks enter the selected radial moments; do not infer a leak from absence of a preservation lemma |
| Check curl/projection boundary terms at the axis and infinity | [ ] | Concrete boundary value or inequality, not a generic pressure/localization objection |
| Check finite-prefix moments before the infinite tail is active | [ ] | Exhibit a stage and a value of `t` with an exact nonzero remainder, if one exists |
| Derive `False` from a selected nonzero remainder | [ ] | Zero-sorry theorem combining the actual selected-field identity with the correction invariant |

The review-side scanner
`NavierStokesReview/tools/radial_profile_integrals.py` is a symbolic
calculation aid. It accepts explicit profile expressions and computes the five
integrals and their residuals against the promoted debt vector. It does not
pretend to extract a Cartesian expression from Lean. A remainder becomes
evidence only after the expression is linked to the selected field by a Lean
theorem.

## Companion Euler interval audit: 2026-09-25

The Euler parent-child route is tracked separately. The source audit found
geometric contraction and positive common horizons, but no theorem establishing
a quiet Zeno endpoint before the advertised singular time. The seam
constructions prove value and first-derivative matching. An all-order time-jet
theorem across every parent-child seam remains an open check; it must not be
converted into a discontinuity claim without a concrete unmatched jet. The
audit is recorded in `docs/Euler_Parent_Child_Interval_Audit.md` and
`NavierStokesReview/evidence/euler_parent_child_interval_audit_2026-09-25.md`.

## Cartesian-to-radial gate completion: 2026-09-25

The first exact coordinate recovery identity is now compiled. It is a gate
into the remaining calculation, not a nonzero-remainder result.

| Work item | Status | Required result |
|---|---:|---|
| Recover the scalar atlas coefficient from the selected angular component | [x] | `SelectedCartesianRadialGate.meanField_recovered_from_component_one` proves the positive-radius identity under `(radialProjection w).1 ≠ 0`. |
| Derive the radius nonvanishing obligation | [x] | The theorem derives `cartesianRadius ≠ 0` from the selected nonzero angular-frame coordinate. |
| Define a global axis-safe projection | [ ] | A projection must specify its value at the axis and prove compatibility with the off-axis chart; no such convention may be silently assumed. |
| Expand the localisation commutator | [ ] | Compute the contribution from differentiating `SmoothCutoffs.scaledCutoff` before the curl is applied. |
| Transport through the actual curl | [ ] | Identify the cut-stage curl with a scalar radial input only after all component and connection terms are retained. |
| Evaluate axis and outer-support terms | [ ] | Prove exact boundary values or inequalities for the selected field at `R = 0` and the supported outer radius. |
| Run the symbolic radial calculator | [ ] | Supply only a profile expression already identified with the selected field by Lean; arbitrary test profiles are not evidence. |
| Produce a selected nonzero remainder and `False` | [ ] | Requires both the selected equality and a proved `Delta m ≠ 0`; neither is currently available. |

Evidence: `NavierStokesReview/evidence/selected_cartesian_radial_gate_2026-09-25.md`.

## Complete calculation and companion-paper register: 2026-09-25

The following ideas are retained as explicit work lanes so that they are not
mistaken for completed objections:

| Lane | Required audit | Status |
|---|---|---:|
| Cutoff/curl commutator | Test `curl (chi • A)` against the selected source and retain the `fderiv chi` term; do not infer cancellation from smoothness or local finiteness. | [ ] |
| Axis extension | Compare the positive-radius chart with the origin branch and test all required derivatives; an off-axis hypothesis alone is not a discontinuity proof. | [ ] |
| Finite-prefix leak | Choose a concrete selected preterminal stage and time, expand its finite prefix, and calculate the moment before claiming a tail remainder. | [ ] |
| Scalar/vector typing | Construct the exact map from `VelocityField` to `ScalarField (Point P)` required by `barMoment`; document its domain, torus average, and support hypotheses. | [~] Positive-radius coefficient recovery is proved; full map remains open. |
| Five-row collision | Compare the transported selected profile with the correction-profile rows only after the preceding map is established. | [ ] |
| Euler Zeno route | Read `docs/euler.pdf`, the companion source, and the interval constructors; test geometric widths, positive horizons, value seams, first jets, all-order jets, and any hidden forcing term separately. | [~] Geometric and first-jet evidence exists; no quiet Zeno endpoint or seam mismatch is proved. |
| Radial helper | Run `NavierStokesReview/tools/radial_profile_integrals.py` only with a Lean-linked profile; record input and output as evidence. | [~] Tool exists; no selected profile is linked yet. |
| Defence matrix | Keep existential quantification, “given” force provenance, compact pressure support, smooth cutoffs, and five-moment correspondence as separate questions. | [x] Included in the source-context register; no single item is treated as a kernel contradiction without a selected theorem. |
| Editorial synchronisation | Update the plan, tracker, axiom ledger, synthesis, peer review, research paper, README, and control map after every proved source result. | [~] This gate and evidence file are the current synchronisation target. |

## Current execution order

1. Extract the exact selected profile expressions and active cutoff regions.
2. Build the Cartesian-to-cylindrical moment theorem, including axis and tail
   boundary terms.
3. Run the symbolic scanner on those exact expressions and record any nonzero
   remainder.
4. Attempt the zero-sorry contradiction only if the selected equality and a
   nonzero value are both available.
5. Update the paper, peer review, tracker, and control record with the result;
   keep the publication verdict and kernel-level verdict separate.

## Selected-field calculation gate: 2026-09-25

This is the active route for upgrading CTR-005 from an exported
correspondence objection to a selected-path contradiction. The target is an
actual value or inequality for the fields used by `selected_witness`, not a
repetition of the fact that a bridge theorem is absent.

| Calculation target | Required source-level check | Current state |
|---|---|---|
| Finite-prefix contribution | Expand `initialPotential` and `positivePotential` through `potentialSum` on a concrete positive spatial band and a time before the tail is active. | `[ ]` No exact selected radial expression has yet been exposed. |
| Cutoff-mask derivatives | Retain every derivative of `SmoothCutoffs.scaledCutoff` in the curl and residual; do not assume partition terms cancel. | `[ ]` The source gives local-finiteness and smoothness, not the required radial integral identity. |
| Curl-to-profile projection | Map the Cartesian curl in `ActualMeanPotentialRealization` to the cylindrical components consumed by `barMoment`, including the positive-radius hypothesis. | `[ ]` Chart identities exist, but no selected `barMoment` transport theorem has been found. |
| Axis and tail terms | Prove the boundary terms at `R = 0` and at the supported outer radius vanish, or calculate their exact values. | `[ ]` Generic support lemmas exist; selected-field boundary evaluation remains open. |
| Moment operator | Instantiate `DefectIncrementBounds.barMoment_apply` on the actual selected scalar profile, not on `dv` or `ga` alone. | `[ ]` The selected `VelocityField` is not typed as a `ScalarField (Point P)`. |
| Nonzero remainder | Exhibit a concrete `Δm ≠ 0` after all cutoffs, curls, and finite-prefix terms are included. | `[ ]` No source-backed value or inequality has been proved. |
| Kernel collision | Combine that exact selected equality with `SelectedCycleMomentTransport` or `FiveRows` in a zero-sorry theorem. | `[ ]` No `False` theorem exists. |

The symbolic helper `NavierStokesReview/tools/radial_profile_integrals.py`
is only a reproducible calculator for expressions explicitly supplied by the
reviewer. It cannot identify those expressions with the selected Cartesian
field. A calculator output therefore becomes evidence only after a Lean
transport theorem supplies the input profile.

The following arguments are not active contradiction claims and must remain
classified accordingly: zero correction rows are not zero total kinetic
energy; compact pressure support alone is not a Poisson contradiction; a
smooth cutoff is not a discontinuity; and fixed-force perturbations show
path-dependence of the residual construction but do not negate the literal
existential quantifier. The burden remains on the published solution claim to
provide the selected-field transport and moment identities.

## Selected finite-prefix completion: 2026-09-25

The first selected-field theorem beyond the generic endpoint has now been
compiled in
`NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean`.

| Calculation target | Status | Exact consequence |
|---|---:|---|
| Selected schedule is concrete | [x] | `selected_witness` supplies the schedule used by the selected stage aliases. |
| Selected potential `tsum` is locally finite | [x] | `potentialSum_eventuallyEq_partial` gives a finite prefix at every positive preterminal point. |
| All local jets use the same finite prefix | [x] | `potentialSum_allJets_eventuallyEq_partial` gives the result for every iterated derivative order. |
| Empty-filter or empty-tail explanation | [x] | Not available on the selected preterminal path; the tail is exactly zero after a finite index. |
| Cartesian-to-radial transport | [ ] | Still requires a theorem from the selected Cartesian `VelocityField` through curl, cylindrical projection, torus averaging, and `barMoment`. |
| Cutoff derivative contribution | [ ] | Must retain derivatives of `SmoothCutoffs.scaledCutoff`; smoothness alone is not a cancellation identity. |
| Axis and outer-support terms | [ ] | Must be evaluated for the selected field rather than inferred from generic support lemmas. |
| Selected nonzero remainder `Delta m ≠ 0` | [ ] | No source-backed value or inequality has been established. |
| Kernel contradiction | [ ] | Requires the preceding selected equality and nonzero value; no `False` theorem exists yet. |

This completion changes the status of the live route in one important way:
the selected series is not being treated as a vacuous limit. It does not,
however, prove that the paper's radial moments are wrong. The remaining test
is a real field-level calculation, not a restatement of the missing bridge.
Full source ledger:
`NavierStokesReview/evidence/selected_field_finite_prefix_transport_2026-09-25.md`.

## Companion Euler route boundary

The parent-child Euler interval audit remains a separate investigation. The
source proves positive horizons, geometric width control, and value/first-
derivative seam premises. It does not yet provide either a quiet Zeno endpoint
or an all-order time-jet mismatch. Euler evidence cannot be used as a Navier--
Stokes contradiction until the corresponding selected field and endpoint
identity are proved.

**Current next action:** expose one concrete positive-radius selected stage,
expand its Cartesian curl and cutoff derivatives, and attempt the first
`barMoment_apply` equality under explicit integrability and boundary
hypotheses.

### Selected-field calculation route: 2026-09-25

| ID | Required calculation | Status | Acceptance test |
|---|---|---:|---|
| CALC-01 | Identify the selected direct stage family. | [x] | selectedDirectStages is definitionally directStages; directStages_eq identifies each stage with angularMeanStages. |
| CALC-02 | Compute a concrete selected finite prefix. | [x] | SelectedDirectPrefixField.lean proves the uncut prefix equals the selected cycle-state mean angular field, with no sorry, axiom, or unsafe. |
| CALC-03 | Retain cutoff and curl terms. | [~] | Use DirectAngularDiagonal.cut_angularField and ActualMeanPotentialRealization.cartesianPotential_curl; no scalar radial projection theorem is yet supplied. |
| CALC-04 | Transport the selected Cartesian field to barMoment. | [ ] | Required theorem must construct a scalar ScalarField (Point P), torus average, and radial equality for the selected field. |
| CALC-05 | Evaluate axis and outer-support terms. | [ ] | Prove the boundary terms for the selected prefix and its cut-stage tail; generic support statements are insufficient. |
| CALC-06 | Prove a selected nonzero remainder Delta m ≠ 0. | [ ] | A symbolic calculator output is admissible only after CALC-04 identifies its input with the selected field. |
| CALC-07 | Derive kernel False. | [ ] | Combine CALC-06 with the selected correction invariant in a zero-sorry Lean theorem. |

Evidence: NavierStokesReview/evidence/selected_direct_prefix_field_2026-09-25.md and NavierStokesReview/evidence/selected_field_moment_calculation_gate_2026-09-25.md.

### Selected-cycle invariant check: 2026-09-25

The first field-level check against the proposed “clamped energy” route is
now complete. The selected recurrence is definitionally the same fixed
recurrence covered by `ActualCyclePreservation.state_invariant`; the review
completion
`NavierStokesReview/src/completions/SelectedCycleMasses.lean` proves
`ZeroMassesOn` for every selected stage. This is not a proof of the paper's
Cartesian five-moment claim. It is a source-backed result that prevents the
review from alleging a stage-level mass leak that the code actually rules out.

| ID | Required check | Status | Result / next test |
|---|---|---:|---|
| CALC-08 | Identify the selected recurrence behind `selectedCycle`. | [x] | It is definitionally the preserved `ActualCyclePreservation.state` recurrence. |
| CALC-09 | Prove selected-stage radial mass preservation. | [x] | `selected_cycle_zeroMasses` compiles for every `j`; evidence `selected_cycle_mass_preservation_2026-09-25.md`. |
| CALC-10 | Identify the selected Cartesian field corresponding to those state moments. | [~] | `selectedDirectStages` reaches `meanAngularField`; a vector-to-scalar `barMoment` projection is still required. |
| CALC-11 | Check cutoff/curl/axis/tail terms after that projection. | [ ] | Expand the actual angular vector and `cartesianPotential_curl`, retaining all derivative and boundary terms. |
| CALC-12 | Prove or disprove `Delta m ≠ 0` for the selected field. | [ ] | No value may be inferred from the correction invariant alone. |

| CALC-13 | Expose a concrete selected Cartesian component. | [x] | `SelectedAngularComponentFormula.lean` proves the component-one formula for `meanAngularField`; evidence `selected_angular_component_formula_2026-09-25.md`. |
| CALC-14 | Evaluate the atlas coefficient in the component formula. | [ ] | Requires a positive-radius selected band and an explicit physical-point/radial-profile expression. |
| CALC-15 | Carry the component through cutoff and curl into the radial operator. | [ ] | Retain all mask derivatives and connection terms; no cancellation may be assumed. |

The component theorem is a genuine selected-field refinement. It narrows the
calculation from a generic `VelocityField` to the scalar coefficient and
angular frame used by the selected direct stages. It still does not prove a
nonzero remainder.

| CALC-16 | Prove the selected scalar `barMoment` values. | [x] | `SelectedCycleMomentTransport.lean` proves the angular second and axial first scalar moments vanish on the carrier for every selected stage. Evidence `selected_scalar_barMoment_transport_2026-09-25.md`. |
| CALC-17 | Compare the scalar moment identity with the exported Cartesian field. | [~] | The selected field multiplies the atlas coefficient by the angular frame and then passes through localisation/curl; the equality and any boundary remainder remain to be calculated. |
| CALC-18 | Transport each selected direct stage through its actual positive-radius chart. | [x] | `SelectedDirectPrefixField.lean` proves `selected_direct_stage_eq_chart` using `ActualCandidateAssembly.directStages_eq` and `ActualCandidateConstruction.angularMeanStages_on_chart`. |
| CALC-19 | Expand the chart-realised field through localisation, Cartesian curl, axis/tail limits, torus average, and `barMoment`. | [ ] | Source order is now fixed: cutoff before `tsum`, then spatial curl, then local finite-prefix reduction. Retain every cutoff derivative and connection term. |

| CALC-20 | Isolate the cutoff-gradient curl term. | [x] | `SelectedCutoffCurlCommutator.lean` proves `curl (χ • A) = χ • curl A + curlLinear ((fderiv χ).smulRight (A x))`; the term is exact but its selected radial value remains open. |
| CALC-21 | Transport the commutator through the selected radial operator. | [ ] | Identify the selected potential, torus average, axis/tail limits, integrability, and `barMoment` input in one theorem. |
| CALC-22 | Recover a selected scalar coefficient on the radial section. | [x] | `SelectedRadialSectionComponent.lean` proves component one of the actual selected angular field equals `meanField` for `r > 0`. |
| CALC-23 | Join the positive-radius recovery to the axis and full mixed field. | [ ] | Handle the totalised axis frame, meridional curl contribution, cutoff commutator, torus average, and `barMoment` in one selected theorem. |

This result also records a required correction to the review vocabulary:
“zero correction rows” means preserved radial moments of correction/state
profiles in `ZeroMassesOn`; it does not mean zero total energy, zero total
momentum, or zero moment of the final Cartesian velocity.

### Complete idea and follow-up register: 2026-09-25

| Lane | Required work | Status |
|---|---|---:|
| Selected-field radial calculation | Expand `meanAngularField`, `angularVector`, `cartesianPotential_curl`, `scaledCutoff`, torus averaging, `barMoment_apply`, and axis/tail terms. | [~] Positive-radius coefficient now exposed; full mixed field remains. |
| Cutoff-curl commutator | Carry `curlLinear ((Dχ).smulRight A)` through the selected finite prefix and radial projection. | [x] Exact local term isolated; selected radial value open. |
| Radial-section coefficient | Recover the scalar coefficient from the actual selected angular field. | [x] Positive-radius theorem proved; axis and mixed-field transport remain open. |
| Grid-mask leakage | Check derivatives of every partition/cutoff in overlap zones; do not assume a partition identity cancels nonlinear residual terms. | [ ] |
| Finite-prefix remainder | Evaluate a concrete preterminal prefix before the tail is active; distinguish a finite-prefix value from an infinite-series limit. | [ ] |
| Curl/profile mismatch | Check whether the 3D curl-to-cylindrical projection preserves the radial identities or creates a boundary term. | [ ] |
| Kernel contradiction | Only write `False` after a selected equality and a selected nonzero value are both proved. | [ ] |
| Pressure semantics | Keep compact support, comparison recovery, and absolute Poisson semantics separate; seek a selected contradiction, not an interface-only objection. | [~] |
| Force provenance | Keep residual-as-force and fixed-force perturbation results as causal/provenance objections, not automatic negations of the existential endpoint. | [x] |
| Temporal gluing | Preserve the cleared result: smooth cutoffs and all-order jet premises are present; seek only an actual unmatched selected jet. | [x] |
| Selected-label inhabitation | Check constructive nonemptiness of active labels at every selected stage; do not infer vacuity from a generic filter risk. | [~] |
| Euler companion | Audit parent-child horizons, Zeno sums, value/first-jet seams, all-order seams, and any hidden forcing term separately from Navier--Stokes. | [~] |
| Euler source context | Read the supplied Euler PDF and OpenAI companion material; record only source-supported interval and PDE claims. | [ ] |
| Radial helper | Run `NavierStokesReview/tools/radial_profile_integrals.py` only after Lean supplies an exact selected profile; repair the local Python interpreter path before execution. | [~] |
| Source-context objections | Keep CMI wording, force provenance, existential quantification, pressure support, and physical five-moment semantics separate. | [x] The review distinguishes literal C/D endpoint obligations from the paper-to-code correspondence burden. |
| Editorial release | Maintain a human-readable README abstract and synchronise plan, tracker, axiom ledger, synthesis, peer review, research paper, and control map after each source result. | [~] Add the radial-section evidence to the release set. |
| Editorial packaging | Maintain the README abstract/editorial summary and synchronise paper, peer review, tracker, axiom ledger, control map, and plan after each proved result. | [~] |

### Tooling and source-control gates

| Gate | Acceptance test | Status |
|---|---|---:|
| Lean review tree | `lake build NavierStokesReview` has zero errors, zero `sorry`, zero custom axioms, and no `unsafe` in new review modules. | [x] 3700 jobs under Lean `v4.34.0-rc2` |
| Symbolic helper | V-lab Python interpreter executes the radial helper and records its exact input/output. | [ ] Current interpreter points to an inaccessible `uv` Python path. |
| Build hygiene | No `.olean`, `.ilean`, `.c`, or `.lake` outputs are tracked. | [x] |
| Documentation sync | New evidence is cited by the plan, tracker, axiom ledger, peer review, research paper, synthesis, README, and control map. | [x] Scalar moment and positive-radius chart evidence are recorded; the field-level `Delta m` calculation remains open. |
| Release | Commit and push the final selected-field audit update. | [x] Commit `73867db` is pushed to `review/cmi-first-navier-stokes-2026-09-22`; the two supplied PDFs and existing scratch file remain intentionally untracked. |

### Counter-paper source anchor

The target is the claim actually published, not a weaker generic proxy. OpenAI's
paper states a theorem with smooth compactly supported forcing, smooth fields
before the singular time, bounded kinetic energy, and unbounded velocity, and
then identifies the result with Alternatives C and D. Its Appendix A presents
the five cumulative quantities (M, I, J, S, C_p) as the mechanism removing
exterior stress and pressure tails. The review therefore treats the selected
Cartesian-to-radial composition as a load-bearing affirmative burden. The
official paper is
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf.

**Last updated:** 2026-09-25
