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
| The local paper theorem and exported R³ candidate are automatically the same realised object. | Compare `LocalPaperTheorem`, `PaperLocalization`, and `ActualCandidateAssembly.selected_witness`. | Not established by the inspected signatures. Local velocity/pressure agreement is present, but force equality and five-moment transport are not stated together. |

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

The pressure attack is likewise narrower than the supplied criticism claimed.
Compact pressure slices are present, but the selected comparison path derives
compact-test pressure-gradient identities from equal-residual comparison
hypotheses and constructs pressure-flux bounds internally. No source-level or
zero-sorry probe proves that compact pressure support trivialises the velocity.
That narrow route is rejected. Separately, `PressureRecovery.Hypotheses` has no
absolute pressure-Poisson representative or normalisation; the zero-sorry
comparison probe accepts identical zero velocities and any common smooth
pressure. The selected `pressure_germ`, `base_equation`, and residual-limit
chain must therefore be connected to the paper's global pressure semantics
before this lane can be closed.

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

The selected-cycle source requires one further qualification. Its internal
`CycleAnalyticInvariant` includes and propagates a two-moment `masses` field;
the new zero-sorry completion exposes this for the selected cycle. The
remaining counter-paper issue is not that the recurrence lacks every mass
constraint, but that the source does not display the theorem identifying those
two radial identities with the paper's five quantities and carrying them into
the mixed `Witness` endpoint.

The proposed final collision test was also run against the literal source. It
does not turn the fixed correction rows into a selected-field energy theorem.
`FiveRowRank.five_rows` is inhabited for nonzero three-coordinate debt, while
`ActualCandidateAssembly.Witness` contains no debt or perturbation field. The
correction-state preservation theorems therefore cannot be combined with the
compact perturbation by type unification. The direct `False` route is rejected
as stated; the missing selected-path transport of the five paper moments is
still the load-bearing objection.

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
## Actual-field recomputation adjudication

The official construction requires each correction to be recomputed from the updated divergence-free field. The selected Lean path contains actual local velocity and pressure germs in `PhysicalFields`, carries them through `StateRealization`, and proves `StateRealization.chartIdentity`, which reconstructs the Cartesian residual from those actual fields. The stale-background objection is therefore not supported by the selected source path. This is a cleared attack surface, not evidence that the analytic estimates are independently correct.

## Filter adjudication

The generic `JetRate` interface remains vacuous on `Filter.bot` because it lacks a `NeBot` condition. The selected endpoint uses `GlobalBaseError.originPast`, a neighbourhood-within filter with explicit pre-singular and scale-limit lemmas. The selected rate proof is therefore not shown to be vacuous. The synthesis retains the generic API hazard while withdrawing any claim that it already refutes the endpoint.

## Formal synthesis update: 2026-09-23

The central adverse result is now formal rather than rhetorical. The paper's five-coordinate moment system and the repository's `FiveRowRank` system cannot be the same system under direct row identification: their exponent vectors differ, and their debt spaces have dimensions five and three. This is proved by `MomentBridgeObstructionProbe.lean` with no `sorry`.

The source also contains `PositiveOrderMoments.lean`, which proves an exact five-dimensional repair for a separate physical row system. That positive result prevents an overstatement in the opposite direction. The review has not shown that the endpoint lacks all five-row repair machinery; it has shown that the paper has not yet supplied the theorem connecting its named moments to the rows actually used by the selected endpoint.

The remaining claims are classified as follows:

- residual-defined forcing active through the singular interval: source-confirmed, but permitted by CMI alternatives (C) and (D);
- `JetRate` without a generic `NeBot`: a genuine interface vacuity hazard, not a demonstrated top-level exploit;
- challenge-file `sorry`: confirmed lexical facts, not endpoint dependencies;
- non-Newtonian or hypo-dissipative robustness: external physical scope, not a contradiction to the classical Newtonian theorem;
- division-by-zero failure: not supported by the inspected source.

The human-readable research paper and referee report now state these distinctions as arguments and findings rather than as a chronological work log.

## Correction: the reduced-form repair bridge

The previous synthesis treated the five-versus-three interface difference as the strongest adverse result. That interpretation is now narrowed. `FiveRowPositiveOrderBridgeProbe.lean` proves, with no `sorry`, that the physical repair functions are exactly the positive-order repair functions after promoting the three debts to `(0,0,-P,-Jθ,-Jz)`, and that the five weighted moments are exact for this promoted target.

