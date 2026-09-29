# The Final Dependency Closure Validation Ledger
**Target Modules:** `NavierStokes/R3/Theorem.lean`, `NavierStokes/R3/ActualCandidate.lean`, Import Graph History

## Verification correction: existential assembly is not a hollow proof

The selected theorem does unpack a generic existential witness, but that is the
declared `Witness` interface. `ActualCandidateAssembly.selected_witness` is
constructed from the actual stage-estimate and germ/residual chain before it
is consumed by `R3/ActualCandidate` and `R3/Theorem`. The unpacking operation
does not establish that the fields are geometrically fake.

The defensible finding is narrower: the selected public witness does not expose
the paper's five named moments as a field, and the selected residual interface
does not visibly import `FiveRowRank` as a semantic identity. That is a missing
paper-to-code bridge, not proof of a compiler illusion.

## 1. The Hollow Type Inhabitation Proof
**Target Definitions:** `selected_candidate_one_with_initial_rest` (Line 148 of `NavierStokes/R3/ActualCandidate.lean`) and `theorem_1_1_with_initial_rest` (Line 32 of `NavierStokes/R3/Theorem.lean`).
**Analysis:** 
The final proof structure explicitly unpacks the constructed variables using the `obtain` tactic:
`obtain ⟨a, _, ea, eb, ep, forcing, hc, hf, _⟩ := ActualCandidateAssembly.selected_witness`
* **The Compiler Acceptance:** The Lean 4 compiler accepts this unpack purely because `selected_witness` successfully inhabits the `Witness` existential type. 
* **The actual limitation:** The public witness does not expose a theorem
  identifying its fields with the paper's five named moments or with a
  `FiveRowRank` matrix. That is a missing semantic bridge, not a hollow
  existential assertion or evidence that the geometry is fake.

## 2. The Explicit Import Graph Closure
**Target Interface:** The unbroken import chain from the final theorem to the realization core.
**Analysis:** 
The exact file chain is:
`Theorem.lean` ➔ `ActualCandidate.lean` ➔ `ActualCandidateAssembly.lean` ➔ `ActualCycleResidualBounds.lean` ➔ `PhysicalResidualJetBounds.lean`.
* **The transport gap:** The direct residual-bound modules do not expose a
  semantic `FiveRowRank` equality. A transitive closure rooted at
  `ActualCandidateAssembly.lean` nevertheless reaches `FiveRowRank`,
  `FiveProfileMoments`, and `PositiveOrderMoments` through upstream
  construction modules. Direct-import separation is therefore evidence about
  the endpoint interface, not evidence that the rank machinery is absent.
* **The interface boundary:** `selected_witness` is consumed as a generic
  `CandidateProperties` structure. This hides the construction history from
  the public endpoint, but does not prove that the underlying fields violate
  the PDE or that every moment constraint was discarded. The missing item is
  an explicit theorem exposing and transporting the paper's five moments.

## 3. The Chronological Override Statement
**Target History:** Git chronolog of `WholeDomain*` dead code branch (CTR-011).
**Analysis:** 
A review of the repository's git commit timestamps confirms a deliberate architectural override.
* **The Abandonment:** The `WholeDomain*` branch (e.g., `WholeDomainStageBounds.lean`, `WholeDomainPhysicalStageTheorem.lean`) was created on `2026-09-10`. 
* **Correction:** The import separation shows that some `WholeDomain*`
  modules are not on the selected-witness path. It does not establish motive,
  chronology, abandonment because of failed physics, or a purely topological
  result. Those claims require evidence beyond file timestamps and are not
  used in the active verdict.

***
### Dependency Validation Summary
The validated conclusion is narrower: the final public witness does not expose
the paper's five-moment realisation as a selected-path theorem. Its pressure
comparison infrastructure likewise does not expose an absolute global
Poisson representative for the selected pressure. These are material
paper-to-code correspondence objections. They are not irrefutable formal
disproofs, and they do not establish that the endpoint contains no 3D
Navier–Stokes fields.

## 4. Selected-closure census

The import traversal was rerun from `ActualCandidateAssembly.lean` and reached
507 local modules. Literal occurrence counts in that closure were 154 for
`PositiveOrderMoments`, 146 for `FiveProfileMoments`, 104 for `FiveRowRank`,
44 for `FiveRows`, 42 for `physicalMoments`, and 44 for
`CorrectionState.debt`. The surviving objection is the missing selected-field
transport theorem, not a dead-code claim.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Internal invariant versus exported witness

The selected import closure contains an actual cycle invariant: the
`CycleAnalyticInvariant.masses` field is propagated by `state_invariant`.
This is distinct from the public `Witness` type, which does not expose that
field or an equality to the paper's five moments. The valid correspondence
objection is therefore an endpoint transport gap, not absence of all local
mass-preservation logic.

## Endpoint payload check: 2026-09-25

