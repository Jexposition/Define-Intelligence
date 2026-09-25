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
