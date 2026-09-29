# Priority 148 source review: Euler cylinder graph, path, and support infrastructure

**Date:** 2026-09-29
**Scope:** twelve source files under `Euler/`, selected from the repository-wide review queue.
**Method:** direct source inspection with declaration and import anchors.
**Status:** tranche evidence only; this report does not claim that unreviewed repository files lack any declaration.

## Scope and classification

These files form a functional-analysis and cylinder-infrastructure tranche. They construct periodic measure descent, continuous (L^2)-valued paths, bilinear and advective products, support preservation, heat-product differentiation, and graph-trace (L^2) representatives. They are not part of the captured `NavierStokes.R3.Theorem` import closure.

The tranche contains real mathematical infrastructure. It does not, in the inspected declarations, connect that infrastructure to the selected Navier–Stokes witness, the five paper observables ((M,I,J,S,C_p)), `barMoment`, `FiveRowRank`, or an absolute pressure-Poisson representative.

## Direct source findings

| File | Source anchors | What is proved | Audit boundary |
|---|---:|---|---|
| `Euler/CylinderGraphRealization.lean` | 18-24, 26-38, 41-65 | Builds an (L^2) graph representative (x\mapsto f(x,\theta(x))) and proves its almost-everywhere representative and norm bound. | No radial moments, selected witness, pressure, or CMI statement. |
| `Euler/CylinderHeatEquation.lean` | 17-75, 78-135 | Defines finite real heat products; proves additivity, homogeneity, continuity, strong directional differentiation, and generator identities. | A heat/operator identity is not a Navier–Stokes field-level transport theorem. |
| `Euler/CylinderLocalSupport.lean` | 25-43, 47-58, 64-97 | Proves angular primitives, derivatives, potential paths, and slow-curl paths preserve spatial support; proves first derivatives vanish outside closed support. | Support preservation does not establish preservation of weighted radial observables or cutoff commutator cancellation. |
| `Euler/CylinderMeasureDescent.lean` | 32-48, 50-79, 81-89 | Defines the fundamental strip and proves measure-preserving cylinder covering and deck-equivariant descent. | Measure descent alone does not prove a torus-average/barMoment identity. |
| `Euler/CylinderPathAdvection.lean` | 17-30, 32-43, 62-82 | Constructs (p\cdot\nabla q); proves orbit smoothness, almost-everywhere representation, point-field equality, and H6 majorant. | No Cartesian selected field or five-moment payload. |
| `Euler/CylinderPathBilinear.lean` | 15-32, 39-66, 80-90 | Decomposes a bilinear operation into three components and proves the reconstructed path agrees a.e. and pointwise with the literal bilinear field. | This is a generic finite-dimensional bilinear lift, not the paper’s global moment bridge. |
| `Euler/CylinderPathBilinearBounds.lean` | 23-44 | Proves block and Gevrey-style majorant bounds for bilinear paths. | Rate bounds do not imply global radial integral identities. |
| `Euler/CylinderPathDerivativeProduct.lean` | 21-56 | Defines a derivative-product path; proves orbit smoothness, pointwise product representation, and majorant with a derivative shift. | No `barMoment` or selected-witness transport. |
| `Euler/CylinderPathIntegral.lean` | 18-30, 32-49 | Proves translation commutes with time integration and derives smooth translated paths from derivative data. | No connection to the exported Navier–Stokes endpoint. |
| `Euler/CylinderPathProduct.lean` | 42-58, 68-116 | Defines bounded bilinear path application, proves norm and smoothness, and identifies the actual (L^2) product a.e. and pointwise. | Exact product realization is not the five-observable realization claimed in the paper. |
| `Euler/CylinderPathProductBounds.lean` | 34-46, 48-58, 62-109 | Proves Sobolev-orbit and block/majorant bounds for products. | Quantitative bounds are not moment transport. |
| `Euler/CylinderPathProductSupport.lean` | 19-35, 46-82 | Proves scalar, bilinear, derivative-product, and advection paths preserve the prescribed support. | No integrated radial moment or pressure-Poisson conclusion. |

## Cross-check against the audit questions

### 1. Does the tranche contain a hidden five-moment bridge?

No declaration in these twelve files mentions `barMoment`, `FiveRowRank`, `PositiveOrderMoments`, `selected_witness`, `CandidateProperties`, or the five-observable tuple. The declaration signatures are instead parameterised by cylinder period, (L^2) paths, bounded linear maps, support sets, translations, derivatives, and majorant hypotheses.

This does **not** prove that no differently named bridge exists elsewhere. It proves only that this source tranche is not that bridge.

### 2. Do the support theorems settle the cutoff question?

No. `CylinderLocalSupport.lean` proves that fields and derivatives vanish outside a closed support. That is stronger than a mere filename-level association, but it is still different from proving that a cutoff-gradient commutator has zero or nonzero radial integral. The relevant mathematical distinction is:

\[
\operatorname{supp}(F)\subseteq S
\quad\not\Rightarrow\quad
\operatorname{barMoment}(F)=0
\]

The tranche therefore supplies support control, not the missing value-level observable calculation.

### 3. Do the path product and advection theorems supply the endpoint PDE?

They supply exact a.e. and pointwise reconstructions of generic products and (p\cdot\nabla q), together with regularity and majorants. They do not instantiate the selected Navier–Stokes candidate, prove its force provenance, or transport the paper’s radial moments through curl, localization, periodisation, and summation.

### 4. Source hygiene

A direct token scan of the twelve files found no `sorry`, `admit`, or `axiom` token. This is a source-hygiene observation, not a proof that every imported dependency is admitted-free.

## Classification

- **Positive infrastructure:** exact cylinder measure, support, product, advection, heat, and (L^2) representative results are present.
- **Outside captured NS endpoint:** these files are not evidence about the declaration-level contents of `NavierStokes.R3.Theorem` itself.
- **No transport evidence in tranche:** no five-moment, `barMoment`, selected-witness, or absolute pressure-Poisson bridge appears here.
- **No escalation:** this tranche produces neither a nonzero selected-field defect nor `False`.

## Next audit action

Continue with the remaining repository-wide queue, keeping the two questions separate: (i) whether a file contains genuine mathematics, and (ii) whether that mathematics is transported into the claimed OpenAI endpoint and paper semantics.
