# Input Document Synthesis for the Navier–Stokes Counter-Paper

*Synthesis memorandum. This document consolidates supplied criticisms into evidence-backed propositions; it is not the research paper or the execution tracker.*

## Purpose

The supplied reports and notes are treated as proposed adverse hypotheses. They are not treated as evidence merely because they are detailed. Each proposition is compared with the official paper and then tested against the actual Lean source tree.

## Official paper claim

The local official PDF, `navier-stokes.pdf`, states a whole-space construction with a smooth compactly supported force, smooth velocity and pressure before time one, zero initial velocity, bounded kinetic energy, and unbounded velocity approaching time one. It then claims that a same-force global finite-energy solution cannot exist. Section 2 explicitly describes the force as the momentum residual of a chosen flow, and Appendix A presents a five-moment repair mechanism.

This matters because two common objections are too broad. First, residual forcing is not automatically forbidden by alternatives (C) and (D). Second, the repository's R³ endpoint is not merely a periodic declaration. The counter-paper must therefore attack the construction's interfaces.

## Adverse hypotheses and adjudication

| Input hypothesis | Source test | Present assessment |
| --- | --- | --- |
| The force remains active until blow-up. | Read the paper's residual construction and R³ force support definitions. | Supported. It is a physical autonomy criticism, not alone a C/D contradiction. |
| A force defined from the residual may absorb errors. | Inspect force definition and residual-smoothing obligations. | Valid concern. Requires checking that the residual is genuinely smooth and decaying, not assuming that residual definition proves it. |
| The five-equation system repairs `(M,I,J,S,C_p)`. | Compare Appendix A with `FiveProfileMoments`, `PositiveOrderMoments`, `FiveRowRank`, and `MeanRankUpdate`. | `FiveProfileMoments` matches the paper's normalised vectors; `PositiveOrderMoments` proves exact five-component repair for the recursive slow profiles; `FiveRowRank` is a distinct three-debt physical rank interface. `MomentBridgeObstructionProbe.lean` rules out only direct row-by-row identification, so the remaining issue is cross-layer correspondence. |
| `JetRate` may be vacuous over `Filter.bot`. | Compile `JetRateVacuityProbe.lean`; trace selected witness filters. | Generic hazard confirmed. Global failure remains unproved because concrete origin-past filters have non-vacuity witnesses. |
| Pressure, Leray projection, and whole-space bounds are absent. | Search actual source paths and inspect `WholeSpaceUniqueness`, pressure recovery, and breakdown modules. | Earlier filename-based criticism is unreliable. Actual modules exist; their analytic interfaces still require correspondence audit. |
| Division by zero invalidates the singular limit. | Search actual source for the claimed file and guarded denominators. | No division-by-zero failure has been established in the current snapshot. Do not repeat the old claim. |
| Ladyzhenskaya stress or fractional dissipation defeats the construction. | Compare those equations with the official Newtonian statement. | A robustness objection, not an internal contradiction of the stated C/D theorem. |
| Level A stress covariance is not Level B exact PDE realisation. | Trace all three moment layers into the selected candidate and force residual. | Correct audit distinction. The missing staging theorem between nominal, positive-order, and physical-rank interfaces is a concrete Level A to Level B correspondence target. |

## Source-to-paper map

| Paper object | Lean location | Review question |
| --- | --- | --- |
| C/D endpoint | `NavierStokes/R3/ProblemStatement.lean`, `R3/Theorem.lean` | Does the endpoint state the intended whole-space proposition? |
| Five cumulative moments | Official PDF Appendix A; `NavierStokes/FiveProfileMoments.lean`, `PositiveOrderMoments.lean`, `FiveRowRank.lean`, `MeanRankUpdate.lean` | Does one explicit staging map preserve the rows and coordinates? Direct equality of two interfaces is formally impossible; exact repair exists in the positive-order layer, but the complete cross-layer map remains unproved in the inspected source. |
| Mean-patch repair | `NavierStokes/MeanRankUpdate.lean` | Are the physical rows the paper's rows? |
| Selected witness | `NavierStokes/ActualCandidateAssembly.lean` | Does the selected witness consume the same repaired fields? |
| Whole-space endpoint provenance | `NavierStokes/R3/Theorem.lean`, `R3/ActualCandidate.lean`, `R3/ViscosityScaling.lean` | Is the R³ theorem connected to the selected witness, localisation, energy estimate, and viscosity scaling? Source inspection answers yes. |
| Pressure and comparison | `NavierStokes/R3/WholeSpaceUniqueness.lean`, pressure modules | Are the comparison premises derived from the candidate? |
| Rate and germ limits | `NavierStokes/ActualCycleResidualBounds.lean`, `JetRate` uses | Are all filters non-vacuous on the selected path? |

