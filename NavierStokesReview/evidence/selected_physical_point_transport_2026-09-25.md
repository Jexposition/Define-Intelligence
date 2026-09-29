# Selected physical-point transport record

Date: 2026-09-25

Status: `NOT ESTABLISHED AS A CMI SOLUTION`; no kernel contradiction has been
derived.

## Source anchors

| Component | Source location | What is actually defined |
|---|---|---|
| Physical chart point | `NavierStokes/ActualMeanPotentialRealization.lean:20-27` | `Point` is the chart lift and `chartPoint : SpaceTime → Point`. |
| Local chart regularity | `NavierStokes/ActualMeanPotentialRealization.lean:42-57` | Smoothness and radial-coordinate identities require a nonzero/positive radius. |
| Local curl transport | `NavierStokes/ActualMeanPotentialRealization.lean:113-190` | The component potential and its Cartesian curl are related on a valid cylindrical chart. |
| Global production stages | `NavierStokes/ActualCandidateAssembly.lean:1121-1137,1163-1177` | The witness exports Cartesian stage sums and a forcing predicate; it does not export a selected scalar radial profile. |
| Moment input | `NavierStokes/DefectIncrementBounds.lean:24-25,214-220` | `barMoment` consumes `ScalarField (Point P)` and evaluates a torus average followed by a radial integral. |
| Moment linearity | `NavierStokes/DefectIncrementBounds.lean:239-276` | Additivity, subtraction, scalar multiplication, and zero are proved for the supplied scalar families. |

## Review-side verification

`NavierStokesReview/src/completions/SelectedPhysicalPointTransport.lean`
compiles without `sorry`, `axiom`, or `unsafe`.

The completion records two facts:

1. the chart/lift domain can be related to the moment-domain aliases;
2. a `SelectedBarMomentTransportData` record is sufficient to expand the
   selected component into the exact `barMoment` integral.

It does not manufacture that record for the final post-curl, post-`tsum`
field. The missing load-bearing statement remains an equality of the form

$$
g_{\mathrm{selected}}(n,q)
= \bigl(u_{\mathrm{selected}}(\phi(q))\bigr)_i,
$$

with the required point-to-spacetime map, torus averaging, axis/outer-boundary
limits, and passage through the infinite sum. Without this equality, a
nonzero radial remainder `Δm` is not a theorem about the selected witness.

## Disposition

This result narrows the audit. It rejects the imprecise claim that the two
domains are simply unrelated, but confirms that the selected endpoint still
does not provide the scalar transport data required for a field-level
`barMoment` calculation. The result supports a publication-blocking
correspondence objection, not `False`.
