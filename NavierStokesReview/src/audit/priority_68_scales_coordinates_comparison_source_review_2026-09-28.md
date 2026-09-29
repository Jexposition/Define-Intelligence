# Priority-68 source review: scales, endpoint coordinates, and comparison estimates

Date: 2026-09-28
Scope: direct source inspection of four reachable Lean modules.
Evidence class: source declarations and theorem signatures only.
This report does not claim a global absence result and does not claim a nonzero moment defect.

## `NavierStokes/ChartScales.lean`

- Lines 5–11 identify the module as the implementation of the manuscript's native chart scales, floor index, coefficient comparisons, carrier scale, and decay estimates.
- Lines 21–34 define `Tg`, `Lambda`, `rho`, `kappa`, `radialExponent`, `Q`, `S`, `epsilon`, `nativeIndex`, `timeCoefficient`, and `radialCoefficient`.
- Lines 122–157 prove native-index and time-coefficient inequalities.
- Lines 161–208 prove the exact radial-coefficient identity and two-sided coefficient bounds.
- Lines 210–255 prove reciprocal coefficient and rounded carrier-frequency bounds.
- Lines 257–307 prove slow-power identities and asymptotic decay/cutoff consequences.

This is genuine scale and asymptotic infrastructure. The inspected declarations contain no `barMoment`, `FiveRows`, `PositiveOrderMoments`, `NominalProfile.Witness.five_moments`, `CandidateProperties`, or selected-field `tsum` transport statement. Its bounds can support later estimates, but they do not themselves identify any global radial observable.

## `NavierStokes/EndpointCoordinates.lean`

- Lines 1–2 import `PositiveRepresentatives` and `SlowBorelBase`.
- Lines 23–40 define the positive endpoint root and prove its scalar equation and slope.
- Lines 72–89 define the time-axial map, endpoint domain, `qExtension`, `etaExtension`, `XExtension`, and `chartExtension`.
- Lines 91–138 prove smoothness and openness on the stated domain.
- Lines 140–185 prove endpoint agreement, physical agreement, eventual equality, and jet equality for the similarity chart.
- Lines 228–283 lift the extension to Cartesian spacetime coordinates and prove smoothness, positivity/range facts, endpoint agreement, eventual equality, and jet equality.
- Lines 303–326 prove generic smooth-composition and jet-equality lemmas.

This is a real coordinate-extension layer and records a domain restriction through `domain` and the nonzero endpoint hypotheses used by `endpointRoot_pos` and the endpoint theorems. It does not evaluate a Cartesian vector field, a torus average, a radial integral, or the five paper moments. Coordinate/jet agreement is therefore not evidence of moment transport.

## `NavierStokes/R3/CompactComparisonBounds.lean`

- Lines 1–3 import finite-energy, compact-time-integral, and comparison-cutoff modules.
- Lines 24–30 establish compact spatial support for slices.
- Lines 33–47 establish a global first-derivative bound from compact support and smoothness.
- Lines 49–98 establish `L^3` slice membership, continuity of the cube-norm integral, an integral formula, and a uniform `L^3` bound.
- Lines 102–129 establish plateau/large-radius derivative-zero facts for comparison cutoff weights.
- Lines 133–155 derive `uniformFiniteEnergy_of_compact_slab`.

These are whole-space comparison and compactness estimates. They do not contain the selected candidate, pressure Poisson reconstruction, `barMoment`, `FiveRows`, or a theorem linking comparison cutoffs to the paper's five cumulative radial quantities.

## `NavierStokes/R3/ComparisonFiniteEnergy.lean`

- Lines 22–38 relate square-integrable slices to `MemLp` and establish slice continuity.
- Lines 42–121 prove nonnegativity, difference square-integrability, difference-energy bounds, and uniform finite-energy consequences.
- Lines 124–172 establish pointwise tensor-product domination, measurability, integrability, and an `L^1` estimate for the nonlinear tensor difference.
- Lines 175–228 lift the bounds uniformly over time and express them in comparison `L^p` notation.

This module proves ordinary energy and nonlinear tensor-difference estimates for arbitrary velocity fields satisfying its hypotheses. It is not a profile-moment module and it does not transport reduced profile data into the selected Cartesian construction.

## Correspondence classification

| Question | Result from these four files |
|---|---|
| Are the modules substantive? | Yes. They prove scale, coordinate, compactness, energy, and tensor estimates. |
| Do they establish selected-field five-moment transport? | No declaration inspected has that target or payload. |
| Do they establish a nonzero cutoff/curl defect? | No. They do not perform that value-level calculation. |
| Do they undermine the existing endpoint finding? | No. They add boundedness, coordinate, and comparison infrastructure while leaving the selected-field moment correspondence unestablished in this tranche. |

## Register action

The four modules are entered as `evidence_inspected` with direct source anchors. The full register and its public Markdown/HTML mirrors must be regenerated after this report is added.
