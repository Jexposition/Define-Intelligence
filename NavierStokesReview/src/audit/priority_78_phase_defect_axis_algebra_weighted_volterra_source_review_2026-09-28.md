# Priority 78 source review: phase defect, axis algebra, weighted classes, and Volterra regularity

Date: 2026-09-28
Scope: fourteen directly inspected Lean source files in `NavierStokes/`
Method: live source declarations and theorem statements were inspected. This is a bounded source classification, not a claim that the remaining open modules have been cleared.

## Source findings

### Phase and physical control

`ActualPhaseDefect.lean` defines the actual chart-phase change, slot coordinates, material-coordinate identities, and radial/axial/temporal slow-change formulas. It is a concrete phase/coordinate comparison layer, but the inspected declarations do not define a global radial-observable map or connect one to `Witness`.

`ActualPhaseJetBounds.lean` proves affine positive-jet bounds, phase-size constants, phase-cell containment/mapping, and native remainder/jet infrastructure. It supplies actual phase regularity controls, not the five-observable endpoint equality.

`ActualSignedControl.lean` identifies pulse matrices/vectors with the actual phase construction and proves phase-geometry jet/range bounds through a `ReferenceBounds` interface. The source explicitly describes the estimates as geometric phase controls; it does not transport reduced-profile moments into the final selected Cartesian field.

### Axis algebra and charts

`AxisEvaluationAlgebra.lean` contains actual complex phase factors, carrier/mode differentiability, along-mode identities, cylindrical Laplacian identities, angular-independent cases, and the three-component complex mode construction. This is substantive cylindrical differential algebra. It is not a theorem evaluating the selected field's (M,I,J,S,C_p)-type observables.

`PolarCharts.lean` defines four genuine polar chart rotations and inverses, proves norm/radius invariance, positivity and smoothness, and chart-offset identities. It confirms that the chart layer is real and four-charted, but no global radial moment transport to `selected_witness` is stated in the inspected declarations.

### Weighted geometry and jets

`PhysicalClassBounds.lean` defines flat geometry and proves edge-weight, uniform flatness, moving-strip flatness, and absorption of edge growth into uniform coefficient classes. This is a real weighted-class bound layer; it is not a physical moment evaluator.

`ReferenceJetBounds.lean` proves parameter/radial derivative identities, coefficient-family jet constants and bounds, and natural (U)/log-coordinate value and derivative bounds. These are reference-path coefficient estimates, with no complete selected-field observable equality.

`WeightedClasses.lean` defines strip data, growth, majorants, and polynomial/edge-weight domination. It provides the generic weighted local-jets framework. It does not encode the paper's five cumulative radial quantities.

`WeightedQuotients.lean` proves iterated derivative bounds for powers, square-root and inverse-square-root bounds, composition jet bounds, and positive-power composition estimates. This is regularity infrastructure and does not bridge to `Witness`.

`AxisWeightEstimates.lean` defines the exact coefficient weight, square-decay factors, radial/parameter shifts, product-weight sums, radial divisors, mixed-weight sums, and jet-product bounds. This is substantive coefficient convolution and radial-inverse control, but it carries no selected-field five-observable equality.

`EdgeWeightJets.lean` proves polynomial edge-jet masses, compact-coefficient jet bounds, weighted smoothness, edge division/vanishing identities, mixed derivative bounds, and weighted products/powers. This is substantive edge regularity, not endpoint moment transport.

### Actual radial integral and Volterra layers

`HarmonicCalculus.lean` proves actual complex harmonic carrier/mode calculus, scalar and vector cylindrical Laplacian identities, exact harmonic divergence/longitudinal identities, finite-jet contraction bounds, and graph derivative formulas. This is a strong local cylindrical differential layer, but it does not state the complete selected-field five-observable equality.

`StressActivation.lean` constructs smooth activation/damping functions, weighted fields, weighted primitives, derivative identities, zero-at-origin behaviour, and controlled fields from a flat primitive integral. This is positive evidence that the relevant primitives are constructed rather than postulated. It does not state the complete five-observable equality for the selected Cartesian field.

`VolterraRegularity.lean` defines the actual weighted radial mean and regular primitive, proves continuity, equality-on-domain, differentiation under the actual weighted integral, and (C^\infty) regularity including diagonal and scale-family forms. This is an important integral-regularity layer, but it does not identify its outputs with the paper tuple or connect them to final `Witness` packaging.

## Calibrated conclusion

This tranche adds genuine positive evidence for the chart, phase, weighted, cylindrical, primitive, and Volterra layers. It does not prove a nonzero defect, an impossibility theorem, or `False`. The live correspondence question remains specific: locate a declaration-level composition from the exact reduced observables and actual radial integrals through the selected stage/curl/localisation/periodisation/`tsum`/pressure path into `ActualCandidateAssembly.Witness`, or record that the inspected dependency path still lacks that composition.
