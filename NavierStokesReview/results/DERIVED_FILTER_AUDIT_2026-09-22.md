# Derived-filter audit

## Result

The helper predicate `DiagonalResidual.JetRate` is domain-weak: it accepts an
arbitrary filter and has no `NeBot` premise. On the bottom filter, every
eventual proposition is true, so the rate predicate can be proved without a
derivative estimate. `src/probes/JetRateVacuityProbe.lean` establishes this
with no `sorry`.

The review also checked the main endpoint. `GlobalBaseError.originPast` is
proved nontrivial by `src/probes/OriginPastNeBotProbe.lean`. However, that fact
does not automatically transfer to a derived filter such as
`originPast ⊓ 𝓟 activeᶜ`: the zero-sorry `DerivedFilterAudit.lean` gives the
counterexample `⊤ ⊓ 𝓟 univᶜ = ⊥`.

## Why this is not yet a CMI refutation

The main selected-rate lemma does not simply consume the exterior rate on the
derived filter. It rewrites eventuality over
`originPast ⊓ 𝓟 Sᶜ` and then splits into `w ∈ S` and `w ∉ S`. The selected-region
branch uses the independently supplied selected bound; the exterior branch
uses the base rate. Therefore the generic `JetRate` weakness is a formal
specification hazard and an audit obligation, not evidence that the exported
CMI theorem is vacuous.

The remaining concrete question is geometric: whether the actual `activeᶜ`
branch is frequent near the endpoint. The current theorem does not need that
fact for the Boolean branch combination, but proving it would make the
exterior estimate independently substantive rather than merely conditional.

## Source evidence

- `NavierStokes/DiagonalResidual.lean`: `JetRate` is an eventual inequality
  over a caller-supplied filter.
- `NavierStokes/ActualCycleResidualBounds.lean:555-575`:
  `base_exterior_jetRate` uses `originPast ⊓ 𝓟 activeᶜ`.
- `NavierStokes/ActualCycleResidualBounds.lean:956-985`:
  `selected_residual_jetRate` combines the selected and exterior branches.
- `NavierStokes/GlobalBaseError.lean` and `JointResidualLimits.lean`:
  `originPast` itself is nontrivial.

Classification: `FORMAL SPECIFICATION HAZARD`, not a demonstrated CMI
statement mismatch.
