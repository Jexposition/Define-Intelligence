# Independent peer review of the OpenAI Navier–Stokes formalisation

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
