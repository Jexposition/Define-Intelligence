# Germ Geometry Core Extraction Ledger

## Verification correction: scope of the geometry claim

The direct import observation is valid: `GermCandidateAssembly.lean` does not import `PositiveOrderMoments` or `FiveProfileMoments`. The stronger conclusion that the selected construction is entirely independent of five-moment machinery is not valid, because the active upstream chain reaches that machinery through `GlobalSlowProfiles`, `NominalProfile`, and `ModulatedProfileAssembly`. The defensible finding is narrower: the generic germ/summation interface does not expose a theorem transporting the five named physical moments into the selected endpoint.

## 1. The Geometric Specification Drift (The Component Count)
**Target Definition:** `potentialSum_eq_base_germ` (Lines 75-96 in `GermCandidateAssembly.lean`)
**Analysis:** 
Your hypothesis correctly anticipated a semantic shift, but the reality is even starker. `potentialSum_eq_base_germ` is **not** an algebraic vector construction lemma; it is a purely topological equivalence theorem.
* **Component Count Evaluated:** **Zero explicit components.** The lemma does not build a 3D matrix, a `Triple`, or any geometric vectors. It operates entirely on abstract functions of type `VelocityField` (which maps `SpaceTime → Space`). 
* **The Mechanism:** The lemma merely proves that because the `initial` and `stages j` fields are constructed to be strictly zero in a neighborhood of the origin (via `hInitial` and `hStages`), the infinite sum `SolenoidalDiagonal.potentialSum` collapses algebraically to exactly the `base` germ near the origin. 
* **Corrected verdict:** The lemma is agnostic about component formulas because its type is `VelocityField`. The three-dimensional geometry is supplied upstream by `TailGaugePotential.finalPotential` and the solenoidal/curl construction. Thus the lemma proves localisation of the series, not omission of cross-components. Its audit consequence is narrower: the localisation lemma carries no five-moment payload.

## 2. The Holomorphic/Analytic Envelope (The Scaling Factor)
**Target Definition:** `exists_candidate_witness_of_finite_stages` (Lines 164-271 in `GermCandidateAssembly.lean`)
**Analysis:** 
The series convergence does **not** rely on a hard-coded geometric decay rate (like $2^{-j}$). Instead, it uses a dynamically generated, infinitely accelerating sequence.
* **The Scaling Factor (`ar : ℕ → ℝ`):** At Line 225, the scale is defined as `let ar : ℕ → ℝ := fun j => (a j : ℝ)`.
* **The Bounding Lemma:** The sequence `a j` is forcibly extracted from `E.exists_schedule` (Line 224), which takes the `StageEstimates` (the massive inductive bounds proven in earlier files) and generates an integer sequence that guarantees the supports of the fluid stages shrink fast enough to sum cleanly.
* **Corrected verdict:** The schedule is selected to satisfy analytic estimates; it is not evidence of physical energy dissipation. No invalidity follows from the schedule alone. The live question is whether the selected schedule also preserves the paper's five moment identities and the residual estimates required by the PDE interpretation.

## 3. The Missing Balance Refutation
**Target Cross-Reference:** `GermCandidateAssembly.lean` vs. `PositiveOrderMoments.lean`
**Analysis:** 
I executed a strict dependency search for `PositiveOrderMoments` within the import closure and namespace of `GermCandidateAssembly.lean`.
* **Occurrences Found:** **Zero.**
* **Verdict:** `GermCandidateAssembly` compiles its infinite series (via
  `potentialSum_eq_base_germ` and `exists_candidate_witness_of_finite_stages`)
  without directly importing or invoking the five-moment evaluation functions.
* **Conclusion:** This supports CTR-005 in its narrower form: the generic germ
  interface does not expose a theorem transporting the named five moments into
  the selected velocity and residual endpoint. The import closure nevertheless
  reaches five-moment modules upstream, so this is not evidence that those
  modules are dead code or that the final field is independent of them.

