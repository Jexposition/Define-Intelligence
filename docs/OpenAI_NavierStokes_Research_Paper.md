# A Counter-Paper on OpenAI's Navier–Stokes Blow-Up Claim

## 17. Base profile and core-asymptotics finding

The core profile is axisymmetric in reduced variables `(t, s, z)`, but its potential is embedded in three Cartesian directions and converted to velocity by spatial curl. The source therefore supports a three-component axisymmetric field, not a globally one-dimensional or globally zero-swirl field. The radial-anchor zero is a local normalisation.

Five-moment repair algebra exists upstream. The unresolved issue is transport into the selected endpoint: the generic finite-stage summation theorem does not itself identify the final fields with `(M, I, J, S, C_p)`. Base smoothness follows from coefficient regularity, while force smoothness depends on residual-jet limits and away extensions. The `WholeDomain*` family is disconnected from `selected_witness` but not globally unused. No zero-sorry contradiction has yet been established.

## 18. The composition gap between the local construction and the exported endpoint

The source separates the local paper construction from the exported R³
candidate. `LocalResidualFlatness` selects a schedule for the raw-stage aliases,
and `LocalPaperTheorem` proves the local properties for that schedule.
`ActualCandidateAssembly.selected_witness` exposes an existential assembly
containing a schedule, away extensions, a force, generic candidate properties,
and asymptotic consequences. `PaperLocalization` connects these layers by
proving local velocity and pressure agreement at late times, but its result does
not state force equality or carry the paper's five named moments `(M, I, J, S,
C_p)` into the final R³ comparator.

That omission is not a Lean compilation error. It is a missing semantic
transport theorem at the point where a local construction becomes the claimed
whole-space solution. The earlier stronger statement that the five-moment
module is dead code is withdrawn: the local layer consumes the selected
aliases, and a genuine five-component repair theorem exists upstream.

## Abstract

This paper reports an independent formal review of the public Lean development associated with OpenAI's claim of finite-time breakdown for the three-dimensional incompressible Navier–Stokes equations. The review asks a narrower question than whether the repository compiles: does the exported formal theorem establish the mathematical construction described in the accompanying paper, and does that construction meet the exact alternatives in Charles Fefferman's Clay Mathematics Institute problem statement?

The current evidence gives a mixed result. The repository contains a genuine whole-space endpoint with the quantifier shape of a forced CMI alternative, and the inspected endpoint depends only on Lean's standard foundational axioms. The uniqueness and comparator chain is not a superficial compilation artefact. However, the paper's five-coordinate moment narrative is not directly identified with the repository's `FiveRowRank` system: the two systems have different debt dimensions and incompatible row exponents. The repository also contains a separate five-dimensional `PositiveOrderMoments` repair theorem, but no inspected endpoint theorem establishes the required identification between that layer, the paper's `(M,I,J,S,Cp)` coordinates, and the exported candidate. The appropriate conclusion is therefore **major revision: the claimed paper-to-code correspondence is not established**. A formal contradiction to the exported endpoint has not yet been derived.

## 1. Question and standard

The audit separates three propositions that are often conflated:

1. Lean accepts a term under a fixed compiler and dependency snapshot.
2. The accepted term proves the proposition written in its declaration.
3. That proposition is the same mathematical claim made in the paper and satisfies a Clay alternative.

Fefferman's problem explicitly permits a smooth external force in alternatives (C) and (D). Consequently, the fact that the construction uses forcing is not itself a counterargument. A valid adverse finding must identify a false implication, a missing hypothesis, an untrusted dependency, or a mismatch between the stated PDE and the claimed construction.

The Clay prize procedure is a separate institutional question. Publication, a two-year review period, and general mathematical acceptance are not supplied by a GitHub repository or by a kernel certificate. This paper concentrates on mathematical validity and records the procedural distinction without treating it as a mathematical refutation.

## 2. Source and reproducibility boundary

The primary source is the public fork checkout at commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, on the review branch `review/cmi-first-navier-stokes-2026-09-22`. The downloaded directory `NavierStokesAndEuler-main-open Ais solution` is retained as a comparison snapshot and is not edited. The two trees are not interchangeable: their file counts, imports, and hashes differ.

All claims in this paper name the relevant source layer. The review probes are under `NavierStokesReview/src/probes`; they are zero-sorry auxiliary checks and are not additions to the OpenAI source.

## 3. What the exported theorem states

`NavierStokes/R3/ProblemStatement.lean` defines a candidate with smooth pre-singular velocity and pressure, compact spatial support, zero initial velocity, incompressibility, the Newtonian Navier–Stokes residual equation, bounded kinetic energy, and unbounded pointwise speed as time approaches one. The global comparator is required to be smooth for future times, divergence-free, a solution of the same forced equation, and uniformly finite-energy.

`NavierStokes/R3/Theorem.lean` and `NavierStokes/R3/CandidateBreakdown.lean` then use the candidate's agreement with every global finite-energy comparator before the singular time to derive nonexistence of such a global solution. `NavierStokes/R3/ComparatorBridge.lean` transports that conclusion to the CMI-facing whole-space statement. The inspected `#print axioms` reports for the headline R3 declarations contain only `propext`, `Classical.choice`, and `Quot.sound`.

