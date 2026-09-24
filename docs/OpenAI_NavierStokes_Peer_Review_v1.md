# Independent peer review of the OpenAI Navier–Stokes formalisation

## Finding 18: base-profile geometry is not a one-component collapse

The reduced `(t, s, z)` profile is embedded into three Cartesian basis directions before spatial curl. The only proven zero is on the radial gauge anchor. No global zero-swirl theorem was found.

## Finding 19: the selected-interface bridge remains the real objection

The repository has genuine upstream five-moment repair algebra, but the generic finite-stage summation interface does not state that the selected stages preserve the paper's named moments through the final residual and force construction. This is a correspondence gap, not yet a zero-sorry contradiction.

The force boundary must also be quoted accurately: the zero-force branch starts at `t ≥ 2`, not `t ≥ 1`; `force_smooth` is conditional on residual-jet and extension premises.

## Finding 20: local and exported composition are not one exposed theorem

`LocalResidualFlatness` and `LocalPaperTheorem` work with the selected raw
stage aliases and a supplied schedule. The public whole-space endpoint is
instead extracted from `ActualCandidateAssembly.Witness` and then passed
through the R³ localisation layer. `PaperLocalization` proves local agreement
of velocity and pressure on an open set at late times, but the combined result
does not state equality of the forces or identify the five named moments with
the exported residual. The paper therefore needs an explicit composition
theorem before it can claim that its local five-moment construction is the
object used by the CMI endpoint.

This strengthens CTR-005 as a source-level correspondence objection. It does
not refute `selected_candidate` by itself.

## Finding 21: the compact-pressure attack does not replace the correspondence failure

The R³ candidate imposes compact support on each pre-singular pressure slice.
That condition is an adversarial audit target, but the inspected comparison
path does not simply set pressure to zero. `PressureRecovery` derives the
differentiated Poisson identity against compact tests from the residual
equations; `ActualPressureFlux` and `PressureFlux` turn it into the uniform
cutoff flux bound; and `WholeSpaceComparisonClosure` constructs the scalar rate
estimate internally. The intermediate axiom probe reports only standard Lean
foundations for these endpoints.

The claim that compact pressure support forces the candidate velocity to vanish
is therefore rejected as a standalone counterexample. It does not answer the
load-bearing objection: the selected-path theorem still does not identify the
paper's named moments and force with the fields consumed by the exported R³
endpoint. That correspondence claim remains unestablished.

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

The runtime audit also rules out an overstrong version of the objection. In
`MeanRankUpdate.lean`, `scaleDebt` carries three debt coordinates with explicit
length and velocity powers. In `FiveRowRank.lean`, the first two rows constrain
the correction functions `dv` and `ga`; they do not define total kinetic
energy. The source theorem `five_rows` constructs these corrections for
nonzero debt. The remaining issue is therefore transport into the selected
Cartesian field, not an immediate contradiction from clamped energy rows.

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

## Finding 12: the selected-witness falsification lane remains open

The earlier pressure discussion was too willing to treat a failed
trivialisation probe as a cleared hypothesis. That is corrected here. The R3
`CandidateProperties` record requires compact pressure support and a residual
identity, but it does not expose a global pressure-Poisson/Leray equation. The
force can therefore absorb the pressure gradient at the record level. This is
an unresolved semantic attack: the review must add the global elliptic premise
and test it against the selected pressure and velocity before deciding the
support/topology contradiction.

The force-jet attack remains equally active. `force_smooth` consumes a family
of residual-limit premises `hlim`; it does not derive those premises from the
velocity blow-up. The required proof is a selected-field lower bound showing
that the residual derivatives cannot have the endpoint jets used by the
gluing theorem.

Finally, `SelectedWitnessInhabitationProbe.lean` gives a zero-sorry
type-level countermodel: the inhabited `Witness` envelope can be paired with
an arbitrary nonzero five-debt payload because no such payload occurs in the
type. This proves that the envelope does not certify five-moment transport. It
does not yet prove the actual selected fields violate the moments, so the next
step is to add the missing field-level equality and attack it directly.


## Selected-path transport boundary

`ActualCandidateAssembly.Witness` packages the stage schedule, residual force,
periodic `CandidateProperties`, and endpoint consequences. The R3 theorem then
passes that package through `R3/ActualCandidate.of_localized_fields`. None of
these interfaces consumes an equality between the selected fields and
`PositiveOrderMoments.moments` or `FiveRowRank.FiveRows`. This is a load-bearing
transport omission, not yet a proof that the concrete fields fail those
moments. The active falsification task is to use the actual selected residual,
pressure, and origin data to derive `False`, rather than to treat a generic
type-level countermodel as field-level evidence.

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

$$
\int_{\mathbb R^3} f(x,t)\,dx=0
\quad\text{and}\quad
\nabla\cdot f=0.
$$

Those conditions cannot be used as CMI disproof criteria without an additional theorem or admissibility assumption. In the forced alternatives, the external body force is not an internal stress. It may inject net momentum, and incompressibility is imposed on the velocity field rather than on the body force. The repository's `CandidateProperties` likewise requires force smoothness, positive-time support, rapid decay, the Navier–Stokes residual identity, and the stated energy/blow-up consequences, but not either proposed conservation identity.

