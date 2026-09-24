# OpenAI Navier–Stokes Axiom and Assumption Ledger

*Evidence ledger. Source snapshot: OpenAI Navier–Stokes repository, commit `f9e8bc5`.*

## AX-030 to AX-034: base-profile verification

**AX-030.** `finalPotential` uses reduced axisymmetric coordinates but produces a three-component Cartesian field through `spatialCurl`.

**AX-031.** `radialNormalize_anchor` is a local gauge identity. It does not prove global zero swirl.

**AX-032.** Five-moment repair machinery exists upstream, but the selected generic germ/sum interface does not expose a theorem identifying its output with `(M, I, J, S, C_p)`.

**AX-033.** `CandidateFromLimits.force_smooth` depends on residual-jet limits and away extensions. Those premises require independent selected-path verification.

**AX-034.** `WholeDomain*` is unreachable from `ActualCandidateAssembly.selected_witness` but reachable from paper-result modules. The precise finding is selected-endpoint disconnection, not global dead code.

**AX-035.** The local paper schedule and exported R³ candidate expose different
interfaces. `PaperLocalization` states local velocity/pressure agreement, but
the inspected result does not carry force equality or the paper's five-moment
tuple into `selected_candidate`. This is a missing transport assertion, not a
new axiom or a kernel inconsistency.

**AX-036.** The selected whole-space comparison does not treat pressure-flux
or scalar rate bounds as opaque endpoint axioms. `PressureFlux` and
`ComparisonRateBound` construct them from their displayed hypotheses, while
`PressureRecovery` supplies the compact-test gradient identity. Compact
pressure support therefore remains a rejected standalone attack, not a
demonstrated trivialisation theorem. This finding does not close CTR-005.

**AX-037.** `SelectedWitnessEndpointResidualProbe.lean` extracts the selected
schedule and proves origin speed blow-up together with a zero limit for the
selected raw mixed residual. It also proves that any fixed positive
velocity-to-residual lower bound would be contradictory. This records an
explicit cancellation result; it is not a force-singularity theorem and does
not by itself refute the final endpoint.

**AX-038.** `SameDatumFixedForcePerturbation.lean` adds no axiom and uses no
admitted declaration. Its selected-candidate theorem preserves the zero initial
datum while proving a nonzero fixed-force residual defect for an interior,
smooth, compactly supported, divergence-free perturbation. This is a stronger
CTR-012 provenance test, not a new premise of the C/D endpoint. Its dedicated
axiom audit reports only `[propext, Classical.choice, Quot.sound]`.

## Purpose

This ledger separates logical foundations, project-level premises, formal definitions, and physical requirements. A standard Lean axiom is not treated as a defect. A proposition imported as a premise, or a definition that is weaker than the paper's object, is a separate audit target.

## 1. Kernel-level foundations

The inspected endpoint reports:

```text
propext
Classical.choice
Quot.sound
```

These are standard Lean foundations. `#print axioms` on `NavierStokesR3.theorem_1_1`, `NavierStokesR3.theorem_1_1_with_initial_rest`, and `NavierStokesR3.ProblemStatement.breakdownStatement` found no named custom axiom. This finding is evidence about dependency hygiene only. It is not evidence that the definitions express the intended PDE construction.

## 2. Declared endpoint objects

`NavierStokes/R3/ProblemStatement.lean` declares:

- smooth velocity and pressure on the pre-singular whole-space domain;
- a globally smooth force with compact positive-time support;
- compact spatial support for each pre-singular slice;
- zero initial velocity, incompressibility, and the Newtonian equation;
- uniform finite energy and unbounded speed approaching time one;
- a global finite-energy comparison statement for the same force.

These declarations are materially closer to the official C/D statement than a periodic model. They must not be misreported as merely toy definitions.

## 3. Project-level assumptions and interfaces

| Interface | What it states | Audit status |
| --- | --- | --- |
| `FiveRowRank.Debt` | Three real residual debts | Abstract type; correspondence to `(P,Jθ,Jz)` and the paper's five cumulative moments is not shown here. |
| `FiveRowRank.FiveRows` | Five integral identities for angular and axial increments | Used by the physical rank-repair pipeline; its relation to `FiveProfileMoments` is not established. |
| `FiveProfileMoments` | Paper-shaped normalised moment map and five coefficient coordinates | Its exponent vectors match Appendix A when `b = -1/2 - λ`; its bridge to `FiveRowRank` is not established. |
| `MeanRankUpdate.physical_five_rows` | Scaled repair functions satisfy `FiveRows` | Formally checked, but only for the Lean row system. |
| `GlobalBaseError.originPast` | A concrete past-neighbourhood filter | Non-vacuity has a probe; downstream derived-filter audit remains open. |
| `JetRate` | A filter-based rate predicate | No `NeBot` parameter; generic `Filter.bot` vacuity is formally demonstrated. |
| `ActualCandidateAssembly.selected_witness` | Selected finite-stage data yield the candidate | Kernel accepted with standard axioms; load-bearing correspondence beneath it remains under review. |

## 4. The coordinate-level contradiction

The official paper's Appendix A gives the normalised intermediate blocks

```text
U: (0, -λ)
E: (1/2, -1/2 - λ, -3/2 - λ).
```

`FiveProfileMoments` gives those same blocks through:

```lean
axialPowers b   := ![0, b + 1 / 2]
angularPowers b := ![1 / 2, b, b - 1]
```

The separate `FiveRowRank` source gives:

```lean
angularPowers lam := ![2, -2 - 2 * lam, -2 * lam]
axialPowers lam   := ![1, 1 - 2 * lam]
```

`MomentCoordinateMismatchProbe.lean` proves the vector inequalities between these two source systems for every real `lam` by evaluating at index zero. This is a genuine zero-sorry theorem. It establishes that the code does not identify the two interfaces by definitional equality, even though one of them matches the paper's normalised blocks.

`MomentBridgeObstructionProbe.lean` strengthens this result. Its `DirectMomentBridge` structure requires both source power vectors to be equal, and `no_direct_moment_bridge` proves that structure impossible for arbitrary `lam` and `b`. The obstruction is therefore not a special-feature failure caused by the paper's substitution; it rules out the direct row-by-row reading of the declarations.

The probe also proves that the two debt spaces have no linear equivalence. `FiveRowRank.Debt` is `Fin 3 → ℝ`, while `FiveProfileMoments.Debt` is `Fin 5 → ℝ`. This is not a proof that no constrained or nonlinear correspondence can exist. It is a zero-sorry obstruction to claiming that the two full debt interfaces are the same linear coordinate space.

