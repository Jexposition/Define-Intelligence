# A Formal Audit of OpenAI's Navier–Stokes Blow-Up Claim

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

Two `sorry` declarations remain in each of the separate Comparator challenge files. Source and dependency inspection did not place those declarations on the selected R3 endpoint path. They must remain visible in the axiom ledger, but they cannot be used as a refutation of the headline theorem without a transitive dependency witness.

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

## Revision statement: the moment objection is narrowed

The direct mismatch between the paper-shaped five-coordinate interface and `FiveRowRank` remains a proved type-level fact, but it is not a proof that the repair mechanism fails. `FiveRowPositiveOrderBridgeProbe.lean` is a zero-sorry construction showing that the positive-order repair reduces exactly to the physical-rank repair under the promotion

```text
(P, Jθ, Jz) ↦ (0, 0, -P, -Jθ, -Jz).
```

The probe proves equality of the repair fields and exactness of the five weighted moments for the promoted target. This supersedes any claim that the three-debt interface is, by itself, inconsistent with the five-row repair. The remaining adverse result is an endpoint-level correspondence question: the selected witness must identify `CorrectionState.debt` and `ZeroMasses` with the paper's named quantities and must carry that identification into the residual estimates. Until that theorem is exhibited, the paper-to-code claim remains unestablished. A formal refutation still requires a zero-sorry contradiction on the selected witness path.