This is meaningful formal evidence. It does not, on its own, validate the analytic construction that supplies the candidate properties.

## 4. Main findings

### 4.1 The force is residual-driven and remains active near the singular time

The construction defines the force from the momentum residual of the selected fields and applies a smooth temporal cutoff. `NavierStokes/R3/PositiveTimeForce.lean` makes the cutoff equal to one through the interval containing the singular time. The force is therefore not shown to switch off before the velocity becomes unbounded.

This is a substantive description of the mechanism, but it is not a failure of alternatives (C) or (D), which permit smooth forcing. It becomes an adverse finding only if the paper claims the stronger statement that the singularity is autonomous or that the force vanishes before blow-up. The current formal review does not treat that stronger physical interpretation as proved.

### 4.2 The uniqueness and pressure-flux bridge is not the present failure

The inspected chain in `WholeSpaceUniqueness.lean`, `PressureFlux.lean`, and `WholeSpaceComparisonClosure.lean` takes an arbitrary global finite-energy competitor, derives the pressure-flux bound from its stated PDE and energy assumptions, and proves agreement with the compact candidate before time one. No custom project axiom was found in the selected endpoint reports.

This does not prove every analytic estimate in the construction is correct. It does rule out the simpler accusation that the final contradiction is merely an unguarded boundedness assertion or an implicit use of an admitted global competitor estimate.

### 4.3 The paper's five-moment system is not directly identified with `FiveRowRank`

The paper describes five cumulative profile quantities `(M, I, J, S, Cp)` and a five-parameter local repair. The repository's `FiveRowRank.lean` instead defines a three-dimensional debt, with three angular powers and two axial powers. Its first two rows are fixed zero-moment conditions, while the remaining rows act on a three-coordinate defect.

The zero-sorry probe `MomentBridgeObstructionProbe.lean` proves two exact facts:

- the paper-shaped and `FiveRowRank` exponent vectors cannot be made equal by direct row identification;
- there is no linear equivalence between their debt spaces, because one has dimension three and the other dimension five.

This is a genuine formal obstruction to the direct identification suggested by the paper narrative. It is not yet a contradiction to the exported endpoint, because the repository also contains `PositiveOrderMoments.lean`, which defines a separate five-dimensional physical row system and proves an exact repair theorem. The missing result is a theorem identifying the paper's five quantities with the actual rows used by the selected candidate and showing that the repair is consumed by the endpoint.

### 4.4 Regularity does not imply the required moment identities

`MovingFieldRowNonImplicationProbe.lean` proves that smoothness and field motion alone do not entail the five row identities. Thus a proof of `ContDiff` or of local field reconstruction cannot be cited as a substitute for the missing moment-transport theorem. The burden is to provide the exact integrals, row ordering, coefficient map, and use of the repaired field in the PDE residual estimate.

