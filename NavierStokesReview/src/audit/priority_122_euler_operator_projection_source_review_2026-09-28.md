# Priority 122: Euler operator, projection, and compact-support source review

## Scope

This tranche reviews the next ten repository-indexed Euler modules. They are
outside the captured Navier--Stokes endpoint closure. The review records what
their declarations actually establish, so that genuine Euler infrastructure is
neither called dead code nor misused as evidence for the selected
Navier--Stokes Cartesian radial-moment bridge.

## Declaration-level findings

| File | Anchors | Actual content | Boundary |
|---|---:|---|---|
| `Euler/ClosedTranslationGraph.lean` | 1, 16--18, 21--37, 40--50, 53--84 | Proves additive translation paths, propagation of derivative data, uniform convergence of translation orbits, and closedness of a translation-derivative graph in the Euler cylinder L2 space. | Euler translation/operator graph; no selected NS observable. |
| `Euler/CoefficientPathOrbit.lean` | 1, 21--23, 31--54, 56--95 | Proves smoothness, derivative identities, orbit derivative paths, and coefficient-path norm bounds for bounded coefficient fields. | Euler coefficient-path regularity; no radial `barMoment`. |
| `Euler/CoefficientPathSobolev.lean` | 1--2, 28--36, 43--94 | Defines Sobolev operators along coefficient paths and proves value, derivative, and continuity results. | Euler Sobolev operator layer; no selected NS endpoint transport. |
| `Euler/CoerciveEndpointBounds.lean` | 1, 24--37, 40--119, 129--132 | Defines correction, endpoint, and form operators and proves operator-norm/subtraction bounds. | Abstract Euler operator estimates; no selected Cartesian field. |
| `Euler/CompactCurlBounds.lean` | 1--2, 19--30 | Derives a compact-set vorticity bound from spatial derivative bounds and the curl matrix operator. | Euler compact vorticity estimate; not the selected NS curl/localisation chain. |
| `Euler/CompactParameterIntegral.lean` | 1--4, 20--26, 29--51, 53--72 | Defines a parameter derivative and proves differentiability and smooth parameter dependence of compact interval integrals. | Generic parametric calculus; no five-moment transport. |
| `Euler/CompactProjectedEulerLaw.lean` | 1--3, 32--51, 55--66 | Proves the weak projected Euler derivative identity on compact smooth solenoidal test fields from the Euler existence/smoothness assumptions. | Euler comparator weak law; no CMI C/D selected witness. |
| `Euler/CompactProjectedPairing.lean` | 1, 21--26, 30--46, 49--65 | Removes the Helmholtz projection in solenoidal pairings and derives integral forms for projected Euler right-hand sides. | Euler pressure/projection pairing; no selected NS pressure or radial tuple. |
| `Euler/CompactSmoothBounds.lean` | 1--3, 22--30, 32--48 | Relates spatial derivatives to joint derivatives and proves compact spatial/time derivative bounds for smooth Euler solutions. | Euler regularity bounds; no selected NS packaging. |
| `Euler/CompactSupportBoundedPath.lean` | 1--2, 17--25, 29--55, 57--70 | Bundles compactly supported continuous families as bounded-continuous-function paths and proves uniform-norm continuity. | Generic compact-support path construction; no radial observable. |

## Scope and integrity checks

All ten files were source-read and declaration-indexed. A direct source census
found no `sorry`, `admit`, or `axiom` token in any of them. Their imports show
real Euler-side dependencies, including Euler proof, translation, Sobolev,
projected pairing, compact smoothness, and classical calculus modules.

The strongest result in this tranche is the weak projected Euler law and its
compact solenoidal pairing. None has the selected-field composition

\[
 u_{\rm selected}
 \longrightarrow \operatorname{torusAverage}(u_{\rm selected})
 \longrightarrow \operatorname{barMoment}(\cdot)
 \longrightarrow (M,I,J,S,C_p).
\]

This is a bounded source classification, not an absence theorem over the
repository and not a refutation. It does not alter the status of CTR-005.

## Anti-blindside conclusion

The review separates three facts that must not be conflated:

1. Euler has genuine compact-support, projection, vorticity, and operator
   regularity theorems.
2. Those theorems are outside the captured Navier--Stokes endpoint closure.
3. They do not prove or disprove transport of the five paper observables by
   the selected Cartesian Navier--Stokes field.

The remaining audit must continue through both OpenAI roots and the selected
field's actual definitions. No theorem is counted as a bridge merely because
its name contains `curl`, `compact`, `projection`, `moment`, or `transport`.
