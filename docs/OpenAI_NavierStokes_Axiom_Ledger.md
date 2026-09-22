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
| AX-012 | Kernel extraction | `C:\Users\Admin\.elan\bin\elan.exe`; declared 4.34.0-rc2 cache; `#print axioms` | Cache retrieval completed, but the bounded target build did not emit `ComparatorSolution.olean`; exact transitive output remains pending | OPEN environment |
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

The isolated Lean 4.32 preflight is wired to that shared Mathlib path. Its
first run reported a stale compiled Lake configuration; the bounded `-R`
reconfiguration run did not return within 60 seconds. This is recorded as
`AUD-040` and is not used to classify the OpenAI theorem.

The formal-trust boundary is now recorded separately in
`NavierStokesReview/results/TRUST_AND_CMI_COMPLETION_CRITERIA_2026-09-22.md`.
It follows Lean's official guidance that `#print axioms` is transitive,
`sorryAx` is disqualifying for a completed proof, and repository metadata is
not an independent kernel certificate. This ledger therefore keeps the
transitive extraction pending until the target interface is available.

## Targeted extraction update: 2026-09-22

The repository's declared 4.34.0-rc2 cache retrieval restored 3,311 cached
Mathlib files successfully. A targeted build then exceeded 120 seconds and was
stopped without producing `NavierStokes.ComparatorSolution.olean`. No axiom
output is inferred from this partial build. The exact command and result are
recorded in `NavierStokesReview/results/BUILD_AND_AXIOM_EXTRACTION_LOG_2026-09-22.md`.

An independent probe was nevertheless run against the already-built analytic
comparison layer. `classical_uniqueness_on_Icc`, the pressure-flux closure,
pressure recovery, and the actual pressure-flux bound each report only
`propext`, `Classical.choice`, and `Quot.sound`. This is positive evidence for
that intermediate layer only; it is not substituted for the missing headline
export output. See
`NavierStokesReview/results/INTERMEDIATE_AXIOMS_4_34_RC2.txt`.

## Pressure-flux dependency update: 2026-09-22

The source-level pressure-flux route was traced through
`WholeSpaceComparisonClosure.eq_of_pressure_flux_bound`,
`PressureRecovery.gradient_recovery`, `ActualPressureFlux`, and
`PressureFlux.exists_uniform_actual_pressure_flux_bound`. The closure's flux
estimate is an explicit premise, but the uniqueness theorem derives it from
the comparison equations, divergence, smoothness, uniform finite energy, and
compact-candidate bounds. No new source-level axiom or circular agreement
assumption was found. The result is recorded in
`NavierStokesReview/results/PRESSURE_FLUX_AUDIT_2026-09-22.md` as `AUD-036`.

This does not settle the independent analytic validity of the imported proof
terms or their transitive kernel axiom set. The latter remains pending because
the targeted build did not emit `ComparatorSolution.olean`.

## Semantic coverage update: 2026-09-22

The source-level semantic pass found positive evidence for three previously
open obligations. `SmoothFamilyTorusInverse.inverse_finiteJets` fixes a
five-derivative inverse loss; `PhysicalResidualJetBounds` decomposes and bounds
the source, mean, base, Gaussian, alias, and excluded residual terms; and the
native residual path carries a derivative-order loss independently of the
correction index. These findings are recorded as `AUD-038` in the audit
tracker. They do not close common-domain coverage, premise provenance, or the
independent transitive axiom report. The endpoint path itself is source-level
verified through `OneSidedExtension`, joint-limit smoothness, and
`PhysicalJets.of_rawStage`; its transitive kernel and analytic provenance are
still pending.

The corrected probe invocation is now recorded in
`NavierStokesReview/results/AXIOM_PROBE_4_34_RC2.txt`. It was run from the
fork root and reached the real missing `ComparatorSolution.olean` interface;
the prior wrong-root module-prefix error is retained only as provenance. No
`#print axioms` output is asserted until the interface is emitted.
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

## JetRate specification finding: 2026-09-22

`DiagonalResidual.JetRate` is an eventual inequality over an arbitrary
`Filter D`. A zero-sorry independent probe proves that the proposition is
automatically true for the bottom filter, regardless of the function or its
iterated derivatives. This does not show that the selected candidate uses a
bottom filter, but it requires explicit nontrivial-domain evidence at each
load-bearing call site. The result is recorded as `AUD-046` with raw output
in `NavierStokesReview/results/JET_RATE_VACUITY_4_34_RC2.txt`.

## Pre-export kernel evidence: 2026-09-22

The direct R3 theorem, periodic paper theorem, and periodic comparator bridge
were independently probed under the declared 4.34.0-rc2 toolchain. All three
report only `propext`, `Classical.choice`, and `Quot.sound`. This is positive
evidence for the pre-export layer, not yet the final wrapper or Euler export
gate. Raw output is in
`NavierStokesReview/results/PREEXPORT_AXIOMS_4_34_RC2.txt` as `AUD-047`.

## Navier–Stokes headline kernel evidence: 2026-09-22

The independent headline probe now has a completed interface. The whole-space
and periodic Comparator exports, the underlying R3 theorem, and the periodic
corollary each report only `propext`, `Classical.choice`, and `Quot.sound`.
No `sorryAx`, native-evaluation axiom, or project-specific axiom appears in
these four reports. This closes the Navier–Stokes formal-trust row, but not
the CMI semantic or human-acceptance rows. Raw output is in
`NavierStokesReview/results/HEADLINE_AXIOMS_4_34_RC2.txt` as `AUD-048`.

## Euler headline kernel evidence: 2026-09-22

The independent Euler probe was run after the resumable direct closure supplied
the `Euler.Solution` interface. Both exported Euler declarations report only
`propext`, `Classical.choice`, and `Quot.sound`:

- `Euler.euler_breakdown_R3`;
- `Euler.exists_compact_smooth_euler_singularity`.

No `sorryAx`, native-evaluation axiom, or project-specific axiom appears in
the reports. The raw output is preserved in
`NavierStokesReview/results/EULER_AXIOMS_4_34_RC2.txt` as `AUD-050`. This
closes the repository's headline formal-trust inventory under the declared
toolchain; it does not close the CMI semantic or procedural gates.
