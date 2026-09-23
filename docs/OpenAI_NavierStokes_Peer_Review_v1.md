# Adverse Peer Review of the OpenAI Navier–Stokes Formalisation

*Referee report. Source snapshot: OpenAI Navier–Stokes repository, commit `f9e8bc5`.*

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

## Finding 2: the R³ endpoint is connected to the selected witness

The source trace closes a second possible objection. `NavierStokes/R3/Theorem.lean` obtains the viscosity-one fields from `ActualCandidateAssembly.selected_witness`. `R3/ActualCandidate.lean` applies the proved spatial localisation and positive-time force cutoff, then discharges the whole-space finite-energy bound with `CompactEnergy.uniform_finite_energy`. `R3/ViscosityScaling.lean` proves the residual transformation and transports the result to every positive viscosity.

Accordingly, the review cannot honestly describe the whole-space theorem as an unrelated wrapper. This positive result strengthens the remaining adverse finding: the question is whether the selected witness's internal moment interfaces have the physical meaning claimed in the paper, not whether the R³ endpoint is attached to the construction at all.

## Finding 3: the source contains three moment layers

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

## Finding 4: kernel axioms do not expose a custom assumption

The corrected `MainAxiomProbe.lean` prints axioms for the headline theorem, the initial-rest theorem, and the endpoint proposition. Each reports only `propext`, `Classical.choice`, and `Quot.sound`. The result is important in both directions: it rules out a visible custom axiom at the endpoint, but it cannot establish that the formal definitions carry the intended PDE meaning.

## Finding 5: filter degeneration is a live hazard, not yet a fatal result

`JetRate` does not require `NeBot`, and `JetRateVacuityProbe.lean` formally demonstrates the generic `Filter.bot` vacuity. This warrants an audit of all rate obligations. The selected base-error path uses `GlobalBaseError.originPast` and concrete neighbourhood lemmas, so a global refutation requires proving that a bot filter reaches a mandatory premise of `selected_witness` or the exported theorem. The current evidence supports “hazard requiring a reachability audit”, not “headline theorem refuted”.

## Finding 6: force timing is a semantic criticism, not a C/D contradiction

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

## Preliminary assessment

The review has two formal findings and one important correction. First, the force activity probe establishes that every candidate force is nonzero at some time before one. The construction is therefore forced throughout the approach to the singular time. This is relevant to interpretation, but the CMI C/D statement allows a smooth external force, so it is not a rejection criterion by itself.

Second, the moment audit establishes a narrower correspondence problem. The source contains a genuine paper-shaped five-moment layer and a genuine exact five-coordinate repair layer, but the physical rank interface is not directly equal to them. The zero-sorry bridge probe proves that the direct row-by-row identification is impossible. The authors must provide the missing transformation or explain the stage separation. Without that explanation, the stronger statement that the Lean tree formalises one coherent Appendix A construction remains unestablished.

The declaration-level audit also corrects the description of the physical rank file. `FiveRowRank.FiveRows` is not a generic five-by-five inverse: its debt is `Fin 3 → ℝ`, its first two rows are fixed zero-moment conditions, and its last three rows consume the three debt coordinates. `FiveRowsStructureProbe.lean` verifies this decomposition. The fixed rows may be legitimate invariants, so this correction does not refute the C/D endpoint. It does require the authors to identify the exact map from those two invariants and three residual rows to `(M, I, J, S, C_p)`.

The earlier periodic-endpoint objection is withdrawn. The repository does contain a periodic D-shaped endpoint, so absence of a named theorem is not evidence of failure. Likewise, the pressure-chain and bottom-filter concerns remain open review obligations unless a concrete false premise is shown to reach the exported endpoint.

## Finding 7: the imported-rate-bound objection is withdrawn

The whole-space comparison chain was checked against the stronger allegation that the final scalar rate estimate is simply accepted as an unproved premise. That allegation is not supported by the source. `WholeSpaceComparisonClosure.eq_of_pressure_flux_bound` constructs the rate bound internally through `ComparisonRateBound.exists_uniform_rate_bound`. Before that call, `WholeSpaceUniqueness.classical_uniqueness_on_Icc` constructs the pressure-flux estimate through `PressureFlux.exists_uniform_actual_pressure_flux_bound`, using a `PressureRecovery.Hypotheses` record assembled from smoothness, divergence, equation equality, and finite-energy assumptions.

This is a material correction to the adverse case. The comparison theorem still contains substantial analytic claims requiring mathematical review, especially pressure recovery on the whole space and the localised energy identities. However, the source does not expose the rate estimate as a free endpoint assumption. `R3ComparisonPremiseProbe.lean` records the internal construction. The correct status is “derivation under analytic review”, not “missing rate-bound premise”.

