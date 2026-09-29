# Deep Semantics Audit Log

## Verification correction: residual force regularity

The force is indeed constructed from a traced residual of already supplied velocity and pressure fields. However, the source does not make `force_smooth` an unconditional smoothness assertion: `CandidateFromLimits.tracedResidual_smooth` requires pre-singular regularity and locally uniform residual-jet limits, and the force also depends on away-extension premises. The audit target is whether those hypotheses are proved for the selected fields. This is stronger and more precise than calling the final theorem a tautology.

## 1. The Tensor Index Hole Search
**Target Files Analyzed:** All files exceeding 1,000 lines (e.g., `EulerProof.lean`, `CorrectionState.lean`, `CorrectionInitialization.lean`) and key structural modules (`PeriodicSobolev.lean`, `FiveRowRank.lean`, `CandidateFromLimits.lean`).
**Search Criteria:** `Fin.cast`, `Fin.cases`, array coercions, and structural downcasts from 5D to 3D.
**Findings:** 
* **Zero instances** of illegal index casting to drop off-diagonal terms.
* In Lean 4, the convective term `(u · ∇)u` is rigorously hardcoded in `ProblemStatement.lean` as `spatialDerivative u t x (u (t, x))`, which expands to all 9 terms of the $3 \times 3$ Jacobian.
* Because Lean's kernel checks equality by strict algebraic reduction (definitional equality), any internal helper lemma that dropped an off-diagonal term would fail to unify with the rigid global `navierStokesResidual` definition.
* **Verdict:** The tensor math is intact. There are no index holes or artificial term-dropping coercions.

## 2. Parameter Drift Analysis (Variable Shadowing)
**Target Parameters:** `selectedBudget`, `selectedThreshold`, `geometricThreshold`.
**Search Criteria:** Local `variable` declarations shadowing global parameters within large induction loops.
**Findings:** 
* A global scan of `ActualCandidateAssembly.lean`, `LocalScheduleWitness.lean`, and `LocalPotentialRebundle.lean` tracks `selectedBudget` through its entire lifecycle.
* Lean 4 strictly enforces variable contexts. Any local `variable (selectedBudget : ℝ)` that shadows an outer variable triggers a compiler warning or requires explicit namespacing. The parameters are passed explicitly as continuous functional arguments to the `StageEstimates` structures, rather than floating globally.
* `geometricThreshold` and `selectedThreshold` are structurally locked into the bounding integrals before the induction loops begin. There is no instance of them being locally overridden to `0` or `1`.
* **Verdict:** There is no parameter drift or variable shadowing. The parameters are conserved strictly across file boundaries.

## 3. Internal Tautology Detector
**Target File:** `CandidateFromLimits.lean` (223 lines).
**Search Criteria:** Algebraic circularity where velocity `u` and pressure `p` are defined in terms of each other, or where `force` is circularly defined to construct `u`.
**Findings:**
* **Line 28 (`tracedResidual`):** Extends the residual of `u` and `p`.
* **Line 82 (`force`):** Defines the external force strictly as `SpacetimeGluing.smoothExtension 1 (tracedResidual u p L)`.
* **Line 172 (`candidate_properties`):** Takes `u` and `p` as **given inputs** (via `CandidateProperties (activatedVelocity u) (activatedPressure p) (force u p ...)`). 
* The velocity field `u` is entirely constructed in `GermCandidateAssembly.lean` (via `potentialSum_eq_base_germ`) *before* the force is ever calculated.
* **Verdict:** There is no algebraic circular loop. The architecture is strictly sequential: 
  1. Construct singular `u` and `p`.
  2. Prove their limits evaluate to 0 (`VanishingJointJets`).
  3. Define `force := R(u, p)`.
  Because step 1 does not reference step 3, it is mathematically valid (this is exactly the Residual-Feedback Exploit we confirmed earlier).

---
### Summary
The Deep Semantics Audit confirms that the inspected FFI perimeter contains no
tensor truncation, variable shadowing, or circular algebraic loop. That is not
a certification of the complete CMI claim. The force result remains conditional
on the selected residual limits and extension data. The live objections are
the **Specification Drift (Missing Moment Transport Glue)** and the absence of
an absolute pressure-semantic bridge in the comparison interface.

