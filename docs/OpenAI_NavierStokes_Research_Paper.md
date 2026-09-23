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

## 6. Formal and CMI-interface result

The public source has a concrete CMI-oriented theorem and bridge, while the downloaded snapshot is stale relative to `main`. The current lexical scan finds four intentional `sorry` placeholders in Comparator challenge files. Independent transitive reports for the six audited headline exports now contain only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`, native-evaluation axiom, or project-specific axiom appears. The formal-trust gate is therefore closed for those exports, while analytic peer review remains separate.

## 7. Planned findings structure

Each finding will state the snapshot, exact declaration, CMI criterion, proof dependency, reproduction command, observed result, severity, and remediation or rebuttal. Numerical experiments, prose concerns, and failed builds caused solely by using the wrong toolchain will remain labelled as review evidence rather than proof failures.

## 8. Current evidence update

The downloaded ZIP is not simply an unrelated tree: all 2,493 comparable source/text entries are present in the public fork, with 2,478 unchanged after line-ending normalisation and 15 changed. The review therefore pins the public commit and treats the ZIP as a comparison snapshot rather than silently substituting it for current source.

The source audit confirms four actual `sorry` declarations, all in the separately named `ComparatorChallenges` files. The reviewed Navier–Stokes and Euler result modules do not import those challenge files lexically. The periodic route also explicitly declares pressure periodicity in `PeriodicPaperTheorem` and supplies it in `PeriodicComparatorSolution`, correcting the older supplied criticism that this condition was absent.

No concrete CMI statement mismatch has been demonstrated in the source-level pass. The R3 adapter has the forced-C shape required by the official Clay statement, and the force is existentially constructed after the candidate fields. That a-posteriori construction is a legitimate peer-review question, but not a CMI violation unless the resulting force or bridge fails the official hypotheses. The completed `#print axioms` reports close the formal-integrity gate for the audited exports. An independent zero-sorry force-bridge probe also elaborates the implication from compact smooth positive-time support to the full Comparator force-decay predicate.

# Current review position: 2026-09-22

The current public snapshot is materially newer than the downloaded directory. The review therefore uses the public Git clone as the primary source and preserves the downloaded directory as a comparison snapshot. The latest public README claims forced breakdown alternatives in whole-space and periodic settings, while also presenting a separate unforced Euler result. The official Clay statement permits smooth forcing in its C and D alternatives, so the presence of forcing is not, by itself, a failure to address the Millennium problem.

The central peer-review question is narrower and more testable: whether the Lean theorem chain establishes the exact Clay quantifiers and analytic conditions, rather than a proposition with similar vocabulary. In particular, the review follows the chain from the exported adapters through `ComparatorR3Theorem`, the R3 candidate construction, the periodic compression and periodisation route, and the global-solution definitions. It also separates the challenge files, which contain intentional placeholders, from the main result path until the import graph proves otherwise.

The first machine census found 2,659 project Lean files and 173 files added relative to the downloaded copy. It found no lexical `sorry` in the four exported result files. The independent reports now confirm the formal-trust status, and the CMI quantifier and force-bridge probes confirm the Lean-level statement mapping. The appropriate status is therefore a formal-trust pass with analytic peer review still open. The stopped dependency build was an environment limitation, not evidence of a theorem failure.

One suspected bridge failure was also checked and not found at source level: `CandidateProperties.not_global_agreement` bounds a global smooth comparator on the candidate's fixed compact spacetime support and uses that bound against the candidate's unbounded speed. It does not claim that a uniform finite-energy bound alone implies an `L∞` bound.

The finite-stage construction was then audited at its load-bearing interfaces. `StageEstimates` explicitly carries raw smoothness, growth, field bounds, background rates, and residual rates. The actual constructor obtains these from concrete cycle data, representations, coherence, and physical-field data. The source path does not expose a missing residual estimate disguised as a theorem conclusion. A related specification concern remains: `JetRate` is only an eventual inequality for `iteratedFDeriv` and does not itself bundle smoothness. Because the stage record separately requires `ContDiffOn` for the raw fields, and the inspected residual-stability consumers likewise require explicit smoothness, this is not currently a CMI failure. A complete endpoint-consumer audit is still required.

The pressure-flux uniqueness route was also traced. The localized closure theorem receives an explicit pressure-flux inequality, but the R3 uniqueness theorem derives that inequality through pressure-gradient recovery from the comparison equations and finite-energy hypotheses, then through canonical Riesz pairing and cutoff estimates. Compact support supplies the reference-field bounds; the competing global solution supplies smoothness and uniform finite energy. No source-level circular assumption of global agreement was found. This remains a structural source result rather than an independent validation of the analytic proof terms; its inspected kernel footprint is now recorded as standard-only in the intermediate report.

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

