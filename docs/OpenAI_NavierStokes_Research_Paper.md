# Against the Claim of a Verified Navier–Stokes Blow-Up Proof

## Abstract

OpenAI's Navier–Stokes release presents a Lean 4 theorem intended to realise alternatives (C) and (D) of the Clay Mathematics Institute formulation. The repository does contain a substantial whole-space formal statement: it quantifies over smooth velocity, pressure, and force fields on R³, includes compact support and finite-energy conditions, and concludes finite-time unbounded speed. The theorem is not a periodic toy, and its exported proof currently reports only Lean's standard foundational axioms.

That result does not settle whether the Lean development formalises the analytic construction described in the accompanying paper. This paper develops an adverse but evidence-led finding. The repository contains a paper-shaped `FiveProfileMoments` system, a distinct `FiveRowRank` repair interface, and a third `PositiveOrderMoments` system that proves an exact five-component repair for the recursive slow profiles. A zero-sorry Lean probe proves that the first two source-level power-vector declarations are not definitionally equal. The unresolved load-bearing question is whether the nominal, positive-order, and physical-rank representations are connected by explicit theorems along the selected witness path.

The immediate conclusion is therefore precise. The claim that the repository mechanically verifies the paper's Appendix A construction is not established, and the stronger claim of direct formal correspondence is contradicted by the checked coordinate declarations unless an additional change-of-variables theorem is supplied. The source also contains substantial positive evidence in `PositiveOrderMoments`, so the adverse result is not that the repository lacks a five-row repair. It is that the cross-layer correspondence required by the public claim has not yet been demonstrated. This is a formal correspondence failure, not a contradiction of the final existential proposition itself. The paper also distinguishes genuine objections from arguments that do not work: an a posteriori force is allowed by alternatives (C) and (D), and a local `Filter.bot` hazard is not a global refutation unless it reaches the selected witness.

## Audit verdict

The answer is split. Yes, the repository contains a Lean-checked theorem with the outer shape of alternatives (C) and (D). No, the inspected source does not establish that this theorem is a faithful formalisation of the official paper's five-moment construction. The direct row-by-row identification is formally impossible; only a separately proved nontrivial change of variables could close that gap.

## 1. What must be shown

The relevant question is not whether Lean compiles. Compilation establishes that the kernel accepts a term of the declared type. The research question is whether the declared type and every load-bearing interface mean what the official paper says they mean.

For a counter-paper, a valid adverse result must take one of three forms:

1. a zero-sorry Lean theorem proving that a required correspondence is impossible;
2. a reachable premise that is false, admitted, or weaker than the published construction requires; or
3. a direct contradiction between a formal definition used by the selected witness and a required mathematical identity in the paper.

A physical objection alone is not enough. Non-Newtonian regularisation, hypo-dissipation, or a preference for an autonomous force may be relevant scientific criticism, but they are not internal failures of an alternative (C) or (D) proof unless those requirements are part of the stated theorem.

## 2. The official claim and the Lean endpoint

The accompanying paper states a smooth compactly supported force, a smooth divergence-free velocity and pressure on R³ before time one, zero initial velocity, uniformly bounded kinetic energy, and unbounded velocity as time approaches one. It then argues that no global smooth finite-energy solution with the same force can exist. The force is constructed as a residual of the chosen flow and is intended to extend smoothly through the singular time.

The Lean R³ modules mirror this outer shape. `NavierStokes/R3/ProblemStatement.lean` defines `CandidateProperties`, including smoothness, compact positive-time support for the force, zero initial velocity, incompressibility, the Navier–Stokes equation on the pre-singular interval, finite energy, and `SpeedUnboundedAtOne`. `NavierStokes/R3/Theorem.lean` exports `theorem_1_1` and the initial-rest variant. This inspection rules out two earlier overstatements: the source is not merely periodic, and continuous forcing is not automatically disallowed by the C/D wording.

The endpoint still depends on the integrity of the construction below that interface. A well-typed existential theorem can be valid as a proposition while failing to be the formalisation claimed in prose if an intermediate coordinate system, analytic bridge, or physical identity is missing.

## 3. Provenance of the whole-space endpoint

