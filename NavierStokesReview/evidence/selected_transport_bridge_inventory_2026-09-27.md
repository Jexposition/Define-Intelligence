# Selected-field transport bridge inventory

Date: 2026-09-27  
Repository: `Jexposition/Define-Intelligence`  
Scope: current checkout, production `NavierStokes/` modules and review-side
`NavierStokesReview/src/completions/` modules.

## Purpose

This ledger tests a precise claim: whether the five paper observables
\((M,I,J,S,C_p)\), or an equivalent promoted debt vector, are proved to be
the observables of the final selected Cartesian field exported by
`ActualCandidateAssembly.selected_witness`.

The audit does **not** treat the existence of an upstream five-moment theorem
as proof that the theorem reaches the endpoint. It also does **not** treat the
absence of a theorem with an obvious name as proof that no differently named
bridge exists. The source was therefore checked in two layers:

1. production reachability from `NavierStokes.ActualCandidateAssembly`;
2. declaration-level inspection of the review-side bridge candidates.

## Endpoint boundary

Production source inspection gives the following boundary:

| Source location | Declaration | Scope at the boundary | Missing target |
|---|---|---|---|
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` | Nested existential proposition containing schedule, `ASum`/`BSum`/`PSum`, extensions, force, `CandidateProperties`, consequences, H³ limit, force-jet limits, and boundary jets | No `Debt`, `FiveRows`, `barMoment`, or equality to \((M,I,J,S,C_p)\) |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1181` | `selected_witness` | Specialises the generic witness and supplies the selected construction | No exported moment equality |
| `NavierStokes/CandidateConsequences.lean: mixed_exists_force_with_consequences` | force/consequence constructor | Uses smoothness, divergence, residual jets, away extensions, and origin blow-up | No selected Cartesian-to-radial moment theorem |
| `NavierStokes/GermCandidateAssembly.lean:160-270` | `exists_candidate_witness_of_finite_stages` | Converts `StageEstimates` and finite-stage data into the witness route | No five-observable equality in `StageEstimates` or `SelectedSchedule` |

This is a type-boundary result. It does not say that upstream moment algebra
is dead or mathematically false.

## Production reachability

A direct source breadth-first traversal beginning at
`NavierStokes.ActualCandidateAssembly` found 507 reachable `NavierStokes.*`
modules. Two relevant paths are:

```text
ActualCandidateAssembly
  -> ActualPhysicalPrefixFields -> TailGaugePotential -> ModulatedExterior
  -> BaseExterior -> AssembledSlowBase -> GlobalSlowProfiles
  -> PositiveOrderMoments

ActualCandidateAssembly
  -> InitialPhysicalData -> ActualPrimaryBounds -> CorrectionInitialization
  -> MeanRankUpdate -> FiveProfileMoments -> FiveRowRank
```

The production graph therefore disproves a simple “these files are not
imported” explanation. Import reachability and endpoint transport are separate
questions.

### Current source-path cross-check

The same source parser, run with a corrected Lean import regular expression,
gives the following shortest paths from the endpoint roots:

```text
ActualCandidateAssembly
  -> ActualPhysicalPrefixFields -> TailGaugePotential -> ModulatedExterior
  -> BaseExterior -> AssembledSlowBase -> GlobalSlowProfiles
  -> PositiveOrderMoments

ActualCandidateAssembly
  -> InitialPhysicalData -> ActualPrimaryBounds -> CorrectionInitialization
  -> MeanRankUpdate -> FiveProfileMoments -> FiveRowRank

R3.Theorem
  -> R3ActualCandidate -> ActualCandidateAssembly
```

The current seven-root source closure is 588 modules and 1,648 import edges.
The 507-module count is the single-root `ActualCandidateAssembly` closure.
`LocalPaperTheorem`, `LocalResidualFlatness`, and `PaperLocalization` are real
files, but they are not reachable from either endpoint root: their imports run
in the opposite direction or belong to downstream comparison wrappers. They
therefore cannot serve as an implicit selected-witness transport theorem.

This is still an import result, not a value-level result. The endpoint path
loads the moment definitions and their upstream proofs, while the inspected
packaging declarations do not carry a field-to-moment equality.

