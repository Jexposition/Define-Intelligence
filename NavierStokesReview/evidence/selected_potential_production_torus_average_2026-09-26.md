# Evidence record: finite-prefix torus-average reduction

**Date:** 2026-09-26
**Scope:** selected finite-prefix review construction
**Status:** verified local identity; no selected-field contradiction

## Source and verification

The result is implemented in
`NavierStokesReview/src/completions/SelectedPotentialProductionTorusAverage.lean`.
It imports the finite-prefix construction from
`SelectedPotentialProductionFinitePrefix.lean` and uses the repository
definitions `PressureStream.torusAverage`, `PressureStream.torusInner`, and
`DefectIncrementBounds.barMoment`.

The focused check and the full review-library build both completed with exit
code `0`:

```text
cmd /c "C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedPotentialProductionTorusAverage.lean"
cmd /c "C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview"
```

The full build reported `Built ... (3732 jobs)`. The new file contains no
`sorry`, custom `axiom`, or `unsafe` declaration.

## What is proved

For the lifted finite-prefix scalar used by this review construction, the
sampling map `pointToCyl` ignores the auxiliary `Plane` coordinate. Therefore
the two interval integrals in the torus average reduce definitionally to one
sample:

$$
\operatorname{torusAverage}(F_{a,N,n})(r,p)
=F_{a,N,n}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr).
$$

The exact weighted radial reduction is then:

$$
\operatorname{barMoment}_k(F_{a,N})(n,p)
=\int_{\mathbb R} r^k\,
V_{a,N}\bigl(\operatorname{pointToCyl}(r,(p,(0,0)))\bigr)\,dr.
$$

The theorem names are:

| Theorem | File location | Meaning |
|---|---|---|
| `torusAverage_selected_potential_partial_production` | `SelectedPotentialProductionTorusAverage.lean:22-29` | exact finite-prefix torus-average reduction |
| `finite_prefix_barMoment_radial_reduction` | `SelectedPotentialProductionTorusAverage.lean:31-40` | exact `barMoment` radial-integral reduction |

## Limitation

This is a theorem about the explicitly constructed finite-prefix lifted scalar.
It does not identify that scalar with the complete mixed Cartesian velocity
field exported by `selected_witness`. In particular, it does not prove:

- the value or sign of the remaining radial integral;
- vanishing or non-vanishing axis and outer-boundary contributions;
- passage from finite prefixes to the selected infinite `tsum`;
- equality with the five-row invariant at the selected endpoint;
- `\Delta m \ne 0`; or
- a kernel contradiction `False`.

The result therefore strengthens the selected-field calculation lane but does
not, by itself, falsify the published theorem. The publication verdict stays
**NOT ESTABLISHED** until the full selected-field transport is proved or a
zero-sorry contradiction is derived.

## Related source fact: axis scale

The source also contains an exact axis-coordinate result in
`NavierStokes/AxisPreservation.lean:130-148`:

$$
\operatorname{physicalQ}(h,(t,0))=1-t,
\qquad
\operatorname{physicalQ}(h,(t,0))\to0\quad(t\to1^-).
$$

This uses the defining `coordinateQ` equation at axial coordinate zero and
continuity. It closes the scale-coordinate premise, but it does not evaluate
the selected Cartesian `tsum` on the axis or its contribution to `barMoment`.
