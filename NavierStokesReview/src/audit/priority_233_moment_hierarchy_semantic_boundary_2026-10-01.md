# Priority 233: moment hierarchy and semantic boundary

Date: 2026-10-01  
Status: source-checked against production declarations  
Disposition: deeper state-level moment transport established; final selected-field manuscript identity not established

## Purpose

This audit tests whether the previous Priority 232 result was too shallow by
searching for the moment mathematics under its structural roles rather than
only under the names `M`, `I`, `J`, `S`, and `C_p`.

The relevant question is not whether a public `Witness` record repeats a tuple
field. It is whether the production theorem graph carries the mathematical
dependencies implied by the manuscript: profile repair, radial integration,
torus averaging, pressure reconstruction, flux balance, and their connection
to the selected Cartesian field.

## Deeper production machinery found

| Layer | Production source | Established role |
|---|---|---|
| Radial integral calculus | `NavierStokes/IntegratedMeanBalances.lean:22-211` | Defines Bochner radial moments, weighted integrability, integration by parts, divergence identities, viscosity identities, and pressure moment reconstruction. |
| Parameter and torus operations | `NavierStokes/IntegratedMeanBalances.lean:237-520` | Defines radial moments of parameterised fields, differentiation under the integral, torus averages, and derivative/average identities. |
| State-to-mean identification | `NavierStokes/StateMomentBalances.lean:738-740` | Proves `CorrectionState.radialMoment` equals the radial moment of the averaged state field. |
| State residual balances | `NavierStokes/StateMomentBalances.lean:767-820, 956-1004` | Uses state moment premises to derive angular, axial, pressure, and flux identities for correction-state residuals. |
| Production import route | `NavierStokes/CorrectionInitialization.lean:1-15` and `NavierStokes/ActualPrimaryCoherence.lean:1` | Imports `IntegratedMeanBalances`, `StateMomentBalances`, rank, correction, and field-assembly machinery into the actual primary construction. |
| Cartesian assembly | `NavierStokes/ActualCandidateConstruction.lean:392-404, 464-502` and `ActualCandidateAssembly.lean:1079-1185` | Constructs chart-level potential/direct/pressure data and packages selected physical data, estimates, extensions, force, and consequences. |

This rules out the shallow claim that the code only contains disconnected
profile tuples. The production tree contains genuine intermediate observable
mathematics and state-level transport identities.

## What this deeper evidence does and does not establish

The state identity has the form

\[
  \operatorname{radialMoment}_{\mathrm{state}}(f,n,s)
  =
  \operatorname{radialMoment}_{\mathrm{averaged}}(f,n,s).
\]

The residual balance theorems then use these state-level moments to derive
identities for correction-state residual fields. This is materially stronger
than merely importing `FiveProfileMoments`.

It is still not the endpoint statement

\[
  \operatorname{Obs}_{\mathrm{paper}}
    (u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  = (M,I,J,S,C_p),
\]

where `u_selected` is the completed selected Cartesian field after the actual
potential/direct/pressure sums, curl/localisation, periodisation, averaging,
and the relevant limiting or support operations. The inspected declarations
continue to expose the intermediate state and radial identities separately;
the final selected-field observable identification remains absent from the
consumed production endpoint.

## Adjudication

| Proposition | Status | Reason |
|---|---|---|
| The repository contains only name-level or disconnected moment code | **Rejected** | `IntegratedMeanBalances`, `StateMomentBalances`, `CorrectionInitialization`, and the actual cycle route provide substantive connected intermediate mathematics. |
| The finite-stage repair and state-level radial balance engine is used in the production construction | **Established** | The imported declarations feed correction states, residual balances, physical data, estimates, and the selected Witness route. |
| State-level radial moment identities are equivalent to the final selected Cartesian manuscript observables | **Not established** | No consumed theorem with that completed semantic type was located. |
| The repair engine was bypassed wholesale | **Rejected** | The source graph shows actual use at the rank, invariant, state-balance, residual-rate, and estimate layers. |
| The final selected observable identity is false | **Not established** | No direct value-level mismatch or impossibility theorem has been proved. |

Therefore the correct controlled result remains:

> The repair engine is integrated into the selected production route through a
> nontrivial hierarchy of profile, rank, radial-balance, state, residual, and
> estimate declarations. The complete paper-to-endpoint identification of the
> final selected Cartesian observables with `(M,I,J,S,C_p)` remains
> unestablished. This is `CTR-005: NOT ESTABLISHED`, not a claim of wholesale
> bypass or concrete mismatch.

## Evidence links

- `../evidence/priority_233_moment_hierarchy_semantic_boundary_2026-10-01.json`
- `../evidence/priority_232_symbol_search_raw_2026-10-01.txt`
- `../src/completions/SelectedMixedProductionFullProductRule.lean`
- `../src/completions/SelectedMixedProductionBarMomentProductRule.lean`
- `../src/probes/SelectedBaseMomentCompatibilityProbe.lean`
- `../src/probes/SelectedWitnessPathProbe.lean`