The correct conclusion is a missing cross-layer account, not an automatic refutation of every possible rescaling. The source must be credited with `PositiveOrderMoments.weighted_moments_exact`, `moments_repair_target`, and `GlobalSlowProfiles.profiles_moments`, which prove an exact five-coordinate repair in the recursive slow-profile layer. The remaining question is whether that layer is explicitly connected to the nominal `FiveProfileMoments` debt and to the later `FiveRowRank` physical inputs. `SelectedDependencyAxiomProbe.lean` confirms that the selected witness and stage-estimate interfaces do not rely on a visible custom axiom, so the remaining adverse target is semantic correspondence rather than kernel admission. Without an explicit staging and correspondence account, the public claim that the complete mixed pipeline directly verifies one coherent Appendix A system is unsupported.

## 5. Physical requirements that are not kernel axioms

The following are relevant to scientific interpretation but are not silently promoted to formal contradictions:

- a posteriori residual forcing versus an autonomous driver;
- stability under Ladyzhenskaya non-Newtonian stress;
- behaviour under fractional hypo-dissipation;
- pressure bounds on unbounded domains;
- smoothness of temporal and spatial cutoffs at the singular time;
- the distinction between Level A stress-cone matching and Level B exact PDE realisation.

Each requires its own theorem or counterexample. None follows merely from the presence of a smooth force in a C/D statement.

## 6. Ledger conclusion

The standard kernel report is not the end of the audit. The selected candidate also carries a substantive, non-axiomatic consequence: its force is nonzero at some time strictly before one. This belongs in the semantic ledger because it describes the witness actually constructed, not an additional axiom.

## 7. Selected-witness force consequence

`NavierStokes/CandidateConsequences.lean` proves

```lean
CandidateProperties u p f →
  ∃ t ∈ Set.Ioo (0 : ℝ) 1, ∃ x, f (t, x) ≠ 0
```

The review probe is `NavierStokesReview/src/probes/ForceActivityProbe.lean`. The proposition is compatible with alternatives (C) and (D), which permit a smooth time-dependent force. It does, however, rule out describing this witness as an autonomous collapse after the force has been removed. That is a semantic correction to the physical narrative, not a new kernel axiom and not, by itself, a CMI contradiction.

The command `lake env lean NavierStokesReview/src/probes/ForceActivityProbe.lean` succeeds, and `#print axioms force_nonzero_before_one_probe` reports only `propext`, `Classical.choice`, and `Quot.sound`.

## 8. Correspondence status

The ledger now distinguishes three claims that must not be conflated:

1. `#print axioms` reports only Lean's standard foundations on the inspected endpoints.
2. The selected force remains active before the singular time.
3. The direct row-by-row identification of the nominal and physical moment declarations is impossible without an additional transformation theorem.

Only the third is a formal correspondence obstruction. None of the three, standing alone, proves that the final C/D proposition is false.

No custom axiom has been found at the inspected headline or selected-witness interfaces. A zero-sorry formal obstruction has been found to a direct identification of the nominal five-coordinate interface with the physical three-debt interface, but a separate exact five-coordinate `PositiveOrderMoments` repair is present and load-bearing. The outstanding question is whether the repository proves the required maps and staging relations among all three layers. Until answered, the claim of complete direct formal verification must be reported as not established.

## 9. Regularity does not entail the physical rows

The distinction between an analytic interface and a moment equation is now formalised. `GaugeMomentBalances.MovingField` contains only `smooth`, `supported`, and `periodic` fields. The zero-sorry probe `MovingFieldRowNonImplicationProbe.lean` constructs the zero moving field and pairs it with zero backgrounds, zero increments, and a constant nonzero debt. The moving-field predicate is satisfied, while the third physical row becomes

```text
0 = -1
```

and is therefore false.

This is not evidence that the selected physical rank stage lacks a row solve. `LocalRankDefect.RankGeometry.fiveRows` supplies `FiveRowRank.FiveRows` through the stronger rank-geometry assumptions and `CorrectionState.rank_rows_on_patch`. The formal conclusion is narrower and useful: generic smoothness, support, and periodicity premises cannot be cited as if they already carried the five moment identities. The missing review obligation is the transport of the paper's five named quantities into the stronger rank-geometry data actually consumed by the selected path.

## 10. Empty active-pair branch audit

`ActualParticularStageControls.raw_jets` splits on `Nonempty (ActivePair B N0)`. Its negative branch does not obtain a contradiction from an arbitrary proposition. Instead, it proves `False` only after receiving `hz : z ∈ controlPatch l n k`; the first component of `hz` is an `Active l n` witness and therefore constructs the forbidden active pair. The control patch is consequently empty in that branch, and the estimates are vacuous over that empty support.

The positive branch uses `exists_surjective_nat (ActivePair B N0)` and an explicit reindexing. This audit removes a tempting but invalid claim that the source uses `False.elim` to prove arbitrary estimates on a nonempty physical patch. It does not yet prove that the selected active subtype is inhabited, so the endpoint-level reachability of the empty branch remains a live but narrower question.

## 11. Import graph versus semantic bridge

The import edge from `MeanRankUpdate.lean` to `FiveProfileMoments.lean` does not itself transport any proposition or data. A source census of `MeanRankUpdate.lean` finds its operative definitions in `FiveRowRank`: `Debt` is abbreviated to `FiveRowRank.Debt`, the rows are `FiveRowRank.FiveRows`, and `scaleDebt` has three coordinates. No theorem in that file invokes a `FiveProfileMoments` declaration. The ledger therefore records the edge as library availability, not as evidence of a nominal-to-physical moment correspondence.

## 12. Exact shape of the physical five-row predicate

The source-level declaration `FiveRowRank.FiveRows` must be read literally. It takes `Debt := Fin 3 → ℝ`, not a five-coordinate debt. Its conjunction is structured as two fixed zero-moment equations followed by three equations whose right-hand sides are `-(d 0)`, `-(d 1)`, and `-(d 2)`. `FiveRowsStructureProbe.lean` compiles these projections without assumptions beyond the declaration itself.

This is not a contradiction: the first two rows can be invariants established independently, and the source proves them for the constructed bumps. It is, however, a correction to any statement that this declaration alone implements an arbitrary five-equation, five-unknown inverse. The ledger therefore records the issue as a specification and correspondence obligation, not as a final C/D refutation.

