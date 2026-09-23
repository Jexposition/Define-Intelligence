# Normative basis for `ClaySpec.lean`

This note records the source decisions made before comparing the independent
specification to OpenAI's Comparator statement.

Normative source: the official Clay Mathematics Institute PDF by Charles L.
Fefferman, including its appended erratum. Local audited copies:

- `../audit-artifacts/clay-navierstokes.pdf`
- `../audit-artifacts/clay-navierstokes.txt`

The OpenAI repository, Comparator definitions, and bridge were not used to
choose the mathematical content below.

## Literal transcription decisions

- Dimension is fixed to three.
- Both alternatives quantify over every real viscosity `ν > 0` before choosing
  the bad initial velocity and force.
- Equation (1) is stated component by component and contains the time
  derivative, convection, spatial Laplacian, pressure gradient, and force.
- Equation (2), equation (3), and every condition are restricted to `t ≥ 0`.
- Initial data are smooth and divergence-free.
- (4) and (5) quantify over every spatial derivative and every decay order;
  (5) also quantifies over every time derivative.
- (6)/(11) require joint space-time smoothness on the closed half-space.
- (7) is a single uniform-in-time energy bound, not merely membership in `L²`
  separately at each time. `MemLp` is included to prevent the convention for
  non-integrable Bochner integrals from making the formula vacuous.
- (8) imposes unit-coordinate periodicity on initial velocity and force.
- (9) imposes rapid temporal decay uniformly in the spatial variable.
- (10) imposes unit-coordinate periodicity on the velocity.
- The erratum is represented by imposing unit-coordinate periodicity on the
  pressure as part of an accepted periodic solution.

## Explicit interpretation boundaries

1. `C∞` on `ℝ³ × [0,∞)` is represented by Mathlib's `ContDiffOn` on the closed
   half-space. This is the chosen formal meaning of smoothness up to the time
   boundary.
2. A conventional spatial multi-index is encoded by a finite word of coordinate
   directions. Repeated indices give the multiplicities. For smooth functions,
   equality of mixed partials makes the order immaterial; the specification does
   not quotient words by permutations.
3. Absolute values of vectors and their derivatives are represented by the
   Euclidean norm. In finite dimension, componentwise versions are equivalent,
   but the PDF itself uses vector absolute-value notation in (4), (5), and (9).

These choices must not subsequently be weakened merely to make a Comparator
bridge provable. Any incompatible Comparator clause is an audit finding.