## Hidden-name bridge screen

As a declaration-screening check, the 507 reachable production modules were
searched for direct textual co-occurrence between the endpoint predicates and
the moment interfaces. The result was:

| Terms required in the same production module | Count | Interpretation |
|---|---:|---|
| `FiveRows` and `CandidateProperties` | 0 | No direct source-level join found |
| `barMoment` and `CandidateProperties` | 0 | No direct source-level join found |
| `PositiveOrderMoments` and `CandidateProperties` | 0 | No direct source-level join found |
| `FiveProfileMoments` and `CandidateProperties` | 0 | No direct source-level join found |
| `barMoment` and `Witness` | 0 | No direct source-level join found |

The screen is evidence about the inspected source text, not a proof that a
differently named theorem cannot exist. In particular, `BaseRankPatch` contains
a `Witness` in its own base-patch context, and the review-side completion
modules contain explicit partial transport declarations. The decisive missing
item remains a source-backed theorem that instantiates those transport data for
the final selected Cartesian field and exports the resulting five observables
at the `ActualCandidateAssembly.Witness` boundary.

## Partial bridges found in review-side completion modules

The following declarations are genuine partial bridges. They narrow the open
claim and must not be described as absent mathematics.

| File and line | Declaration | What it proves | What it does not prove |
|---|---|---|---|
| `src/completions/SelectedBarMomentInterface.lean:32` | `selected_component_barMoment_apply` | Definition-level `barMoment` integral for an arbitrary supplied point-to-spacetime map and scalar profile | The selected witness supplies the required map/profile equality |
| `SelectedBarMomentInterface.lean:46-54` | `SelectedBarMomentTransportData`, `selected_component_requires_transport_data` | Exact component-to-`barMoment` identity under an explicit transport-data hypothesis | Instantiation of that hypothesis by the exported witness |
| `SelectedPhysicalPointTransport.lean:23-28` | physical point pullback lemmas | Definitional compatibility of the physical moment point and a supplied scalar pullback | A selected-field equality to the paper's scalar observable |
| `SelectedPotentialProductionFinitePrefix.lean:34` | `selected_potential_partial_curl_eq_stage_sum` | Finite-prefix curl expansion | Infinite-sum value or moment evaluation |
| `SelectedPotentialProductionFinitePrefix.lean:48` | `selected_potential_partial_cut_product_rule` | Localised curl product rule, including the cutoff-gradient commutator | Vanishing of the commutator after integration |
| `SelectedPotentialProductionFinitePrefix.lean:61` | `selected_potential_partial_production_expansion` | Finite-prefix production expansion | A nonzero or zero global remainder |
| `SelectedPotentialProductionFinitePrefix.lean:93-117` | finite-prefix pullback and radial identities | Finite-prefix `barMoment` pullback and radial integral formula | Passage from finite prefix to final `tsum` and the paper tuple |
| `SelectedPotentialProductionRadialScalar.lean:83` | `selected_potential_production_radial_scalar_eq` | Local radial scalar formula for the selected potential sum | Numerical evaluation of its radial integral |
| `SelectedPotentialProductionRadialScalar.lean:107` | `selected_witness_production_radial_scalar_transport` | Selected schedule gives the local radial production formula under stated hypotheses | A five-moment equality in `Witness` |
| `SelectedPotentialProductionTorusAverage.lean:22,31` | torus-average and finite-prefix radial reduction | Torus average and finite-prefix `barMoment` reduce to a scalar radial expression | Limit interchange and value/sign of the final integral |
| `SelectedMixedVelocityDecomposition.lean:23-48` | velocity decompositions | Splits uncut and periodic mixed velocity into potential/direct pieces | Equality of either piece with a paper moment tuple |
| `SelectedMixedVelocityFinitePrefix.lean:24` | local finite-prefix representation | Local representation by two finite prefixes | A common-prefix global integral or remainder calculation |
| `SelectedMixedProductionRadialComponent.lean:37` | mixed scalar split | Mixed production scalar is potential plus direct contribution | Vanishing of either contribution after radial integration |
| `SelectedMixedProductionBranchSplit.lean:42` | branch split | Pointwise branch decomposition | Global moment value and sign |
| `SelectedMixedProductionBarMoment.lean:38-52` | mixed pullback/`barMoment` lemmas | Applies `barMoment` to a constructed mixed scalar pullback | Equality of that pullback with the paper's named observable |
| `SelectedMixedProductionTorusAverage.lean:25,34` | mixed torus/radial reductions | Mixed scalar torus average and radial reduction | Numerical evaluation of the resulting integral |
| `SelectedPotentialProductionTsumScope.lean:29` | eventual finite-prefix jet equality | Each point/jet is eventually represented by a finite prefix under hypotheses | Interchange of `tsum`, curl, torus average, and `barMoment` |
| `SelectedCartesianRadialGate.lean:20` | `meanField_recovered_from_component_one` | Positive-radius algebraic recovery under a nonzero component hypothesis | A global axis-inclusive radial identity |
| `SelectedCutoffCurlCommutator.lean:18` | curl product rule | Explicit cutoff-gradient commutator term | Its integrated cancellation |
| `SelectedCycleMomentTransport.lean:19-67` | cycle/state moment invariants | Zero-mass and selected cycle angular/axial conclusions | Final mixed Cartesian-field moments |
| `SelectedDirectStageMomentTransport.lean:32` | native stage moment zero | Zero angular native-stage moment | Final selected mixed field moment |
| `SelectedBaseProfileTransport.lean:21-28` | base curl and axis limit | Constructed base curl agrees with selected slow-base velocity and has the axis limit | Five-moment transport for the full selected field |
| `SelectedBaseMomentCompatibilityProbe.lean` | base compatibility declarations | Upstream aligned base five-moment identities and base blow-up | Equality between base identities and final selected mixed observables |
| `SelectedR3PackagingBoundary.lean:30,41` | packaging non-implications | The weak exported candidate type is compatible with a nonzero five-payload and does not export a zero payload | A contradiction or a numerical field mismatch |
| `SelectedEndpointMomentTransportObstruction.lean:37,42` | endpoint non-implications | The `Witness` type alone does not imply a selected five-payload equality | That the concrete selected field violates the moments |

