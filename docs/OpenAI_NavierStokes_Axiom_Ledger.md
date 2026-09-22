# OpenAI Navier–Stokes Lean Axiom Ledger

Status: initial census; all dependency claims remain pending kernel extraction unless marked confirmed.

| ID | Item | Location or command | Classification | Status |
|---|---|---|---|---|
| AX-001 | `#print axioms` commands for whole-space adapters | `NavierStokes/ComparatorSolution.lean:31-32` | Measurement hook, not an axiom | CONFIRMED |
| AX-002 | `sorry` in Comparator challenge files | `ComparatorChallenges/NavierStokes.lean`, `ComparatorChallenges/Euler.lean` | Intentional challenge placeholders; test whether reachable from exported theorem | CONFIRMED lexical hits; dependency OPEN |
| AX-003 | `axiom` declarations in main source | Repository-wide lexical search | No declaration-level `axiom` was found in the reviewed main result path; comments and text still require classification | CONFIRMED source-level |
| AX-004 | `sorryAx` in exported theorem dependencies | Lean `#print axioms <name>` under pinned build | Disqualifying if it supports the mathematical conclusion | PENDING |
| AX-005 | `Classical.choice`, `propext`, `Quot.sound` | Lean axiom output | Foundation-level logical/classical dependencies; not automatically a mathematical gap | PENDING |
| AX-006 | Opaque or noncomputable definitions | Source search for `opaque`, `noncomputable` | Review interface theorem and construction, not the keyword alone | PENDING |
| AX-007 | Imported mathlib/Comparator declarations | `lake-manifest.json`, import graph | Dependency provenance and version pin | PENDING |
| AX-008 | Trusted compiler/kernel boundary | Lean version, Lake version, cache origin | Reproducibility condition | PENDING |
| AX-009 | Selected witness construction | `NavierStokes/ActualCandidateAssembly.lean`, `GermCandidateAssembly.lean` | Derived from finite-stage estimates and an existence theorem; not a source-level axiom | CONFIRMED source-level |
| AX-010 | A-posteriori force | `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` | Existentially produced after candidate fields and residual data; audit its CMI force class separately | CONFIRMED interpretation |
| AX-011 | Challenge placeholders | `ComparatorChallenges/NavierStokes.lean`, `ComparatorChallenges/Euler.lean` | Four intentional `sorry` lines in separate challenge files; reachability to exported results is OPEN | CONFIRMED lexical |
| AX-012 | Kernel extraction | `elan`, `lake`, and `#print axioms` | No `elan` or `lake` executable is currently on this shell's PATH; exact transitive output remains pending | OPEN environment |
| AX-013 | Supplied-report axiom protocol | Technical audit report and backup audit | Adopted: transitive footprint must be measured, not inferred from `sorry_count` | CONFIRMED protocol |
| AX-014 | Input corpus provenance | `NavierStokesReview/evidence/input_documents_manifest.json` | Technical report, four backup documents, paper, ZIP, root critiques, and fork review docs are hash-recorded | CONFIRMED |

## Rules

- A lexical occurrence is not evidence of an axiom dependency. Comments, documentation, `#print axioms`, and challenge placeholders must be classified separately.
- A theorem is not treated as independent merely because its source file contains no `sorry`; its transitive axiom set is required.
- `Classical.choice`, `propext`, and quotient extensionality are recorded transparently but are not equivalent to assuming the Navier–Stokes construction.
- Any `sorryAx` reachable from a main exported theorem is a high-severity finding and must be reproduced from a clean build.

## Required captures

```text
#print axioms NavierStokesR3.theorem_1_1
#print axioms NavierStokesR3.breakdownStatement
#print axioms NavierStokes.Comparator.navier_stokes_breakdown_R3
#print axioms NavierStokes.Comparator.navier_stokes_breakdown_periodic
```

The exact qualified names may change between the downloaded snapshot and the public commit; record the compiler’s resolution rather than guessing a name.

The supplied technical audit report is explicitly incorporated. Its claims
about other Astra proofs are not imported into this ledger unless the current
Navier–Stokes exported declarations depend on those files. Its Navier–Stokes
tests remain active: challenge-file reachability, CMI predicate matching,
scaling guards, and independent kernel output.

## Current extraction state: 2026-09-22

`elan` is installed at `C:\Users\Admin\.elan\bin`, and the repository-declared `leanprover/lean4:v4.34.0-rc2` toolchain is installed. The broad all-project build was stopped because compilation is not the review criterion. A targeted `NavierStokes.ComparatorSolution` dependency build was attempted and stopped before emitting the target interface needed by the independent probe. No transitive axiom set is asserted here until the probe captures compiler output for each exported declaration, including whether `sorryAx` is reachable.

## Source audit update: 2026-09-22

The finite-stage path was inspected through `StateRealization`, `PhysicalFields`, `ActualCycleResidualBounds.Invariant.residual_jetRate`, `GluedStageEstimates.actualStageEstimates`, and `ActualCandidateAssembly.estimates`. The source-level result is that the residual-rate input is derived from explicit physical germ, exterior, invariant, and representation premises. No declaration-level `axiom` or `sorry` was found in this path. The independent kernel footprint remains pending because the target `.olean` interface was not produced.

`DiagonalResidual.JetRate` is separately logged as a specification concern: it is a bound on `iteratedFDeriv` and does not bundle smoothness. This does not currently contaminate the final candidate path because `StageEstimates` separately requires `ContDiffOn` for each raw field, but every consumer that uses a rate as a regularity statement must be checked.

The requested shared package root at `D:\Research Lab\V-lab-Equipment\.lake\packages-4.32` contains `mathlib` but no `Comparator` package. It is therefore not the dependency tree for this fork's declared 4.34.0-rc2 project and is tracked as a compatibility lane rather than substituted into the main audit.
# Current-snapshot update: 2026-09-22

## Source-level dependency inventory

- Lean version declared by the public repository: `leanprover/lean4:v4.34.0-rc2`.
- Main exported declarations named by `formalization.yaml`:
  - `NavierStokes.Comparator.navier_stokes_breakdown_R3`;
  - `NavierStokes.Comparator.navier_stokes_breakdown_periodic`;
  - `Euler.euler_breakdown_R3`;
  - `Euler.exists_compact_smooth_euler_singularity`.
- The repository itself includes four `#print axioms` commands for these declarations, but those outputs must be independently captured rather than trusted from YAML metadata.

## Lexical findings requiring classification

The project-only census excludes `.lake` dependencies and reports four actual `sorry` declarations, all in:

- `ComparatorChallenges/NavierStokes.lean` at lines 277 and 284;
- `ComparatorChallenges/Euler.lean` at lines 88 and 184;
- comments and metadata are excluded from the declaration count.

These challenge files are not assumed to be imported by the exported result path. The review will verify this with the import graph and kernel output. Raw occurrences of `axiom`, `opaque`, and `noncomputable` are not automatically axioms: each must be classified by declaration syntax and, where relevant, by `#print axioms`.

## Independence rule

`formalization.yaml` is project metadata and is marked self-assessed. It is useful provenance, not an independent certificate. The review ledger therefore treats the official Git commit, compiler invocation, exact theorem statements, source imports, and kernel output as the load-bearing evidence.
