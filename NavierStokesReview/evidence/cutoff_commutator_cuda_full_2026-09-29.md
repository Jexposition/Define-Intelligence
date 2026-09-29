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
| gpu | 257 | 0.5 | 0 | 2.436725e-01 | 8.408886e-02 | 2.237490e+00 | 1.621095e-01 | 3.807986e-02 |
| gpu | 257 | 0.5 | 0.25 | 3.045907e-01 | 8.890116e-02 | 2.008164e+00 | 2.026369e-01 | 4.759983e-02 |
| gpu | 257 | 1 | 0 | 2.808829e-01 | 1.031033e-01 | 2.942155e+00 | 1.912876e-01 | 4.492827e-02 |
| gpu | 257 | 1 | 0.25 | 3.511036e-01 | 1.220209e-01 | 3.332699e+00 | 2.391095e-01 | 5.616034e-02 |
| gpu | 257 | 2 | 0 | 2.910521e-01 | 1.085587e-01 | 3.161525e+00 | 1.993672e-01 | 4.682447e-02 |
| gpu | 257 | 2 | 0.25 | 3.638152e-01 | 1.337361e-01 | 3.842317e+00 | 2.492090e-01 | 5.853058e-02 |

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
| 0.5 | 0 | `[129, 193, 257]` | `[-0.084082388, -0.084090101, -0.084088858]` | `[0.50017, 0.266077, 0.16211]` | `[6.908112, 3.674416, 2.23749]` |
| 0.5 | 0.25 | `[129, 193, 257]` | `[-0.088894316, -0.088902469, -0.088901155]` | `[0.625213, 0.332597, 0.202637]` | `[6.202113, 3.306805, 2.008164]` |
| 1 | 0 | `[129, 193, 257]` | `[-0.103095009, -0.103104861, -0.103103288]` | `[0.587646, 0.312773, 0.191288]` | `[9.034793, 4.811052, 2.942155]` |
| 1 | 0.25 | `[129, 193, 257]` | `[-0.122011058, -0.122022715, -0.122020853]` | `[0.734558, 0.390966, 0.23911]` | `[10.245211, 5.446836, 3.332699]` |
| 2 | 0 | `[129, 193, 257]` | `[-0.108549853, -0.108560333, -0.108558663]` | `[0.611804, 0.325672, 0.199367]` | `[9.706853, 5.169579, 3.161525]` |
| 2 | 0.25 | `[129, 193, 257]` | `[-0.133725272, -0.133738183, -0.133736125]` | `[0.764755, 0.40709, 0.249209]` | `[11.790543, 6.279285, 3.842317]` |

The current run records monotone decrease of both finite-difference
error sequences, but neither sequence is zero. This is a numerical
qualification, not a selected-field PDE certificate.

## Runtime and reproducibility

- Backend: `gpu`
- CUDA device: `NVIDIA GeForce RTX 4060 Ti`
- Resolutions: `[129, 193, 257]`
- Profile scales: `[0.5, 1.0, 2.0]`
- Modulations: `[0.0, 0.25]`
- Trusted derivative radius: `0.1` (axis-excluded validation mask; full 3D field remains plotted)
- Plot: `NavierStokesReview\evidence\cutoff_commutator_cuda_full_2026-09-29.png`
