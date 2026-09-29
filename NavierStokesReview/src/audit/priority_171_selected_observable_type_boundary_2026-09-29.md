# Priority 171: selected observable type boundary

Date: 2026-09-29
Status: source-bound P2 progress; no selected-field defect claimed.

## Question

Does the production Lean source identify the five paper observables with the
completed selected Cartesian field, rather than merely proving related
intermediate radial identities?

## Direct source trace

1. `NavierStokes/SolenoidalDiagonal.lean:31-42` defines each stage as a
   scaled cutoff potential and defines `potentialSum` as an actual `tsum`.
   `:56-67` proves local equality with a finite prefix on the positive-scale
   domain. This proves the local meaning of the sum, but not a weighted radial
   integral of its completed Cartesian curl.

2. `NavierStokes/ActualCandidateAssembly.lean:1121-1151` defines the endpoint
   proposition `Witness`. Its local `ASum`, `BSum`, and `PSum` are three
   `potentialSum` terms at `:1125-1130`. The selected fields are

   ```lean
   TimeLocalization.activatedVelocity
     (MixedPeriodicAssembly.periodicVelocity ASum BSum)
   TimeLocalization.activatedPressure
     (SpatialLocalization.periodicPressure PSum)
   ```

   at `:1134-1141`.

3. `NavierStokes/SpatialLocalization.lean:164-207` proves that localisation
   occurs before the spatial curl and exposes the cutoff-gradient commutator:

   ```lean
   cutVelocity A (t, x) =
     spatialCutoff x • SpatialCurl.spatialCurl A (t, x) +
     SpatialCurl.curlLinear
       ((fderiv ℝ spatialCutoff x).smulRight (A (t, x)))
   ```

   The commutator is therefore part of the selected operator, but its radial
   integral is neither automatically zero nor automatically nonzero.

4. `NavierStokes/SpatialLocalization.lean:209-217` defines the periodised
   potential and velocity, while `MixedPeriodicAssembly.lean:32-49` adds the
   periodised direct field and defines the residual. The final field is thus
   not definitionally the pre-curl profile field.

5. `NavierStokes/DefectIncrementBounds.lean:22-25,214-220` gives the type of
   the radial observable:

   ```lean
   abbrev Point (P : Type) := PressureStream.Lift P
   abbrev ScalarField (D : Type) := MeanIncrementBounds.Field D
   barMoment k f n p =
     ∫ r, r ^ k * PressureStream.torusAverage (f n) (r, p)
   ```

   Thus `barMoment` consumes a scalar field on a lifted pressure-stream
   domain. It is not definitionally a function of the endpoint's activated
   Cartesian `VelocityField`.

## Consequence

The source establishes a genuine operator chain

\[
  \text{profile stages}
  \to \operatorname{tsum}
  \to \text{cut potential}
  \to \nabla\times
  \to \text{periodisation}
  \to \text{mixed velocity}
  \to \text{time activation}.
\]

It also establishes genuine intermediate `barMoment`, `FiveRows`, debt, and
zero-mass identities. It does not, in the inspected declarations, establish
the additional representation theorem required to identify

\[
  \mathcal O(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  =(M,I,J,S,C_p),
\]

where \(\mathcal O\) includes the completed sum, curl, cutoff commutator,
periodisation, torus average, scalar/component pullback, radial integration,
support and integrability, and axis/endpoint extension.

This is a positive type/domain finding about the missing bridge. It is not a
proof that the selected observable is wrong, and it is not an impossibility
theorem. It narrows P2 to an explicit value-level representation search.

## Status update

- Concrete selected `tsum`/curl/localisation/periodisation route: established.
- Concrete invariant-backed residual-rate and smooth-force route: established.
- Direct selected Cartesian equality with the five paper observables: not
  established.
- Selected nonzero defect, force nonsmoothness, literal CMI failure, or Lean
  contradiction: not proved.

Reproducible source check:

```text
rg -n "potentialSum|periodicVelocity|activatedVelocity|barMoment" \
  NavierStokes/ActualCandidateAssembly.lean \
  NavierStokes/SolenoidalDiagonal.lean \
  NavierStokes/SpatialLocalization.lean \
  NavierStokes/MixedPeriodicAssembly.lean \
  NavierStokes/TimeLocalization.lean \
  NavierStokes/DefectIncrementBounds.lean
```
