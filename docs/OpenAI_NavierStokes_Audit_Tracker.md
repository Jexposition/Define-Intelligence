# OpenAI Navier–Stokes Counter-Paper Evidence Tracker

This document is the working ledger for the counter-paper. It records evidence, status, and the next falsification test. It is intentionally a tracker. The argument itself is written in `OpenAI_NavierStokes_Research_Paper.md`.

## Scope

- Upstream source under review: OpenAI Navier–Stokes repository, snapshot recorded as `f9e8bc5`.
- Review branch: `review/cmi-first-navier-stokes-2026-09-22`.
- Formal environment: the repository-declared Lean 4.34.0-rc2 through the local elan installation. The separate V-lab `packages-4.32` cache was not substituted because this fork pins matching 4.34.0-rc2 Mathlib and Comparator revisions.
- Boundary: the OpenAI source tree is not edited. Review probes live under `NavierStokesReview/src/probes`.

## Current position

The repository contains a genuine R³ C/D-shaped endpoint and the headline theorem reports only standard Lean axioms. The strongest adverse result is a formal correspondence failure: the selected repair pipeline uses `FiveRowRank`, whose declared exponent vectors differ from the vectors stated in the official paper's Appendix A, while other selected branches use `FiveProfileMoments`. A zero-sorry theorem now rules out a direct row-by-row bridge for arbitrary parameters. The final theorem is not labelled refuted until a nontrivial bridge is shown impossible or its absence is shown to invalidate a mandatory witness premise.

## Evidence register

| ID | Claim or question | Evidence | Status | Next action |
| --- | --- | --- | --- | --- |
| CTR-001 | The source is only a periodic toy. | `NavierStokes/R3/ProblemStatement.lean` defines whole-space fields, compact support, finite energy, and unbounded speed. | Closed: objection rejected | Keep the R³ distinction in the paper. |
| CTR-002 | The force is active and residual-defined. | Official paper Section 2 and the R³ force definitions construct the force from the momentum residual through the collapse. | Confirmed semantic criticism, not C/D refutation | Audit smooth extension and decay directly. |
| CTR-003 | The endpoint hides custom axioms. | `MainAxiomProbe.lean` reports `propext`, `Classical.choice`, and `Quot.sound` only. | Closed for the inspected endpoints | Continue premise and correspondence inspection. |
| CTR-004 | Generic `JetRate` can be vacuous. | `JetRateVacuityProbe.lean` proves a `Filter.bot` limit can discharge the generic predicate. | Live hazard, not yet endpoint failure | Trace a non-bottom proof into every selected rate premise. |
| CTR-005 | The complete Lean pipeline is one coherent implementation of the paper's five-moment system. | `FiveProfileMoments.lean` contains the paper-shaped vectors, while `FiveRowRank.lean` declares `(2, -2 - 2λ, -2λ)` and `(1, 1 - 2λ)`. The zero-sorry probe proves the two source vectors are not definitionally equal. | Formal correspondence gap unless a bridge exists | Locate or formalise the bridge between the two systems. |
| CTR-006 | Both moment interfaces reach the selected construction. | `MeanRankUpdate` consumes `FiveRowRank`; `ModulatedHistories` and `ReservedPatches` consume `FiveProfileMoments`; actual candidate modules import both branches. | Confirmed mixed path | Map every row, debt, coefficient, and scaling between branches. |
| CTR-007 | Non-Newtonian regularisation disproves the Newtonian theorem. | The published endpoint is Newtonian and C/D allows smooth force. | Rejected as internal refutation | Retain only as a physical robustness limitation. |
| CTR-008 | The two moment declarations may be treated as the same system by direct identification. | `MomentBridgeObstructionProbe.lean` proves `¬ DirectMomentBridge lam b` for all real `lam` and `b`, by evaluating the first axial coordinate. | Formally disproved at the direct-correspondence level | Require an explicit nontrivial change-of-variables theorem. |
| CTR-009 | The selected witness hides a custom axiom at the stage-estimate interface. | `SelectedDependencyAxiomProbe.lean` reports only `propext`, `Classical.choice`, and `Quot.sound` for `selected_witness`, `physicalData`, `actualStageEstimates`, and `Invariant.residual_jetRate`. | Closed for custom-axiom suspicion | Continue semantic and interface audit; do not treat standard axioms as defects. |
| CTR-010 | The two debt interfaces admit a direct full linear identification. | `MomentBridgeObstructionProbe.lean` proves `¬ Nonempty (FiveRowRank.Debt ≃ₗ[ℝ] FiveProfileMoments.Debt)` by finite-dimensional rank. | Formally disproved for full linear identification | Require an explicit constrained embedding or stage-separation theorem. |

## Formal artefacts

- `NavierStokesReview/src/probes/MomentCoordinateMismatchProbe.lean`: zero-sorry vector inequalities.
- `NavierStokesReview/src/probes/MomentBridgeObstructionProbe.lean`: zero-sorry impossibility of a direct row-by-row bridge.
- `NavierStokesReview/src/probes/MainAxiomProbe.lean`: endpoint axiom report.
- `NavierStokesReview/src/probes/SelectedDependencyAxiomProbe.lean`: selected-path interface axiom report.
- `NavierStokesReview/src/probes/JetRateVacuityProbe.lean`: generic filter-vacuity witness.
- `NavierStokesReview/src/probes/OriginPastNeBotProbe.lean`: non-vacuity of the concrete origin-past filter.
- `NavierStokesReview/src/probes/OpenPastNeBotProbe.lean`: non-vacuity of a concrete open-past filter.

## Decision rule

Use “formal disproof” only for a zero-sorry contradiction or a demonstrated false premise on the selected witness path. Use “correspondence failure” when the code proves a different proposition or leaves a required bridge absent. Use “semantic criticism” for physical objections that are outside the literal C/D statement.