Recommendation: major revision of the formalisation claim and its explanatory paper. The code should expose the cross-layer maps, preserve the physical meaning of all five moments across those maps, and include a dependency-level proof that no vacuous filter enters a mandatory estimate. The current evidence does not justify calling the final C/D proposition disproved, but it does justify rejecting the stronger claim that compilation alone demonstrates faithful formalisation of the published construction.

## Finding 8: pressure recovery remains analytically load-bearing

The pressure route was inspected as a possible hidden-premise failure. `PressureRecovery.gradient_recovery_complex` obtains pointwise interior-time pressure-gradient identities from compact temporal tests and continuity. `HarmonicTestFunctionals.eq_zero_of_compact_harmonic` then uses an explicit Fourier Sobolev bound and weighted `L²` representation to eliminate the compactly harmonic remainder. `ActualPressureFlux` converts the recovered pairings into the cutoff pressure flux used by the energy estimate.

This inspection did not produce a zero-sorry contradiction or a custom-axiom defect. It also confirms that the scalar rate bound is constructed internally by `WholeSpaceComparisonClosure`, rather than being handed to the endpoint as a free premise. These are positive findings about the source structure, not independent validation of every analytic estimate. The pressure reconstruction and localised energy identity remain appropriate targets for specialist review, but they must not be described as absent or vacuous without further evidence.

The release is evidence of a machine-checked proposition. It is not yet evidence that the official analytic proof has been faithfully formalised. The five-row coordinate mismatch supplies an honest counter-result to the stronger correspondence claim. The final C/D proposition remains unresolved until the missing bridge is either supplied or shown impossible along the selected witness path.

## Finding 9: the preserved-mass objection does not reach the selected witness

The physical rank predicate has two fixed zero-moment rows. We tested the concrete failure mode in which those rows only preserve a nonzero initial mass. `ActualInitialization.initial_zeroMasses` proves that the selected initial state has the required zero masses, while the temporal and rank-stage interfaces preserve the invariant. `MomentInitializationProbe.lean` compiles that source theorem with no added assumptions.

This is a corrected objection, not a new rejection. It removes one possible contradiction to `FiveRowRank`. It does not supply the missing theorem relating the fixed rows and three debt coordinates to the five published quantities `(M, I, J, S, C_p)`, nor does it identify the positive-order repair with the physical-rank state. The correspondence finding therefore remains open at the cross-layer level, but this particular initialization attack is closed.

## Finding 10: the zero-sorry claim must be scoped to the exported path

Direct compilation of `ComparatorChallenges/NavierStokes.lean` emits two `declaration uses sorry` warnings, at its whole-space and periodic challenge theorem declarations. `NavierStokes/ComparatorSolution.lean` does not import that module; it imports the independent comparator definitions and the project’s own whole-space and periodic bridge theorems. The headline endpoint therefore remains free of that module’s admitted dependency according to its own axiom report.

This is not a refutation of the exported C/D theorem. It is a correction to the broader repository claim. “The selected endpoints compile with only standard Lean axioms” is supported. “The repository contains no admitted theorem bodies anywhere in its Lean source” is not supported by the source tree. The paper should use the first formulation and identify the excluded challenge file.

The selected estimate interface was also traced. `GluedStageEstimates.actualStageEstimates` receives a family of `PhysicalData` records, and `ActualPhysicalPrefixFields.physicalFields_all` constructs those records from smoothness, local germ agreement, pressure-germ agreement, and exterior equality. This is positive evidence against a disconnected-wrapper objection. It leaves the decisive cross-layer question unchanged: the source still needs to show how the nominal five moments, positive-order five-coordinate repair, and physical three-debt rank system encode the same published quantities.

## Finding 11: empty active-pair branches are not a demonstrated ex-falso failure

The particular-wave source uses `by_cases hne : Nonempty (ActivePair B N0)`. In the negative branch it proves that any member of `controlPatch l n k` would create an inhabitant of `ActivePair B N0`, so all local jet obligations on that patch are discharged because the patch is empty. In the positive branch it uses a surjection from `ℕ` onto the active-pair subtype and transports the selected estimates back to the original labels.

This is not, by itself, the claimed illusion of proof. The empty branch is a valid total definition for inactive data, and the displayed `False` is derived from an impossible patch-membership hypothesis. The remaining question is whether the selected endpoint requires the active subtype to be inhabited, or whether the slow-base route can establish the endpoint even if the particular-wave family contributes no points. That question remains open and is now a targeted reachability test. No formal refutation is recorded from this branch alone.

## Finding 12: an import is not a moment-system bridge

`MeanRankUpdate.lean` imports `FiveProfileMoments.lean`, but its source declarations use `FiveRowRank.Debt`, `FiveRowRank.FiveRows`, and the three-coordinate scaling maps. A direct source census finds no reference to the `FiveProfileMoments` namespace in that file. The import can provide general library material, but it does not establish that the nominal five-coordinate moment system is the system consumed by the physical rank update.