The honest remaining criticism is therefore not that the repository has incompatible repair machinery. It is that the selected endpoint has not yet displayed the theorem connecting the paper's five named quantities to the promoted physical debt and showing that the correspondence is preserved through the actual witness and residual estimates.

## Selected import closure is not a bridge theorem

The selected theorem import closure contains both `PositiveOrderMoments` and `FiveRowRank`; this is verified by the zero-sorry `SelectedImportClosureProbe.lean`. That finding corrects any suggestion that the repository simply omitted the five-row layer.

The unresolved issue is more precise. The selected witness is assembled through `ActualCandidateAssembly.selected_witness` and the actual stage-estimate chain, yet the inspected endpoint has not exposed a theorem that identifies the paper's named five moments with the promoted physical debt and carries that identification into the residual estimates. The review should ask for that theorem, while avoiding the unsupported claim that the compiled endpoint is already contradicted.

The initial-face regularity objection is rejected. `Ico 0 1` includes zero, and relative `ContDiffOn` supplies the relevant half-domain regularity. It is removed from the adverse findings.

## Moment-system correction

The source does contain real integral moment machinery. `FiveRowRank.FiveRows` is a five-conjunct proposition whose first two conjuncts are explicit zero-moment integrals, and the associated repair theorems prove them. `CorrectionState` and `DefectIncrementBounds` contain bridges from actual slow base fields to those rows. `PositiveOrderMoments` independently defines a five-coordinate debt from actual radial integrals and proves exact repair.

The adverse claim must therefore be stated precisely. The current source trace does not show a theorem that transports those proved rows into the selected aliases used by `ActualCandidateAssembly.selected_witness`, nor a theorem equating them with the paper’s `(M, I, J, S, C_p)`. The issue is not that the rows are fake. It is that the selected endpoint’s public theorem type does not make the paper-to-code identification explicit. This remains a material correspondence gap and a live falsification target, but not a formal disproof by itself.

## Repository-wide admitted declarations

## Selected-path construction interface

The construction-interface audit changes the status of three proposed failure modes. The finite residual rates are fields of `StageEstimates`, but they are supplied on the actual path by `ActualCycleResidualBounds.finite_residual_rates`, which derives them from the cycle invariant and physical-field data. The diagonal schedule and vanishing residual jets are then derived by `StageEstimates.exists_schedule`. The force and its smoothness, PDE, energy, blow-up, and decay consequences are constructed by `CandidateConsequences.mixed_exists_force_with_consequences`.

The localisation objection is also narrower than initially stated. The selected velocity localisation is curl-generated and has an explicit divergence-free theorem, while the residual argument uses local equality. The cone-preservation step receives a derived coefficient bound from the modulated repair family. The source therefore does not support the claim that these three properties are obtained by simply assuming the desired endpoint.

The synthesis now separates two conclusions. The repository and the official exposition still contain material overclaims: the source tree is not globally admitted-free, and the paper does not yet expose a complete named-moment transport theorem. Those findings justify major revision and continued correspondence review. They do not, on their own, falsify the selected forced C/D theorem. A formal counterexample remains contingent on a contradiction in the actual selected dependency path.

The source census must be stated precisely. There are four `sorry` declarations in the repository's `ComparatorChallenges` area: two in `ComparatorChallenges/NavierStokes.lean` and two in `ComparatorChallenges/Euler.lean`. The Navier–Stokes challenge file identifies them as standalone challenge placeholders, and the selected R³ endpoint does not import that module.

This yields a two-level conclusion. The repository is not globally zero-sorry, so an unqualified claim of complete source-level derivation is false. Separately, the inspected selected endpoint remains standard-axiom-only, so the census does not by itself prove that the C/D theorem is false. The counter-paper records the former as a concrete integrity defect and keeps the latter as an open selected-path falsification target.
## Selected parameters: interpretation required by the source

The phrase “one closed choice fixes all three raw sequences together” corresponds in the Lean source to three definitions specialised to `selectedBudget`, `selectedThreshold`, and `selectedThreshold_geometry`. The definitions are not proof admissions. The selected budget is literally `0`, but it is an input to an infinite stage family, not the number of stages. The stage index remains `j : ℕ`.

This corrects an earlier possible overreading of the source. The review may still demand a theorem connecting the paper's named five moments to the promoted physical debt used by the endpoint, and it may test any paper statement requiring a positive budget. It should not claim that the selected aliases themselves are `sorry` cheats or that `B = 0` alone falsifies the C/D endpoint.

## Residual-invariant finding

