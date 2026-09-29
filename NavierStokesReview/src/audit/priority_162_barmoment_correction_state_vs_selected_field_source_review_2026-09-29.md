# Priority 162: `barMoment` correction-state boundary versus selected field

Date: 2026-09-29

Status: direct declaration review; no nonzero selected-field defect claimed.

## Finding

The repository contains genuine `barMoment` and `FiveRowRank.FiveRows`
mathematics. The declarations inspected here prove exact radial integral
identities and preservation laws for correction-state mean fields. They do not,
in the inspected declarations, identify those quantities with the final
activated Cartesian velocity or pressure stored by `ActualCandidateAssembly.Witness`.

## Exact source boundary

### `DefectIncrementBounds.lean:214-220`

```lean
noncomputable def barMoment (k : ℕ) (f : ScalarField (Point P)) : ScalarField P :=
  CorrectionState.radialMoment k f

theorem barMoment_apply ... :
    barMoment k f n p = ∫ r, r ^ k * PressureStream.torusAverage (f n) (r, p)
```

This is a genuine torus-averaged radial moment of a scalar stage field. Its
domain is a scalar field indexed by a correction-state point, not the final
`VelocityField` assembled by `periodicVelocity` and activated by
`TimeLocalization`.

### `DefectIncrementBounds.lean:621-658`

`fiveRows_mass_zero` derives
`barMoment 2 h.angular = 0` and `barMoment 1 h.axial = 0` from a
`FiveRowRank.FiveRows` hypothesis on `slowSlice` fields. `fiveRows_preserve_masses`
then proves preservation under `updated m h`, and
`linearRows_eq_neg_of_fiveRows` identifies three linear `barMoment` rows with
the negative correction defects.

These are substantive correction-state theorems. They do not quantify over the
final mixed Cartesian field, its spatial curl, the infinite potential sum, the
periodised velocity, or the activated whole-space candidate.

### `StateMomentBalances.lean:956-978`

`axial_flux_pressure_moment` proves a radial-moment identity for
`axialAxialFlux c u + u.pressure` under shell, periodicity, pressure-recipe,
and pressure-defect hypotheses. It is a pressure/flux reconstruction identity
for a state, not an absolute pressure-Poisson identity for the selected
whole-space pressure.

### `CorrectionStep.lean:1469-1498`

The temporal correction preserves the radial moments of `u.mean.angular` and
`u.mean.axial` because the temporal increment has zero torus average. Again,
the theorem is about correction-state mean variables.

### `NominalProfile.lean:2078-2089;2108-2140`

`FiveMomentCertificate` is a real five-integral certificate for literal profile
fields `U` and `E`, including integrability, four zero identities, and the
pressure datum. `heated_five_moments` transports those profile identities to a
heated reduced profile. This confirms genuine reduced-profile mathematics,
not a dead-code shell.

## Adverse correspondence result

The source proves the following chain of increasingly concrete facts:

```text
profile U,E and pressure data
  -> reduced five-moment certificates
  -> correction-state barMoment / FiveRows identities
  -> physical stage residual and jet bounds
  -> mixed sums, periodisation, activation, force, Witness
```

The inspected declarations do not yet provide the final arrow in the stronger
semantic form needed for the published paper claim:

```text
barMoment / reduced (M,I,J,S,Cp)
  = the corresponding observable of the completed selected Cartesian field
```

A repository-wide name search found no declaration combining `barMoment` with
`periodicVelocity`, `activatedVelocity`, `activatedPressure`, `potentialSum`,
or `Witness` in one final observable-equality theorem.

This supports `CTR-005` as a paper-to-endpoint correspondence finding. It does
not prove that the final values are nonzero, that the selected force is not
smooth, or that the endpoint is false.

## Controlled conclusion

The correct description is neither “the moments are absent” nor “the final
Cartesian transport is verified”. The source contains real profile and
correction-state moment proofs, and it contains a separate concrete residual
and force construction. The final selected-field semantic identification
remains unclosed in the declarations inspected here.

