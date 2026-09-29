# Selected potential production radial scalar

**Date:** 2026-09-25
**Review tree:** `review/cmi-first-navier-stokes-2026-09-22`
**Classification:** selected transport identity; no contradiction

## Result

The zero-sorry completion
`NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean`
defines the first Cartesian component of the selected localised potential
production field on the source radial section. It proves, for the selected
schedule and every radial point satisfying the stated physical-domain and
unit-cube hypotheses,

$$
V_{\mathrm{prod},1}=
\chi\,\bigl(\operatorname{curl}A\bigr)_1
 +\bigl(\operatorname{curlLinear}(D\chi\,A)\bigr)_1.
$$

The differentiability premise is derived from the source `physicalDomain`,
`stages_smooth`, `potentialSum_contDiffOn`, and the selected schedule's
`Tendsto` component. The theorem therefore does not assume smoothness as an
opaque endpoint fact on the selected physical domain.

## Source anchors

| Item | Location |
|---|---|
| Radial section | `NavierStokes/ActualMeanStageData.lean:23-24` |
| Physical domain and openness | `NavierStokes/ActualCandidateConstruction.lean:189-192` |
| Potential-sum smoothness | `NavierStokes/SolenoidalDiagonal.lean:122-128` |
| Localised product rule | `NavierStokes/SpatialLocalization.lean:200-207` |
| Selected scalar definition | `SelectedPotentialProductionRadialScalar.lean:28-31` |
| Derived differentiability | `SelectedPotentialProductionRadialScalar.lean:33-81` |
| Radial scalar identity | `SelectedPotentialProductionRadialScalar.lean:83-105` |
| Selected schedule transport | `SelectedPotentialProductionRadialScalar.lean:107-136` |

## Verification

Command:

```text
cmd /c "C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean"
```

Result: exit code `0`; no `sorry`, custom axiom, or `unsafe` declaration was
added by this completion.

## Boundary of the result

This theorem does not yet supply the point-to-spacetime map required to feed
the selected production scalar into `PressureStream.torusAverage` on the full
`barMoment` domain. It also does not prove that the commutator has a nonzero
weighted radial integral. The status therefore remains **NOT ESTABLISHED**, not
`False`.
