# Priority 0/1 source review: geometry, regularity, profiles, and gluing

Date: 2026-09-27
Scope: direct reading of the OpenAI source files listed below.  This is a bounded source review, not an endpoint-completeness claim.

## Reading rule

The classifications below distinguish three things:

1. a theorem that is mathematically real inside its own module;
2. a theorem that reaches the selected candidate through imports; and
3. a theorem that transports a paper observable into the exported selected endpoint.

Only the first two are established for most files in this tranche.  None of the files below, by its inspected declarations, supplies the missing equality

\[
  \operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  =(M,I,J,S,C_p).
\]

That absence is a scope result.  It is not a proof that the concrete selected field has a non-zero defect.

## Findings by source file

| Source file | Main declarations inspected | What the file actually establishes | Endpoint consequence |
|---|---|---|---|
| `NavierStokes/ActualCarrierGeometry.lean` | `cell_geometry`, `labelCarrier_*`, `geometry_liftedSupport`, `labelCarrier_disjoint` (50–342) | Signed-label carrier cells, phase/log bands, physical boxes, support lifting, injectivity, and disjointness under threshold hypotheses. | Geometry/support infrastructure; no radial moment or `Witness` transport. |
| `NavierStokes/ActualParticularBackground.lean` | reindexing, `zeroRescale_*`, `backgroundFamily_eq`, `background_normal`, `background_defect` (26–314) | Reindexing and rescaling identities for actual wave-family normal/defect/auxiliary data. | Intermediate coefficient construction; no selected Cartesian moment equality. |
| `NavierStokes/ActualParticularGaussian.lean` | `gaussianLength_*`, `envelope_gaussian`, `globalGaussian_all_gains`, `gaussianBlock_all_gains` (40–229) | Positive length/scale bounds and Gaussian envelope/gain bounds for active labels and cycle states. | Quantitative Gaussian bounds; no `barMoment`/`FiveRows` export. |
| `NavierStokes/ActualSignedGaussian.lean` | `localGaussian_formula`, support/plateau theorems, `actual_gaussianBlock_jets` (34–267) | Actual signed Gaussian local fields, zero regions, smooth jets, and gain bounds. | Actual intermediate jet branch; no five-observable endpoint identity. |
| `NavierStokes/AnalyticPrimitive.lean` | `primitive`, segment/continuity and smooth-factor results (26 onward) | Complex analytic primitive and differentiability machinery used to build smooth factors. | Analytic regularity only; no fluid-field moment transport. |
| `NavierStokes/CartesianCopySource.lean` | `pullStrip`, `rotationMap`, `rotationMap_smooth`, `rotationMap_jets`, source bounds (20 onward) | Pullback/rotation of source profiles into Cartesian coordinates on annular/off-axis domains. `rotationMap_smooth` excludes the axis (`y ≠ 0`) and jet bounds use positive annulus parameters. | Explicit chart-scope boundary; no on-axis-to-global moment bridge. |
| `NavierStokes/CauchyRestriction.lean` | disk restriction maps, `cauchyMap`, derivative CLMs and integral identities (24–296) | Bounded restriction and Cauchy-integral operators for nested complex disks. | Complex regularity/restriction tool; unrelated to selected radial observables. |
| `NavierStokes/Covariance.lean` | `signedMatrix`, `reconstruct`, `solution_unique`, positivity/amplitude identities (29–207) | Finite-dimensional covariance coefficient reconstruction and positivity under determinant hypotheses. | Local algebraic covariance solve; no field-level endpoint transport. |
| `NavierStokes/CurlGeometry.lean` | `cross`, triple products, `curl_symbol_transverse`, cylindrical curl/div identities (19–157) | Algebraic curl/transversality and cylindrical differential identities. | Supports solenoidal construction; does not evaluate selected radial integrals. |
| `NavierStokes/FlatPrimitive.lean` | `primitive`, derivative/recurrence, normalized primitive and limits (25–291) | Flat primitive construction, derivative identities, positivity/normalisation and zero-limit behaviour. | Scalar flatness machinery; no `tsum`-to-moment theorem. |
| `NavierStokes/FlatPrimitiveFactor.lean` | denominator/coordinate/kernel/factor and integrability/smooth-factor results (26–315) | Parameterised coordinate/factorisation identities, integrability, smoothness, and derivative bounds, with positive-coordinate hypotheses. | Analytic factorisation only; no global selected-field moment equality. |
| `NavierStokes/GaussianErrorNaturality.lean` | cutoff/tail transport and `fromReference_*` Gaussian transport (23–455) | Naturality of Gaussian error, cutoff, tail, source, amplitude, and reference-to-actual transports under linear maps. | Transport is for Gaussian/coefficient data; no transport to `(M,I,J,S,Cp)`. |
| `NavierStokes/HolomorphicFamily.lean` | angle integrals, Cauchy values, disk-family differentiability (21–359) | Holomorphic/continuous parameter-family and Cauchy-integral regularity. | Complex regularity layer; no selected PDE endpoint theorem. |
| `NavierStokes/LocalAngularDiagonal.lean` | `rawSeries_eq`, `angularSum_eq_potentialSum`, zero-germ, smoothness, divergence (30–183) | Local angular series equals potential/direct diagonal, with smoothness, zero-germ, and divergence identities under similarity-domain hypotheses. | Genuine local `tsum`/potential connection; no five-moment radial integral after Cartesian lift and endpoint packaging. |
| `NavierStokes/ParametricEvenDescent.lean` | partial/fderiv decomposition, even radial descent, localisation (47–367) | Even radial descent and localised smoothness identities, including axis-local hypotheses. | Reduced-coordinate descent; no selected Cartesian moment transport. |
| `NavierStokes/ParametricFlatFactor.lean` | `kernel`, `factor`, `primitive`, factorisation and smoothness (53–259) | Parameterised flat factors and primitives with joint/parameter regularity. | Regularity/flatness support; no endpoint observable identity. |
| `NavierStokes/ParametricKernelBounds.lean` | coordinate/transform/amplitude/kernel bounds (29–324) | Derivative and iterated-derivative estimates for parameterised kernels and amplitudes. | Rate bounds that can feed jet interfaces; no moment payload. |
| `NavierStokes/PrimaryMaterialDefect.lean` | `NativeCoordinates`, `DirectionMatch`, material pullback, defect classes, finite jet bounds (27–450) | Native material coordinates, affine pullbacks, defect formulas/classes, and finite jet bounds. | Intermediate defect bookkeeping; no final `Witness` moment equality. |
| `NavierStokes/R3/GradientOperator.lean` | `gradientSq_*`, derivative sum and operator norm bounds (20–57) | Pointwise derivative estimates in Cartesian \(\mathbb R^3\), including continuity of the gradient square. | R3 analytic estimate; no radial moment transport. |
| `NavierStokes/R3/WeightedSobolev.lean` | compact/Lp/cutoff-gradient bounds and weighted Sobolev inequality (32–237) | Compact-support integrability, cutoff-gradient amplitude bounds, and weighted Sobolev control. | Supports energy/regularity estimates; no selected moment identity. |
| `NavierStokes/Scaling.lean` | core/length/Reynolds/scaling powers and carrier frequency bounds (24–230) | Algebraic scaling and frequency/viscosity bounds under positivity hypotheses. | Scaling layer; no physical-field moment transport. |
| `NavierStokes/SimilarityApproach.lean` | `upperScale_*`, `physical_q_*`, `jet_tendsto_zero` (24–93) | Similarity scale bounds and \(q\to0\) jet limits from explicit `JetRate` hypotheses. | Establishes a limit route, not the five radial observables. |
| `NavierStokes/SlowDivergence.lean` | `radialFlux_*`, `physical_flux_axial_balance`, `slow_order_divergence` (21–170) | Reduced radial flux, history/integral representations, axial balance, and slow-order divergence. Division-based smoothness is scoped away from the axis; history identities remove that division for later statements. | Real reduced-profile incompressibility result; not a global selected Cartesian endpoint theorem. |
| `NavierStokes/SmoothCovariance.lean` | strict cone, reconstruction, continuous/compact perturbation stability (27–346) | Smooth finite-dimensional covariance reconstruction and compact stability margins. | Covariance control; no endpoint moment transport. |
| `NavierStokes/SmoothPathFamily.lean` | path-family continuity/differentiability and ODE-family derivatives (34–263) | Smooth parameter/path families and derivative identities for ODE coefficient families. | Parameter regularity; no selected-field observable. |
| `NavierStokes/UniformCone.lean` | compact cone margins, gaps, stability (29–268) | Uniform compact cone positivity and perturbation-stability bounds. | Cone admissibility; no selected radial moment equality. |
| `NavierStokes/ValidBandGluing.lean` | `Compatible`, representatives, germs, derivatives, `representative_spatialCurl_*` (20–172) | Compatible local representatives glue to global fields while preserving smoothness, germs, jets, and spatial curls. | Strong local-to-global regularity/curl gluing; no theorem preserving the five global moments. |
| `NavierStokes/ValidDyadicBandCover.lean` | band cover, `Compatible`, field/germ/smoothness/jet bounds, endpoint extension (32–168) | Dyadic bands cover the sublevel region; compatible fields glue with jet bounds and zero germs. Endpoint extension requires an explicit one-sided extension premise. | Global regularity assembly; no `(M,I,J,S,Cp)` transport. |
| `NavierStokes/WaveStateRegularity.lean` | angular/covariance smoothness, local data, field sums/support (26–288) | Smooth angular averages, covariance increments, local wave-state data, support, and field-sum regularity. | Wave-state regularity; no selected endpoint moment identity. |

