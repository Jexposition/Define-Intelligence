# Independent peer review of the OpenAI Navier–Stokes and Euler formalisation

Status: working review, current public snapshot pinned to commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

This review is conducted in `NavierStokesReview`. The downloaded directory and the public source repository are not edited. The review distinguishes four questions that must not be conflated:

1. Does the Lean source compile?
2. Does the Lean kernel accept the exported theorem without `sorryAx` or an unreviewed project axiom?
3. Does the theorem statement match the claimed Navier–Stokes problem, including its quantifiers and function classes?
4. Does the mathematical construction establish the theorem rather than merely package the desired properties into an assumed interface?

The first two are formal verification questions. The last two are mathematical peer-review questions.

## Executive finding

The current evidence does **not** justify either “the proof is false” or “the Millennium problem is solved”. The downloaded copy is stale relative to the public repository, and the public repository contains a substantially newer formal development. The official CMI statement permits the forced alternatives (C) and (D), so the presence of a smooth external force is not by itself a defect. The decisive audit is therefore whether the exported forced-breakdown theorems are kernel-checked from explicitly constructed witnesses and whether their global-solution negations use exactly the CMI admissible class.

The current repository-wide Lean scan finds four actual `sorry` lines in `ComparatorChallenges`, which the repository documents as intentionally separate challenge files. This is not yet evidence that the exported result theorems depend on `sorryAx`; that must be settled by recording `#print axioms` for each exported declaration. The repository’s `formalization.yaml` is a self-assessment and cannot substitute for that independent check.

There is also a procedural CMI distinction. CMI's rules require publication in a qualifying outlet, two years of rigorous examination, and general acceptance before CMI considers a proposed solution. CMI's 11 September 2026 announcement says the Navier–Stokes problem has apparently been settled and that the work is being analysed; it is not a prize decision. This review reports mathematical and formal evidence separately from CMI recognition status.

## Snapshot and provenance

The public repository is:

`https://github.com/openai/NavierStokesAndEuler`

The reviewed public snapshot is commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, dated 10 September 2026. The downloaded ZIP contains 2,493 comparable text/source entries. The current public clone contains all 2,493; 2,478 are identical after line-ending normalisation and 15 changed, including the theorem-facing and metadata files listed in `NavierStokesReview/evidence/download_snapshot_comparison.json`. Conclusions drawn only from the downloaded copy therefore require a changed-file check.

The review census excludes `.lake` dependencies and records file hashes separately. It is stored in:

`NavierStokesReview/results/UPSTREAM_SOURCE_CENSUS.md`

The source-to-result map is stored in:

`NavierStokesReview/results/UPSTREAM_PROOF_PATH_MAP.md`

## CMI criterion used in this review

The official Clay statement is the controlling specification:

`https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf`

It asks for one of four alternatives. Alternatives (A) and (B) concern the unforced problem. Alternatives (C) and (D) explicitly concern forced problems. Accordingly, a forced construction can be relevant to the CMI problem; the review must test the exact hypotheses rather than reject it because it is forced.

For a forced alternative, the review checks:

| Requirement | Review question |
|---|---|
| viscosity | Is the theorem quantified for every `ν > 0`? |
| domain | Is the result on `R³` or the periodic torus as claimed? |
| data | Is the initial velocity smooth, divergence-free, and in the required decay or periodicity class? |
| force | Is the force smooth and in the required spatial and temporal class? |
| solution class | Are velocity and pressure globally smooth in the precise sense required by CMI? |
| conclusion | Is there finite-time breakdown or failure of a global smooth bounded-energy solution, with the correct quantifier over global solutions? |

The official statement is authoritative for the CMI wording. The paper’s informal description is evidence about intent, not a replacement for that statement.

## What the current source visibly claims

The exported Navier–Stokes declarations are:

```text
NavierStokes.Comparator.navier_stokes_breakdown_R3
NavierStokes.Comparator.navier_stokes_breakdown_periodic
```

The exported Euler declarations are:

```text
Euler.euler_breakdown_R3
Euler.exists_compact_smooth_euler_singularity
```

The Euler results are separate from the CMI Navier–Stokes prize problem. They may be mathematically interesting, but they cannot by themselves establish a CMI alternative.

The R3 theorem visibly has the shape

```text
∀ ν > 0,
  ∃ u₀ f,
    InitialVelocityConditionDecay u₀ ∧
    ForceConditionDecay f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn ν u₀ f v p)
```

The periodic theorem has an analogous comparator shape. The internal R3 construction provides a candidate velocity, pressure, force, compact set, smoothness, divergence-free condition, PDE identity before the singular time, bounded kinetic energy before the singular time, and unbounded speed as the singular time is approached.

## Main proof path found in the source

The R3 path is not a single opaque theorem. It is routed through the following layers:

1. `NavierStokes/R3/ProblemStatement.lean` defines the candidate and global-solution predicates.
2. `NavierStokes/R3/ActualCandidate.lean` assembles the compactly supported candidate and transfers its properties.
3. `NavierStokes/ComparatorR3Theorem.lean` converts the candidate properties into the comparator theorem.
4. `NavierStokes/ComparatorR3Bridge.lean` defines the global-solution class and the normalisation/contradiction bridge.
5. `NavierStokes/ComparatorSolution.lean` exports the public theorem and prints its axiom dependencies.

The periodic path uses `PeriodicPaperTheorem.lean` and `PeriodicPaperComparator.lean`, including compression, scaling, and periodisation. That path needs its own audit; it should not be inferred automatically from the R3 path.

## Preliminary formal findings

### Compilation status

