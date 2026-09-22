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

## 8. Current evidence update

The downloaded ZIP is not simply an unrelated tree: all 2,493 comparable source/text entries are present in the public fork, with 2,478 unchanged after line-ending normalisation and 15 changed. The review therefore pins the public commit and treats the ZIP as a comparison snapshot rather than silently substituting it for current source.

The source audit confirms four actual `sorry` declarations, all in the separately named `ComparatorChallenges` files. The reviewed Navier–Stokes and Euler result modules do not import those challenge files lexically. The periodic route also explicitly declares pressure periodicity in `PeriodicPaperTheorem` and supplies it in `PeriodicComparatorSolution`, correcting the older supplied criticism that this condition was absent.

No concrete CMI statement mismatch has been demonstrated in the source-level pass. The R3 adapter has the forced-C shape required by the official Clay statement, and the force is existentially constructed after the candidate fields. That a-posteriori construction is a legitimate peer-review question, but not a CMI violation unless the resulting force or bridge fails the official hypotheses. The transitive `#print axioms` report remains the final formal-integrity gate. The targeted dependency build was attempted only to obtain the required project interface, but it stopped before emitting `ComparatorSolution.olean`; no axiom set is claimed from that incomplete run.

# Current review position: 2026-09-22

The current public snapshot is materially newer than the downloaded directory. The review therefore uses the public Git clone as the primary source and preserves the downloaded directory as a comparison snapshot. The latest public README claims forced breakdown alternatives in whole-space and periodic settings, while also presenting a separate unforced Euler result. The official Clay statement permits smooth forcing in its C and D alternatives, so the presence of forcing is not, by itself, a failure to address the Millennium problem.

The central peer-review question is narrower and more testable: whether the Lean theorem chain establishes the exact Clay quantifiers and analytic conditions, rather than a proposition with similar vocabulary. In particular, the review follows the chain from the exported adapters through `ComparatorR3Theorem`, the R3 candidate construction, the periodic compression and periodisation route, and the global-solution definitions. It also separates the challenge files, which contain intentional placeholders, from the main result path until the import graph proves otherwise.

The first machine census found 2,659 project Lean files and 173 files added relative to the downloaded copy. It found no lexical `sorry` in the four exported result files, but source cleanliness is only a preliminary result. The remaining formal-integrity item is independently captured `#print axioms` output from the elaborated project interface, followed by the line-by-line semantic comparison with the official CMI alternatives. Until those checks are complete, the appropriate status is preliminary review, not validation and not refutation. The stopped dependency build is an environment limitation, not evidence of a theorem failure.

One suspected bridge failure was also checked and not found at source level: `CandidateProperties.not_global_agreement` bounds a global smooth comparator on the candidate's fixed compact spacetime support and uses that bound against the candidate's unbounded speed. It does not claim that a uniform finite-energy bound alone implies an `L∞` bound.

The finite-stage construction was then audited at its load-bearing interfaces. `StageEstimates` explicitly carries raw smoothness, growth, field bounds, background rates, and residual rates. The actual constructor obtains these from concrete cycle data, representations, coherence, and physical-field data. The source path does not expose a missing residual estimate disguised as a theorem conclusion. A related specification concern remains: `JetRate` is only an eventual inequality for `iteratedFDeriv` and does not itself bundle smoothness. Because the stage record separately requires `ContDiffOn` for the raw fields, and the inspected residual-stability consumers likewise require explicit smoothness, this is not currently a CMI failure. A complete endpoint-consumer audit is still required.

The pressure-flux uniqueness route was also traced. The localized closure theorem receives an explicit pressure-flux inequality, but the R3 uniqueness theorem derives that inequality through pressure-gradient recovery from the comparison equations and finite-energy hypotheses, then through canonical Riesz pairing and cutoff estimates. Compact support supplies the reference-field bounds; the competing global solution supplies smoothness and uniform finite energy. No source-level circular assumption of global agreement was found. This remains a structural source result rather than an independent validation of the analytic proof terms or their kernel axiom footprint.

An independent September 2026 semantic-coverage preprint identifies three further source-level tests: a common positive domain for every inverse and differentiated inverse, term-by-term residual closure through curl, self-interaction, pressure, mean, support, and normalisation terms, and derivative-loss bounds independent of correction stage. The present audit records these as open leads. They sharpen the review method without establishing a defect: a zero-sorry kernel proof can validate an abstraction while leaving the paper-to-abstraction correspondence underexamined.

The subsequent source pass partially resolved those leads. `SmoothFamilyTorusInverse.inverse_finiteJets` explicitly fixes a five-derivative loss, `PhysicalResidualJetBounds` expands the residual into source, mean, base, Gaussian, alias, and excluded contributions, `ActualCycleResidualBounds` carries a derivative-order loss through all correction indices, and the endpoint adapter derives smooth extensions from `OneSidedExtension`, joint limits, and `PhysicalJets.of_rawStage`. These checks are meaningful positive evidence against an under-specified residual ledger. They do not by themselves establish one common inverse domain, prove the analytic provenance of every invariant and `PhysicalData` premise, or identify the torus candidate with the whole-space CMI witness. The semantic status therefore remains partially verified and open.

The inverse call-site map narrows the common-domain concern. The universal
torus estimate is specialised to a fixed `fiberShell a b s`; the radial
source-jet induction preserves that same fibre and support interval; and the
mixed-jet and real-complexification interfaces retain one slow parameter set.
No empty-domain failure was found. The unresolved question is whether the
conditions guaranteeing `a ≤ b`, nonempty fibres, and physical-domain
coverage are visibly connected to the final selected witness and its R3
localisation.

The periodic-to-compact transition is also deliberate rather than contradictory. The periodic candidate layer is localised by `R3CompactCandidate`, and `R3/ActualCandidate` packages the resulting compact fields and positive-time compact force into the whole-space statement. The audit records this as a tested non-failure and keeps the pressure-flux and kernel dependency checks open.

## 9. External research update

The external literature was checked as a prioritisation aid rather than as a substitute for inspecting the repository. An independent September 2026 semantic-coverage preprint identifies the same three high-value tests now tracked locally: common nonempty domains for all inverse constructions, term-by-term closure of the nonlinear residual and pressure/mean/support terms, and derivative-loss bounds independent of correction stage. The source audit has positive evidence for several interfaces, but the common physical-domain and torus-to-R3 correspondence remain open.

A later arXiv paper studies data generated by the compact forced construction while explicitly taking the OpenAI theorem as an input. It is therefore downstream work, not independent validation. A separate neural-forcing paper provides a useful methodological warning that a computational objective is not a continuum proof certificate without a theorem and robust margin, but it does not audit this Lean repository. The exact sources and dispositions are recorded in `NavierStokesReview/results/EXTERNAL_RESEARCH_UPDATE_2026-09-22.md`.

The external review does not change the current classification: no concrete CMI statement mismatch has been established, intermediate analytic declarations report only standard foundational axioms, and the headline transitive axiom audit remains open until the candidate and exported theorem interfaces are available.

## References

1. Charles L. Fefferman, [Existence and Smoothness of the Navier–Stokes Equation, official CMI problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
2. OpenAI, [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/).
3. OpenAI, [NavierStokesAndEuler repository](https://github.com/openai/NavierStokesAndEuler).
