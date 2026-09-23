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

## F-012 — Zero-angular repair claim is locally supported and reaches the construction path

Status: `CONFIRMED local algebra and downstream use; physical row-label identification OPEN`

Evidence:

- `NavierStokes/FiveRowRank.lean` explicitly declares the debt order `(P, Jθ, Jz)`, proves the three angular exponents are injective, and defines `FiveRows` as two zero-mass constraints plus three defect-cancellation rows.
- `NavierStokes/CorrectionState.lean:449-476` and `DefectIncrementBounds.lean:776-787` carry those rows into the actual rank increment, rather than leaving them as an unused lemma.
- `NavierStokes/BaseRankPatch.lean:337-352` proves the five rows for the actual final base from the proved patch identities, positivity, and nonzero coefficient/velocity scales.
- `NavierStokes/PositiveOrderMoments.lean` and `FiveProfileMoments.lean` provide a related downstream positive-order repair path with exact moments, invertibility, support, and jet bounds.

Conclusion: the supplied attachment describes a real local repair mechanism and the source proves its downstream use. However, the source's exact row order is `(P, Jθ, Jz)` and its first two `FiveRows` clauses are zero-mass constraints; the attachment's labels `M_theta`, `-P_q`, and `-J_z,q` are not yet shown to be a one-to-one transcription of those declarations. In addition, exact five-row cancellation is only one interface in the larger PDE argument. This is a row-semantics and sufficiency audit, not an absent-code finding.

## F-013 — Five-row assumptions are supplied by the actual geometry, but remain interface boundaries

Status: `CONFIRMED discharged for the inspected final-base call; full PDE sufficiency OPEN`

Evidence:

- `CorrectionInitialization.lean:4413-4431` constructs the rank geometry with positive patch radii, positive lengths, nonzero coefficients and nonzero velocities, and supplies the background/zero-axial patch identities from `BaseRankPatch.rank_fields`.
- `BaseRankPatch.lean:347-352` discharges the corresponding hypotheses directly for the final base using `rankCoefficient_pos`, `rankLength_pos`, `rankVelocity_pos`, and `rank_fields`.
- The theorem still proves only the five weighted integral rows. It does not, by itself, prove the complete residual estimate, pressure compatibility, smooth force extension, or CMI conclusion.

Conclusion: the earlier suggestion that the rank proof merely accepts arbitrary `hV`, `hG`, `hC`, or `hU` at the final call site is not supported by the inspected source. Those assumptions are supplied by proved construction data. The remaining failure-to-claim lane is whether the row identities are sufficient for every later analytic interface, not whether this local call is vacuous.

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

## F-014 — The zero-angular attachment over-specifies the source row semantics

Status: `CONFIRMED description/provenance correction; no local cancellation failure found`

Evidence:

- `NavierStokes/FiveRowRank.lean:93-107` defines `angularDebt` and `axialDebt`
  separately. The angular repair has three generalized-power moments, while
  the axial repair has two.
- `NavierStokes/FiveRowRank.lean:240-246` defines `FiveRows` as five clauses:
  two exact mass constraints, followed by three defect rows for the debt order
  `(P, Jθ, Jz)`.
- `NavierStokes/LocalizedMomentRepair.lean:87-115,164-180` constructs the
  compactly supported bump matrix and proves exact moments from its nonzero
  determinant. The source does not define a named `A_theta` or use the
  attachment's explicit `μ_p e_j^{dp}` matrix notation.
- `NavierStokes/DefectIncrementBounds.lean:635-724,789-825` proves that the
  first two rows preserve the relevant masses and that the final three rows
  solve the linear defects; `rankStage_defectBounds` then consumes that result.

Conclusion: the attachment correctly identifies a real local repair and an
exact zero-mass constraint, but its statement that the source itself exposes a
three-by-three `M_theta, -P_q, -J_z,q` block is not a literal source map. The
closest source-level statement is: a three-moment angular repair plus a
two-moment axial repair jointly establish five rows, with the first two rows
preserving mass and the final three rows cancelling the named debt components.
The row-cancellation chain is used in the actual rank-stage estimate. This
does not establish the full PDE residual or CMI conclusion.
