# OpenAI Navier–Stokes Audit Tracker

Statuses: `CONFIRMED`, `PENDING`, `OPEN`, `NOT_TESTED_THOROUGHLY`. No negative seal is issued from this initial pass.

| ID | Area | Finding or test | Evidence | Status | Next action |
|---|---|---|---|---|---|
| AUD-001 | Provenance | Local extraction is not a Git checkout; no remote or commit metadata is present. | Local root census, 2026-09-22 | CONFIRMED | Preserve the local path and hash its manifests and theorem files. |
| AUD-002 | Version drift | Public `main` is commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, dated 2026-09-10; it has 2,659 Lean files versus 2,486 locally and adds the `PaperResults` entry import. | `NavierStokesReview/src/upstream-current`, local extraction | CONFIRMED | Produce a path-level and normalized-content diff. |
| AUD-003 | CMI statement | CMI permits smooth external forcing in alternatives C and D; forcing alone is not a mismatch. | Official CMI PDF, equations (1)-(11), alternatives C-D | CONFIRMED | Audit force decay/support and periodicity exactly. |
| AUD-004 | Main theorem | Whole-space `theorem_1_1` quantifies over every positive viscosity and returns candidate properties plus no global finite-energy solution. | `NavierStokes/R3/Theorem.lean:26-62` | CONFIRMED at source level | Kernel-check theorem and transitive axioms. |
| AUD-005 | CMI bridge | `comparator_of_breakdown` turns candidate nonexistence into the Comparator C statement by translating a comparator solution into `GlobalFiniteEnergySolution`. | `NavierStokes/R3/ComparatorBridge.lean:47-88` | CONFIRMED at source level | Check all conversion lemmas and PDE conventions. |
| AUD-006 | Challenge stubs | Current public tree retains four intentional `sorry` lines in two Comparator challenge files: two in `ComparatorChallenges/NavierStokes.lean` and two in `ComparatorChallenges/Euler.lean`. | `rg -n '\bsorry\b'` | CONFIRMED lexical | Determine whether any main theorem imports them. |
| AUD-007 | Axiom dependencies | A source file containing `#print axioms` is not itself an axiom declaration. | `NavierStokes/ComparatorSolution.lean:31-32` | CONFIRMED | Capture actual outputs under Lean. |
| AUD-008 | Toolchain | Repository declares Lean 4.34.0-rc2/mathlib and Comparator rc2; requested shared package root is 4.32. | `lean-toolchain`, `lakefile.toml`, V-lab package directory | CONFIRMED | Build a 4.32 compatibility harness and a declared 4.34 build separately. |
| AUD-009 | Snapshot integrity | Local zip and extracted folder have not yet been compared file-by-file with normalized line endings. | Local zip plus extraction | PENDING | Hash archive entries and compare normalized source files. |
| AUD-010 | Whole-space regularity | Candidate and comparator use different domains and solution structures; endpoint and all-time clauses need direct proof tracing. | `R3/ProblemStatement.lean`, `R3/ComparatorBridge.lean` | OPEN | Make a quantifier/domain table. |
| AUD-011 | Force decay | Compact support to CMI Schwartz-type decay is asserted through a bridge lemma; this is a critical mathematical dependency. | `R3/ComparatorBridge.lean:22-45` | OPEN | Inspect `CompactSpatialForceDecay` and prove the exact implication. |
| AUD-012 | Periodic route | Periodic result is separate from the whole-space route and must not be inferred from C. | `PeriodicPaperTheorem.lean`, `PeriodicPaperComparator.lean` | OPEN | Trace periodic theorem and run its axiom audit. |
| AUD-013 | Independent check | Comparator instructions require tools not yet verified in this environment. | `ComparatorChallenges/README.md` | PENDING | Record tool availability and run when dependencies are pinned. |
| AUD-014 | R3 uniqueness bridge | `WholeSpaceUniqueness.candidate_global_agrees_before_one` reduces any global smooth finite-energy competitor to agreement with the compact candidate on every `0 <= t < 1`; the proof uses pressure recovery, pressure-flux bounds, compact comparison bounds, and closure. | `NavierStokes/R3/WholeSpaceUniqueness.lean:30-113` | OPEN | Audit each imported analytic theorem and confirm its hypotheses are proved, not merely packaged. |
| AUD-015 | Candidate assembly | `ActualCandidateAssembly.selected_witness` is derived from `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` with a concrete `StageEstimates` object, endpoint extensions, support, cone, and residual inputs. | `NavierStokes/ActualCandidateAssembly.lean:1090-1183`; `NavierStokes/GermCandidateAssembly.lean:164-302` | CONFIRMED at source level | Map the `StageEstimates` dependency chain and inspect for hidden assumptions. |
| AUD-016 | A-posteriori force | The finite-stage witness existentially returns `forcing` after constructing candidate fields and residual consequences. This is a construction choice and is compatible with the forced CMI alternatives unless the resulting force class fails. | `NavierStokes/GermCandidateAssembly.lean:164-302` | CONFIRMED interpretation | Check `ContDiff`, compact positive-time support, derivative decay, and exact force identity. |
| AUD-017 | R3 force decay bridge | Compact smooth force support is converted into the Comparator decay predicate through `CompactSpatialForceDecay` and the R3 bridge. | `NavierStokes/R3/ComparatorBridge.lean:22-45`; `R3/CompactSpatialForceDecay.lean` | OPEN | Verify all spatial/time derivative quantifiers and the exact CMI force class. |
| AUD-018 | Positive-viscosity scaling | `candidate_at_viscosity` uses `a = sqrt nu`, with the residual scaling lemma and transformed force; the theorem quantifies `nu > 0`. | `NavierStokes/R3/ViscosityScaling.lean:82-195`; `R3/Theorem.lean:26-62` | CONFIRMED at source level | Check transformed force, pressure, support, and energy scaling independently. |
| AUD-019 | Periodic route | The periodic CMI route is separately defined and proved through `PeriodicPaperTheorem` and `PeriodicPaperComparator`; it cannot be inferred from the R3 theorem. | `NavierStokes/PeriodicPaperTheorem.lean:92-165`; `PeriodicPaperComparator.lean:21-58` | OPEN | Complete periodicity, temporal decay, pressure, and Comparator mapping audit. |
| AUD-020 | Critique reconciliation | Existing critique drafts correctly identify a posteriori forcing and model-robustness concerns, but several call forcing a CMI defect and treat altered PDEs as counterexamples. | Supplied drafts listed in review plan §8 | CONFIRMED disposition | Preserve as interpretation/robustness questions; do not promote to proof failures. |
| AUD-021 | Build environment | The current machine session has no `elan` or `lake` executable on PATH, so an independent current-toolchain `#print axioms` run has not yet been obtained. | `where.exe elan`, `where.exe lake`, 2026-09-22 | OPEN environment issue | Locate the declared toolchain or record the exact external reproduction command without treating this as a mathematical failure. |

