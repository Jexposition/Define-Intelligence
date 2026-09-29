# Source-path reconciliation: selected candidate and energy claims

**Date:** 2026-09-26
**Scope:** current worktree, excluding `.lake/` and `.git/` from the census.

## Result

No file named `SelectedCandidate.lean`, `selectedcandidate.lean`, or
`R3/SelectedCandidate.lean` exists in the current tree. A reachable-object
scan of Git history found no such Lean path either. The filename is therefore
a source-map error, not evidence that the selected candidate is absent.

The R3 source itself is present in two layers. Root-level wrapper modules
include `NavierStokes/R3.lean`, `NavierStokes/R3ActualCandidate.lean`,
`NavierStokes/R3CompactEnergy.lean`, `NavierStokes/R3PressureFourier.lean`,
`NavierStokes/R3EnergyNorms.lean`, and `NavierStokes/R3EnergyBoundary.lean`.
Detailed implementation modules live under `NavierStokes/R3/`, including
`ActualCandidate.lean`, `Theorem.lean`, `CompactEnergy.lean`,
`PressureRecovery.lean`, and `ActualPressureFlux.lean`. The earlier claim
that the root-level R3 files were absent was false and is corrected here.

The active path is:

| Role | Verified location |
|---|---|
| Selected existential witness | `NavierStokes/ActualCandidateAssembly.lean:1177` |
| Candidate projection | `NavierStokes/ActualCandidateAssembly.lean:1183` |
| Viscosity-one wrapper | `NavierStokes/R3/ActualCandidate.lean:127-151` |
| Exported theorem | `NavierStokes/R3/Theorem.lean:26-80` |
| Uniform finite-energy lemma | `NavierStokes/R3/CompactEnergy.lean:343` |

The named energy claims are present. `uniform_finite_energy` is used by the
viscosity-one candidate construction, and
`theorem_1_1_with_dissipation` is explicitly declared at
`NavierStokes/R3/Theorem.lean:66`. The audit must therefore not describe the
energy theorem as missing merely because a report cited the wrong filename.

## Current census

| Scope | Lean files | Lines |
|---|---:|---:|
| `NavierStokes/` | 817 | 381,843 |
| `NavierStokesReview/` | 123 | 5,855 |
| Whole worktree, excluding `.lake/` and `.git/` | 2,783 | 570,520 |

These counts are current-worktree measurements, not historical repository
metadata. Older counts such as 2,486 files or 618,762 lines must be labelled
with their snapshot and should not be presented as current.

## Axiom and `sorry` scope

The selected-witness probe reports only
`propext`, `Classical.choice`, and `Quot.sound`. A source census separately
finds four literal `sorry` declarations: two in
`ComparatorChallenges/NavierStokes.lean` and two in
`ComparatorChallenges/Euler.lean`. This supports the two-level statement:
the repository is not globally zero-sorry, while the inspected selected
endpoint is standard-axiom-only.

## Audit consequence

The filename discrepancy is corrected. The substantive review question is
unchanged: whether the exported selected path proves the paper’s advertised
field-level moment and provenance semantics. The existence of the correctly
located energy theorem does not supply that missing transport theorem.
