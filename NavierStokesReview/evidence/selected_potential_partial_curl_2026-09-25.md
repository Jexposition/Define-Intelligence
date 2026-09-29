# Selected potential partial-curl transport

Date: 2026-09-25  
Classification: selected source identity  
Status: proved without `sorry`, custom axioms, or `unsafe`

## Result

The selected potential branch has a finite local representation before the
terminal time. For every (x) in `PhysicalWaveSum.preterminal`, the selected
schedule supplies an (N) such that

\[
\operatorname{velocitySum}(a,q,A)
  =_{\mathcal N x}
\nabla\times\operatorname{partialPotential}(a,q,A,N).
\]

This is a field-level identity for the selected Cartesian potential velocity.
It is stronger than a generic statement that a transport theorem is missing,
but it is not yet a radial moment calculation.

## Lean statement

The theorem is

```lean
selected_potential_velocity_eventuallyEq_partial_curl
```

in

```text
NavierStokesReview/src/completions/SelectedPotentialPrefixCurlExpansion.lean:24-48
```

It is obtained from

```text
NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean:34-55
NavierStokes/SolenoidalDiagonal.lean:238-244
```

The first source theorem supplies local finiteness of the selected potential
`tsum`. `spatialCurl_eventuallyEq` then transports that eventual equality
through the spatial-curl operator.

## Meaning for the selected construction

The source defines the production potential velocity as the spatial curl of
the potential sum (`NavierStokes/SolenoidalDiagonal.lean:188`). The new result
therefore establishes the exact local order of operations:

```text
selected potential stages
  -> cut-stage potential tsum
  -> finite partial potential near x
  -> spatial curl of that finite partial potential
```

The identity does not replace the finite curl with the sum of stage curls.
That stronger expansion requires each cut stage to be known smooth on the
same open neighbourhood. The selected endpoint currently exports summed
smoothness and stage smoothness on the physical sublevel domain, while the
remaining theorem must transport the cut-stage hypotheses to the full
preterminal neighbourhood used by the curl expansion.

An attempted direct application of
`SolenoidalDiagonal.velocitySum_eventuallyEq_sum` was rejected by the Lean
type checker because its `hA` argument requires
`ContDiffOn ... PhysicalWaveSum.preterminal`, whereas
`ActualCandidateAssembly.stages_smooth` supplies smoothness on
`ActualCandidateConstruction.physicalDomain`. The latter is the strict
sublevel

\[
\{w : w_1<1\}\cap\{w : q(w)<q_{\mathrm{big}}\},
\]

not the entire preterminal domain. This is the precise remaining domain
transport obligation behind the stagewise expansion; the rejected application
was not promoted as evidence of a mathematical contradiction.

## What this does not prove

This result does not establish any of the following:

* a Cartesian-to-cylindrical projection for the selected potential branch;
* an identity after `torusAverage` or `barMoment`;
* a nonzero cutoff/curl commutator or weighted radial remainder;
* a selected-field contradiction or Lean `False`.

The live calculation remains the potential/curl contribution together with
the already identified cutoff-weighted direct term. The proof graph therefore
continues through the radial projection rather than treating this local curl
identity as a completed disproof.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

Result:

```text
Build completed successfully (3723 jobs).
```
