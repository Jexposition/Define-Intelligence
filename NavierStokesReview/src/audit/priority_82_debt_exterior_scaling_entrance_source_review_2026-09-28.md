# Priority 82 source review: actual debt, exterior support, R³ scaling, and entrance flux

Date: 2026-09-28
Scope: direct source review of the next six reachable modules selected from the live semantic register.

## Reviewed source

1. `NavierStokes/ActualIntermediateDebtBounds.lean`
2. `NavierStokes/ActualMeanExterior.lean`
3. `NavierStokes/R3/SpatialEnergyScaling.lean`
4. `NavierStokes/R3/SpatialSupportScaling.lean`
5. `NavierStokes/R3ActualCandidate.lean`
6. `NavierStokes/NaturalEntrance.lean`

## Findings

### `ActualIntermediateDebtBounds.lean`

`stage_debt_bounds` (approximately lines 68–75) proves componentwise `UnweightedClass` bounds for both the signed and temporal intermediate debts. `stage_debt_from_stepData` (approximately lines 136–170) derives those bounds from actual correction-step data, including covariance and temporal increment hypotheses. `afterTemporal_debt_from_stepData` (approximately lines 172–177) packages the three-component slow source.

This is a concrete intermediate rank/debt bridge. It corrects any claim that the active construction carries no physical debt information. Its scope is three-component intermediate data; the reviewed declarations do not identify it with the complete five paper observables or transport it into the selected Cartesian `Witness`.

### `ActualMeanExterior.lean`

`active_of_mem_tsupport` and `not_mem_tsupport_of_exterior` (approximately lines 22–71) establish that the actual moving support lies in the nominal active annulus. `exterior_zero_germs` and `exterior_zero` (approximately lines 73–104) give germ and pointwise exterior vanishing. The initial and cycle declarations (approximately lines 121–230) propagate the same result to angular, pressure, temporal, rank, stream, increment, and cycle families.

This is positive localisation and exterior-matching evidence. It does not state a global radial observable equality for the final assembled Cartesian field.

### `R3/SpatialEnergyScaling.lean`

`kineticEnergy_spatial_smul` (approximately lines 25–36) proves the exact factor

\[
E[a\,u(t,bx)] = \lVert a\rVert^2\, |(b^3)^{-1}|\,E[u](t),
\]

and `UniformFiniteEnergy.spatial_smul` (approximately lines 38–48) transports a uniform finite-energy bound. This is a genuine whole-space analytic scaling result, not a moment theorem.

### `R3/SpatialSupportScaling.lean`

`isCompact_spatialScale_image` and `tsupport_spatialScale_subset` (approximately lines 15–32) prove compact-support transport under a nonzero spatial dilation. `CompactPositiveTimeSupport.spatialScale` (approximately lines 34–57) transports compact positive-time force support. These results strengthen the R³ support record but contain no five-observable transport premise or conclusion.

### `R3ActualCandidate.lean`

`selected_compact_candidate` (lines 17–21) destructs `ActualCandidateAssembly.selected_witness` and applies `R3CompactCandidate.of_localized_fields` to produce an existential compact whole-space candidate. This is a real packaging path using the concrete assembled fields. The exported type is `Properties`; the reviewed wrapper adds no equality identifying the final field with `(M,I,J,S,C_p)`.

### `NaturalEntrance.lean`

The module constructs natural entrance profiles and retains a coefficient-space witness. `angular_flux_integral` and `axial_flux_integral` (approximately lines 1186–1227) are exact interval-integral identities. `angular_source_integral` (approximately lines 1235–1278), `Sn_eq_radial` (approximately lines 1291–1297), and `axial_source_integral` (approximately lines 1299–1303) connect the constructed source terms to reduced radial derivatives and boundary values.

These are substantive reduced PDE and entrance-coordinate identities. They materially strengthen the positive side of the audit. They do not, in the inspected declarations, compose with the final Cartesian curl, spatial localisation, infinite `tsum`, periodisation, torus averaging, and public `Witness` into the complete paper tuple.

## Correspondence result

Priority 82 adds positive evidence at four distinct layers:

- actual three-component debt is derived from checked correction data;
- exterior annular support and vanishing are proved for actual mean/cycle families;
- R³ energy and support transformations are exact;
- the selected witness is wrapped into a compact whole-space candidate;
- reduced entrance flux identities are proved exactly.

The audit must therefore not say that the repository is moment-free, that the endpoint is only a generic zero-field interface, or that the R³ candidate wrapper is absent. The remaining issue is narrower: the reviewed declarations still do not provide the complete selected-field theorem

\[
\operatorname{Obs}_{\mathrm{radial}}
\bigl(\operatorname{periodise}(\nabla\!\times(\operatorname{tsum}(A_j))\;\text{with localisation})\bigr)
= (M,I,J,S,C_p)
\]

with the exact paper semantics and public `Witness` transport.

This tranche does not prove a nonzero \(\Delta m\), an impossibility theorem, `False`, or a kernel-level refutation. The calibrated classification remains `CTR-005: selected endpoint correspondence not established`, pending the remaining reachable-module reviews and the value-level composition audit.
