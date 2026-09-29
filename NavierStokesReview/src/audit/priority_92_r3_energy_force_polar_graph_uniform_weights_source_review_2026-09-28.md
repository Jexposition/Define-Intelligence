# Priority 92 source review: R3 energy/force, polar graph, and uniform weights

Date: 2026-09-28
Scope: seven reachable Lean modules reviewed directly from `NavierStokes/`.

## Modules reviewed

| Module | What the source actually proves | Correspondence status |
|---|---|---|
| `R3/ForceL2Norm.lean` | Defines `l2Norm` and `cumulativeForceNorm`; proves continuity, interval integrability, derivative, nonnegativity, monotonicity, and the square-integral identity. | Genuine R3 force accounting; no selected radial moment theorem. |
| `R3/IntegratedDissipation.lean` | Proves integrated energy balance, force-work bounds, candidate dissipation integrability, L2 control by cumulative force, uniform kinetic-energy bounds, and total dissipation bounds. | Real `CandidateProperties` energy consequences; no five-observable transport. |
| `R3/PositiveTimeForce.lean` | Defines a smooth time cutoff, equal to one on `[3/8,1]`, zero outside `[1/16,21/16]`, and proves compact positive-time support for the cut-off force. | Confirms smooth temporal localisation; the discontinuous-cutoff objection is not supported. |
| `R3/ScalarEnergyBound.lean` | Proves weighted, unweighted, and uniform forced Gronwall estimates. | Abstract scalar estimate; not a field-level moment or pressure result. |
| `R3/ViscousEnergyBalance.lean` | Proves the compact-support viscous energy identity with viscosity and force work, its derivative form, force-work continuity, and slab regularity. | Real Newtonian energy layer under explicit hypotheses; no selected Cartesian moment transport. |
| `ResidualPolarGraph.lean` | Defines physical radial projection, local angle, cylindrical reconstruction, chart identities, positivity, and eventual chart-domain membership. | Genuine off-axis coordinate bridge; no global radial tuple or origin-to-global closure. |
| `UniformPrimaryWeights.lean` | Propagates uniform weighted classes through products, covariance weights, primary coefficients, cylindrical curls, curl remainders, phase data, cutoffs, and wave corrections. | Substantive uniform regularity/curl-rate infrastructure; output remains rate classes rather than `barMoment` equality. |

## Source-grounded findings

1. The R3 energy chain is stronger than a generic placeholder. `IntegratedDissipation` consumes `ProblemStatement.CandidateProperties` and derives concrete integrability and energy inequalities. This reinforces the earlier conclusion that kinetic-energy packaging is not the principal correspondence failure.

2. `PositiveTimeForce` explicitly proves smooth temporal cutoffs and compact support. It removes the earlier discontinuous-cutoff attack surface, but it does not resolve force provenance or the paper-to-field transport question.

3. `ResidualPolarGraph` supplies a real scaled physical-to-cylindrical chart reconstruction, but its hypotheses are local/off-axis chart-domain hypotheses. It is not a theorem identifying the final selected Cartesian field with the five paper observables over the full radial domain.

4. `UniformPrimaryWeights` is a major rate-propagation layer. Its final declarations produce `UniformClass` and `UniformWaveClass` estimates for curls, remainders, phase constructions, and cutoffs. Those rates are mathematically meaningful, but a rate class is not by itself a theorem of the form

   \[
   \operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p).
   \]

5. No module in this tranche proves `Delta m != 0`, an impossibility result, or `False`. The correct classification remains a selected-field transport question, not a kernel contradiction.

## Impact on the audit

This tranche updates the correspondence map in both directions. It records positive evidence for energy, smooth forcing localisation, off-axis chart reconstruction, and uniform curl/rate propagation. It also sharpens the remaining boundary: those results must still be composed with the actual selected `ASum`/`BSum`/`PSum` field and the paper's radial observables before the paper-to-code claim can be accepted.

Evidence anchors are recorded in `semantic_coverage_register.py` and the regenerated semantic coverage register.
