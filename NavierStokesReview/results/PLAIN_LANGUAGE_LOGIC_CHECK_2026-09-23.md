# Plain-language logic check

Snapshot reviewed: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

## Verdict

The supplied summary is directionally correct as a description of the current audit, but it contains four material overstatements. The precise status is `NOT ESTABLISHED`, not a demonstrated formal refutation.

| Summary claim | Assessment | Source-backed correction |
|---|---|---|
| The code has not verified a valid physical solution to the Millennium problem. | Correct if “physical” means autonomous/unforced fluid dynamics or a completed mathematical peer review. | The source exports a forced C/D-shaped proposition. The review has not verified every analytic premise needed for the full forced CMI claim. This is not evidence for A/B or unforced blow-up. |
| The force is calculated backward from a pre-programmed collapse and remains active up to the singular time. | Substantially correct, with wording tightened. | `CandidateFromLimits.lean:82-112` constructs the force a posteriori from the candidate residual and proves equality for every `0 ≤ t < 1`; `:114-125` proves zero only for `t ≤ 0` and `t ≥ 2`. Say “chosen a posteriori” rather than “backward”, and do not strengthen equality with the residual into a pointwise claim that the force is nonzero at every time. |
| The repository contains the full pressure and five-moment implementation, with no incompleteness in those sections. | Too strong. | The five-row repair is real and reaches the final-base construction: `FiveRowRank.lean`, `CorrectionState.lean`, `BaseRankPatch.lean`, and `CorrectionInitialization.lean` prove and discharge the local hypotheses. The pressure machinery is also real. But local cancellation and pressure lemmas are not the same as a completed PDE/CMI proof; downstream analytic sufficiency remains under review. |
| The omitted nonlinear viscosity and hypo-dissipation would keep velocity bounded and force divergence. | Scope observation only; consequence unproved. | Ladyzhenskaya stress and `alpha < 1` are outside the formalised PDE. The repository makes no theorem about those altered equations, and the audit has not proved boundedness or force divergence there. These are robustness questions, not counterexamples to the classical Newtonian theorem unless separately proved. |
| `JetRate` lacks `NeBot`, so intermediate limits can be vacuous. | Correct as a specification hazard, not yet a fatal theorem defect. | A bottom-filter probe proves arbitrary `JetRate` claims on `⊥`. The endpoint filter is separately non-bottom, but every derived filter such as `originPast ⊓ 𝓟 activeᶜ` still needs an explicit non-vacuity proof. |
| Division-by-zero reports are false. | Too absolute. | No source-confirmed division failure was found in the pinned snapshot. The cited `Scaling/SingularLimits.lean` file is absent, and analogous inspected divisions have guards. A complete denominator census remains open. |

## Zero-angular-momentum attachment

The local algebraic core is present. `PositiveOrderMoments.lean:142-181` defines a three-component `angularDebt` and proves exact angular repair moments. `FiveProfileMoments.lean:202-222` proves the generalized power-moment matrix is invertible for injective exponents, and `:274-285` supplies the three angular exponents and their injectivity. `:356-374` proves the normalized linear-plus-quadratic map identity, with later existence machinery solving the local repair problem.

Therefore the attachment identifies a real three-parameter local repair mechanism, and the actual call path now confirms its use in the final base. The source's exact `FiveRows` order is `(P, Jθ, Jz)`, with two preceding zero-mass constraints, so the attachment's labels `M_theta`, `-P_q`, and `-J_z,q` still need a declaration-level mapping. The five-row theorem also remains only one interface in the full Navier–Stokes residual argument.

## Review conclusion

Use this sentence in the research paper:

> The Lean source contains nontrivial local repair and pressure-analysis components, but the audit has not established that those components jointly prove the full forced CMI conclusion. The a-posteriori force and the missing `NeBot` obligations are genuine semantic review issues; the omitted regularisations and the alleged division failure are, respectively, scope limitations and an unconfirmed concern.
