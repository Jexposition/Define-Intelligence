# Base Profile Diagnostic Ledger
**Target Module:** `TailGaugePotential.lean`
## Verification correction: what the source actually proves

The reduced profile coordinates do not imply a scalar or one-component field. `AxisymmetricFields.potential` uses the profile in the three Cartesian basis directions, and `velocity` is obtained by `SpatialCurl.spatialCurl`. The gauge subtraction proves zero only on the radial anchor through `radialNormalize_anchor`; it does not globally kill swirl. The diagnostic therefore supports an axisymmetric three-component construction with a local gauge boundary, not a global zero-swirl collapse.

## 1. Component Matrix Envelope
**Target Definitions:** `potential` (Line 66) and `heatPotential` (Line 217)
**Analysis:** 
The underlying profile is parameterised through an **axisymmetric wrapper**,
then embedded in Cartesian components and converted to velocity by spatial
curl. The wrapper is a reduced-coordinate representation, not evidence that
the selected field is only two-dimensional.
* **Coordinate Mapping:** `potential` explicitly invokes `AxisymmetricFields.potential (SlowBorelBase.streamFactor ...) (gaugedSwirl ...)`.
* **Component Count:** The base germ is manufactured from exactly **two** independent geometric scalars: a 2D scalar stream function (`streamFactor`) and a 1D scalar angular swirl function (`gaugedSwirl`). 
* **Verdict:** The profile is parameterised by reduced axisymmetric data, but
  `AxisymmetricFields.potential` places that data in three Cartesian components
  and the selected velocity is obtained by spatial curl. The specialised
  `heatPotential` component does not establish that the full endpoint is
  one-dimensional or physically decoupled.

## 2.  Zero-Swirl Override Probe
**Target Definitions:** `gaugedSwirl` (Line 59) and `radialNormalize_anchor` (Line 55)
**Analysis:** 
The angular velocity/swirl profile is **not** a global zero or a static
constant by type constraint. The source proves only a zero at the specified
radial anchor via a mathematical gauge transformation.
* **Override (Line 55):** `radialNormalize_anchor (K : Point → ℝ) (t z : ℝ) : radialNormalize K (t, (1, z)) = 0`.
* **Mechanism:** The source defines `gaugedSwirl` (Line 59) as `radialNormalize (SlowBorelBase.swirlPotential...)`. This proves a zero value at the radial anchor `s = 1`.
* **Verdict:** The inspected theorem is a local gauge identity. It does not
  prove global zero swirl, zero helicity, or failure of the physical boundary
  equations. Those stronger claims are rejected unless a separate theorem is
  supplied.

## 3.   Definitional Tautology Verdict
**Target Definitions:** `finalPotential_smooth` (Line 443) and `potential_smooth` (Line 85)
**Analysis:** 
I traced the dependency link for the $C^{\infty}$ smoothness predicate. 
* **The Proof (Line 85):** `potential_smooth` invokes `AxisymmetricFields.contDiffOn_potential`, which rigorously composes the smoothness of the underlying `streamFactor` and `gaugedSwirl`. 
* **Tautology Check:** The source does **not** declare smoothness as an `opaque` mapping, nor assume it as an unproven axiom. The smoothness is legitimately built up from basic 1D and 2D smooth components in Lean's mathlib.
* **Verdict:** There is no tautological smoothness bypass in this module. The
  base field is genuinely $C^{\infty}$ smooth by construction. That fact is
  only one input to the later residual-limit construction; it does not prove
  the selected `VanishingJointJets` premise or the force endpoint by itself.

***
### Diagnostic Conclusion
The Base Profile Diagnostic confirms a smooth axisymmetric profile in reduced
coordinates, embedded into a three-component field and converted by spatial
curl. It also confirms a local radial-anchor gauge identity. It does not
establish a global swirl collapse or a physical boundary-layer violation.

The smoothness and curl construction are source-supported. The remaining
CTR-005 question is whether the paper's five-moment balances are transported
into the selected residual estimates. The pressure comparison interface also
needs an absolute semantic bridge. This note does not establish that the
endpoint is a physical phantom.

## Selected scalar-to-Cartesian boundary

The selected cycle's scalar mean profiles do satisfy the local `barMoment`
zero identities used by the correction invariant. The selected angular field
then multiplies that coefficient by the Cartesian angular frame; its component
one is explicitly exposed in `SelectedAngularComponentFormula.lean`. The
remaining question is whether the resulting atlas/curl field preserves the
same radial quantity, including axis and outer-tail terms. No nonzero
remainder is inferred from the base profile alone.

The radial-section completion now recovers the coefficient from the actual
selected angular field for positive radius. This confirms the next calculation
input while leaving the meridional curl, cutoff commutator, torus average,
axis, and outer-tail terms unresolved.

The axis boundary is no longer an uninspected definition: the review theorem
`SelectedRadialAxisBoundary.lean` proves the first selected direct angular
component is zero at (r=0). This does not evaluate the base profile's full
curl or establish a moment leak; it supplies one exact endpoint for the
remaining radial calculation.

The selected field calculation is two-branch rather than one-curl: the
potential sum is spatially curled and the direct angular sum is added after
that operation. A base-profile curl calculation alone cannot certify the
radial moment of the complete selected velocity.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.