## Synthesis

The source review now supports a sharper synthesis than the initial critique set. The official paper does not claim that the force is switched off before the singularity. Its stated construction defines the force from the momentum residual and aims to extend it smoothly through the endpoint. The Lean consequence that the force is nonzero at some time in `(0,1)` therefore confirms the residual-driven mechanism, but does not violate alternatives (C) or (D).

The moment-system material also requires a two-sided account. `FiveProfileMoments` is paper-shaped and reproduces the stated normalised exponent vectors. `PositiveOrderMoments` proves an exact five-coordinate repair used by the recursive slow-profile construction. `FiveRowRank` is a separate physical-rank interface with a three-coordinate debt and two fixed constraints. The direct correspondence probe proves that the first and third declarations cannot be identified row by row. This is a genuine formalisation gap unless an explicit change of variables or stage-separation theorem is supplied. It is not evidence that all five-equation repair code is absent.

The resulting counter-paper position is deliberately tiered:

- kernel acceptance is established for the inspected endpoints;
- the C/D outer proposition is present in both whole-space and periodic routes;
- active forcing is formally established for the selected candidate;
- exact moment repair exists in at least one internal layer;
- the cross-layer physical meaning required by the public narrative remains unproved.

This synthesis is the boundary between evidence and conclusion. It prevents a true local objection from being inflated into a false claim that the final existential theorem has already been contradicted.

The notes correctly insist that compilation is not semantic validation and that Level A stress matching is not Level B exact PDE realisation. They overreach when they treat force activity, missing physical regularisations, or a generic `Filter.bot` possibility as immediate refutations of alternatives (C) and (D). The paper's strongest current counterclaim is narrower and formally supported: the repository contains a paper-shaped nominal module, an exact positive-order five-row repair, and a separate physical rank module. A zero-sorry Lean theorem rules out direct identification of the nominal and physical-rank exponent vectors, but the positive-order layer means this is not by itself a failure of the selected construction. The selected dependency axiom probe finds no custom axiom that would independently explain the interfaces. The remaining issue is whether the published claim is backed by explicit cross-layer staging and correspondence theorems.

The debt types sharpen the same point. The physical rank route exposes `Fin 3 → ℝ`, while the profile route exposes `Fin 5 → ℝ`; Lean proves that no linear equivalence exists between them. This does not establish that the construction is false, because a constrained embedding or stage distinction could be intended. It does establish that the published claim cannot be supported by silently treating the two debt interfaces as one full linear system.

The declaration-level audit adds an important qualification. `FiveRowRank.FiveRows` contains five displayed integral identities, but only its final three rows are debt-controlled. The first two are explicit zero constraints on the increment fields. `FiveRowsStructureProbe.lean` verifies this structure directly. Thus the honest criticism is not that Lean attempted an impossible arbitrary five-by-five solve; it is that the publication must explain how the two fixed invariants and three debt-controlled rows represent the paper's five named moments and how that representation is connected to the other two moment layers.

That finding is now carried consistently into the plan, ledger, tracker, peer review, and research paper.

The latest provenance check narrows the adverse case further. The R³ endpoint is source-connected to `ActualCandidateAssembly.selected_witness`; it is not a disconnected formal wrapper. The remaining formal objection is therefore not endpoint provenance but semantic transport: the selected path must explain how the several moment systems encode the same five published quantities.
## Comparison-premise correction

The whole-space comparison audit supplies a further correction. The scalar rate bound is not merely inserted at the final endpoint: `WholeSpaceComparisonClosure` derives it from `ComparisonRateBound.exists_uniform_rate_bound`, and `WholeSpaceUniqueness` derives the pressure-flux bound from the pressure-recovery hypotheses. This closes the specific objection that a free rate-bound premise is being consumed by the endpoint. The review must now test the pressure reconstruction and localised energy estimates themselves, with their exact hypotheses, rather than treating the rate-bound interface as missing.

## Preserved-mass test

