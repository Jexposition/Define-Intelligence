# Human-readable repository architecture map

> **State-control note (2026-09-30):** This file preserves dated architecture
> snapshots and source-review chronology. Its embedded coverage counts are not
> the live register. For current counts and the controlling scientific status,
> use [`DOCUMENTATION_RECONCILIATION_2026-09-30.md`](DOCUMENTATION_RECONCILIATION_2026-09-30.md)
> and [`SEMANTIC_CORRESPONDENCE_MAP.md`](SEMANTIC_CORRESPONDENCE_MAP.md).

## Historical audit state (2026-09-28)

The current semantic register reports 2,790 indexed modules, 588 reachable,
613 evidence-inspected, 0 reachable-open, and 0 missing project import edges.
These figures describe audit coverage, not proof of the paper-to-code bridge.

> This is the map to read before opening Lean. It explains the mathematical flow, the software layers, and the exact place where each family connects. The exhaustive [module explanation cards](LEAN_MODULE_EXPLANATIONS.md) then give one entry for every file.

## What is being mapped

For the paper-to-code argument, start with
[`SEMANTIC_CORRESPONDENCE_MAP.md`](SEMANTIC_CORRESPONDENCE_MAP.md). This
architecture page supplies the broader module and dependency navigation;
it is not a replacement for the claim-by-claim field correspondence
analysis.

The source tree is not one proof file. It is a layered construction. A typical path is:

```text
formal problem statement
        ↓
candidate construction and finite-stage data
        ↓
moment/debt repair and profile updates
        ↓
potential, wave, germ, and temporal assembly
        ↓
periodic/localised velocity, pressure, and residual fields
        ↓
whole-space R³ packaging and energy consequences
        ↓
exported existential theorem
```

The arrows mean that declarations/imports connect the layers. They do not, by themselves, prove that every informal interpretation survives the entire route.

## Mathematical reading of the selected route

### 1. Problem and endpoint layer

`NavierStokes/R3/ProblemStatement.lean` defines the formal candidate predicate. `NavierStokes/R3/Theorem.lean` packages the selected candidate into the exported theorem `NavierStokesR3.theorem_1_1`. This is the final logical interface: a reviewer must first identify exactly what this predicate requires, rather than infer requirements from the paper narrative.

### 2. Concrete candidate assembly

`ActualCandidateAssembly.lean` is the construction junction. It names the initial, zeroth, particular, mean, signed, germ, and stage data, and exports `selected_witness`. Its imports are the incoming construction graph; its witness is the object consumed by the R³ theorem route.

### 3. Germs, stages, and profiles

The `Germ*`, `Stage*`, `Potential*`, `Wave*`, `Pulse*`, `Profile*`, and `Time*` families build the local pieces and control their smoothness, support, rates, and endpoint limits. These files explain how the candidate is assembled, but a declaration-level connection is still not the same thing as a field-level identity after infinite summation and localisation.

### 4. Moment and correction layer

`FiveRowRank.lean`, `PositiveOrderMoments.lean`, `FiveProfileMoments.lean`, `MeanRankUpdate.lean`, and `DefectIncrementBounds.lean` form the finite-dimensional correction branch. In plain terms, they define debt vectors, moment rows, profile corrections, and estimates used to repair selected quantities. The audit therefore records these modules as reachable, not dead. The unresolved question is stronger: where is the theorem that transports those named quantities into the final Cartesian field exported by `selected_witness`?

### 5. Periodic and residual assembly

`MixedPeriodicAssembly.lean` and related `Periodic*`, `Localized*`, `Cutoff*`, and `Support*` modules turn local or periodic pieces into assembled velocity, pressure, and residual objects. This is where support, cutoff, divergence, temporal activation, and residual identities meet. Any moment claim must survive these operations, not only hold for an isolated profile or correction increment.

### 6. R³ and energy layer

