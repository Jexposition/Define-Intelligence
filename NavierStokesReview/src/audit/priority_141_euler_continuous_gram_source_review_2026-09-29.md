# Priority 141: Euler continuous Gram/tensor source review

Date: 2026-09-29
Scope: direct raw-source review of five queued Euler modules selected from the
repository-wide register. This is a source review, not a completion claim for
the Euler branch and not a verdict about the Navier--Stokes endpoint.

## Files and declared roles

| File | Raw declarations reviewed | What the file establishes |
|---|---|---|
| `Euler/ContinuousBoundedTensor.lean` | `coordinates` 26, `reassembly` 41, `tensorPath` 64, `tensorPath_eq` 74, `tensorPath_norm_le` 97, `tensorPathMap` 130, `tensorPathMap_norm_le` 143, `tensorPath_iteratedFDeriv` 150 | Reassembles finite-dimensional multilinear tensors from continuous bounded paths; proves pointwise evaluation, a norm bound, linear/continuous map structure, and derivative commutation. |
| `Euler/ContinuousGramAcceleration.lean` | `accelerationPath` 27, `accelerationPath_equation` 41, `accelerationPath_norm` 48, `accelerationPath_ae` 81 | Constructs a continuous acceleration from a coercive Gram inverse and proves its equation, norm estimate, and an almost-everywhere identification under explicit hypotheses. |
| `Euler/ContinuousGramPath.lean` | `gramPathUnit` 31, `gramInversePath_eq_ringInverse` 48, `solve` 53, `solve_equation` 57, `solve_left_inverse` 64, `solve_norm` 71, `gramPath_contDiff` 77, `gramInversePath_contDiff` 82, `solve_contDiff` 96, `gramPath_bound` 104 | Constructs a continuous-in-time Gram operator path and its inverse, then proves two-sided inverse identities, norm control, parameter smoothness, and derivative bounds. |
| `Euler/ContinuousGramGevrey.lean` | `leftMultiplicationMap` 47, `leftMultiplicationMap_norm` 54, `inversePath_gevrey` 75, `solution_gevrey` 124 | Propagates factorial/Gevrey bounds through the uniformly coercive continuous Gram inverse and solution operator under explicit majorant assumptions. |
| `Euler/ContinuousGramSobolev.lean` | `solution_block_gevrey` 21 | Propagates a fixed Sobolev-word-block/Gevrey estimate through the continuous Gram solve, conditional on coercivity, smoothness, and input bounds. |

## Import and dependent-module trace

The five files import the following upstream layers:

- `ContinuousBoundedTensor` imports `FinitePathTensor` and bounded continuous
  map norms.
- `ContinuousGramPath` imports `ContinuousPathComposition`,
  `TransverseGramPath`, and `TransverseStrongEstimates`.
- `ContinuousGramGevrey` imports `ContinuousGramPath`, `BoundedInverseGevrey`,
  and `TimeLpGramGevrey`.
- `ContinuousGramSobolev` imports `ContinuousGramGevrey` and
  `TimeLpGramSobolev`.
- `ContinuousGramAcceleration` imports `TransverseStrongEstimates` directly.

The raw import search identifies these consumers: `BoundedTensorCoordinates`,
`CylinderSmoothTimeField`, `ContinuousAccelerationSobolev`,
`ContinuousAccelerationGevrey`, `TransverseForwardRegularity`,
`MeanClassicalTime`, `TransverseFixedEvolution`, and
`TransverseForwardCoefficientGevrey`, with the expected transitive chain from
`ContinuousGramPath` through the Gevrey/Sobolev layers.

## Formal content and limits

These files are genuine, non-vacuous Euler functional-analysis infrastructure.
They are not placeholders and they do not themselves use the selected
Navier--Stokes names `ActualCandidateAssembly`, `CandidateProperties`,
`VelocityField`, `PressureField`, `navierStokesResidual`, `barMoment`,
`FiveRowRank`, or `PositiveOrderMoments`. Their hypotheses are explicit:
coercivity/lower bounds, complete inner-product spaces, finite-dimensionality
where required, smoothness, and derivative majorants. The `accelerationPath_ae`
result is conditional on an almost-everywhere strong equation; it does not
derive that equation from the Euler or Navier--Stokes PDE.

The review therefore finds no endpoint transport theorem, pressure Poisson
identity, force-provenance condition, or five-observable equality in these
modules. That is a scope boundary, not evidence that the Euler construction is
false. Conversely, these generic inverse and regularity results cannot be used
as evidence that the OpenAI paper's selected Cartesian field preserves
`(M,I,J,S,C_p)`.

## Classification

`source_reviewed`: direct raw declarations and imports inspected.
`mathematical finding`: genuine conditional continuous Gram/tensor/regularity
results.
`CMI relevance`: indirect Euler infrastructure only; no selected
Navier--Stokes endpoint bridge located in this tranche.
`falsification result`: none. No nonzero moment defect, impossibility theorem,
or kernel-level `False` was obtained.