The code inspection also answers the implementation question. `PositiveTimeForce.force` contains no pressure gradient; it is only `timeCutoff z.1 • f z`. The pressure gradient enters through `navierStokesResidual` in `CandidateFromLimits.force`, which agrees with the activated residual before `t = 1` and is smoothly extended at the endpoint. Therefore the proposed momentum/divergence test does not refute the formal C/D proposition. It remains a legitimate physical-provenance concern because the force is selected from the candidate residual.

**Verdict:** the proposed conservation trap is not an ironclad counterexample. The live formal target is to prove, without `sorry`, that the selected residual cannot have the endpoint limits or force predicates required by the code. Evidence: `NavierStokesReview/evidence/force_conservation_obstruction_adjudication_2026-09-23.md`.

## Finding 14: fixed-data perturbation exposes residual path dependence

The independent-data objection has now been tested against the concrete
residual operator rather than left as a physical analogy. The zero-sorry probe
`IndependentDataPerturbationProbe.lean` defines

$$
e_a(t,x)=(t-t_0)a,qquad a\ne0,
$$

and proves that `e_a` is globally smooth and spatially divergence-free. At
the reference time its spatial derivatives and Laplacian vanish, while its
time derivative is `a`. The exact residual defect is therefore `a`, so the
perturbed velocity cannot satisfy the same fixed force as the base velocity.

