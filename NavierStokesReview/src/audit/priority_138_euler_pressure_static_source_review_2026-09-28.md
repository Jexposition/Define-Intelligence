# Priority 138: Euler pressure, static-solution, and graph reconstruction review

**Status:** direct source review completed for five current Lean modules. This
is a bounded semantic review, not a claim that the Euler branch is complete.

## Scope and dependency accounting

The reviewed files are:

| File | Direct imports | Direct source anchors | Known source dependents |
|---|---|---|---|
| `Euler/StaticEulerSolution.lean` | `Euler.StaticEulerCorrection`, `Euler.ConstantEulerGraph`, `Euler.EulerTimeRescaling`, `Euler.LpSmoothFieldAlgebra`, `Euler.PacketFieldGraphBounds` | `localVelocity` 24, `localForce` 32, `localMomentum` 60, `localVelocity_divergence` 78, `localVelocity_smooth` 158 | `Euler.StaticEulerParity`, `Euler.StaticEulerRegularity` |
| `Euler/AllOrderDriftPressure.lean` | `Euler.AllOrderDriftFinite`, `Euler.CorrectionAssemblyPressureParity` | `Budget.commonPressure` 20, `pressureTower` 37, `pointPressure` 56, `normalizedGraphPotential` 95, `exists_normalized_pressure` 157 | `Euler.AllOrderDriftEquation`, `Euler.CorrectionAssemblySourceTower`, `Euler.PacketPhysicalCorrectionPotential` |
| `Euler/CorrectionAssemblyPressureParity.lean` | `Euler.CorrectionAssemblyParity`, `Euler.CorrectionAssemblyReconstruction` | `cylinderGraph_neg` 13, `pointPressure_odd` 43, `normalizedGraphPotential_even` 62, uniqueness 71 | `Euler.AllOrderDriftPressure` |
| `Euler/CorrectionAssemblyReconstruction.lean` | `Euler.CorrectionAssemblyPressure`, `Euler.CanonicalGraphPotential`, `Euler.CommonPressureRepresentative` | `pointPressure` 21, `pointPressure_smooth` 41, `graphPressure_has_potential` 64, `normalizedGraphPotential_gradient` 96 | `Euler.CorrectionAssemblyPressureParity`, `Euler.CorrectionAssemblyTime` |
| `Euler/ExactLiftedGraphPressure.lean` | `Euler.ExactLiftedJointDifferentiability`, `Euler.CanonicalGraphPotential`, `Euler.CommonPressureRepresentative`, `Euler.GraphDivergence` | `graphPressure` 20, `graphPressure_has_potential` 29, `graphPotential_gradient` 52, `graphVelocity_divergence` 75 | `Euler.ConstantEulerGraph`, `Euler.PacketExactPhysicalMomentum`, `Euler.PacketExactPressureError`, `Euler.PacketForwardExactFields` |

The dependent-module names above are direct import dependents from the current
source map, not guesses about theorem usage. Declaration-level use still
requires the Lean environment export.

## What the source actually proves

`StaticEulerSolution` constructs a rescaled local Euler field from an exact
packet. `localMomentum` proves zero momentum residual only on the open interval
`0 < t < amplitude`; `localVelocity_divergence` proves the spatial divergence
identity, and the later declarations prove continuity and smooth spatial
regularity. The force is an explicitly rescaled field obtained from the exact
packet's force (`localForce`, lines 32-35), not a theorem about the
Navier--Stokes selected endpoint.

The two reconstruction modules provide genuine pressure mathematics. They
construct a common lifted (L^2) pressure, a pointwise representative, a graph
restriction, and a radial scalar potential. The source proves smoothness,
normalisation at the origin, gradient recovery, parity, and uniqueness under
the stated graph hypotheses. `ExactLiftedGraphPressure` also proves a graph
velocity divergence identity. These are real intermediate Euler constructions,
not empty wrappers.

## Boundary tests against the Navier--Stokes audit

The five files contain no declaration named `selected_witness`,
`CandidateProperties`, `NavierStokesR3`, `barMoment`, `FiveRows`, or a theorem
whose result is a selected Navier--Stokes Cartesian field. They do not state a
global
\[
\operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p)
\]
transport identity, nor do they prove that a pressure representative is the
absolute whole-space Navier--Stokes Poisson pressure used by the CMI endpoint.

The correct classification is therefore:

1. **Positive:** genuine Euler local momentum, divergence, pressure-potential,
   parity, and regularity results are present.
2. **Scope:** these results belong to the Euler packet/graph architecture and
   are not evidence for or against the Navier--Stokes selected-witness bridge.
3. **Open:** declaration-level use and full Euler endpoint closure still need
   the environment dependency export and direct review of the remaining Euler
   modules.
4. **No escalation:** this tranche yields no nonzero moment defect,
   impossibility theorem, `sorry`-based conclusion, or kernel-level `False`.

This review corrects both possible overclaims: it does not dismiss the Euler
pressure construction as dead code, and it does not promote a graph pressure
potential into a global CMI Navier--Stokes pressure theorem.
