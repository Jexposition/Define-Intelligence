# Priority-97 Source Review: Local Cartesian Curl and Reduced Moment Bridges

Date: 2026-09-28

This tranche corrects a potentially overbroad audit formulation. The source does contain genuine local Cartesian-curl identities and reduced profile-to-moment/chart identities. The remaining issue is not “no curl bridge exists”; it is whether those bridges compose through the selected global assembly and endpoint observable interface.

## Scope

Reviewed:

- `NavierStokes/ActivationContinuation.lean`
- `NavierStokes/ActualMeanPotentialRealization.lean`
- `NavierStokes/CurlClassBounds.lean`
- `NavierStokes/SmoothFourierData.lean`
- `NavierStokes/FourierAlias.lean`
- `NavierStokes/MixedAxisPreservation.lean`
- `NavierStokes/NaturalCore.lean`
- `NavierStokes/ActivationHolomorphic.lean`
- `NavierStokes/ActualWaveRegularityData.lean`
- `NavierStokes/NominalConeAssembly.lean`
- `NavierStokes/TailGaugePotential.lean`

## Positive source evidence

### Local Cartesian curl realization

`ActualMeanPotentialRealization.lean` defines the scaled graph, component potential, and Cartesian potential. Its source proves:

- `componentPotential_realCurl`: the real Cartesian curl retains the cylindrical connection term and equals the meridional velocity on the valid positive-radius graph;
- `cartesianPotential_curl_forward`: the spatial curl of the Cartesian potential agrees with the polar velocity map on the valid cylindrical domain;
- `coherent_angularField_curl`: the same curl identity is propagated to coherent physical mean fields through a germ/coherence argument.

These are substantive local field-level realization theorems. They invalidate any blanket statement that the repository has no potential-to-Cartesian-curl bridge.

`TailGaugePotential.lean` is stronger within its own scope. It defines an anchored/gauged summed swirl potential and proves `spatialCurl_potential`, including the spatial axis, as well as `finalPotential_sameCurl` for the final slow-base potential. It also proves identification with the heat-exterior potential on the stated exterior hypotheses.

### Reduced profile and moment/chart identities

`NominalConeAssembly.lean` proves:

- `history_eq_moment`, expressing reduced profile histories through `NominalProfile.moments`;
- `moments_eq_profile_moments`, identifying the witness profile moments;
- logarithmic chart identities for outgoing `M` and `J` and heated `I`, `J`, and `S` moment components.

Thus the repository contains real reduced/chart-level moment transport. These declarations concern reduced profiles, logarithmic charts, and heat/outgoing stages. They are not yet the complete theorem that evaluates the final selected Cartesian field after all selected-stage assembly, cutoffs, periodisation, and endpoint packaging.

### Activation, core, Fourier, and wave layers

`ActivationContinuation.lean` supplies relaxed shear/projection/transverse coordinates, hold models, stock/field jets, density histories, and transfer bounds. `ActivationHolomorphic.lean` supplies smooth/holomorphic parameter families, continuation, controlled activation, averages, primitives, and real/complex regularity. `NaturalCore.lean` supplies reduced core values, regularity, and speed-unboundedness. `SmoothFourierData.lean` and `FourierAlias.lean` provide Fourier-side smoothness and conversion infrastructure. `MixedAxisPreservation.lean`, `CurlClassBounds.lean`, and `ActualWaveRegularityData.lean` provide axis, curl-rate, wave support, zero-germ, phase, deck, and `tsum`-zero facts.

These are real contributing layers. Their reviewed declarations do not expose the final five-observable equality at `ActualCandidateAssembly.Witness`.

## Corrected correspondence statement

The evidence now supports the following distinction:

```text
reduced profile moments
    -> logarithmic/chart moment identities                 proved in NominalConeAssembly
    -> local Cartesian potential/curl realization          proved in ActualMeanPotentialRealization
    -> anchored summed potential curl                     proved in TailGaugePotential
    -> selected wave/stage sums, spacetime localisation,
       periodisation, endpoint barMoment/Witness equality  not established by this tranche
```

The last arrow remains the load-bearing audit target. The existence of the preceding arrows means the prior stronger wording “curl transport is absent” must be retired. The narrower claim “the complete selected-field observable transport has not been located or proved at the endpoint” remains supported by the inspected declarations and the `Witness` type boundary.

## Status

- `CTR-005`: remains **not established**, now with a narrower formulation. The repository has local/reduced bridges; the inspected endpoint still does not expose the complete composed selected-field observable theorem.
- `CTR-012`: unchanged. This tranche does not decide force provenance.
- `AX-029/AX-030`: unchanged. Local potential/curl identities do not supply absolute global pressure-Poisson semantics.
- `FORMALLY REFUTED`: not triggered. No concrete `Delta m != 0`, impossibility theorem, or kernel `False` was proved.

## Register action

The eleven path-qualified evidence records from this review are added to `semantic_coverage_register.py`. The generated JSON/Markdown/HTML registers and their public `docs/` mirrors must be regenerated from the hardened source map.
