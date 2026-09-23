# CMI-first review map: OpenAI Navier–Stokes claim

**Working verdict:** `NOT ESTABLISHED AS A CMI SOLUTION` until the selected endpoint is independently checked. This document is a compact work plan, not the research log. Evidence belongs under `NavierStokesReview/evidence/`; completed arguments belong in the peer review and paper.

## Status key

`[x]` checked and closed as an attack route  ·  `[~]` active review  ·  `[ ]` not yet checked  ·  `[!]` formal failure found

## Agent 2 verification board: 2026-09-23

| ID | Question | Status | Evidence / next action |
|---|---|---|---|
| BP-01 | Does `finalPotential` define a genuinely three-component field? | [x] | Reduced `(t, s, z)` profile is embedded in three Cartesian components and spatially curled. |
| BP-02 | Is the base field globally swirl-free? | CORRECTED | Only the radial gauge anchor is zero; no global angular-component-zero theorem was found. |
| BP-03 | Are the paper's five moments transported into the selected endpoint? | [~] | Upstream five-moment machinery exists, but no selected-path transport theorem was found through the generic germ/sum interface. |
| BP-04 | Is smooth forcing derived or injected? | [~] | `force_smooth` consumes residual-jet limits and away extensions; verify those premises for the selected fields. |
| BP-05 | Is `WholeDomain*` dead code? | CORRECTED | Unreachable from `selected_witness`, but reachable through paper-result modules. |
| BP-06 | Has a zero-sorry contradiction been obtained? | [ ] | None yet. Do not label the claim refuted without a selected-path contradiction. |

Evidence: `NavierStokesReview/evidence/base_profile_core_asymptotics_audit_2026-09-23.md` and `NavierStokesReview/src/probes/BaseProfileCoreAsymptoticsProbe.lean`.

## 1. Target and admissibility gate

| ID | Question | Status | Evidence / next action |
|---|---|---:|---|
| CMI-01 | Which Fefferman alternative is claimed? | [x] | R³ forced breakdown, matching the repository `CandidateProperties` shape. |
| CMI-02 | Is the force globally smooth, rapidly decaying in time, and supported at positive time? | [~] | `ProblemStatement.lean`, `CandidateFromLimits.lean`; verify selected endpoint predicates. |
| CMI-03 | Is the velocity smooth before the singular time and finite-energy as required? | [~] | Trace `CandidateConsequences` to the selected velocity; audit exact norm statements. |
| CMI-04 | Does the code prove the PDE on the required domain, rather than only define a residual? | [~] | Match `navierStokesResidual = forcing` against the selected candidate fields. |

CMI does not impose the additional conditions `∫ f dx = 0` or `∇ · f = 0` on the external force. Those are possible physical diagnostics, not automatic CMI disproofs. A conservation-law attack becomes decisive only after deriving the relevant identity from the stated hypotheses and showing that the selected force violates it.

## 2. Selected endpoint trace

| ID | Task | Status | Required result |
|---|---|---:|---|
| END-01 | Trace `selected_witness` into `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`. | [x] | Selected witness consumes actual stage estimates, endpoint extensions, and axis conditions. |
| END-02 | Check whether residual rate bounds are inserted or derived. | [x] | `ActualCycleResidualBounds.native_residual` derives the full residual bound from component estimates. |
| END-03 | Check whether `VanishingJointJets` and `AwayExtensions` are derived on the selected path. | [~] | Inspect the exact theorem chain and compile a zero-sorry dependency probe. |
| END-04 | Run `#print axioms` on the exported R³ endpoint and selected witness. | [x] | Current reports show only `propext`, `Classical.choice`, and `Quot.sound`. |
| END-05 | Audit `selectedBudget = 0` and selected stage aliases. | [x] | Zero is an input parameter; stage families remain indexed by `ℕ`; no `sorry` found. |

## 3. Force and endpoint regularity

| ID | Task | Status | Escalation test |
|---|---|---:|---|
| FORCE-01 | Inspect `PositiveTimeForce.timeCutoff`. | [x] | Smooth bump; active on `[3/8,1]`; no step discontinuity. |
| FORCE-02 | Locate pressure in the force residual. | [x] | Pressure enters `navierStokesResidual` in `CandidateFromLimits`; `PositiveTimeForce.force` is only a wrapper. |
| FORCE-03 | Check residual provenance. | [x] | Before `t=1`, `CandidateFromLimits.force` equals the activated residual; endpoint uses smooth extension. |
| FORCE-04 | Prove or refute selected residual endpoint limits. | [~] | Write a zero-sorry probe against actual `hlim`, not an arbitrary force norm. |
| FORCE-05 | Prove force-norm divergence, failed support, failed decay, or failed `ContDiff`. | [ ] | Any one exact selected-path failure upgrades this lane to `[!]`. |

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
| GLU-01 | Trace temporal gluing and endpoint jets. | [~] | `SpacetimeGluing.smoothExtension` proves the interface form; verify selected residual-limit inputs. |

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
| PRS-03 | Keep R³ and periodic-lift domains separate. | [x] | R³ `CandidateProperties` uses Euclidean compact support; periodic endpoint uses lifted periodicity. Do not transfer torus support arguments to R³. |
| PRS-04 | Print the exact meaning of `pressure_support`. | [x] | It is `tsupport(slice p) ⊆ K` with `IsCompact K`, not a pressure-Poisson axiom. |
| PRS-05 | Trace `PressureRecovery` and `ActualPressureFlux`. | [x] | `candidate_unique_on_Icc` supplies the selected candidate; `classical_uniqueness_on_Icc` constructs the recovery hypotheses and pressure-flux bound. |
| PRS-06 | Test the compact-pressure trivialisation inference. | [x] | Zero-sorry probe proves compact support does not imply a scalar slice is zero. |
| PRS-07 | Seek a genuine selected-path pressure contradiction. | [ ] | Must derive a Poisson/normalisation/decay premise from the endpoint and contradict the selected pressure; generic compact-support intuition is insufficient. |

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
| 1 | Trace `VanishingJointJets` and `AwayExtensions` into `selected_witness`. | Source-linked dependency note and probe. |
| 2 | Search for the five-moment transport theorem on the selected import closure. | Theorem citation or exact absence report. |
| 3 | Test the strongest actual selected obligation in Lean without `sorry`. | Compiled probes now cover divergence, pressure support, force smoothness, and energy exposure. |
| 4 | Update tracker, axiom ledger, synthesis, peer review, and paper. | Human-readable findings are being integrated; preserve counter-paper framing. |

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

**Last updated:** 2026-09-23
**Owner:** CMI-first formal review
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
parent-directory copy or Agent 2 diagnostic note. A claim enters this plan only
after source inspection or a recorded zero-sorry probe.

| ID | Control task | Status | Decisive condition |
|---|---|---:|---|
| DOC-01 | Quarantine stale parent verdicts and unsupported pure-axial claims | [x] | The control map identifies active, supporting, archival, and rejected notes. |
| DOC-02 | Reconcile Agent 2 notes with current source paths | [x] | `finalPotential`, selected imports, force gluing, and pressure support are corrected in the active corpus. |
| DOC-03 | Maintain one human-readable peer review and one research paper | [x] | Narrative documents point to tracker/evidence rather than functioning as logs. |
| DOC-04 | Resolve the selected five-moment transport objection | [ ] | Find or refute the theorem transporting the named moments through the selected endpoint. |
| DOC-05 | Verify final authority-map packaging | [x] | Control map, tracker, six core documents, and Agent 2 dispositions agree; no tracked build artefacts. |
