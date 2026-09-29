# Priority 124: selected dynamics, comparator, and appendix review

Date: 2026-09-28
Scope: ten queued Navier–Stokes modules selected because they can carry endpoint dynamics, appendix identities, comparator semantics, finite sums, or endpoint jets.

## Findings

| Source | Source-level result | Bridge status |
|---|---|---|
| `NavierStokes/ActualParticularDynamicsNoOptions.lean` | Proves selected principal dynamics from carrier, geometry, wave-class, patch, radius, time, and source hypotheses. | Concrete selected dynamics are present. The inspected theorem does not conclude a final `barMoment` or five-observable identity. |
| `NavierStokes/BaseWitnessClosure.lean` | Retains the actual profile, outgoing parameters, axis parameters, scale order, cone certificate, finite slow identities, threshold order, and selected initial cycle invariant. | This closes real base/initialisation data. It does not transport the final Cartesian field to `(M,I,J,S,C_p)`. |
| `NavierStokes/AppendixHeatResults.lean` | Proves rising-factorial, gamma, endpoint-jet, and heat-profile remainder bounds, including an upstream `moment_zero` use. | Upstream heat/profile identity and jet estimates are real; no final selected-field radial observable theorem is exported here. |
| `NavierStokes/AppendixJoiningResults.lean` | Proves explicit axis margins, source cancellation identities, denominator positivity, and reference-profile lower bounds. | Joining/axis bounds are real scalar/profile results; they do not identify final Cartesian `barMoment` values. |
| `NavierStokes/CommonCoverWithin.lean` | Proves localised-copy smoothness, finite locally-common-torus sums, and one-sided boundary jet limits. | This is genuine finite-sum and jet transport. It is not a five-observable transport theorem. |
| `NavierStokes/CompactHolomorphicFamily.lean` | Proves evaluation commutes with circle integrals and upgrades pointwise holomorphic evaluations to a compact-valued holomorphic family. | Complex-analysis infrastructure; no selected Navier–Stokes radial observable. |
| `NavierStokes/ComparatorR3Bridge.lean` | Defines a whole-space global solution predicate and proves residual, divergence, initial-data, integrability, and bounded-energy transport from comparator coordinates, including viscosity rescaling. | This is a substantive \\(\mathbb R^3\\) comparator bridge. It is not a selected witness moment bridge and does not add force-independence. |
| `NavierStokes/ComparatorSolution.lean` | Packages whole-space and periodic comparator breakdown statements and prints endpoint axioms for the periodic comparator theorem. | Endpoint comparator semantics are real; no paper five-moment field equality is present. |
| `NavierStokes/EndpointLimits.lean` | Constructs smooth left endpoint extensions from successive derivative limits and states the separate right-branch hypotheses needed for two-sided gluing. | This distinguishes proved left-side regularity from an assumed right branch; it is not an origin-to-global moment theorem. |
| `NavierStokes/FlatPrimitivePaper.lean` | Constructs compactly supported smooth factors and local coefficient extension bounds on compact rectangles. | Local cutoff machinery is real; it does not establish preservation of global radial observables. |

## Important source anchors

- `ActualParticularDynamicsNoOptions.lean:48-80`: exact selected fast-direction calculation.
- `ActualParticularDynamicsNoOptions.lean:82-95`: selected-principal theorem inputs include carrier, wave-class, patch, radius/time positivity, and geometry hypotheses.
- `BaseWitnessClosure.lean:22-36`: actual profile and outgoing parameter facts.
- `BaseWitnessClosure.lean:39-73`: axis/scale/cone/axis-pressure compatibility.
- `BaseWitnessClosure.lean:89-96`: smooth coefficients and finite slow identities.
- `BaseWitnessClosure.lean:100-131`: selected threshold and initial cycle invariant.
- `AppendixHeatResults.lean:49-166`: derivative coefficients, endpoint jets, remainder/positivity bounds, and heat-profile estimates.
- `AppendixJoiningResults.lean:17-80`: axis margins, source identity, denominator lower bound, and reference lower bound.
- `CommonCoverWithin.lean:84-125`: cutoff-localised representatives, finite local torus sums, and boundary jet limits.
- `CompactHolomorphicFamily.lean:13-40`: evaluation/circle-integral interchange and holomorphic-family regularity.
- `ComparatorR3Bridge.lean:24-32`: `GlobalSolutionRn` predicate with smoothness, zero initial data, divergence, residual, `MemLp`, and bounded energy.
- `ComparatorR3Bridge.lean:34-47`: comparator residual equation in physical coordinates.
- `ComparatorR3Bridge.lean:49-80`: viscosity rescaling into the whole-space predicate.
- `ComparatorSolution.lean:16-32`: whole-space/periodic comparator breakdown packaging and endpoint axiom print.
- `EndpointLimits.lean:137-167`: endpoint jets and the explicit right-branch assumptions required for two-sided gluing.
- `FlatPrimitivePaper.lean:17-100`: smooth compact-support factor and local coefficient extension.

## Hardened classification

This tranche confirms further genuine mathematics in the selected infrastructure:

1. The construction has real selected dynamics, base closure, comparator transport, finite local sums, and endpoint-jet machinery.
2. The comparator bridge is not an empty wrapper: it explicitly carries smoothness, residual equality, incompressibility, integrability, and bounded energy.
3. The appendix and profile identities are not being dismissed as dead code.

The tranche still does not expose a declaration proving

\[
\operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p)
\]

after the complete selected Cartesian/periodic construction. It also does not prove a nonzero defect or `False`. Therefore it strengthens the evidence map but does not change the classification from **CTR-005: selected paper-to-code observable correspondence not established**.

## Anti-blindside corrections

- `moment_zero` in a heat/profile theorem is not automatically the moment of the final selected Cartesian field.
- A comparator residual/energy bridge is not a selected-profile transport theorem.
- A finite locally common-torus sum and one-sided jet limit are not an infinite selected `tsum` radial integral identity.
- A left endpoint extension theorem does not prove the existence of an independent right branch or a global origin chart transport.
- A compact smooth cutoff factor does not imply preservation of the five global observables.

The remaining search must match declaration signatures and bodies to the concrete selected composition, not merely to words such as `moment`, `bridge`, `sum`, `periodic`, or `curl`.