The public project pins Lean `4.34.0-rc2`, Mathlib at the matching revision, and the Comparator package at the matching revision. The requested V-lab 4.32 package cache has `mathlib` but no Comparator package, so it cannot be substituted for the declared project dependency tree. The broad all-project build was stopped because compilation is not the CMI criterion. A targeted `NavierStokes.ComparatorSolution` dependency build was attempted only to obtain project interfaces and kernel axiom output, but stopped before emitting `ComparatorSolution.olean`.

### Raw placeholders

The current repository-wide Lean scan finds four actual `sorry` lines, all intentional challenge placeholders in:

```text
ComparatorChallenges/NavierStokes.lean
ComparatorChallenges/Euler.lean
```

These files are not automatically disqualifying if they are not imported by the exported result declarations. They are disqualifying for any theorem that depends on them. The dependency and axiom report is therefore the decisive test, not the repository-wide raw token count alone.

### Project axioms

The repository reports the standard Lean axioms `propext`, `Classical.choice`, and `Quot.sound` for its headline results. These are ordinary axioms used by Lean and Mathlib and are not equivalent to an unproved Navier–Stokes assumption. Independent transitive confirmation with `#print axioms` remains pending because the targeted dependency build did not emit the required project interface. The status record does not substitute the repository’s self-report with an invented result.

The audit specifically searches for:

- `sorryAx` or `admitAx` in an exported result;
- project-level `axiom` or `opaque` declarations in the result dependency graph;
- imported challenge files containing `sorry`;
- declarations whose names suggest a theorem but whose body is only a wrapper around an assumed property;
- circular use of a target theorem or of a proposition definition that already contains the desired conclusion.

## CMI alignment questions still requiring closure

The formal statement appears structurally aimed at forced alternatives (C) and (D), which is legitimate. The remaining questions are exact and testable:

1. Does `InitialVelocityConditionDecay` imply the full CMI initial-data requirement, not merely decay?
2. Does `ForceConditionDecay` imply the complete smooth force condition on the entire future time domain?
3. Does the global-solution predicate quantify over the same solution regularity, domain, pressure, divergence, initial condition, and kinetic-energy bound required by CMI?
4. Is the statement’s finite-time conclusion about a genuine solution on the maximal pre-singular interval, rather than only a field satisfying the equation on an arbitrarily selected subinterval?
5. Is the force independent of the candidate solution and fixed before the global-solution contradiction is formed?
6. In the periodic route, are the velocity, pressure, force, and all required derivatives genuinely periodic after periodisation?
7. Are the scaling and compression maps proved to preserve the exact PDE, viscosity, initial data, and energy hypotheses rather than only a weaker surrogate?

These are not objections merely because they are difficult. They are the obligations that determine whether the Lean theorem is a formal proof of the CMI alternative or a formally verified theorem about a weaker custom predicate.

## Tested non-failure: compact-support contradiction

One potentially serious-looking objection was checked at source level. `CandidateProperties.not_global_agreement` in `NavierStokes/R3/CandidateBreakdown.lean:17-40` does not infer a pointwise bound from finite energy. It restricts the global smooth comparator to the compact spacetime set `Icc 0 1 × K`, obtains a continuous-on-compact bound, and then contradicts `SpeedUnboundedAtOne`. The generic `L²` versus `L∞` objection therefore does not apply to this particular bridge.

## What would count as a positive result

The review can classify the Navier–Stokes R3 claim as formally established for the stated CMI alternative only if all of the following are recorded:

- the pinned project interfaces are available for independent kernel inspection;
- every exported theorem has an independent `#print axioms` report with no `sorryAx` or unreviewed project axiom;
- the challenge files are absent from the dependency graph of the exported theorems;
- the exact source predicates are shown to imply the official CMI hypotheses;
- the candidate construction is traced from definitions to the exported witness without an assumed target property;
- the global-solution negation is proved for the same class of solutions CMI quantifies over;
- the R3 and periodic routes are reported separately.

Even then, “formal proof accepted by Lean” and “mathematical exposition independently understood by referees” remain separate standards. The former establishes kernel-level derivability; the latter requires a human-readable proof audit of the construction and its analytic estimates.

## Current classification

| Item | Status |
|---|---|
| Current public revision identified | VERIFIED |
| Downloaded copy current | NOT CURRENT |
| CMI forced alternatives allowed | VERIFIED from official CMI statement |
| R3 theorem shape mapped | VERIFIED at source level |
| Periodic theorem shape mapped | VERIFIED at source level; semantic audit pending |
| Challenge `sorry` files isolated | VERIFIED by source/import inspection; dependency proof pending |
| Exported theorem axiom sets | PENDING targeted dependency build and independent probe |
| Full CMI hypothesis equivalence | PENDING semantic audit |
| Independent claim that the Millennium problem is solved | NOT ESTABLISHED |

## Review rule

Until the pending rows are closed, the accurate description is:

> The repository contains a substantial Lean formalisation whose current public snapshot targets forced CMI alternatives (C) and (D). Its headline theorem may be formally strong, but the independent review must still verify the kernel dependency graph and the exact correspondence between the custom solution predicates and the official Clay hypotheses.

That is a narrower and more defensible statement than either dismissing the work because it uses forcing or accepting the repository’s self-assessed completion flag as an independent proof review.

## Review artefacts

- Plan: `docs/OpenAI_NavierStokes_CMI_First_Review_Plan.md`
- Axiom ledger: `docs/OpenAI_NavierStokes_Axiom_Ledger.md`
- Audit tracker: `docs/OpenAI_NavierStokes_Audit_Tracker.md`
- Source census: `NavierStokesReview/results/UPSTREAM_SOURCE_CENSUS.md`
- Proof-path map: `NavierStokesReview/results/UPSTREAM_PROOF_PATH_MAP.md`
- Kernel probe: `NavierStokesReview/src/probes/AxiomProbe.lean`
- Kernel output: `NavierStokesReview/results/AXIOMS_2026-09-22.txt`