## 13. Whole-space endpoint provenance

The whole-space endpoint is not an isolated wrapper around an unrelated witness. `NavierStokes/R3/Theorem.lean` obtains the viscosity-one candidate from `ActualCandidateAssembly.selected_witness`. `NavierStokes/R3/ActualCandidate.lean` then applies the proved spatial localisation, positive-time force cutoff, and compact-support energy estimate. `NavierStokes/R3/ViscosityScaling.lean` transports the candidate from viscosity one to every positive viscosity and proves the residual scaling identity.

This closes a separate provenance objection: the R³ theorem is connected to the selected construction at source level. It does not close the moment objection. The endpoint provenance passes through interfaces whose physical meaning still depends on the missing correspondence account among `FiveProfileMoments`, `PositiveOrderMoments`, and `FiveRowRank`.

## 14. Whole-space comparison premise correction

An earlier audit formulation treated the final scalar rate inequality as an unproved hypothesis consumed by the whole-space endpoint. The source does not support that description. `WholeSpaceComparisonClosure.eq_of_pressure_flux_bound` calls `ComparisonRateBound.exists_uniform_rate_bound` internally after constructing constants from comparison norms. The pressure-flux constant is likewise produced inside `WholeSpaceUniqueness.classical_uniqueness_on_Icc` by `PressureFlux.exists_uniform_actual_pressure_flux_bound`, using `PressureRecovery.Hypotheses` assembled from smoothness, divergence, residual equality, and finite-energy bounds.

This correction removes a proposed interface-premise failure. It does not certify the analytic validity of pressure recovery or localised energy estimates. Those remain load-bearing and must be checked for correct hypotheses and whole-space meaning. Status: no external rate-bound assumption found at this endpoint; analytic derivation remains under review.

## 15. Pressure-chain axiom adjudication

The inspected pressure path uses compact temporal tests, continuity, a Fourier Sobolev bound, and weighted `L²` representation before producing the cutoff flux. The selected dependency probes found no custom axiom at these interfaces. The generic `Filter.bot` risk remains a valid audit question for other modules, but it was not shown to enter this pressure chain. No new axiom defect is therefore recorded.

## 16. Preserved-mass check

The fixed zero rows in `FiveRowRank.FiveRows` were tested against the possibility that the selected initial state had nonzero invariants. `ActualInitialization.initial_zeroMasses` proves zero angular and axial masses for `initialState B N0`; the correction-stage theorems preserve `ZeroMassesOn`; and `MomentInitializationProbe.lean` compiles the initialization theorem without adding an axiom. This is positive source evidence and removes the proposed invariant failure. It does not create a bridge between the nominal, positive-order, and physical-rank moment layers.

## 17. Source-tree admitted declarations

The selected endpoint and the archived challenge module must be reported separately. Direct compilation of `ComparatorChallenges/NavierStokes.lean` emits two warnings that theorem declarations use `sorry`, at the whole-space and periodic challenge theorem bodies. `NavierStokes/ComparatorSolution.lean` does not import that module, so those placeholders do not appear in the axiom dependency report for the exported solution.

Ledger status:

- exported headline and selected-witness paths: no visible custom axiom or `sorry` dependency in the inspected reports;
- `ComparatorChallenges/NavierStokes.lean`: two admitted challenge declarations remain in the source tree;
- interpretation: this is a repository-scope metadata defect, not a demonstrated defect in the selected C/D endpoint.

The defensible statement is therefore “the exported theorem path is standard-axiom-only,” not “every Lean file in the repository is zero-sorry.”

## 18. Selected-stage provenance

`ActualCandidateAssembly.selected_witness` feeds the R³ endpoint through `GluedStageEstimates.actualStageEstimates`. The estimate constructor consumes `ActualCycleResidualBounds.PhysicalData`; `ActualPhysicalPrefixFields.physicalFields_all` derives that record from actual smoothness, local physical germ agreement, pressure-germ agreement, and exterior equality. This closes the disconnected-wrapper suspicion at source level. It does not resolve whether the several moment systems passed through those fields have the common five-moment meaning claimed in the paper.

## 19. Selected-closure moment census

The selected import closure does contain the nominal moment layer. `NominalProfile`, `ModulatedHistories`, `ModulatedCone`, `ModulatedProfileAssembly`, `MatchingDebtBounds`, `RepairConeBounds`, and `ReservedPatches` contain substantive references to `FiveProfileMoments`. The adverse claim must therefore not be phrased as absence of nominal five-moment code.

The inspected `ReservedPatches` cross-use is not a transport theorem. `momentPatch` and `five_row_updates_supported` establish support for the nominal bump functions, while `radial_heated_fields` identifies the heated outgoing field with a `FiveRowRank.background` profile. No inspected declaration there equates `FiveProfileMoments.physicalMoments` with `FiveRowRank.FiveRows` or converts the nominal five-coordinate debt into the physical three-coordinate debt used by `MeanRankUpdate`.

Ledger status: both representations are present; local support and background identities are proved; a complete five-row transport theorem remains unidentified. This supports a correspondence objection to the public narrative, not a kernel-level refutation of the C/D endpoint.
## 20. Actual-field recomputation chain

The selected endpoint is not connected only through nominal profile declarations. `ActualPhysicalPrefixFields.physicalFields_all` constructs `PhysicalData` from actual regularity, local velocity and pressure germs, and exterior agreement. `ActualCycleResidualBounds.Invariant.stateRealization` carries those fields into `StateRealization`. Its `chartIdentity` theorem reconstructs the Cartesian residual from the actual velocity and pressure after the polar inverse. This is positive provenance evidence for the paper's requirement that a correction be recomputed from the updated field.

No contradiction was found in the stale-background attack on the selected path. This evidence does not prove the analytic estimates independently, nor does it identify the published five moments with every downstream physical row.

## 21. Selected filter non-vacuity

`DiagonalResidual.JetRate` has the generic form `∃ C, 0 ≤ C ∧ ∀ᶠ x in l, ...`; it has no `NeBot l` premise and is therefore vacuous at `Filter.bot`. The selected consumer is more specific. Its base filter is `GlobalBaseError.originPast`, defined as a neighbourhood-within filter at the endpoint, and the proof uses `originPast_before`, `originPast_tendsto`, and `originPast_q_tendsto_zero` before splitting on the selected region.

The generic specification hazard is confirmed, but selected endpoint vacuity is not demonstrated. A future audit must census every other `JetRate` consumer rather than generalising this local result.