The source trace closes an important alternative explanation. The whole-space theorem is not an unrelated wrapper around a toy existential statement. `NavierStokes/R3/Theorem.lean` extracts its viscosity-one fields from `ActualCandidateAssembly.selected_witness`. `NavierStokes/R3/ActualCandidate.lean` applies spatial localisation and a smooth positive-time force cutoff, proves the compact-support energy estimate, and preserves the pre-singular speed assertion. `NavierStokes/R3/ViscosityScaling.lean` proves the residual scaling identity and transports the construction to every positive viscosity.

This is positive evidence for endpoint provenance. It also changes the adverse question. The review cannot reject the claim merely because the R³ theorem is disconnected from the selected construction. The remaining issue is semantic transport inside that construction: the selected witness uses several moment interfaces, and the source must prove that the interface consumed by the endpoint preserves the five physical quantities named in the paper.

## 4. Three moment layers and the missing bridge

Appendix A of the official paper describes five cumulative radial moments `(M, I, J, S, C_p)`. At the intermediate parameterisation, it records the normalised blocks

```text
U block: (0, -λ)
E block: (1/2, -1/2 - λ, -3/2 - λ).
```

The repository has a paper-shaped declaration in `NavierStokes/FiveProfileMoments.lean`:

```lean
axialPowers b   := ![0, b + 1 / 2]
angularPowers b := ![1 / 2, b, b - 1]
```

With `b = -1/2 - λ`, these are exactly the Appendix A blocks. That is positive evidence which the earlier version of this paper omitted.

The separate physical rank declaration in `NavierStokes/FiveRowRank.lean` is

```lean
def angularPowers (lam : ℝ) : Fin 3 → ℝ := ![2, -2 - 2 * lam, -2 * lam]
def axialPowers   (lam : ℝ) : Fin 2 → ℝ := ![1, 1 - 2 * lam]
```

The rank file defines `Debt := Fin 3 → ℝ` and `FiveRows` as five integral equations: two mass-zero constraints and three residual rows involving `V`, `G`, `dv`, `ga`. It proves smooth compactly supported repair functions satisfying those rows. `MeanRankUpdate.physical_five_rows`, `prescribed_five_rows`, and `reserved_five_rows` transport this rank interface into the actual candidate pipeline. Other branches, including `ModulatedHistories` and `ReservedPatches`, consume `FiveProfileMoments` directly.

The source also contains an important intermediate construction which must be credited. `NavierStokes/PositiveOrderMoments.lean` defines a five-coordinate `Debt := Fin 5 → ℝ`, the actual recursive `rowDensity`, and the transformed `weightedDensity`. Its theorem `weighted_moments_exact` proves all five positive-radius integrals exactly, while `moments_repair_target` and `exists_smooth_exact_repair` construct the correction for an arbitrary five-coordinate target. `GlobalSlowProfiles.exists_repaired_order` consumes this repair, and `GlobalSlowProfiles.profiles_moments` proves that the recursively constructed sequence has zero five-row moments. This is positive evidence against the earlier claim that the repository has only a three-row approximation.

The relationship among the three layers is nevertheless not automatic. `FiveRowRank` is a three-debt interface with two rows fixed to zero; `PositiveOrderMoments` is a five-debt interface whose first two components are repaired rather than fixed; and `FiveProfileMoments` is the nominal physical-density system. The source proves exactness within each relevant layer, but the inspected tree does not expose one theorem identifying the nominal physical-density debt with the positive-order debt and then with the later physical-rank inputs. If the layers are deliberately staged, the authors need to state that staging and its maps. If they are claimed to represent one literal Appendix A system, those cross-layer equalities are load-bearing.

The physical-rank declaration deserves a precise qualification. `FiveRowRank.FiveRows` has five displayed rows, but its adjustable debt is `Fin 3 → ℝ`. The first two rows are independent zero-moment constraints, while the final three rows use the three debt coordinates. The zero-sorry probe `FiveRowsStructureProbe.lean` verifies this decomposition directly from the source definition. This does not show that the construction fails: an invariant can legitimately be fixed rather than solved for. It does show that the code cannot be described as a generic five-equation, five-unknown inverse without an additional explanation. The load-bearing question becomes whether the two fixed constraints and three debt rows preserve the five paper moments, and whether the selected witness consumes exactly those preserved quantities.

