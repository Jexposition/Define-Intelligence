# Selected radial-section component

## Result

`NavierStokesReview/src/completions/SelectedRadialSectionComponent.lean`
proves, for the actual `meanAngularField` construction and a cylindrical
point with positive radius `r`,

$$
\bigl(\operatorname{meanAngularField}(\operatorname{radialSection}(p))\bigr)_1
=\operatorname{meanField}(\operatorname{radialSection}(p)).
$$

This is a selected-field coordinate identity. It supplies an explicit scalar
profile along the positive radial section instead of treating the field as an
untyped vector placeholder.

The same file specialises the result to `selectedDirectStages` in
`selected_direct_stage_radial_component_one` (lines 38-53), using the actual
`ActualCandidateAssembly.directStages_eq` path through
`SelectedDirectPrefixField`.

## Axis boundary

The theorem requires `0 < p.2.1`. This is necessary in the source model:
`PhysicalMeanJetBounds.angularVector` uses a totalised division by the
Cartesian radius, and the source theorem `angularVector_axis` makes the frame
zero on the axis. Therefore the coefficient cannot be recovered from the
first component at `r = 0`. Any global radial transport theorem must add a
separate axis extension or boundary term.

## Source anchors

| Item | Location | Meaning |
|---|---|---|
| radial section | `NavierStokes/ActualMeanStageData.lean:23-38` | Embeds `(t,r,z)` as `(t,(r,0,z))` and proves the radius identity. |
| angular frame | `NavierStokes/PhysicalMeanJetBounds.lean:518-520` | Defines the Cartesian angular direction with totalised radius division. |
| axis value | `NavierStokes/DirectAngularDiagonal.lean:174-175` | Proves the angular field is zero on the spatial axis. |
| selected theorem | `NavierStokesReview/src/completions/SelectedRadialSectionComponent.lean:22-53` | Recovers the actual and selected scalar coefficient for positive radius. |

## Boundary of the result

This theorem does not identify the full mixed velocity with the scalar
`barMoment` input. The selected construction still contains the meridional
curl-generated contribution, cutoff commutators, torus averaging, and outer
support. No nonzero `Delta m` or `False` follows from this coordinate identity
alone.

## Build record

Command: `lake build NavierStokesReview` under Lean `v4.34.0-rc2`.

Result: `Build completed successfully (3700 jobs).`
