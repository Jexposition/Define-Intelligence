# Priority-79 source review: axis operators, chart jets, matching cones, physical coordinates, signed covariance, and wave-edge extension

Date: 2026-09-28
Scope: direct source review of six modules selected from the generated reachable queue.
Method: read the Lean declarations and their local proofs; classify what each module proves and whether it reaches the selected Cartesian endpoint or the paper's five cumulative radial observables.

## Scope and result

This tranche examined:

- `NavierStokes/AxisOperators.lean`
- `NavierStokes/BaseChartJets.lean`
- `NavierStokes/MatchingConeBounds.lean`
- `NavierStokes/PhysicalCoordinateBounds.lean`
- `NavierStokes/SignedCovariance.lean`
- `NavierStokes/WaveEdgeExtension.lean`

The modules are substantive and reachable. They add real operator, chart, matching, covariance, weighted-jet, and edge-extension mathematics. The inspected declarations do not state the composed map

\[
 (M,I,J,S,C_p)_{m reduced}
 \longmapsto
 \operatorname{barMoment}\bigl(\operatorname{torusAverage}(u_{\rm selected})\bigr)
 \]

for the final selected Cartesian field, and they do not state a nonzero defect, an impossibility theorem, or `False`.

## Declaration-level findings

### `AxisOperators.lean`

The file imports `AxisCoefficientSpace` and defines finite Leibniz sums (`leibnizSum`, lines 27-42), derivative/continuity rules (53-74), input jets and their norm bounds (77-82), product jet families (87-120), bounded linear and bilinear jet families and lifts (124-339), and row operators for averaging, primitive, radial inverse, parameter primitive, and multiplication by the radial variable (349-467).

The local result is an operator calculus on `AxisSpace`. It does not define a Cartesian velocity field, a torus-average observable, a `barMoment` map, or a selected `Witness` equality. Its radial inverse bounds are estimates for jet operators, not evaluations of the global field moments.

### `BaseChartJets.lean`

The file imports `BasePhaseGeometry`, `SlowBorelBase`, `SimilarityHomogeneity`, `ConstructedSlowBase`, and `PositiveRepresentatives`. It defines the actual normalised chart (`physicalInput`, `normalizedCoordinates`, lines 206-239), chart jet/envelope estimates (244-328), the frequency and axial chart fields (358-446), and concrete positive-cell estimates (744-923).

Two declarations are positive field-level evidence:

- `axial_eq_normalized_velocity` (687-701) identifies the axial component of the constructed chart field with the normalised velocity component.
- `frequency_eq_normalized_velocity` (703-721) identifies the frequency component with the normalised swirl/angular component and invokes the local angular-moment identity.

These identities are component-level chart equalities. They do not compose with the full `tsum`, spatial localisation, periodisation, pressure, torus averaging, and `ActualCandidateAssembly.Witness` boundary to prove the five paper observables.

### `MatchingConeBounds.lean`

The file imports `MatchingDebtBounds` and `OutgoingEntranceCone`. It defines shape-transition models and lower bounds (22-129), shape jets and source identities (161-226), angular barriers and relaxed-profile conditions (238-296), and seed/source jet bounds (304-551). The `PreparedWitness` structure and `preparedWitness_exists` occur at lines 952-979.

The matching results constrain reduced profiles and cone admissibility under explicit smallness and source hypotheses. They do not quantify over the final selected Cartesian field and do not return an equality for `(M,I,J,S,C_p)` at the exported endpoint.

### `PhysicalCoordinateBounds.lean`

The file defines physical points, inverse coordinates, inverse differentials and inverse jets (23-150), normalised compact regions and dilation estimates (161-302), homogeneous pullback and derivative bounds (312-425), and physical time-reflected coordinates together with derivative bounds for `q`, `eta`, and `x` (434-575).

This is genuine chart regularity and scaling control. The domain is the positive-time/off-axis coordinate region used by the chart machinery. No global radial observable evaluator or selected-field transport theorem is present.

### `SignedCovariance.lean`

The file imports `PartitionedCovariance`, `FlatCovariance`, `WeightedQuotients`, and `WeightedClasses`. It defines the signed covariance increment and proves inverse/cross reconstruction (23-75). It then defines finite and assembled radial/tangent waves, finite-support reductions, and bilinear covariance identities (107-377), followed by physical chart scaling and covariance identities (385-425).

The later sections prove weighted jet-class bounds for signed quotients, square columns, balanced signed squares, native variants, and compactly supported masked extensions (449-742 and 752-976). These results are meaningful local covariance and wave-assembly results. They do not define or prove the global `barMoment` of the selected Cartesian `tsum` field.

### `WaveEdgeExtension.lean`

The file imports `PrimaryCopyBounds`, `PhysicalClassBounds`, `FlatZeroExtension`, and `VariableGaugeMean`. It defines moving radial windows and smooth inside/outside extensions (24-71), boundary derivative and Taylor-series results (78-227), logarithmic coordinates and edge weights (115-283), native radius/profile extensions (438-640), zero-germ covers and native regularity (684-825), and mean-coordinate extensions (839-892).

The result is strong edge regularity: fields can be extended across moving radial boundaries with controlled jets and flat zero germs. No declaration evaluates the selected whole-space field against `(M,I,J,S,C_p)`, and no theorem identifies the extension boundary terms with a vanishing or nonvanishing global moment defect.

## Correspondence classification

| Layer | Direct evidence | What remains unproved at this layer |
|---|---|---|
| Axis operators | finite Leibniz/product/primitive/inverse jet operators | global field observable transport |
| Base charts | actual normalised chart and component identities | full selected Cartesian five-observable equality |
| Matching cones | shape, angular barrier, seed/source jets, prepared witness | endpoint `Witness` transport |
| Physical coordinates | inverse charts, dilation, homogeneous derivative bounds | global radial integration semantics |
| Signed covariance | exact local covariance reconstruction and weighted bounds | selected-field `barMoment`/tuple identity |
| Wave edge extension | smooth moving-edge and zero-germ extensions | moment boundary cancellation or defect |

## Audit disposition

The six modules are marked `evidence_inspected` in the authoritative semantic register. This tranche strengthens the record of genuine intermediate mathematics and narrows the remaining question to composition into the selected endpoint. It does not justify `Delta m != 0`, impossibility, `False`, or a claim that the upstream machinery is absent.