## 22. Current formal adjudication: 2026-09-23

| ID | Proposition or interface | Evidence | Classification |
|---|---|---|---|
| AX-009 | Direct identification of paper moments with `FiveRowRank` | `MomentBridgeObstructionProbe.lean` proves incompatible exponent vectors and no linear equivalence of debt spaces | PROVED ADVERSE |
| AX-010 | Separate exact five-dimensional repair | `PositiveOrderMoments.lean` proves exact repair for a distinct physical row system | CONFIRMED, BUT DISTINCT |
| AX-011 | Paper moments are identified with the actual five-row repair and consumed by the selected endpoint | No inspected correspondence theorem in the R3 endpoint path | OPEN, LOAD-BEARING |
| AX-012 | Force-free or autonomous blow-up | `PositiveTimeForce.lean` keeps the residual-driven force active through the singular interval | NOT ESTABLISHED; stronger interpretation contradicted |
| AX-013 | Generic `JetRate` is safe without non-vacuity | Definition has no `NeBot`; selected `originPast` path separately checked | INTERFACE HAZARD, ENDPOINT EXPLOIT NOT DEMONSTRATED |
| AX-014 | Challenge `sorry` declarations contaminate headline R3 endpoint | Source and selected dependency reports do not place them on the path | NOT SUPPORTED |

The ledger distinguishes a proved adverse correspondence result from an unproved assertion that the exported endpoint is false. Standard foundational axioms are recorded transparently and are not counted as project-specific assumptions.

## AX-015: constructive correction to the moment objection