## Cross-cutting conclusions from this tranche

### Positive results that must not be erased

- The source contains substantive geometric carrier, Gaussian, covariance, curl, gluing, scaling, and R3 analytic machinery.
- `LocalAngularDiagonal`, `ValidBandGluing`, and `ValidDyadicBandCover` provide real local-series and local-to-global regularity results.
- `SlowDivergence` provides a genuine reduced radial-flux identity, with its axis restrictions visible in the theorem hypotheses.

### Remaining correspondence boundary

The inspected files establish regularity, support, local coordinate identities, rate bounds, and reduced flux/divergence identities. They do not establish the composition

\[
\text{profile moments}
\to \text{potential lift}
\to \nabla\!\times
\text{localisation}
\to \operatorname{tsum}
\to \text{periodised selected field}
\to \operatorname{barMoment}.
\]

The presence of curl/gluing identities and commutator formulas is therefore evidence that the relevant operators exist, not evidence that their five radial contributions cancel or are non-zero. The concrete selected-field calculation remains open.

## Register action

These 30 source files must be changed from `reachable_not_semantically_inspected` to `evidence_inspected` in the generated register. The register must be regenerated from `hardened_source_map_2026-09-27.json`; its JSON, Markdown, and HTML outputs are all derived artefacts and must remain synchronised.

