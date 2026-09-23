# OpenAI Navier–Stokes Axiom and Assumption Ledger

*Evidence ledger. Source snapshot: OpenAI Navier–Stokes repository, commit `f9e8bc5`.*

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
