# Independent peer review of the OpenAI Navier–Stokes formalisation

## Finding 18: base-profile geometry is not a one-component collapse

The reduced `(t, s, z)` profile is embedded into three Cartesian basis directions before spatial curl. The only proven zero is on the radial gauge anchor. No global zero-swirl theorem was found.

## Finding 19: the selected-interface bridge remains the real objection

The repository has genuine upstream five-moment repair algebra, but the generic finite-stage summation interface does not state that the selected stages preserve the paper's named moments through the final residual and force construction. This is a correspondence gap, not yet a zero-sorry contradiction.

The force boundary must also be quoted accurately: the zero-force branch starts at `t ≥ 2`, not `t ≥ 1`; `force_smooth` is conditional on residual-jet and extension premises.

## Recommendation

**Major revision.** The public Lean development contains a substantial formal endpoint for a forced whole-space breakdown statement, but the accompanying mathematical narrative is not yet shown to correspond to the actual source implementation. The most concrete issue is the mismatch between the paper's five cumulative moments and the repository's `FiveRowRank` debt system.

This recommendation is not based on compilation failure. It is based on a source-level and zero-sorry formal audit of the propositions, interfaces, and dependency path that compilation alone does not inspect.

## Materials and scope

The review targets commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd` in the fork branch `review/cmi-first-navier-stokes-2026-09-22`. The downloaded non-Git directory is treated as a historical comparison snapshot. No upstream source file was edited.

The audit separates four questions:

1. Does the code elaborate and kernel-check?
2. What exact proposition is exported?
3. Does the candidate construction prove the hypotheses consumed by that proposition?
4. Does the proposition match the paper and a CMI alternative?

## Positive evidence

The R3 endpoint is not an empty wrapper. `ProblemStatement.lean` defines explicit smoothness, support, divergence, PDE, initial-data, energy, and speed-growth predicates. `WholeSpaceUniqueness.lean` and `WholeSpaceComparisonClosure.lean` contain a real comparison chain for a global finite-energy competitor. The selected endpoint reports only the standard logical foundations `propext`, `Classical.choice`, and `Quot.sound`; the intentional challenge-file `sorry` declarations were not found on that endpoint path.

The construction also contains an actual-field route. `ActualStageEstimates`, `ActualMeanPhysicalData`, and the state-realisation lemmas pass the activated velocity and pressure fields into residual estimates rather than merely naming a stale nominal field. This removes one plausible but currently unsupported criticism.

## Findings requiring revision

### Finding 1: the paper-to-code moment correspondence is missing

The paper describes five cumulative quantities `(M, I, J, S, Cp)` and a five-parameter repair. `FiveRowRank.lean` defines `Debt := Fin 3 → ℝ`, uses three angular powers and two axial powers, and treats its first two rows as fixed zero-moment conditions. `MomentBridgeObstructionProbe.lean` proves that the paper-shaped exponent vectors cannot be directly equal to the `FiveRowRank` vectors and that the associated debt spaces have no linear equivalence.

This is not a stylistic discrepancy. It blocks the direct inference that the paper's five-equation Jacobian is the matrix verified by `FiveRowRank`.

### Finding 2: a separate five-dimensional repair does not close Finding 1

`PositiveOrderMoments.lean` defines `Debt := Fin 5 → ℝ` and proves an exact repair theorem for five physical rows. This is positive evidence that the source has a serious five-row mechanism. It does not establish that these rows are the paper's `(M, I, J, S, Cp)`, nor that this module is the repair consumed by the selected exported candidate. A correspondence theorem and endpoint dependency trace are required.

### Finding 3: regularity is not a substitute for moment tracing

`MovingFieldRowNonImplicationProbe.lean` formalises the relevant logical point: smooth moving fields need not satisfy the required row identities. Any paper passage that moves from smoothness or field reconstruction directly to zero angular debt must be supplemented by the missing integral identities and their use in the residual estimates.

### Finding 4: the force is active through the singular regime

`PositiveTimeForce.lean` uses a smooth cutoff that is still one on the interval containing the singular time. The force is residual-driven and remains active as the speed becomes unbounded. This defeats any stronger description of the result as an unforced or autonomous singularity.

It does not defeat CMI alternatives (C) or (D) by itself, because the official problem statement permits smooth forcing. The paper should state the result as a forced breakdown construction and should not imply a force-free result.

### Finding 5: the generic `JetRate` interface needs a non-vacuity contract

`JetRate` accepts an arbitrary filter without a `NeBot` premise. Over `Filter.bot`, its eventual bound is vacuous. The selected `originPast` route has a separate non-bottom proof, so this is not currently a demonstrated endpoint exploit. It is nevertheless a serious interface defect: future lemmas can silently prove rates on empty regions unless non-vacuity is made explicit or proved at every consumer.

### Finding 6: external regularisation objections must be labelled correctly

Non-Newtonian viscosity and hypo-dissipation are different equations. They are appropriate robustness questions, not internal failures of a formal theorem about the classical Newtonian equation. The paper and review should keep these objections in a separate physical-scope section.


## Technical objections and adjudication

### Moment-system objection

The original action-reaction objection was too strong. `FiveRowRank.FiveRows` is an explicit conjunction of five radial integral identities, including the two zero-moment rows. `five_rows`, `CorrectionState.rank_rows_on_patch`, and `DefectIncrementBounds.RankGeometry.fiveRows` prove or transport those equations for the rank subsystem. `PositiveOrderMoments` separately defines five integral moments and proves exact repair.

The remaining issue is endpoint correspondence. The selected witness does not expose a theorem identifying its actual stage fields with `FiveRows`, `PositiveOrderMoments.moments`, or the paper tuple `(M, I, J, S, C_p)`. This is a material reproducibility gap, not evidence that the first two rows were merely inserted by type definition.

### Force regularity and residual provenance

The force remains active at `t = 1`, but `PositiveTimeForce.timeCutoff` is a smooth bump and `timeCutoff_contDiff` proves global smoothness. The source does not support a discontinuous-cutoff objection. `CandidateFromLimits.force` agrees with the activated residual for `0 ≤ t < 1` and obtains its global smooth extension from locally uniform residual limits and boundary jets. This confirms a posteriori force engineering, but does not prove force divergence. A valid adverse result must show, without `sorry`, that the selected residual fails those endpoint limits or that the resulting force violates smoothness, support, or decay.

## Questions the authors must answer

1. Where is the theorem identifying the paper's five quantities with the exact rows used by the selected candidate?
2. Which exported theorem consumes `PositiveOrderMoments.moments_repair`, if it is intended to be the implementation of Appendix A?
3. Where are the two fixed zero-moment rows proved for the actual activated field, rather than merely imposed in the row type?
4. Which theorem prevents every `JetRate` consumer from using `Filter.bot` vacuously?
5. Does the paper claim autonomous blow-up, or only a forced CMI alternative? The source supports only the latter description.

## Final assessment

The formal endpoint should not be dismissed as a mere compile illusion. Conversely, a clean endpoint axiom report does not verify the paper's construction line by line. The current evidence supports a **major-revision** decision: the authors have a formal C/D-shaped endpoint and substantial construction machinery, while the paper's endpoint-level five-moment transport remains unproved at the source level. The review does not yet possess a zero-sorry theorem showing that the exported endpoint is false.

## Review artefacts

- `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean`
- `NavierStokesReview/src/probes/FiveRowsStructureProbe.lean`
- `NavierStokesReview/src/probes/MovingFieldRowNonImplicationProbe.lean`
- `NavierStokesReview/src/probes/ForceActivityProbe.lean`
- `NavierStokesReview/src/probes/OriginPastNeBotProbe.lean`
- `OpenAI_NavierStokes_Axiom_Ledger.md`

## Correction to the moment finding

The initial wording treated the dimension and exponent mismatch as the strongest adverse result. That wording was too strong. `FiveRowPositiveOrderBridgeProbe.lean` now proves, without `sorry`, that the positive-order repair and the physical-rank repair agree after promoting `(P, Jθ, Jz)` to `(0, 0, -P, -Jθ, -Jz)`. The probe also proves the exact five weighted moments for that promoted repair.

The review therefore withdraws any suggestion that `FiveRowRank` is inconsistent with the five-row repair. The remaining major-revision issue is endpoint transport: the source must show that `CorrectionState.debt`, `ZeroMasses`, and `RankGeometry.fiveRows` carry the paper's named `(M, I, J, S, C_p)` quantities into the actual selected witness and residual estimates. Without that theorem, the public paper-to-code correspondence remains unestablished. This is narrower than a formal refutation.

## Finding 8: import availability does not establish paper-to-endpoint transport

`SelectedImportClosureProbe.lean` imports `NavierStokes.R3.Theorem` and resolves both `PositiveOrderMoments.Debt` and `FiveRowRank.Debt`. The repository therefore contains, and the selected import closure can see, both moment layers.

That positive fact does not close the review. The selected witness is assembled through `ActualCandidateAssembly.selected_witness`, the actual stage estimates, and the germ endpoint. The inspected source still lacks a named theorem that identifies the paper's `(M,I,J,S,Cp)` with the promoted physical debt and proves that the identity is preserved in the fields used by the residual estimates. This is a correspondence obligation. It is not a zero-sorry contradiction.

## Withdrawn objection: initial-face regularity

The earlier claim that `ContDiffOn` only covers `0 < t < 1` was incorrect. `preSingularDomain` is `Ico 0 1 × univ`, including `t = 0`, and the source specifies relative half-domain smoothness. This objection is withdrawn and must not be used as evidence against the endpoint.

## Finding 7: the repository is not globally zero-sorry

A repository-wide source census finds four admitted declarations in `ComparatorChallenges`: two in `ComparatorChallenges/NavierStokes.lean` and two in `ComparatorChallenges/Euler.lean`. This directly contradicts any unqualified statement that every Lean source file in the repository is fully derived.

The finding must not be inflated. The challenge module is marked as a standalone comparator with intentional placeholders, and the inspected dependency reports for the exported R³ theorem and selected witness do not include it. The correct peer-review demand is therefore disclosure and scope separation: identify the challenge files as admitted, and do not use their existence either to dismiss the selected endpoint automatically or to claim repository-wide zero-sorry verification.

## Finding 9: the selected convergence interface is derived

The earlier review required a direct audit of the construction interface before treating the endpoint as an illusion of proof. That audit has now been performed. `StageEstimates` does not contain an unconstrained “infinite residual is flat” field. It contains finite-prefix smoothness and jet-rate bounds. `ActualCycleResidualBounds.finite_residual_rates` derives the finite residual rates from the actual cycle invariant and `PhysicalData`; `StageEstimates.exists_schedule` derives the scale schedule and vanishing joint residual jets; and `CandidateConsequences.mixed_exists_force_with_consequences` constructs the force and derives the candidate consequences.

The same audit found that the spatial localisation is curl-based and accompanied by a divergence-free theorem, while the quantitative moment-repair path derives the coefficient smallness used by `ModulatedCone.profiles_trueCone`. The proposed objections that convergence, incompressibility after localisation, or cone preservation were merely asserted are therefore not supported by the selected source.

This finding does not certify the underlying analysis outside Lean. It does establish the correct review boundary: the remaining correspondence criticism concerns whether the formal symbols are adequately identified with the paper's named moments and physical interpretation, not whether the selected endpoint simply assumes its own conclusion.


## Finding 10: selected aliases are not admitted proofs

The block at `ActualCandidateAssembly.lean:1163-1181` defines three selected stage sequences and proves `selected_witness` for the selected parameters. The supporting construction sets `selectedBudget := 0` and proves the selected threshold inequality. These facts are unusual enough to audit, but they do not constitute `sorry` placeholders: the aliases have definitions, the geometric condition is a theorem, and the endpoint witness is obtained through the actual witness chain.

The zero-sorry `SelectedBudgetProbe.lean` confirms the literal parameter facts. It also clarifies the key distinction: `B = 0` is not a zero-stage construction because the raw sequences remain indexed by `j : ℕ`. The review should now ask whether the paper requires a positive budget or another quantitative condition that the selected endpoint fails to expose. In the absence of that comparison, this issue is not a formal refutation.

The earlier trivial transport probe has been removed from the evidence set. It constructed arbitrary existential scalars and therefore did not prove that the paper-to-code transport theorem is false.

## Finding 11: the native residual bound is not an inserted invariant field

The selected residual path was traced through `CycleAnalyticInvariant`, `ActualCycleResidualBounds.native_residual`, and `residual_jetRate`. The invariant stores component estimates and a residual decomposition. The native bound is derived by combining the mean, base, alias, Gaussian, and source estimates, after which the jet-rate theorem consumes the derived bound alongside state-realisation and exterior estimates.

This clears the specific allegation that the endpoint declares its final residual estimate as an unproved invariant field. It does not settle whether the formal estimates capture the paper's intended analysis or whether the named five moments are transported into the selected debt system. Those remain correspondence questions.

## Finding 12: the zero-row accusation is false, but the selected moment bridge is not shown

The suggested Newton’s-third-law objection was tested at source level. `FiveRowRank.FiveRows` is not a record that declares the first two rows zero by construction. It is a conjunction of five explicit radial integral equations. `five_rows`, `rank_rows_on_patch`, and `RankGeometry.fiveRows` prove or transport those equations for the rank subsystem. `PositiveOrderMoments` also contains a genuine five-coordinate integral repair theorem.

The remaining criticism is stronger when stated narrowly. `ActualCandidateAssembly.selected_witness` returns `Witness` over three raw stage sequences and the downstream schedule, force, blow-up, decay, and boundary properties. The selected endpoint does not expose a theorem identifying those stage fields with `FiveRowRank.FiveRows`, `PositiveOrderMoments.moments`, or the paper’s five named quantities. The zero-sorry `SelectedMomentBridgeAudit.lean` probe records this type boundary.

This is a material correspondence and reproducibility defect. It is not yet a formal disproof, because an absent public bridge does not establish that no transitive theorem can be supplied. The review should require that bridge, and should escalate only after a false required equality or a zero-sorry countermodel is produced.

## Finding 13: the cutoff is smooth, active, and residual-driven

The proposed cutoff loophole was inspected in the actual R³ implementation. `PositiveTimeForce.timeCutoff` is a rescaled smooth bump with `ContDiff ℝ ∞` regularity. It is equal to one on `[3/8,1]`, so the force remains active through the singular time, but it is not discontinuous at `t = 1`. `ForceActivityProbe.lean` compiles the endpoint value and continuity claims without `sorry`.

The residual concern survives in a narrower form. `CandidateFromLimits.force` agrees with the activated Navier–Stokes residual before one and uses a smooth extension at the endpoint. The extension depends on locally uniform residual limits and boundary jets constructed upstream. This confirms a posteriori force engineering, but it does not prove that the force diverges. Blow-up of the velocity alone is insufficient to infer blow-up of the residual because cancellation is possible and is precisely what the extension obligations address.

The appropriate review demand is therefore a zero-sorry proof that the selected residual fails the required endpoint limits or that the selected force fails global smoothness, compact positive-time support, or decay. Until such a result exists, this is a physical interpretation and proof-obligation concern, not a formal C/D refutation.

## Revised recommendation

The recommendation remains **major revision**, but for narrower reasons. The repository-wide zero-sorry claim is false because four challenge-file declarations are admitted, and the paper does not yet present a source-linked theorem mapping all named paper moments into the selected endpoint. Those are material reproducibility and correspondence defects. They are not a formal disproof of the selected C/D theorem. The review must not state otherwise without a new contradiction on the endpoint dependency path.

## Physical realizability verdict: force-conservation proposal

The proposed counter-argument asks whether Newton's third law forces

\[
\int_{\mathbb R^3} f(x,t)\,dx=0
\quad\text{and}\quad
\nabla\cdot f=0.
\]

Those conditions cannot be used as CMI disproof criteria without an additional theorem or admissibility assumption. In the forced alternatives, the external body force is not an internal stress. It may inject net momentum, and incompressibility is imposed on the velocity field rather than on the body force. The repository's `CandidateProperties` likewise requires force smoothness, positive-time support, rapid decay, the Navier–Stokes residual identity, and the stated energy/blow-up consequences, but not either proposed conservation identity.

The code inspection also answers the implementation question. `PositiveTimeForce.force` contains no pressure gradient; it is only `timeCutoff z.1 • f z`. The pressure gradient enters through `navierStokesResidual` in `CandidateFromLimits.force`, which agrees with the activated residual before `t = 1` and is smoothly extended at the endpoint. Therefore the proposed momentum/divergence test does not refute the formal C/D proposition. It remains a legitimate physical-provenance concern because the force is selected from the candidate residual.

**Verdict:** the proposed conservation trap is not an ironclad counterexample. The live formal target is to prove, without `sorry`, that the selected residual cannot have the endpoint limits or force predicates required by the code. Evidence: `NavierStokesReview/evidence/force_conservation_obstruction_adjudication_2026-09-23.md`.

## Finding 14: the selected endpoint is divergence-free

The proposed direct test of `selectedPotentialStages` targets the wrong object.
Those are intermediate potential fields. The final velocity is produced by the
solenoidal construction, and `CandidateProperties` requires its divergence to
vanish on `0 < t < 1`. The zero-sorry probe
`SelectedDivergenceAudit.lean` imports the selected endpoint and extracts that
property directly as `hc.divergence_free`.

This closes the raw-stage incompressibility objection. It does not validate the
analytic estimates or the paper's moment correspondence, and it does not close
the remaining endpoint residual audit.

## Finding 15: pressure support, energy, and temporal gluing require narrower claims

The source does explicitly give compact spatial support to each pre-singular
pressure slice through `CandidateProperties.pressure_support`, and the selected
endpoint exposes that field. It also contains an exact viscous energy identity
in `R3/ViscousEnergyBalance.lean` and a derivative form in
`R3/CompactEnergy.lean`, with the expected forcing-work and Laplacian
dissipation terms. The zero-sorry `AnalyticObjectionsProbe.lean` confirms that
the selected endpoint exposes pressure support, finite energy, and global force
smoothness.

These facts support a serious modelling objection: the paper must explain why
its compact pressure localisation represents the intended whole-space pressure,
and it must show where the exact energy identity is applied to the selected
fields. They do not yet establish a CMI contradiction. With an arbitrary
external force, the pressure equation includes the force contribution, so the
usual force-free Riesz-transform argument cannot be applied without an
additional hypothesis such as `div f = 0`.

The temporal interface is likewise not visibly a kink: `CandidateFromLimits`
uses `SpacetimeGluing.smoothExtension` and records all endpoint derivatives via
`force_boundary_jets`. The remaining adverse test is whether the selected
dependency path actually supplies the required residual limits and jets, not
whether a stage switch is syntactically present.

## Pressure-support objection: narrowed finding

The selected R3 construction does compactly localise pressure: `SpatialLocalization.cutPressure` multiplies the pressure by a spatial cutoff, and `R3CompactCandidate.localized_pressure_tsupport` transfers that support to the candidate properties. This is a material paper-to-code question because whole-space pressure is ordinarily recovered through a non-local Poisson/Riesz relation.

The objection must be stated narrowly. The repository also contains compact-test pressure identities in `ConservativeDifference`, `PressureRecoveryHelpers`, `PressureRecovery`, and `RieszTestOperators`. Those results are comparison/recovery theorems with explicit hypotheses, and `WholeSpaceUniqueness.classical_uniqueness_on_Icc` constructs those hypotheses for the candidate-versus-competitor comparison. This removes the claim that the selected pressure path is disconnected. It still does not certify the analytic estimates merely because they compile, nor does it show a contradiction: the arbitrary external force can absorb a pressure-gradient residual unless an independent pressure or force constraint is proved.

## Filter-vacuity correction

The generic `JetRate` predicate does not carry a `NeBot` condition, so arbitrary-filter lemmas should not be presented as automatically non-vacuous. The selected endpoint is narrower than that generic interface: `JointResidualLimits.past_filter_neBot` proves the one-sided endpoint filter is non-vacuous, and `FilterNonVacuityAudit.lean` verifies the instantiation without `sorry`. The correct review statement is therefore “generic filter API hazard, selected endpoint not shown vacuous,” not “the main theorem is proved over `Filter.bot`.”

## Finding 16: the five-moment transport obligation remains open

The source does not support the strongest version of the earlier dimensional
objection. `FiveRowRank` uses a three-coordinate debt and fixes two correction
moments to zero, but `PositiveOrderMoments` contains a real five-coordinate
integral repair. The zero-sorry `FiveRowPositiveOrderBridgeProbe` verifies the
explicit promotion `(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)` and the resulting exact
five weighted identities.

That positive result does not clear the paper. The selected endpoint still
needs a source-linked theorem identifying the paper's `(M,I,J,S,C_p)` with the
promoted coordinates and carrying that identity into the actual state,
`StateRealization.chartIdentity`, residual estimates, and `selected_witness`.
The public `CandidateConsequences` bundle contains maximality, lifespan,
unboundedness, force nonzero, and force-jet decay, but no moment-realisation
field. This is the strongest current formal correspondence objection.

## Finding 17: pressure support does not by itself trivialise the candidate

The R³ candidate explicitly localises each pressure slice with
`SpatialLocalization.cutPressure`, and `CandidateProperties.pressure_support`
records containment in a compact set. The repository also has
`PressureRecovery`, `ActualPressureFlux`, compact-test Poisson identities, and
Riesz pairings. These modules are comparison infrastructure with explicit
equal-residual, smoothness, incompressibility, and energy premises; the
selected candidate enters them through `candidate_unique_on_Icc`.

The zero-sorry `SemanticTransportPressureProbe` proves that compact support
alone does not imply a scalar pressure slice is zero. Therefore the valid
review demand is to supply the missing selected-path pressure Poisson and
recovery bridge, not to assert a trivialisation loop without those premises.

**Peer-review assessment:** the paper-to-code moment correspondence remains
materially under-documented. The selected pressure-recovery comparison is
present, but its analytic estimates remain a legitimate inspection target.
Neither lane has yielded a zero-sorry contradiction of the claimed C/D
predicate.

## Technical Discrepancies

### The Semantic Firewall and the Orphaned Moment Specification
The repository achieves a flawlessly valid Lean 4 compilation by constructing a robust semantic firewall between the physical PDE evaluation and the algebraic moment constraints. The foundational modules, including the base profile (`TailGaugePotential`) and the residual bounds (`PhysicalResidualJetBounds`), contain mathematically sound, genuine 3D spatial evaluations. The theorem does not rely on dimension-dropping tricks or 'fake' 2D math; the underlying vectors interact dynamically in full 3D space, and the `radialNormalize_anchor` only regulates swirl on a precise line rather than annihilating the entire global 3D structure.

However, a critical divergence occurs at the final assembly boundary (`ActualCandidateAssembly.selected_witness`). The proof evaluates PDE correctness through direct geometric jet decay bounds (`NativeBounds` in `PhysicalResidualJetBounds.lean`). The selected assembly's transitive import closure does contain `FiveProfileMoments`, `FiveRowRank`, and `PositiveOrderMoments` through upstream construction modules, but the residual-realisation theorems inspected here do not expose those five-coordinate moment arrays $(M, I, J, S, C_p)$ as semantic premises or prove their identification with the selected residual.

Consequently, while the repository's modules are internally valid and satisfy the mechanical requirements of the type checker, the existential abstraction boundary leaves the paper's primary physical proof strategy semantically unconnected on the inspected endpoint. The five-moment machinery exists upstream, but the final theorem does not visibly transport the paper's named quantities through `StateRealization`, the residual estimates, and `selected_witness`. The claimed paper-to-code correspondence is therefore not established by the inspected source.

## Editorial control

This is the active human-readable review. Its evidence boundary and the status
of older notes are defined in [`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md).
It is intentionally not a chronological audit log: claims are stated with
their present status and linked evidence, while unresolved objections remain
explicitly unresolved.