## Exact unresolved equality

The remaining selected-path obligation is a value-level statement of the form

\[
 (M,I,J,S,C_p)_{\rm paper}
 =
 \mathcal O\bigl(u_{\rm selected},p_{\rm selected},f_{\rm selected}\bigr),
\]

where \(\mathcal O\) includes the actual operations used by the construction:

\[
\texttt{potentialSum}
\to \nabla\times
\to \text{localisation}
\to \text{periodisation}
\to \texttt{torusAverage}
\to \text{radial pullback}
\to \texttt{barMoment},
\]

with axis and whole-space extension conditions included. A proof of this
equality must address:

1. cutoff-gradient commutator terms;
2. passage from finite prefixes to the infinite sum;
3. interchange of derivatives, sums, averages, and integrals;
4. the off-axis \(r>0\) chart and the on-axis limit route;
5. the direct-potential contribution in the mixed field;
6. the identification with the named five paper observables.

## Current classification

- **Confirmed:** upstream five-moment and five-row algebra is reachable and is
  used in slow-base/correction branches.
- **Confirmed:** review-side files prove several local, finite-prefix, and
  pullback identities.
- **Not established:** the final selected Cartesian field satisfies the named
  five-observable equality.
- **Not established:** a nonzero selected-field remainder has been computed.
- **Not established:** a kernel-level `False` follows from the current bridge
  inventory.

The correct next computation is therefore a concrete value-level transport
attempt, not another import-name search and not a claim that all bridge
mathematics is absent.

## Direct source check of the proposed architectural clusters

The candidate clusters named in the review plan are present, with one naming
correction: `StateRealization` and `PhysicalFields` are not standalone module
paths in the live tree. `StateRealization` is a structure in
`NavierStokes/PhysicalResidualJetBounds.lean:885`, while the physical field
definitions are distributed across the prefix and realization modules.

The source-level results are:

