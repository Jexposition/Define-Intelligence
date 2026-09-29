# The Axisymmetric-Rank Interface Audit Ledger
**Target Modules:** `TailGaugePotential.lean`, `FiveRowRank.lean`, `LocalHeatExterior.lean`

## 1. The Angular Debt Extrication
**Target Interface:** `gaugedSwirl` mapping to $J_\theta$ (`d 1` / `Debt`).
**Analysis:** 
I executed a strict symbol dependency and import trace between the axisymmetric core and the production rank system.
* **The Trace:** The `gaugedSwirl` term is isolated entirely within `TailGaugePotential.lean` and `LocalHeatExterior.lean`.
* **The Interface Missing Link:** `FiveRowRank.lean` and `MeanRankUpdate.lean` **never import or reference** `gaugedSwirl` or `TailGaugePotential`.
* **Verdict:** No selected-path theorem was located that identifies the gauge
  subtraction with the paper's $J_\theta$ quantity or transports it into the
  production rank data. This is a correspondence question, not proof that the
  algebraic rank system is disconnected from the full construction.

## 2. The Axial Field Isolation
**Target Interface:** Convective terms `(u \cdot \nabla)u` evaluated on `heatPotential`.
**Analysis:** 
`heatPotential` (Line 217 of `TailGaugePotential.lean`) strictly activates only `coordinateVector 2` (the axial $z$-component, so $u_r = 0, u_\theta = 0$).
* **The Convective Transport:** In cylindrical coordinates, the non-linear convective interaction terms for the radial and angular momentum equations depend heavily on $u_\theta^2/r$ (centrifugal force) and $u_r u_\theta / r$ (Coriolis force). 
* **Scope correction:** The gauge anchor fixes a radial reference value; it does not prove that the selected field is globally purely axial or that $u_r$ and $u_\theta$ vanish everywhere. Any claim of global component collapse requires a separate theorem about the selected field.
* **Verdict:** The displayed `heatPotential` component is a specialised
  auxiliary field. It does not establish that the assembled velocity is purely
  axial or that the selected Navier–Stokes residual loses its cross-component
  terms. The endpoint field is produced from the full potential and spatial curl.

## 3. The Fixed Constraint Verification
**Target Interface:** `FiveRows` (Lines 241-244 in `FiveRowRank.lean`) vs 2D `streamFactor`.
**Analysis:** 
I cross-referenced the 5-row rank system with the base profile logic.
* **The Constraint Definitions:** 
  `FiveRows` has two explicit zero constraints on its correction functions:
  ` (∫ R, R ^ (2 : ℕ) * dv R) = 0 `
  ` (∫ R, R * ga R) = 0 `
* **The Disconnect:** The debt parameter `d` only starts feeding into the equations at row 3 (`d 0`), row 4 (`d 1`), and row 5 (`d 2`) (corresponding to $P$, $J_\theta$, $J_z$). Upstream preservation identifies the fixed rows with `barMoment 2` of the angular correction and `barMoment 1` of the axial correction. The source does not identify either row with a kinetic-energy integral or directly with the selected Cartesian velocity.
* **Verdict:** `FiveRows` contains two zero constraints and a three-coordinate
  debt interface. The review still requires the selected-path theorem showing
  how these constraints correspond to the paper's named moments; the row shape
  alone does not prove that the physical energy cascade is absent.

***
### Interface Falsification Summary
The surviving result is narrower. The inspected files do not exhibit the
selected-path theorem that identifies the paper's boundary variables with the
`FiveRowRank` debt and carries that identification through the residual bounds.
The source does establish a three-component potential and a curl-generated,
divergence-free endpoint, so this note does not prove a disconnected or
tautological fluid. The pressure comparison probe adds a separate limitation:
comparison identities do not, by themselves, establish an absolute global
pressure-Poisson representative for the selected pressure.

## Selected-cycle refinement

The production cycle is not free of all moment constraints. Its
`CycleAnalyticInvariant.masses` field is propagated by
`ActualCyclePreservation.state_invariant`, and the separate completion
`SelectedCycleMomentTransport.lean` exposes the two local radial moments for
the selected cycle. The unresolved issue is narrower: those two constraints
are not displayed as the paper's complete `(M,I,J,S,C_p)` identity at the
mixed `Witness` endpoint.

