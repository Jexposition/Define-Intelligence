# Adverse Peer Review of the OpenAI Navier–Stokes Formalisation

## Recommendation

The public claim should be narrowed. The repository contains a substantial Lean theorem with the outer shape of alternatives (C) and (D), but the claim that the code verifies the analytic construction in the official paper is not established. The strongest formal adverse finding is a missing cross-layer correspondence at the load-bearing moment-repair interfaces. The source does contain an exact five-coordinate positive-order repair, so a direct coordinate mismatch is not by itself a refutation.

This review does not call the final existential proposition false merely because the force is residual-defined, because C/D permit smooth forcing. It also does not call the theorem invalid merely because a generic filter abstraction can be vacuous. Those arguments require stronger reachability proofs than are presently available.

## Claim under review

The official paper claims a smooth compactly supported force and a finite-time velocity blow-up, with a construction based on a five-equation cumulative radial moment repair. The Lean release presents `theorem_1_1` as a formal endpoint for the corresponding whole-space statement.

The relevant review standard is correspondence, not compilation alone:

1. every formal object used by the endpoint must match the mathematical object named in the paper;
2. every interface premise must be derived or explicitly justified;
3. the exported theorem must not hide a changed coordinate system without a proved bridge; and
4. any alleged contradiction must be demonstrated against the actual selected witness, not an obsolete filename or an unused lemma.

## Finding 1: the outer R³ statement is real

The source tree defines a genuine whole-space type in `NavierStokes/R3/ProblemStatement.lean`. It includes smoothness on the pre-singular domain, compact support in space, compact positive-time support for the force, zero initial velocity, incompressibility, the Newtonian equation, finite energy, and unbounded speed at time one. `NavierStokes/R3/Theorem.lean` exports the headline theorem.

This finding defeats the earlier objection that the release merely compiles a periodic toy. The adverse case must therefore attack the construction or an interface premise, not the existence of the R³ declaration.

## Finding 2: the source contains two five-moment interfaces

The official paper's Appendix A uses five named cumulative moments `(M, I, J, S, C_p)` and gives normalised power blocks `(0, -λ)` and `(1/2, -1/2 - λ, -3/2 - λ)`. The repository contains a matching declaration in `NavierStokes/FiveProfileMoments.lean`, where `b = -1/2 - λ` gives exactly those blocks. This is positive evidence and must be credited.

A separate physical rank interface in `NavierStokes/FiveRowRank.lean` declares

```lean
angularPowers lam := ![2, -2 - 2 * lam, -2 * lam]
axialPowers lam   := ![1, 1 - 2 * lam]
```

It defines `Debt` abstractly and proves five integral rows for localised increments. The actual assembly consumes those rows through `MeanRankUpdate`, including `physical_five_rows`, `prescribed_five_rows`, and `reserved_five_rows`. Other construction modules consume `FiveProfileMoments` directly. In addition, `PositiveOrderMoments` proves exact five-component repairs for the recursively constructed slow profiles, and `GlobalSlowProfiles.profiles_moments` proves their vanishing five-row moments. The review issue is therefore not absence of a five-row repair, but the semantic connection among these non-identical systems and the selected final fields.

`MomentCoordinateMismatchProbe.lean` proves both vector inequalities between `FiveRowRank` and `FiveProfileMoments` in Lean without admitted steps. The stronger `MomentBridgeObstructionProbe.lean` proves that no direct row-by-row bridge exists for any pair of real parameters. Thus the declarations are not definitionally the same. A valid rescaling might still exist, but no theorem mapping all five rows, debt coordinates, parameter choices, and coefficient normalisations was found in the inspected dependency path.

The same probe proves that `FiveRowRank.Debt` and `FiveProfileMoments.Debt` admit no linear equivalence: the former has three coordinates and the latter five. This rules out a full linear identification of the debt spaces. It does not rule out a constrained subspace, an embedding, or a deliberate separation of construction stages. Those alternatives must be made explicit and proved if they are the intended bridge.

The selected-witness trace is concrete. `ActualCandidateAssembly.selected_witness` consumes `estimates`; those estimates are constructed by `GluedStageEstimates.actualStageEstimates` from a `PhysicalData` family. The physical prefix and reserved-patch route uses `MeanRankUpdate` and `FiveRowRank`; the nominal and modulation route uses `NominalProfile`, `ModulatedHistories`, `ReservedPatches`, and `FiveProfileMoments`; and the recursive slow-profile route uses `PositiveOrderMoments` through `GlobalSlowProfiles`. `SelectedDependencyAxiomProbe.lean` shows that the inspected interfaces are kernel-accepted using only standard axioms. That result removes custom-axiom speculation, but it does not supply a single theorem explaining the cross-layer correspondence.

This is a cross-layer correspondence gap. It invalidates the sentence “the complete Lean pipeline verifies the paper's Appendix A moment system” unless the authors supply the staging and correspondence account. It does not by itself disprove the abstract Lean endpoint, and it does not justify saying that the repository lacks an exact five-equation repair.

## Finding 3: kernel axioms do not expose a custom assumption

The corrected `MainAxiomProbe.lean` prints axioms for the headline theorem, the initial-rest theorem, and the endpoint proposition. Each reports only `propext`, `Classical.choice`, and `Quot.sound`. The result is important in both directions: it rules out a visible custom axiom at the endpoint, but it cannot establish that the formal definitions carry the intended PDE meaning.

## Finding 4: filter degeneration is a live hazard, not yet a fatal result

`JetRate` does not require `NeBot`, and `JetRateVacuityProbe.lean` formally demonstrates the generic `Filter.bot` vacuity. This warrants an audit of all rate obligations. The selected base-error path uses `GlobalBaseError.originPast` and concrete neighbourhood lemmas, so a global refutation requires proving that a bot filter reaches a mandatory premise of `selected_witness` or the exported theorem. The current evidence supports “hazard requiring a reachability audit”, not “headline theorem refuted”.

## Finding 5: force timing is a semantic criticism, not a C/D contradiction

The force is constructed a posteriori as a residual and remains active through the collapse. This undermines any description of the event as an autonomous or spontaneous blow-up. It does not violate the literal C/D alternatives if the force is smooth, compactly supported in the required sense, and decays as stipulated. The review must therefore separate the following claims:

- literal C/D-shaped mathematical proposition: formally present;
- physical autonomy or robustness under altered stress laws: not established by this construction;
- direct verification of the published five-moment construction: not established and presently contradicted at the coordinate-declaration level.

## Required author response

The authors should publish a correspondence appendix containing:

1. the exact map from `(M, I, J, S, C_p)` to `Debt` and `FiveRows`;
2. the change of variables taking the paper's exponent blocks to `angularPowers` and `axialPowers`;
3. the proof that all bump functions and moment equations are preserved by that map;
4. a theorem showing that the mapped rows are consumed by the selected whole-space witness; and
5. `#print axioms` and dependency output for those bridge theorems.

Until that appendix exists, the defensible answer is: the repository proves a C/D-shaped Lean proposition, but the claimed proof of the published construction has not been demonstrated.

## Final assessment

The release is evidence of a machine-checked proposition. It is not yet evidence that the official analytic proof has been faithfully formalised. The five-row coordinate mismatch supplies an honest counter-result to the stronger correspondence claim. The final C/D proposition remains unresolved until the missing bridge is either supplied or shown impossible along the selected witness path.