This is a concrete documentation and correspondence defect, not a kernel contradiction. The authors must point to an explicit theorem elsewhere that transports `(M,I,J,S,C_p)` into the physical three-debt interface while preserving the two fixed zero rows and the three residual rows. Until that theorem is identified on the selected dependency path, the paper’s claim of one continuous five-moment formalisation remains unsubstantiated.

## Finding 13: the selected closure contains the nominal layer, but support identities are not row transport

The import-only finding must not be widened into a claim that the selected construction never uses `FiveProfileMoments`. A recursive import census of `ActualCandidateAssembly` finds substantive nominal-layer uses in `NominalProfile`, `ModulatedHistories`, `ModulatedCone`, `ModulatedProfileAssembly`, `MatchingDebtBounds`, `RepairConeBounds`, and `ReservedPatches`. The presence of those modules is positive source evidence.

The inspected cross-use in `ReservedPatches` has a narrower meaning. `five_row_updates_supported` proves that the `FiveProfileMoments` bump functions are supported in the reserved windows. `radial_heated_fields` and its witness variants identify the heated field with a `FiveRowRank.background` profile. Neither result is a theorem equating the five nominal moment integrals with the five entries of `FiveRowRank.FiveRows`, nor does either result transfer the debt coordinates and coefficient normalisation into `MeanRankUpdate`.

The correct review finding is therefore: both moment languages occur on the selected closure, but the inspected source does not expose the row-transport theorem needed to claim that they encode one continuous implementation of `(M,I,J,S,C_p)`. This remains a formal correspondence failure in the paper-to-code claim. It is not yet a contradiction of the C/D endpoint, because absence of an identified theorem is not the same as a proved false mandatory premise.

## Finding 14: moving-field regularity is not the five-row equation

The review tested whether the generic interface used throughout the actual cycle already contains the physical moment identities. It does not. `GaugeMomentBalances.MovingField` requires smoothness, radial support, and periodicity. The zero-sorry `MovingFieldRowNonImplicationProbe.lean` constructs the zero moving field and chooses zero background fields, zero increments, and a constant nonzero debt. The regularity premise holds, but the third row of `FiveRowRank.FiveRows` becomes `0 = -1`, so the row predicate fails.

This is a genuine formal interface result, but its scope must be stated exactly. The selected physical rank route is not based on `MovingField` alone. `LocalRankDefect.RankGeometry.fiveRows` derives the five physical rows from the stronger rank-geometry model, including the background profile, nonzero coefficient and velocity data, interval geometry, and debt. The probe therefore does not refute the exported C/D theorem. It does refute any explanatory claim that smoothness, support, and periodicity by themselves verify the five-equation repair.

The authors must still identify the transport from the paper's five quantities `(M, I, J, S, C_p)` into the debt and background data supplied to `RankGeometry.fiveRows`. Without that map, the repository demonstrates a physical row solve at one interface and a paper-shaped five-moment repair at another, but not their asserted identity.

## Recommendation and conclusion

The submission requires major revision of its formalisation claim. The exported Lean theorem has the outer shape of alternatives (C) and (D), and the selected endpoint does not presently expose a custom axiom or an imported scalar rate bound. Those are positive findings.

The stronger claim, that the Lean development verifies the published five-moment construction, is not established. The source contains three distinct moment interfaces, and the direct nominal-to-physical identification is impossible by a zero-sorry Lean theorem. The exact positive-order repair prevents that result from being treated as a refutation of the endpoint, but it does not replace the missing transport theorem. The authors should provide that theorem, its dependency path into `selected_witness`, and its axiom report before the release is described as a faithful formal proof of the paper.
## Actual-field and filter adjudication

The selected endpoint was tested against two stronger objections. The paper requires each correction to be recomputed from the updated velocity. The selected source path contains `PhysicalFields.velocity_germ`, `PhysicalFields.pressure_germ`, `StateRealization`, and `StateRealization.chartIdentity`; these declarations identify the actual local fields and reconstruct the Cartesian residual from them. The stale-background objection is therefore not established on this path.

`DiagonalResidual.JetRate` is generically vacuous on `Filter.bot`, because it has no `NeBot` premise. The selected rate proof instead uses `GlobalBaseError.originPast`, a neighbourhood-within filter at the pre-singular endpoint, together with proved endpoint relations. This leaves a generic API hazard, but not a demonstrated vacuous proof of the selected endpoint.

Require an explicit theorem transporting `(M, I, J, S, C_p)` into the physical-rank rows used by the selected witness, and expert verification of the pressure and localised-energy estimates. Do not report the two cleared objections as a refutation. The present review rejects the stronger claim that compilation alone establishes complete paper-to-code fidelity, while leaving the truth of the exported C/D proposition formally unresolved.