This formally establishes path dependence: a force selected as the residual
of one trajectory does not remain the residual after an independent velocity
variation. It does not, by itself, prove that the literal existential C/D
statement is false. The chosen test field is not compactly supported or
finite-energy on `ℝ³`, and no source theorem currently states that
`StageEstimates.exists_schedule` must be stable under an admissible variation.
The result is a direct causality objection and a precise target for a stronger
selected-path theorem, not a fabricated `False` certificate.

Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`.

## Finding 29: the five-moment branch is present, but the selected transport theorem is not

The dependency closure was rerun from `ActualCandidateAssembly.lean` rather
than inferred from direct imports. It reaches 507 local modules, including
154 occurrences of `PositiveOrderMoments`, 146 of `FiveProfileMoments`, 104 of
`FiveRowRank`, 42 of `physicalMoments`, and 44 of `CorrectionState.debt`.
`MeanRankUpdate.physical_five_rows`, `CorrectionState.rank_model_rows`, and
`ActualStageEstimates.RunData.rank_class` show that the upstream construction
does use genuine rank and debt data.

That result withdraws any broad allegation that the five-moment subsystem is
dead or globally disconnected. It strengthens the narrower objection. The
selected `Witness` type at `ActualCandidateAssembly.lean:1121-1151` and its
`selected_witness` instantiation at lines 1177-1180 contain no equality
identifying the final mixed sums with `PositiveOrderMoments.moments`,
`FiveProfileMoments.physicalMoments`, `FiveRowRank.FiveRows`, or the paper's
tuple `(M,I,J,S,C_p)`. The missing theorem is therefore a selected-endpoint
transport obligation. It is material to the paper-to-code claim, but it is not
itself a zero-sorry contradiction to the concrete endpoint.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Finding 31: the proposed zero-row collision is not a selected-field contradiction

The claim that a compact perturbation must force `False` through the first two
rows of `FiveRowRank.FiveRows` was tested at the declaration and theorem
levels. `FiveRows` constrains the correction functions `dv` and `ga`; its first
two equations are explicit radial correction integrals. The theorem
`FiveRowRank.five_rows` proves all five rows for every admissible
`d : Fin 3 → ℝ`, including a nonzero debt. The downstream theorem
`DefectIncrementBounds.fiveRows_preserve_masses` preserves two radial moments
of the correction state, not a generic energy integral of the selected
Cartesian velocity.

The selected `Witness` type contains stage sequences, extensions, force
properties, consequences, norm growth, decay, and endpoint jets. It contains
no `Debt`, `FiveRows`, `physicalMoments`, or equality to the paper tuple. A
zero-sorry probe therefore establishes that a nonzero rank debt and the
selected witness can coexist as separate data. The compact fixed-force
perturbation remains an operator-level obstruction, but it is not transported
into the selected correction state by the endpoint theorem.

This rejects the direct collision argument without clearing CTR-005. The
remaining decisive question is whether a selected-path theorem identifies the
paper's five moments with the correction-state rows and carries that identity
into the mixed residual and force. Evidence:
`NavierStokesReview/evidence/five_row_collision_boundary_2026-09-24.md`.

## Finding 32: the zero rows give a conditional perturbation obstruction

The correction subsystem does support a genuine contradiction once the
perturbation has been transported into the correction increment. A new
zero-sorry completion proves that the full `FiveRows` predicate forces
`barMoment 2 h.angular = 0` and `barMoment 1 h.axial = 0`; adding either
corresponding nonzero hypothesis yields `False`.

The production recurrence does carry a related internal invariant: its
`CycleAnalyticInvariant.masses` field is propagated through every selected
cycle stage. `SelectedCycleMomentTransport.lean` exposes that fact and proves
the same conditional impossibility for a nonzero selected-cycle radial
moment. This removes the stronger claim that the cycle has no local mass
preservation theorem.

That result does not yet apply to the selected witness. `FiveRows` constrains
the correction increment, while `Witness` exposes the assembled stages,
pressure, force, endpoint consequences, and norm growth. The selected theorem
does not provide an equality identifying an independently injected Cartesian
perturbation with `h.angular` or `h.axial`. It also does not identify these
radial moments with kinetic energy or `(M, I, J, S, C_p)`.

The correct conclusion is therefore a live conditional attack, not a completed
endpoint refutation: prove the missing selected-path transport and the
nonzero-moment calculation, then the new theorem supplies the contradiction.
Evidence: `NavierStokesReview/evidence/correction_invariant_scope_2026-09-24.md`;
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.

## Finding 22: the force attack now has an exact conditional contradiction

The review has now attacked the selected witness itself. The zero-sorry probe
`SelectedWitnessEndpointResidualProbe.lean` extracts the actual
`CandidateProperties` package and proves that, before the singular time, the
selected force is exactly the selected Navier–Stokes residual. It then proves
the following implication:

$$
\begin{aligned}
\lVert u(t,0)\rVert&\longrightarrow\infty,\\
\lVert f(t,0)\rVert&\leq B,\\
c\lVert u(t,0)\rVert&\leq\lVert\mathcal R(u,p)(t,0)\rVert,\quad c>0
\end{aligned}
\qquad(t\to1^-)
\quad\Longrightarrow\quad\bot.
$$

This is stronger than the earlier residual-naming objection. The probe now
also instantiates the selected schedule and proves that its origin speed tends
to infinity while its actual mixed residual tends to zero. Consequently, the
positive lower bound in the displayed contradiction is impossible for that
selected raw residual. This is evidence of deliberate residual cancellation,
not evidence that the force is singular.

The composition question is now settled on the selected path. The zero-sorry
probe `SelectedForceOriginCompositionProbe.lean` uses the late-time activation
identities, the periodic plateau at the origin, and the selected
`VanishingJointJets` premise to prove

$$
\lVert f(t,0)\rVert\longrightarrow0\qquad(t\to1^-).
$$

The selected force therefore does not diverge at the origin. This closes the
force-explosion route and records genuine residual cancellation. It does not
validate the paper's five-moment or absolute-pressure interpretation, and it
does not itself produce `False`.

Evidence: `NavierStokesReview/evidence/selected_force_origin_composition_2026-09-24.md`.

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

### The missing selected-endpoint moment transport
The repository compiles on the inspected Lean path, and the source contains
three-component spatial evaluations. That is not a certification of the full
mathematical claim. The base profile (`TailGaugePotential`) and residual bounds
(`PhysicalResidualJetBounds`) do not support the stronger pure-axial or fake-2D
allegation; `radialNormalize_anchor` regulates a precise line rather than
annihilating the global field.

However, a critical divergence occurs at the final assembly boundary (`ActualCandidateAssembly.selected_witness`). The proof evaluates PDE correctness through direct geometric jet decay bounds (`NativeBounds` in `PhysicalResidualJetBounds.lean`). The selected assembly's transitive import closure does contain `FiveProfileMoments`, `FiveRowRank`, and `PositiveOrderMoments` through upstream construction modules, but the residual-realisation theorems inspected here do not expose those five-coordinate moment arrays $(M, I, J, S, C_p)$ as semantic premises or prove their identification with the selected residual.

Consequently, while the repository's modules are internally valid and satisfy the mechanical requirements of the type checker, the existential abstraction boundary leaves the paper's primary physical proof strategy semantically unconnected on the inspected endpoint. The five-moment machinery exists upstream, but the final theorem does not visibly transport the paper's named quantities through `StateRealization`, the residual estimates, and `selected_witness`. The claimed paper-to-code correspondence is therefore not established by the inspected source.

### A machine-checked countermodel to the generic stage interface

The objection is stronger than a missing-name search. A zero-sorry Lean probe constructs a nonempty `StageEstimates` object whose potential, direct, and pressure stages are all zero. Its finite background and residual rate obligations also hold, while a separate theorem proves that the corresponding zero velocity is not unbounded at time one. The generic stage interface therefore admits a static field and cannot itself encode either the five named moments or the blow-up conclusion.

This is a formal refutation of the interface-level implication claimed by any reading that identifies `StageEstimates` with the paper's physical repair system. It is not a formal refutation of `selected_witness`, because the selected endpoint adds further premises for the actual base, physical realization, axis preservation, and origin growth. The remaining load-bearing failure is that no theorem inspected so far transports the paper's five moments through all of those additional premises into the exported candidate.

Evidence: `NavierStokesReview/evidence/stage_estimates_moment_blindness_2026-09-24.md`.

## Pressure-chain finding

The compact-pressure objection does not currently refute the selected C/D
predicate. The exact R3 source records compact pressure support, but the force
is an unrestricted smooth external field and may carry the pressure-gradient
part of the residual. `PressureRecovery` derives gradient pairings only under
explicit comparison hypotheses, while `ActualPressureFlux` converts those
pairings into the cutoff flux used by `WholeSpaceUniqueness`. The zero-sorry
pressure probe proves that compact support does not imply a slice is zero.

This route is therefore closed only as the narrow implication that compact
support forces a slice to vanish. That is not an acceptance of the pressure
construction. The selected endpoint still lacks
an inspected theorem connecting its compactly localised pressure and local
`StateRealization`/`chartIdentity` identities to the paper's global pressure
semantics. The adverse finding that remains is narrower and stronger: the
selected endpoint also has no inspected theorem transporting the paper's five
named moments into the selected residual and force construction. Evidence:
`NavierStokesReview/evidence/pressure_recovery_chain_audit_2026-09-24.md`.

### Finding 22: comparison recovery is not absolute pressure verification

The pressure conclusion must not be over-cleared. `PressureRecovery.Hypotheses`
contains smoothness, divergence-free velocity, equal residuals, and finite
energy for a pair `(u,p)` and `(v,q)`. It has no absolute pressure-Poisson
representative or pressure-normalisation field. The zero-sorry
`PressureRecoveryAbsolutePremiseProbe.lean` instantiates it with identical zero
velocities and any common smooth pressure. Consequently, the recovery theorem
can certify a pressure-difference identity while saying nothing by itself about
whether the selected pressure has the global semantics asserted in the paper.

This is a formally demonstrated limitation of the comparison interface, not yet
a contradiction to `selected_witness`. The remaining decisive test is to show
that `PhysicalFields.pressure_germ`, `StateRealization.base_equation`, and the
selected `VanishingJointJets` premise jointly imply the required absolute
global pressure relation, or else to derive a contradiction from those actual
premises. Evidence:
`NavierStokesReview/evidence/physical_transport_bridge_spec_extraction_2026-09-24.md`.

The selected residual trace shows where the live endpoint obligation enters:
`StageEstimates.exists_schedule` derives `VanishingJointJets` from rate
estimates, and `ActualCandidateAssembly.selected_witness` consumes it through
the generic germ theorem. The public interface does not expose the five named
moments as premises of that limit. This is the current CTR-005 transport
objection, not yet a zero-sorry contradiction to the selected theorem.
Evidence: `NavierStokesReview/evidence/selected_residual_endpoint_trace_2026-09-24.md`.

## Axis scope of the residual bridge

The selected residual proof has a second interface limitation, specifically at the boundary interface where the off-axis chart meets the singular origin. The discrepancy is isolated to two distinct coordinate regimes:

1. **The Off-Axis Cartesian Fields:** The core engine that lifts coordinates and evaluates residual properties (`StateRealization.chartIdentity`, Line 927 of `NavierStokes/PhysicalResidualJetBounds.lean`) explicitly excludes the singular axis. The type parameter requires `radius_ne : ∀ x ∈ U, x.1.1 ≠ 0`.
2. **The On-Axis Global Limits:** The construction of the vanishing jet fields along the singular temporal limit requires a joint bound across the central axis (`GlobalBaseError.originPast`, Line 159 of `NavierStokes/GlobalBaseError.lean`), which evaluates spatial coordinates passing through `r = 0`.

The repository does structurally separate these regions. The terminal theorem
(`selected_residual_jetRate`, `ActualCycleResidualBounds.lean:956-989`)
combines an estimate on `S` with a base estimate on `Sᶜ`. The `houtside`
hypothesis is the transport step that makes this legitimate: outside `S`, the
selected velocity and pressure are eventually equal to the base fields. Thus
the source proves a piecewise rate bound; it does not prove a discontinuity or
an automatic failure at the axis.

The genuine limitation is narrower. `chartIdentity` is not an origin theorem,
and the selected public interface does not state that the paper's five
moments or an absolute pressure-Poisson identity are preserved when the
piecewise residual bound is assembled. This leaves a selected-path
correspondence obligation under CTR-005. It does not show that the nonlinear
terms fail to match at `r → 0`, because the source may be intentionally
placing the correction support away from the origin and using the base germ
there. A formal refutation still requires a false equality or an incompatible
origin consequence for the actual selected fields.

Evidence: `NavierStokesReview/evidence/state_realization_axis_scope_audit_2026-09-24.md`.

## Finding 23: the rate interface cannot carry the paper's five debt

The formal review now contains a second zero-sorry result beside the
zero-stage countermodel. `StageEstimatesMomentBlindnessProbe` proves
`interface_does_not_determine_five_debt`: the generic rate record cannot
determine an arbitrary `PositiveOrderMoments.Debt`. This closes a precise
interface question. The paper's five quantities cannot be treated as present
merely because the selected construction imports five-moment modules or
because a three-coordinate debt can be promoted algebraically.

The result does not prove that the selected endpoint has the wrong moments.
It identifies the missing load-bearing theorem: the actual selected velocity,
pressure, and residual must be shown to realise the five named integrals and
to preserve them through the selected schedule. Until that theorem or a
contradiction from its concrete premises is supplied, the correct verdict is
**formal correspondence failure not yet converted into a formal refutation**.

Evidence: `NavierStokesReview/evidence/stage_estimates_moment_blindness_2026-09-24.md`.

## Editorial control

This is the active human-readable review. Its evidence boundary and the status
of older notes are defined in [`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md).
It is intentionally not a chronological audit log: claims are stated with
their present status and linked evidence, while unresolved objections remain
explicitly unresolved.