`FiveRowPositiveOrderBridgeProbe.lean` proves that the positive-order five-coordinate repair reduces exactly to the `FiveRowRank` repair under the promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)`. It also proves the exact positive-order weighted moments for the promoted physical repair. Status: **confirmed constructive bridge**.

This supersedes the stronger reading of AX-009. AX-009 proves that literal row-by-row identification and a full linear equivalence of the two debt spaces are impossible. It does not prove that the repair formulas are inconsistent. AX-011 remains open: the selected endpoint still needs a theorem transporting the paper's five named moment defects into the promoted physical interface.

## Supplement: selected import closure is not selected theorem dependence

`NavierStokesReview/src/probes/SelectedImportClosureProbe.lean` imports `NavierStokes.R3.Theorem` and resolves both `PositiveOrderMoments.Debt` and `FiveRowRank.Debt`. This proves that both namespaces are present in the compiled import closure. It does not prove that the selected endpoint uses the positive-order repair as the implementation of the paper's five-moment system.

The current dependency claim is deliberately narrow: the endpoint construction passes through `ActualCandidateAssembly.selected_witness`, `ActualStageEstimates`, `GermCandidateAssembly`, and `CandidateProperties`; a theorem identifying `(M,I,J,S,Cp)` with the promoted physical debt and transporting that equality into the residual estimates has not been located. This is a missing correspondence theorem, not a new axiom and not a contradiction.

## Supplement: withdrawn initial-face objection

The initial-face regularity objection is rejected. `preSingularDomain` is `Set.Ico 0 1 × Set.univ`, so it contains the initial face. `ContDiffOn` is relative to that half-domain and the source documents this semantics. No initial-time smoothness loophole should remain in the review.

## AX-016: repository-wide `sorry` census

A direct source census on 2026-09-23 found four admitted declarations under `ComparatorChallenges`: two in `ComparatorChallenges/NavierStokes.lean` and two in `ComparatorChallenges/Euler.lean`. The Navier–Stokes challenge file labels these as intentional standalone challenge placeholders, and the selected R³ solution does not import that module.

Status: **CONFIRMED REPOSITORY-SCOPE DEFECT; ENDPOINT CONTAMINATION NOT SHOWN**.

## AX-017: selected construction-interface provenance

The selected witness does not take an infinite residual-flatness assertion as an isolated axiom. `StageEstimates` contains finite-prefix smoothness and jet-rate obligations. `ActualCycleResidualBounds.finite_residual_rates` derives those obligations from the actual cycle invariant and physical-field data. `StageEstimates.exists_schedule` derives the diagonal schedule and vanishing joint residual jets. The force and candidate consequences are then constructed by `CandidateConsequences.mixed_exists_force_with_consequences`.

The localisation and cone interfaces are similarly connected to constructions: the velocity localisation is curl-generated with a proved divergence-free property, and the modulated repair coefficient bound is derived before cone preservation is invoked. These declarations introduce no new project-specific axiom in the selected endpoint reports.

Status: **SELECTED INTERFACE DERIVATION CONFIRMED; EXTERNAL ANALYTIC ADEQUACY STILL OPEN**.

## AX-022: global germ transport and semantic endpoint fields

`CandidateConsequences.mixed_exists_force_with_consequences` is a derived
local-to-global theorem. Its premises include local smoothness, divergence,
residual-jet limits, away extensions, and origin growth; its conclusion includes
`CandidateProperties`, lifespan and H³ consequences, force-jet decay, and
boundary jets (`CandidateConsequences.lean:185-215`). The selected assembly
supplies actual cycle data through `physicalData`, `estimates`, and `endpoints`
(`ActualCandidateAssembly.lean:1079-1115`).

The remaining admission is semantic rather than foundational: the exported
`Witness` has no field identifying the selected mixed fields with the paper's
five named moments. This is not a custom axiom and not a proof of inconsistency.
It is the load-bearing unverified correspondence recorded as CTR-005/CTR-016.

This entry narrows the counter-paper's adverse claim. A missing human-readable bridge from the paper's named moments to the selected promoted debt remains a correspondence defect, but the inspected source does not show that the final endpoint assumes convergence or incompressibility as its own conclusion.

The precise axiom claim is therefore limited. The inspected headline and selected-witness dependency reports are standard-axiom-only. The repository as a whole is not a zero-sorry corpus. Any public statement using the latter as evidence for the former is invalid until the challenge files are excluded explicitly.
## AX-018: selected stage aliases and zero budget

**Source:** `NavierStokes/ActualCandidateConstruction.lean:205-210`; `NavierStokes/ActualCandidateAssembly.lean:1163-1181`.

`selectedBudget` is a noncomputable definition with value `0`. `selectedThreshold_geometry` is a proved inequality, not an axiom. The three selected-stage names are definitions, and `selected_witness` is the theorem that applies the witness construction to those selected parameters. `noncomputable` controls executable reduction; it does not introduce a proof hole.

The selected budget does not truncate the stage index: the raw stage functions remain functions of `j : ℕ`. The zero-sorry `SelectedBudgetProbe.lean` verifies the literal value and the threshold inequality. No custom axiom or `sorry` was found in this alias block. The unresolved review question is whether the paper imposes an additional positive-budget condition that is absent from the formal interface; that would require a source-linked comparison, not an accusation that the aliases themselves are admitted proofs.
## AX-020: five-row integrals versus selected endpoint transport

**Sources:** `NavierStokes/FiveRowRank.lean:241-310`; `NavierStokes/CorrectionState.lean:462-476`; `NavierStokes/DefectIncrementBounds.lean:775-813`; `NavierStokes/PositiveOrderMoments.lean:23,916-960`; `NavierStokes/ActualCandidateAssembly.lean:1121-1185`.

The first two rows of `FiveRowRank.FiveRows` are not type-level axioms. They are explicit radial integrals and are proved by the repair theorems. The rank subsystem also has source-level bridges from actual slow base fields to those rows. Separately, `PositiveOrderMoments` defines a genuine five-coordinate debt from radial integrals and proves exact repair.

## AX-021: active smooth cutoff and residual-derived force

**Sources:** `NavierStokes/R3/PositiveTimeForce.lean:21-67`; `NavierStokes/CandidateFromLimits.lean:28-147`; `NavierStokes/ActualCandidateAssembly.lean:1121-1185`; `NavierStokesReview/src/probes/ForceActivityProbe.lean`.

`PositiveTimeForce.timeCutoff` is a globally smooth rescaled bump. It equals one at `t = 1`, so the wrapper does not switch the force off before the singular time. The compiled probe proves this and proves continuity of the wrapped force at the endpoint for every smooth input field. Thus “active at the singular time” is confirmed, while “non-smooth cutoff” is rejected.

The wrapper is not the residual definition. `CandidateFromLimits.force` glues the past residual to a smooth extension, and `force_eq_activated_residual` proves residual equality for `0 ≤ t < 1`. The global smoothness conclusion depends on locally uniform residual limits `hlim` and endpoint jets `L`, which are constructed upstream in `PeriodicResidualLimits.exists_candidate_force`. This records a genuine residual-feedback concern without converting it into an unsupported claim that the force must diverge.

**Status:** active smooth forcing confirmed; residual-driven construction confirmed; no zero-sorry force singularity or failed C/D premise established.

The selected endpoint still lacks an exposed theorem identifying its selected raw stage fields with either moment construction, or identifying those constructions with the paper tuple `(M, I, J, S, C_p)`. This is a missing transport obligation, not a newly discovered axiom. No formal contradiction is entered here.

Status: **EXPLICIT REPAIR PROVED; SELECTED TRANSPORT UNVERIFIED**.

## AX-019: native residual estimate is derived from invariant fields

**Source:** `NavierStokes/CorrectionStep.lean:9408-9460`; `NavierStokes/ActualCycleResidualBounds.lean:248-261, 845-884, 1158-1172`.

The residual estimate used by the selected endpoint is not a field named `native_residual` inserted into `CycleAnalyticInvariant`. The invariant carries analytic component bounds and an exact residual decomposition. The theorem `native_residual` derives the full native estimate from those components, then `residual_jetRate` restricts and combines it with the state-realisation and exterior estimates.

Status: **CLEARED AS A HIDDEN-FINAL-PREMISE OBJECTION; ANALYTIC ADEQUACY AND PAPER CORRESPONDENCE REMAIN OPEN**.

## AX-022: force-conservation proposal is not a CMI premise

**Sources:** `NavierStokes/R3/ProblemStatement.lean`; `NavierStokes/R3/PositiveTimeForce.lean`; `NavierStokes/CandidateFromLimits.lean`.

The proposed obstruction used `∫ f dx = 0` and `∇ · f = 0` as if they were mandatory CMI conditions. They are not present in the repository's forced C/D predicate. `PositiveTimeForce.force` is a smooth scalar time-cutoff wrapper, while the pressure gradient appears in the upstream `navierStokesResidual` used by `CandidateFromLimits.force`. A nonzero external momentum input therefore is not a contradiction to the formal statement.

## AX-024: selected incompressibility is attached to the final velocity

`ActualCandidateAssembly.selectedPotentialStages` are raw potential stages. The
selected witness does not use their individual divergence as the CMI condition.
The final velocity is assembled through the solenoidal construction, and
`SolenoidalDiagonal.divergence_velocitySum_on` proves its spatial divergence is
zero under the actual smoothness and schedule hypotheses. The zero-sorry
`SelectedDivergenceAudit.lean` probe extracts `hc.divergence_free` from the
selected endpoint.

This closes a category error, not the whole review. It does not prove the
endpoint residual limits, global force regularity, or paper-to-code moment
transport. Evidence:
`NavierStokesReview/evidence/selected_divergence_audit_2026-09-23.md`.

This lane is classified as **physical-realizability concern, not formal disproof**. It becomes decisive only if a separately justified admissibility axiom is added, or if the selected force is shown to fail one of the explicit smoothness, support, decay, PDE, or energy predicates.

## AX-023: external analytic-forcing regularity theorem

**Source:** [Constantin–Ignatova–Vicol, arXiv:2609.20803](https://arxiv.org/html/2609.20803v1), Theorem 1.1 and the discussion at lines 49–51 and 70–80.

The paper proves regularity under real-analytic forcing together with the anisotropic angular-mean bounds and exact axisymmetric core attributed to the OpenAI construction. It also states that, with a force bounded in `C²` up to the singular time, such a force cannot be analytic or vanish identically near the singular point. The reported OpenAI force is smooth and compactly supported, hence nonanalytic, so the theorem does not contradict the CMI forced predicate.

Status: **independent method limitation confirmed; selected Lean theorem not refuted**.

## AX-025: analytic-objection adjudication

**Evidence:** `NavierStokesReview/evidence/analytic_objections_adjudication_2026-09-23.md`; `AnalyticObjectionsProbe.lean`; `SelectedDivergenceAudit.lean`.

The selected endpoint exposes four distinct facts that must not be conflated: final-velocity incompressibility, an exact forced energy identity, compact pressure localisation, and smooth temporal gluing. The first two have positive source-level support. The latter two are live correspondence targets: compact pressure must be reconciled with any claimed whole-space pressure equation, and smooth gluing must be traced back to the concrete residual-limit and endpoint-jet premises. None of these observations alone is a formal disproof.

**Status:** **three analytic lanes remain open; raw-stage divergence objection closed**.

## AX-026: selected residual filter is non-vacuous

**Source:** `NavierStokes/DiagonalResidual.lean:33-34`; `NavierStokes/JointResidualLimits.lean:84-90,162-165`; `NavierStokesReview/src/probes/FilterNonVacuityAudit.lean`.

The generic `JetRate` predicate is defined without a `NeBot` typeclass, so generic lemmas using it should not be treated as self-validating limit statements. On the selected path, however, the residual filter is `𝓝[SpacetimeEndpoint.openPast 1] (1, x)`, and the repository proves it is non-vacuous by rewriting it as `(𝓝[<] 1) ×ˢ 𝓝 x`. The zero-sorry probe instantiates this theorem at the selected origin.

This closes the claim that the selected endpoint is already proved only through `Filter.bot`. It does not automatically clear every restricted filter used elsewhere; those must be checked when they become premises of the endpoint.

**Status:** **selected endpoint filter non-vacuity confirmed; generic API hazard remains**.

## AX-027: selected pressure-recovery comparison is instantiated

**Source:** `NavierStokes/R3/ConservativeDifference.lean:431`; `PressureRecoveryHelpers.lean:116`; `PressureRecovery.lean:188,391,419`; `RieszTestOperators.lean:277,284`; compiler probe `PressureRecoveryInfrastructureProbe.lean`.

The repository contains typechecked compact-test pressure/Poisson and Riesz identities. These are not axioms or an automatic bridge from `cutPressure` alone. The selected path does instantiate the comparison chain: `WholeSpaceUniqueness.classical_uniqueness_on_Icc` constructs `PressureRecovery.Hypotheses` and obtains the actual pressure-flux bound, while `candidate_unique_on_Icc` supplies the selected candidate properties. The remaining question is analytic validity of the estimates, not whether the pressure modules are disconnected.

**Status:** **selected comparison instantiation confirmed; analytic estimates remain review targets**.

## AX-028: explicit three-to-five repair promotion

**Source:** `NavierStokes/FiveRowRank.lean:21-22,241-246`; `NavierStokes/PositiveOrderMoments.lean:21-23,192-228`; `NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean:22-51`.

The production rank debt has three coordinates. Its five-row predicate fixes
the first two correction moments to zero and uses the final three rows for the
three defects. A separate positive-order module has five actual integrated
moments. The zero-sorry probe proves that the explicit promoted vector
`(0,0,-P,-Jθ,-Jz)` makes the positive-order repair equal to the production
repair and satisfies the five weighted identities.

This is a proved algebraic bridge, not an axiom. It does not prove that the
paper's named `(M,I,J,S,C_p)` variables are the same quantities, nor that the
bridge is transported into the selected endpoint.

**Status:** **algebraic promotion proved; paper-to-selected semantic transport remains open**.

## AX-030: the zero rows are correction-state invariants, not selected-field energy axioms

**Source:** `NavierStokes/FiveRowRank.lean:21-22,240-284`; `NavierStokes/DefectIncrementBounds.lean:635-646,799-813`; `NavierStokes/ActualCandidateAssembly.lean:1121-1151`; `NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean`.

`FiveRowRank.FiveRows` constrains `dv` and `ga`, with a three-coordinate debt.
`five_rows` proves the predicate for nonzero debt, and the correction-state
theorems preserve two radial moments. Neither declaration is an axiom saying
that the selected Cartesian velocity has zero mass or zero kinetic energy.
The zero-sorry collision probe confirms that a nonzero rank debt and the
selected `Witness` can coexist because `Witness` exposes no rank debt or
perturbation parameter.

**Status:** **the proposed direct `False` collision is rejected; selected
five-moment transport remains the CTR-005 obligation**.

## AX-031: conditional obstruction for a nonzero correction moment

**Source:** `NavierStokes/FiveRowRank.lean:241-246,280-318`;
`NavierStokes/DefectIncrementBounds.lean:621-646,799-813`;
`NavierStokesReview/src/completions/CorrectionInvariantScope.lean`.

The two zero rows do have a rigorous consequence. Under the full `FiveRows`
hypotheses, the angular correction satisfies `barMoment 2 h.angular = 0` and
the axial correction satisfies `barMoment 1 h.axial = 0`. The new zero-sorry
completion derives `False` from either corresponding nonzero hypothesis.

This does not identify `h` with the selected Cartesian perturbation. It also
does not identify either radial moment with kinetic energy or with the paper's
tuple `(M, I, J, S, C_p)`. The load-bearing unresolved premise is therefore
the selected-path transport theorem that would supply those identifications.

**Status:** conditional contradiction proved; selected-field transport remains
open under CTR-005.

## AX-029: compact pressure support is not a zero theorem

**Source:** `NavierStokes/R3/ProblemStatement.lean:92-109`; `NavierStokes/R3/ActualCandidate.lean:59-108`; `NavierStokes/R3/PressureRecovery.lean:33-44,407-438`; `NavierStokes/R3/ActualPressureFlux.lean:28-45`; `NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean:37-50`.

The R³ candidate requires each pre-singular pressure slice's topological
support to lie in a compact set. The property does not include a pressure
Poisson equation or a pressure normalisation. The recovery modules are
comparison theorems with equal-residual, smoothness, divergence, and energy
hypotheses. The zero-sorry probe proves compact support alone does not imply a
scalar field is zero.

**Status:** **pressure attack remains open; compact-support-only implication is unproved, comparison instantiation is confirmed, and absolute selected-pressure semantics remain unresolved**.

The failed compact-support-only implication is not a clearance of the pressure objection.  The comparison lemmas prove identities under explicit comparison hypotheses; they do not supply a global pressure-Poisson or Leray-projection identity for the selected fields.  The selected whole-space envelope can therefore absorb the pressure-gradient residual into its prescribed force.  A valid refutation still requires a theorem about the selected fields themselves, not merely the support predicate.

This status is deliberately limited. It confirms only that the comparison
wrapper is present; it does not confirm the paper's global pressure semantics.
The selected source still lacks a single paper-linked theorem connecting the
local `StateRealization`/`chartIdentity` identities to the global pressure
object asserted in the narrative.

## AX-030: comparison pressure recovery is not absolute pressure verification

**Source:** `NavierStokes/R3/PressureRecovery.lean:31-44,419-438`;
`NavierStokes/R3/ConservativeDifference.lean:428-469`;
`NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean`.

`PressureRecovery.Hypotheses` is parameterised by two velocities and two
pressures and requires equality of their Navier--Stokes residuals. It does not
require a pressure-Poisson representative or a pressure normalisation for
either pressure. The zero-sorry probe constructs the record with both
velocities identically zero and with the same arbitrary smooth pressure on both
sides. The residual equality and divergence obligations then close
definitionally or by zero calculation.

This does not show that the selected pressure is false. It does show that the
comparison recovery and flux chain cannot, by its type alone, be cited as an
absolute semantic verification of that pressure. The unresolved obligation is
to connect `PhysicalFields.pressure_germ`, `StateRealization.base_equation`,
and the selected residual limits to a global pressure equation or equivalent
normalisation for the actual selected field.

**Status:** **comparison limitation machine-checked; selected-path contradiction not established**.

## AX-031: selected residual limits are rate-derived but moment-untransported

**Source:** `NavierStokes/MixedCandidateAssembly.lean:29-91`;
`NavierStokes/MixedDiagonalResidual.lean:168-195`;
`NavierStokes/GermCandidateAssembly.lean:223-271`;
`NavierStokes/ActualCandidateAssembly.lean:1153-1181`;
`NavierStokesReview/evidence/selected_residual_endpoint_trace_2026-09-24.md`.

The selected schedule derives `VanishingJointJets` from finite stage JetRates
and consumes the result in the generic force-consequence theorem. The public
selected-witness interface does not expose the five named moments as premises
of that limit or identify them with the selected residual. This is a semantic
transport gap, not proof that the residual limits are false.

**Status:** **selected-path moment transport unestablished; no formal
contradiction obtained**.

## AX-033: generic stage estimates carry no five-debt equality

**Probe:** `NavierStokesReview/src/probes/StageEstimatesMomentBlindnessProbe.lean`.

The zero-sorry theorem `interface_does_not_determine_five_debt` shows that the
`StageEstimates` type alone cannot determine a value of
`PositiveOrderMoments.Debt`. This is not an extra axiom and does not alter the
official endpoint. It records the exact information missing from the generic
interface: a theorem identifying the actual selected-field integrals with the
five moments in the paper.

**Status:** **confirmed interface obstruction; no selected-witness
contradiction yet**.

## AX-032: chart identity excludes the singular axis

**Source:** `NavierStokes/PhysicalResidualJetBounds.lean:885-966`;
`NavierStokes/PhysicalResidualTZ.lean:388-389`;
`NavierStokes/ActualCycleResidualBounds.lean:915-1000`;
`NavierStokesReview/src/probes/StateRealizationAxisExclusionProbe.lean`.

`StateRealization` requires nonzero radius on its domain, and
`graphSourceTZ` requires a strictly positive radial coordinate. Therefore
`StateRealization.chartIdentity` is an off-axis residual identity and does not
itself certify the origin used by `origin_blowup`. The selected construction
has a separate `GlobalBaseError.actual_error_vanishingJointJets` route for the
origin error. No theorem inspected here proves those two routes inconsistent.

**Status:** machine-checked scope limitation; not a selected-path
contradiction. A refutation still requires a false origin estimate or a
five-moment/pressure identity forcing a nonzero residual there.

## Document-control note

This ledger is active only in the fork. See
[`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md) for the status of
parent copies and supporting notes. A source file being imported in some
paper-result module is not enough to show that it is on the selected endpoint
path, and a source file not imported by `GermCandidateAssembly` is not enough
to show that its entire upstream construction is absent.