## Finding format

For every new item, record: snapshot/commit, exact file and line, proposition, command, output, affected CMI criterion, and whether the item is a proof failure, a statement mismatch, an environment issue, or merely a review question.
# Execution update: 2026-09-22

| Check | Current evidence | Status | Next action |
|---|---|---|---|
| Upstream provenance | Current public clone at `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`; downloaded copy is stale and non-Git | Confirmed | Preserve both snapshots and cite commit in every result |
| Project source census | 2,659 Lean files; 4 raw `sorry` lines in two `ComparatorChallenges` files; no raw `sorry` hit in exported result files | Preliminary | Run declaration-level dependency and kernel checks |
| CMI force criterion | Official CMI alternatives C and D explicitly allow smooth forcing | Corrected | Audit the exact force hypotheses instead of treating forcing as disqualifying |
| Main result path | `ComparatorSolution`, `ComparatorR3Theorem`, `ComparatorTheorem`, `R3/ProblemStatement`, `R3/ActualCandidate`, `PeriodicPaperTheorem`, and `Euler/Solution` identified | Mapped | Trace every exported theorem to its lowest-level premises |
| Kernel build | Upstream compilation is accepted as given; the review does not treat successful compilation as evidence of the CMI theorem | Not a gate | Use the declared repo/toolchain only to obtain exact kernel elaboration and `#print axioms` output when available |
| Axiom probe | Review probe exists at `NavierStokesReview/src/probes/AxiomProbe.lean`; its purpose is dependency inspection, not compilation validation | Pending | Inspect exported theorem dependencies and record exact `#print axioms` output |

## Build observation: 2026-09-22

The pinned public checkout was launched with:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build
```

The process remained active after approximately fifteen minutes and had emitted one project `.olean` under `.lake/build/lib/lean`. No final exit code or theorem-level axiom output was available at this update. This is an environment/build-state observation, not evidence for or against the mathematical theorem. The exported declarations therefore remain `PENDING` for kernel-level confirmation.

## Scope correction

The `ComparatorChallenges` files are reference challenge statements with intentional placeholders and are not evidence that the exported theorem path uses `sorry`. They still matter for reproducibility and must be reported separately. The audit must not convert their existence into a claim about the main result without a dependency check.

## Source-backed update: 2026-09-22

The main R3 path now has a more precise map. `ActualCandidateAssembly.selected_witness` is derived from a concrete `StageEstimates` object and `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`; the witness returns the candidate fields, an existential force, residual consequences, derivative decay, and endpoint extensions. The R3 nonexistence step then uses `WholeSpaceUniqueness.candidate_global_agrees_before_one`, whose proof invokes pressure recovery and pressure-flux estimates rather than assuming agreement.

This makes the finite-stage estimate chain and the whole-space pressure-flux comparison the two principal mathematical audit lanes. The a-posteriori definition of the force is recorded as an interpretation/relevance issue, not a CMI mismatch, because CMI alternatives C and D explicitly permit forcing. Hyperviscosity and Ladyzhenskaya objections change the PDE and therefore cannot refute a theorem about the classical Newtonian equation without an additional robustness claim.

The current environment does not expose `elan` or `lake` on `PATH`; therefore exact kernel-generated `#print axioms` output remains pending. This is an environment limitation, not evidence against the theorem and not a reason to re-test obvious compilation.
