# Selected potential stagewise curl transport

Date: 2026-09-25

## Result

The zero-sorry theorem
`selected_potential_velocity_eventuallyEq_stage_curls_on_physicalDomain`
compiles in `NavierStokesReview`.

For every point in the source-defined open physical domain, the selected
potential velocity is eventually equal to a finite sum of the curls of the
individual cut stages:

$$
u_{mathrm{pot}} =_{mathcal N x}
\sum_{j<N}\operatorname{curl}
\bigl(\operatorname{cutStage}(a,q,A_j)\bigr).
$$

The theorem uses the actual source boundary. `physicalDomain` is the open
sublevel domain on which `ActualCandidateAssembly.stages_smooth` exports
per-stage smoothness. It does not silently extend that hypothesis to all of
`preterminal`.

## Commutator exposed by the selected expression

The source theorem `selected_cut_stage_curl_expansion` gives, for each finite
stage,

$$
\operatorname{curl}(\chi_j A_j)
=\chi_j\operatorname{curl}(A_j)
 +(\nabla\chi_j)\times A_j.
$$

Its first component is

$$
\chi_j(\operatorname{curl}A_j)_1
 +(\partial_1\chi_j)(A_j)_2
 -(\partial_2\chi_j)(A_j)_1.
$$

The second term is therefore part of the selected field calculation. No
theorem in this result sets it to zero.

## What this establishes

- the selected finite sum is a genuine Cartesian curl expression on the
  source-defined physical domain;
- the cutoff derivatives survive the curl operation;
- the remaining radial calculation has a concrete finite integrand rather
  than an unspecified infinite series.

## What remains open

This result does not yet prove any of the following:

- a Cartesian-to-cylindrical equality for the selected potential branch;
- a `torusAverage` or `barMoment` equality for that branch;
- a nonzero weighted remainder `Δm`;
- a contradiction with a selected invariant or `False`.

Those statements require an explicit radial transport theorem, including axis
and support-boundary terms. The present result is selected-path evidence for
that calculation, not the calculation's conclusion.

## Source anchors

| Item | Location |
|---|---|
| New theorem | `NavierStokesReview/src/completions/SelectedPotentialStagewiseCurlOnPhysicalDomain.lean:23-77` |
| Physical-domain openness | `NavierStokes/ActualCandidateConstruction.lean:190-193` |
| Per-stage smoothness | `NavierStokes/ActualCandidateAssembly.lean:879-886` |
| Finite stage-curl expansion | `NavierStokes/SolenoidalDiagonal.lean:257-270` |
| Selected commutator expansion | `NavierStokesReview/src/completions/SelectedCutStageCurlScope.lean:21-58` |

Build: `lake build NavierStokesReview` using Lean 4.34.0-rc2; 3,724 jobs
completed successfully.