### 4.5 The generic filter interface has a vacuity hazard, but the selected path is not shown vacuous

`DiagonalResidual.JetRate` has no `NeBot` premise. As a generic definition, it can be satisfied over `Filter.bot`, where eventual statements are vacuous. This is a real specification hazard and must be guarded at every call site.

The selected `originPast` path has been checked separately with `OriginPastNeBotProbe.lean`, and the selected endpoint's axiom report does not expose a `sorryAx`. The current evidence therefore supports the narrower statement: **the generic interface is under-specified, but a vacuous-filter proof of the exported endpoint has not been demonstrated**.

### 4.6 Challenge-file placeholders are not endpoint evidence

The repository contains four `sorry` declarations in `ComparatorChallenges`: two in `ComparatorChallenges/NavierStokes.lean` and two in `ComparatorChallenges/Euler.lean`. Source and dependency inspection did not place those declarations on the selected R3 endpoint path. This is a verified repository-integrity defect and defeats any unqualified claim that the entire source tree is zero-sorry. It is not, without a transitive dependency witness, a refutation of the exported headline theorem.

### 4.7 Physical robustness objections are not contradictions to the stated PDE

Ladyzhenskaya stresses, hypo-dissipation, and other regularisations change the equation being solved. They are legitimate questions about physical robustness and modelling scope, but they do not refute a theorem about the classical Newtonian Laplacian equation. The review records them as external scope questions, not as Lean failures.

## 5. Adjudicated claim table

| Claim under review | Present result | Classification |
|---|---|---|
| The public endpoint has a C/D-shaped forced nonexistence statement | Supported by source and zero-sorry endpoint probes | CONFIRMED at the formal interface |
| The endpoint is autonomous or force-free | The force remains active near the singular time | NOT ESTABLISHED; stronger claim contradicted by source |
| The paper's Appendix-A five moments are transported through the selected repair | Direct equality is impossible, while the promoted positive-order repair agrees with `FiveRowRank` | ENDPOINT TRANSPORT OPEN |
| A separate exact five-row repair exists in the repository | `PositiveOrderMoments` proves a five-dimensional exact repair | CONFIRMED as a separate module |
| The separate repair is proved to be the paper's repair and is consumed by the endpoint | No such identification theorem was found in the inspected endpoint path | OPEN, load-bearing |
| The endpoint is vacuous because of `Filter.bot` | Generic risk confirmed; selected non-bottom path checked | NOT DEMONSTRATED |
| Challenge-file `sorry` proves the headline result | Not on the inspected endpoint path | REFUTED as a dependency claim |

## 6. Verdict

The exported Lean endpoint is not refuted by the present audit. It is also not enough to support the strongest narrative claim that the published paper and the formal development are already the same proof. The zero-sorry moment obstruction is the most concrete adverse result so far: it shows that the obvious row-by-row reading of the paper cannot be the implementation in `FiveRowRank`.

Accordingly, the review recommendation is **major revision**. The authors must supply a formal, source-linked correspondence theorem from the paper's five moments to the actual five-row repair or revise the paper so that it describes the implemented three-debt/two-invariant architecture accurately. Until that is done, the claim “the Lean formalisation verifies the paper's stated construction” remains unestablished. A stronger conclusion, namely that the exported CMI theorem is false, requires a further zero-sorry counterexample or a proved failure in the actual candidate dependency chain.

## References