The fixed zero rows in `FiveRowRank` cannot presently be criticised as preserving nonzero initial moments. `ActualInitialization.initial_zeroMasses` initializes the selected state with the two relevant masses equal to zero, and the correction interfaces preserve them. This closes a candidate contradiction against the physical-rank implementation. It leaves the substantive correspondence question intact: the repository still needs an explicit map across the nominal, positive-order, and physical-rank moment systems.

## Pressure-chain finding

The pressure and comparison modules were inspected as a possible source of a hidden premise. That proposed failure is not supported by the current source. `PressureRecovery` derives pointwise interior-time pressure-gradient identities from compact temporal tests, continuity, and a harmonic-functional argument. `ActualPressureFlux` derives the cutoff pressure flux from those identities. Finally, `WholeSpaceComparisonClosure` constructs the scalar rate bound internally rather than receiving it as an unexplained endpoint input.

This does not certify the analytic argument merely because Lean accepts it. It establishes the correct review category: the chain is a substantive mathematical derivation whose identities and estimates must be checked, not an obvious axiom or filter-vacuity defect. The strongest present counterclaim remains the missing demonstrated correspondence among the moment layers, together with the formally proved impossibility of a direct identification between the nominal and physical-rank interfaces.

## Source-scope qualification

The source census adds a narrower but concrete correction. `ComparatorChallenges/NavierStokes.lean` still contains two theorem bodies admitted by `sorry`, and direct compilation reports both warnings. That file is not imported by the exported solution, which instead uses the independent comparator definitions and project bridges. The correct synthesis is therefore not “all source files are zero-sorry” and not “the headline theorem depends on `sorryAx`.” It is: the selected endpoint is standard-axiom-only, while the repository also carries an unused challenge module with admitted declarations.

The selected witness is source-connected through `ActualCandidateAssembly.selected_witness` and `GluedStageEstimates.actualStageEstimates`, with `PhysicalData` derived from actual local field realisations and exterior agreement. The remaining adverse question is semantic transport across the moment layers, not endpoint provenance.

The empty-index audit adds a similar qualification to the filter-vacuity discussion. `ActualParticularStageControls.raw_jets` only uses empty elimination after a patch-membership hypothesis has produced an active-pair witness; it does not prove estimates on a known nonempty patch from an arbitrary contradiction. The nonempty branch explicitly enumerates active pairs. This closes the proposed ex-falso objection at that local interface, while leaving the endpoint-level question of whether the active subtype is required and inhabited.

The moment census also separates imports from bridges. `MeanRankUpdate.lean` imports `FiveProfileMoments.lean`, but its operative debt and row definitions are exclusively those of `FiveRowRank`; no `FiveProfileMoments` symbol is used there. The remaining correspondence claim therefore needs a named theorem outside that file. Without one, the source map shows adjacent moment layers, not a proved transport of the paper’s five quantities into the selected physical update.

The selected import closure does contain substantive nominal-layer code, so the synthesis must not call the five-moment system absent. `NominalProfile`, `ModulatedHistories`, `ModulatedCone`, `ModulatedProfileAssembly`, `MatchingDebtBounds`, `RepairConeBounds`, and `ReservedPatches` use `FiveProfileMoments`. The inspected `ReservedPatches` theorems prove support for the nominal bump functions and background agreement with `FiveRowRank`; they do not provide the full equality between `physicalMoments` and `FiveRows`, or the conversion from five nominal debts to the three physical debts. The honest counter-paper position is thus a missing selected-path transport theorem, not a claim that the repository contains no five-moment implementation.

## Regularity is not moment repair

The interface audit now has a compiled countermodel. `GaugeMomentBalances.MovingField` records smoothness, radial support, and periodicity only. `MovingFieldRowNonImplicationProbe.lean` proves that the zero field satisfies this predicate while a constant nonzero debt makes the third `FiveRowRank.FiveRows` identity impossible for zero background and zero increments. Therefore the generic moving-field assumptions cannot be used as a substitute for the moment equations.

The source does contain a stronger selected-path theorem: `LocalRankDefect.RankGeometry.fiveRows` obtains the physical rows from the rank geometry and the constructed rank increment. This changes the audit question from “is there any physical row solve?” to “does the rank geometry receive the same five published quantities repaired in the nominal and positive-order modules?” Until that transport is displayed, the paper-to-code correspondence remains unestablished, while the final C/D proposition remains formally unresolved rather than refuted.