`R3CompactCandidate.lean`, `R3ActualCandidate.lean`, `R3CompactEnergy.lean`, `R3EnergyNorms.lean`, `R3EnergyBoundary.lean`, and the other `R3*` modules package whole-space regularity, compact support/decay, pressure, energy, and comparison statements. These modules are part of the author source and must be read as the final analytical interface, not as evidence that upstream informal quantities have automatically been preserved.

### 7. What the current route proves and does not prove

- The route proves structural reachability: the selected endpoint depends on the listed source modules in the captured environment.
- The route does not by reachability alone prove value-level equality between the five named moment quantities and the final Cartesian velocity/pressure fields.
- The route does not turn source names into physical meaning. The module cards mark inferred roles explicitly so that a human reviewer can verify each one against the source.
- The endpoint `sorryAx` result is an endpoint dependency result, not a blanket claim about every standalone file in the repository.

## Selected endpoint route with source coordinates

| Target | Source span | Reachability |
|---|---|---|
| `NavierStokesR3.theorem_1_1` | `NavierStokes/R3/Theorem.lean:46-51` | True |
| `NavierStokes.ActualCandidateAssembly.selected_witness` | `NavierStokes/ActualCandidateAssembly.lean:1177-1182` | True |
| `NavierStokes.FiveRowRank.FiveRows` | `NavierStokes/FiveRowRank.lean:241-248` | True |
| `NavierStokes.FiveRowRank.Debt` | `NavierStokes/FiveRowRank.lean:22-24` | True |
| `NavierStokes.PositiveOrderMoments.Debt` | `NavierStokes/PositiveOrderMoments.lean:23-24` | True |
| `NavierStokes.MeanRankUpdate.scaleDebt` | `NavierStokes/MeanRankUpdate.lean:30-32` | True |
| `NavierStokes.MixedPeriodicAssembly.periodicVelocity` | `NavierStokes/MixedPeriodicAssembly.lean:36-39` | True |
| `NavierStokes.DefectIncrementBounds.barMoment` | `NavierStokes/DefectIncrementBounds.lean:214-217` | True |
| `NavierStokes.R3CompactCandidate.velocity` | `NavierStokes/R3CompactCandidate.lean:201-203` | True |
| `NavierStokesR3.ProblemStatement.CandidateProperties` | `NavierStokes/R3/ProblemStatement.lean:92-111` | True |

## Key connection table

| Layer | Representative files | Receives | Produces | Review question |
|---|---|---|---|---|
| Formal specification | `R3/ProblemStatement.lean`, `R3/Theorem.lean` | candidate fields and predicates | exported theorem package | What exactly is required by the formal predicate? |
| Assembly | `ActualCandidateAssembly.lean`, `ActualCandidateConstruction.lean` | base, germ, stage, pressure, and exterior data | `selected_witness` and candidate fields | Which concrete fields enter the witness? |
| Moments/corrections | `FiveRowRank.lean`, `PositiveOrderMoments.lean`, `MeanRankUpdate.lean` | profile/debt data | correction rows and update estimates | Are the named moments transported to the final field? |
| Local/periodic fields | `MixedPeriodicAssembly.lean`, `PeriodicResidualLimits.lean` | local velocity, pressure, cutoffs | assembled velocity/residual limits | Are identities preserved across localisation and periodisation? |
| R³ analysis | `R3CompactCandidate.lean`, `R3CompactEnergy.lean`, `R3Pressure*.lean` | assembled candidate and force | whole-space support, energy, pressure, comparison facts | Do these facts match the advertised whole-space problem? |
| Review layer | `NavierStokesReview/src/audit/*` | source tree and Lean environment | maps, joins, claims, probes | Are source facts separated from semantic conclusions? |

## Coverage and integrity

The map accounts for **2790 / 2790 Lean modules**, with **0 unaccounted**. It records **50191 source declarations**, **30721 compiled nodes**, **22958 exact source joins**, and **0 reachable `sorryAx` users** in the selected endpoint environment. The selected endpoint closure contains **572 source-joined modules**.

## Reading order

