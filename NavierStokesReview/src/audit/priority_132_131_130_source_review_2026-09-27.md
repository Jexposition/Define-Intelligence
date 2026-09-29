# Priority 132/131/130 source review: initial exclusion, comparator predicates, heat tails, signed gain, cylindrical residuals

Date: 2026-09-27
Scope: six reachable OpenAI source modules selected from the live semantic register.
Method: direct inspection of source imports, definitions, structures, and theorem statements.
Status: tranche evidence only; 302 reachable modules remain open after registration.

## Executive result

This tranche supplies more positive evidence than a filename scan would show. The code defines formal comparator predicates, constructs actual initial excluded/Gaussian fields with support and jet bounds, proves parametric heat-tail regularity and limits, derives a signed mean-gain theorem, and proves the off-axis Cartesian/cylindrical residual identity.

The same inspection does not produce the endpoint bridge under audit. None of the six modules states a theorem transporting the final activated Cartesian `tsum` field through curl, localisation, and periodisation to the five paper observables \((M,I,J,S,C_p)\). None proves a concrete selected-field \(\Delta m\neq0\), an impossibility theorem, or kernel-level `False`.

## 1. `ActualInitialExcluded.lean`

Source anchors: `NavierStokes/ActualInitialExcluded.lean:299-411,666-718,728-758,1153-1199,1208-1371`.

`nativeApproach` packages a compact carrier, past, radial, and scale properties for the actual base-error approach (`:299-341`). `physical_error_eventual`, `physical_error_fixed`, `physical_error_jet_bound`, and the following prefix theorem provide actual error derivative bounds over slow-carrier points (`:346-411`).

The Gaussian section proves copied and periodised Gaussian uniform classes and support/zero-plateau facts (`:666-718,728-758`). The later `initialGaussian` field-sum section lifts per-label field classes to the initial Gaussian sum and derives unweighted classes (`:1153-1199`). Initial alias bounds are then derived from actual primary data (`:1208-1371`).

Audit result: this is concrete initial-stage field and rate infrastructure. It does not expose the final selected witness's five radial observables or a transport equality for them.

## 2. `ComparatorDefinitions.lean`

Source anchors: `NavierStokes/ComparatorDefinitions.lean:37-93,95-189,191-249`.

The module defines comparator divergence and proves its elementary zero/addition/scalar laws (`:37-93`). It defines initial-velocity conditions, force conditions, and their periodic/decay extensions (`:95-189`). The `NavierStokesExistenceAndSmoothness`, `NavierStokesExistenceAndSmoothnessRn`, and periodic structures package the comparator-side smoothness, divergence, initial data, force, and residual predicates (`:191-249`).

Audit result: these are formal comparator-side specifications. They clarify what the comparator theorem consumes but do not identify the selected construction with the paper's five radial moment tuple.

## 3. `ParametricHeatTail.lean`

Source anchors: `NavierStokes/ParametricHeatTail.lean:28-112,185-260,377-477,489-562,571-811,903-1062`.

The module proves integrability, continuity, differentiability, domination, and iterated-derivative results for parametric heat-tail chains (`:28-112`). It defines correction, square-correction, edit, weighted debt, and normalised debt jets with bounds (`:185-260,292-370,377-477`).

It defines physical pressure, energy, and angular functions and proves their smoothness, decay, derivative, and jet bounds (`:571-811`). It also proves outgoing and physical debt integrability, physical edit regularity, heat-carrier identities, and endpoint derivative results (`:903-1062`).

Audit result: this is substantive one-parameter tail/profile analysis. It does not prove that these scalar quantities are transported through the final Cartesian field construction or equal the selected field's global five-observable tuple.

## 4. `SignedMeanGain.lean`

Source anchors: `NavierStokes/SignedMeanGain.lean:24-111,168-244,286-337,382-434,920-970,1091-1190,1321-1360`.

The module defines signed covariance changes, wave-stage fields, pressure changes, torus-slice continuity, mean-bar operations, and local assembly structures. It proves local residual decompositions and an averaged residual decomposition (`:920-970`).

The `native_signed_mean_gain` theorem derives improved `MeanClass` exponents for theta and axial residuals and their actual torus means under explicit native assembly, support, operator, and defect hypotheses (`:1321-1352`). The source comment immediately states that the excluded Gaussian is retained and that the raw mean estimate does not set that field or its average to zero (`:1354-1360`).

Audit result: this is important intermediate mean/residual evidence and a warning against silently treating a mean estimate as a global zero invariant. It is not a theorem about the final selected `(M,I,J,S,C_p)` observables.

## 5. `CylindricalResidual.lean`

Source anchors: `NavierStokes/CylindricalResidual.lean:29-88,137-249,451-512,514-600`.

The module defines the off-axis cylindrical chart, frame, connection, Jacobian, and pullback derivative operators (`:29-88,137-249`). It defines `velocityComponents`, `pressurePullback`, and `cylindricalResidual` (`:451-460`).

`navierStokesResidual_cylindrical_of_slices` and `navierStokesResidual_cylindrical` prove the Cartesian residual identity in cylindrical coordinates under local C2/differentiability and positive-radius hypotheses (`:471-506`). It also proves cylindrical divergence and explicit radial, angular, axial advection and Laplacian component formulas (`:508-548`). `cylindricalResidual_congr` and `navierStokesResidual_of_representation` establish local-germ and representation transport (`:550-593`), while `navierStokesResidual_zero_iff` relates Cartesian and cylindrical zero residuals (`:595-607`).

Audit result: this is a genuine off-axis coordinate/residual bridge. Its positive-radius hypothesis confirms the chart scope boundary. It does not integrate the transformed field, evaluate radial moments, or bridge the final field to the paper tuple.

## 6. `HeatTailHistoryLimits.lean`

Source anchors: `NavierStokes/HeatTailHistoryLimits.lean:343-443,466-573,709-729`.

The module proves integrability and history formulas for angular and energy quantities, including future-tail and power-tail decompositions (`:343-443`). It derives pressure formulas and parameter-germ results (`:466-573`). `actual_history_limits` proves the relevant angular, energy, pressure, derivative, and tail terms tend to zero as the outgoing coordinate tends to infinity (`:709-729`).

Audit result: these are exact one-dimensional outgoing-tail formulas and limits. They are valuable upstream evidence, but they are not a theorem about the final Cartesian `tsum` field after localisation and periodisation.

## Cross-module classification

| Question | Result |
|---|---|
| Is there real mathematics in this tranche? | Yes: comparator structures, initial/Gaussian fields, heat-tail estimates, signed mean gain, cylindrical residual identities, and history limits. |
| Is the off-axis coordinate restriction explicit? | Yes. Cylindrical residual theorems require positive radius. |
| Is a global selected-field five-moment transport theorem present? | Not in the inspected declarations. |
| Is a concrete selected-field \(\Delta m\neq0\) proved? | No. |
| Is endpoint `False` proved? | No. |

## Register action

These six path-qualified modules are registered as `evidence_inspected` in `semantic_coverage_register.py`. The authoritative JSON, Markdown, and HTML registers must be regenerated from the hardened source map after this tranche, then mirrored to `docs/REPOSITORY_SEMANTIC_COVERAGE_REGISTER.{md,html}`.