The scalar result is now explicit in `barMoment` notation: the selected cycle
mean angular and axial profiles have the required zero radial moments on the
carrier. This does not extend automatically to the final Cartesian velocity;
the angular frame, atlas scaling, cutoff, curl, and boundary terms remain the
field-level transport calculation.

The latest selected-field result makes the positive-radius part explicit:
`SelectedRadialSectionComponent.lean` recovers the scalar coefficient from
component one of the actual angular field on the radial section. The source
totalises the frame to zero on the axis, so this does not remove the axis
boundary obligation or prove a full `barMoment` identity.

`SelectedRadialAxisBoundary.lean` now proves the corresponding selected-stage
axis value: component one is zero when both radial Cartesian coordinates are
zero. The two results should be read together as a source-level branch split,
not as a discontinuity theorem.

The selected production field has an additional source-level split: the
potential sum is curled first and the direct angular sum is added afterwards.
The rank/profile interface therefore cannot be treated as the full
curl-generated Cartesian field without a separate transport theorem.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

The positive-radius frame calculation is now explicit:
`(frame θ v) 1 = sin θ * v 0 + cos θ * v 1`, and the source
`velocity_polar_forward` theorem transports it to the selected chart velocity.
This is a local component identity only; it does not identify the mixed field
with the scalar radial `barMoment` input.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

The selected direct branch now has its full component factor exposed on the
valid chart: polar rotation, graph scale, and `swapCylinder` reindexing all
remain present before comparison with a scalar radial profile. This is a
transport constraint, not a rank collision or a selected contradiction.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

The direct branch now has a selected scalar moment calculation: its positive-
radius first component is the native angular scalar, whose exact order-two
torus-averaged radial integral is zero.  This does not transport the curled
potential branch or the mixed endpoint into the same moment operator.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

The rank correction is active in the selected stream: its zero-mass identity
is consumed by `rankPotential`, and the successor stream is the temporal-plus-
rank angular field. The exported stream still reaches `barMoment` only through
an unresolved curl-to-scalar torus-average identification.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

The cut-stage curl calculation is now explicit at component level:
`(D₁χ)A₂ − (D₂χ)A₁` for the first Cartesian component. The rank/axis analysis
must retain this term before claiming a scalar `barMoment` identity.

The selected radial production completion now proves the corresponding first
component on the positive-radial section. Rank data therefore reaches a
concrete local scalar gate, but the torus-average and full `barMoment` bridge
remain open.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

The finite-prefix scalar has now been reduced through the exact torus-average
and `barMoment` definitions. The rank identities therefore have a concrete
finite-prefix radial target, but the target's value and its equality with the
complete mixed selected field remain open.

Evidence: `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md`.

## 2026-09-26 synchronization: finite-prefix endpoint

`SelectedFiniteCutoffEndpoint.lean` proves that every fixed finite set of
scaled cutoffs is eventually one on the axis as `physicalQ h (t, 0) → 0`.
This gives the finite-prefix endpoint input for the radial calculation. It is
not uniform in the prefix length and does not evaluate the complete mixed
field, `barMoment`, or a nonzero remainder.

Evidence: `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md`.

## 2026-09-26 synchronization: mixed `barMoment` domain

`SelectedMixedProductionBarMoment.lean` now pulls the first Cartesian
component of the actual mixed endpoint back to the scalar-family domain used
by `barMoment`. On positive radius it reduces to the mixed radial section.
This closes a typing and coordinate interface only; it does not evaluate the
mixed weighted integral or establish a nonzero remainder.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

The auxiliary torus average now reduces exactly, giving the literal mixed
weighted radial integral. Its value remains unevaluated.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The selected mixed radial pullback is also unit-periodic. The repository's
generic support theorem shows that bounded radial support would force it to
vanish identically; the selected endpoint does not export that support premise.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

The R3 packaging check confirms that the exported `CandidateProperties` record
does not carry a five-coordinate moment payload. This is an interface
non-implication only; the actual mixed radial integral remains the decisive
field-level test.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.
