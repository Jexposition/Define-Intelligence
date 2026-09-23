# OpenAI Navier–Stokes Counter-Paper Evidence Tracker

This document is the working ledger for the counter-paper. It records evidence, status, and the next falsification test. It is intentionally a tracker. The argument itself is written in `OpenAI_NavierStokes_Research_Paper.md`.

## Scope

- Upstream source under review: OpenAI Navier–Stokes repository, snapshot recorded as `f9e8bc5`.
- Review branch: `review/cmi-first-navier-stokes-2026-09-22`.
- Formal environment: Lean 4.32 through the local elan installation.
- Boundary: the OpenAI source tree is not edited. Review probes live under `NavierStokesReview/src/probes`.

## Current position

The repository contains a genuine R³ C/D-shaped endpoint and the headline theorem reports only standard Lean axioms. The strongest adverse result is a formal correspondence failure: the selected repair pipeline uses `FiveRowRank`, whose declared exponent vectors differ from the vectors stated in the official paper's Appendix A. The final theorem is not labelled refuted until the missing bridge is shown impossible or its absence is shown to invalidate a mandatory witness premise.

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

## Formal artefacts

- `NavierStokesReview/src/probes/MomentCoordinateMismatchProbe.lean`: zero-sorry vector inequalities.
- `NavierStokesReview/src/probes/MainAxiomProbe.lean`: endpoint axiom report.
- `NavierStokesReview/src/probes/JetRateVacuityProbe.lean`: generic filter-vacuity witness.
- `NavierStokesReview/src/probes/OriginPastNeBotProbe.lean`: non-vacuity of the concrete origin-past filter.
- `NavierStokesReview/src/probes/OpenPastNeBotProbe.lean`: non-vacuity of a concrete open-past filter.

## Decision rule

Use “formal disproof” only for a zero-sorry contradiction or a demonstrated false premise on the selected witness path. Use “correspondence failure” when the code proves a different proposition or leaves a required bridge absent. Use “semantic criticism” for physical objections that are outside the literal C/D statement.