The review probe `NavierStokesReview/src/probes/MomentCoordinateMismatchProbe.lean` proves, with no `sorry`,

```lean
FiveRowRank.angularPowers lam ≠
  FiveProfileMoments.angularPowers (-1 / 2 - lam)
FiveRowRank.axialPowers lam ≠
  FiveProfileMoments.axialPowers (-1 / 2 - lam)
```

The proof is elementary: evaluation at the first finite index reduces the first equality to `2 = (1/2 : ℝ)` for the angular vector and `1 = 0` for the axial vector. Lean checks this contradiction directly.

This does not show that a rescaling could never relate the two systems. It shows that no such relation is definitional. The existence of `PositiveOrderMoments` also means that the probe cannot be cited as a contradiction of the selected construction by itself. The correct requirement is an explicit account of which layer is used at each stage, together with the maps that preserve the five named moments and the physical constraints. The existence of `FiveProfileMoments` prevents the stronger claim that the paper-shaped system is absent. The adverse result is instead that the source contains several non-identical moment interfaces and the public claim has not yet supplied a single cross-layer correspondence theorem.

The stronger `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean` packages the proposed direct correspondence as a Lean structure and proves

```lean
theorem no_direct_moment_bridge (lam b : ℝ) :
  ¬ DirectMomentBridge lam b
```

for arbitrary `lam` and `b`, not only for the paper's substitution. This is a formal obstruction to treating the two declarations as the same five-row system. It does not rule out a nontrivial analytic transformation, but that transformation must be stated and proved rather than inferred from compilation.

The same probe proves a dimension-level obstruction to a direct linear debt identification:

```lean
theorem no_linear_debt_equivalence :
  ¬ Nonempty (FiveRowRank.Debt ≃ₗ[ℝ] FiveProfileMoments.Debt)
```

Here the physical rank interface exposes three free residual-debt coordinates, whereas the profile interface exposes five moment coordinates. This does not exclude an embedding into a constrained five-dimensional subspace, nor does it prove that the two modules are intended to represent the same stage. It does establish that a full linear identification of their debt spaces is impossible and that any claimed correspondence must state its restriction or stage distinction explicitly.

The dependency trace is load-bearing: `ActualCandidateAssembly.selected_witness` consumes `estimates`, which is constructed by `GluedStageEstimates.actualStageEstimates` from `ActualCycleResidualBounds.PhysicalData`. The actual candidate correction route uses `MeanRankUpdate` and `FiveRowRank`. The nominal and modulation route uses `NominalProfile`, `ModulatedHistories`, `ReservedPatches`, and `FiveProfileMoments`; the recursive positive-order route uses `PositiveOrderMoments` through `GlobalSlowProfiles`. The remaining audit obligation is therefore not merely a comparison of unused declarations. It is to show that these routes are intentionally staged and that the fields and debts handed from one route to the next preserve the published five-moment meaning.

## 5. Why other proposed objections are insufficient by themselves

The force is deliberately defined from the residual and remains active up to the singular time. That is a legitimate criticism of physical interpretation, but alternatives (C) and (D) explicitly allow a smooth external force. It therefore does not refute the stated C/D proposition.

The repository contains a `JetRate` abstraction without an explicit `NeBot` parameter. The review probe `JetRateVacuityProbe.lean` proves that a generic limit predicate over `Filter.bot` can be discharged vacuously. This identifies a real proof-engineering hazard. The selected path, however, uses the concrete `GlobalBaseError.originPast` filter and non-vacuous local neighbourhood lemmas. A fatal result requires tracing a bot filter into a mandatory premise of `selected_witness` or `theorem_1_1`; that reachability has not yet been proved.

Similarly, omitted Ladyzhenskaya stress laws and fractional dissipation are not contradictions to a Newtonian C/D theorem. They matter to claims of physical robustness, not to literal compliance with the stated Newtonian problem.

## 6. Axioms and kernel evidence

`#print axioms` on `theorem_1_1`, `theorem_1_1_with_initial_rest`, and `ProblemStatement.breakdownStatement` reports only `propext`, `Classical.choice`, and `Quot.sound`. This rules out the claim that the headline R³ endpoint visibly depends on a custom axiom. It does not prove that every analytic assertion in the source corresponds to the paper's intended mathematics. Foundational consistency and semantic correspondence are separate obligations.

