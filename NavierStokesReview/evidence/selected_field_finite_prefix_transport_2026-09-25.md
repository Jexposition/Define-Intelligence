# Selected-field finite-prefix transport

## Question

Does the concrete `selected_witness` hide its potential series behind an
empty or vacuous limit, and does the source already transport that series to
the radial `barMoment` quantities used by the five-row construction?

## Source trace

| Source | Exact construction | Finding |
|---|---|---|
| `NavierStokes/ActualCandidateAssembly.lean:1165-1175` | Defines the three selected stage histories using the closed selected budget and threshold. | The endpoint uses concrete stage histories, not an abstract zero placeholder. |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1185` | `selected_witness` and `selected_candidate`. | The exported candidate is obtained from the actual selected schedule and assembled fields. |
| `NavierStokes/SolenoidalDiagonal.lean:31-42` | `cutStage`, `potentialSum`, and `partialPotential`. | The series is a natural-indexed sum of cutoff stages. |
| `NavierStokes/SolenoidalDiagonal.lean:46-67` | `eventually_zero_tail` and `potentialSum_eventuallyEq_partial`. | At positive scale, a neighbourhood has a finite active prefix; the tail is exactly zero there. |
| `NavierStokes/SolenoidalDiagonal.lean:140-147` | `potentialSum_allJets_eventuallyEq_partial`. | The same finite prefix represents every iterated Frechet derivative locally. |
| `NavierStokes/ActualCandidateConstruction.lean:953-970` | `initialPotentialStage_field` and `positivePotentialStage_field`. | Each selected positive stage is a sum of two potential fields and the mean stream stage. |
| `NavierStokes/DirectAngularDiagonal.lean:64-71,208-227` | Angular field, cutoff multiplication, and divergence preservation. | The angular component is a genuine cylindrical field with explicit radius factors and smooth cutoff multiplication. |
| `NavierStokes/ActualMeanPotentialRealization.lean:29-40,293-316` | Meridional embedding, Cartesian potential, and curl identities. | The mean potential is transported into Cartesian velocity through a positive-radius chart and spatial curl. |
| `NavierStokes/DefectIncrementBounds.lean:214-220` | `barMoment` and `barMoment_apply`. | `barMoment` consumes `ScalarField (Point P)` and computes a torus-averaged radial integral. |
| `NavierStokes/FiveRowRank.lean:241-246` | `FiveRows`. | The first two zero identities constrain correction profiles `dv` and `ga`, not the selected Cartesian field. |
| `NavierStokes/NominalProfile.lean:955-994` | `idealPrefixRows` and `outgoing_moments_ideal`. | The repository has an explicit five-coordinate nominal profile formula, but this theorem is not an identification with the selected Cartesian `tsum`. |

## Review-side theorem

`NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean` compiles
without `sorry`, `axiom`, or `unsafe`. It proves:

```lean
selected_potential_sum_locally_finite
selected_potential_sum_all_jets_locally_finite
```

Both theorems use `ActualCandidateAssembly.selected_witness`, the selected
schedule, the positive preterminal scale, and the actual selected stage
aliases. They rule out the claim that the selected `tsum` is justified only
by an empty limit or a vacuous tail.

## Calculation boundary

The source does not provide a theorem of the form

```lean
barMoment k selectedCartesianProfile = selectedCartesianMoment
```

and the types do not identify the selected `VelocityField` with the scalar
radial profile expected by `barMoment`. The missing work is therefore an
actual Cartesian-to-cylindrical transport calculation, including cutoff
derivatives, curl terms, axis terms, outer-support terms, and torus averaging.

No nonzero selected remainder `Delta m ≠ 0` has been proved in this audit. The
finite-prefix theorem strengthens the calculation target, but it does not
itself yield `False`.

## Status

The selected-series route is now source-grounded and non-vacuous. The
affirmative paper still lacks an exported selected-field five-moment identity;
that is a live burden-of-proof defect. A kernel contradiction remains
conditional on deriving a concrete nonzero remainder for the selected field.