1. Read this page for the architecture and the unresolved transport question.
2. Read the selected route evidence for exact declaration spans.
3. Search `LEAN_MODULE_EXPLANATIONS.md` for any file name. Its card gives imports, dependents, declarations, flags, and endpoint status.
4. Search `LEAN_DECLARATION_INDEX.md` when the question starts from a theorem, definition, or namespace rather than a file.
5. Use `REPOSITORY_MODULE_ATLAS.md` for compact filtering and the raw JSON only for machine-level evidence.
6. Open `REPOSITORY_ARCHITECTURE_MAP.html` for claim cards, source excerpts, declaration search, and import-path queries.
7. Treat the role summaries as navigation, not as proof claims.

Companion files: [module cards](LEAN_MODULE_EXPLANATIONS.md), [declaration index](LEAN_DECLARATION_INDEX.md), [REPOSITORY_MODULE_ATLAS.md](REPOSITORY_MODULE_ATLAS.md), [interactive map](REPOSITORY_ARCHITECTURE_MAP.html), [selected route evidence](../NavierStokesReview/evidence/selected_endpoint_routes_2026-09-26.md), and `REPOSITORY_ARCHITECTURE_MAP.tex`.
## Coverage checkpoint: 2026-09-28

The current source-review register contains 2,790 indexed modules and 588
reachable modules, of which 329 have direct semantic evidence and 284 remain
open. The latest reviewed layers include residual stability, finite-copy and
pressure jets, past extension, local axisymmetric residuals, physical graph
bounds, primary pulses, periodised field assembly, R3 comparison, harmonic
interaction, actual cycle geometry, polar coverage, and axis series. This
checkpoint confirms that these layers contain substantive intermediate
mathematics; it does not assert final `(M,I,J,S,C_p)` transport or completion.

The current checkpoint also covers graph calculus, localised mean interaction,
natural axis ranges, pulse growth, torus/request rebasing, and base stress
classes. Register state is 2,790 indexed modules, 588 reachable, 335 directly
inspected, 278 reachable still open, and zero missing project import edges.

The next architecture checkpoint covers native chart scales, endpoint coordinate
extensions, compact R3 comparison bounds, and finite-energy/tensor-difference
comparison estimates. Register state is 2,790 indexed modules, 588 reachable,
339 directly inspected, 274 reachable still open, and zero missing project
import edges. These layers are substantive but do not by themselves establish
the selected-field `(M,I,J,S,C_p)` transport bridge.

The current architecture checkpoint also covers the R3 comparison-energy and
slot-geometry layer: comparison setup, localised difference energy and
Laplacian identities, sharp energy inequalities, spatial work bounds,
whole-space cutoff limits, and torus-slot geometry. Register state is 2,790
indexed modules, 588 reachable, 346 directly inspected, 267 reachable still
open, and zero missing project import edges. These layers remain intermediate
mathematics and do not by themselves establish the selected-field moment bridge.
### 2026-09-28 priority-69 source tranche: nine modules registered

Direct source review completed for `AnnularEndpoint.lean`, `AxisContraction.lean`, `PhysicalCopyBounds.lean`, `R3/LocalizedFluxEstimates.lean`, `ResetEnergyBounds.lean`, `ScaledActualParticularControl.lean`, `TerminalCone.lean`, `ViscousPropagator.lean`, and `VolterraAnalyticBounds.lean`. These modules add substantive support/germ, periodisation, reduced-axis, tail-energy, cone, coefficient-propagator, and analytic Volterra bounds. They do not state the final selected Cartesian `torusAverage`/`barMoment` transport theorem, and this tranche yields no nonzero defect, impossibility theorem, or kernel `False`.

The regenerated full semantic register now reports **355 evidence-inspected reachable modules** and **258 reachable modules still open**. The authoritative outputs are `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`, `.md`, and `.html`, mirrored under `docs/`. Detailed evidence is in `NavierStokesReview/src/audit/priority_69_annular_axis_copy_flux_reset_cone_propagator_source_review_2026-09-28.md`.

### 2026-09-28 priority-70 source tranche: activation, wave regularity, base context, and copy-solve transport