## Finding 24: the five-moment machinery is live upstream, but its selected-endpoint transport is not shown

The review withdraws the stronger claim that the five-moment branch is dead or
disconnected. `GlobalStressSupport.moments_zero` is used by
`EntranceAlignedBase.aligned_moments_zero`; the modulated construction derives
finite residual identities, and `FinalSlowBase` exports those identities for the
same profile that supplies the base origin blow-up. The zero-sorry
`SelectedBaseMomentCompatibilityProbe` verifies this chain directly.

That correction does not remove CTR-005. The selected endpoint accepts generic
`StageEstimates` and local `PhysicalFields`/germ data. Those interfaces do not
state that the final mixed sums equal the repaired five rows or the paper's
`(M,I,J,S,C_p)`. No theorem carrying that equality into the selected residual,
pressure, force, and `VanishingJointJets` premises was found in the inspected
path. The correct criticism is therefore a missing selected-mixed-sum transport
theorem, not a nonexistent upstream repair subsystem.

**Status:** material correspondence failure; no zero-sorry `False` theorem yet.

Evidence: `NavierStokesReview/evidence/selected_base_moment_chain_reaudit_2026-09-24.md`.

## Finding 25: the force-jet attack now has a precise missing theorem

The new zero-sorry probe `SelectedResidualLowerBoundObstructionProbe.lean`
proves the exact conditional contradiction: if the selected origin residual
satisfies a fixed positive lower bound

