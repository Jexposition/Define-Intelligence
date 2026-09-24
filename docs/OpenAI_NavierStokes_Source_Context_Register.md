# Source context register

This register keeps the external wording and the repository-level findings in
the same place. It is a context map for the counter-paper, not a substitute
for a proof.

## CMI formulation

Fefferman's official problem statement defines the unknown velocity and
pressure, says that the initial velocity and force are given, externally
applied data, and imposes incompressibility. It then defines the four
alternatives. In particular, alternatives C and D are existential statements:
they ask for a smooth divergence-free initial field and a smooth force for
which no global physically reasonable solution exists. The same statement also
requires the force decay estimates (5) or (9), and the solution regularity and
periodicity conditions in (6)--(11).

Primary source: [Fefferman's official problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf), especially pp. 1--2.

The phrase “given, externally applied” supports a serious causal/provenance
question: a force chosen after a candidate trajectory is constructed is not
the ordinary forward-data presentation of a Cauchy problem. It does not,
without an additional formal admissibility predicate, prove that the
existential C/D proposition is false. The review must keep those two claims
separate.

That qualification does not make the burden symmetrical. OpenAI must establish
the stronger paper and CMI claim it chose to publish. If the selected Lean
endpoint does not expose the paper's field-level identifications and their
analytic composition, the correct review result is **not established as
claimed**, even if the narrower existential endpoint has not been formally
refuted. This is a failure to discharge the published claim, not a request
that the reviewer prove its negation.

## OpenAI's stated construction

The published paper makes the residual strategy explicit. Its introduction
states a theorem with a smooth compactly supported force and a velocity that is
smooth for `t < 1`, bounded in kinetic energy, and unbounded in supremum norm
as `t` approaches one. In its physical-description section it says that for
an incompressible flow and pressure one can define the external force to be
the residual, and that the construction must arrange cancellation so the
residual and all derivatives extend smoothly.

Primary source: [OpenAI's Navier--Stokes paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), Theorem 1.1 and Sections 2--3. The repository copy is retained as `docs/navier-stokes openai.pdf`.

OpenAI's public announcement repeats the stronger headline: it says the
formalisation establishes statement C and D, with a smooth applied force and
bounded energy. The announcement also describes cancellation of the large
acceleration, pressure, momentum-transfer, and viscous terms. Those public
claims make the selected-field transport theorem the relevant review target;
they do not turn the residual construction into an automatic contradiction.
See [OpenAI's announcement](https://openai.com/index/navier-stokes-solution/).

This wording defeats a weak objection that merely says “the force is
residual-defined”. The stronger review question is whether the Lean endpoint
actually proves every advertised bridge: the selected fields, the full
five-moment quantities, the pressure semantics, the residual limits, and the
force extension must be the same object under the paper's definitions.

## Five moments and correction constraints

The paper's Appendix A uses five named cumulative radial quantities `(M, I, J,
S, C_p)` and solves a five-coordinate correction problem. The source audit
confirms that the repository contains substantive five-moment machinery
upstream. It also confirms that `FiveRowRank.FiveRows` has two exact zero
correction-moment rows and three debt-controlled rows. The selected-cycle
invariant transports two radial moments internally, but the exported `Witness`
does not expose an equality identifying those moments with the paper's five
named quantities.

That is the active CTR-005 correspondence objection. It is stronger and more
precise than claiming that the five-moment machinery is absent or that the
zero rows automatically freeze kinetic energy.

## Euler paper as a comparison, not a transfer

The companion Euler paper describes a different iterative architecture: smooth
parent and child Euler solutions are built on nested time intervals, with
target times increasing to a finite limit. It explicitly describes the child
becoming the parent at the next stage and controls convergence of initial data
and gradient growth.

Primary source: [OpenAI's Euler paper](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf), Sections 1--2. The repository copy is retained as `docs/euler.pdf`.

This comparison prevents a category error. The Navier--Stokes Lean files
inspected for CTR-017 use indexed raw stage families, finite prefix sums, and
smooth cutoffs. They do not, in the files audited, define a theorem saying
that the raw stage index is a sequence of temporal Cauchy intervals. The
Euler paper's parent-child time language therefore cannot be silently used as
evidence that the Navier--Stokes Lean construction has, or lacks, a temporal
matching theorem.

The public release makes the separation explicit as well: it describes the
Euler result as unforced, while the Navier--Stokes result is presented through
the forced alternatives C and D. That comparison is useful for scope control,
but it does not transfer the Euler argument into the Navier--Stokes endpoint.
The review must therefore test the forced candidate against the CMI statement
and its own selected-field transport, rather than infer a force-free conclusion
from the companion paper.

Primary source for the release distinction: [OpenAI's announcement](https://openai.com/index/navier-stokes-solution/).

## Counter-argument register

| Proposed argument | Source-backed assessment |
|---|---|
| “Residual-defined force is automatically illegal.” | Too strong as a literal C/D refutation; OpenAI explicitly presents residual construction, and C/D are existential. Keep it as a causal/provenance objection unless an independence requirement is formalised. |
| “The first two zero rows freeze total mass and kinetic energy.” | Not established. They constrain correction moments; the source does not identify them with total kinetic energy. |
| “The indexed stage constructor proves a temporal jump.” | Not established. The constructor has no adjacent-stage matching premise, but the selected summed fields have smoothness theorems. |
| “Smoothness lemmas alone prove the paper's semantics.” | Not established. Smoothness is conditional evidence; the selected five-moment and absolute pressure transport remain separate obligations. |

## Review rule

The paper should state “not established as claimed” where the selected bridge
is missing, and “formally refuted” only where a source-linked zero-sorry
theorem proves a false mandatory premise or derives `False` from the actual
selected witness.

## Selected-path force provenance

`SelectedResidualProvenance.lean` now extracts the exported selected witness
and proves that its force equals the selected Navier--Stokes residual at every
interior time. This establishes the causal/provenance mismatch as a property
of the construction rather than an inference from names. It still does not
add an independence predicate to the exported existential statement; the
distinction between a provenance objection and a literal C/D contradiction
remains essential.

## Whole-space uniqueness correction

The whole-space no-global-solution route is formally active. The comparison
theorem derives equality before time one from the two residual equations,
incompressibility, smoothness, finite-energy bounds, compact reference support,
and compact-test pressure recovery. The selected-candidate wrapper then uses
that equality with the speed blow-up. Compact pressure support is not used as
a substitute for the pressure argument and does not imply that the pressure or
velocity vanishes.

This source fact narrows the counter-paper. The remaining pressure objection is
the absence of an absolute selected pressure representative in the exported
semantic bridge, not the absence of a uniqueness proof. Evidence:
`NavierStokesReview/evidence/whole_space_uniqueness_audit_2026-09-24.md`.

## Fixed-force stability extension

The review-side theorem `FixedForcePerturbationStability.lean` makes the
forward-data reading explicit by requiring the same force and pressure to
survive every smooth, compactly supported, divergence-free perturbation of
the velocity. The selected candidate fails this stronger predicate at an
interior point. This is evidence of residual path dependence, not a literal
contradiction of the existential C/D endpoint, which does not include that
predicate.

Evidence: `NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md`.

The stronger review extension `SameDatumFixedForcePerturbation.lean` uses the
factor `t(t-t₀)`. It preserves the selected zero initial datum while retaining
smoothness, compact spatial support, divergence-free slices, and a nonzero
fixed-force residual defect at an interior switch. This removes the initial-data
qualification from the earlier probe, but it remains a strengthened
forward-data test rather than a literal contradiction of the existential C/D
predicate.

Evidence: `NavierStokesReview/evidence/same_datum_fixed_force_obstruction_2026-09-24.md`.

## Published claim versus exported endpoint: 2026-09-24

The official sources state a C/D solution claim, while the repository's
`Witness` exports a concrete C/D-shaped predicate. The review therefore does
not rely on the weaker argument that the theorem is merely an existential
placeholder. The unresolved issue is more specific: the paper's five-moment
mechanism is not identified with the selected final mixed fields, pressure,
residual, and force by any theorem located in the exported `Witness` chain.

This is an author-side burden of proof. The absence of that selected-path
transport theorem is enough to keep the stronger paper claim unestablished;
it is not, without a false selected identity, a formal contradiction to the
literal C/D endpoint.

Evidence: `NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.