Direct source review completed for `ActivationBounds`, `ActualWaveRegularity`, `CommonBaseContext`, and `CopySolveCompatibility`. These layers add activation-factor bounds, smooth wave/curl/tsum regularity, base/stress context, and generic copy-solve transport. They remain intermediate mathematics and do not by themselves establish the selected-field `(M,I,J,S,C_p)` transport bridge.

Register state is 2,790 indexed modules, 588 reachable, 359 directly inspected, 254 reachable still open, and zero missing project import edges.

### 2026-09-28 priority-71 source tranche: curl realization, diagonal extensions, carrier binding, and finite heads

Direct source review completed for `LocalizedCurlRealization`, `MixedDiagonalExtensions`, `ActualCarrierTransport`, and `FiniteHeadClass`. These layers add patchwise curl/divergence/germ identities, potential support and extension, canonical carrier-record binding, and finite-prefix jet-class transfer. They remain intermediate mathematics and do not by themselves establish the selected-field `(M,I,J,S,C_p)` transport bridge.

The register remains 2,790 indexed, 588 reachable, 359 directly inspected, 254 reachable still open, and zero missing project import edges; the rows were already evidence-classified.

### 2026-09-28 priority-72 source tranche: pulse, geometry, time averages, and edge stress

`CorrectedPulseAmplitude`, `PrimaryGeometryAssembly`, `R3/ComparisonTimeAverages`, and `SlowFirstOrderEdge` add corrected energy-reset, reduced geometry, finite-energy comparison, and conditional radial-stress layers. `SlowFirstOrderEdge` points to separate renormalized-moment and slow-order theorems for global closure. These modules remain intermediate/reduced mathematics and do not establish the selected-field `(M,I,J,S,C_p)` transport bridge.

The register now reports 2,790 indexed, 588 reachable, 363 directly inspected, 250 reachable still open, and zero missing project import edges.

### 2026-09-28 priority-73 source tranche: base velocity, representatives, context, and reserved patches

`ActualBaseVelocityBounds`, `BaseContextAssembly`, `PhaseEstimates`, `PrimaryRepresentatives`, `PositiveRepresentatives`, and `ReservedPatches` add actual coefficient/support and rate layers, reduced stress identities, phase/representative geometry, and radial five-row patch identities. They remain intermediate/reduced mathematics and do not establish the final selected-field `(M,I,J,S,C_p)` transport bridge.

The register now reports **2,790 indexed, 588 reachable, 369 directly inspected, 244 reachable still open, and zero missing project import edges**. Evidence: `NavierStokesReview/src/audit/priority_73_base_representative_reserved_source_review_2026-09-28.md`.
## Coverage update: 2026-09-28

The current generated coverage state is **2,790 indexed; 588 reachable; 375 evidence-inspected; 238 reachable still open; 0 missing project import edges**. Activation, particular-control, extension, local-physical, and moving-frame modules were classified in the latest tranche. Their layer roles are documented without treating import reachability as final paper-to-code transport.
## Coverage update: 2026-09-28 cutoff/Volterra/wave-interaction tranche

The current generated coverage state is **2,790 indexed; 588 reachable; 381 evidence-inspected; 232 reachable still open; 0 missing project import edges**. The latest source review maps cutoff jets, Volterra sums, physical wave sums, angular loops, tail energy, and support-separated curl interactions without conflating these layers with final paper-observable transport.
## Coverage update: 2026-09-28 radial/chart/integral tranche

The current generated coverage state is **2,790 indexed; 588 reachable; 392 evidence-inspected; 221 reachable still open; 0 missing project import edges**. The latest source review maps radial base realisation, support-based radial aliases, chart jets, smooth rephasing/integration, and spacetime extension layers without collapsing them into endpoint proof.

## Coverage update: 2026-09-28 axis/dilation/extension/ODE tranche

The current generated coverage state is **2,790 indexed; 588 reachable; 400 evidence-inspected; 213 reachable still open; 0 missing project import edges**. The latest source review maps axis coefficient evaluation/resolvent machinery, reduced-profile dilation moments, radial extension, Gaussian localisation, phase geometry, and weighted ODE jets. These layers are not collapsed into a final selected-field transport claim.

