# Priority 61-64 source review: localisation, curl, gluing, and copy bridges

Date: 2026-09-27
Scope: ten directly inspected reachable modules.
Method: source-first reading of definitions and theorem statements at the cited ranges.

## Executive result

This tranche closes several possible misunderstandings. The physical curl is
genuine Euclidean Frechet calculus and proves divergence-free output under C²
regularity. Positive-time copy gating proves equality of individual terms,
periodised sums, and jets on the preterminal region. The cutoff layers prove
smooth compact support and derivative bounds. Spacetime gluing proves C∞
assembly from one-sided normal time jets. Parametric modulation proves periodic
zero-mean primitives. The primary copy bridge proves equality with the actual
anchored copy solve, explicitly without an ambient energy inequality.

These are real bridges at their own layers. None of the inspected declarations
maps the final selected Cartesian field through the five paper observables
`(M,I,J,S,C_p)`, and the direct curl theorem does not by itself evaluate any
radial integral.

## Module findings

### `PositiveTimeCopyFamily.lean`

The gate is equal to the original copy on the preterminal region, zero outside
it, and equal in germs and all jets there (`PositiveTimeCopyFamily.lean:90-158`).
The equality is then lifted through periodised sums and vector sums
(`:140-188`). This is a genuine preterminal copy transport theorem, but its
observable is the copy field itself, not a global radial moment.

### `SpatialCurl.lean`

The module defines the physical Euclidean curl from the Frechet derivative
(`SpatialCurl.lean:23-52`). It proves mixed-partial symmetry, differentiability
of curl, and divergence-of-curl equal to zero for C² potentials
(`:54-92`). It also proves smoothness loss bounds, time-slice support, periodic
transport, and closed-support non-enlargement (`:94-128, :168-208`). This is a
strong kinematic result. It does not prove that a radial moment survives the
curl or that a selected `barMoment` equals any paper tuple.

### `TangentODE.lean`

The interval system defines integral curves, proves a contraction/fixed-point
solution on a finite interval, uniqueness, and linear uniformly Lipschitz
solutions (`TangentODE.lean:26-197`). This is a finite-dimensional tangent ODE
existence/uniqueness layer with no whole-space field observable.

### `CutStageEstimates.lean`

The module derives derivative bounds for the constructed scaled cutoff and
diagonal stage products (`CutStageEstimates.lean:28-180, :349-368`). The finite
family theorem uses one common doubling schedule for Cartesian stream
potentials, direct angular fields, and scalar pressures and applies the cutoff
to each component (`:370-428`). These are local jet estimates; no radial
integral or moment-preservation premise is present.

### `EvenSmoothDescent.lean`

Proves even-function descent through the square map, regularised radial
derivatives, Hadamard integral formulas, and vanishing derivative consequences
at the axis (`EvenSmoothDescent.lean:32-121, :126-231`). This is axis regularity,
not a global selected-field moment identity.

### `R3/ComparisonCutoffs.lean`

Defines a smooth compactly supported whole-space bump, scaled cutoff, local
energy weight, and pressure multiplier, with exact one/zero regions and support
bounds (`R3/ComparisonCutoffs.lean:28-100`). It supplies the comparison
localisation used by R3 uniqueness estimates, not the selected field's radial
profile map.

### `SmoothCutoffs.lean`

Defines the actual Mathlib `ContDiffBump`, proves C∞ regularity, support, one
and zero regions, and scaled/time-switch infrastructure
(`SmoothCutoffs.lean:25-78`). The file explicitly makes no analyticity claim.
No moment theorem is present.

### `SpacetimeGluing.lean`

Defines past/future gluing and proves full Frechet derivative gluing from value
and normal-derivative matching (`SpacetimeGluing.lean:192-258`). It then proves
finite-order and C∞ gluing from all one-sided normal time-slice jets
(`:260-300`). This establishes regularity of the assembled object, not
preservation of radial integrals.

### `ParametricModulation.lean`

Constructs normalised interval primitives, proves periodicity and exact
zero-mean identities, and extends them with compact parameter cutoffs
(`ParametricModulation.lean:23-107, :181-218`). It proves the extended
primitive remains periodic, smooth, and zero mean (`:218-287`). These are
one-dimensional modulation identities, not the final Cartesian five moments.

### `PrimaryCopyBridge.lean`

Reindexes the primary frame and source along copy paths and proves the
reconstructed path satisfies the actual projected tangent equation and equals
the anchored copy solve by uniqueness (`PrimaryCopyBridge.lean:42-116,
:210-228`). The direct canonical bridge and all ordinary tensor derivatives are
then transferred (`:459-483`). The module explicitly says no ambient
reference-energy or output-bound hypothesis is assumed (`:167-174`), and the
seeded path is not identified with the zero-entry copy solve (`:487-539`).

## Cross-layer disposition

| Question | Source-grounded answer |
|---|---|
| Is the physical curl genuine and divergence-free? | Yes, under the stated C² spatial regularity. |
| Are preterminal copy sums and jets transported? | Yes, through the positive-time gate under its hypotheses. |
| Are cutoffs and spacetime gluing smooth? | Yes, with explicit support and one-sided jet hypotheses. |
| Is the actual copy solve identified? | Yes, by the primary bridge's uniqueness theorem. |
| Does this establish final `(M,I,J,S,C_p)` transport? | No. |
| Does this prove a selected-field nonzero defect, impossibility, or `False`? | No. |

## Controlled conclusion

The localisation layer is not a fake shell: it contains genuine curl,
support, smoothness, copy, and gluing theorems. The remaining semantic issue
is narrower: no inspected theorem composes these layer-local identities with
the final selected field's radial moment engine. The audit therefore records
strong positive infrastructure while keeping endpoint paper-to-code
correspondence unresolved.
