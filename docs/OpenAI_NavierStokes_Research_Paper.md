# A CMI-First Peer-Review Protocol for the OpenAI Navier–Stokes Lean Development

## Abstract

This paper records an independent, reproducible review of the Lean formalization accompanying OpenAI’s public claim concerning finite-time singularity formation for the three-dimensional incompressible Navier–Stokes equations. The review does not treat the words “blowup”, “formalized”, or “kernel checked” as interchangeable. It separates kernel validity, proposition content, and compliance with the official Clay Mathematics Institute formulation. The first local census finds a version drift between a downloaded extraction and the public repository’s later `main` commit. The public source exposes a whole-space theorem that claims a candidate construction for every positive viscosity and a bridge translating its nonexistence result into CMI alternative (C). The decisive work is therefore a transitive Lean axiom audit and a semantic audit of the candidate-to-comparator bridge, force decay, regularity domains, viscosity scaling, and periodic route.

## 1. Scope and standard

The official CMI statement allows a smooth external force. For alternative (C), it asks for smooth divergence-free initial data and a smooth force satisfying the stated decay conditions such that no globally smooth, bounded-energy solution exists on `R^3 × [0,∞)`. Alternative (D) is the periodic analogue. A criticism based only on external forcing would therefore misstate the official target. A valid objection must identify a missing hypothesis, a false implication, a dependency on an untrusted declaration, or a mismatch in the exact PDE and solution class.

## 2. Reproducibility boundary

The downloaded directory `NavierStokesAndEuler-main-open Ais solution` has no Git metadata and was timestamped locally on 2026-09-08. The separately cloned public checkout is pinned to commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, dated 2026-09-10. The local tree contains 2,486 Lean files; the public checkout contains 2,659. The current entry point imports `NavierStokes.PaperResults`, while the downloaded entry point does not. Results referring to “the OpenAI repository” must therefore name the snapshot.

## 3. Formal claim map

The public whole-space route is layered. `R3/ProblemStatement.lean` defines the candidate properties and breakdown statement. `R3/Theorem.lean:26-62` states `theorem_1_1_with_initial_rest`, `theorem_1_1`, `candidateStatement`, and `breakdownStatement`. `R3/ComparatorBridge.lean:22-45` converts compact support into the force condition used by the comparator, and lines 47-88 convert a hypothetical comparator solution into a global finite-energy solution, yielding the contradiction. This architecture is a useful review boundary because it exposes the exact lemmas where a semantic mismatch would occur.

## 4. Review hypotheses

The main risks are not the existence of many files by itself. They are: an exported theorem depending transitively on `sorryAx`; a bridge that changes viscosity, force, pressure sign, or time domain; compact support that does not imply the exact CMI decay condition used; endpoint regularity being conflated with global regularity; a scaling lemma that changes the quantified data; or a periodic theorem that is assumed rather than independently established. The Comparator challenge placeholders are intentionally retained benchmark stubs and will be treated separately from the main theorem dependency graph.

## 5. Methods

The review uses two toolchain lanes. The first is the requested Lean 4.32 environment with packages under `D:\Research Lab\V-lab-Equipment\.lake\packages-4.32`, used for compatibility and independent checks. The second is the repository-declared Lean 4.34.0-rc2 environment with mathlib and Comparator at their declared revisions, used to reproduce the public source. For each lane, the review records exact commands, compiler output, imported modules, and `#print axioms` results. Source files in the downloaded OpenAI extraction are not edited.

## 6. Preliminary result

The preliminary result is a review status, not a mathematical verdict. The public source has a concrete CMI-oriented theorem and bridge, while the downloaded snapshot is stale relative to `main`. The current lexical scan finds four intentional `sorry` placeholders in Comparator challenge files. This establishes what must be tested, but does not establish that the exported theorem depends on them. The first high-value deliverable is the kernel-derived axiom set for the whole-space and periodic exported claims.

## 7. Planned findings structure

Each finding will state the snapshot, exact declaration, CMI criterion, proof dependency, reproduction command, observed result, severity, and remediation or rebuttal. Numerical experiments, prose concerns, and failed builds caused solely by using the wrong toolchain will remain labelled as review evidence rather than proof failures.

## References

1. Charles L. Fefferman, [Existence and Smoothness of the Navier–Stokes Equation, official CMI problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
2. OpenAI, [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/).
3. OpenAI, [NavierStokesAndEuler repository](https://github.com/openai/NavierStokesAndEuler).
# Current review position: 2026-09-22

The current public snapshot is materially newer than the downloaded directory. The review therefore uses the public Git clone as the primary source and preserves the downloaded directory as a comparison snapshot. The latest public README claims forced breakdown alternatives in whole-space and periodic settings, while also presenting a separate unforced Euler result. The official Clay statement permits smooth forcing in its C and D alternatives, so the presence of forcing is not, by itself, a failure to address the Millennium problem.

The central peer-review question is narrower and more testable: whether the Lean theorem chain establishes the exact Clay quantifiers and analytic conditions, rather than a proposition with similar vocabulary. In particular, the review follows the chain from the exported adapters through `ComparatorR3Theorem`, the R3 candidate construction, the periodic compression and periodisation route, and the global-solution definitions. It also separates the challenge files, which contain intentional placeholders, from the main result path until the import graph proves otherwise.

The first machine census found 2,659 project Lean files and 173 files added relative to the downloaded copy. It found no lexical `sorry` in the four exported result files, but source cleanliness is only a preliminary result. Completion requires a successful current-toolchain build, independently captured `#print axioms`, and a line-by-line semantic comparison with the official CMI alternatives. Until those checks are complete, the appropriate status is preliminary review, not validation and not refutation.
