# Against the Claim of a Verified Navier–Stokes Blow-Up Proof

## Abstract

OpenAI's Navier–Stokes release presents a Lean 4 theorem intended to realise alternatives (C) and (D) of the Clay Mathematics Institute formulation. The repository does contain a substantial whole-space formal statement: it quantifies over smooth velocity, pressure, and force fields on R³, includes compact support and finite-energy conditions, and concludes finite-time unbounded speed. The theorem is not a periodic toy, and its exported proof currently reports only Lean's standard foundational axioms.

That result does not settle whether the Lean development formalises the analytic construction described in the accompanying paper. This paper develops an adverse but evidence-led finding. The repository contains both a `FiveProfileMoments` system whose normalised exponent vectors match the paper's Appendix A and a distinct `FiveRowRank` system whose vectors differ. The selected construction uses both families of modules. A zero-sorry Lean probe proves that the two source-level power-vector declarations are not definitionally equal. The unresolved load-bearing question is whether a proved bridge identifies their debts, rows, coefficients, and parameter normalisation along the selected witness path.

The immediate conclusion is therefore precise. The claim that the repository mechanically verifies the paper's Appendix A construction is not established, and the stronger claim of direct formal correspondence is contradicted by the checked coordinate declarations unless an additional change-of-variables theorem is supplied. This is a formal correspondence failure, not yet a contradiction of the final existential proposition itself. The paper also distinguishes genuine objections from arguments that do not work: an a posteriori force is allowed by alternatives (C) and (D), and a local `Filter.bot` hazard is not a global refutation unless it reaches the selected witness.

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

## 3. Two five-row systems and the missing bridge

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

The review probe `NavierStokesReview/src/probes/MomentCoordinateMismatchProbe.lean` proves, with no `sorry`,

```lean
FiveRowRank.angularPowers lam ≠
  FiveProfileMoments.angularPowers (-1 / 2 - lam)
FiveRowRank.axialPowers lam ≠
  FiveProfileMoments.axialPowers (-1 / 2 - lam)
```

The proof is elementary: evaluation at the first finite index reduces the first equality to `2 = (1/2 : ℝ)` for the angular vector and `1 = 0` for the axial vector. Lean checks this contradiction directly.

This does not show that a rescaling could never relate the two systems. It shows that no such relation is definitional. To claim that the combined pipeline verifies one coherent Appendix A system, the project must expose and prove the missing bridge, including the mapping of all five rows, the debt coordinates, the bump coefficients, and the parameter normalisation. The existence of `FiveProfileMoments` prevents the stronger claim that the paper-shaped system is absent. The adverse result is instead that the source contains two non-identical moment interfaces and the selected witness path has not yet been shown to preserve their meaning when it moves between modules.

The stronger `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean` packages the proposed direct correspondence as a Lean structure and proves

```lean
theorem no_direct_moment_bridge (lam b : ℝ) :
  ¬ DirectMomentBridge lam b
```

for arbitrary `lam` and `b`, not only for the paper's substitution. This is a formal obstruction to treating the two declarations as the same five-row system. It does not rule out a nontrivial analytic transformation, but that transformation must be stated and proved rather than inferred from compilation.

The dependency trace is load-bearing: `ActualCandidateAssembly.selected_witness` consumes `estimates`, which is constructed by `GluedStageEstimates.actualStageEstimates` from `ActualCycleResidualBounds.PhysicalData`. The physical prefix and reserved-patch route uses `MeanRankUpdate` and `FiveRowRank`, while the nominal and modulation route uses `NominalProfile`, `ModulatedHistories`, `ReservedPatches`, and `FiveProfileMoments`. The missing bridge is therefore a selected-path obligation, not merely a comparison of unused declarations.

## 4. Why other proposed objections are insufficient by themselves

The force is deliberately defined from the residual and remains active up to the singular time. That is a legitimate criticism of physical interpretation, but alternatives (C) and (D) explicitly allow a smooth external force. It therefore does not refute the stated C/D proposition.

The repository contains a `JetRate` abstraction without an explicit `NeBot` parameter. The review probe `JetRateVacuityProbe.lean` proves that a generic limit predicate over `Filter.bot` can be discharged vacuously. This identifies a real proof-engineering hazard. The selected path, however, uses the concrete `GlobalBaseError.originPast` filter and non-vacuous local neighbourhood lemmas. A fatal result requires tracing a bot filter into a mandatory premise of `selected_witness` or `theorem_1_1`; that reachability has not yet been proved.

Similarly, omitted Ladyzhenskaya stress laws and fractional dissipation are not contradictions to a Newtonian C/D theorem. They matter to claims of physical robustness, not to literal compliance with the stated Newtonian problem.

## 5. Axioms and kernel evidence

`#print axioms` on `theorem_1_1`, `theorem_1_1_with_initial_rest`, and `ProblemStatement.breakdownStatement` reports only `propext`, `Classical.choice`, and `Quot.sound`. This rules out the claim that the headline R³ endpoint visibly depends on a custom axiom. It does not prove that every analytic assertion in the source corresponds to the paper's intended mathematics. Foundational consistency and semantic correspondence are separate obligations.

The follow-up `SelectedDependencyAxiomProbe.lean` reports the same three standard axioms for `ActualCandidateAssembly.selected_witness`, `ActualCandidateAssembly.physicalData`, `GluedStageEstimates.actualStageEstimates`, and `ActualCycleResidualBounds.Invariant.residual_jetRate`. This is negative evidence against a hidden custom axiom at those interfaces. It is also why the adverse finding is stated as a missing correspondence theorem rather than as a claim that the kernel accepted an explicit `axiom` or `sorry`.

## 6. Conclusion

The honest adverse conclusion is not “Lean cannot prove this” and not “the force is illegal”. The checked evidence supports a narrower and stronger statement:

> The repository has a formally accepted C/D-shaped R³ endpoint, and it contains a paper-shaped `FiveProfileMoments` module. However, the claim that the complete selected witness formally verifies one coherent Appendix A construction is not established. The source also contains a distinct load-bearing `FiveRowRank` coordinate system, and the required bridge between the two systems has not yet been found.

That is already a valid counter-result against the stronger public claim of direct formal verification. The next decisive task is to either locate the missing bridge or prove that the selected witness depends on the mismatched coordinates without any valid conversion. Only the latter would justify escalating from “formal correspondence failure” to “the final theorem is false or unproved”.

## Reproducibility record

- Source snapshot under review: OpenAI Navier–Stokes repository, commit `f9e8bc5` as recorded in the review materials.
- Review branch: `review/cmi-first-navier-stokes-2026-09-22`.
- Kernel environment: Lean 4.32 via `C:\Users\Admin\.elan\bin\lake.exe`.
- New zero-sorry probes: `NavierStokesReview/src/probes/MomentCoordinateMismatchProbe.lean`, `MomentBridgeObstructionProbe.lean`, `SelectedDependencyAxiomProbe.lean`, and the corrected `MainAxiomProbe.lean`.
- No source file in the OpenAI construction was edited.