The selected `Witness` is inhabited and carries the concrete C/D-shaped
properties, but its exported proposition contains no five-coordinate debt or
moment equality. The zero-sorry extension
`SelectedEndpointMomentTransportObstruction.lean` proves that a nonzero
abstract five-moment payload can coexist with the selected witness. This
formalises the endpoint's inability to certify the paper tuple without
claiming that the selected integrals themselves are false.

The result strengthens the paper-level counterfinding under CTR-005. It does
not justify calling the selected endpoint a fake field or a kernel-level
contradiction.

Evidence: `NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md`.

## Profile-tail collision route

The closure contains the rank and moment machinery, but the source-level
types remain distinct at the endpoint. `FiveRows` acts on correction profiles;
`barMoment` acts on radial/toroidal profile histories; `Witness` exports the
assembled Cartesian sums and candidate consequences. The new zero-sorry
refutation module confirms that nonzero runtime debt does not collide with the
zero correction rows.

The unresolved task is a genuine field-level evaluation bridge, not a search
for a dimension mismatch. Until a selected nonzero remainder is proved, no
`False` theorem follows from this route.

Evidence: `NavierStokesReview/evidence/ctr005_profile_tail_collision_route_2026-09-25.md`.

## Selected scalar moment correction

The closure contains a proved selected-cycle scalar result in the exact
`barMoment` operator: the angular second and axial first mean-state moments
vanish on the carrier for every selected stage. This confirms that the active
upstream invariant is substantive. It remains distinct from the exported
Cartesian `Witness` sums, so the selected-field transport calculation is still
the load-bearing paper objection.

Evidence: `NavierStokesReview/evidence/selected_scalar_barMoment_transport_2026-09-25.md`.

The selected radial-section theorem is an additional active closure result.
It connects one actual Cartesian component to the scalar coefficient on the
positive-radius section, but does not connect the entire mixed `Witness` field
to `barMoment` or establish a nonzero remainder.

The new axis-boundary completion is part of the active review closure. It
proves the selected direct stage's component-one value on the axis, while
leaving the full mixed-field-to-`barMoment` transport open. It therefore adds
source precision without changing the burden-of-proof classification.

Evidence: `NavierStokesReview/evidence/selected_radial_axis_boundary_2026-09-25.md`.

The active closure now includes `SelectedMixedVelocityDecomposition.lean`.
It proves the source order `curl(potential sum) + direct sum`. This is a
review-side identity with no new upstream assumptions; the radial
`barMoment` transport remains open for both summands.

The closure also builds `SelectedCylindricalComponentTransport.lean`, which
transports the exact positive-radius frame component through the source polar
chart theorem. It adds no moment identity or contradiction; the scalar
radial-field equality remains the next selected-path obligation.

The closure now also builds `SelectedPhysicalComponentTransport.lean`. It
retains the source `swapCylinder` reindexing and graph scale in the selected
direct component. This is selected-path positive evidence and does not alter
the unresolved full-field-to-`barMoment` obligation.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

The closure now includes the direct radial moment bridge.  It compiles the
selected direct component-to-scalar equality and the exact zero radial
integral, while leaving the potential/curl-to-`barMoment` transport open.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.
## Selected-stream refinement: 2026-09-25

The closure result must be read with the selected-field trace. The rank
modules are reachable and their zero-mass premise is consumed by
`LocalRankDefect.rankPotential`; the selected stream is assembled from
temporal and rank families and then enters the Cartesian curl branch. The
remaining CTR-005 issue is not dead-code reachability. It is the absence of a
selected theorem transporting that assembled curl field into the scalar
`PressureStream.torusAverage` input used by `barMoment_apply`, with all
localisation, summation, and boundary terms accounted for.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

The review closure now includes a zero-sorry selected component theorem for
the cutoff--curl term. It adds a source dependency to the radial calculation,
not a new axiom and not a contradiction.

The selected radial completion derives the same component from the selected
schedule and source physical-domain smoothness. Its remaining dependency is
the full scalar `barMoment` transport, not a missing upstream module.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

## Closure update: finite-prefix endpoint transport

`SelectedFiniteCutoffEndpoint.lean` adds only existing source dependencies:
the axis-scale limit and the finite-family cutoff plateau. It introduces no
new axiom and no endpoint contradiction. The remaining closure obligation is
the uniform transport from finite prefixes to the selected infinite sum.

Evidence: `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md`.

## Closure update: mixed `barMoment` typing

The review-side completion imports the existing mixed decomposition and
bar-moment interface only. Lean verifies the scalar pullback and its
positive-radius coordinate identity without new axioms; the weighted value and
infinite-sum transport remain outside the closure.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

The closure now includes the branch split and exact torus-average reduction,
without adding axioms or evaluating the remaining radial integral.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The closure now contains a zero-sorry periodicity theorem and a conditional
support obstruction. It adds no support premise to the authors' endpoint and
does not produce `False`.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

The R3 endpoint closure has now been tested separately. The review completion
shows that the exported `CandidateProperties` record admits coexistence with
a nonzero abstract five-coordinate payload. This is a type-level packaging
observation; it does not imply that the concrete selected field has nonzero
moments and does not close the `barMoment` transport.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.
