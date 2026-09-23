# Semantic findings from source inspection

Snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd` (OpenAI upstream, 2026-09-10)

Review branch: `review/cmi-first-navier-stokes-2026-09-22`

This file records source-backed findings. A compilation result is not treated as evidence that the encoded proposition matches an autonomous physical blow-up claim.

## F-001 — A-posteriori residual forcing is built into the candidate construction

Status: `CONFIRMED semantic feature; not yet a formal CMI failure`

Evidence:

- `NavierStokes/CandidateFromLimits.lean:82` defines `force` as
  `SpacetimeGluing.smoothExtension 1 (tracedResidual u p L) ...`.
- `NavierStokes/CandidateFromLimits.lean:108-112` proves that this force equals the activated Navier–Stokes residual for every `0 ≤ t < 1`.
- `NavierStokes/R3/ProblemStatement.lean:101-107` requires only existence of a force satisfying smoothness and the residual identity. It does not require the force to be prescribed independently of the candidate velocity.

Interpretation: the Lean result may encode an existential forced alternative C/D statement, because CMI's forced alternatives quantify over the existence of suitable `u₀` and `f`. It does not establish that the velocity evolves autonomously and that an external driver was specified independently before the velocity was chosen. Therefore claims that this formalisation proves an autonomous physical instability, or proves alternatives A/B, are unsupported by this construction.

Required follow-up: document the construction as `a posteriori residual forcing` and keep it separate from any claim of unforced or causally independent blow-up.

## F-002 — The force is not shown to be off before the singular time

Status: `CONFIRMED overclaim in supplied review drafts`

Evidence:

- `NavierStokes/CandidateFromLimits.lean:99-108` proves equality with the past residual, including the activated residual throughout `0 ≤ t < 1`.
- `NavierStokes/CandidateFromLimits.lean:114-125` proves zero forcing only from `t ≥ 2`, plus zero forcing for `t ≤ 0`.
- `NavierStokes/R3/ProblemStatement.lean:102` requires compact positive-time support, which does not mean support ends before `t = 1`.

Conclusion: the source does not support the statement repeated in the supplied `Analysis.md` and `Critical Peer-Review and Verification Blueprint...md` that the force is turned off before `T* = 1` and the remaining blow-up is unforced. The actual source supports forcing through the entire pre-singular interval and only guarantees a future cutoff after the singular time.

CMI effect: this does not refute alternatives C/D, since their force is allowed to be time-dependent and smooth. It does refute the stronger narrative that the repository has demonstrated a force-independent or post-forcing singularity.

## F-003 — The generic `JetRate` interface admits bottom-filter proofs

Status: `CONFIRMED specification hazard; headline impact remains OPEN`

Evidence:

- `DiagonalResidual.JetRate` has the form `∃ C, ∀ᶠ x in l, ...` and has no `NeBot l` hypothesis.
- The independent probe `NavierStokesReview/src/probes/JetRateVacuityProbe.lean` proves arbitrary `JetRate` claims on `⊥`.
- The main endpoint filter `originPast` is separately shown nontrivial in `NavierStokesReview/src/probes/OriginPastNeBotProbe.lean`.
- `ActualCycleResidualBounds.lean:956-985` consumes a derived filter `originPast ⊓ 𝓟 Sᶜ`; the source review has not yet established a general non-bottom theorem for every such derived filter.

Conclusion: this is a real weakness in the specification API. It is not yet a demonstrated false CMI conclusion, because the headline route uses the non-bottom endpoint filter and the actual geometry may supply the needed exterior neighbourhood. The missing audit obligation is an explicit non-vacuity proof at every derived filter used to obtain the residual rates.

## F-004 — Several named audit files in the supplied drafts are not present in this snapshot

Status: `CONFIRMED provenance error in review drafts`

Evidence:

- The source tree contains `NavierStokes/CandidateFromLimits.lean`, `NavierStokes/JointResidualLimits.lean`, `NavierStokes/R3/PressureRecovery.lean`, and `NavierStokes/CompactForceDecay.lean`.
- It does not contain the draft-cited paths `NavierStokes/Forcing/Smoothness.lean`, `NavierStokes/Pressure/LerayProjection.lean`, `NavierStokes/Scaling/SingularLimits.lean`, or `EnergyDefect.lean`.

Conclusion: claims attributed to those paths cannot be used as evidence until mapped to actual declarations in the snapshot. In particular, the supplied drafts' assertions that a named Leray projection or `EnergyDefect` bottom-filter theorem was checked are not source-backed as written.

## F-005 — Energy-rate input is not the same as a formally derived energy identity

Status: `CONFIRMED overstatement in supplied drafts; source chain substantially traced`

Evidence:

- `NavierStokes/R3/WholeSpaceEnergyLimit.lean:57-69` describes the weighted differential estimate as an explicit input and says that deriving it from the PDE and pressure is separate.
- The theorem `eq_zero_of_weighted_rate_bound` consumes `hrate` as a hypothesis; it does not derive `hrate` from the Navier–Stokes equation.
- The supplied drafts state that convective skew-symmetry and viscous energy identities were formally verified, but no source declaration with that claimed role has been located in the pinned Navier–Stokes tree.

Conclusion: the documents must not report the energy identity as independently verified merely because the uniqueness closure compiles. The final scalar theorem consumes a rate bound, but the whole-space closure does assemble that bound from explicit localized PDE balance, Sobolev/cutoff estimates, and pressure-flux estimates. Therefore this finding is an overstatement in the supplied drafts, not by itself a missing-premise refutation of the repository theorem. The remaining audit is whether every pressure-recovery and finite-energy hypothesis is genuinely supplied by the candidate/competitor interfaces.

## F-006 — The whole-space uniqueness bridge is conditional on a strong competitor interface

Status: `CONFIRMED conditional structure; not yet a false theorem`

Evidence:

- `NavierStokes/R3/WholeSpaceUniqueness.lean:28-68` constructs `PressureRecovery.Hypotheses` from smoothness, divergence-free equations, and uniform finite energy, obtains the difference `L²`, reference `L³`, and tensor `L¹` bounds, then invokes `PressureFlux.exists_uniform_actual_pressure_flux_bound`.
- `NavierStokes/R3/WholeSpaceComparisonClosure.lean:32-157` derives the rate inequality from `LocalizedDifferenceEnergy.difference_energy_balance`, the pressure-flux hypothesis, and explicit cutoff/Sobolev bounds before applying `WholeSpaceEnergyLimit.eq_zero_of_weighted_rate_bound`.
- `NavierStokes/R3/PressureRecovery.lean` defines the pressure-recovery hypotheses as an equality of the two residual equations together with smoothness, divergence-free conditions, and finite-energy bounds.

Interpretation: the source does not simply assume the final rate inequality at the point where uniqueness is concluded. However, the conclusion is only as strong as the `GlobalFiniteEnergySolution`/`PressureRecovery.Hypotheses` interface. The peer review must therefore audit the exact definition of “smooth global solution” and “bounded energy” against every regularity and integrability condition used by the pressure and localized integration lemmas. Compilation of this bridge does not prove that those interfaces capture all analytic requirements of the classical CMI formulation.

## F-007 — The cited zero-division concern is not presently a source-confirmed failure

Status: `OPEN concern; analogous divisions are guarded`

Evidence:

- The cited `NavierStokes/Scaling/SingularLimits.lean` path is absent from the snapshot.
- In the inspected analogous scaling code, `NavierStokes/ActivationContinuation.lean`, the substantive division lemmas require `0 < A` and `0 < κ` or the corresponding nonzero hypotheses.
- The repository uses Lean's total division semantics, but the audited downstream theorems either carry positivity/nonzero premises or state identities that remain algebraically valid under the totalized value at zero.

Conclusion: the review should not claim a division-by-zero defect without locating a theorem whose proof uses an unguarded denominator in a singular-limit argument. The missing named file remains a provenance problem; the mathematical guard audit remains open.

## Current disposition

The present evidence supports this narrower statement:

> The repository contains a formal forced C/D-shaped target and a substantial candidate/bridge development. It does not, on the evidence inspected so far, establish an autonomous unforced Navier–Stokes blow-up, and the supplied documents overstate the force-off-before-singularity mechanism. The residual-limit and comparison estimates remain the load-bearing analytic audit lane.

No `[REFUTED]` seal is issued here. F-002 is a confirmed correction to the claim description. F-003 and F-007 remain open proof-content audits, while F-005 is now narrowed to a confirmed overstatement rather than an alleged missing energy derivation.

## F-008 — Five-moment repair is present, but local algebra is not the whole PDE proof

Status: `CONFIRMED source correction; downstream consequence OPEN`

Evidence:

- `NavierStokes/FiveProfileMoments.lean` contains the five-profile patch,
  determinant nonvanishing, a linear equivalence, normalized repair, physical
  moment identities, support statements, and jet bounds.
- The module is imported on the construction path through
  `MeanRankUpdate`, `ModulatedHistories`, `ModulatedCone`,
  `ModulatedProfileAssembly`, and `ConstructedSlowBase`.

Conclusion: the supplied allegation that the five-equation repair system is
absent or merely asserted is not supported. The remaining review question is
whether the local repaired moments are correctly propagated into the finite
identities, stress cancellation, and full Navier–Stokes residual estimates.

## F-009 — The cited Fourier pressure file is not the direct headline import path

Status: `CONFIRMED provenance correction; pressure validity OPEN`

Evidence:

- `NavierStokes/R3PressureFourier.lean` contains genuine Riesz-symbol,
  Poisson, and pressure `L²` results.
- The headline R3 uniqueness route imports the `R3/RieszTestOperators`,
  pressure-recovery, and pressure-flux hierarchy; it does not establish the
  separate `R3PressureFourier.lean` file as the direct proof path.

Conclusion: pressure formalisation is not absent. The supplied documents must
not attribute the headline pressure argument to a file that is not shown to be
on that import path. The actual imported hierarchy and each of its analytic
hypotheses remain subject to review.

## F-010 — Ladyzhenskaya and hypodissipative tests are outside the claimed source scope

Status: `CONFIRMED scope limitation`

No source theorem was found for the Ladyzhenskaya stress tensor with `p ≥ 3`,
or for a dissipation exponent `α < 1`. The headline theorem uses the classical
Newtonian positive-viscosity route. These omissions prevent robustness claims
for altered PDEs, but they are not counterexamples to a theorem stated for the
classical forced equation.

## F-011 — The actual singular formula is guarded; the cited division defect is unconfirmed

Status: `OPEN concern; no source-confirmed failure`

The cited `NavierStokes/Scaling/SingularLimits.lean` path is absent. The actual
origin statement in `ConstructedSlowBase.lean` uses a guarded hypothesis
`t < 1` with `(1-t)^(-A)`, and inspected moment/scaling divisions carry
positivity or nonzero premises. A complete denominator census is still
required, but the pasted zero-division allegation is not presently a proven
failure.

The six-question disposition and required follow-up checks are collected in
`NavierStokesReview/results/SIX_QUESTION_SOURCE_AUDIT_2026-09-23.md`.
