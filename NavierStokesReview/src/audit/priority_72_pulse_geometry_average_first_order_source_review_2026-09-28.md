# Priority 72 source review: pulse amplitude, primary geometry, time averages, and first-order edge

Date: 2026-09-28
Scope: direct source inspection of four reachable modules in the OpenAI tree.
Purpose: classify the exact mathematical content and test whether this tranche supplies the selected-field Cartesian five-observable bridge.

## Source evidence

### `NavierStokes/CorrectedPulseAmplitude.lean`

- Lines 1-2 import `PulseAmplitude` and `ResetEnergyBounds`.
- Lines 21-64 define the corrected energy integrand, total energy, energy shift, constant term, and energy polynomial.
- Lines 404-422 prove `amplitude_spec`: smoothness, amplitude bounds, zero corrected total energy, derivative bounds, and uniqueness of the amplitude root within a prescribed interval.
- Lines 424-464 prove `exists_corrected_amplitude`.  In particular, lines 435-437 state integrability of the declared radial energy integrand and that its integral over `Ioi 0` is zero.

This is a substantive corrected-angular energy identity.  It is not a theorem about the final Cartesian `selected_witness`, `torusAverage`, `barMoment`, or the five paper observables `(M,I,J,S,C_p)`.  The zero integral is an energy-reset statement, not evidence that the full five-moment tuple has been transported.

### `NavierStokes/PrimaryGeometryAssembly.lean`

- Lines 1-2 import `FinalSlowBase` and `BaseChartJets`.
- Lines 29-198 define open cells, cell domains, representatives, carriers, and native jet support.
- Lines 225-239 define frequency, axial, leading frequency, leading axial, and shear data.
- Lines 356-360 define the phase construction from family data and geometric hypotheses.
- Lines 364-391 prove majorant and cone-order facts.
- Lines 498-550 identify the construction's frequency, axial, viscosity, length, slot, lambda, ratio, transverse direction, and angular mode; lines 547-550 retain the carrier-times-phase-to-integer-mode identity.
- Lines 561-595 prove common geometric bounds, normalized-stress target identification, and frequency/axial equalities to `FinalSlowBase.velocity`.

This module is a geometry and parameter-binding layer.  It supplies reduced chart/frequency/stress identities but no radial-observable evaluator, no `barMoment` theorem, no `torusAverage` theorem, and no endpoint `Witness` transport.

### `NavierStokes/R3/ComparisonTimeAverages.lean`

- Lines 1-3 import finite-energy comparison and measure-theoretic integral tools.
- Lines 25-134 define and analyse the time-average operator, including integrability and exchange of time and space integrals.
- Lines 274-293 prove `timeAverage_memLp_two_of_uniformFiniteEnergy` and the corresponding averaged-difference result.
- Lines 295-344 prove componentwise spatial square-integrability bounds for a velocity and a difference field.
- Lines 346-368 prove continuity and integrability of nonlinear tensor-difference components.
- Later declarations continue the same finite-energy/time-average comparison layer, including complex pairings.

This module establishes analytic comparison estimates from uniform finite energy.  It does not identify the selected field's radial profiles or moments and does not connect time averaging to the paper's five cumulative observables.

### `NavierStokes/SlowFirstOrderEdge.lean`

- Line 1 imports `TerminalEdgeFactor`.
- Lines 21-141 define the first-order taper/source/stress factors and prove smoothness/factorisation.
- Lines 128-219 define `radialSource`, `radialStress`, `profileStress`, their primitive representation, factorisation, and integrability/regularity facts.
- Lines 625-661 prove scaled physical-stress identities under positive-radius and pre-singular-time hypotheses.
- Lines 663-670 explicitly state that “Global moment closure is supplied by the separate renormalized-moment and slow-order moment theorems” and prove `forward_eq_physicalStress` from hypotheses `hi`, `hzero`, and exterior agreement `hmatch`.
- The `hzero` premise at lines 667-668 is the scalar weighted condition
  `∫ u in Ioi 0, u ^ 2 * F u = 0`.
- Lines 703-725 prove weighted integrability for the physical source.
- Lines 739-751 prove the analogous forward/radial-stress equality under a weighted-zero premise.

This is the strongest bridge-like content in this tranche, but it is still a reduced radial-stress result.  It is conditional on a scalar weighted closure and exterior agreement.  It does not identify the complete five-observable tuple with the fully activated Cartesian field after curl, localization, periodization, and `tsum`, and it does not mention `Witness`, `selected_witness`, `torusAverage`, or `barMoment`.

## Correspondence classification

| Module | Verified source role | Selected-field five-observable transport? | Defect/refutation result? |
|---|---|---:|---:|
| `CorrectedPulseAmplitude.lean` | Corrected angular energy and radial energy reset | No | No |
| `PrimaryGeometryAssembly.lean` | Reduced geometry, phase, frequency, axial, shear, chart binding | No | No |
| `R3/ComparisonTimeAverages.lean` | Finite-energy time averages and tensor integrability | No | No |
| `SlowFirstOrderEdge.lean` | Conditional reduced radial stress closure and scaling | No final-field bridge in this module | No |

## Calibrated finding

This tranche confirms additional genuine reduced mathematics and one explicit reference to separate global renormalized-moment theorems.  It therefore does **not** justify the claim that all moment closure is absent from the repository.  It also does not supply the missing endpoint theorem.  The current status remains:

`CTR-005`: selected-field Cartesian five-observable transport is not established in the inspected source.
`Delta m != 0`: not shown.
Transport impossibility: not shown.
Kernel-level `False`: not shown.

The register and control documents must retain the distinction between reduced radial closure and endpoint Cartesian transport.