The proposed hidden-final-premise objection was tested against the selected dependency path. `CycleAnalyticInvariant` contains component analytic fields and an exact residual decomposition. `ActualCycleResidualBounds.native_residual` derives the full native estimate from those fields, and `residual_jetRate` uses that derived estimate with the state-realisation and exterior bounds. This is materially different from inserting an unproved `native_residual` field into the invariant.

The objection is therefore cleared in its narrow form. The remaining concern is whether the formal component estimates and their promoted debt are the exact objects described by the paper, not whether the selected endpoint merely assumes its own residual theorem.

## Force-cutoff audit

The source corrects two competing narratives. First, the R³ wrapper does not use a discontinuous `if` cutoff: `PositiveTimeForce.timeCutoff` is a smooth bump, and the zero-sorry probe proves smooth endpoint activity. Second, the force is not an independently specified driver in the construction. `CandidateFromLimits.force` agrees with the activated momentum residual for all `0 ≤ t < 1` and is extended through the endpoint using locally uniform residual limits and a boundary-jet family.

This is a meaningful physical and explanatory criticism because the force is engineered from the candidate motion. It is not yet a formal failure of alternatives (C) or (D): the formal predicate asks for a globally smooth force, and the current source supplies a smooth-extension theorem. A valid disproof must show that the selected residual cannot meet those limits, or that the resulting force fails one of the explicit smoothness, support, or decay properties. The proposition suggested in the review notes with `sorry` cannot establish that result and is excluded from the evidence set.

## Force-conservation proposal: corrected scope

The suggested equal-and-opposite attack is useful as a physical diagnostic but not as an automatic CMI contradiction. The forced alternatives do not require the body force to have zero spatial integral or to be divergence-free. Internal action-reaction cancellation constrains internal stresses; an external body force can inject net momentum. Incompressibility constrains `u`, not necessarily `f`, because pressure can absorb a gradient component.

The source-level result is precise: `PositiveTimeForce.force` applies a smooth temporal bump, and `CandidateFromLimits.force` uses the activated residual before the singular time and a smooth endpoint extension. The next decisive test is consequently a zero-sorry failure of the selected residual limits or of an explicit force/PDE/energy predicate, not a generic momentum objection.

## Incompressibility audit

The raw `selectedPotentialStages` are not the final velocity field. The
selected construction forms its velocity through the solenoidal/curl-based
assembly, for which `SolenoidalDiagonal.divergence_velocitySum_on` proves zero
spatial divergence. The zero-sorry `SelectedDivergenceAudit.lean` probe
extracts the selected witness and returns its
`CandidateProperties.divergence_free` field. Therefore the proposed “raw
stages are not visibly divergence-free” argument is a semantic category error,
not a counterexample.

The endpoint remains open to audit for residual limits, force regularity,
finite energy, and the missing paper-to-code moment transport. Evidence:
`NavierStokesReview/evidence/selected_divergence_audit_2026-09-23.md`.

## External regularity evidence

The [Scientific American report](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/)
records expert criticism that the construction is a contrived forced branch
and that the force is central to the blow-up mechanism. That supports the
physical-provenance criticism, but the same report notes that the written Clay
formulation permits the forced alternative.

Constantin, Ignatova, and Vicol prove an external regularity theorem for an
analytic-forcing regime with the relevant anisotropic bounds and an exact
axisymmetric collapsing core. This is strong evidence against an autonomous
or robust physical interpretation, but it is not a direct CMI refutation
because the repository claims smooth compactly supported forcing, not analytic
forcing.

## Additional structural probes

The selected endpoint's final velocity is divergence-free through the
solenoidal construction; the raw potential stages are not the semantic object
on which the incompressibility predicate is imposed. This is proved on the
selected path by `SelectedDivergenceAudit.lean`.

The source also contains an exact Newtonian energy identity with forcing work
and viscous dissipation, and the selected witness exposes a uniform finite
energy bound. The energy-mismatch proposal therefore remains an open test, not
an established failure.

The selected R³ candidate explicitly imposes compact support on each pressure
slice via `CandidateProperties.pressure_support`. This is a serious
paper-to-code and whole-space modelling question. It becomes a formal
contradiction only if the review first proves the extra pressure Poisson
assumption that removes the arbitrary force contribution; CMI's forced
alternative does not supply that assumption. Temporal gluing is likewise
implemented by a smooth extension with endpoint jets, so the live target is the
selected residual-limit inputs, not a generic claim of stage kinks.

