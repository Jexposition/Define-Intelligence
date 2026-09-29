# Priority 150 source review: Euler cylinder slow curl, Sobolev, embedding, and mean infrastructure

**Date:** 2026-09-29
**Scope:** twelve current source files under `Euler/`, selected from the direct-review queue.
**Method:** raw source inspection of imports, declarations, theorem signatures, targeted semantic tokens, and source-hygiene tokens.
**Status:** tranche evidence only. This report does not claim that an unreviewed file lacks a declaration.

## Direct source findings

| File | Source anchors | What the source establishes | Audit boundary |
|---|---:|---|---|
| `Euler/CylinderSliceRepresentatives.lean` | 1; 17-34 | Identifies continuous cylinder path representatives from equal slice data, including scalar representatives. | Representative equality is not selected-field moment transport. |
| `Euler/CylinderSlowCurl.lean` | 1-3; 38-47; 55-77; 80-107 | Defines three curl terms, their finite path sum, almost-everywhere reconstruction, the classical field, and equality with the lifted slow-curl operator. | Genuine curl reconstruction, but no `(M,I,J,S,C_p)` observable or selected Navier–Stokes endpoint equality. |
| `Euler/CylinderSlowCurlBounds.lean` | 1; 39-72 | Proves a block bound in which one spatial derivative consumes one shift while the external radius is unchanged. | A derivative/rate bound is not a global radial moment identity. |
| `Euler/CylinderSlowCurlWeight.lean` | 1-2; 30-59; 74-101 | Proves weight commutation, path normalisation, normalised block bounds, and time-derivative normalisation/bounds. | Weight and time-profile identities do not identify the selected Cartesian field with the paper observables. |
| `Euler/CylinderSobolevDensity.lean` | 1; 16-63 | Defines Sobolev mollifiers, proves boundedness, convergence, representative compatibility, word-level almost-everywhere identities, and density of smooth representatives. | Density and approximation do not imply moment transport. |
| `Euler/CylinderSobolevDerivatives.lean` | 1; 13-103 | Defines truncation and derivative indices/operators, proves operator bounds, value recovery, derivative existence, and translation compatibility. | Sobolev operator calculus has no selected-field or five-moment conclusion. |
| `Euler/CylinderSobolevEmbedding.lean` | 1-2; 18-67 | Defines an embedding constant and proves mollifier and pointwise value bounds for sufficiently high Sobolev order. | Pointwise Sobolev control is not the paper's radial integral bridge. |
| `Euler/CylinderSobolevOperators.lean` | 1; 16-53; 68-145 | Defines array/value/word operators, derivative-sum norms, translation-commuting lifted operators, and norm preservation/continuity. | Operator commutation and norms do not establish global pressure or moment semantics. |
| `Euler/CylinderSobolevOrbit.lean` | 1-2; 23-71 | Defines Sobolev translation orbits and assembled paths, with coordinate and smoothness theorems. | Orbit smoothness is not endpoint transport. |
| `Euler/CylinderSobolevWordBounds.lean` | 1-2; 23-89 | Defines word operators and proves word-level, summed-level, and block-level Sobolev bounds for the orbit. | Quantitative word bounds do not state or imply `(M,I,J,S,C_p)` equality. |
| `Euler/CylinderSpatialEmbedding.lean` | 1-3; 23-61; 79-109 | Embeds ordinary spatial `L²` fields into the cylinder, proving linearity, norm scaling, continuity, and inner-product identities. | An `L²` embedding is not a Cartesian radial-moment or pressure-Poisson theorem. |
| `Euler/CylinderSpatialMean.lean` | 1-3; 18-44; 51-86 | Defines a bounded cylinder-to-spatial mean as an adjoint, and proves translation covariance, retraction on constant embeddings, and invariance under angular averaging. | This is a cylinder spatial mean operator, not the paper's five cumulative radial observables or selected Navier–Stokes transport. |

## Cross-checks against the audit questions

`Euler/CylinderSlowCurl.lean` is direct evidence that the repository contains a real three-component curl reconstruction. Its `term`, `path`, `path_ae`, `field_formula`, and `field_eq_liftedSlowCurl` declarations connect coefficient paths and derivative paths to a classical lifted field. This corrects any claim that the repository contains only scalar or purely axial plumbing.

The same file does not prove that the curl reconstruction preserves any of the paper's five cumulative radial quantities. `CylinderSlowCurlBounds` proves a rate/block estimate, and `CylinderSlowCurlWeight` proves weight and time-normalisation identities. Neither theorem has a conclusion involving `barMoment`, `FiveRowRank`, `PositiveOrderMoments`, `selected_witness`, `CandidateProperties`, or `(M,I,J,S,C_p)`.

`CylinderSpatialEmbedding` and `CylinderSpatialMean` establish a genuine `L²` embedding/adjoint pair. In particular, `mean_embedding` is a retraction identity and `mean_average` states invariance under the cylinder angular-average operator. These are meaningful functional-analytic facts, but they are not the `barMoment` radial observable and do not establish an absolute pressure-Poisson representative on `R³`.

The inspected declarations contain no occurrence of `barMoment`, `FiveRowRank`, `PositiveOrderMoments`, `selected_witness`, or `CandidateProperties`. They also contain no declaration whose input and output identify a final Cartesian field with `(M,I,J,S,C_p)`.

This is a **tranche-level absence result**. It does not prove repository-wide nonexistence and does not assert that these modules are dead. The register treats repository inventory, captured `NavierStokes.R3.Theorem` closure, and direct semantic review as separate dimensions.

## Source hygiene

A direct token scan of all twelve files found no `sorry`, `admit`, or `axiom` token. This is a tranche-level observation and does not certify every imported dependency.

## Classification

- **Positive infrastructure:** genuine curl reconstruction, path representatives, weight/time normalisation, Sobolev operators, density, embeddings, translations, and bounded spatial means.
- **No selected-field transport evidence in this tranche:** no five-observable equality, `barMoment` result, selected-witness theorem, or absolute pressure-Poisson theorem.
- **No escalation:** the tranche proves neither a nonzero selected-field defect nor `False`.

## Next action

Continue the direct source queue with the remaining Euler spatial-mean, representative, terminal-amplitude, development-bridge, and divergence-free heat modules, while maintaining separate labels for repository inventory, captured endpoint closure, and declaration-level semantic inspection.
