# The Solenoidal Assembly Collapse Ledger
**Target Modules:** `SolenoidalDiagonal.lean`, `PhysicalResidualJetBounds.lean`

## Verification correction: the collapse premise is not source-supported

The original claim below assumes that the base potential is globally clamped
to a pure axial field. That assumption is false for the inspected source.
`AxisymmetricFields.potential` has three Cartesian components, and the
zero-sorry base-profile probe shows that `radialNormalize_anchor` is a gauge
condition on an anchor line, not a global annihilation of swirl or axial
structure. The final velocity is spatial-curl generated and is separately
proved divergence-free on the selected path.

Accordingly, the pure-swirl, zero-helicity, and fake-two-dimensional-fluid
claims below are rejected as evidence. The absence of a direct moment import
into the residual-bound module remains a correspondence question, but it does
not prove geometric collapse.

## 1. The Curl Extension Collapse
**Target Definition:** `velocitySum` (Line 188 of `SolenoidalDiagonal.lean`)
**Analysis:** 
`velocitySum` computes the mathematical spatial curl of the assembled potential field: `SpatialCurl.spatialCurl (potentialSum a q A)`. 
* **Correction:** The inspected source does not establish the pure-axial
  premise. `AxisymmetricFields.potential` has three Cartesian components, so
  the claimed zero radial and zero axial components do not follow.

## 2. Helicity and component structure
**Target Definition:** Any selected-path claim about $H = \int u \cdot (\nabla \times u) \, dx$
**Analysis:**
No selected-path theorem proving zero helicity, pure angular velocity, or
purely axial vorticity was located. `AxisymmetricFields.potential` supplies
three Cartesian components and `TailGaugePotential.radialNormalize_anchor`
only fixes a radial gauge value on an anchor line. The reduced profile
coordinates therefore do not justify a global helicity cancellation.

## 3. The Kernel Matching Matrix Check
**Target Definitions:** `StateRealization.chartIdentity` vs `FiveRowRank` matrices
**Analysis:** 
I executed a comprehensive cross-reference to find where the compiler enforces definitional equality between the solenoidal `velocitySum` and the production equations in `FiveRowRank.lean`.
* **The Missing Check:** No named lemma equating the production rank data
  with the selected curl-generated field was found. `PhysicalResidualJetBounds`
  evaluates the residual, but the inspected source does not show a direct
  `FiveRowRank` transport theorem there.
* **Correction:** The source separation supports a missing semantic bridge
  between rank data and the selected residual chain. It does not prove an
  intentional coordinate drop or that the physical equations were ghosted.

***
### Assembly Falsification Summary
No formal disproof is established by this note. Its surviving result is the
need for an explicit theorem transporting the paper's moment data into the
selected curl-generated field and residual estimates.

## Selected scalar moment refinement

The active selected cycle carries zero scalar angular and axial `barMoment`
values on the carrier at every stage. This rules out a stage-level collapse
argument based only on the two zero correction rows. The unresolved assembly
question remains concrete: whether the atlas coefficient and angular frame,
after localisation and spatial curl, realise the same radial moments in the
exported Cartesian sum.

The field-level refinement is now explicit on `r > 0`: component one of the
selected angular field recovers its scalar coefficient. At `r = 0` the source
uses a totalised zero angular frame. This is a calculation boundary, not
evidence of pure-axial collapse or a selected moment contradiction.

The new axis theorem reinforces the narrower reading. A zero component on the
radial axis follows from the totalised angular frame, but it does not imply a
globally pure-axial field, a curl collapse, or a nonzero moment defect.

The assembly order supplies a further restriction: the selected field is a
curl-generated potential sum plus a direct angular sum. The direct branch
cannot be silently absorbed into the solenoidal curl calculation.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

The positive-radius frame component is now exact and source-backed. It is a
rotated Cartesian component, so the assembly cannot be compared with a scalar
radial moment until the torus-average and boundary transport are supplied.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

The selected direct branch's component formula is now explicit and retains
the polar rotation, graph scale, and `swapCylinder` coordinate reindexing. This
further rules out treating the scalar profile as an unrotated Cartesian field,
but it does not establish pure-axial collapse or a moment defect.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

The direct branch is not a source of an unrotated moment leak: its selected
component is identified with the native scalar and its exact order-two radial
moment is zero.  Any remaining contradiction must come from the separately
curled potential branch or from a proved failure of their composition.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

The rank correction is not eliminated by the solenoidal assembly: its
zero-mass premise is consumed before the temporal-plus-rank stream enters the
curl branch. The unresolved issue is instead whether the final curled mixed
field has the scalar radial representative required by `barMoment`.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

The solenoidal production calculation now exposes the first cutoff--curl
component as `(D₁χ)A₂ − (D₂χ)A₁`. The assembly is not entitled to discard this
term when passing to a radial moment.

The direct production branch has the same localisation issue: its native
zero-moment profile is multiplied by `spatialCutoff` before periodisation.
The exact unit-cube identity is proved by
`SelectedProductionDirectCutoff.lean`; the weighted radial moment remains to
be calculated.

The potential branch now has the corresponding selected positive-radial
component identity. Both production branches retain their localisation terms;
neither branch yet supplies the final mixed-field `barMoment` value.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

The potential branch now has a finite-prefix torus-average reduction. The
localisation commutator remains present inside the scalar integrand; no
boundary cancellation or nonzero weighted value has been inferred.

Evidence: `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md`.

## Finite-prefix endpoint qualification

The new endpoint theorem concerns only the cutoff factors in a fixed finite
prefix. It does not collapse the solenoidal assembly, identify the infinite
mixed field with the radial scalar, or prove a nonzero moment. The assembly
remains fully three-component at the source level and the selected value is
still open.

Evidence: `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md`.

## Mixed radial observable qualification: 2026-09-26

The actual mixed first component now has a typed `barMoment` pullback on the
positive-radius section. This confirms that the direct branch remains part of
the selected field rather than disappearing by definition. No value-level
moment calculation or collapse to zero follows from the interface theorem.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

The mixed torus average now reduces to the actual radial integrand. The
solenoidal assembly does not collapse by this identity; the direct branch is
still explicit and its weighted value remains uncomputed.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The selected radial pullback is periodic after Cartesian periodisation. The
conditional bounded-support obstruction does not collapse the solenoidal field
because the required support premise is not established.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

The R3 packaging theorem confirms that the solenoidal field's exported type
does not itself identify a five-coordinate moment payload. It does not show
that the assembled field collapses or that its actual moment is nonzero.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.
