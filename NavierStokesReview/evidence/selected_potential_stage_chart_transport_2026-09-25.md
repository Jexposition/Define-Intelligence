# Selected potential-stage chart transport

**Date:** 2026-09-25
**Review tree:** `review/cmi-first-navier-stokes-2026-09-22`
**Result class:** selected-path evidence; not a contradiction

## Compiled result

`NavierStokesReview/src/completions/SelectedPotentialStageChartTransport.lean`
proves, for every selected stage `k`, valid chart index `i`, positive chart
radius parameter `a`, and admissible band `n`, that

```text
EqOn (SpatialCurl.spatialCurl (selectedPotentialStages k))
  (CyclePhysicalPrefixes.potentialParts ... k)
  (ActualPhysicalPrefixFields.cartesianChartDomain ...)
```

The theorem is `selected_potential_stage_curl_on_chart`. It obtains the result
from the selected instance of `ActualCandidateAssembly.stageRealizations`; it
does not introduce an axiom or an additional physical premise.

## Source anchors

| Location | Role |
|---|---|
| `NavierStokes/ActualCandidateAssembly.lean:531-533` | Definition of `potentialStages` |
| `NavierStokes/ActualCandidateAssembly.lean:911-938` | Initial potential curl chart realization |
| `NavierStokes/ActualCandidateAssembly.lean:1025-1056` | Positive potential curl chart realization |
| `NavierStokes/ActualCandidateAssembly.lean:1059-1082` | Combined `StageRealizations` record |
| `NavierStokes/ActualCandidateAssembly.lean:1165-1168` | Selected potential-stage alias |
| `NavierStokes/ActualPhysicalPrefixFields.lean:342-356` | Meaning of the potential realization field |
| `NavierStokesReview/src/completions/SelectedPotentialStageChartTransport.lean:21-44` | Review-side selected theorem |

## What this establishes

The selected potential branch is not merely an abstract stage family on the
valid chart domain. Its spatial curl has the concrete chart representation used
by the physical-prefix construction. This closes one local field-equality step
in the Cartesian-to-radial route.

## What remains open

The result does not prove that the chart potential part is the scalar input to
`DefectIncrementBounds.barMoment`, does not evaluate the torus average, and
does not establish a nonzero cutoff-shell or boundary contribution. Therefore
it supplies no `Delta m != 0` and no `False`.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

Result: `Build completed successfully (3704 jobs).` The new module contains no
`sorry`, custom `axiom`, or `unsafe` declaration.
