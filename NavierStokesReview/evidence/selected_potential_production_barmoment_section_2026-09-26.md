# Selected production: `barMoment` section bridge

**Date:** 2026-09-26
**Review tree:** `review/cmi-first-navier-stokes-2026-09-22`
**Evidence class:** Proven local transport; not a contradiction
**Lean file:** `NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean`

## Result

The positive-radius potential-production calculation now has an explicit
`ScalarField` representation on the point type consumed by `barMoment`:

$$
q=(R,(T,Z),Y)longmapsto
V_a\bigl(T,(R,Z)\bigr).
$$

The section is defined by `pointToCyl` and does not assert that every point of
the full lifted domain is the image of a physical Cartesian point.  This is
intentional: the source code provides a physical-point map but not a proved
global inverse for it.

## Source anchors

| Result | Location |
|---|---|
| `MomentPoint` type | `SelectedPotentialProductionBarMomentSection.lean:31` |
| Section coordinate map | `:33-34` |
| Scalar-field lift | `:36-38` |
| Pointwise unfolding | `:40-42` |
| Exact `barMoment` integral interface | `:45-49` |
| Positive radial physical-point compatibility | `:54-63` |
| Pullback to the radial production scalar | `:65-72` |
| Source `barMoment` definition/expansion | `NavierStokes/DefectIncrementBounds.lean:214-220` |
| Source physical-point equality | `NavierStokes/ActualMeanPotentialRealization.lean:331-358` |

## Verification

Command:

```text
cmd /c "C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean"
```

Result: exit code `0`; no `sorry`, custom axiom, or `unsafe` declaration was
added by this file.

## Boundary of the result

This closes a type and coordinate gate only. It does not prove:

- equality with the full mixed selected velocity;
- support or integrability for this lifted production scalar;
- interchange of `barMoment` with the selected infinite sum;
- a nonzero cutoff-shell value `Δm`;
- a contradiction with `FiveRows` or `False`.

Those remain the next selected-field obligations.
