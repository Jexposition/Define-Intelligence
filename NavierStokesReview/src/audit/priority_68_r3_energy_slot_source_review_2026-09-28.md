# Priority-68 source review: R3 comparison energy and slot geometry

Date: 2026-09-28
Scope: direct source inspection of seven reachable Lean modules.
Evidence class: source declarations and theorem signatures only.
This report records substantive intermediate results and does not claim a global absence, a nonzero selected-field defect, or `False`.

## `NavierStokes/R3/ComparisonSetup.lean`

Lines 22–53 define the comparison slab, weak spatial derivative notation, `comparisonLpNorm`, `l2Sq`, `gradientSq`, weighted energy/dissipation rates, a dissipation root, an `L^6` cutoff quantity, and the componentwise nonlinear tensor difference. These are comparison-layer observables and definitions; no selected witness, radial moment tuple, `barMoment`, or five-row transport target is present.

## `NavierStokes/R3/LocalizedDifferenceEnergy.lean`

- Lines 34–56 prove integrability and nonnegativity of cutoff-weighted energy and dissipation.
- Lines 62–101 establish continuity, derivative, and integrability facts for weighted energy rates.
- Lines 102 onward prove the localized difference energy balance and its integrated derivative form under explicit smoothness, support, residual, and divergence hypotheses.

This is a genuine local energy identity for differences of two fields. The cutoff is a scalar weight in the comparison estimate. The file does not identify the selected field with the paper's five cumulative radial observables.

## `NavierStokes/R3/LocalizedLaplacian.lean`

- Lines 35–74 prove integrability of weighted partial-square, gradient-square, cutoff second-partial, cutoff-Laplacian, and weighted-Laplacian terms.
- Lines 85–142 prove integration-by-parts identities for weighted second partials and the Laplacian.
- Lines 144–153 lift the result to the spatial Laplacian of a time slice of a velocity field.

This file supplies local analytic integration identities used by the energy route. It does not state a radial moment functional or a selected `tsum`/curl/localisation transport theorem.

## `NavierStokes/R3/SharpEnergyBound.lean`

- Lines 20–53 prove a square-root energy bound from an integral differential inequality.
- Lines 56–68 prove the corresponding squared-energy bound.

This is scalar real-analysis infrastructure. It has no field construction, pressure semantics, torus average, or five-moment payload.

## `NavierStokes/R3/SpatialCauchySchwarz.lean`

Lines 22–46 prove the spatial work estimate that bounds the integral of the velocity-force pairing by the square roots of the two spatial `L²` energies. This supports energy estimates but does not perform a selected-field radial projection or moment calculation.

## `NavierStokes/R3/WholeSpaceEnergyLimit.lean`

- Lines 25–38 prove convergence of cutoff-weighted integrals toward the whole-space integral.
- Lines 40–68 prove zero-field consequences from vanishing `L²` or weighted-rate bounds.
- Lines 70–93 state the final scalar cutoff-removal/uniqueness consequence under the supplied comparison hypotheses.

This is a whole-space energy-limit layer. Its cutoff removal concerns scalar energy integrals, not preservation of the five paper moments under the selected Cartesian construction.

## `NavierStokes/SlotGeometry.lean`

- Lines 28–87 define a linear plane cover and prove injectivity, norm bounds, and positivity properties.
- Lines 95–129 define lattice slot centres and prove positivity, norm, and injectivity facts.
- Lines 138–187 define torus equivalence and prove lattice/cover separation properties.
- Lines 208–282 define rectangles and prove common-radius existence.
- Lines 311–376 prove torus-equivalence algebra, cover compatibility, lifted-support separation, and disjoint lifted slots.
- Lines 387–477 define oriented rectangles and prove slot/label construction consequences.

This is substantive geometric support infrastructure. `torusEq` and lifted supports do not amount to a `torusAverage` of the selected field, nor to a radial `barMoment` equality.

## Correspondence classification

| Question | Result from these seven files |
|---|---|
| Are the modules substantive? | Yes. They prove comparison energy, integration, whole-space cutoff limits, work bounds, and slot geometry. |
| Do they prove selected-field five-moment transport? | No declaration inspected has that target or payload. |
| Do they prove a nonzero cutoff/curl defect? | No. The energy cutoffs and slot supports are not evaluated against the five radial observables here. |
| Do they change the endpoint classification? | They strengthen the positive intermediate PDE record while leaving the selected-field paper-to-endpoint correspondence open. |

## Register action

The seven modules are entered as `evidence_inspected` with direct source anchors. The full JSON, Markdown, and HTML registers and the control documents must be regenerated after this report is added.
