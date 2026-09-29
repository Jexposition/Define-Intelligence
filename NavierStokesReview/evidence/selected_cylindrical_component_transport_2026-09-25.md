# Selected Cartesian component transport

## Result

The review completion
`NavierStokesReview/src/completions/SelectedCylindricalComponentTransport.lean`
compiles without `sorry`, custom axioms, or `unsafe` declarations.

It proves, on the valid positive-radius polar chart,

$$
\bigl(\operatorname{frame}(\theta)v\bigr)_1
 = \sin(\theta)v_0+\cos(\theta)v_1,
$$

and transports that identity through the source theorem
`CyclePhysicalPrefixes.velocity_polar_forward`:

$$
\bigl(\operatorname{velocity}(z)\bigr)_1
 = \sin(z_1)\,\operatorname{cylindricalVelocity}(z)_0
   +\cos(z_1)\,\operatorname{cylindricalVelocity}(z)_1.
$$

## Source anchors

- `NavierStokes/CylindricalResidual.lean:42-50` defines and expands `frame`.
- `NavierStokes/CyclePhysicalPrefixes.lean:150-200` defines
  `polarVelocityMap` and proves `velocity_polar_forward`.
- `NavierStokesReview/src/completions/SelectedCylindricalComponentTransport.lean:19-37`
  contains the review theorems.

## Interpretation

This is selected chart-field evidence. It identifies the Cartesian component
used by the radial gate as a rotated combination of cylindrical components.
It does not establish a global torus average, a `barMoment` identity for the
selected mixed field, a nonzero cutoff-shell contribution, `Delta m ≠ 0`, or
`False`.

## Build

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
Build completed successfully (3705 jobs).
```
