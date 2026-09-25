# Selected-field remainder trace

## Purpose

This record tests the proposed upgrade of CTR-005 from an exported-interface
objection to a kernel-level contradiction. The test is deliberately aimed at
the concrete selected field rather than at a generic `StageEstimates` record.

## Source path

| Layer | Source | Exact consequence |
|---|---|---|
| Stage sequence | `NavierStokes/ActualCandidateAssembly.lean:531-551,1165-1168` | `selectedPotentialStages` is `potentialStages`, whose stage zero is `initialPotential` and whose successors are `positivePotential`. |
| Stage field | `NavierStokes/ActualCandidateConstruction.lean:945-970` | A positive stage is `particular.field + signed.field + streamMeanStages`; the initial stage is `wave.field + streamMeanStages`. |
| Stage-to-chart map | `NavierStokes/ActualCandidateConstruction.lean:509-520,540-572` | Meridional and angular stage data are mapped into Cartesian chart fields under explicit positive-radius/domain hypotheses. |
| Infinite assembly | `NavierStokes/SolenoidalDiagonal.lean:31-42,46-75` | `potentialSum` is a `tsum` of cutoff stages; local positivity gives a finite prefix, but does not itself compute a profile integral. |
| Cartesian curl | `NavierStokes/ActualMeanPotentialRealization.lean:300-316,621-648` | Curl identities and finite cycle-prefix identities are proved for the chart realization. |
| Radial moment | `NavierStokes/DefectIncrementBounds.lean:214-220,239-249` | `barMoment` is a torus-averaged radial integral and is linear only under explicit scalar-field shell hypotheses. |
| Correction rows | `NavierStokes/FiveRowRank.lean:241-246` | The first two rows constrain correction profiles `dv` and `ga`; they are not declarations about the total selected Cartesian field. |

The finite-cycle recurrence is explicit at
`NavierStokes/ActualMeanPotentialRealization.lean:630-648`:
`meanIncrementComponents` is the sum of temporal and rank meridional
increments, and `meridionalComponents_iterate` expands a finite cycle state as
the seed plus a finite sum of those increments. This is a useful intermediate
formula, but the selected `potentialSum` adds independent spatial cutoffs and
then takes a `tsum`; the source trace still contains no theorem transporting
that cut-stage sum into `barMoment`.

## Result

The source establishes the Cartesian construction and the radial moment
operator separately. The inspected tree does not contain a theorem of the form

```text
barMoment k (selected Cartesian field) = selected five-moment expression
```

nor an equivalent theorem carrying the selected cut-stage `tsum` through the
Cartesian-to-cylindrical projection. Consequently, no exact selected nonzero
remainder has been proved in this audit. The missing equality is now a precise
calculation target, not a claim that the selected field is already known to
violate the rows.

## Required calculation before `False`

1. Instantiate the selected cutoff and profile expressions on an actual radial
   region.
2. Expand the spatial curl and retain derivatives of the cutoff masks.
3. Prove the axis and far-field boundary terms used by the projection.
4. Evaluate the finite prefix and the locally finite tail through `barMoment`.
5. Exhibit a nonzero remainder and combine it with the actual selected-field
   invariant in a zero-sorry Lean theorem.

`NavierStokesReview/tools/radial_profile_integrals.py` performs step 4 for
reviewer-supplied explicit profiles. It is not evidence for step 5 until a Lean
identity supplies those profiles from `selectedPotentialStages`.

## Classification

This is an open, load-bearing kernel-level falsification target. The current
publication-level result remains **NOT ESTABLISHED** because the advertised
five-moment mechanism is not transported to the selected exported field. A
selected-path `False` theorem has not been obtained from this trace.