| Source span | What is actually proved | Boundary that remains |
|---|---|---|
| `LocalPaperTheorem.lean:128-176` | A selected local schedule supplies smooth fields, divergence freedom, residual flatness, exterior zero residual, and angular growth | No five-observable equality for the final whole-space witness |
| `PaperLocalization.lean:28-48` | A local theorem packages a compact candidate and local agreement on a neighbourhood | Local agreement is not Cartesian-to-radial moment transport |
| `EntranceAlignedBase.lean:666-671` | `PositiveOrderMoments.moments` vanishes for the aligned base history under its stated hypotheses | The theorem concerns the aligned base history, not `ASum`, `BSum`, or the selected mixed field |
| `CorrectionState.lean:449-476` | `rank_model_rows` and `rank_rows_on_patch` establish `FiveRowRank.FiveRows` for the correction subsystem | The conclusion is about correction profiles and patch hypotheses |
| `DefectIncrementBounds.lean:621-646` | `fiveRows_mass_zero` and `fiveRows_preserve_masses` prove local radial correction-moment vanishing and preservation | No equality to the final Cartesian `potentialSum` field |
| `DefectIncrementBounds.lean:775-813` | `RankGeometry.fiveRows`, `preserve_masses`, and `zeroMasses` propagate the local rank invariant across a rank stage | The stage invariant is not exported as a `Witness` field |
| `FinalSlowBase.lean:616-660` | The slow-base record and `exists_final_base` package profile, finite identities, scales, and bounds | The record explicitly does not store a final PDE or selected five-moment conclusion |

This is the required project-wide distinction: source reachability and local
invariant propagation are confirmed; the selected-field value theorem remains
unproved. The result is not a claim that the moment branch is dead code.

## Positive upstream five-moment route confirmed

The source trace found a stronger upstream result than the correction-row
screen alone:

- `GlobalSlowProfiles.lean:1043-1060`, `profiles_moments`, proves all five
  `PositiveOrderMoments.moments` rows for the constructed positive-order
  profile sequence.
- `GlobalStressSupport.lean:144-157`, `moments_zero`, transfers that result to
  the named axial and angular histories by `moments_congr_positive`.
- `AssembledSlowBase.lean:592-617` consumes the zero mass row to prove the
  extended axial primitive vanishes outside the support radius.

These are genuine value-level results for the upstream radial history and
slow-base construction. They do not identify the final `ASum`/`BSum`/`PSum`
Cartesian fields in `ActualCandidateAssembly.Witness` with those histories
after the full mixed assembly, spatial curl, localisation, periodisation,
torus averaging, and radial projection. The audit records the upstream route
as **transported locally**, while the final selected-field identity remains
**not established**.

## Reachable outgoing-profile moment route

The selected import closure contains an additional moment-bearing route that
must be distinguished from the `GlobalSlowProfiles` route. Its shortest source
path is:

```text
ActualCandidateAssembly
  -> InitialPhysicalData -> ActualPrimaryBounds -> CorrectionInitialization
  -> MeanRankUpdate -> FiveProfileMoments -> UniformAngularReset
  -> OutgoingTail -> OutgoingSchedule
```

`OutgoingSchedule.lean:739-747` defines the scalar `massMoment` and
`angularMoment` integrals. `OutgoingSchedule.lean:846-927` proves the endpoint
identities `massMoment_endpoint`, `angularMoment_endpoint`, and
`exact_axial_moments`; `OutgoingSchedule.lean:929-950` propagates the two zero
identities after the pulse. `OutgoingTail.lean:908-923` preserves the same two
quantities through the extended angular profile.

These are real, reachable profile-level results. They establish two scalar
outgoing-profile identities used in the correction/rank construction. The
inspected declarations do not identify those scalars with the full five-tuple
of named paper observables, nor do they prove that the final Cartesian fields
`ASum`, `BSum`, and `PSum` have those values after curl, localisation,
periodisation, infinite summation, torus averaging, and radial pullback. The
correct classification is therefore: **reachable upstream profile transport;
final selected-field transport still not established**.

## Final mixed-field assembly trace checked

The endpoint is not a disconnected placeholder. The source contains a real
Cartesian assembly route:

