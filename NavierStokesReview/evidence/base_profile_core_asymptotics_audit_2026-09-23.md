# Base-profile and core-asymptotics audit

Audit date: 2026-09-23  
Audited checkout: `Define-Intelligence-github`  
Lean probe: [`BaseProfileCoreAsymptoticsProbe.lean`](../src/probes/BaseProfileCoreAsymptoticsProbe.lean)  
Probe result: exit code 0 with no `sorry` declarations.

## Verdict

Agent 2 identified two real architectural review targets, but two formulations were too strong.

| ID | Finding | Status | Exact basis |
|---|---|---|---|
| BP-01 | The base potential is an axisymmetric, three-component Cartesian field generated from two scalar profiles. | Confirmed | `AxisymmetricFields.lean`, `TailGaugePotential.lean` |
| BP-02 | The selected base is not proved to have globally zero swirl. The gauge-normalisation theorem gives zero only on the radial anchor `s = 1`. | Confirmed correction | `TailGaugePotential.lean:26-61` |
| BP-03 | `GermCandidateAssembly` does not transport five-moment identities in its generic summation interface. | Confirmed interface gap | `GermCandidateAssembly.lean:1,75-115`; `MixedCandidateAssembly.lean:29-91` |
| BP-04 | The selected profile construction does contain a five-moment layer upstream through `NominalProfile` and `ModulatedProfileAssembly`. | Confirmed correction | `NominalProfile.lean:6,31,222-228`; `ModulatedProfileAssembly.lean:193,515` |
| BP-05 | Base smoothness is derived from smooth scalar coefficients and the axisymmetric potential theorem, not from the Navier–Stokes PDE. | Confirmed | `TailGaugePotential.lean:85-99,443-450` |
| BP-06 | The force smoothness construction is conditional on locally uniform limits of every residual derivative. | Confirmed interface obligation | `CandidateFromLimits.lean:28-48,83-87`; `MixedPeriodicAssembly.lean:338-368` |
| BP-07 | The `WholeDomain*` branch is not reachable from `ActualCandidateAssembly.selected_witness`. | Confirmed for selected endpoint | `ActualCandidateAssembly.lean:1-15,1153-1185`; WholeDomain imports below |

These are correspondence and dependency findings. This audit does not yet produce a zero-sorry contradiction to `selected_candidate`.

## 1. Geometric profile count

`AxisymmetricFields.potential` is a map into the full Cartesian `VelocityField` and has the component form

```text
(-(1/2) * x₁ * H(t,s,z)) • e₀
+ ( (1/2) * x₀ * H(t,s,z)) • e₁
+ K(t,s,z) • e₂
```

where `s = (x₀² + x₁²)/2`. The definition is in `NavierStokes/AxisymmetricFields.lean` near `potential`; `profilePoint`, `radialEnergy`, and `coordinateVector` make the coordinate map explicit. The two scalar profiles are `SlowBorelBase.streamFactor` and `SlowBorelBase.swirlPotential` at `SlowBorelBase.lean:1169-1174`.

`TailGaugePotential.finalPotential` is defined at `TailGaugePotential.lean:433-435` by applying that potential constructor to the selected slow-base scales and coefficients. `finalPotential_sameCurl` at `448-450` identifies its spatial curl with `FinalSlowBase.velocity` for `t < 1`.

Therefore the “cylindrical `Triple` placeholder” description is incomplete. The code does use an axisymmetric reduction, but it injects the profiles into all three Cartesian components and then takes a three-dimensional curl. Axisymmetry is a structural ansatz, not by itself a proof failure.

## 2. Angular-swirl firewall

The gauge definitions are:

```text
radialAnchor p    = (p.1, (1, p.2.2))
radialNormalize K p = K p - K (radialAnchor p)
gaugedSwirl       = radialNormalize SlowBorelBase.swirlPotential ...
```

They occur at `TailGaugePotential.lean:26-61`. The zero theorem
`radialNormalize_anchor` proves

```text
gaugedSwirl (t, (1, z)) = 0
```

on the anchor surface only. No theorem found in the selected path proves
`gaugedSwirl = 0` globally. The exact potential identity at
`TailGaugePotential.lean:437-441` subtracts an axial `coordinateVector 2` gauge term from `FinalSlowBase.vectorPotential`; it does not erase the radial or angular components of the resulting curl.

The component formulas in `AxisymmetricFields.velocity_zero`, `velocity_one`, and `velocity_two` show that the first two velocity components depend on derivatives of both scalar profiles. The selected axis statement is narrower: `FinalSlowBase.origin` at `FinalSlowBase.lean:361-370` gives a pure `coordinateVector 2` value at `x = 0`, and `axis_tendsto` at `372-374` proves blow-up of that axis norm. That is an axial-core statement, not a global no-swirl theorem.

## 3. Five-moment transport

