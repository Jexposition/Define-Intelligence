# Deep 3D Cartesian curl/cutoff calculation

This is a CUDA-first 3D reconstruction of the exact cutoff shape in
`SpatialLocalization.spatialCutoff`, followed by `curl(c*A)` on a
nonseparable axisymmetric stream. It is not the selected Lean tsum.

## Source bindings

- `SpatialLocalization.lean:41-53`: exact squared-radius/axial cutoff.
- `SpatialLocalization.lean:165-171`: cutoff potential and curl field.
- `SpatialLocalization.lean:200-208`: product-rule commutator.
- `SpatialLocalization.lean:210-214`: periodised potential route.
- `ActualPrimaryCoherence.lean:1633-1871`: physical potential and Cartesian lift.

## Finest-resolution summaries

| backend | points | scale | modulation | defect L∞ | defect L1 | divergence L∞ | Cartesian curl error L∞ | product-rule error |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| gpu | 321 | 1 | 0 | 2.808831e-01 | 1.031034e-01 | 1.999935e+00 | 1.298283e-01 | 3.039445e-02 |

## Interpretation boundary

A stable nonzero defect in this exact-cutoff 3D diagnostic establishes
a numerical mechanism for moment alteration in the explicit profile.
It does not establish selected `Delta m != 0`: the selected field still
requires binding its actual potential sums, periodisation, `torusAverage`,
`barMoment`, and axis route.

## Numerical qualification

The refinement audit treats the defect estimate and derivative checks
as separate quantities. A stable defect with decreasing finite-difference
errors is evidence of a resolved diagnostic profile, not an exact PDE
identity. The finite-difference errors are reported explicitly and are
not required to be zero in this numerical instrument.

| scale | modulation | resolutions | signed defect sequence | curl-error sequence | divergence-error sequence |
|---:|---:|---|---|---|---|
| 1 | 0 | `[129, 193, 257, 321]` | `[-0.103095009, -0.103104861, -0.103103288, -0.103103358]` | `[0.587646, 0.312773, 0.191288, 0.129828]` | `[9.034793, 4.811052, 2.942155, 1.999935]` |

The current run records monotone decrease of both finite-difference
error sequences, but neither sequence is zero. This is a numerical
qualification, not a selected-field PDE certificate.

## Runtime and reproducibility

- Backend: `gpu`
- CUDA device: `NVIDIA GeForce RTX 4060 Ti`
- Resolutions: `[129, 193, 257, 321]`
- Profile scales: `[1.0]`
- Modulations: `[0.0]`
- Trusted derivative radius: `0.1` (axis-excluded validation mask; full 3D field remains plotted)
- Plot: `None`
