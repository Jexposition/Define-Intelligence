# Priority 153 source review: Euler finite-grade algebra, path tensors, and fixed-endpoint evolution

**Date:** 2026-09-29
**Scope:** twelve current source files selected from the highest-priority unresolved queue.
**Method:** direct source inspection of imports, declarations, theorem statements, proof-side hypotheses, targeted endpoint/moment tokens, and source-hygiene tokens.
**Status:** tranche evidence only. This report does not claim that an unreviewed file lacks a declaration.

## Direct source findings

| File | Source anchors | What the source establishes | Audit boundary |
|---|---:|---|---|
| `Euler/ExternalTransportCommutator.lean` | 1-12; 17-28; 30-51; 53-107; 109-139 | Defines the literal differentiated transport commutator, expands it into scalar multiplication commutators, and proves H6 and weighted Gevrey radius-loss bounds under smoothness and all-order `MemLp` hypotheses. | This is Euler lifted-domain regularity and commutator control, not selected Cartesian moment transport or CMI force independence. |
| `Euler/FiniteGradeAlgebra.lean` | 1-22; 24-35; 61-100 | Defines finite evaluation, truncation, and bilinear convolution. Proves linear-map evaluation, exact bilinear grade expansion, vanishing above the finite degree, zero constant convolution, inverse evaluation, and high-grade tail extraction. | Finite graded algebra does not identify a physical field, pressure, or five-observable tuple. |
| `Euler/FiniteGradeAssembly.lean` | 1-18; 20-49; 51-74 | Reindexes primary and corrector coefficients, proves evaluation/shift identities, retains the final corrector in the finite expansion, and proves zero, interior, last, and above-range cases. | The assembly is coefficient-level Euler packet algebra, not `ActualCandidateAssembly.Witness`. |
| `Euler/FiniteGradeDiagonal.lean` | 1-4; 15-44 | Identifies bounded convolution with the natural-number antidiagonal and range sums, and proves dependence only on coefficients up to the target grade. | No Cartesian lift, localisation, pressure-Poisson, or five-moment transport is present. |
| `Euler/FiniteGradeSupport.lean` | 1-3; 13-61 | Proves truncation/support identities, finite evaluation extension, and the exact inverse-evaluation shift caused by a fast derivative. | These are finite support identities, not global selected-field estimates. |
| `Euler/FiniteGradeTriangular.lean` | 1-3; 14-59 | Proves strict lower-grade dependence for the slow convolution and the two new-grade contributions in the fast convolution. | Triangular coefficient dependence does not establish the Navier–Stokes endpoint or CMI admissibility. |
| `Euler/FinitePathTensor.lean` | 1-7; 16-69; 71-106 | Constructs a continuous path of finite-dimensional multilinear maps, proves evaluation and norm bounds, linearity, and commutation with iterated Fréchet derivatives. | This is an abstract compact-path tensor reconstruction; it carries no selected physical moments. |
| `Euler/FinitePathTensorIntegral.lean` | 1-5; 18-40 | Proves that the tensor-path map commutes with constant paths and the Bochner time integral under compactness and finite-dimensional hypotheses. | Integral interchange is not a theorem about the selected Cartesian `tsum` or radial observables. |
| `Euler/FiniteQuadraticCauchy.lean` | 1-10; 10-30 | Proves a finite-family quadratic-observation criterion forcing a sequence to be Cauchy. | This is an abstract convergence lemma, not a selected-witness or pressure theorem. |
| `Euler/FixedEndpointStrong.lean` | 1-10; 40-113; 157-203 | Constructs a fixed-coordinate endpoint inverse, proves range, H1, coordinate-equation, reconstruction, derivative, and forward-history identities under coercivity, frame, derivative, and smallness hypotheses. | Endpoint here is an Euler transverse-coordinate endpoint, not `NavierStokesR3.theorem_1_1`. |
| `Euler/FixedEndpointClassical.lean` | 1-19; 21-31; 40-124 | Builds displacement/acceleration maps, proves initial and terminal values, almost-everywhere velocity representation, differentiability, a projected equation, and uniqueness among twice-differentiable coordinate paths. | The uniqueness is conditional on finite-dimensional operator hypotheses and is unrelated to whole-space Navier–Stokes uniqueness. |
| `Euler/FixedEvolutionNaturality.lean` | 1-20; 22-71; 73-127 | Proves adjoint, Gram-operator, Gram-solver, velocity, acceleration, and endpoint-path intertwining for compatible rectangular operators and explicit coercivity/regularity hypotheses. | Naturality of this Euler coordinate reconstruction is not a field-level five-moment bridge. |

## Cross-checks against the audit questions

The finite-grade files contain genuine exact algebra. In particular, `FiniteGradeAlgebra` defines the finite evaluated packet explicitly, `FiniteGradeDiagonal` reduces the convolution to the antidiagonal, and `FiniteGradeTriangular` proves which coefficients can affect slow and fast grades. These are not empty declarations. They are also not the final physical observables claimed in the Navier–Stokes paper.

The tensor files establish an important but narrower fact: finite-dimensional multilinear maps valued in continuous paths can be reassembled pointwise, with norm control and commutation with iterated derivatives. `FinitePathTensorIntegral` extends that to the stated Bochner integral. No theorem in this tranche transports those identities through the selected spatial curl, localisation, periodisation, infinite `tsum`, torus averaging, or `barMoment` construction.

The fixed-endpoint files are conditional functional-analysis results. Their hypotheses explicitly include coercivity, frame derivative identities, operator bounds, positivity, and smallness conditions such as `K*(T^2/2) ≤ 1/2`. Their conclusions concern an Euler transverse coordinate history and its naturality under compatible operators. They do not instantiate the Navier–Stokes `Witness` or `CandidateProperties` predicates.

## Targeted absence and hygiene checks

A direct token scan of all twelve files found no `selected_witness`, `CandidateProperties`, `barMoment`, `FiveRowRank`, `PositiveOrderMoments`, `NavierStokes`, `R3`, five-observable tuple, `sorry`, `admit`, or `axiom` token. This is tranche-level evidence only. It is not a repository-wide nonexistence proof.

No nonzero selected-field defect, force-independence failure, pressure contradiction, or `False` was derived in this tranche. The appropriate classification is positive Euler infrastructure with no selected-Navier–Stokes transport evidence.

## Classification

- **Positive infrastructure:** finite graded packet algebra, exact triangular coefficient dependence, finite path tensor reconstruction, Bochner-integral interchange, conditional fixed-endpoint evolution, and compatible-operator naturality.
- **Endpoint boundary:** no declaration in this tranche reaches `ActualCandidateAssembly.Witness`, `selected_witness`, or the Navier–Stokes whole-space endpoint.
- **Correspondence status:** CTR-005 remains an open selected-field transport question; this tranche neither proves nor disproves the missing bridge.
- **No escalation:** no nonzero moment defect and no kernel-level `False`.

## Next action

Continue with the next highest-priority unresolved Euler regularity and fixed-evolution modules, while keeping Euler packet identities, the captured Navier–Stokes endpoint closure, and declaration-level selected-field transport as separate audit dimensions.