*** 
### Extraction Summary
This extraction isolates a review target. Topological localisation
(`potentialSum_eq_base_germ`) and the schedule theorem (`E.exists_schedule`)
construct the germ and convergence interfaces, while the selected path also
contains upstream five-moment machinery. The remaining question is whether an
explicit selected-path theorem connects those moments to the physical residual;
the present note does not establish an architectural severing.

The closure census confirms that this conclusion is an interface statement,
not a dead-code claim: 507 local modules are reachable from
`ActualCandidateAssembly`, including the substantive five-moment and rank
modules. The missing object remains a theorem for the actual selected mixed
sums and residual.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Selected recurrence and scalar moment correction

The selected natural-indexed construction does carry a proved scalar local
moment invariant. `SelectedCycleMomentTransport.lean` identifies `barMoment`
with the cycle state's radial moment and proves the selected angular and axial
values vanish on the carrier at every stage. Thus the unresolved issue is not
that the recurrence silently drops its local moment constraints. It is whether
the atlas/cutoff/curl construction transports those scalar values to the
Cartesian endpoint and the paper's full five-moment tuple.

Evidence: `NavierStokesReview/evidence/selected_scalar_barMoment_transport_2026-09-25.md`.

The coordinate transport is now concrete on the positive radial section:
`SelectedRadialSectionComponent.lean` recovers the scalar coefficient from the
actual angular field. The axis, localisation commutator, curl-generated
meridional field, and outer boundary still require separate transport.

The axis part of that transport is now exact for the selected direct angular
branch: its first component is zero at (r=0). This is not a substitute for
the all-order germ and moment calculation of the complete mixed field.

The complete mixed field is now source-resolved as two branches: a
curl-generated potential sum and a direct angular sum added after the curl.
The positive-radius and axis results therefore do not yet transport the
whole field into `barMoment`.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

The valid-chart component is now formally reduced to the frame rotation of the
cylindrical velocity. This clarifies the local germ data needed by the radial
gate but does not cross the axis or prove the global `barMoment` identity.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

The selected direct component is now source-resolved beyond the frame identity:
the formula retains `cos(theta)`, the graph scale, and `swapCylinder`. This
specifies the coordinate data that a global radial transport theorem must
carry, without asserting a nonzero remainder.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

The selected direct radial section now has an exact native scalar moment
identity.  Its order-two torus-averaged integral vanishes on the carrier;
this does not extend automatically across the potential/curl branch.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

The germ trace now records that rank data enters the selected stream through
`rankPotential` and is added to the temporal family. The germ-to-curl theorem
therefore has genuine rank content, but no selected theorem yet carries the
assembled result through torus averaging and `barMoment`.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

At the selected stage, the first Cartesian localisation contribution is
`(D₁χ)A₂ − (D₂χ)A₁`. Any germ-to-radial transport must preserve this term and
its support boundaries.

`SelectedPotentialProductionRadialScalar.lean` now records that term in the
actual first component on the positive-radial section. The remaining germ
transport is the lifted averaging map, boundary control, and final `tsum`.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

## Endpoint scale update: 2026-09-26

The selected axis scale is now source-confirmed as `1 - t`, and every fixed
finite cutoff prefix is eventually on at the endpoint. This does not evaluate
the germ's infinite curl sum or its radial moment; the germ-to-radial
transport and boundary terms remain open.

Evidence: `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md`.

## Mixed germ observable: 2026-09-26

The first component of the selected mixed field now has a source-typed radial
observable on the positive-radius section. The germ calculation remains open
at the value level because the direct localisation and periodisation terms
have not been integrated.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

The germ-to-radial map now exposes the exact mixed weighted integral. The cut
direct term remains a value-level calculation target.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The radial germ pullback is unit-periodic after the selected Cartesian
periodisation. A bounded radial shell would force zero, so support transport
must be justified before treating it as a genuine compact radial profile.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

The selected R3 type boundary has now been checked in zero-sorry Lean. It
does not export the five-moment payload used by the paper, but this remains a
packaging limitation rather than a numerical claim about the germ field.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.