## Interface countermodel entry: 2026-09-24

The probe `StageEstimatesMomentBlindnessProbe.lean` adds no axiom and contains
no `sorry`. It proves a `Nonempty StageEstimates` instance for zero velocity and
pressure stages and separately proves that the zero velocity is not
`SpeedUnboundedAtOne`. The result is evidence about the weakness of the
interface, not an additional assumption used by the official endpoint.

**Status:** **confirmed interface-level countermodel; selected endpoint not
formally refuted by this probe alone**.

## AX-033: upstream five-moment construction is live, endpoint transport remains unexposed

**Source:** `NavierStokes/GlobalStressSupport.lean:144-180`;
`NavierStokes/EntranceAlignedBase.lean:666-697,871-874`;
`NavierStokes/FinalSlowBase.lean:107-109,356-382`;
`NavierStokesReview/src/probes/SelectedBaseMomentCompatibilityProbe.lean`.

The aligned and modulated construction proves the five positive-order moment
identities, derives conservative flux identities, exports finite residual
identities, and proves base origin blow-up. Therefore the claim that the entire
five-moment branch is dead is false. The selected endpoint still lacks an
exhibited theorem transporting those identities to the final mixed velocity,
pressure, residual, and force fields consumed by `selected_witness`.

**Status:** upstream chain confirmed; selected-mixed-sum transport unresolved.