The periodic-to-compact transition is also deliberate rather than contradictory. The periodic candidate layer is localised by `R3CompactCandidate`, and `R3/ActualCandidate` packages the resulting compact fields and positive-time compact force into the whole-space statement. The audit records this as a tested non-failure; the remaining concern is semantic correspondence and analytic peer review.

## 9. External research update

The external literature was checked as a prioritisation aid rather than as a substitute for inspecting the repository. An independent September 2026 semantic-coverage preprint identifies the same three high-value tests now tracked locally: common nonempty domains for all inverse constructions, term-by-term closure of the nonlinear residual and pressure/mean/support terms, and derivative-loss bounds independent of correction stage. The source audit has positive evidence for several interfaces, but the common physical-domain and torus-to-R3 correspondence remain open.

A later arXiv paper studies data generated by the compact forced construction while explicitly taking the OpenAI theorem as an input. It is therefore downstream work, not independent validation. A separate neural-forcing paper provides a useful methodological warning that a computational objective is not a continuum proof certificate without a theorem and robust margin, but it does not audit this Lean repository. The exact sources and dispositions are recorded in `NavierStokesReview/results/EXTERNAL_RESEARCH_UPDATE_2026-09-22.md`.

The external review does not change the current classification: no concrete CMI statement mismatch has been established, intermediate analytic declarations report only standard foundational axioms, and the completed headline transitive axiom audit reports the same standard set. The remaining open work is semantic correspondence and human PDE review.

## 10. A concrete specification-quality finding

The independent Lean probe also exposed a weakness in the generic residual
rate interface. `DiagonalResidual.JetRate` quantifies over an arbitrary
filter and requires only an eventual derivative inequality. On the bottom
filter, every proposition is eventual, so the rate is provable for arbitrary
functions, including functions for which the displayed iterated derivatives
do not provide a smoothness certificate. This is a genuine formalisation
issue and is now recorded as `AUD-046` with a zero-sorry kernel probe.

It is not yet a disproof of the Navier–Stokes result. The principal path uses
named approach filters such as `originPast`, and the review must establish
their nontriviality and domain coverage at every load-bearing rate use. If
those filters are proved nontrivial and all smoothness premises remain
independent, the finding remains a reusable API warning rather than a CMI
mismatch. If a bottom or unverified filter can reach the selected witness's
residual closure, it becomes a proof-relevant defect.

The principal `GlobalBaseError.originPast` filter has now been independently
proved `NeBot`, clearing this concern for that endpoint. Derived intersections
and local correction filters remain to be checked individually.

The kernel audit meanwhile reached the direct pre-export layer. The R3 bridge,
periodic paper theorem, and periodic comparator bridge each report only
`propext`, `Classical.choice`, and `Quot.sound`.

The Navier–Stokes part of that gate is now closed at the kernel level: the
whole-space and periodic public exports, the R3 theorem, and the periodic
corollary all report only the standard foundational axioms. The Euler exports
now report the same standard foundational set. No audited headline declaration
reports `sorryAx`, native evaluation, or a project-specific axiom. This closes
the repository's formal-trust inventory under the declared toolchain, but it
still does not establish the exact CMI analytic correspondence or CMI
procedural acceptance.

## 11. Completion status

The independent formal-trust gate is now complete for the audited public
exports. Under Lean 4.34.0-rc2, the whole-space and periodic Navier–Stokes
exports, the R3 theorem, the periodic corollary, and both Euler exports report
only `propext`, `Classical.choice`, and `Quot.sound`. The four lexical
`sorry` declarations remain isolated in the separate Comparator challenge
target and do not appear in any of the six headline transitive reports.

The direct resumable compiler used for the Euler closure was an evidence
collection mechanism only. It avoided the large intermediate IR footprint of
the ordinary Lake closure and produced ignored interface files; successful
elaboration was not used as a mathematical verdict.

The CMI Lean-interface gate passes. The public statements elaborate with the
expected whole-space and periodic quantifier shapes, and the source mapping
covers the official PDE, force, decay/periodicity, pressure, and energy
clauses. Three items remain for independent PDE review: textbook equivalence
of the half-space `ContDiffOn` and within-derivative convention, proof-relevant
nontriviality of every derived filter used by the residual-rate path, and
explicit common-domain/premise provenance from the inverse/correction
construction to the selected R3 witness.

