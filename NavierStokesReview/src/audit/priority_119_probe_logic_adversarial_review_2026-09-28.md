# Priority 119: adversarial review of probe logic

## Purpose

This review checks whether the existing probe conclusions establish facts
about the concrete selected field or only facts about weaker interfaces and
conditional propositions.  It is a logic review of the audit apparatus, not a
new claim about OpenAI's endpoint.

## Findings

| Probe or completion | What is actually proved | What it does not prove | Classification |
| --- | --- | --- | --- |
| `StageEstimatesMomentBlindnessProbe` | A generic `StageEstimates` value does not determine an arbitrary `PositiveOrderMoments.Debt`; a zero-field countermodel inhabits that interface. | The selected concrete stages are zero, or that their moments are wrong. | Interface non-determination |
| `SelectedWitnessAttackBoundaryProbe` | The `Witness` proposition does not entail that every externally supplied `Debt` is zero. | A selected-field moment is nonzero, or that no separately stated theorem can be proved from the selected definitions. | Packaging non-implication |
| `SelectedEndpointMomentTransportObstruction` | The selected `Witness` can coexist with a ghost nonzero `Debt` because `Debt` is not a field of `Witness`. | The ghost payload is the physical moment of the selected velocity. | Type-boundary diagnostic |
| `SelectedCycleMomentTransport` | The selected cycle mean satisfies the two local zero-row identities on the carrier. | Those two rows are the five paper observables, or that the identities survive localization, periodization, `tsum`, and mixed-field assembly. | Upstream/local invariant |
| `SelectedDirectRadialMomentBridge` | The uncut native angular scalar has a zero order-two `barMoment`. | The periodised cut-potential branch has the same moment. | Native-to-production gap |
| `SelectedPotentialProductionRadialScalar` | The selected potential production scalar equals a cutoff-times-curl term plus the cutoff-gradient commutator under explicit regularity hypotheses. | The commutator moment is nonzero. | Exact conditional field identity |
| `SelectedMixedMomentResidualDecomposition` | The mixed order-two moment equals the potential branch plus the direct production branch, under `Shell` hypotheses. | Either branch has a computed value, or the direct branch vanishes. | Exact conditional decomposition |
| `SelectedPeriodicSupportTransportGate` | A periodic selected radial pullback with bounded radial support would be identically zero. | The selected pullback has bounded radial support, or is nonzero. | Conditional contradiction gate |
| `PressureRecoveryAbsolutePremiseProbe` | The comparison hypotheses accept identical zero velocities with identical smooth pressures. | The selected pressure lacks an absolute Poisson representative. | Comparative-vs-absolute scope test |
| `SameDatumFixedForcePerturbation` | A particular admissible perturbation changes the residual while the force is held fixed. | Literal CMI Alternatives (C) or (D) are negated. | Provenance/path-dependence test |

## Concrete blindside closed by Priority 119

The native direct moment theorem is upstream of a spatial cutoff.  The
selected source identity is

\[
  u_{\mathrm{cut},1}(p)
  = c(p)\,u_{\mathrm{native},1}(p),
  \qquad
  u_{\mathrm{cut},1}(p)-u_{\mathrm{native},1}(p)
  = (c(p)-1)u_{\mathrm{native},1}(p).
\]

`SelectedDirectCutoffMomentBoundary.lean` now records this identity directly
for the selected stage.  It also proves that, whenever the cutoff differs
from one and the native component is nonzero, the cut component differs from
the native component.  This is still not a nonzero radial integral: proving
that requires the actual cutoff-weighted `barMoment` of the periodised
`selectedDirectSum` and its `tsum` convergence/support hypotheses.

## Prohibited inference rules

The following rewrites are not licensed by the current source record:

1. `barMoment native = 0` implies `barMoment (cutPotential native) = 0`.
2. `barMoment (curl potential) = 0` implies the cutoff-gradient commutator
   has zero moment.
3. A finite-prefix identity implies the corresponding `tsum` identity.
4. Periodic local equality near the origin implies equality of an unbounded
   radial integral.
5. A ghost `Debt` variable can be identified with a physical selected-field
   observable.
6. A conditional support gate is an endpoint contradiction without both of its
   selected-field premises.

## Current status

The stronger probe is source-written but not compiler-verified until the
review project's missing transitive `.olean` dependencies are rebuilt under
Lean `v4.34.0-rc2`.  No conclusion of `False`, nonzero moment, or formal
refutation is asserted here.
