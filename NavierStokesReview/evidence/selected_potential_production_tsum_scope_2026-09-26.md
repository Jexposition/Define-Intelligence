# Selected potential production: local `tsum` scope

Date: 2026-09-26

## Source and review artefacts

- Source API: `NavierStokes/SolenoidalDiagonal.lean`,
  `potentialSum_allJets_eventuallyEq_partial`.
- Review completion:
  `NavierStokesReview/src/completions/SelectedPotentialProductionTsumScope.lean`.
- Related finite-prefix calculations:
  `SelectedPotentialProductionFinitePrefix.lean` and
  `SelectedPotentialProductionTorusAverage.lean`.

## Zero-sorry result

The completion specialises the source theorem to
`ActualCandidateAssembly.selectedPotentialStages`. Under
`Tendsto a atTop atTop`, continuity of
`PhysicalWaveSum.physicalQ ActualPrimary.h`, and positivity of the scale at a
point `z`, it proves

$$
\exists N\;\forall k,\quad
D^k\operatorname{potentialSum}(z)
=D^k\operatorname{partialPotential}_N(z)
\quad\text{eventually near }z.
$$

The same prefix works for every derivative order `k`.

## Boundary of the result

This is local finite-prefix/all-jet transport only. It does not prove:

- passage of the equality through `PressureStream.torusAverage`;
- equality with the scalar family consumed by `barMoment` on the full domain;
- the radial weighted integral, including axis and tail terms;
- a nonzero remainder `Delta m != 0`;
- a kernel contradiction `False`.

CALC-38 therefore remains open, but the infinite-sum step now has a precise
source-backed local reduction theorem rather than an unspecified obstruction.
