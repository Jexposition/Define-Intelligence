# Final binary verdict: OpenAI Navier–Stokes claim

Date: 2026-09-23  
Audited public source commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`  
Review branch: `review/cmi-first-navier-stokes-2026-09-22`

## Answer

**NO: this review has not verified OpenAI's claim as a valid mathematical
proof.**

The source does compile and it exports a forced, C/D-shaped proposition. That
is not the same as completing peer review of the analytic construction. The
current evidence supports the narrower statement that Lean checks the stated
formal dependencies. It does not yet justify the stronger statement that the
repository has established a genuine CMI solution.

**NO, for Alternatives A or B.** Those alternatives require `f = 0`, whereas
the audited construction makes the force an active residual of the candidate
flow on every pre-singular time `0 < t < 1`.

## What is established and what is not

1. `NavierStokes.R3.Theorem.theorem_1_1` and the comparator bridge encode a
   forced existential breakdown shape. CMI C/D do permit an external force,
   so residual construction is not by itself a formal CMI contradiction.
2. `CandidateFromLimits.force` is defined through
   `SpacetimeGluing.smoothExtension` of `tracedResidual`. The source proves
   equality with that residual for `t < 1` and proves force zero only for
   `t ≤ 0` or `t ≥ 2`; it does **not** turn the force off before `t = 1`.
3. The pressure/energy route is not merely an unexamined top-level oracle:
   `WholeSpaceComparisonClosure` assembles localized balance, pressure-flux,
   Sobolev, cutoff, and rate estimates. However, the final scalar limit
   theorem consumes a rate premise, and the semantic strength of the
   solution interfaces and derived-filter conditions remains under audit.
4. The generic `JetRate` definition permits bottom-filter proofs without a
   `NeBot` premise. The principal endpoint is separately shown nontrivial,
   but non-vacuity of every derived filter used by the construction is not
   yet closed.
5. Several claims in the supplied drafts cite source paths that are absent
   from this snapshot, including `EnergyDefect.lean`,
   `Forcing/Smoothness.lean`, `Pressure/LerayProjection.lean`, and
   `Scaling/SingularLimits.lean`. Those claims cannot be treated as source
   evidence. The cited zero-division failure is likewise not confirmed by the
   analogous guarded divisions actually inspected.

Accordingly, the correct peer-review status is **NOT ESTABLISHED**, not
“proved” and not yet “formally refuted.” The confirmed result is a set of
semantic corrections and unresolved load-bearing audit obligations.

## CMI status versus theorem status

This report separates proposition shape from mathematical validity. The
official problem statement identifies C and D as valid alternatives, but that
does not certify this particular formal construction. Publication and CMI
procedure are separate questions and are not used here to decide whether the
analytic proof obligations have actually been discharged.

## Evidence

- `NavierStokes/R3/Theorem.lean`
- `NavierStokes/ComparatorR3Theorem.lean`
- `NavierStokes/R3/ComparatorBridge.lean`
- `NavierStokesReview/results/HEADLINE_AXIOMS_4_34_RC2.txt`
- `NavierStokesReview/results/CMI_QUANTIFIER_PROBE_4_34_RC2.txt`
- `NavierStokesReview/results/OPEN_PAST_NEBOT_4_34_RC2.txt`
- `NavierStokesReview/results/SEMANTIC_FINDINGS_2026-09-23.md`
- `NavierStokesReview/results/PRESSURE_ENERGY_CHAIN_2026-09-23.md`
- `docs/OpenAI_NavierStokes_Axiom_Ledger.md`