1. Charles L. Fefferman, [Existence and Smoothness of the Navier–Stokes Equation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
2. Clay Mathematics Institute, [Millennium Prize Problem rules](https://www.claymath.org/millennium-problems/rules/).
3. OpenAI, [NavierStokesAndEuler repository](https://github.com/openai/NavierStokesAndEuler).

## Additional adjudication: import closure and regularity

The selected theorem's import closure contains both `PositiveOrderMoments.Debt` and `FiveRowRank.Debt`, as verified by the zero-sorry `SelectedImportClosureProbe.lean`. This rules out the simplistic claim that the repository lacks a five-row module. It does not prove that the module is the implementation of the paper's five named quantities.

The selected witness is assembled through `ActualCandidateAssembly.selected_witness`, the actual stage-estimate chain, and the germ endpoint. The inspected source has not supplied a theorem identifying `(M,I,J,S,Cp)` with the promoted debt `(0,0,-P,-Jθ,-Jz)` and transporting that identification into the residual estimates. The correct conclusion is that paper-to-endpoint correspondence remains unestablished, not that the exported C/D theorem has been formally contradicted.

One proposed adverse argument is expressly withdrawn. `preSingularDomain = Ico 0 1 × univ` includes the initial face, and `ContDiffOn` is relative to that half-domain. The formal source therefore does not support an initial-time smoothness loophole.

## Revision statement: the moment objection is narrowed

The direct mismatch between the paper-shaped five-coordinate interface and `FiveRowRank` remains a proved type-level fact, but it is not a proof that the repair mechanism fails. `FiveRowPositiveOrderBridgeProbe.lean` is a zero-sorry construction showing that the positive-order repair reduces exactly to the physical-rank repair under the promotion

```text
(P, Jθ, Jz) ↦ (0, 0, -P, -Jθ, -Jz).
```

The probe proves equality of the repair fields and exactness of the five weighted moments for the promoted target. This supersedes any claim that the three-debt interface is, by itself, inconsistent with the five-row repair. The remaining adverse result is an endpoint-level correspondence question: the selected witness must identify `CorrectionState.debt` and `ZeroMasses` with the paper's named quantities and must carry that identification into the residual estimates. Until that theorem is exhibited, the paper-to-code claim remains unestablished. A formal refutation still requires a zero-sorry contradiction on the selected witness path.

## 7. Selected-path construction audit

The remaining question was whether the endpoint obtains convergence, residual flattening, and whole-space localisation from proved premises, or whether one of those properties is simply inserted as an interface assumption. The source does not support the stronger accusation.

`MixedCandidateAssembly.StageEstimates` explicitly stores finite smoothness and jet-rate bounds for every finite residual prefix. `ActualCycleResidualBounds.finite_residual_rates` supplies those bounds from the actual cycle invariant and the constructed physical-field data. `StageEstimates.exists_schedule` then derives a rapidly increasing scale sequence, smooth sums, and vanishing joint residual jets. The selected witness passes these results through `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` and `CandidateConsequences.mixed_exists_force_with_consequences`, which constructs the force and derives its smoothness, PDE, energy, blow-up, and decay consequences.

The whole-space step is not an unexamined scalar cutoff. `SpatialLocalization.localizedVelocity` is curl-generated and has a proved divergence-free property. `R3CompactCandidate` uses local equality of the residual together with compact support, so the localisation argument is intended to preserve the equation on the active region rather than to claim that an arbitrary product cutoff remains incompressible. The quantitative repair route likewise derives coefficient bounds before invoking `ModulatedCone.profiles_trueCone`; the cone condition is not supplied as an unconnected final premise.

These results close several proposed formal disproofs. They do not establish that every analytic estimate in the source is mathematically adequate outside Lean, and they do not supply the missing exposition-level theorem identifying every paper symbol `(M,I,J,S,C_p)` with the promoted physical debt used by the endpoint. That correspondence remains a legitimate publication requirement. It is not, however, a contradiction to the selected C/D proposition.

The counter-paper therefore has a narrower but defensible result. It establishes that the repository-wide claim of a completely admitted-free source tree is false, and that the paper-to-code correspondence is not documented at the level needed for independent mathematical review. It has not established that the selected forced C/D theorem is false. A stronger verdict would require a zero-sorry contradiction or a false mandatory premise on the selected witness path, neither of which has been found in this research pass.

## 8. Selected parameters and proof obligations

The selected-stage block deserves inspection because it fixes one budget and uses that choice to define the potential, direct, and pressure sequences. The source sets `selectedBudget` to `0`, proves the geometric threshold condition, and then applies the witness theorem to those parameters. The three aliases are definitions, not admitted propositions. Their `noncomputable` modifier records that the selected mathematical objects need not be executable algorithms; it does not bypass the kernel.

The value zero also does not mean that the construction has zero stages. Each raw sequence remains a function of `j : ℕ`; the selected budget is a fixed input to the cycle and scale data. A zero-sorry probe verifies these facts directly. Thus this particular suspicion does not falsify the selected endpoint. It becomes a genuine counterexample only if the human argument requires a positive budget, or if a theorem on the selected dependency path proves that the zero choice cannot satisfy a mandatory estimate.

This narrower conclusion matters for the counter-paper. The repository-wide claim of an admitted-free source tree remains false because of the separately identified challenge placeholders, and the paper still needs a source-linked theorem transporting its named moment quantities into the selected residual construction. But neither the selected aliases nor `selectedBudget = 0` currently provide a formal contradiction. The review therefore retains major revision while keeping the endpoint falsification lane open for a precise false premise or contradiction.

## 9. Moment-system audit

The moment audit does not support the claim that the first two zero-moment equations were smuggled into the proof by a type definition. In `FiveRowRank.lean`, `FiveRows` is an explicit conjunction of five radial integral identities. Its repair theorems derive the two zero rows together with the three debt equations. The surrounding rank code connects those rows to actual slow base fields and proves mass preservation. A separate module, `PositiveOrderMoments.lean`, defines a five-coordinate debt from radial integrals and proves exact local repair.

That positive result makes the remaining correspondence issue more exact, not less important. The selected endpoint in `ActualCandidateAssembly.lean` exposes three raw stage sequences and a `Witness` proposition containing the schedule, localised fields, smooth force, PDE consequences, blow-up, decay, and boundary limits. The selected theorem does not itself identify those fields with either moment-repair construction, nor does it map them to the paper’s named tuple `(M, I, J, S, C_p)`. The audit probe compiles the relevant types and records this boundary.

This distinction is central to the counter-paper. A real integral repair subsystem exists, so the accusation of a fake zero-row matrix must be withdrawn. But a paper claiming that its selected endpoint implements a particular five-moment construction must provide a source-linked transport theorem. Until it does, the mathematical correspondence is unverified. The present evidence supports a material reproducibility and exposition defect, not a completed formal disproof of the selected forced claim.

## 10. Residual estimates are derived, not simply assumed

One proposed failure mode was that the selected endpoint might hide its decisive residual estimate by placing it directly in the analytic invariant. Source tracing does not support that allegation. `CycleAnalyticInvariant` stores component estimates and an exact residual decomposition. `ActualCycleResidualBounds.native_residual` derives the native full-residual estimate from those components, including the mean, base, alias, Gaussian, and source contributions. `residual_jetRate` then combines that derived estimate with state-realisation and exterior estimates.

This closes one possible formal disproof route, but only in its narrow form. It does not independently validate the analytic content of the component estimates, nor does it provide the missing source-linked theorem identifying the paper's five named moments with the promoted debt used by the selected endpoint. The counter-paper should therefore distinguish a cleared hidden-premise objection from the still-open correspondence and mathematical-adequacy review.

## 11. Force cutoff and residual extension

The force construction is active through the claimed singular time. In the R³ wrapper, `PositiveTimeForce.timeCutoff` equals one on `[3/8,1]`, including the endpoint, but the cutoff is a genuine smooth bump rather than a step function. The compiled audit probe proves both its endpoint value and continuity of the resulting force trace. The source therefore does not support a discontinuity-based refutation.

The more substantive issue is provenance. `CandidateFromLimits.force` agrees with the activated Navier–Stokes residual throughout `0 ≤ t < 1`. At the endpoint it is defined by a smooth extension whose construction requires locally uniform residual limits and a full boundary-jet family. The upstream theorem derives those limits from its vanishing-jets and away-extension inputs, and the selected witness packages the resulting force, smoothness, support, decay, and endpoint conclusions together.

This makes the force a posteriori in the mathematical construction and raises a legitimate physical and explanatory objection: the candidate motion is selected first and the force is then made to realise its residual. But the objection is not equivalent to proving that the force is singular. A residual can have cancellations, and the formal construction explicitly makes those endpoint limits a proof obligation. The counter-paper therefore requires a concrete zero-sorry failure of those limits or of the stated force predicates before calling the forced C/D theorem formally refuted.

## 12. Adjudication of the force-conservation objection

A proposed counter-strategy was to derive a contradiction from
\(\int_{\mathbb R^3} f\,dx=0\) or \(\nabla\cdot f=0\). That strategy does not follow from the CMI forced formulation. The external body force is not an internal Newtonian stress, so action-reaction cancellation does not require zero net external momentum. Likewise, incompressibility constrains the velocity field; it does not require the body force to be divergence-free.

The implementation audit is consistent with this distinction. `PositiveTimeForce.force` is a smooth temporal cutoff applied to a supplied velocity field and contains no pressure-gradient expression. The pressure gradient is part of `navierStokesResidual`, which `CandidateFromLimits.force` matches for pre-singular times before applying a smooth endpoint extension. Thus active residual forcing is a provenance and physical-interpretation issue, not by itself a failure of the formal C/D predicate.

The counter-paper therefore retains a sharper falsification criterion: a zero-sorry proof that the selected residual lacks the endpoint limits needed for the extension, or that the selected force fails global smoothness, support, rapid derivative decay, PDE equality, or finite-energy requirements. Until such a proof is obtained, the conservation proposal is rejected as a CMI disproof but retained as a review question.

## 13. Pressure localisation and the non-locality objection

The selected R³ candidate does make a strong structural choice: `R3CompactCandidate.pressure`
is built from `SpatialLocalization.cutPressure`, and
`CandidateProperties.pressure_support` requires every pre-singular pressure
slice to have support inside the same compact set as the velocity. The
zero-sorry `AnalyticObjectionsProbe.lean` confirms that this is part of the
exported selected endpoint, not an inference from prose.

This is a legitimate counter-paper question because pressure in the unforced
incompressible equation is recovered non-locally from the velocity. But it is
not, by itself, a formal contradiction to the forced CMI alternative. Here the
body force is not required to be divergence-free, and taking the divergence of
the forced equation leaves the force contribution in the pressure equation.
The Riesz-transform objection becomes decisive only after proving that the
selected force has the additional divergence or independence property needed to
remove that contribution. The current Lean target does not contain that
premise.

The correct adverse demand is therefore source-linked: identify the pressure
Poisson or Leray statement that the paper claims, prove it for the selected
fields, and compare its spatial tail with the compact pressure predicate. Until
that bridge is formalised, this is a load-bearing modelling objection rather
than a completed CMI disproof.

### Pressure-recovery infrastructure

The audit also found real pressure-recovery infrastructure in the repository:
`ConservativeDifference.weak_pressure_poisson`,
`PressureRecoveryHelpers.gradient_poisson_test`,
`PressureRecovery.pressure_gradient_recovery`, and the Riesz test-operator
identities all compile. This changes the precise research question. The issue
is not whether pressure analysis exists: `WholeSpaceUniqueness.classical_uniqueness_on_Icc`
constructs the pressure-recovery hypotheses and obtains the actual pressure-
flux bound, while `candidate_unique_on_Icc` supplies the selected candidate.
The remaining question is whether the analytic estimates have the claimed
whole-space meaning. Their compilation is evidence of a formal derivation,
not by itself a mathematical validation. This lane is therefore an analytic
inspection target, not a current formal disproof.

## 14. Energy balance and temporal gluing

The repository contains the exact identity

\[
\frac{d}{dt}\|u(t)\|_2^2
 =-2\nu\,D(u(t))+2\int_{\mathbb R^3}u(t,x)\cdot f(t,x)\,dx,
\]

in `R3/ViscousEnergyBalance.lean`, together with the derivative theorem used
for time slabs. This removes the broad allegation that the formal code has no
Newtonian dissipation law. The selected endpoint also exposes a uniform finite
energy predicate. A real energy mismatch would require a zero-sorry theorem
showing that the selected fields fail the hypotheses of the identity or violate
its conclusion; the current scan has not produced that theorem.

The temporal gluing route is similarly narrower than a generic “stage kink”
claim. `CandidateFromLimits` constructs the force by
`SpacetimeGluing.smoothExtension`, proves global `ContDiff`, and records every
endpoint derivative through `force_boundary_jets`. The open question is whether
the selected witness supplies the actual locally uniform residual limits and
boundary jets consumed by this construction. That dependency audit remains a
primary falsification target.

The three probes and their compiler outputs are indexed in
`NavierStokesReview/evidence/selected_divergence_audit_2026-09-23.md` and
`NavierStokesReview/results/analytic_objections_probe_2026-09-23.txt`.

## Filter semantics and the residual-limit endpoint

The asymptotic API defines `JetRate` without a `NeBot` parameter. That omission is worth documenting because generic statements over an arbitrary filter can be vacuous. It is not, on the present evidence, a refutation of the selected endpoint: the actual filter at the singular boundary is proved non-vacuous by `JointResidualLimits.past_filter_neBot`, and the zero-sorry `FilterNonVacuityAudit` probe confirms the selected-origin instance. The remaining task is to audit any restricted or comap filters introduced downstream.

## 15. What the semantic audit establishes

The counter-paper's principal objection is now stated at the level of the
selected dependency graph. The production mean-rank construction uses a
three-coordinate debt `(P,Jθ,Jz)` and imposes two zero correction moments.
Independently, the repository contains a five-coordinate positive-order
moment repair with exact integral identities. A zero-sorry Lean probe proves
that the production repair is recovered from the explicit promotion

\[
(P,J_\theta,J_z)\longmapsto(0,0,-P,-J_\theta,-J_z).
\]

This means that a simple dimension-mismatch refutation would overstate the
evidence. The unresolved issue is the semantic bridge: the source audit has
not located a theorem that identifies the paper's five named moments
`(M,I,J,S,C_p)` with the promoted debt and transports that identification
through `StateRealization.chartIdentity`, the residual estimates, and the
selected endpoint. The public consequence bundle does not expose such a
moment-realisation field. The paper therefore still carries a material
formal-correspondence obligation.

## 16. Pressure localisation is a bridge problem, not a trivialisation theorem

The whole-space candidate localises pressure by multiplying it by a smooth
compact cutoff. Its `pressure_support` property says that each pre-singular
slice has support inside a compact set; it does not assert a pressure Poisson
equation or imply that the pressure is zero. The repository's pressure
recovery and Riesz modules prove useful compact-test comparison identities,
and `WholeSpaceUniqueness` constructs those hypotheses for the selected
candidate-versus-competitor comparison. The remaining question is the
analytic validity and whole-space meaning of those estimates, not whether the
selected pressure path is absent.

A zero-sorry probe uses the repository's own nonzero spatial cutoff to prove
that compact support does not imply vanishing. The rigorous counter-paper
claim is therefore that OpenAI must provide the selected-path pressure
recovery/Poisson bridge if the paper relies on one. A generic non-locality
argument cannot be upgraded to a formal disproof while the force term remains
unrestricted by the candidate predicate.

Evidence for Sections 15–16 is collected in
`NavierStokesReview/evidence/semantic_transport_pressure_audit_2026-09-23.md`.

## Editorial control

This paper is the active explanatory account of the review. The fork document
map [`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md) governs which
supporting notes may be cited. Historical logs and unverified agent summaries
are not treated as results; each material conclusion must be backed by source
locations or recorded zero-sorry evidence.