## AX-034: selected residual lower-bound obstruction

**Source:** `NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean`;
`NavierStokes/CandidateFromLimits.lean:39-41,80-87`;
`NavierStokes/FinalSlowBase.lean:330-382`.

The zero-sorry probe proves that the selected origin velocity blow-up and
vanishing residual jets are inconsistent with any eventual fixed positive
lower bound from velocity norm to residual norm. The production source exposes
upper `JetRate` bounds and an explicit flat-error cancellation, but no such
lower bound. The selected-force composition probe now identifies the final
force with that flat residual at the origin, so this lower-bound route is
closed rather than a remaining force-singularity target.

**Status:** conditional contradiction proved; lower-bound force attack closed
by selected residual cancellation.

## AX-035: selected force inherits the flat origin residual

**Source:** `NavierStokesReview/src/probes/SelectedForceOriginCompositionProbe.lean`;
`NavierStokes/CandidateFromLimits.lean:108-111`;
`NavierStokes/MixedPeriodicAssembly.lean:91-100`.

The selected witness, late-time activation identities, and the periodic
localisation identities combine to identify the final force with the original
selected residual at the origin for (t\to1^-). The selected joint residual
jets then prove

$$
\lVert f(t,0)\rVert\to0.
$$

This formally closes the proposed force-explosion route. It also confirms that
the selected construction is designed around residual cancellation: velocity
growth alone does not force force growth. The remaining review target is the
unexhibited transport of the paper's five moments and global pressure meaning
into this cancellation theorem.

**Status:** selected force composition confirmed; force-singularity objection
closed; selected-witness contradiction still unestablished.