Evidence: `NavierStokesReview/src/probes/AnalyticObjectionsProbe.lean` and
`NavierStokesReview/results/analytic_objections_probe_2026-09-23.txt`.

The source tree also contains compiled compact-test pressure infrastructure,
and the selected comparison path uses it:
`ConservativeDifference.weak_pressure_poisson`,
`PressureRecoveryHelpers.gradient_poisson_test`,
`PressureRecovery.pressure_gradient_recovery`, and Riesz test identities. The
`WholeSpaceUniqueness` constructs the recovery hypotheses and pressure-flux
bound for the candidate-versus-competitor comparison. The remaining question
is the analytic validity of those estimates, not their selected-path
reachability. This is tracked as an analytic review target rather than a
completed contradiction.

## Filter-vacuity finding

The source distinguishes a generic API weakness from the selected path. `JetRate` has no `NeBot` guard, but `JointResidualLimits.past_filter_neBot` proves the one-sided endpoint filter used by the residual limit is non-vacuous. The zero-sorry probe records this at the selected origin. Any later restricted filter still needs a separate check.

## Counter-paper synthesis: transport and pressure

The new source trace refines the central objection. The production rank
engine is genuinely three-coordinate, but the repository also contains a
genuine five-coordinate positive-order repair. A zero-sorry probe verifies the
explicit promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)`. The adverse claim must
therefore target the missing semantic transport from the paper's five named
moments into the selected state, residual, and endpoint modules. A dimension
count alone is no longer sufficient.

The pressure route is likewise narrower. `pressure_support` is a compact
support inclusion in R³. `PressureRecovery` and `ActualPressureFlux` provide
comparison-level compact-test identities, and `WholeSpaceUniqueness` does
instantiate them for the selected candidate in the uniqueness comparison. A
zero-sorry probe proves compact support is not itself a zero-pressure
condition. This does not accept the authors' global pressure semantics: the
selected source still lacks a single paper-linked theorem connecting local
`StateRealization`/`chartIdentity` recovery to the global pressure object used
in the narrative. The counter-paper should inspect that bridge, while
avoiding the false statement that support alone trivialises pressure.

Evidence: `NavierStokesReview/evidence/semantic_transport_pressure_audit_2026-09-23.md`.

## Document-control conclusion

This synthesis is the controlled intake for supplied critiques and earlier
source reports. Its corrections take precedence over the stale parent verdict
and over unsupported summaries. The active document map is
[`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md).

## Global germ-transport recheck

The latest source pass confirms that the actual cycle, wave, chart, and residual
objects do reach the selected assembly. The correct criticism is therefore not
that globalisation is absent. It is that the final `Witness` does not export the
field-level theorem identifying those objects with the paper's five named
moments and their promoted rank representation. The fixed-force perturbation
result remains a selected-path provenance objection, not a contradiction of the
literal existential forced alternative.

The synthesis therefore carries forward the missing selected-path moment
transport as an open, load-bearing objection, while rejecting the stronger
claims that the final field is globally pure axial, that compact pressure
support alone proves triviality, or that generic filter and force hazards have
already invalidated the selected theorem.

## Formal strengthening of the moment objection

The generic stage-estimate layer has now been tested by a zero-sorry
countermodel. `StageEstimates` admits identically zero velocity and pressure
stages with zero residual-rate data, while the same zero velocity is formally
not unbounded near time one. Thus the layer cannot be treated as a formal
encoding of the paper's five-moment repair or blow-up mechanism. This is a
confirmed interface failure, not yet a contradiction to the selected endpoint,
which supplies additional physical-data and origin-growth premises.

Evidence: `NavierStokesReview/evidence/stage_estimates_moment_blindness_2026-09-24.md`.

The companion theorem `interface_does_not_determine_five_debt` makes the
scope precise: the generic stage-rate record cannot determine an arbitrary
five-coordinate debt. This is stronger than a missing-name search, but it is
still not a contradiction to the selected witness, which adds concrete
construction premises. The required next result is a field-level transport
theorem, or a zero-sorry contradiction using those concrete premises.
## Selected force-origin composition

The selected-path force audit is now stronger than the generic residual
objection. `SelectedForceOriginCompositionProbe.lean` extracts the actual
selected witness and proves that late-time activation, periodic localisation,
and the selected joint residual jets give

$$
\lVert f(t,0)\rVert\to0\qquad(t\to1^-).
$$

The selected velocity still has unbounded origin speed. Thus the construction
contains residual cancellation, and velocity growth cannot be converted into
force growth without an additional lower-bound theorem. This closes the force
explosion route and leaves the five-moment and absolute-pressure transport
questions as the live formal objections.

