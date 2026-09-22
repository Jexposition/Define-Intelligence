# CMI semantic requirement matrix

Date: 2026-09-22  
Audited commit: `d22a07e66928213ecec94baa3165857431b13869`  
Upstream source commit contained by the fork: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

Controlling specification: [Clay Mathematics Institute statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf). The CMI statement explicitly permits smooth external forcing in alternatives C and D. The repository is therefore tested against the forced alternatives, not against the unforced alternatives A and B.

## Requirement-by-requirement result

| CMI requirement | Lean encoding and evidence | Result |
|---|---|---|
| Every `ν > 0` | `coreBreakdownStatement` and the exported Comparator theorems quantify over positive viscosity. The R3 construction is rescaled to arbitrary positive viscosity. | Confirmed at proposition and source level |
| Smooth divergence-free initial data | `InitialVelocityConditionDecay` contains `ContDiff`, divergence-free, and all derivative decay. The exported witness uses the zero field. `CMIForceBridgeProbe.lean` independently elaborates the zero-data theorem. | Confirmed for the selected datum |
| Whole-space force class | `ForceConditionDecay` requires relative smoothness on `R³ × [0,∞)` and all mixed space-time derivative decay. `forceConditionDecay_of_compact` derives it from global smoothness, compact spatial support, and compact future-time support. `CMIForceBridgeProbe.lean` independently elaborates this bridge. | Confirmed at Lean-predicate level |
| Classical Newtonian PDE | The residual is `∂ₜu + (u·∇)u - νΔu + ∇p`; the bridge transfers it to the Comparator equation. No fractional or hypo-dissipative operator appears in the audited R3 route. | Confirmed |
| Smooth global competitor | `NavierStokesExistenceAndSmoothnessRn` requires relative `C∞` velocity and pressure on the full nonnegative-time domain, divergence-free condition, initial data, PDE, square integrability, and a uniform energy bound. | Confirmed at predicate level |
| Energy condition | The Comparator class requires finite square-integrability at every time and a uniform bound on the full-space integral. The R3 bridge converts it to the explicit `UniformFiniteEnergy` record, preserving integrability rather than relying on a totalised integral alone. | Confirmed |
| Finite-time breakdown | The internal candidate has smooth fields on `0 ≤ t < 1`, compact spatial support, bounded energy before one, and `SpeedUnboundedAtOne`. The contradiction bounds a smooth global competitor on `Icc 0 1 × K`, not by an invalid `L²` to `L∞` argument. | Confirmed as the proof route, subject to the analytic premises below |
| Periodic alternative | The periodic route is separate. It includes spatial periodicity for initial data, force, velocity, and pressure, plus future-time derivative decay. The pressure periodicity is included in accordance with the CMI erratum. | Confirmed at proposition and source level |
| Same force and initial datum in the negation | The whole-space bridge maps a Comparator global solution for the same `u₀` and `f` into the internal global-solution record. The periodic adapter does the corresponding mapping for the periodic class. | Confirmed at source level and headline axiom reports |

## Actual issue found

`DiagonalResidual.JetRate` is a generic eventual inequality over an arbitrary filter. A zero-sorry probe proves that `JetRate (⊥ : Filter D) q f m r` holds for arbitrary `q`, `f`, `m`, and `r`. This is a genuine formalisation-quality weakness because the predicate does not carry a `NeBot` assumption or smoothness field.

The audited endpoint `GlobalBaseError.originPast` is independently proved `NeBot`. The final residual theorem returns a rate on that endpoint filter, and the inspected stage records separately carry smoothness. The audit has not found a CMI disproof from this weakness. Derived intersections used as premises remain a review item because their nontriviality is not bundled into the generic rate API.

## Boundary convention

The repository uses `ContDiffOn` on `Ico 0 1 × R³` and `Ici 0 × R³`, with ordinary derivatives used only at interior positive times. The Comparator definitions use `ContDiffOn` and `iteratedFDerivWithin` on the closed future half-space. This is a coherent one-sided interpretation of the CMI notation `C∞(R³ × [0,∞))`, and no Lean counterexample showing a weaker accepted field has been found.

It is still not a completed formal equivalence theorem to every possible textbook interpretation of `C∞` on a manifold with boundary. That is a mathematical exposition obligation, not an observed CMI mismatch. The CMI-facing theorem is stronger than the internal candidate statement because the exported nonexistence target is the Comparator predicate.

## Construction provenance

The selected witness is obtained through `ActualCandidateAssembly.estimates`, `GluedStageEstimates.actualStageEstimates`, concrete cycle run data, coherence, representations, and `PhysicalData`. `PhysicalData` supplies local smoothness, local field germs, and exterior equality; it is not a field named “the desired residual bound”. The residual rate is derived in `ActualCycleResidualBounds.Invariant.residual_jetRate`, where the source, mean, base, Gaussian, alias, and excluded terms are explicitly combined.

The remaining independent peer-review obligation is not compilation. It is a line-by-line analytic verification that those imported estimates genuinely establish the stated PDE construction, including common inverse domains, every residual channel, and provenance of the invariant certificates.

## Classification

Current classification: `FORMAL TRUST PASS; CMI PREDICATE MATCH CONFIRMED AT LEAN INTERFACE LEVEL; ANALYTIC PEER REVIEW OPEN; NO NEGATIVE CMI FINDING ESTABLISHED`.

This classification does not imply CMI prize recognition. [CMI rules](https://www.claymath.org/millennium-problems/rules/) require a qualifying publication, at least two years of rigorous examination, and general acceptance before CMI considers a proposed solution.
