# Selected direct-prefix field identity

## Purpose

This record tests the live CTR-005 target against the actual selected stage
family. It is not a generic rate-contract test and it is not a numerical
substitute for the missing radial transport theorem.

## Source ledger

| Layer | Source | Result |
|---|---|---|
| Selected alias | NavierStokes/ActualCandidateAssembly.lean:1169-1172 | selectedDirectStages is the selected directStages family. |
| Stage identity | NavierStokes/ActualCandidateAssembly.lean:553-557 | Every direct stage is identified with ActualCandidateConstruction.angularMeanStages. |
| Native stage family | NavierStokes/ActualCandidateConstruction.lean:392-401 | Angular stages are mean fields of the cycle's native angular increments. |
| Prefix recurrence | NavierStokes/ActualCandidateConstruction.lean:419-427 | The uncut prefix through J equals the cycle-state mean angular field at J. |
| Cutoff transport | NavierStokes/DirectAngularDiagonal.lean:208-214,231-237 | Cutoffs multiply the angular field before the natural-indexed potentialSum. |
| Cartesian transport | NavierStokes/ActualMeanPotentialRealization.lean:29-40,167-184,245-251 | Meridional potential data are embedded and passed through a spatial curl on a positive-radius chart. |
| Radial moment | NavierStokes/DefectIncrementBounds.lean:214-220 | barMoment accepts a scalar radial-profile field and integrates its torus average. |

## Zero-sorry completion

NavierStokesReview/src/completions/SelectedDirectPrefixField.lean compiles
under Lean 4.34.0-rc2. It proves:

~~~lean
selectedDirectStages j =
  angularMeanStages selectedBudget selectedThreshold j
~~~

and, for every J,

~~~lean
uncutPrefix selectedDirectStages (J + 1) =
  meanAngularField selectedBudget selectedThreshold (CoordinateAlgebra.A h)
    (selectedCycle J).state.mean.angular
~~~

This is a concrete selected Cartesian-stage identity. It rules out describing
the direct family as an unconnected placeholder.

## Remaining calculation

The completion stops before barMoment for a type-correct reason. The proved
prefix is a VelocityField on spacetime; barMoment requires a scalar field on
Point P, followed by torus averaging. The source still supplies no selected
theorem for:

~~~text
selected Cartesian prefix
  -> cylindrical scalar profile
  -> torus average
  -> barMoment
~~~

Consequently no selected Delta m ≠ 0 is claimed. The remaining calculation
must retain cutoff derivatives, the positive-radius curl terms, and axis and
outer-support contributions before a nonzero remainder can be proved.

## Classification

This strengthens CTR-005 from a generic interface concern to a concrete
selected-field calculation gate. It does not by itself prove a selected-path
contradiction.