The selected-closure census fixes the scope of that objection. The closure
rooted at `ActualCandidateAssembly.lean` reaches 507 local modules and contains
the upstream five-moment and rank machinery. The remaining issue is not an
algebraic circularity or a dead subsystem; it is the absence of an exposed
selected-field equality carrying the paper moments into the final residual and
force chain.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Source-trace correction: the five-moment machinery is active upstream

The 507-module selected closure reaches `PositiveOrderMoments`,
`GlobalSlowProfiles`, `AssembledSlowBase`, `FiveProfileMoments`, and
`FiveRowRank`. In particular, `PositiveOrderMoments.lean:76-85` defines the
five integrated rows, `GlobalSlowProfiles.lean:1043-1055` proves their
positive-order cancellation, and `AssembledSlowBase.lean:592-617` consumes
that result. The record therefore does not support a dead-code or absent-formula
objection.

The remaining load-bearing gap is at the selected mixed-field boundary:
`ActualCandidateAssembly.lean:515-523` assembles the final potential and
pressure fields, while `1121-1151` exports the `Witness` contract without a
field-level equality carrying the paper moments into the residual and force
claims. The publication verdict remains **NOT ESTABLISHED**, because the
paper markets those moments as part of the solution mechanism and the selected
endpoint does not expose their realisation.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.

## Selected Cartesian-to-radial checkpoint

The selected path contains substantive stage data and local moment
preservation. The unresolved semantic step is narrower and more concrete:
`barMoment` consumes scalar radial profiles, whereas the exported witness
contains Cartesian fields assembled by curl and `tsum`. The audit must now
evaluate the selected finite prefix, cutoff derivatives, and axis/tail terms.
No nonzero remainder is recorded until a Lean theorem identifies the resulting
profile with the selected field.

## Selected scalar moment result

The selected-cycle path now has a zero-sorry `barMoment` result for its scalar
mean profiles. This is a positive source fact and rules out a stage-iteration
leak as the explanation for any future mismatch. It does not settle the
Cartesian endpoint: the angular coefficient is transformed by the physical
atlas and frame before localisation and curl. The next contradiction target
must therefore be a proved field-level projection or boundary remainder, not a
generic claim that the moment system is absent.

Evidence: `NavierStokesReview/evidence/selected_scalar_barMoment_transport_2026-09-25.md`.

The selected radial section is now source-backed: component one recovers the
scalar angular coefficient for `r > 0`, while the axis is a separate zero-frame
branch. This narrows the remaining semantic question to the full selected
field composition rather than a generic coordinate objection.

The axis case is now proved for the selected direct stages: the first angular
component is exactly zero when the radial coordinates vanish. This is a
totalisation branch in the source, not a claim that the off-axis field fails to
extend smoothly. The unresolved semantic test remains the full radial moment
of the curl-generated mixed field.

The source-level mixed field is more specific than that shorthand: only the
potential branch is curl-generated, while the direct angular branch is added
after the curl. Consequently, the cutoff commutator cannot describe the whole
field until a separate direct-branch representation is proved.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

The positive-radius semantic bridge now has an exact component formula. It
shows that the Cartesian component used by the radial gate is frame-rotated,
not an unqualified scalar profile. The remaining semantic question is the
selected torus-average and `barMoment` transport of the complete two-branch
field.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

The component audit now includes the complete selected direct-branch factor:
frame rotation, graph scaling, and `swapCylinder` coordinate order. This
narrows the semantic bridge but does not establish a global radial moment or a
contradiction.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

The direct component's scalar source is now explicitly identified and its
order-two torus/radial moment is zero under the selected carrier hypotheses.
This is not a global moment identity for the mixed Cartesian endpoint.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

The semantic trace now separates active rank construction from endpoint
meaning. Rank zero-mass is used to build `rankPotential`, and the selected
stream is the temporal-plus-rank angular field before Cartesian curl. The
exported `MovingField` contract records smoothness, support, and periodicity;
it does not by itself establish the five cumulative moments of the final mixed
velocity.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

The source-level localisation semantics now expose the first curl component
as `(D₁χ)A₂ − (D₂χ)A₁`. This is a concrete transport obligation, not evidence
that the term is nonzero.

The latest image calculation is now source-specific: the production
`physicalPoint` map misses an explicit auxiliary point used by the full
`torusAverage` domain. The raw scalar family and the sampled production field
must still be compared before any selected moment difference is asserted.