### Coverage update: 2026-09-28 priority-78

The current generated coverage state is **2,790 indexed; 588 reachable; 414 evidence-inspected; 199 reachable still open; 0 missing project import edges**. The latest source review maps phase-defect, axis-mode, coefficient-weight, polar-chart, stress-activation, and weighted-Volterra layers. These remain intermediate layers and are not collapsed into a final selected-field `(M,I,J,S,C_p)` transport claim. Evidence: `NavierStokesReview/src/audit/priority_78_phase_defect_axis_algebra_weighted_volterra_source_review_2026-09-28.md`.

### Coverage update: 2026-09-28 priority-79

The current generated coverage state is **2,790 indexed; 588 reachable; 420 evidence-inspected; 193 reachable still open; 0 missing project import edges**. The latest source review maps axis operators, chart/component identities, matching-cone and source-jet bounds, physical coordinate scaling, signed covariance, and moving-edge extension. These remain intermediate layers and are not collapsed into a final selected-field `(M,I,J,S,C_p)` transport claim. Evidence: `NavierStokesReview/src/audit/priority_79_axis_chart_matching_coordinate_covariance_edge_source_review_2026-09-28.md`.
## Priority 80 architecture note (2026-09-28)

The axis/regularity and reduced-radial layer now has direct source evidence for six more reachable modules. `BoundaryAxisJets` handles axis jets; `GenericEndpointExtension` handles strip and periodic endpoint gluing; `PhaseJetBounds` handles quantitative phase geometry; `RadialPullback` handles exact reduced radial changes of variables; `ReferencePath` rebuilds reduced histories; and `WeightedRadialPrimitive` handles weighted radial inverse/mean-class transport. These modules sit below the selected Cartesian packaging boundary. Their declared outputs do not by themselves reach `ActualCandidateAssembly.Witness` as a five-observable equality.
## Priority 81 architecture note (2026-09-28)

The R3/residual boundary is now source-mapped more precisely. `MixedDiagonalResidual` consumes actual potential sums; `R3CompactCandidate` wraps periodic local properties into compact whole-space properties; `GaugeRadialResidualBounds` connects pressure-gauge defect to radial mass; and `OutgoingSchedule` performs exact two-moment reduced-profile closure. This is a connected intermediate architecture, but the map still lacks a declared full `(M,I,J,S,C_p)` equality at the public selected Cartesian witness.

## Priority 82 architecture note (2026-09-28)

The next boundary is now source-mapped for actual intermediate debt, exterior annulus control, R³ scaling, selected compact packaging, and natural entrance flux. `ActualIntermediateDebtBounds` derives three-component debt from checked step data; `ActualMeanExterior` propagates exterior vanishing through actual cycle families; `SpatialEnergyScaling` and `SpatialSupportScaling` prove exact R³ transformations; `R3ActualCandidate` wraps `selected_witness` through `of_localized_fields`; and `NaturalEntrance` proves exact reduced angular/axial source integrals. These are connected intermediate layers, not a complete selected Cartesian `(M,I,J,S,C_p)` transport theorem.

## Priority 83 architecture note (2026-09-28)

The localisation and physical-profile layer is now source-mapped for exact squared mask partitions, mixed curl-plus-angular field construction, Gaussian tail bounds, leading-stress edge joins, signed torus/radial requests, and pulse covariance. `SquaredPartition` supplies exact normalisation; `DirectAngularDiagonal` supplies actual field/divergence identities; `GaussianTailFlat` supplies all-order tail controls; `LeadingStressWeights` supplies stress/edge bounds; `LocalSignedRequest` supplies physical radial primitive identities; and `PulseCovariance` supplies a strict covariance cone. These layers remain below the public selected Cartesian five-observable transport boundary.

## Priority 84 architecture note (2026-09-28)

