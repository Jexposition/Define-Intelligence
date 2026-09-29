# Priority 154 source review: Euler transport, frame endpoint, and Gaussian heat support

**Date:** 2026-09-29
**Scope:** twelve current Euler source files selected from the next priority-0 queue.
**Method:** direct inspection of imports, declarations, theorem statements, proof hypotheses, endpoint/moment tokens, and source-hygiene tokens.
**Status:** tranche evidence only. The absence statements below are limited to these twelve files.

## Direct source findings

| File | Source anchors | What the source establishes | Audit boundary |
|---|---:|---|---|
| `Euler/FixedEvolutionRegularity.lean` | 1-5; 24-43; 45-92 | Smooth dependence of fixed-coordinate velocity, acceleration, physical velocity, and derivative paths on parameterised frames, coercivity, derivative, potential, smallness, and `ContDiff` hypotheses. | Conditional Euler transverse-frame regularity; no selected Navier-Stokes field or radial moment theorem. |
| `Euler/FixedFrameNaturality.lean` | 1-2; 28-39; 45-96 | Norm control and intertwining for time multiplication, product derivative, fixed derivative, primitive, and fixed-frame solver under compatible bounded maps. | Operator naturality; no `selected_witness`, `CandidateProperties`, or five-observable transport. |
| `Euler/FlowEscapeBound.lean` | 1-4; 26-70; 99-180 | Integral action bounds control curve displacement, flow escape, and the measure of escaping trajectories under explicit integrability and derivative hypotheses. | Euler flow estimate; not a whole-space Navier-Stokes endpoint or moment calculation. |
| `Euler/FlowL2Transport.lean` | 1-2; 13-29; 43-69 | A determinant-one inverse flow gives a measure-preserving homeomorphism and transports continuous spatial `L²` paths with exact norm preservation and almost-everywhere composition identities. | Flow transport is abstract and conditional; it does not transport the paper's five radial observables. |
| `Euler/FrameEndpointUniqueness.lean` | 1-2; 21-40; 40-99; 100-130 | Energy coercivity and projected second-order frame equations imply zero and uniqueness for paths with endpoint conditions and explicit frame/potential smallness assumptions. | Moving-frame coordinate uniqueness, not `WholeSpaceUniqueness` for the selected Navier-Stokes witness. |
| `Euler/FrameWronskian.lean` | 1-4; 19-65 | Constant frame Wronskian and symmetry of the induced strain under the stated differentiability and frame identities. | Local frame algebra; no Cartesian selected-field moment or pressure semantics. |
| `Euler/FrozenEvolutionGevrey.lean` | 1; 23 onward | A frozen-evolution derivative recurrence in the Hilbert-coercive Gevrey layer. | Gevrey recurrence only; no selected endpoint transport. |
| `Euler/FunctionalVelocity.lean` | 1-2; 15-19; 24-57 | Assembles four lifted velocity coefficients as a bounded linear map and proves coordinate Sobolev decomposition and a dimension-factor bound under smoothness and all-order `MemLp`. | Genuine velocity assembly, but no `ActualCandidateAssembly.Witness`, radial moments, or CMI semantics. |
| `Euler/GainedMildFormula.lean` | 1; 16-69 | Defines the high-order heat-plus-Duhamel path and proves its singular mild formula, lower Sobolev truncation identity, and equivalence with ordinary Duhamel evolution. | Euler cylinder/Sobolev mild evolution; not the Navier-Stokes selected witness. |
| `Euler/GainedMildPasting.lean` | 1-2; 15-25; 30-50 | Bounded spatial maps commute with matching-endpoint path gluing, and matching gained-mild solutions paste under explicit source restrictions and endpoint hypotheses. | Pasting identity; no global Cartesian moment bridge. |
| `Euler/GaussianCylinderHeat.lean` | 1-2; 17-73; 85-144 | Defines line orbits and Gaussian line heat operators, proving continuity, integrability, contraction, translation, semigroup, commutation, and standard Gaussian representation. | Cylinder heat analysis; no selected pressure or five-moment equality. |
| `Euler/GaussianHeatSmoothing.lean` | 1; 16-91 | Defines the bounded Gaussian moment derivative operator and proves differentiability, derivative bounds, and translation compatibility for line heat smoothing. | Heat smoothing with Gaussian moment bounds; not the selected-field radial observables. |

## Cross-checks

The twelve files contain no declaration token for `selected_witness`, `CandidateProperties`, `barMoment`, `FiveRowRank`, `PositiveOrderMoments`, or `NavierStokesR3`. They also contain no literal equality identifying a final selected Cartesian field with `(M, I, J, S, C_p)`. This is a bounded tranche result, not a repository-wide nonexistence theorem.

The files do contain real transport, frame, heat, Sobolev, and regularity mathematics. In particular, `FlowL2Transport` proves exact `L²` norm preservation for a determinant-one inverse flow, while `FunctionalVelocity` proves a concrete four-component velocity assembly bound. Neither theorem has the type or conclusion needed for selected-field five-moment transport.

Direct source-hygiene scans found no `sorry`, `admit`, or `axiom` token in this tranche. No nonzero defect, pressure contradiction, or `False` derivation is established here.

## Classification

| Classification | Result |
|---|---|
| CMI endpoint bridge | Not addressed by these files |
| Selected-field five-moment transport | Not found in this tranche |
| Force provenance | Not addressed by these files |
| Pressure absolute semantics | Not addressed by these files |
| Source hygiene | No `sorry`, `admit`, or `axiom` token found |

The tranche clears twelve queued source rows as directly inspected Euler support. It neither weakens nor strengthens CTR-005 by itself. The next review remains the next register queue, with selected-endpoint and Cartesian transport rows kept distinct from Euler support.