- `TailGaugePotential.lean:433-450` defines `finalPotential` from
  `FinalSlowBase.vectorPotential` and proves `finalPotential_sameCurl`, which
  identifies its spatial curl with `FinalSlowBase.velocity` for `t < 1`.
- `ActualPhysicalStageBounds.lean:616-656` gives the initial-potential curl
  decomposition into the slow-base velocity, initial curl data, and the direct
  angular contribution.
- `ActualCandidateAssembly.lean:205-211` defines the zeroth potential from
  the final base plus the initial increment; `:531-568` defines the three
  stage families and their zero/successor equations; `:1003-1077` proves
  stage curl/chart, pressure, and `stageRealizations` equalities.
- `ActualCandidateAssembly.lean:1125-1151` forms `ASum`, `BSum`, and `PSum`
  with `SolenoidalDiagonal.potentialSum`, then applies localisation,
  periodisation, and time activation before `CandidateProperties`.
- `MixedPeriodicAssembly.lean:20-170` proves smoothness, periodicity, local
  equality, and divergence transfer for the mixed field.

An exact-name search found the final-series names `ASum`, `BSum`, and `PSum`
only in the endpoint and generic witness layers. The moment declarations occur
in the upstream profile/history clusters. No inspected declaration has the
combined endpoint shape

```text
five_observables (activatedVelocity (periodicVelocity ASum BSum))
  (activatedPressure (periodicPressure PSum)) = promoted_profile_moments
```

This does not prove that the missing theorem cannot be derived. It fixes the
current boundary precisely: Cartesian stage realisation is proved, while the
selected-field observable calculation and equality to the named paper moments
remain an unperformed value-level transport obligation.

## Finite-modification scope checked

`AssembledSlowBase.lean:1514-1529` defines `FiniteModification`. Its record
contains field agreement, pressure agreement, support/domain conditions, and
one explicit moment field:

```text
mass : ∀ eta ∈ S,
  Q.M (nominalOuterX W, eta) = W.profiles.M (nominalOuterX W, eta)
```

The record does not itself contain a five-coordinate equality for
`(M, I, J, S, Cp)`. This is not evidence that the other identities are
missing: `EntranceAlignedBase.aligned_moments_zero` and the rank/profile
theorems supply additional local identities. It does establish that the
finite-modification record alone is not the selected-field five-moment
transport theorem. The remaining audit target is the composition of those
separate identities through the final stage sums and field operators.

## Logarithmic profile/history bridge checked

`NominalConeAssembly.lean:366-446` proves chart identities for the outgoing
profile quantities `M`, `J`, `I`, and `S`. In particular,
`NominalConeAssembly.Witness.log_histories` at `:452-470` maps the profile
history quantities to the outgoing and heat-switch histories in logarithmic
radial coordinates. `:596-667` then transports the corresponding history
parameters and derivative identities.

This is a genuine profile-to-history bridge and corrects any claim that the
paper observables are merely named but never related to upstream radial data.
The bridge's codomain is still profile/history data. The inspected theorem
does not take the endpoint `ASum`, `BSum`, or `PSum` as an input and does not
return a `barMoment` or five-observable equality for the activated Cartesian
field. The endpoint composition remains the open value-level check.

## Local Cartesian coherence checked

`ActualPrimaryCoherence.lean:1866-1940` supplies a real local Cartesian
realisation layer. `cartesianPotential` and `cartesianVelocity` are defined
from the physical potential and spatial curl; `cartesianPotential_smooth`,
`cartesianVelocity_smooth`, `cartesianVelocity_axis_zero`,
`piece_cartesian_velocity`, `piece_physical_pressure`, and
`cartesianVelocity_divergence` establish smoothness, axis behaviour, the
piece-to-Cartesian velocity relation, pressure representation, and
divergence-freeness on their stated domains. This is positive evidence
against describing the Cartesian layer as absent or purely formal.

Those declarations still do not compute the five profile observables on the
final `ASum`/`BSum`/`PSum` fields after all endpoint operations. The audit
therefore records a narrower unresolved composition obligation rather than a
missing local Cartesian realisation.
