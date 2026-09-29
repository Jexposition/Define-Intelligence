# Priority 73 source review: base velocity, representative geometry, and reserved patches

Date: 2026-09-28

This is a declaration-level source review of six reachable modules. It records what
the source proves and what it does not prove. The review does not infer a defect from
the existence of a cutoff, a curl, a reduced profile, or an imported moment module.

## ActualBaseVelocityBounds.lean

Relevant source: `NavierStokes/ActualBaseVelocityBounds.lean`, lines 415-449 and
435-449.

The source explicitly states that support and zero-mass identities are consequences
of the actual coefficient construction rather than hypotheses on the final velocity.
`actual_exterior_coefficients` then proves exterior coefficient zero/positivity
properties from `FinalSlowBase.realizesScheme`, `EntranceAlignedBase.modulated_base_eq`,
and `EntranceAlignedBase.modulated_outer`. `actual_leading_eq` identifies the actual
slow-base velocity with the leading exterior velocity on the Cartesian exterior.
`actual_bounded_rate`, `actual_middle_rate`, and `actual_outer_rate` provide finite-jet
or jet-rate bounds for the actual velocity in endpoint regions.

This is positive evidence for an actual coefficient and velocity-rate construction.
It is not, by itself, a theorem transporting the final Cartesian field through
`tsum`, torus averaging, and the five paper observables. The inspected declarations
do not state `barMoment`, `torusAverage`, or an equality of the selected field with
the five-moment tuple.

## BaseContextAssembly.lean

Relevant source: `NavierStokes/BaseContextAssembly.lean`, lines 425-468,
470-544, and 546-620.

`radialBase`, `frequencyBase`, and `axialBase` assemble scaled components of the
slow-base velocity. `rawStress` builds a pair of scaled theta/axial stress fields;
`virtualStress` extends that stress by zero on the non-positive-radius half-line.
Theorems `axialBase_physical` and `angularBase_physical` identify components with
the corresponding physical slow-base velocity under positive-time/radius hypotheses.
`base_smooth`, `native_estimates`, and the unweighted/base-bound theorems establish
smoothness and local rate bounds. `rawStress_normalized`, `rawStress_zero_inner`,
and `rawStress_zero_near_axis` establish normalized stress identities and inner
vanishing behaviour.

This is a substantial reduced-coordinate and stress-realisation layer. It does not
show that the final global selected Cartesian field has the paper's five radial
observables after all summation and localization operations. It therefore supports
an intermediate correspondence classification, not endpoint transport.

## PhaseEstimates.lean

Relevant source: `NavierStokes/PhaseEstimates.lean`, lines 440-475,
950-971, and 985-1000.

`normalVelocity_bound` bounds the representative normal velocity from slope and
shear errors. `representative_slope_scaled` and `velocity_error_scaled` turn
representative parameters into explicit quantitative error bounds. The later
phase-estimate theorem supplies derivative, slope, direction, and angular-velocity
bounds, while `radialSlope_uniform_bound` supplies a uniform radial-slope bound.

These are parameter and phase estimates. They are not radial-integral evaluations,
Cartesian field moment identities, or endpoint `Witness` transport theorems.

## PrimaryRepresentatives.lean

Relevant source: `NavierStokes/PrimaryRepresentatives.lean`, lines 53-118,
120-186, and 188-220.

The module defines native masks and grid boxes, proves smoothness and support
containment, constructs active labels and representatives, and proves representative
distance bounds and mesh convergence. It also gives the physical-mask/normalized-mask
identity and an active-mask reindexing theorem. The reference-cone declarations bind
frequency, shear, and opening conditions.

This is genuine spatial representative and covariance geometry. It is not a proof
that an observable computed from the final activated Cartesian `tsum` field equals
the reduced profile moments.

## PositiveRepresentatives.lean

Relevant source: `NavierStokes/PositiveRepresentatives.lean`, lines 365-425 and
452-487.

The module proves stable-branch coordinate bounds, constructs open positive cells,
proves openness/convexity, places representatives in the cells, and proves that
fine-mesh cells eventually lie in prescribed neighbourhoods. This supplies a
controlled representative cover for the positive-time branch.

The inspected declarations do not define `barMoment` or `torusAverage`, and do not
transport the five cumulative radial observables to the selected endpoint.

## ReservedPatches.lean

Relevant source: `NavierStokes/ReservedPatches.lean`, lines 260-267, 288-357,
546-572, and 576-590.

`momentPatch` is an actual `FiveProfileMoments.Patch`. The clean/heated-field
theorems identify the outgoing profile on non-heat slots and isolate the heat-slot
increment. `radial_heated_fields` and `radial_witness_fields` prove, on radial
windows and closed patches, that the axial component is zero and the angular field
equals `FiveRowRank.background` applied to the radial amplitude. The support theorems
show that the heat increment and five-row updates are confined to their declared
patches.

This is strong evidence that the upstream radial patch and five-row machinery is
real and used. It is not evidence that those identities survive the complete lift
to the final global Cartesian velocity, spatial localization, periodization, and
natural-indexed summation. No unconditional `selected_witness`/`Witness` theorem
was found in these declarations asserting the five final Cartesian observables.

## Cross-module conclusion

The six modules close an important part of the queue: actual coefficient support,
reduced stress, phase bounds, representative geometry, and radial five-row patch
identities are now source-inspected. They strengthen the positive upstream record;
they do not close CTR-005. The precise remaining question is still the value-level
transport from these reduced/intermediate identities to the exported selected field.

The review therefore records:

- selected-field Cartesian five-observable transport: **not established in this
  inspected tranche**;
- nonzero selected-field remainder `Delta m != 0`: **not shown**;
- impossibility of transport: **not shown**;
- kernel-level `False`: **not shown**.