Evidence: `NavierStokesReview/evidence/selected_force_origin_composition_2026-09-24.md`.

## Fixed-force perturbation and mirror checks

The fixed-force probe derives the exact homogeneous perturbation equation when
the same pressure and spacetime force are retained after replacing (u) by
(u+e). A nonzero defect rules out the perturbed field under that unchanged
force. The extension applies this to the positive-time force wrapper.

The structural duality probe separately verifies that negating a smooth force
preserves smoothness, reverses the local work pairing, and cancels pointwise
under superposition. It also proves that the same fields cannot satisfy both
the original and mirror residual equations where the force is nonzero.

These results formally support path dependence and the distinction between a
residual-designed field and a forward prescribed-force construction. They do
not prove that the selected schedule fails under an arbitrary perturbation, or
that the selected velocity solves the unforced equation after force
superposition. Those stronger conclusions require additional selected-path
theorems.

Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`;
`NavierStokesReview/evidence/mirror_force_symmetry_2026-09-24.md`.

## Closure census correction

The selected import closure was rerun rather than inferred from direct imports.
It reaches 507 local modules and contains substantive references to
`PositiveOrderMoments`, `FiveProfileMoments`, `FiveRowRank`, `physicalMoments`,
and `CorrectionState.debt`. The counter-paper therefore withdraws any claim
that the five-moment construction is absent or globally orphaned.

The sharper finding survives: the endpoint `Witness` type does not expose a
selected-field equality transporting the paper's five named moments into the
final mixed velocity, pressure, residual, force, or all-order residual-jet
premises. This is the live CTR-005 correspondence objection.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Selected-witness fixed-force result

The fixed-force objection has been instantiated on the actual selected field,
not only on an abstract smooth field. A compact divergence-free perturbation
has a nonzero residual defect at an interior origin point, so the selected
velocity and its perturbation cannot share the selected force. This is a precise
path-dependence result. It does not turn the literal existential endpoint into
`False`, because perturbation stability and causal force independence are not
fields of `CandidateProperties`.

Evidence: `NavierStokesReview/evidence/selected_witness_fixed_force_obstruction_2026-09-24.md`.

The selected-force provenance is now explicit in a zero-sorry extension:
`SelectedResidualProvenance.selected_candidate_force_is_residual_output`
extracts the exported witness and proves that its force equals the selected
residual on the whole pre-singular interval. This confirms the causal
provenance objection while preserving the formal boundary: the C/D endpoint
does not encode force independence, so the result is not a literal `False`.

## Whole-space uniqueness audit

The source also contains a genuine no-global-solution comparison chain. It
uses compact-test pressure recovery and a weighted energy estimate before
applying compact support and speed blow-up. The pressure-support predicate is
not itself a global Poisson contradiction, and the comparison argument leaves
absolute pressure normalisation implicit. The synthesis therefore keeps the
pressure and five-moment transport questions focused on selected-endpoint
semantics rather than alleging that the uniqueness machinery is absent.

Evidence: `NavierStokesReview/evidence/whole_space_uniqueness_audit_2026-09-24.md`.

## Fixed-force stability extension

The review-side extension defines an explicit stronger forward-data predicate
and proves that the selected candidate fails it under a smooth, compactly
supported, divergence-free perturbation with force and pressure held fixed.
This formalises the residual provenance concern. It does not change the
literal C/D endpoint, which contains no perturbation-stability or force-
independence premise.

Evidence: `NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md`.

## 2026-09-24 source-scope addition

The source's `ActivePair` type has a real empty/nonempty branch. A concrete
label is sufficient to produce an active pair at its own band, using the
four-band threshold and `CommonWindow.self_mem`. The selected endpoint still
does not export label-subtype inhabitance. This is retained as an interface
question, not described as a vacuity proof.

The follow-up zero-sorry probe adds an important separation. `LocalScheduleWitness.potentialSum`
is a `SolenoidalDiagonal.potentialSum` whose `tsum` is indexed by natural
stage numbers, not by `ActivePair`. Thus an empty active-pair hypothesis leaves
the output type inhabited and does not, by itself, make the diagonal limit an
empty-set limit. The unresolved item is specifically the missing theorem that
the selected primary-label subtype is inhabited.

The CMI force wording is tracked separately from the Lean endpoint. “Given,
externally applied force” supports the causal interpretation of the review,
while the formal C/D proposition contains no explicit independence predicate.
