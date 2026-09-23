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