$$c\lVert u(t,0)\rVert \leq \lVert\mathcal R(u,p)(t,0)\rVert,$$

then the residual's vanishing endpoint jets and the origin velocity blow-up
derive `False`. The probe also proves the one-sided residual norm limit from
`VanishingJointJets` on the actual non-bottom endpoint filter.

The selected source instead proves the raw residual and final force tend to
zero at the origin. The positive lower bound is therefore not merely
unlocated; it is incompatible with the selected cancellation. This closes the
force-jet route as a formal disproof strategy. The remaining falsification
work must identify a different false selected premise, most directly in the
transport of the paper's five moments or in the absolute pressure semantics.

## Finding 26: the selected-witness falsification boundary is still open

The direct attacks have been tested against the production path. The force
attack now has a stronger selected-path result: the final force tends to zero
at the origin while the selected speed diverges, so the proposed force
explosion is not available. The pressure attack identifies the absence of a
global Poisson/Leray premise, but compact support alone does not imply
triviality.
The moment-blindness probe shows that the exported witness envelope does not
carry the paper's five-debt payload, but it does not prove a wrong moment for
the concrete selected sums.

These are not clearances. They are the exact remaining proof obligations for
turning the architectural objections into a zero-sorry `False` theorem.
The current review verdict remains **not established**, with a live formal
falsification programme and no completed selected-witness contradiction.

Evidence: `NavierStokesReview/evidence/selected_witness_boundary_attack_status_2026-09-24.md`.

The companion zero-sorry probe `SelectedWitnessAttackBoundaryProbe.lean`
now fixes the logical scope of this finding. It proves that the exported
`Witness` does not entail zero for every five-coordinate debt and that scalar
blow-up can coexist with a scalar residual tending to zero. Consequently,
the missing velocity-to-residual lower bound is not a technicality: it is the
premise required to turn the force-jet objection into `False`.

Evidence: `NavierStokesReview/evidence/selected_witness_attack_boundary_2026-09-24.md`.

## Finding 27: the flat residual premise is all-order but debt-blind

`JointResidualLimits.VanishingJointJets` is defined by a quantifier over every
natural derivative order. The selected construction derives it from finite
residual-rate estimates through `ActualCycleResidualBounds`,
`ActualStageEstimates`, `StageEstimates.exists_schedule`, and
`MixedDiagonalResidual.exists_physical_schedule_residual_zero`. The result is
not a truncated `H^3` condition.

The late time switch and the periodic spatial localisation are also source
supported. The switch is globally smooth, equals one for `t ≥ 3/4`, and its
positive-order derivatives vanish on the late side. The localisation compares
the complete residual by neighbourhood equality, preserving advection,
diffusion, pressure gradient, and all local derivative orders.

Those identities nevertheless take no `FiveRowRank.Debt`,
`PositiveOrderMoments.Debt`, or paper-moment parameter. They cannot supply the
missing selected transport theorem. This is a precise debt-blind interface
finding, not evidence of a temporal discontinuity or deleted three-dimensional
cross term.

Evidence: `NavierStokesReview/evidence/vanishing_joint_jets_and_localisation_trace_2026-09-24.md`.

## Finding 28: fixed-force perturbations expose residual dependence

The phrase “given, externally applied force” has a stronger causal meaning
than the source's construction: `CandidateFromLimits.force` is built from the
selected residual and then extended through the endpoint. To test the
consequence rather than merely describe it, the review adds a smooth velocity
perturbation (e) while keeping pressure and force fixed.

