# Priority 93 source review: limits, debt matching, lifespan, reindexing, pulse history, and radial flux

Date: 2026-09-28
Method: direct inspection of the six Lean source files; findings are declaration-scoped and conservative.

## Scope

This tranche follows the live reachable queue after the Priority 92 R3 energy and polar-graph review. It checks whether six modules add a selected-field moment transport theorem, a contradiction, or only intermediate construction/regularity results.

## Source findings

### `NavierStokes/JointResidualLimits.lean`

The module imports `NavierStokes.SpacetimeEndpoint` and the locally uniform convergence API. It defines `OneSidedExtension`, `AwayExtensions`, and `VanishingJointJets`, then proves joint boundary convergence, continuity and locally uniform convergence of boundary limits, compact-uniform convergence, non-bottom past-filter nonemptiness, extension independence, compatible derivative recurrences, smoothness of the boundary family, and the extended residual theorems (`extendedResidual_agrees`, `extendedResidual_smooth`, `extendedResidual_flat_at_origin`, `exists_residual_limits`, and `exists_smooth_compatible_limits`).

This is genuine endpoint-limit and residual-flatness infrastructure. It does not define `barMoment`, evaluate the five paper observables, or transport them through the selected Cartesian field into `Witness`.

### `NavierStokes/MatchingDebtBounds.lean`

The module imports `NominalProfile` and `ActivationContinuation`, sets `Debt := FiveProfileMoments.Debt`, and develops smooth parameter/radial clamps, extended fields and debt, reset-vector jet bounds, vanishing sums, fixed bounds, prefix budgets, normalised debt bounds, matching bounds, ordered matching thresholds/continuations, and existence of assembled and nominal witnesses with small coefficients.

This is substantive five-coordinate reduced-profile matching and debt control. It is not a theorem identifying the resulting debt coordinates with the final selected Cartesian radial observables or requiring such an equality at `ActualCandidateAssembly.Witness`.

### `NavierStokes/MaximalLifespan.lean`

The module imports `PeriodicUniqueness`, defines the lifespan domain, `ClassicalSolution`, agreement and extension predicates, and proves restriction, overlap agreement, periodic slab bounds, exclusion of continuous extension after time one, maximality/greatest-lifespan results, admissible-lifespan characterisation, and non-global-solution consequences. It also records that the candidate force is nonzero before one under its hypotheses.

These are whole-space lifespan consequences relative to the formal candidate and supplied force. They do not add force-independence, an autonomous-forward-force predicate, or selected-field five-moment transport.

### `NavierStokes/MeanBoundsReindex.lean`

The module proves pullback and return equivalences for strip round-trips, majorants, finite-jet bounds, band bounds, mean/unweighted classes, operator/base/cumulative/increment bounds, context bounds, residual-block bounds, and uniform velocity under linear isometric reindexing.

This is exact chart/rate-class invariance. Its conclusions are inequalities and class membership under reindexing, not value-level equality of the selected whole-space `barMoment` tuple.

### `NavierStokes/PulseEnergyHistory.lean`

The module imports outgoing histories and pulse lag data. It proves the pulse normalisation and weight identities, the actual pulse energy weight and parameter derivative, the incoming prefix energy and its derivative, source-factor and energy-source bounds, initial-history bounds, normalised-history bounds, forcing and ratio bounds, and corrected pulse-history bounds using the supplied energy solve.

This is concrete energy-history and forcing control for the pulse stage. It neither exports the five selected Cartesian observables nor closes the endpoint correspondence.

### `NavierStokes/RadialFluxResidual.lean`

The module imports `AxisymmetricResidual` and `LocalAxisymmetricResidual`. It defines the radial quotient `radialB V := -V/(2s)`, proves its regularity and derivative identities, derives the divergence coefficient and radial-flux velocity identity, defines `fluxResidual`, and proves `residualRadial_radialB` and `physical_radial_flux_residual` under the explicit positive-radius hypothesis.

This is a real local axisymmetric residual bridge. Its domain excludes the singular axis through the positive radial-energy condition, and its output is a local residual coefficient/equality. It is not a global radial-moment evaluation and does not connect to the public `Witness` five-observable tuple.

## Classification

| Module | Classification | Selected-field five-observable transport? | Contradiction? |
|---|---|---:|---:|
| `JointResidualLimits.lean` | Positive endpoint-limit/flat-residual infrastructure | No | No |
| `MatchingDebtBounds.lean` | Positive reduced five-coordinate debt/matching infrastructure | No | No |
| `MaximalLifespan.lean` | Positive relative lifespan consequence | No | No |
| `MeanBoundsReindex.lean` | Positive exact rate-class chart invariance | No | No |
| `PulseEnergyHistory.lean` | Positive pulse energy/history control | No | No |
| `RadialFluxResidual.lean` | Positive local off-axis radial residual bridge | No | No |

## Controlled conclusion

Priority 93 strengthens the record of the construction: endpoint limits, reduced debt matching, lifespan reasoning, chart reindexing, pulse energy histories, and local radial residual identities are all represented by actual declarations. The tranche does not prove or disprove the full composition

\[
\text{reduced profiles}
\longrightarrow \text{Cartesian curl/localisation/tsum/periodisation}
\longrightarrow \text{global radial observables}
\longrightarrow \texttt{Witness}.
\]

Therefore no `\Delta m \ne 0`, impossibility theorem, kernel `False`, or final selected-field moment-transport claim is recorded from this tranche.

## Register action

The six path-qualified source records are added to `semantic_coverage_register.py`. The authoritative JSON, Markdown, HTML, and public Markdown/HTML mirrors are regenerated from `hardened_source_map_2026-09-27.json`.
