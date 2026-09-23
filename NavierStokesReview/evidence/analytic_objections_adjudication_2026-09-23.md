# Analytic-objection adjudication

**Date:** 2026-09-23  
**Scope:** selected R3 endpoint and the proposed incompressibility, energy, pressure, and temporal-gluing objections.

## Verdict

The proposed objections do not yet produce a formal disproof. Source inspection instead separates one closed attack from three live audit lanes:

| Objection | Source finding | Review status |
|---|---|---|
| Raw-stage divergence | `selectedPotentialStages` are intermediate potentials. The final velocity is assembled by the solenoidal diagonal, and `divergence_velocitySum_on` proves its divergence is zero. | Closed as stated; it targets the wrong field. |
| Energy mismatch | `ViscousEnergyBalance` proves the exact forced identity, and the selected endpoint exposes uniform finite energy. | No mismatch established; selected instantiation remains required. |
| Compact pressure / non-locality | `ActualCandidate` explicitly localises the pressure and proves compact slice support. This is a serious correspondence and PDE-consistency question, but arbitrary CMI forcing does not itself require zero divergence or zero spatial integral. | Live conditional objection, not a contradiction yet. |
| Temporal gluing | `CandidateFromLimits` supplies a smooth extension, endpoint jets, and residual equality before the singular time. | Live dependency audit: trace the concrete residual limits and joint-jet vanishing premises. |
| Filter degeneration | `JetRate` has no generic `NeBot` parameter, but the selected endpoint filter has the explicit theorem `past_filter_neBot`. | Generic hazard remains; selected-endpoint vacuity is not shown. |

## What is actually established

The zero-sorry probes establish source-level facts rather than merely reading names:

1. `SelectedDivergenceAudit.lean` extracts `CandidateProperties.divergence_free` from the selected endpoint.
2. `AnalyticObjectionsProbe.lean` extracts the selected pressure-support, finite-energy, and force-smoothness fields.
3. `ViscousEnergyBalance.energy_balance_viscosity` states the Newtonian forced energy identity with the work term and viscous dissipation.
4. `CandidateFromLimits.force_smooth` and `force_boundary_jets` show that the gluing interface is designed to be smooth; they do not, without the upstream limit proofs, independently establish those limits.
5. `FilterNonVacuityAudit.lean` proves that the selected residual-limit filter is non-vacuous.

## Pressure objection: precise form

The compact pressure support is not a fabricated grep finding. `SpatialLocalization.cutPressure` multiplies the pressure by a spatial cutoff, and `R3CompactCandidate.localized_pressure_tsupport` carries that support into the selected candidate. The correct objection is therefore:

> Identify the theorem that relates this localised pressure to the whole-space pressure equation required by the paper, including its non-local tail, and show that the relation is incompatible with the selected velocity and force.

The weaker statement “pressure in incompressible flow is non-local, therefore compact pressure is impossible” is insufficient here. With an arbitrary external force, the pressure gradient and force are coupled in the momentum residual. A decisive contradiction needs an explicit pressure Poisson/Leray identity, an independently specified force constraint, or a proved decay/moment theorem that the selected fields violate.

The source scan also found substantive pressure infrastructure rather than an empty placeholder: `ConservativeDifference.weak_pressure_poisson`, `PressureRecoveryHelpers.gradient_poisson_test`, `PressureRecovery.pressure_gradient_recovery`, and the Riesz test-operator identities. These are compact-test or comparison-level results with explicit hypotheses. The unresolved issue is whether the selected compact pressure is connected to them on the selected endpoint path. Their existence prevents the stronger claim that the repository contains no pressure analysis; their non-use or failed instantiation could still establish a correspondence gap.

## Energy objection: precise form

The repository does not simply omit viscous dissipation. Its source contains an exact identity of the form

\[
\frac{d}{dt}\int |u|^2
=-2\nu\int |\nabla u|^2+2\int u\cdot f.
\]

The review must therefore test the hypotheses on the selected endpoint and compare the actual `energyRate`, `dissipation`, and forcing-work terms. Until that instantiation fails, “the five-row debt truncates dissipation” is an unproved allegation.

## Temporal-gluing objection: precise form

The source uses a smooth extension with prescribed boundary jets rather than a raw `if` or stage switch. The credible audit target is upstream: determine whether the selected residual estimates really imply the local uniform limits and vanishing joint jets consumed by the extension. If that dependency is missing, the failure is a hidden analytic premise. If it is present, a generic “temporal kink” objection is false.

## Next formal tests

1. Trace `PeriodicResidualLimits.exists_candidate_force` to the selected cycle and record every premise used for `hlim` and endpoint jets.
2. Search for a pressure Poisson or Leray theorem connecting the localised pressure to the selected velocity.
3. Instantiate the exact energy identity on the selected endpoint, or record the precise type mismatch preventing instantiation.
4. Audit any restriction or comap filter introduced after the selected endpoint filter, rather than extrapolating from the generic `JetRate` API.

This evidence is deliberately classified as **not a completed refutation**. It narrows the search to claims that can still be falsified by source-linked Lean obligations.