The zero-sorry theorem in
`NavierStokesReview/src/probes/IndependentDataPerturbationProbe.lean` proves
that simultaneous satisfaction of the same fixed-force equation requires

$$
\partial_t e-\Delta e+(u\cdot\nabla)e+(e\cdot\nabla)u+(e\cdot\nabla)e=0.
$$

The companion extension in
`NavierStokesReview/src/extensions/FixedForcePerturbationCompletion.lean`
instantiates the obstruction for `PositiveTimeForce.force`. Thus a nonzero
perturbation defect cannot be absorbed by the unchanged force. This is a
formal, source-level demonstration that the construction is path-dependent:
the force must be recomputed when the selected velocity path changes.

The result must not be overstated. It does not prove that an arbitrary
perturbation is one of the admissible witnesses in the repository, nor that
`exists_schedule` fails for every perturbation. It therefore establishes a
causality and correspondence defect in the claimed physical interpretation,
not yet an unconditional `False` theorem for the literal existential C/D
statement. Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`.

## Finding 30: the fixed-force obstruction survives spatial localisation

The earlier affine-time test was useful for isolating the operator identity but
was not spatially localised. The new extension
`NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean`
constructs a smooth compactly supported potential, takes its spatial curl, and
uses that curl in a time-affine perturbation. The source proves smoothness,
slice compact support, and exact divergence freedom without `sorry`.

At the switch time, the perturbation itself, its spatial derivative, and its
spatial Laplacian vanish, while its temporal derivative is the curl field. The
potential is chosen so that the curl at the origin is `coordinateVector 0`, a
nonzero vector. The theorem
`compactPerturbation_breaks_any_fixed_force_at_origin` therefore proves that a
base field satisfying `navierStokesResidual u p = f` cannot also satisfy that
same fixed-force equation after this localised perturbation.

This closes the earlier localisation limitation in the operator test. It still
does not prove `False` from the literal existential C/D endpoint: the endpoint
does not state perturbation stability or quantify over this test field. The
load-bearing CMI objection remains the missing theorem connecting the selected
residual construction to the independent-data semantics claimed in the paper.

Evidence: `NavierStokesReview/evidence/compact_fixed_force_perturbation_2026-09-24.md`.

## Finding 33: temporal patching is an open interface question, not a proved jump

The stage-transition audit does not find a piecewise-in-time stage definition.
`GermCandidateAssembly.initializedSeries` selects a base/initial field at index
zero and a raw stage at each successor index. The constructor does not itself
require adjacent fields to match, so a proof of selected-field continuity must
come from the later summed-field regularity theorems. This is a legitimate
interface obligation, but it is not a proof that the selected field has a
temporal discontinuity or an energy-gradient jump.

The distinction is now formal. `initialized_series_admits_concrete_boundary_mismatch`
constructs unequal raw entries at indices zero and one, using a nonzero
coordinate vector for the first stage. Because the index is not a time
coordinate, this establishes only that the raw selector lacks an adjacent-stage
matching contract. It does not establish a temporal PDE jump, nor does it show
that the concrete family satisfies the selected endpoint hypotheses.

The source does contain the relevant positive results: `timeSwitch` is used
through a `ContDiffOn ℝ ∞` theorem, late local equality preserves temporal
derivatives, and spatial localization transfers residual jet limits by local
equality. The zero-sorry probe
`NavierStokesReview/src/probes/TemporalPatchingDiscontinuityProbe.lean`
records those facts and the exact indexed-prefix recurrence.

The review therefore retains `CTR-017` as an unresolved verification task:
close it only by deriving a nonzero derivative mismatch for the selected
spacetime sum, not merely by pointing to the absence of an adjacent-stage
equation. The external-source distinction is recorded in
`docs/OpenAI_NavierStokes_Source_Context_Register.md`: residual construction is
a real causal/provenance criticism, but it is not by itself a literal C/D
contradiction under the existential formulation.

## Finding 31: the compact obstruction reaches the selected witness

`selected_candidate_fixed_force_obstruction` now destructs
`ActualCandidateAssembly.selected_witness` and binds its selected velocity,
pressure, and force. At $(t,x)=(1/2,0)$, the compact divergence-free
perturbation has defect `coordinateVector 0`, so the selected field and its
perturbation cannot satisfy the same fixed-force residual equation. The
extension compiles without `sorry`, `axiom`, or `unsafe` declarations.

This is a selected-path causality result, not a global existential
contradiction. `CandidateProperties` does not state perturbation stability or
an independence predicate for the force. The result strengthens CTR-012 while
leaving CTR-005, the missing selected five-moment transport theorem, as the
load-bearing correspondence objection.

Evidence: `NavierStokesReview/evidence/selected_witness_fixed_force_obstruction_2026-09-24.md`.

## Selected-force provenance closure

The provenance claim is now directly extracted from the selected endpoint.
`SelectedResidualProvenance.selected_candidate_force_is_residual_output`
proves that the selected force equals the selected Navier--Stokes residual at
every interior time. This removes any ambiguity about whether the concern is
merely terminological: the construction really does choose the force from the
candidate motion. The proof still has a precise boundary. The exported C/D
predicate asks for existence of a smooth force and does not state that the
force must be chosen independently, nor that the witness must be stable under
independent perturbations. The causal objection is therefore established as a
paper-to-code provenance failure, while a literal formal refutation still
requires an additional admissibility premise or a false selected identity.

Evidence: `NavierStokesReview/evidence/selected_residual_provenance_2026-09-24.md`.

## Finding 34: the runtime rank layer is real, but endpoint transport remains unshown

The correction-row re-audit rules out an exaggerated version of the zero-row
objection. `MeanRankUpdate.physical_five_rows` proves the full runtime row
system for arbitrary three-coordinate debt, and the actual cycle consumes
that debt through `CorrectionState`. The first two rows constrain the radial
moments of the correction functions and preserve the corresponding internal
mean moments. They are not an energy axiom and do not force the selected
Cartesian velocity to vanish.

The remaining objection is more precise. The public `Witness` exports the
mixed fields, pressure, force, residual consequences, jets, and blow-up, but
no equality identifying the internal correction moments with the paper's
`(M,I,J,S,C_p)` or transporting that equality into the final residual and
force. This is a material paper-to-endpoint correspondence gap. It is not
itself a selected-witness `False` theorem.

Evidence: `NavierStokesReview/evidence/selected_rank_transport_reaudit_2026-09-24.md`.

## Endpoint transport recheck

The final source trace does not support the claim that the five-moment system
is dead. `ActualCandidateAssembly.physicalData` is built from actual cycle
fields, `ActualStageEstimates` consumes `CorrectionState.debt`, and the rank
layer proves its five integral rows for the constructed correction. The
upstream machinery is therefore substantive.

The exported `Witness` still exposes only the schedule, mixed stage fields,
away extensions, force, candidate properties, residual consequences, blow-up,
decay, and endpoint jets. It does not expose an equality to
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or `(M,I,J,S,C_p)`. The correct objection is that the
paper's five-moment interpretation is not transported into the public
endpoint. That is a load-bearing correspondence defect, not a theorem that
the selected fields violate the moments.

Evidence: `NavierStokesReview/evidence/selected_endpoint_direct_source_trace_2026-09-24.md`.

## Finding 35: the whole-space uniqueness route is formally active

The no-global-solution conclusion was checked against its actual dependency
chain. `WholeSpaceUniqueness.classical_uniqueness_on_Icc` derives equality on
each closed interval before time one from the two residual equations,
incompressibility, smoothness, finite-energy bounds, compact support of the
reference velocity, and compact-test pressure recovery. The selected wrapper
`candidate_global_agrees_before_one` supplies the candidate properties, and
`CandidateProperties.no_global_solution_one` uses compact support together
with the speed blow-up.

This removes two weaker objections from the review. The R³ theorem is not
merely a candidate-existence shell, and compact pressure support is not used to
make the pressure or velocity vanish. The pressure argument recovers relative
gradient information for the comparison estimate; it does not expose an
absolute pressure representative. That remains a correspondence question, not
a pressure-trivialisation contradiction.

The audited declarations use only the standard Lean axioms
`propext`, `Classical.choice`, and `Quot.sound`. No selected-path `False`
result follows from this audit.

Evidence: [`whole_space_uniqueness_audit_2026-09-24.md`](../NavierStokesReview/evidence/whole_space_uniqueness_audit_2026-09-24.md).

## Fixed-force stability is a separate formal objection

The review-side theorem `FixedForcePerturbationStability.lean` defines an
explicit stronger requirement: the same force and pressure must continue to
satisfy the residual equation after every smooth, compactly supported,
divergence-free velocity perturbation. The selected candidate fails this
requirement. The compact perturbation at $(t,x)=(1/2,0)$ contributes the
nonzero defect `coordinateVector 0`, while the force is held fixed.

This is a precise formalisation of the causal/provenance concern surrounding
the residual-designed force. It is not, by itself, a refutation of the
literal C/D existential statement, because that endpoint exports one selected
force and one selected candidate and does not quantify over perturbations. The
result therefore belongs under CTR-012, alongside the direct residual
provenance theorem, while CTR-005 remains the unresolved paper-to-endpoint
transport objection.

Evidence: [`fixed_force_stability_extension_2026-09-24.md`](../NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md).

The initial-data loophole in that first probe has now been removed. The review
extension `SameDatumFixedForcePerturbation.lean` uses the factor
`t(t-t₀)`, so the perturbation is zero at the selected initial time as well as
at the interior switch. It remains smooth, compactly supported on each spatial
slice, and divergence-free, but its temporal derivative at the switch is
nonzero at the origin. The theorem
`selected_candidate_fails_fixed_force_same_datum_stability` therefore proves
fixed-force path dependence without changing the zero initial datum. The result
still concerns a strengthened forward-data predicate; it is not a standalone
`False` derivation from the literal existential C/D endpoint.

Evidence: [`same_datum_fixed_force_obstruction_2026-09-24.md`](../NavierStokesReview/evidence/same_datum_fixed_force_obstruction_2026-09-24.md).

## Active-stage non-vacuity is conditional

The stage-control implementation explicitly branches on whether
`ActiveParticularStageControls.ActivePair` is nonempty. That branch cannot be
used as proof that the selected construction is vacuous. The review theorem
`active_pair_of_selected_label` establishes the positive conditional fact:
once a concrete `ActualPrimary.Label B N0` is supplied, its chart-band lower
bound and `CommonWindow.self_mem` produce an active pair.

The selected witness still does not export a theorem asserting inhabitance of
the label subtype. Until that theorem is constructed or its negation is
proved, the empty branch is a source-level reachability question rather than
a formal refutation.

The follow-up probe makes the boundary precise. `potentialSum` is defined as a
natural-indexed `tsum` of stage fields, so an assumed empty `ActivePair` does
not turn the diagonal series into a limit over an empty subtype. The missing
result is narrower and still material: the selected endpoint does not export
`Nonempty (ActualPrimary.Label B N0)` or `Nonempty (ActivePair B N0)`, while
upstream estimates explicitly tolerate an empty index. This is an unresolved
selected-path inhabitability obligation, not evidence that the selected
velocity is already vacuous.

Evidence: [`selected_active_pair_reachability_2026-09-24.md`](../NavierStokesReview/evidence/selected_active_pair_reachability_2026-09-24.md);
[`selected_label_inhabitability_audit_2026-09-24.md`](../NavierStokesReview/evidence/selected_label_inhabitability_audit_2026-09-24.md).

## CMI wording and formal admissibility

Fefferman's statement uses the language of a given, externally applied force
and requires smooth decay estimates. OpenAI's release presents the same
balance as a smooth applied force whose acceleration, pressure, transport, and
viscosity terms cancel. The residual-defined force remains a serious causal
and provenance objection. The exported C/D predicate, however, contains no
formal force-independence or perturbation-stability condition. The compact
fixed-force theorem is therefore a formal objection to the stronger
forward-data reading, not a standalone proof of `False` for the literal
existential endpoint.

## Finding 36: global germ transport is substantial but not semantically complete

The source audit does not support describing the global assembly as a hollow
wrapper. `CandidateConsequences.mixed_exists_force_with_consequences`
(`CandidateConsequences.lean:185-215`) constructs a force together with
`CandidateProperties`, the maximal-lifespan and H³ consequences, force-jet
decay, and all-order boundary jets. `ActualCandidateAssembly.physicalData`,
`estimates`, and `endpoints` (`1079-1115`) supply actual cycle data to the
finite-stage construction, and `Witness` (`1121-1151`) packages the resulting
selected fields.

The remaining defect is an interface omission, not a missing PDE theorem in
those modules. `Witness` exposes no equality transporting the paper's
$(M,I,J,S,C_p)$ moments into the selected mixed velocity, pressure, residual,
or force. It also exposes no fixed-force same-datum stability condition. The
zero-sorry `GlobalTransportBridgeProbe.lean` proves that the selected candidate
has the full `Consequences` bundle while the independently constructed
same-datum perturbation breaks the fixed-force predicate. The separate
`EndpointContractNonImplication.lean` theorem proves that
`CandidateProperties` alone does not imply that predicate.

This is the precise CTR-016/CTR-012 result. It establishes that the exported
global contract is weaker than the forward-data and five-moment interpretation
used in the paper. It does not, without an additional premise or a false
selected identity, derive `False` from the literal C/D existential.

Evidence: [`global_germ_transport_audit_2026-09-24.md`](../NavierStokesReview/evidence/global_germ_transport_audit_2026-09-24.md),
[`endpoint_contract_nonimplication_2026-09-24.md`](../NavierStokesReview/evidence/endpoint_contract_nonimplication_2026-09-24.md).

## Revision note: global germ transport recheck

The global-transport audit was rechecked against the actual cycle construction,
not only against the final `Witness` type. `state_runInvariant`
(`ActualCyclePreservation.lean:826-848`) inducts the selected cycle while
retaining analytic, coherence, and periodicity data. `state_particularData`,
`state_waveData`, and `state_wave_transport` (`850-912`) supply the inputs used
by `ActualCycleCoherence.mean_input_of_transport` (`ActualCycleCoherence.lean:803-820`).
The stage constructors and chart equalities are also real:
`ActualCandidateConstruction.lean:392-404,464-502` defines the native stages
and prefix identities, while `ActualCandidateAssembly.lean:392-424`
identifies the actual fields with their chart expressions.

This removes the claim that the selected endpoint is merely a disconnected
wrapper. It does not remove the load-bearing correspondence objection. The
transport chain carries cycle, covariance, wave, chart, and residual data into
`physicalData`, `estimates`, and `endpoints`; `Witness`
(`ActualCandidateAssembly.lean:1121-1151`) still exports no equality to
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or the paper's $(M,I,J,S,C_p)$ tuple. The precise
finding is therefore a missing field-level semantic identification, not an
absence of global PDE assembly.

The zero-sorry `GlobalTransportBridgeProbe.lean` result remains unchanged: the
selected candidate has the full `Consequences` bundle while the independently
defined fixed-force same-datum stability predicate fails. That result is a
formal selected-path provenance objection. It does not turn the literal
existential C/D statement into `False`, because that statement does not include
the stronger perturbation-stability or force-independence predicate.
