# Clause-by-clause semantic comparison

## Scope and direction of the check

`ClaySpec.lean` was derived from the official Fefferman PDF and its appended
erratum, and conceptually frozen before `ComparatorDefinitions.lean` was read.
The normative source for the Clay side is therefore the PDF, not the OpenAI
bridge or Comparator code.  The comparison below concerns the corrected frozen
ClaySpec hash recorded in `CLAY_SPEC_FREEZE.md`.

For alternatives (C) and (D), proving that Comparator non-existence implies
Clay non-existence requires two differently directed maps:

1. Comparator admissible data imply Clay admissible data; and
2. every Clay-accepted solution for those data yields a Comparator-accepted
   solution.

The second map is deliberately Clay-to-Comparator.  Its contrapositive is what
turns “no Comparator solution” into “no Clay solution”.  Both maps are formal
theorems in `Gap.lean`; this is not an informal statement comparison.

## Clauses

| Clay clause | Independent ClaySpec | ComparatorDefinitions | Lean bridge finding |
|---|---|---|---|
| Dimension | `R3 := EuclideanSpace ℝ (Fin 3)` | the challenged instances specialize `n` to `3` | Exact. The gap fixes all types to `R3`. |
| Viscosity and quantifier order | `∀ ν : ℝ, 0 < ν → ∃ u₀, ∃ f, ...` | each challenged theorem takes `(ν : ℝ) (hν : 0 < ν)` and then produces `u₀,f` | Exact after universal closure in `ComparatorOptionC/D`. |
| Equation (1) | Componentwise time derivative + convection = `ν` times spatial Laplacian − pressure derivative + force | Vector equation using `derivWithin`, `fderiv`, `Δ`, and `gradient` | Formally identified by `partialTime_eq_slice`, `convectionComponent_eq`, `spatialLaplacianComponent_eq`, `pressureGradientComponent_eq`, and `equationOne_to_comparator`. |
| Equation (2) | Sum of coordinate derivatives of components | trace of the Fréchet derivative | Formally identified by `initialDivergence_eq` and `divergence_eq`. |
| Equation (3) | `u (x,0) = u₀ x` | `v x 0 = u₀ x` | Definitional after currying. |
| Smooth initial data | `ContDiff ℝ ∞ u₀` | `ContDiff ℝ ∞ u₀` | Exact. |
| Condition (4) | Every coordinate-word derivative and every natural decay order | operator norm of every full Fréchet jet, every natural derivative order, every real decay exponent | Comparator is sufficient. Evaluation of the jet on unit coordinate vectors is bounded by its operator norm; natural exponents are obtained from real exponents. Proved in `initialRapidDecay_of_comparator`. |
| Smooth force | joint `ContDiffOn ℝ ∞` on `ℝ³ × [0,∞)` | joint `ContDiffOn ℝ ∞` on `univ ×ˢ Ici 0` | Exact after `nonnegativeTime_eq` and uncurrying. |
| Condition (5) | Every spatial multi-index, time order, and natural decay order; denominator `1+‖x‖+t` | every total-order Fréchet jet and every real decay exponent with the same denominator | Comparator is sufficient. Mixed coordinate/time derivatives are evaluations of the total jet on unit directions. Proved in `forceRapidDecayR3_of_comparator`. |
| Condition (6) | joint smoothness of velocity and pressure on the closed half-space | same via uncurried fields | Exact under the stated closed-half-space smoothness trust boundary. |
| Condition (7) | vector-valued `MemLp ... 2 volume` plus one uniform integral bound | `MemLp` of the pointwise norm plus the same uniform integral bound | Every Clay solution gives the Comparator condition via Mathlib's `MemLp.norm`; the integral clauses coincide. Proved in `claySolutionR3_to_comparator`. |
| Condition (8) | unit-coordinate periodicity of `u₀` and `f` | `IsOnePeriodic` for `u₀` and each nonnegative-time force slice | Exact after currying/uncurrying. |
| Condition (9) | all mixed derivatives decay uniformly in space as `(1+|t|)⁻ᴷ` | all total jets decay uniformly in space as `(1+t)⁻ᴷ` for `t≥0` | Comparator is sufficient; `|t|=t` on the domain. Proved in `forceRapidDecayPeriodic_of_comparator`. |
| Condition (10) | unit-coordinate periodic velocity for `t≥0` | `IsOnePeriodic (v · t)` for `t≥0` | Exact after currying. |
| Condition (11) | joint smoothness of velocity and pressure | same | Exact under the stated smoothness trust boundary. |
| Pressure erratum | pressure is unit-coordinate periodic for `t≥0` | explicit `isOnePeriodic_pressure` | Exact. |
| Alternatives (C), (D) | admissible bad data and no Clay-accepted solution | admissible bad data and no Comparator-accepted solution | The two implications are kernel-checked as `ComparatorOptionC_to_ClayOptionC` and `ComparatorOptionD_to_ClayOptionD`. |

## Formalized non-literal identifications

The gap contains proofs—not comments—for:

- coordinate-word derivatives as evaluations of iterated Fréchet derivatives,
  both on all of `ℝ³` and within the closed time half-space;
- the operator-norm bound for those evaluations on unit coordinate/time
  directions;
- trace divergence versus the coordinate sum;
- the vector convection term versus `Σⱼ uⱼ ∂ⱼuᵢ`;
- Mathlib's spatial Laplacian versus the sum of second coordinate partials;
- Mathlib's gradient versus coordinate pressure derivatives;
- `derivWithin` in time versus the space-time directional derivative;
- real-exponent Comparator decay versus the natural-exponent Clay clauses;
- periodicity under currying and uncurrying; and
- vector-valued `MemLp` versus `MemLp` of the pointwise norm, together with the
  unchanged uniform energy integral.

## Trust boundaries and discrepancies

The following are explicit interpretation boundaries inherited from the
independent transcription of the PDF:

1. `C∞` on the closed half-space is interpreted as Mathlib
   `ContDiffOn ℝ ∞` there.
2. A multi-index is represented by a finite word of coordinate directions.
   Smoothness supplies the usual irrelevance of derivative order; quotienting
   words by permutations is unnecessary for the quantified decay property.
3. Vector absolute-value notation in (4), (5), and (9) is interpreted as the
   Euclidean norm.

No substantive discrepancy with Fefferman's clauses or the pressure erratum was
found.  None of these trust boundaries was introduced or weakened to make the
Comparator implication provable.