The axis/heat/release/average layer is now source-mapped for positive-axis Volterra profile existence, pulse-lag identities, radial heat moment ODEs, scheduled renormalised release cancellation, heated physical axial-viscosity cancellation, and torus/Jacobian/periodisation averages. These are genuine intermediate bridges below the public selected Cartesian packaging boundary. The architecture map still has no reviewed declaration composing them into the complete `(M,I,J,S,C_p)` equality at `ActualCandidateAssembly.Witness`.

## Priority 85 architecture note (2026-09-28)

The signed geometry and repair-cone layer is now source-mapped for actual common-cover geometry, finite active-label covariance sums, compensated heat-cone preservation, and the genuine reduced five-coordinate/physical-row bridge in `RepairConeBounds`. The architecture must distinguish this reduced/profile transport from the still-unproved composition into the final Cartesian curl/localised/periodised selected endpoint and `Witness`.

## Priority 86 architecture note (2026-09-28)

The rank/cycle layer is now source-mapped for the direct `BaseRankPatch.five_rows` local `FiveRowRank` result, actual cycle/covariance induction, variable-gauge rank-state bounds, terminal physical compensation, and mean-stage/support data. These are connected local bridges below the final whole-space Cartesian endpoint. The architecture still requires a declaration-level composition into `selected_witness`/`Witness` before the paper-level endpoint claim can be upgraded.

## Priority 87 architecture note (2026-09-28)

The residual/force boundary is now source-mapped for axisymmetric alias grouping, finite local residual reconstruction, diagonal stage-to-limit jet and spatial-curl rates, compact temporal/spatial force decay, and the \(R^3\) compact-force bound. These layers strengthen the route from local construction to regularity and force admissibility, but they remain below the final selected Cartesian five-observable composition. `DiagonalResidual` supplies order-by-order flatness rather than a single fixed-tail radial-moment identity.

## Priority 88 architecture note (2026-09-28)

The profile/cover/mean boundary is now source-mapped for actual cone/stress and loop-moment algebra, analytic axis/heat extensions, similarity-chart transitions, Cartesian axisymmetric curl/support identities, cover/deck copy solves, and temporal mean updates. These are connected intermediate layers below the public selected Cartesian packaging boundary. The architecture still requires an explicit composition of their values with the final `tsum`/localisation/periodisation field and `Witness` observables.

Priority 89 adds the next connected layer: compact reduced moment repair, abstract exact repair, torus inverse and alias transport, stress identities, local gauge-mass preservation, and Cartesian curl covariance. These declarations strengthen the intermediate architecture but do not themselves cross the final selected-field observable boundary. Register state: 2,790 indexed, 588 reachable, 494 evidence-inspected, 119 reachable-open.

Priority 90 adds generalised-power/bump moment matrices, scheduled and prepared outgoing profiles, R3 Gaussian integrability, and abstract smooth quadratic repair. These are upstream solvability and regularity layers. They remain below the public selected Cartesian observable boundary. Register state: 2,790 indexed, 588 reachable, 499 evidence-inspected, 114 reachable-open.

Priority 91 adds the parametric torus-inverse and periodic-phase assembly layers. `ParametricTorusInverse` covers smooth parameter/torus derivatives, zero mean, Fourier inversion, rapid decay, finite jets, and inverse multipliers. `PeriodicPhaseAssembly` covers clock windows, locally finite tsum periodisation, phase and angular-lift periodicity, geometry transport, and carrier-adapter germs/jets. These layers strengthen the intermediate architecture but remain below the public selected Cartesian observable boundary. Register state: 2,790 indexed, 588 reachable, 501 evidence-inspected, 112 reachable-open.