The strongest concrete formalisation issue found is generic rather than yet
route-breaking: `DiagonalResidual.JetRate` is vacuous on the bottom filter.
The selected `GlobalBaseError.originPast` endpoint is independently proved
nontrivial, so the generic issue is recorded as an API risk, not as a negative
finding against the exported theorem. The full disposition and evidence map
are in `NavierStokesReview/results/COMPLETION_AUDIT_2026-09-22.md`.

The exact endpoint check was then strengthened. `SpacetimeEndpoint.openPast 1`
is the explicit set `Iio 1 ×ˢ univ`, and a zero-sorry Lean probe proves that
`nhdsWithin (1, 0) (openPast 1)` is `NeBot`. Thus the selected endpoint is not
an instance of the bottom-filter vacuity. The generic interface remains weaker
than the semantic claim it is intended to represent: any derived intersection
or local-correction filter used by a rate consumer must still be shown
nontrivial or shown to carry the required domain coverage. This narrows, but
does not eliminate, the formalisation-quality finding.

## 12. Final peer-review disposition: 2026-09-22

**Verdict: no, the OpenAI claim is not established as a completed CMI
mathematical proof by this review.**

The repository does establish a different and important result: the audited
Navier–Stokes and Euler exports are kernel-checked Lean theorems, and their
CMI-facing proposition shapes match the whole-space and periodic alternatives
at the Lean-interface level. That answers the formal-trust question positively.
It does not answer the mathematical peer-review question positively, because
kernel checking validates the supplied formal premises and derivation, not the
independent analytic truth or CMI correspondence of every imported premise.

The final unresolved gates are construction-premise provenance, common-domain
coverage for all inverse and correction operations, proof-relevant nontriviality
of every derived filter, term-by-term residual and endpoint-force closure,
independent pressure/energy comparison, and equivalence of the half-space
smoothness convention to the CMI convention. No confirmed fatal counterexample
was found in the audited bridge lanes. The correct classification is therefore
`CLAIM NOT ESTABLISHED`, not `THEOREM REFUTED`.

The complete disposition, evidence links, and conditions for changing the
verdict are recorded in
`NavierStokesReview/results/FINAL_PEER_REVIEW_VERDICT_2026-09-22.md`.

## 13. Binary claim classification: 2026-09-22

The review must distinguish the formal claim from the broader public reading
of “proof of blow-up”. The answer is **yes** at the Lean formal-theorem level
for the forced CMI Alternative C/D-shaped result. The exported theorem
constructs a smooth positive-time force, uses zero initial velocity, and
excludes every global smooth finite-energy solution with that same force. The
CMI statement expressly permits such a force in Alternatives C and D.

The answer is **no** for the unforced Navier–Stokes problem. The development
does not prove that arbitrary unforced three-dimensional data blow up. The
answer is also **not yet certified** for a complete human line-by-line review
of every analytic certificate in the paper. This is a review boundary, not a
Lean compilation objection and not a claim that a fatal formal counterexample
was found.

## 14. Independent semantic composition: 2026-09-23

The semantic question was strengthened beyond matching OpenAI's own
Comparator definitions. An independent audit repository supplies a separate
Clay/Fefferman transcription, a Comparator-to-Clay bridge, and an end-to-end
adapter. We compiled those three layers against the current public OpenAI
source closure `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

The resulting declarations were:

```text
SemanticGap.ComparatorOptionC_to_ClayOptionC
SemanticGap.ComparatorOptionD_to_ClayOptionD
SemanticGapAdapter.openAI_to_ClayOptionC
SemanticGapAdapter.openAI_to_ClayOptionD
```

All four report only `propext`, `Classical.choice`, and `Quot.sound`. The
bridge checks equation conventions, divergence, decay predicates,
periodicity, the energy condition, and the contradiction direction for global
solutions. This is positive evidence that the current formal result has the
right forced CMI meaning. It does not convert the forced result into an
unforced A/B theorem. The raw transcript is in
`NavierStokesReview/results/INDEPENDENT_CLAY_BRIDGE_CURRENT_2026-09-23.txt`.

## 9. Procedural CMI boundary

The CMI prize rules impose a separate procedural condition. Before CMI will
consider a proposed solution, it must be published in a Qualifying Outlet, at
least two years must have passed, and it must have received general acceptance
in the global mathematics community. The public OpenAI announcement and GitHub
repository establish a public release and a formalisation claim, but do not by
themselves establish those three conditions. The audit therefore records a
formal-trust pass and CMI-interface match, while leaving analytic peer review
and CMI procedural eligibility open.

## References

1. Charles L. Fefferman, [Existence and Smoothness of the Navier–Stokes Equation, official CMI problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
2. OpenAI, [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/).
3. OpenAI, [NavierStokesAndEuler repository](https://github.com/openai/NavierStokesAndEuler).
