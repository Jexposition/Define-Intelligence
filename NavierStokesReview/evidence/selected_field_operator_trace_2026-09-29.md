# Direct selected-field operator trace

Date: 2026-09-29
Status: raw-source audit evidence; not a global absence or impossibility proof.

## Scope

This report rechecks the selected-field operator route directly in the
production Lean source. It does not treat the existing audit reports as
evidence, and it does not infer a moment defect from a missing result field.

## Source trace

### Infinite potential sum and spatial curl

`NavierStokes/SolenoidalDiagonal.lean:31-42` defines

```lean
def cutStage (a : ℕ → ℝ) (q : X → ℝ) (A : ℕ → X → V) (j : ℕ) (x : X) : V :=
  SmoothCutoffs.scaledCutoff (a j) (q x) • A j x

def potentialSum (a : ℕ → ℝ) (q : X → ℝ) (A : ℕ → X → V) (x : X) : V :=
  ∑' j : ℕ, cutStage a q A j x
```

The local-finiteness theorem at `:56-67` identifies the sum with a finite
prefix near a point when `q x > 0`. It does not by itself evaluate a weighted
radial integral of the infinite sum.

`NavierStokes/SolenoidalDiagonal.lean:186-190` then defines

```lean
def velocitySum (a : ℕ → ℝ) (q : SpaceTime → ℝ) (A : ℕ → VelocityField) :
    VelocityField :=
  SpatialCurl.spatialCurl (potentialSum a q A)
```

The divergence theorem at `:208-222` proves incompressibility from the
regularity of the summed potential. This is a genuine selected construction
route, not an empty interface.

### Selected endpoint fields

`NavierStokes/ActualCandidateAssembly.lean:1121-1151` defines the proposition
`Witness`. Its local `ASum`, `BSum`, and `PSum` are the three `potentialSum`
terms at `:1125-1130`. The candidate fields supplied to the endpoint are

```lean
TimeLocalization.activatedVelocity
  (MixedPeriodicAssembly.periodicVelocity ASum BSum)

TimeLocalization.activatedPressure
  (SpatialLocalization.periodicPressure PSum)
```

at `:1134-1141`. The proposition also packages smooth extensions,
`CandidateProperties`, `CandidateConsequences`, the H³ limit, force decay,
and boundary limits. `:1177-1181` merely specialises this proposition to the
selected budget and threshold.

### Cutoff, commutator, and periodisation

`NavierStokes/SpatialLocalization.lean:164-173` defines the spatial cutoff
before the curl:

```lean
def cutPotential (A : VelocityField) : VelocityField :=
  fun z => spatialCutoff z.2 • A z

def cutVelocity (A : VelocityField) : VelocityField :=
  SpatialCurl.spatialCurl (cutPotential A)
```

The exact product rule at `:199-207` is

```lean
cutVelocity A (t, x) = spatialCutoff x • SpatialCurl.spatialCurl A (t, x) +
  SpatialCurl.curlLinear ((fderiv ℝ spatialCutoff x).smulRight (A (t, x)))
```

Thus the cutoff-gradient contribution is formally present. Its presence does
not determine the value of any global moment: an integrated cancellation
would still have to be proved or disproved.

`SpatialLocalization.lean:209-214` defines `periodicPotential` by
periodising `cutPotential`, and `periodicVelocity` as the spatial curl of that
periodised potential. `MixedPeriodicAssembly.lean:336-365` constructs the
force from these mixed periodic fields and the residual-limit hypotheses.

### Observable type boundary

`NavierStokes/DefectIncrementBounds.lean:214-220` defines `barMoment` through
`CorrectionState.radialMoment`, with the displayed application formula

```lean
barMoment k f n p =
  ∫ r, r ^ k * PressureStream.torusAverage (f n) (r, p)
```

Here `f` has type `ScalarField (Point P)`. This is not definitionally the
activated Cartesian `VelocityField` in `Witness`. A selected-field theorem
would therefore need to supply the scalar lift, the pullback, the component
identification, the support/integrability facts, and the equality to the named
paper observable.

## Adjudication

The direct source establishes all of the following:

1. The selected endpoint contains a real infinite potential sum and a real
   curl/localisation/periodisation/time-activation pipeline.
2. The spatial cutoff commutator is explicit in the Lean source.
3. The exported `Witness` packages the resulting candidate fields and their
   PDE/regularity consequences.
4. `barMoment` is a separate scalar pressure-stream observable interface, not
   an automatic projection of the final velocity field.

The direct source does **not** establish either of these stronger claims:

- that the selected Cartesian field has a nonzero five-moment defect;
- that no theorem elsewhere transports the named profile quantities into the
  selected field.

The correct remaining question is a value-level composition theorem of the
form

\[
  (M,I,J,S,C_p)_{\mathrm{paper}}
  =
  \mathcal O(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}}),
\]

where `\mathcal O` includes the actual sum, curl, cutoff, periodisation,
torus average, scalar pullback, radial integral, and axis/whole-space
extension. This report narrows that task; it does not decide it by omission.
