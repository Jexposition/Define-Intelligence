# OpenAI Navier–Stokes Lean Review: CMI-First Plan

Status: review scaffold created 2026-09-22. No final mathematical verdict has been issued.

## 1. Review question

Does the public Lean development prove one of the four statements in the Clay Mathematics Institute (CMI) problem specification, or does it only prove a related finite-time or forced construction? The review will keep three questions separate:

1. Does the code elaborate and kernel-check under a pinned Lean/toolchain/dependency snapshot?
2. What proposition is actually proved, including all quantifiers, domains, regularity, support, viscosity, and energy clauses?
3. Does that proposition imply CMI alternative (C) or (D) without an unproved bridge, hidden axiom, `sorryAx`, or semantic mismatch?

The local downloaded extraction is never edited. In this fork branch, the public review checkout is the repository root, pinned to public commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`; review harnesses remain under `NavierStokesReview/src/`.

## 2. CMI acceptance criteria

The official statement defines the incompressible Navier–Stokes system on `R^3` or periodic `R^3/Z^3`, with `nu > 0`, smooth divergence-free initial data, smooth external forcing, the PDE, the initial condition, and physically reasonable solutions. For whole space, the accepted solution class requires `p,u` smooth for all `t >= 0` and uniformly bounded kinetic energy. The CMI alternatives are:

- **(A)** global smooth bounded-energy solution on `R^3` for every admissible datum with `f = 0`;
- **(B)** the periodic analogue with `f = 0`;
- **(C)** an admissible whole-space datum and force for which no such global solution exists;
- **(D)** the periodic analogue.

The CMI document explicitly permits an external force in the problem statement. Therefore, “the construction is forced” is not by itself a CMI failure. The decisive checks are whether the force has the required smoothness/decay or periodicity, whether the prescribed data meet the conditions, and whether the nonexistence conclusion is for the exact CMI solution class.

Primary reference: [Fefferman, official CMI problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf), especially equations (1)–(11) and alternatives (A)–(D).

### CMI prize-procedure gate

The mathematical statement and the prize procedure are separate tests. CMI's current rules require qualifying publication, at least two years since publication, and general acceptance in the global mathematics community before CMI considers a proposed solution. CMI does not accept direct unsolicited submissions. Its 11 September 2026 announcement describes the Navier–Stokes claim as apparently settled and says the work is being analysed; it is not a prize determination.

Primary procedural references: [CMI rules](https://www.claymath.org/millennium-problems/rules/) and [CMI Navier–Stokes announcement](https://www.claymath.org/news/navier-stokes-announcement/).

## 3. Current source map

| Layer | Current public path | Review purpose |
|---|---|---|
| Entry point | `NavierStokes.lean` | Imports `ComparatorSolution` and `PaperResults`. |
| CMI adapter | `NavierStokes/ComparatorSolution.lean` | Exposes theorem names for C and D. |
| Whole-space target | `NavierStokes/R3/ProblemStatement.lean` | Defines `CandidateProperties`, `candidateStatement`, and `breakdownStatement`. |
| Main whole-space theorem | `NavierStokes/R3/Theorem.lean:26-62` | Claims the selected construction for every positive viscosity. |
| Candidate witness | `NavierStokes/R3/ActualCandidate.lean` | Supplies the selected fields and properties. |
| CMI bridge | `NavierStokes/R3/ComparatorBridge.lean:22-88` | Converts compact support and a global comparator solution into the contradiction. |
| Periodic route | `NavierStokes/PeriodicPaperTheorem.lean` and `NavierStokes/PeriodicPaperComparator.lean` | Separate C/D periodic construction and bridge. |
| Challenge stubs | `ComparatorChallenges/*.lean` | Independent Comparator benchmark files; intentional `sorry` placeholders must not be confused with the main theorem dependency. |

The local extraction dated 2026-09-08 has 2,486 Lean files and imports only `NavierStokes.ComparatorSolution` at its top-level entry point. The public checkout dated 2026-09-10 has 2,659 Lean files and imports `NavierStokes.PaperResults` as well. All conclusions must identify which tree they concern.

## 4. Review workflow

1. **Freeze provenance.** Record source path, public URL, commit, file counts, SHA-256 hashes for manifests and theorem files, and whether the local zip matches the extracted tree.
2. **Reproduce builds.** Inventory the requested Lean 4.32 environment using `D:\Research Lab\V-lab-Equipment\.lake\packages-4.32`, then separately test the repository-declared Lean 4.34.0-rc2 environment. The 4.32 cache currently contains `mathlib` but no `Comparator`, while this repository declares matching 4.34.0-rc2 revisions. Do not call that incompatibility a source failure.
3. **Kernel and axiom audit.** Build the main targets, collect `#print axioms` for every exported theorem, and search for `sorry`, `admit`, `axiom`, `opaque`, `unsafe`, and imported declarations that introduce `sorryAx`.
4. **Statement audit.** Expand every definition in the CMI path and produce a quantifier/domain table. Check viscosity scaling, time domain, initial condition, spatial decay/support, periodicity, pressure sign, Laplacian, divergence, and energy quantifiers.
5. **Bridge audit.** Trace the exact dependency chain from the selected witness to `ComparatorSolution`. Check that each conversion preserves the same `nu`, `u0`, `f`, PDE convention, smoothness domain, and energy bound.
6. **Mathematical stress tests.** Target the highest-risk lemmas: compact support to CMI force decay, local pre-singular fields to a global nonexistence statement, uniqueness/continuation assumptions, viscosity rescaling, endpoint regularity, and any use of integrability or measure-theoretic coercion.
7. **Independent reproduction.** Run the public build and Comparator instructions from a clean review checkout. Compare outputs against the pinned manifests and record exact commands and failures.
8. **Verdict discipline.** Use `CONFIRMED`, `PENDING`, `OPEN`, or `NOT_TESTED_THOROUGHLY`. A negative verdict requires a concrete countermodel, failed kernel check, invalid implication, or an explicit CMI criterion not met. Numerical scans and textual suspicions are evidence for a test, not a verdict.

## 5. Highest-value potential failure modes

- **Statement weakening:** proving blow-up only on `0 <= t < 1` without proving that no global solution in the CMI class exists for the same data and force.
- **Bridge mismatch:** a comparator solution uses a different force, pressure sign, viscosity, initial datum, or time convention than the candidate theorem.
- **Support/decay mismatch:** compactness is only spatial, only temporal, or established for a transformed field rather than the exact force in CMI (5)/(9).
- **Regularity boundary:** `ContDiffOn` on a pre-singular domain is used as if it supplied the all-time regularity required of a hypothetical global comparator solution, or differentiability at the endpoint is silently used.
- **Scaling error:** the positive-viscosity rescaling changes the force or energy class in a way not covered by the stated lemmas.
- **Axiom contamination:** the exported theorem depends on `sorryAx`, an unreviewed axiom, or an opaque declaration whose semantic content is stronger than its proved interface.
- **Environment drift:** the downloaded snapshot and public `main` differ, or the proof only builds under a different Lean/mathlib revision than the one being audited.

## 6. Evidence policy

Each finding must contain: source snapshot, exact file and line, proposition or declaration, command used, observed output, CMI criterion affected, severity, and a proposed reproduction. No source file under `NavierStokesAndEuler-main-open Ais solution` will be modified. Review code and scripts belong under `NavierStokesReview/src/audit/`.

## 7. Immediate next actions

1. Complete the 4.32 harness and a separate 4.34 repository build.
2. Capture `#print axioms` for `NavierStokesR3.theorem_1_1`, `NavierStokesR3.breakdownStatement`, periodic theorem exports, and the public Comparator adapters.
3. Fill the first CMI quantifier table from `R3/ProblemStatement.lean` and `PeriodicPaperTheorem.lean`.
4. Reconcile the existing critique notes with source-backed findings in the audit tracker.

## 8. Source-draft disposition

The supplied drafts were read as review hypotheses, not as established findings. Their useful claims are converted into tests below.

| Draft claim | Source-backed disposition | Review treatment |
|---|---|---|
| A forced construction cannot satisfy CMI | Incorrect as a general objection. CMI alternatives (C) and (D) explicitly include smooth forcing. | Test the exact force class, domain, decay, and quantifiers instead. |
| The force is chosen a posteriori from the residual | Substantively accurate as a construction description: the main candidate witness existentially produces `forcing` after the candidate fields and residual estimates. | Treat as an interpretation/relevance concern, not a CMI failure unless the force class or quantifiers fail. |
| Hyperviscosity or Ladyzhenskaya viscosity destroys the construction | This changes the PDE. It does not refute a theorem about the classical Newtonian `nu * Delta u` equation. | Keep as a robustness/physical-model question; do not use it as a counterexample to the stated CMI problem. |
| The main result contains `sorry` or an assumed blowup axiom | Current lexical scan finds four intentional `sorry` lines in two challenge files and no source-level `axiom` declaration in the main result tree. | Require transitive `#print axioms` and declaration-graph evidence before any conclusion. |
| Lean compilation establishes the mathematical claim | Incorrect standard. Compilation only shows elaboration and kernel acceptance under a toolchain. | Use compilation only to obtain reproducible theorem and axiom evidence; perform the CMI and PDE audit separately. |
| The candidate is merely an interface carrying the desired properties | Not established. `ActualCandidateAssembly.selected_witness` is obtained from `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`, using `StageEstimates`, support, endpoint, cone, and residual inputs. | Audit those finite-stage estimates and their dependencies line by line. |

## 9. Current load-bearing proof path

The R3 route currently reads as:

`ActualCandidateAssembly.selected_witness`
→ `R3.ActualCandidate.of_localized_fields`
→ `R3.Theorem.theorem_1_1_with_initial_rest`
→ `WholeSpaceUniqueness.candidate_global_agrees_before_one`
→ `CandidateBreakdown.no_global_solution_one`
→ `ComparatorR3Bridge.comparator_of_breakdown`
→ exported Comparator theorem.

The uniqueness bridge is materially stronger than a simple boundedness lemma. It invokes `PressureRecovery`, `PressureFlux`, `CompactComparisonBounds`, and `WholeSpaceComparisonClosure` to compare a compact candidate with an arbitrary smooth finite-energy competitor. The audit must therefore inspect those analytic interfaces and their exact hypotheses, not only the final theorem signature.

The finite-stage construction is also load-bearing. The selected witness uses a proved `StageEstimates` object and a theorem named `exists_candidate_witness_of_finite_stages`; this is not, by itself, an axiom or a `sorry`, but the contents and dependency graph of those estimates determine whether the advertised smooth residual and blowup properties are genuinely derived.
# Snapshot update: 2026-09-22

The review now distinguishes three artefacts that must not be conflated:

1. the downloaded, non-Git checkout at `NavierStokesAndEuler-main-open Ais solution`;
2. the current public clone at the repository root of this fork branch, pinned to commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`;
3. the independent review workspace under `NavierStokesReview`, which contains the census, probes, logs, and reports.

The current clone contains 2,659 project Lean files and 173 project files not present in the downloaded copy. The downloaded ZIP and current fork share 2,493 comparable text/source entries: 2,478 are identical after line-ending normalisation and 15 changed. The machine-readable comparison is `NavierStokesReview/evidence/download_snapshot_comparison.json`; the local checkout must still be pinned to the public commit for current conclusions.

The public CMI question is not rejected merely because the construction uses forcing. The official CMI statement explicitly permits smooth forcing in alternatives C and D. The decisive audit therefore remains: do the exported theorems prove the stated PDE, regularity, support/decay, initial-data, and no-global-solution clauses, and do their kernel-reported dependencies contain only accepted foundations? The separate Euler result is not itself one of the Clay prize alternatives.

The current source census finds four actual `sorry` lines, all in the intentionally separate `ComparatorChallenges` files. It finds no `sorry` in the main exported result path by lexical source scan, but this is not yet a kernel verdict. The census also records declaration-level-looking `axiom`/`opaque` lexical hits requiring classification; comments and prose account for some hits. The next mandatory step is an independent `#print axioms` probe for the four exported declarations under the declared toolchain.
