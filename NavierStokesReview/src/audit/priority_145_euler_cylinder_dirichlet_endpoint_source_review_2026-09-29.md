# Priority 145: Euler cylinder Dirichlet and endpoint source review

Date: 2026-09-29
Scope: direct raw-source review of twelve files in the Euler cylinder/Dirichlet tier
Method: imports, declaration signatures, theorem bodies where the operator meaning is load-bearing, and bounded endpoint-symbol search

## Result

This tranche contains genuine Euler cylinder functional analysis. It does not establish a selected Navier–Stokes endpoint theorem, a five-observable transport identity, a global pressure representation, a non-zero defect, or `False`.

The important positive result is narrower: the code proves several conditional operator-intertwining and zero-angular-mean statements for the Euler cylinder coefficient model. Those results should not be silently promoted to the radial five-moment correspondence claimed for the Navier–Stokes construction.

## File-by-file map

| File and anchors | What it defines or proves | Audit relevance |
|---|---|---|
| `Euler/CylinderCoverDescent.lean:14-114` | Chooses a section of the periodic cover, descends deck-invariant fields, and proves measurability, continuity, measure preservation, and descended left inverses. | Quotient/cover geometry for Euler cylinder fields; no Navier–Stokes endpoint or radial moment theorem. |
| `Euler/CylinderCoveringDerivative.lean:17-38` | Identifies covered fields, their Fréchet derivative, smoothness, and spatial derivative through the cylinder-time regularity layer. | Regularity transport on the cover; no selected-field observable. |
| `Euler/CylinderCoverTensor.lean:18-68` | Converts coordinate-word derivatives to Euclidean iterated derivatives and bounds their norms. | Coordinate-to-cover derivative control; not the Cartesian `selected_witness` pipeline. |
| `Euler/CylinderDirichletNaturality.lean:38-96` | Proves velocity, acceleration, continuous velocity, and derivative intertwining under coefficient-space translations/adjoints. | Genuine operator naturality, but within the Euler cylinder Dirichlet model. |
| `Euler/CylinderDirichletMean.lean:27-50,65-99,125-159` | Proves angular averaging commutes with the full operator and with velocity/acceleration/physical derivative paths; under an explicit zero-average hypothesis, the corresponding outputs have zero angular mean. | This is an actual invariant-preservation theorem, but for cylinder angular averaging, not the five radial observables `(M,I,J,S,Cp)` of the Navier–Stokes paper. |
| `Euler/CylinderDirichletParity.lean:22-115` | Proves reflection, sign, and oddness identities for the Dirichlet coefficient paths. | Symmetry control in the Euler cylinder model; no selected NS transport. |
| `Euler/CylinderDirichletTranslation.lean:17-130` | Defines shifted coefficient data and proves translation identities for frame, derivative, Hessian, velocity, acceleration, and physical derivative. | Translation covariance; not a global Cartesian moment theorem. |
| `Euler/CylinderDirichletRegularity.lean:41-166` | Propagates smoothness of coefficient orbits and physical paths under translation. | Euler regularity layer; no endpoint CMI field. |
| `Euler/CylinderDirichletSobolev.lean:44-111` | Gives word/block Sobolev bounds for coefficient and velocity paths. | Quantitative regularity bounds; no five-moment equality. |
| `Euler/CylinderEndpointBounds.lean:11-60` | Provides coordinate, acceleration, velocity, and derivative endpoint budgets. | Bounds for the Euler cylinder terminal model; not the Navier–Stokes `NativeBounds` endpoint. |
| `Euler/CylinderEndpointEquation.lean:24-87` | Proves almost-everywhere projected coordinate equations, endpoint velocity/derivative identities, and a physical balance under explicit tangency, range, and flow hypotheses. | A real Euler cylinder equation theorem. Its variables are `Coefficients`, `CylinderL2`, `Q`, `Q₁`, `M`, and `m`; it is not `CandidateProperties`, `Witness`, `selected_witness`, or `theorem_1_1`. |
| `Euler/CylinderEndpointLabels.lean:19-67` | Defines labelled frame, derivatives, Hessian, coordinate, and velocity maps with pointwise identities. | Label/coordinate infrastructure for Euler cylinder data; no NS endpoint bridge. |

## Import and symbol boundary

The reviewed files import `Euler.*` modules and mathematical-analysis support. A bounded search of these twelve raw files found no `NavierStokes`, `ActualCandidate`, `selected_witness`, `theorem_1_1`, `FiveRowRank`, `PositiveOrderMoments`, or `barMoment` reference. That is a source-level fact about this tranche, not a claim that the files are dead or outside every repository build.

The strongest moment-adjacent theorem here is `EulerCylinderDirichlet.Coefficients.velocityPath_mean_zero` and its acceleration/physical-derivative analogues at lines 135-159. Its input is an explicit angular-average premise

\[
\operatorname{average}_P(f(t))=0,
\]

and its output is preservation of that same angular zero-mean property through the Euler cylinder coefficient operators. It does not identify a Cartesian velocity field with the five radial quantities \((M,I,J,S,C_p)\), nor does it transport a `NominalProfile` certificate through `curl`, localisation, `tsum`, or the selected Navier–Stokes witness.

## Endpoint classification

- **Module reality:** genuine, compiled Euler cylinder descent, symmetry, translation, regularity, Sobolev, and endpoint-equation infrastructure.
- **Selected Navier–Stokes correspondence:** not stated in this tranche.
- **Five-observable transport:** not stated in this tranche.
- **Global pressure/Poisson semantics:** not stated in this tranche.
- **Kernel contradiction:** none obtained.
- **Remaining action:** inspect the next priority-zero cylinder modules and separately keep the captured `NavierStokesR3.theorem_1_1` closure distinct from repository-wide Euler infrastructure.