## AX-036: all-order jet premise and debt-blind localisation

**Source:** `NavierStokes/JointResidualLimits.lean:67-106`;
`NavierStokes/MixedCandidateAssembly.lean:67-90`;
`NavierStokes/MixedDiagonalResidual.lean:186-232`;
`NavierStokes/TimeLocalization.lean:74-96,127-153`;
`NavierStokes/MixedPeriodicAssembly.lean:67-101`.

`VanishingJointJets` quantifies over every `n : ℕ` and is derived on the
selected path from finite residual-rate estimates, rather than being an `H^3`
truncation. The time switch and the spatial localisation are also smooth local
equalities, so the complete residual operator is transported, including
advection, diffusion, and pressure-gradient terms.

Neither localisation file accepts a three-debt or five-moment parameter. The
cutoff identities therefore cannot establish the paper's moment transport;
they are debt-blind field identities. This is a correspondence limitation,
not evidence that the cutoffs delete cross terms or make the selected fields
non-Newtonian.

**Status:** all-order jet derivation and localisation regularity confirmed;
selected five-moment transport remains open.

## AX-037: fixed-force perturbation obstruction

**Source:** `NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean`;
`NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean`.

The zero-sorry theorem derives the complete perturbation defect required when
the same force and pressure are retained after replacing (u) by (u+e).
The extension also packages the result for the positive-time force wrapper.
The proof uses the residual add/subtract identity and no project-level axiom.

**Status:** compiled with standard Lean foundations only. This is a proved
fixed-datum obstruction and not yet a contradiction to the selected
existential witness, because the source does not provide an admissible
perturbation theorem.

## AX-038. Selected-closure moment census

The local import closure rooted at `ActualCandidateAssembly.lean` reaches 507
modules. Literal source counts in that closure are: `PositiveOrderMoments`
154, `FiveProfileMoments` 146, `FiveRowRank` 104, `FiveRows` 44,
`physicalMoments` 42, and `CorrectionState.debt` 44.

This is evidence against treating the five-moment implementation as globally
dead. It is not evidence that the selected endpoint exports the paper's
five-moment semantics. `Witness` at `ActualCandidateAssembly.lean:1121-1151`
contains no equality to `moments`, `physicalMoments`, `FiveRows`, or
`(M,I,J,S,C_p)`. The distinction is between reachable implementation and
selected theorem transport.

**Status:** source-backed correspondence gap; no new kernel-level axiom or
`False` derivation.

## AX-039: correction-row invariants do not yet reach the selected endpoint

**Source:** `NavierStokes/FiveRowRank.lean:240-284`;
`NavierStokes/CorrectionState.lean:241-251,444-458`;
`NavierStokes/DefectIncrementBounds.lean:621-646,799-813`;
`NavierStokes/ActualCandidateAssembly.lean:1121-1151,1177-1185`;
`NavierStokesReview/src/completions/CorrectionInvariantScope.lean`.

The zero rows impose two exact radial correction constraints and the generic
rank theorem preserves them through `rankStage`. They do not impose zero
kinetic energy or zero total Cartesian mass. The exported `Witness` has no
field carrying either invariant or the paper's five-moment tuple.

The strongest formal consequence is conditional: if a selected correction
increment is shown to have a nonzero corresponding radial moment, `FiveRows`
is inconsistent. The selected-path identification and nonzero calculation
remain unproved. This is a missing transport premise under CTR-005, not a
kernel-level contradiction.

## AX-040: the internal selected cycle does carry two local mass constraints

**Source:** `NavierStokes/ActualCyclePreservation.lean:259-262,826-833`;
`NavierStokes/ActualCandidateConstruction.lean:212-223`;
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.

`ActualCyclePreservation.Invariant` is a `CycleAnalyticInvariant` and includes
the `masses` field. Consequently, the actual cycle induction supplies
`GaugeMassPreservation.ZeroMassesOn` for every selected cycle state. The review
completion exposes that fact and derives `False` from either corresponding
nonzero radial moment.

This is not the paper's complete five-moment identity and is not yet an
exported `Witness` equality. The remaining load-bearing question is whether
the internal two-moment invariant is transported through the mixed sums and
identified with the paper's `(M,I,J,S,C_p)` at the C/D endpoint.

## AX-041: selected-witness fixed-force obstruction

**Source:** `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean`.

`selected_candidate_fixed_force_obstruction` destructs the selected witness,
binds its velocity, pressure, and force, and proves that the compact
divergence-free perturbation in the extension cannot obey the same residual
equation at $(t,x)=(1/2,0)$. The proof uses the selected candidate residual
equality and the residual addition identity. It adds no axiom and proves no
global `False`; a CMI-level refutation would still require an endpoint
independence predicate or another false mandatory premise.

## AX-042: selected force provenance is residual-defined

**Source:** `NavierStokesReview/src/extensions/SelectedResidualProvenance.lean`;
`NavierStokes/MixedPeriodicAssembly.lean:338-365`;
`NavierStokes/CandidateFromLimits.lean:80-110`.

The selected witness supplies a force satisfying the exact residual equation
throughout the pre-singular interval. The review theorem extracts this from
the exported candidate rather than relying on a name-based search. This is
strong evidence that the force is selected from the candidate motion, but it
is not an extra Lean premise forbidding such construction. Record it as a
provenance defect under CTR-012, not as a kernel contradiction.

## AX-043: whole-space uniqueness chain

`WholeSpaceUniqueness.classical_uniqueness_on_Icc` is proved from the stated
comparison hypotheses. Its pressure step uses compact spatial tests and the
residual equations; it does not assume an absolute pressure normalisation or
infer pressure vanishing from compact support. The selected-candidate wrapper
then supplies the candidate properties and derives agreement with every
global finite-energy competitor before time one.

`NavierStokesReview/src/audit/WholeSpaceAxiomAudit.lean` reports only
`propext`, `Classical.choice`, and `Quot.sound` for the R³ theorem, the
uniqueness lemmas, and the periodic corollary. This is a positive formal
verification result for the no-global-solution chain, not a new axiom and not
a `False` derivation.

## AX-044: fixed-force stability extension

`NavierStokesReview/src/external_semantic/FixedForcePerturbationStability.lean`
adds no axiom. Its theorem uses the existing compact perturbation obstruction
to prove failure of the explicitly strengthened `FixedForceStable` predicate.
The result is not a `False` derivation from the literal C/D endpoint because
force independence and perturbation stability are not endpoint fields.