Evidence: `NavierStokesReview/evidence/selected_torus_lift_image_scope_2026-09-25.md`.

`Atlas.physical` has now been checked at its defining branch. The zero-sorry
completion `SelectedAtlasPhysicalErasure.lean` proves that invalid native
values are not read by the selected physical map. Because `barMoment` reads
the native family on the full averaging domain, this establishes a precise
semantic boundary but not a selected moment discrepancy. Coverage or an
invariance theorem remains required.

The selected potential production is now carried to the first component on the
positive-radial section by `SelectedPotentialProductionRadialScalar.lean`.
This closes a local semantic transport step, while the full lifted-domain
representative and graph-coverage comparison remain open.

The next local semantic gate is now compiled. A section map sends lifted
physical coordinates to the positive-radial cylindrical coordinates, and the
selected potential-production component is represented as the exact scalar
family consumed by `barMoment`. The physical radial section is verified
against the source point construction. This is a genuine selected transport
fact, but it still leaves the full mixed post-curl/post-`tsum` equality and
the weighted value open; no remainder or `False` is inferred.

Evidence: `NavierStokesReview/evidence/selected_potential_production_barmoment_section_2026-09-26.md`.

The finite-prefix semantic gate is now also compiled. The selected partial
potential is expanded through the curl and localisation product rule, and its
production component is placed on the exact scalar family accepted by
`barMoment`. The positive-radius physical pullback is explicit. This does not
yet evaluate the torus average or identify the infinite selected endpoint, so
the semantic status remains unresolved rather than contradictory.

Evidence: `NavierStokesReview/evidence/selected_potential_production_finite_prefix_2026-09-26.md`.

The torus-average gate is also closed for the finite-prefix review scalar.
Because `pointToCyl` ignores the auxiliary coordinate, unfolding the source
integrals gives the exact `torusAverage` and `barMoment` reductions. This
does not supply the missing mixed-field or infinite-`tsum` equality, so it
does not establish a nonzero remainder or contradiction.

Evidence: `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md`.

## Endpoint quantifier correction: 2026-09-26

The finite-prefix cutoff result is source-backed, but its neighbourhood may
depend on the prefix length. It therefore cannot be promoted to uniform
control of the selected `tsum` or to a field-level contradiction. The semantic
load-bearing question remains transport of the complete mixed field into the
five-moment observable.

Evidence: `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md`.

## Mixed scalar-domain closure: 2026-09-26

The selected mixed first component is now transported to the scalar domain
required by `barMoment`, with an exact positive-radius pullback. This removes a
typing objection but not the semantic calculation: no equality with the
paper's five moments and no numerical remainder has been proved.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

The scalar-domain result now reduces `barMoment` to the literal radial
integral of the actual mixed endpoint. This is stronger transport evidence,
not a numerical contradiction.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The selected radial observable is now proved periodic in its unbounded radial
variable. This exposes a support/integrability compatibility obligation, but
not a contradiction without a selected support or nonzero theorem.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

## R3 packaging check: 2026-09-26

The exported R3 predicate was tested directly with a zero-sorry completion.
Its `CandidateProperties` witness can coexist with an arbitrary nonzero
five-coordinate payload because no five-moment equality is part of that type.
This sharpens the semantic boundary but does not determine the selected
field's actual radial integral or yield `False`.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.

## Map-layer safeguard

The repository map treats source-token edges as navigation diagnostics and
compiled `ConstantInfo` edges as the authority for endpoint reachability. This
prevents both opposite errors: calling reachable moment infrastructure dead,
or treating reachability as proof that its values survive the selected
Cartesian-to-radial assembly.

## Periodisation and support semantics: 2026-09-26

The compact support and periodicity interfaces apply to different stages of
the construction. `cutPotential` is supported before periodisation; the
selected mixed velocity is then formed from periodised branches. Because
`barMoment` is a global real-radial integral, compact support cannot be carried
across that step by definitional reduction. The missing selected support or
integrability transport remains part of CTR-005; no unconditional vanishing or
kernel contradiction follows.

## Mapping provenance boundary: 2026-09-26

The hardened map reconciles the extracted tree with the live checkout while
retaining 24 ambiguous entries rather than guessing their paths. Compiled
environment reachability is joined to source spans only by exact qualified
names. This removes filename and parser ambiguity from navigation, but it does
not establish the missing value-level transport from the assembled Cartesian
field to the paper's radial observables.