The follow-up `SelectedDependencyAxiomProbe.lean` reports the same three standard axioms for `ActualCandidateAssembly.selected_witness`, `ActualCandidateAssembly.physicalData`, `GluedStageEstimates.actualStageEstimates`, and `ActualCycleResidualBounds.Invariant.residual_jetRate`. This is negative evidence against a hidden custom axiom at those interfaces. It is also why the adverse finding is stated as a missing correspondence theorem rather than as a claim that the kernel accepted an explicit `axiom` or `sorry`.

## 7. Conclusion

The honest adverse conclusion is not “Lean cannot prove this” and not “the force is illegal”. The checked evidence supports a narrower and stronger statement:

> The repository has a formally accepted C/D-shaped R³ endpoint, and it contains paper-shaped, positive-order, and physical-rank moment constructions. The direct equality between two of those interfaces is formally impossible, while the positive-order layer supplies an exact five-row repair inside its own coordinates. The claim that the complete selected witness formally verifies one coherent Appendix A construction is therefore not established until the cross-layer correspondence and staging are made explicit and proved.

That is already a valid counter-result against the stronger public claim of direct formal verification. The next decisive task is to either locate the missing bridge or prove that the selected witness depends on the mismatched coordinates without any valid conversion. Only the latter would justify escalating from “formal correspondence failure” to “the final theorem is false or unproved”.

## 8. A formal consequence of the selected force construction

The source-level review yields an additional proposition that clarifies the nature of the claimed singularity. `CandidateConsequences.lean` derives, from `CandidateProperties u p f`, the existence of a time `t` with `0 < t < 1` and a spatial point `x` at which `f (t,x) ≠ 0`. The review probe `ForceActivityProbe.lean` restates this implication independently at the candidate interface.

This result matters because it rules out an interpretation of the witness as an autonomous collapse occurring after an external driver has been removed. The force is active during the pre-singular interval. It is nevertheless not a contradiction of alternatives (C) or (D): the official formulation permits a smooth external force, and the accompanying paper itself defines the force from the momentum residual of the constructed fields. The correct conclusion is therefore semantic and mechanistic. The construction is continuously forced; it is not an unforced Navier–Stokes blow-up proof.

## 9. Status of the adverse result

The counter-paper's strongest formal result remains the moment-interface obstruction. The repository has three relevant layers: paper-shaped profile moments, an exact positive-order five-coordinate repair, and a physical rank interface with a three-coordinate residual debt. The checked direct bridge between the nominal and physical declarations is impossible, while the positive-order repair is exact within its own coordinates. Consequently, the public claim that the full Lean development verifies one coherent Appendix A construction is not established by the current source map. This is a failure of demonstrated formal correspondence, not yet a contradiction of the final C/D existential theorem.

The distinction is essential. Kernel acceptance establishes the declared proposition. It does not supply a missing change of variables, prove that differently indexed debts have the same physical meaning, or convert a residual-defined force into an autonomous evolution. A future revision could close the gap by exposing those maps and proving their preservation properties. Until then, the appropriate scientific verdict is that the repository contains a substantial formal C/D-shaped result but has not demonstrated the stronger claim made for the complete paper-to-code correspondence.

## Reproducibility record

- Source snapshot under review: OpenAI Navier–Stokes repository, commit `f9e8bc5` as recorded in the review materials.
- Review branch: `review/cmi-first-navier-stokes-2026-09-22`.
- Kernel environment: the repository-declared Lean `4.34.0-rc2` via `C:\Users\Admin\.elan\bin\lake.exe`; the separate V-lab `packages-4.32` cache was not used for this source snapshot because its manifest pins Lean 4.34.0-rc2.
- New zero-sorry probes: `NavierStokesReview/src/probes/MomentCoordinateMismatchProbe.lean`, `MomentBridgeObstructionProbe.lean`, `FiveRowsStructureProbe.lean`, `SelectedDependencyAxiomProbe.lean`, the corrected `MainAxiomProbe.lean`, and the compiled `ForceActivityProbe.lean`.
- No source file in the OpenAI construction was edited.
