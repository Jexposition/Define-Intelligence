# Input Document Synthesis for the Navier–Stokes Counter-Paper

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

That finding is now carried consistently into the plan, ledger, tracker, peer review, and research paper.
