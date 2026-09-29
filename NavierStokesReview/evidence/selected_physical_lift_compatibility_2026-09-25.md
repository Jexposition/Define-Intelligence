# Selected physical-lift compatibility

**Date:** 2026-09-25
**Claim class:** source-backed local compatibility; not a contradiction
**Review target:** CTR-005, CALC-22, CALC-25

## Result

The source contains a real positive-radius coordinate bridge. The lifted point
used by the mean data is definitionally the same product as the lifted point
used by the slow-coordinate residual layer:

$$
\mathrm{PhysicalResidualTZ.Lift}
  = \mathbb R\times(\mathrm{Plane}\times\mathrm{Plane})
  = \mathrm{PressureStream.Lift}\;\mathrm{PhysicalGraphBounds.Plane}.
$$

For a spacetime point `z` with positive radial coordinate,
`ActualMeanPotentialRealization.physicalPoint_forward` proves

```text
PhysicalMeanJetBounds.physicalPoint h
  (z.1, CylindricalResidual.chart z.2)
= PhysicalResidualTZ.absoluteLiftTZ h z.
```

`ActualCandidateAssembly.stageRealizations` separately transports each selected
potential-stage curl to the source chart field.

## Boundary of the result

These are a type compatibility and a stagewise chart identity. They do not
construct the scalar family required by
`DefectIncrementBounds.barMoment` from the final localised potential `tsum`.
The following remain unproved for the selected endpoint:

1. a global point-to-spacetime or scalar representative for the full averaging
   domain;
2. transport of the cutoff-gradient commutator;
3. axis, outer-support, and integrability limits;
4. passage from the local finite-prefix identities to the selected `tsum`;
5. an exact weighted value, nonzero remainder, or contradiction.

## Source anchors

| Fact | Source |
|---|---|
| `PhysicalResidualTZ.Lift` alias | `NavierStokes/PhysicalResidualTZ.lean:19-21` |
| `PressureStream.Lift` alias | `NavierStokes/PressureStream.lean:25-26` |
| Positive-radius forward equality | `NavierStokes/ActualMeanPotentialRealization.lean:331-358` |
| Stagewise chart transport | `NavierStokes/ActualCandidateAssembly.lean:1059-1088` |
| `barMoment` input and expansion | `NavierStokes/DefectIncrementBounds.lean:214-220` |

## Verification

The result was checked by direct source inspection. No Lean theorem in this
entry claims a selected nonzero integral or `False`; the evidence is therefore
classified as a completed local bridge and an open endpoint calculation.