Priority 92 adds the R3 energy/force accounting layer, the residual polar graph coordinate bridge, and the uniform primary-weight/curl-rate layer. These provide concrete energy, support, off-axis chart, and regularity infrastructure. They remain below the public selected Cartesian observable boundary. Register state: 2,790 indexed, 588 reachable, 508 evidence-inspected, 105 reachable-open.
Priority 93 adds the joint residual-limit/flat-extension layer, reduced matching-debt budgets, relative maximal-lifespan layer, exact mean/rate reindexing, pulse energy-history bounds, and local radial-flux residual bridge. These are connected intermediate layers. The architecture still contains no inspected composition proving the full reduced-to-Cartesian/localised/periodised five-observable equality at the public `Witness`. Register state: 2,790 indexed, 588 reachable, 514 evidence-inspected, 99 reachable-open.
Priority 94 adds reduced history repair, concrete initial mean/covariance/rank state, harmonic coefficient/support calculus, exterior prefix agreement, particular-mean covariance gain, and signed-family support. These are connected intermediate layers. The architecture still contains no inspected composition proving the full reduced-to-Cartesian/localised/periodised five-observable equality at the public `Witness`. Register state: 2,790 indexed, 588 reachable, 521 evidence-inspected, 92 reachable-open.

Priority 95 adds the R3 pressure comparison and Riesz/Fourier layer, compact-test pressure recovery, temporal pressure identities, viscosity and normal scaling, whole-space comparison closure, scalar support, and tangent projection. These are connected relative, analytic, scaling, and support layers. The architecture still contains no inspected composition proving an absolute selected pressure representative or the full reduced-to-Cartesian/localised/periodised five-observable equality at the public `Witness`. Register state: 2,790 indexed, 588 reachable, 539 evidence-inspected, 74 reachable-open.

Priority 96 adds concrete core/support geometry, signed unmasked and uniform block bounds, off-plane and oscillatory-curl estimates, time localisation, comparative weak pressure/Poisson recovery, compact pressure-flux tests, Riesz test operators, reduced schedule pressure, and tail/cone control. These are connected intermediate layers. The architecture still contains no inspected composition proving an absolute selected pressure representative or the full reduced-to-Cartesian/localised/periodised five-observable equality at the public `Witness`. Register state: 2,790 indexed, 588 reachable, 558 evidence-inspected, 55 reachable-open.

Priority 97 adds a necessary positive correction to the architecture: local Cartesian-curl realisation is present in `ActualMeanPotentialRealization` and `TailGaugePotential`, and reduced/chart moment identities are present in `NominalConeAssembly`. The unresolved edge is not “profile to curl is absent”; it is the full composition from those local/reduced identities through the selected global sums, localisation, periodisation, and public `Witness` observables. Register state: 2,790 indexed, 588 reachable, 569 evidence-inspected, 44 reachable-open.

Priority 98 adds signed native regularity, exponent/rate arithmetic, gauge and alias coherence, interval-copy transport, support preservation, reduced exterior matching, axis pressure data, positive-time signed wave data, pressure-kernel bounds, and scaled tangent transport. These strengthen the intermediate architecture. They do not establish the final selected Cartesian five-observable composition at `Witness`. Register state: 2,790 indexed, 588 reachable, 580 evidence-inspected, 33 reachable-open.

Priority 109 adds current-band support, signed request/amplitude/pressure `tsum` transport, cycle-state coherence, angular curl invariance, dependent signed-family periodisation, reduced natural-axis bridges, future pressure data, physical-stage bounds, and comparative whole-space pressure flux. These close additional intermediate edges but leave the selected global `barMoment` / `(M,I,J,S,C_p)` composition unresolved. Register state: 2,790 indexed, 588 reachable, 592 evidence-inspected, 21 reachable-open.

Priority 110 adds initial-state construction, cycle state/block/axis coherence, particular-cycle native source/pressure/Gaussian data, and reduced corrected-pressure matching and bounds. Priority 111 adds cycle preservation, curl-corrected particular realization, and germ/cutoff transport. Priority 112 adds reduced activation stocks, locally finite diagonal `tsum` jet/tail control, and compensated outgoing-profile integral identities. Priority 113 adds reduced outgoing compensation, local mode-level solenoidal reindexing, and temporal hold/wait and decay bounds. These are intermediate architectural edges; the selected global `barMoment` / `(M,I,J,S,C_p)` composition remains unresolved. Register state: 2,790 indexed, 588 reachable, 605 evidence-inspected, 8 reachable-open.