The direct syntactic part of Agent 2’s claim is correct:

- `GermCandidateAssembly.lean:1` imports only `MixedCandidateWitness`.
- `GermCandidateAssembly.lean:75-96` proves an abstract germ identity for arbitrary `base`, `initial`, and `stages`.
- `GermCandidateAssembly.lean:103` defines `potentialStages` from `TailGaugePotential.finalPotential` and initialized stage data, but no moment vector appears in the germ identity.
- `MixedCandidateAssembly.StageEstimates` at `29-65` contains smoothness, scalar gains, losses, and jet-rate bounds, not a five-component physical-moment equality.
- `StageEstimates.exists_schedule` at `67-91` constructs the schedule and `VanishingJointJets` from those estimates.

The stronger statement that the selected endpoint never uses five-moment repair is not supported. The upstream selected profile construction reaches `NominalProfile`, whose `Debt` is an abbreviation of `FiveProfileMoments.Debt` and whose `resetCoefficients_equation` invokes `FiveProfileMoments.physicalMoments` (`NominalProfile.lean:6,31,222-228`). `ModulatedProfileAssembly` also exposes a `FiveProfileMoments.Patch` (`ModulatedProfileAssembly.lean:193,515`).

The defensible objection is therefore:

> The repository contains five-moment machinery upstream, but the generic summation and residual-estimate interface does not carry an explicit theorem that the selected summed velocity, pressure, and residual preserve the paper’s five identities.

This is a paper-to-code bridge failure candidate, not yet an internal Lean contradiction.

## 4. Smoothness and residual-limit interface

`finalPotential_smooth` at `TailGaugePotential.lean:443-446` calls `potential_smooth`, which in turn uses smoothness of the stream and swirl scalar profiles. It does not derive `C^∞` regularity from the Navier–Stokes equations. `finalPotential_sameCurl` is an algebraic curl realization theorem.

The force construction is different. `CandidateFromLimits.tracedResidual` is formed from the past residual and a boundary series; `tracedResidual_smooth` requires, as an explicit premise, locally uniform convergence of every iterated derivative of the actual `navierStokesResidual` (`CandidateFromLimits.lean:28-48`). `force_smooth` then follows from the smooth extension theorem (`83-87`).

In the selected construction, `MixedPeriodicAssembly.exists_candidate_force` receives `VanishingJointJets`, away-extension hypotheses, and the axis blow-up hypothesis (`MixedPeriodicAssembly.lean:338-368`). It constructs `hlim` using `boundaryLimits_locallyUniform` and passes it into `CandidateFromLimits.force`.

Thus the correct audit target is not “the smoothness theorem is an opaque axiom.” It is:

1. verify the selected `VanishingJointJets` theorem is for the exact selected residual;
2. verify its away-extension premises refer to the same selected pressure and velocity;
3. verify `boundaryLimits_locallyUniform` is not merely a generic consequence detached from the five-moment identities.

## 5. WholeDomain branch reachability

The selected endpoint imports `ActualCandidateConstruction`, `GermCandidateAssembly`, `ActualStageEstimates`, and related selected-stage files (`ActualCandidateAssembly.lean:1-15`). Its endpoint is assembled at `1153-1185`, where `selected_witness` calls the finite-stage witness and `selected_candidate` projects its force.

The `WholeDomain*` files form a separate chain. Examples:

- `WholeDomainHeatBounds` imports `WholeDomainHeatScaling` and `WholeDomainHeatCompact`.
- `WholeDomainBaseBounds` imports `WholeDomainHeatBounds` and `ActualBasePressureBounds`.
- `WholeDomainPhysicalStageTheorem` imports `WholeDomainBaseBounds`, `WholeDomainInitializationBounds`, and `WholeDomainPrefixBounds`.
- `ActualBasePressureBounds` imports `WholeDomainHeatBounds`.
- `PaperAdditionalResults` imports `WholeDomainPhysicalStageTheorem`.

No import from `ActualCandidateAssembly`, `ActualCandidateConstruction`, `GermCandidateAssembly`, `ActualStageEstimates`, or the selected witness reaches that branch. The precise finding is that the branch is not selected-endpoint reachable, although it is not globally unused because paper-result modules import it.

## 6. Review consequence

The strongest source-backed statement is now:

> The selected endpoint is a three-dimensional axisymmetric curl construction with an axial core blow-up. Its upstream profile data include genuine five-moment repair machinery, but the generic finite-stage-to-summed-field interface does not expose a selected-path theorem transporting those five physical moment identities into the final residual and force. The force smoothness theorem is conditional on full residual-jet limits supplied through `VanishingJointJets`; the base-profile smoothness itself is independent of the PDE.

This supports a major correspondence audit and a demand for bridge theorems. It does not justify claiming that the Lean kernel has already derived a contradiction or that the profile is globally swirl-free.
