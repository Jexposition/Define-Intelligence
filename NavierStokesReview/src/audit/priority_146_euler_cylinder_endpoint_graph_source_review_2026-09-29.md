# Priority 146: Euler cylinder endpoint, reflection, embedding, and graph source review

Date: 2026-09-29
Scope: direct raw-source review of twelve files in the Euler cylinder endpoint, symmetry, embedding, and graph tiers
Method: imports, declaration signatures, theorem bodies where operator meaning is load-bearing, and bounded searches for the selected Navier–Stokes endpoint vocabulary

## Result

This tranche contains genuine Euler cylinder endpoint analysis. It proves conditional pointwise identities, regularity, support, angular zero-mean preservation, reflection/parity, graph restriction estimates, and Gevrey bounds. It does not state the selected Navier–Stokes witness, the `CandidateProperties` endpoint, a global pressure-Poisson representative, the five radial observables `(M,I,J,S,Cp)`, a non-zero defect, or `False`.

The key positive result is not empty: `Euler/CylinderEndpointSupport.lean:83-109` proves preservation of an explicit angular-average condition, and `Euler/CylinderEndpointPointwise.lean:135-173` upgrades almost-everywhere endpoint identities to pointwise labelled coordinate and velocity identities using continuity. These are real operator-level theorems in the Euler cylinder model. They cannot be promoted to the Navier–Stokes five-moment bridge without a separate theorem connecting the models and observables.

## File-by-file map

| File and anchors | What it defines or proves | Audit relevance |
|---|---|---|
| `Euler/CylinderEndpointParity.lean:24-55` | Odd reflection identities for endpoint forcing, coordinate, acceleration, velocity, and derivative under even coefficient hypotheses. | Euler cylinder symmetry; no selected Navier–Stokes field or radial moment theorem. |
| `Euler/CylinderEndpointPointwise.lean:90-173` | Pointwise endpoint paths, initial/terminal displacement data, projected equation, label-coordinate identification, and pointwise velocity identification. | A genuine endpoint reconstruction theorem for the Euler cylinder model. It does not mention `CandidateProperties`, `Witness`, `selected_witness`, or `theorem_1_1`. |
| `Euler/CylinderEndpointRegularity.lean:50-101` | Smooth translation-orbit propagation through endpoint forcing, coordinate, acceleration, velocity, and derivative paths. | Euler regularity layer, not selected Cartesian Navier–Stokes transport. |
| `Euler/CylinderEndpointSupport.lean:28-73` | Spatial support inheritance through frame, forcing, coordinate, acceleration, velocity, and derivative paths. | Support is conditional on supported terminal data; it is not pressure support or a whole-space Navier–Stokes conclusion. |
| `Euler/CylinderEndpointSupport.lean:77-109` | Explicit zero angular-mean preservation for endpoint forcing, coordinate, acceleration, velocity, and derivative. | A real invariant-preservation theorem, but its observable is `average P`, not `(M,I,J,S,Cp)`. |
| `Euler/CylinderEndpointUnitBounds.lean:30-147` | Unit endpoint budgets for constant, forcing, coordinate, acceleration, velocity, and derivative histories. | Quantitative Euler cylinder bounds; not the Navier–Stokes `NativeBounds` endpoint. |
| `Euler/CylinderFieldReflection.lean:21-138` | Lp reflection, involution, representative identities, supported reflection, and coefficient-operator intertwining. | Symmetry infrastructure for Euler cylinder fields; no selected Navier–Stokes bridge. |
| `Euler/CylinderForwardParity.lean:24-54` | Reflection naturality and odd-solution preservation for supported forward linear evolution under even coefficients. | Euler evolution symmetry; no CMI endpoint or five-observable transport. |
| `Euler/CylinderGradientEmbedding.lean:18-82` | Scalar lifting, gradient evaluation, and embedding of a closed mean-solenoidal gradient space into the cylinder gradient space. | Functional-analysis infrastructure; no radial observable equality. |
| `Euler/CylinderGraphAffine.lean:14-57` | Affine representative/derivative identities and an L2 graph-trace norm estimate. | Graph restriction estimate; not the selected Cartesian field. |
| `Euler/CylinderGraphDerivative.lean:16-57` | Transfers a genuine cylinder/angular derivative to a derivative on a fixed phase graph. | Derivative regularity only; no moment or pressure theorem. |
| `Euler/CylinderGraphGevrey.lean:19-108` | Graph-frequency factors and conditional factorial/Gevrey and L2 derivative bounds after periodic-cover pullback. | Quantitative Euler graph regularity; not the Navier–Stokes moment bridge. |
| `Euler/CylinderGraphPath.lean:23-71` | Continuous spatial L2 path from cylinder values and angular derivatives through graph realization. | Euler graph-local continuity; no `selected_witness` or CMI conclusion. |

## Boundary and dependency findings

The twelve reviewed files import `Euler.*` cylinder, graph, reflection, gradient, and regularity modules. A bounded raw-source search found no occurrences of `NavierStokes`, `ActualCandidate`, `selected_witness`, `theorem_1_1`, `FiveRowRank`, `PositiveOrderMoments`, or `barMoment` in the tranche. This is a source-level statement about the reviewed files, not a claim that they are dead or absent from other repository roots.

The graph results use `Lp` representatives, almost-everywhere equalities, continuity upgrades, and explicit phase maps. None of those constructions supplies a theorem of the form

\[
\operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p).
\]

Likewise, the endpoint support theorems concern the Euler cylinder `Supported` subspace. They do not establish support or Poisson semantics for the selected Navier–Stokes pressure on `\mathbb{R}^3`.

## Controlled classification

- Module reality: genuine compiled Euler cylinder endpoint, symmetry, embedding, graph, and bound infrastructure.
- Mathematical content: several conditional invariant and reconstruction theorems are present.
- Selected Navier–Stokes correspondence: not stated in this tranche.
- Five-observable transport: not stated in this tranche.
- Global pressure/Poisson semantics: not stated in this tranche.
- Kernel contradiction: none obtained.
- Queue meaning: these files are now source-reviewed; remaining modules retain their queue status. No semantic conclusion is inferred from import closure alone.
