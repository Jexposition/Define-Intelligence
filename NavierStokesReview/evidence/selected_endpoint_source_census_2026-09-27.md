# Selected-endpoint source census (2026-09-27)

This report is generated from every current Lean file under `NavierStokes/`.
It is lexical source evidence for audit triage, not a proof of theorem transport.
No surrogate profile, numerical field, cutoff, or radial integral is used.

- Full source files: **817**
- Full source lines: **429297**
- Full source bytes: **23259568**
- Local modules reachable from the two endpoint roots: **588**
- Active source lines: **380791**
- Missing local imports in the closure: **0**
- External import roots not present in this repository: **209**
- Parsed declarations: **35430** total, **31882** active
- Lexical moment/endpoint declaration candidates: **7** active

## Active lexical bridge candidates

These rows identify declaration blocks containing both a moment/debt symbol and an endpoint/field/rate symbol. They are triage targets, not transport proofs.

| File | Line | Declaration | Symbols |
| --- | ---: | --- | --- |
| `NavierStokes/ActualPhysicalStageBounds.lean` | 595 | `initialDirect_rate` | `JetRate, NominalProfile` |
| `NavierStokes/ActualPhysicalStageBounds.lean` | 726 | `background_from_representations` | `JetRate, NominalProfile, VelocityField` |
| `NavierStokes/GermCandidateAssembly.lean` | 75 | `potentialSum_eq_base_germ` | `NominalProfile, VelocityField, potentialSum` |
| `NavierStokes/InitializedPhysicalBackground.lean` | 93 | `directIncrement_rate` | `JetRate, NominalProfile` |
| `NavierStokes/MixedAxisPreservation.lean` | 470 | `origin_blowup_global` | `NominalProfile, VelocityField` |
| `NavierStokes/MixedCandidateAssembly.lean` | 67 | `StageEstimates.exists_schedule` | `NominalProfile, StageEstimates, VanishingJointJets, VelocityField` |
| `NavierStokes/MixedCandidateWitness.lean` | 25 | `SelectedSchedule` | `NominalProfile, VanishingJointJets, VelocityField` |

## Interpretation boundary

A lexical co-occurrence is not a theorem-level equality. The selected-field transport question remains open until the exact declaration body proves the composition through sums, curl, localisation, periodisation, radial averaging, and the axis route.
