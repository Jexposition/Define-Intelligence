# Witness Provenance & Choice Identity Evidence

**Generated:** 2026-10-01T04:06:20.072600+00:00

## 1. Choice Provenance Ledger

Total `Classical.choose` witness selections: 40
Total `Classical.choice` witness selections: 32

### Witness Identity Risk: selections WITHOUT nearby choose_spec

These select a witness but do not immediately use `choose_spec` to
extract or constrain the chosen value. The witness may be consumed
as though canonical without proving independence.

**31 selections without nearby spec (31/72 = 43%)**

- **`NavierStokes\AngularMomentReset.lean`** L453 in `resetBranch`
  Source: `exists_resetBranch`
  `Classical.choice (exists_resetBranch lam hlam)`
- **`NavierStokes\CorrectionInitialization.lean`** L3929 in `choice_nonempty`
  Source: `choice_nonempty`
  `noncomputable def choice (B N0 : ℕ) : Choice B N0 := Classical.choice (choice_nonempty B N0)`
- **`NavierStokes\CorrectionInitializationNoOptions.lean`** L3940 in `choice_nonempty`
  Source: `choice_nonempty`
  `noncomputable def choice (B N0 : ℕ) : Choice B N0 := Classical.choice (choice_nonempty B N0)`
- **`NavierStokes\FinalSlowBase.lean`** L634 in `profileData_nonempty`
  Source: `profileData_nonempty`
  `noncomputable def actualProfile : ProfileData := Classical.choice profileData_nonempty`
- **`NavierStokes\GermCandidateAssembly.lean`** L235 in `exists_candidate_witness_of_finite_stages`
  Source: `TailGaugePotential.finalPotential_awayExtensions`
  `hInitial hx hxz (Classical.choice (TailGaugePotential.finalPotential_awayExtensions H v upper bandFloor x hx))`
- **`NavierStokes\JointResidualLimits.lean`** L124 in `boundaryLimits`
  Source: `hext`
  `ftaylorSeries ℝ (Classical.choice (hext x hx)).value (1, x)`
- **`NavierStokes\JointResidualLimits.lean`** L139 in `boundaryLimits_joint`
  Source: `hext`
  `exact (Classical.choice (hext x hx)).jet_tendsto n`
- **`NavierStokes\LocalPotentialRebundle.lean`** L265 in `awayExtensions`
  Source: `eA`
  `exact extension_sub (Classical.choice (eA x hx))`
- **`NavierStokes\LocalPotentialRebundle.lean`** L266 in `awayExtensions`
  Source: `removedPotential_awayExtensions`
  `(Classical.choice (removedPotential_awayExtensions x hx))`
- **`NavierStokes\LocalPotentialRebundle.lean`** L268 in `awayExtensions`
  Source: `eD`
  `exact extension_add (Classical.choice (eD x hx))`
- **`NavierStokes\LocalPotentialRebundle.lean`** L269 in `awayExtensions`
  Source: `extension_curl`
  `(Classical.choice (extension_curl (Classical.choice (removedPotential_awayExtensions x hx))))`
- **`NavierStokes\LocalPotentialRebundle.lean`** L269 in `awayExtensions`
  Source: `removedPotential_awayExtensions`
  `(Classical.choice (extension_curl (Classical.choice (removedPotential_awayExtensions x hx))))`
- **`NavierStokes\LocalScheduleWitness.lean`** L65 in `awayExtensions_of_schedule`
  Source: `TailGaugePotential.finalPotential_awayExtensions`
  `(Classical.choice (TailGaugePotential.finalPotential_awayExtensions`
- **`NavierStokes\MatchingDebtBounds.lean`** L463 in `fixedBounds`
  Source: `fixedBounds_exists`
  `Classical.choice (fixedBounds_exists F N)`
- **`NavierStokes\MixedCandidateAssembly.lean`** L172 in `candidate_of_finite_stages`
  Source: `TailGaugePotential.finalPotential_awayExtensions`
  `hInitial hx hxz (Classical.choice (TailGaugePotential.finalPotential_awayExtensions H v upper bandFloor x hx))`
- **`NavierStokes\MixedCandidateWitness.lean`** L113 in `exists_candidate_witness_of_finite_stages`
  Source: `TailGaugePotential.finalPotential_awayExtensions`
  `hInitial hx hxz (Classical.choice (TailGaugePotential.finalPotential_awayExtensions H v upper bandFloor x hx))`
- **`NavierStokes\MixedDiagonalExtensions.lean`** L208 in `diagonal_awayExtensions_local`
  Source: `he0`
  `· exact central_extension_local hh hh1 hqbig a hs hx hz (Classical.choice (he0 x hx hz))`
- **`NavierStokes\MixedPeriodicAssembly.lean`** L228 in `cutResidual_awayExtensions`
  Source: `eA`
  `exact ⟨cutResidualExtension (Classical.choice (eA x hx)) (Classical.choice (ev x hx))`
- **`NavierStokes\MixedPeriodicAssembly.lean`** L228 in `cutResidual_awayExtensions`
  Source: `ev`
  `exact ⟨cutResidualExtension (Classical.choice (eA x hx)) (Classical.choice (ev x hx))`
- **`NavierStokes\MixedPeriodicAssembly.lean`** L229 in `cutResidual_awayExtensions`
  Source: `ep`
  `(Classical.choice (ep x hx))⟩`
- **`NavierStokes\NominalConeAssembly.lean`** L990 in `assemble`
  Source: `G.branches`
  `⟨A, c, D, hF, G.bound, Classical.choice (G.branches c.radius hr), hsep, hs⟩`
- **`NavierStokes\NominalProfile.lean`** L135 in `exists_axis_stage`
  Source: `prep.entrances`
  `Classical.choice (prep.entrances Λ (le_max_left _ _) C (le_max_left _ _))⟩,`
- **`NavierStokes\NominalProfile.lean`** L206 in `resetSolver_exists`
  Source: `resetSolver_exists`
  `noncomputable def resetSolver : ResetSolver := Classical.choice resetSolver_exists`
- **`NavierStokes\OffplaneCorrectionExtensions.lean`** L982 in `diagonal_extension`
  Source: `he`
  `let e : ∀ j, JointResidualLimits.OneSidedExtension (F j) x := fun j => Classical.choice (he j)`
- **`NavierStokes\ParametricRadialExtension.lean`** L58 in `parameterWindow`
  Source: `exists_parameterWindow`
  `Classical.choice (exists_parameterWindow hS hI)`
- **`NavierStokes\PartitionedCovariance.lean`** L812 in `constructedSlotSystem`
  Source: `exists_slotSystem`
  `Classical.choice (exists_slotSystem D h hh vr vt)`
- **`NavierStokes\PeriodicResidualLimits.lean`** L90 in `cutResidual_awayExtensions`
  Source: `hA`
  `exact ⟨cutResidualExtension (Classical.choice (hA x hx)) (Classical.choice (hp x hx))⟩`
- **`NavierStokes\PeriodicResidualLimits.lean`** L90 in `cutResidual_awayExtensions`
  Source: `hp`
  `exact ⟨cutResidualExtension (Classical.choice (hA x hx)) (Classical.choice (hp x hx))⟩`
- **`NavierStokes\PreparedOutgoing.lean`** L119 in `PreparedProfile.large_nominal`
  Source: `exists_prepared`
  `noncomputable def prepared : PreparedProfile := Classical.choice exists_prepared`
- **`NavierStokes\PrimaryGeometryAssembly.lean`** L463 in `prepared`
  Source: `exists_prepared`
  `Classical.choice (exists_prepared H v hcone upper B r0 hbox N0)`
- **`NavierStokes\ValidDyadicBandCover.lean`** L178 in `field_endpoint_extension`
  Source: `he`
  `apply MixedDiagonalExtensions.extension_of_eventuallyEq _ (Classical.choice (he n hn hl hr))`

### Witness Identity Risk: same source selected multiple times

**16 source theorems selected from more than once:**

#### `h` — selected 5 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\ParticularCopyBounds.lean` L318 → `nativeEnvelope`
- `NavierStokes\PhysicalCurlCovariance.lean` L825 → `globalCartesianPotential`
- `NavierStokes\PhysicalCurlCovariance.lean` L862 → `globalCartesianPotential_zero`
- `NavierStokes\ValidBandGluing.lean` L29 → `representative`
- `NavierStokes\ValidBandGluing.lean` L45 → `representative_eq_of_mem`

#### `exists_surjective_nat` — selected 4 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\ActualParticularStageControls.lean` L943 → `raw_jets`
- `NavierStokes\ActualParticularStageControls.lean` L1216 → `cutoff_jets`
- `NavierStokes\ActualSignedGeometry.lean` L1278 → `activeEnumeration`
- `NavierStokes\UniformPrimaryWeights.lean` L85 → `enumeration`

#### `TailGaugePotential.finalPotential_awayExtensions` — selected 4 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\GermCandidateAssembly.lean` L235 → `exists_candidate_witness_of_finite_stages`
- `NavierStokes\LocalScheduleWitness.lean` L65 → `awayExtensions_of_schedule`
- `NavierStokes\MixedCandidateAssembly.lean` L172 → `candidate_of_finite_stages`
- `NavierStokes\MixedCandidateWitness.lean` L113 → `exists_candidate_witness_of_finite_stages`

#### `hz` — selected 3 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\ActualMeanPhysicalData.lean` L129 → `Atlas.physical`
- `NavierStokes\ActualMeanPhysicalData.lean` L130 → `Atlas.physical`
- `NavierStokes\ActualMeanPhysicalData.lean` L130 → `Atlas.physical`

#### `exists_admissibleScales` — selected 3 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\ConstructedSlowBase.lean` L612 → `nominalScales`
- `NavierStokes\ConstructedSlowBase.lean` L710 → `modifiedScales`
- `NavierStokes\EntranceAlignedBase.lean` L1019 → `scales`

#### `he` — selected 3 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\OffplaneCorrectionExtensions.lean` L982 → `diagonal_extension`
- `NavierStokes\ValidDyadicBandCover.lean` L178 → `field_endpoint_extension`
- `NavierStokes\WaveStageContinuation.lean` L1919 → `cartesian_radialSupport`

#### `exists_template_bound` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\BorelExtension.lean` L109 → `templateBound`
- `NavierStokes\SpatialBorelExtension.lean` L137 → `templateBound`

#### `exists_nat_gt` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\BorelExtension.lean` L178 → `localScale`
- `NavierStokes\SpatialBorelExtension.lean` L196 → `templateBound_le_boundSum`

#### `choice_nonempty` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\CorrectionInitialization.lean` L3929 → `choice_nonempty`
- `NavierStokes\CorrectionInitializationNoOptions.lean` L3940 → `choice_nonempty`

#### `hext` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\JointResidualLimits.lean` L124 → `boundaryLimits`
- `NavierStokes\JointResidualLimits.lean` L139 → `boundaryLimits_joint`

#### `eA` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\LocalPotentialRebundle.lean` L265 → `awayExtensions`
- `NavierStokes\MixedPeriodicAssembly.lean` L228 → `cutResidual_awayExtensions`

#### `removedPotential_awayExtensions` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\LocalPotentialRebundle.lean` L266 → `awayExtensions`
- `NavierStokes\LocalPotentialRebundle.lean` L269 → `awayExtensions`

#### `hex` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\ParticularCopyBounds.lean` L329 → `nativeEnvelope_eq`
- `NavierStokes\ParticularCopyBounds.lean` L330 → `nativeEnvelope_eq`

#### `hp` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\PeriodicResidualLimits.lean` L90 → `cutResidual_awayExtensions`
- `NavierStokes\PositiveRepresentatives.lean` L147 → `stableInverse`

#### `caps` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\PreparedOutgoing.lean` L45 → `exists_prepared`
- `NavierStokes\PreparedOutgoing.lean` L62 → `exists_prepared`

#### `exists_prepared` — selected 2 times

**Risk:** if these selections occur in different definitions,
the two witnesses are NOT guaranteed to be the same object.

- `NavierStokes\PreparedOutgoing.lean` L119 → `PreparedProfile.large_nominal`
- `NavierStokes\PrimaryGeometryAssembly.lean` L463 → `prepared`

## 2. Explicit Identity Risk Cases

- `exists_surjective_nat` selected in 4 different definitions across 3 files: `activeEnumeration`, `cutoff_jets`, `enumeration`, `raw_jets`. These witnesses are NOT provably identical.
- `exists_nat_gt` selected in 2 different definitions across 2 files: `localScale`, `templateBound_le_boundSum`. These witnesses are NOT provably identical.
- `exists_admissibleScales` selected in 3 different definitions across 2 files: `modifiedScales`, `nominalScales`, `scales`. These witnesses are NOT provably identical.
- `TailGaugePotential.finalPotential_awayExtensions` selected in 3 different definitions across 4 files: `awayExtensions_of_schedule`, `candidate_of_finite_stages`, `exists_candidate_witness_of_finite_stages`. These witnesses are NOT provably identical.
- `hext` selected in 2 different definitions across 1 files: `boundaryLimits`, `boundaryLimits_joint`. These witnesses are NOT provably identical.
- `eA` selected in 2 different definitions across 2 files: `awayExtensions`, `cutResidual_awayExtensions`. These witnesses are NOT provably identical.
- `he` selected in 3 different definitions across 3 files: `cartesian_radialSupport`, `diagonal_extension`, `field_endpoint_extension`. These witnesses are NOT provably identical.
- `h` selected in 5 different definitions across 3 files: `globalCartesianPotential`, `globalCartesianPotential_zero`, `nativeEnvelope`, `representative`, `representative_eq_of_mem`. These witnesses are NOT provably identical.
- `hp` selected in 2 different definitions across 2 files: `cutResidual_awayExtensions`, `stableInverse`. These witnesses are NOT provably identical.
- `exists_prepared` selected in 2 different definitions across 2 files: `PreparedProfile.large_nominal`, `prepared`. These witnesses are NOT provably identical.

## 3. Structure Proof-Obligation Fields

Structures whose field names or types suggest proof obligations.
Each such field must be independently verified for the final selected witness.

**28 structures with ≥ 2 proof-obligation fields:**

### `SupportedContinuation` in `NavierStokes\OffplaneCorrectionExtensions.lean` L339

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `value` | `Lift → ℝ` | no |
| `smooth` | `ContDiffOn ℝ ∞ value (PhysicalMeanDomain.slowDomain W.carrier)` | ⚠️ YES |
| `supported` | `VariableGaugeMean.SupportedGauge a b (stableLength coord) W.carrier value` | no |
| `agrees` | `FiberAgreement W.carrier value f` | no |
| `value` | `= continuedSource coord F` | no |
| `smooth` | `= (continuedSource_smooth hc hc1 hF).mono (fun _ hp => W.stable hp)` | ⚠️ YES |
| `supported` | `= continuedSource_supported hs W.stable` | no |
| `agrees` | `= continuedSource_agreement hc hc1 F W.carrier` | no |
| `value` | `= VariableGaugeMean.compactPrimitive d a b M (stableLength coord) v e.value` | no |
| `smooth` | `= W.compactPrimitive_smooth hc hc1 ha hab hd M v e.smooth e.supported` | ⚠️ YES |
| `supported` | `= VariableGaugeMean.compactPrimitive_supportedGauge ha hab hd (stableLength coor` | no |
| `agrees` | `= compactPrimitive_agreement hc hc1 e.agrees d a b M v` | no |
| `value` | `= VariableGaugeMean.meanPressure d a b M hab (stableLength coord) v e.value` | no |
| `smooth` | `= W.meanPressure_smooth hc hc1 ha hab hd M v e.smooth e.supported` | ⚠️ YES |
| `supported` | `= VariableGaugeMean.compactPrimitive_supportedGauge ha hab hd (stableLength coor` | no |
| `agrees` | `= meanPressure_agreement hc hc1 e.agrees d a b M hab v` | no |
| `value` | `= VariableGaugeMean.streamPotential d a b M (stableLength coord) v e.value` | no |
| `smooth` | `= W.streamPotential_smooth hc hc1 ha hab hd M v e.smooth e.supported` | ⚠️ YES |
| `supported` | `= VariableGaugeMean.streamPotential_supportedGauge ha hab hd (stableLength coord` | no |
| `agrees` | `= streamPotential_agreement hc hc1 e.agrees d a b M v` | no |
| `value` | `= VariableGaugeMean.compactAlias d a b M (stableLength coord) v e.value` | no |
| `smooth` | `= W.compactAlias_smooth hc hc1 ha hab hd M v e.smooth e.supported` | ⚠️ YES |
| `supported` | `= by` | no |
| `agrees` | `= compactAlias_agreement hc hc1 e.agrees d a b M v` | no |

### `H3Curve` in `NavierStokes\R3\H3Curve.lean` L22

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `first` | `Fin 3 → VelocityField` | no |
| `second` | `Fin 3 → Fin 3 → VelocityField` | no |
| `third` | `Fin 3 → Fin 3 → Fin 3 → VelocityField` | no |
| `spatial_continuous` | `∀ t ∈ s, Continuous (fun x => u (t, x))` | ⚠️ YES |
| `approximation` | `∀ t ∈ s, H3Approximation (fun x => u (t, x))` | no |
| `velocity_continuous` | `Continuous (fun t : s =>` | ⚠️ YES |
| `first_continuous` | `∀ i, Continuous (fun t : s =>` | ⚠️ YES |
| `second_continuous` | `∀ i j, Continuous (fun t : s =>` | ⚠️ YES |
| `third_continuous` | `∀ i j k, Continuous (fun t : s =>` | ⚠️ YES |

### `Coefficients` in `NavierStokes\SlowBorelBase.lean` L1099

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `axial` | `ℕ → Inner → ℝ` | no |
| `phi` | `ℕ → Inner → ℝ` | no |
| `pressure` | `ℕ → Inner → ℝ` | no |
| `stressTheta` | `ℕ → Inner → ℝ` | no |
| `stressAxial` | `ℕ → Inner → ℝ` | no |
| `axial` | `∀ j, ContDiff ℝ ∞ (d.axial j)` | ⚠️ YES |
| `phi` | `∀ j, ContDiff ℝ ∞ (d.phi j)` | ⚠️ YES |
| `pressure` | `∀ j, ContDiff ℝ ∞ (d.pressure j)` | ⚠️ YES |
| `stressTheta` | `∀ j, ContDiff ℝ ∞ (d.stressTheta j)` | ⚠️ YES |
| `stressAxial` | `∀ j, ContDiff ℝ ∞ (d.stressAxial j)` | ⚠️ YES |
| `carrier` | `= univ` | no |
| `isOpen` | `= isOpen_univ` | no |
| `scale_mem` | `= by intro p hp t ht; trivial` | no |

### `SmoothFamily` in `NavierStokes\MeanRankUpdate.lean` L1177

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `lam` | `ℝ` | no |
| `a` | `ℝ` | no |
| `b` | `ℝ` | no |
| `length` | `E → ℝ` | no |
| `velocity` | `E → ℝ` | no |
| `amplitude` | `E → ℝ` | no |
| `debt` | `E → Debt` | no |
| `lam_pos` | `0 < lam` | no |
| `a_pos` | `0 < a` | no |
| `ordered` | `a < b` | no |
| `length_pos` | `∀ s, 0 < length s` | no |
| `velocity_ne` | `∀ s, velocity s ≠ 0` | no |
| `amplitude_ne` | `∀ s, amplitude s ≠ 0` | no |
| `length_smooth` | `ContDiff ℝ ∞ length` | ⚠️ YES |
| `velocity_smooth` | `ContDiff ℝ ∞ velocity` | ⚠️ YES |
| `amplitude_smooth` | `ContDiff ℝ ∞ amplitude` | ⚠️ YES |
| `debt_smooth` | `ContDiff ℝ ∞ debt` | ⚠️ YES |

### `LoopData` in `NavierStokes\ModulatedProfileAssembly.lean` L282

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `parameter` | `ParameterData W` | no |
| `etaRadius` | `ℝ` | no |
| `one_lt_etaRadius` | `1 < etaRadius` | no |
| `etaRadius_lt_target` | `etaRadius < parameter.window.inner` | no |
| `modulation` | `ModulatedHistories.Window` | no |
| `after_initial` | `4 / W.axis.scale < modulation.left` | no |
| `before_repair` | `modulation.right < (repairPatch W).left` | no |
| `a` | `Field` | no |
| `m` | `Field` | no |
| `p₁` | `Field` | no |
| `p₂` | `Field` | no |
| `a_smooth` | `ContDiff ℝ ∞ a` | ⚠️ YES |
| `m_smooth` | `ContDiff ℝ ∞ m` | ⚠️ YES |
| `p₁_smooth` | `ContDiff ℝ ∞ p₁` | ⚠️ YES |
| `p₂_smooth` | `ContDiff ℝ ∞ p₂` | ⚠️ YES |
| `angular_eq` | `∀ p ∈ fullRegion W modulation etaRadius,` | no |
| `axial_eq` | `∀ p ∈ fullRegion W modulation etaRadius,` | no |
| `stock₁_eq` | `∀ p ∈ fullRegion W modulation etaRadius,` | no |
| `stock₂_eq` | `∀ p ∈ fullRegion W modulation etaRadius,` | no |
| `positive_f` | `∀ p ∈ fullRegion W modulation etaRadius, 0 < W.profiles.f p` | no |
| `positive_a` | `∀ p ∈ fullRegion W modulation etaRadius, 0 < a p` | no |
| `nonzero_L` | `∀ p ∈ fullRegion W modulation etaRadius, NaturalAxisData.L F.data.h p.2 ≠ 0` | no |
| `projection` | `∀ p ∈ modulationRegion modulation etaRadius, 2 < p₁ p + p₂ p * m p` | no |
| `relaxed` | `∀ p ∈ modulationRegion modulation etaRadius,` | no |
| `true_boundary` | `∀ p ∈ boundaryRegion modulation etaRadius,` | no |
| `true_following` | `∀ p ∈ followingRegion W modulation etaRadius,` | no |

### `RunInvariant` in `NavierStokes\ActualCyclePreservation.lean` L768

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `analytic` | `Invariant σ x` | no |
| `coherent` | `ActualCycleCoherence.Coherent x` | ⚠️ YES |
| `periodic` | `ActualCyclePeriodicity.Periodic x` | no |
| `analytic` | `= by simpa only [ActualIterationLedger.sigma_zero] using initial_invariant B N0` | no |
| `coherent` | `= ActualCycleCoherence.initial B N0` | ⚠️ YES |
| `periodic` | `= ActualCyclePeriodicity.initial B N0` | no |
| `analytic` | `= (stepResult_of_particular R.analytic hN hσ R.coherent.labels P).invariant` | no |
| `coherent` | `= ActualCycleCoherence.step R.analytic (waveData_of_particular R.analytic hN hσ ` | ⚠️ YES |
| `periodic` | `= ActualCyclePeriodicity.step R.analytic R.periodic` | no |

### `Pulse` in `NavierStokes\PartitionedCovariance.lean` L62

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `ψ` | `ℝ → ℝ` | no |
| `x` | `ℝ → ℝ` | no |
| `t` | `ℝ → Vec2` | no |
| `ψ_continuous` | `Continuous ψ` | ⚠️ YES |
| `x_continuous` | `Continuous x` | ⚠️ YES |
| `t_continuous` | `Continuous t` | ⚠️ YES |
| `ψ_compact` | `HasCompactSupport ψ` | no |

### `RegularFamily` in `NavierStokes\PhysicalWaveSum.lean` L745

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `gap_le` | `∀ L, f.gap L ≤ Δ` | no |
| `gap_native` | `∀ L, f.gap L ≤ ChartScales.nativeIndex h L.val.1` | no |
| `amplitude_smooth` | `∀ I, ContDiff ℝ ∞ (f.amplitude I)` | ⚠️ YES |
| `F_smooth` | `∀ L, ContDiff ℝ ∞ (f.carrier L).F` | ⚠️ YES |
| `G_smooth` | `∀ L, ContDiff ℝ ∞ (f.carrier L).G` | ⚠️ YES |
| `angular_integer` | `∀ L, ∃ m : ℤ,` | no |
| `geometry_support` | `∀ I y,` | no |
| `mask_support` | `∀ I y, y ∈ preterminal →` | no |

### `Admissible` in `NavierStokes\PressureDatum.lean` L34

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `cap_nonneg` | `0 ≤ A` | no |
| `integrable` | `Integrable g` | ⚠️ YES |
| `nonneg` | `∀ y, 0 ≤ g y` | ⚠️ YES |
| `measurable` | `Measurable a` | ⚠️ YES |
| `exponent_nonneg` | `∀ y, 0 ≤ a y` | no |
| `exponent_le` | `∀ y, a y ≤ A` | no |

### `H1Approximation` in `NavierStokes\R3\H3Approximation.lean` L31

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `memLp` | `MemLp f 2 volume` | no |
| `derivative_memLp` | `∀ i, MemLp (df i) 2 volume` | no |
| `approx` | `ℕ → Space → E` | no |
| `smooth` | `∀ n, ContDiff ℝ ∞ (approx n)` | ⚠️ YES |
| `compact` | `∀ n, HasCompactSupport (approx n)` | ⚠️ YES |
| `approx_memLp` | `∀ n, MemLp (approx n) 2 volume` | no |
| `derivative_approx_memLp` | `∀ n i, MemLp (spatialPartial i (approx n)) 2 volume` | no |
| `tendsto` | `Tendsto (fun n => (approx_memLp n).toLp (approx n)) atTop (𝓝 (memLp.toLp f))` | ⚠️ YES |
| `derivative_tendsto` | `∀ i,` | no |

### `MeanInput` in `NavierStokes\ActualPhysicalStageBounds.lean` L30

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `firstBand` | `ℕ` | no |
| `gapBound` | `ℕ` | no |
| `lowerRadius` | `ℝ` | no |
| `upperRadius` | `ℝ` | no |
| `alpha` | `ℝ` | no |
| `family` | `PhysicalMeanJetBounds.CoherentFamily h degree firstBand gapBound (region h) ℝ` | no |
| `band_four` | `4 ≤ firstBand` | no |
| `lower_pos` | `0 < lowerRadius` | no |
| `radii_lt` | `lowerRadius < upperRadius` | no |
| `smooth` | `∀ n ≥ firstBand, ContDiffOn ℝ ∞ (family.native n)` | ⚠️ YES |
| `support` | `PhysicalMeanJetBounds.NativeSupport h lowerRadius upperRadius firstBand (region ` | ⚠️ YES |
| `jets` | `PhysicalMeanJetBounds.NativeJets firstBand (region h) (h * alpha) family.native` | no |

### `PhysicalApproach` in `NavierStokes\BaseResidual.lean` L350

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `carrier` | `Set SpaceTime` | no |
| `compact` | `IsCompact carrier` | ⚠️ YES |
| `in_carrier` | `∀ᶠ z in l, z ∈ carrier` | no |
| `past` | `∀ᶠ z in l, z.1 < 1` | no |
| `radial` | `∀ᶠ z in l, (cartesianChart h z).2.1 ∈ Icc lo hi` | no |
| `scale` | `Tendsto (fun z => (cartesianChart h z).1) l (𝓝 0)` | ⚠️ YES |

### `AngularData` in `NavierStokes\DirectAngularDiagonal.lean` L139

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `scalar` | `Coefficient` | no |
| `smooth` | `ContDiffOn ℝ ∞ scalar (positiveDomain U)` | ⚠️ YES |
| `inner` | `Slow → ℝ` | no |
| `inner_continuous` | `ContinuousOn inner U` | no |
| `inner_pos` | `∀ s ∈ U, 0 < inner s` | no |
| `vanishes` | `∀ p, slowOfCyl p ∈ U → 0 ≤ p.2.1 → p.2.1 < inner (slowOfCyl p) → scalar p = 0` | no |
| `smooth` | `= hf.mul D.smooth` | ⚠️ YES |
| `inner` | `= D.inner` | no |
| `inner_continuous` | `= D.inner_continuous` | no |
| `inner_pos` | `= D.inner_pos` | no |

### `Witness` in `NavierStokes\ExtendedHeatedOutgoing.lean` L59

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `radius_pos` | `0 < XR` | no |
| `switch_large` | `1 ≤ switchRadius F XR` | no |
| `coefficients` | `ℝ → Coeff` | no |
| `smooth` | `ContDiffOn ℝ ∞ coefficients ExtendedHeatDebts.enlargedBand` | ⚠️ YES |
| `moments` | `∀ eta ∈ ExtendedHeatDebts.enlargedBand,` | no |
| `coefficient_bound` | `∀ eta ∈ ExtendedHeatDebts.enlargedBand,` | no |
| `derivative_bound` | `∀ eta ∈ ExtendedHeatDebts.enlargedBand,` | no |
| `first_jet` | `∀ eta ∈ ExtendedHeatDebts.enlargedBand,` | no |
| `patch_positive` | `∀ eta ∈ ExtendedHeatDebts.enlargedBand, ∀ X : ℝ, 0 < X →` | no |
| `heat_positive` | `∀ eta ∈ ExtendedHeatDebts.enlargedBand, ∀ X : ℝ, 0 < X →` | no |
| `radius_pos` | `= hXR` | no |
| `switch_large` | `= (le_max_right _ _).trans ((le_max_right _ _).trans hK)` | no |
| `coefficients` | `= c` | no |
| `smooth` | `= hs` | ⚠️ YES |
| `moments` | `= ?_` | no |
| `coefficient_bound` | `= fun eta heta => (hspec eta heta).2.1` | no |
| `derivative_bound` | `= fun eta heta => (hspec eta heta).2.2.1` | no |
| `first_jet` | `= fun eta heta => (hspec eta heta).2.2.2.1` | no |
| `patch_positive` | `= ?_` | no |
| `heat_positive` | `= hp (switchRadius F XR) hKp' }⟩` | no |

### `CompensationWitness` in `NavierStokes\HeatedOutgoing.lean` L300

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `radius_pos` | `0 < XR` | no |
| `switch_large` | `1 ≤ switchRadius F XR` | no |
| `coefficients` | `ℝ → Coeff` | no |
| `smooth` | `ContDiffOn ℝ ∞ coefficients parameterDomain` | ⚠️ YES |
| `moments` | `∀ eta ∈ parameterDomain,` | no |
| `coefficient_bound` | `∀ eta ∈ parameterDomain, ‖coefficients eta‖ ≤ C / switchRadius F XR` | no |
| `derivative_bound` | `∀ eta ∈ parameterDomain,` | no |
| `first_jet` | `∀ eta ∈ parameterDomain,` | no |
| `patch_positive` | `∀ eta ∈ parameterDomain, ∀ X : ℝ, 0 < X →` | no |
| `radius_pos` | `= hXR` | no |
| `switch_large` | `= (le_max_right _ _).trans hK` | no |
| `coefficients` | `= c` | no |
| `smooth` | `= hs` | ⚠️ YES |
| `moments` | `= ?_` | no |
| `coefficient_bound` | `= fun eta heta => (hspec eta heta).2.1` | no |
| `derivative_bound` | `= fun eta heta => (hspec eta heta).2.2.1` | no |
| `first_jet` | `= fun eta heta => (hspec eta heta).2.2.2.1` | no |
| `patch_positive` | `= ?_ }⟩` | no |

### `ModelContinuation` in `NavierStokes\InitialHarmonicContinuation.lean` L425

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `value` | `Model → E` | no |
| `smooth` | `ContDiff ℝ ∞ value` | ⚠️ YES |
| `agrees` | `EqOn value (modelSource f) modelStrip` | no |
| `supported` | `∀ z, value z ≠ 0 → z.2 ∈ spatialSupport L` | no |
| `smooth` | `= A.contDiff.comp e.smooth` | ⚠️ YES |
| `agrees` | `= fun z hz => congrArg A (e.agrees hz)` | no |
| `supported` | `= fun z hz => e.supported z (fun he => hz (by rw [he, map_zero]))` | no |
| `ComplexVector` | `= ActualPrimary.periodicGaussian j L x.1.2 • absoluteAmplitude j L x` | no |
| `ComplexVector` | `=` | no |

### `MeanHypotheses` in `NavierStokes\LiftedMeanResidual.lean` L820

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `isOpen` | `IsOpen U` | no |
| `radius_smooth` | `ContDiffOn ℝ ∞ c.operators.radius U` | no |
| `radius_ne` | `∀ x ∈ U, c.operators.radius x ≠ 0` | no |
| `profile_smooth` | `ContDiffOn ℝ ∞ c.operators.radialProfile U` | no |
| `base_smooth` | `MeanIncrementBounds.SmoothTriple U c.base` | no |
| `mean_smooth` | `MeanIncrementBounds.SmoothTriple U u.mean` | no |
| `pressure_smooth` | `MeanIncrementBounds.SmoothOn U u.pressure` | no |
| `oscillation_smooth` | `∀ n i, ContDiffOn ℝ ∞ (fun p => u.oscillation n p i) (cylinder U)` | no |
| `oscillatoryPressure_smooth` | `∀ n, ContDiffOn ℝ ∞ (u.oscillatoryPressure n) (cylinder U)` | no |
| `oscillation_periodic` | `∀ n i, PeriodicOn U (fun p => u.oscillation n p i)` | no |
| `oscillatoryPressure_periodic` | `∀ n, PeriodicOn U (u.oscillatoryPressure n)` | no |
| `oscillation_mean_zero` | `∀ n x, x ∈ U → ∀ i,` | no |
| `oscillatoryPressure_mean_zero` | `∀ n x, x ∈ U → CorrectionState.angularAverage u.oscillatoryPressure n x = 0` | no |
| `base_divergence` | `∀ n p, p ∈ cylinder U → realDivergence` | no |
| `total_divergence` | `∀ n p, p ∈ cylinder U → realDivergence` | no |
| `base_error_continuous` | `∀ n x, x ∈ U → ∀ i, Continuous (fun θ : ℝ => u.errors.base n (x, θ) i)` | ⚠️ YES |
| `excluded_continuous` | `∀ n x, x ∈ U → ∀ i, Continuous (fun θ : ℝ => u.errors.total n (x, θ) i)` | ⚠️ YES |
| `isOpen` | `= H.isOpen` | no |
| `radius_smooth` | `= H.radius_smooth` | no |
| `radius_ne` | `= H.radius_ne` | no |
| `radial_smooth` | `= contDiffOn_const.add` | no |
| `axial_smooth` | `= contDiffOn_const` | no |
| `time_smooth` | `= contDiffOn_const` | no |

### `ResetSolver` in `NavierStokes\NominalProfile.lean` L186

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `solve` | `Coeff → Coeff` | no |
| `radius` | `ℝ` | no |
| `bound` | `ℝ` | no |
| `radius_pos` | `0 < radius` | no |
| `bound_pos` | `0 < bound` | no |
| `smooth` | `ContDiffOn ℝ ∞ solve (Metric.ball 0 radius)` | ⚠️ YES |
| `at_zero` | `solve 0 = 0` | no |
| `equation` | `∀ q ∈ Metric.ball (0 : Coeff) radius,` | no |
| `positive` | `∀ q ∈ Metric.ball (0 : Coeff) radius, ∀ x : ℝ, 0 < x →` | ⚠️ YES |
| `norm_bound` | `∀ q ∈ Metric.ball (0 : Coeff) radius, ‖solve q‖ ≤ bound * ‖q‖` | no |

### `Specification` in `NavierStokes\OutgoingProfile.lean` L557

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `amplitude_smooth` | `ContDiff ℝ ∞ F.amp` | ⚠️ YES |
| `angular_smooth` | `ContDiffOn ℝ ∞ F.E domain` | no |
| `axial_smooth` | `ContDiffOn ℝ ∞ F.U domain` | no |
| `momentum_smooth` | `ContDiffOn ℝ ∞ F.H domain` | no |
| `pressure_smooth` | `ContDiffOn ℝ ∞ F.Pi domain` | no |
| `angular_positive` | `∀ p ∈ domain, 0 < F.E p` | no |
| `amplitude_bounds` | `∀ eta : ℝ, eta ^ 2 ≤ 1 →` | no |
| `mass_integrable` | `∀ eta : ℝ, IntegrableOn (fun X => F.U (X, eta)) (Ioi 0)` | no |
| `angular_integrable` | `∀ eta : ℝ, IntegrableOn (fun X => F.H (X, eta) * F.U (X, eta)) (Ioi 0)` | no |
| `mass_total_zero` | `∀ eta : ℝ, (∫ X in Ioi 0, F.U (X, eta)) = 0` | no |
| `angular_total_zero` | `∀ eta : ℝ, (∫ X in Ioi 0, F.H (X, eta) * F.U (X, eta)) = 0` | no |
| `after_pulse` | `∀ eta X : ℝ, 0 < X → F.data.core.endpoint ≤ Real.log X →` | no |
| `energy_integrable` | `∀ eta : ℝ, IntegrableOn (F.energyDensity eta) (Ioi 0)` | no |
| `energy_zero` | `∀ eta : ℝ, eta ^ 2 ≤ 1 → F.totalS eta = 0` | no |
| `renormalized_integrable` | `∀ eta : ℝ, IntegrableOn (fun X => F.H (X, eta) - F.powerH X) (Ioi 0)` | no |
| `renormalized_zero` | `∀ eta : ℝ, (∫ X in Ioi 0, F.H (X, eta) - F.powerH X) = 0` | no |
| `eventual_power` | `∀ eta X : ℝ, 0 < X → tailEnd F.data ≤ Real.log X →` | no |
| `ideal_prefix` | `∀ eta X : ℝ, 0 < X → X ≤ 1 →` | no |
| `pressure_integrable` | `∀ eta : ℝ, IntegrableOn (F.canonicalKernel eta) (Ioi 0)` | no |
| `pressure_canonical` | `∀ eta X : ℝ, 0 < X →` | no |
| `same_axis_datum` | `F.axisDatum = SchedulePressure.axisPressure F.data` | no |
| `axis_limit` | `∀ eta : ℝ, Tendsto (fun X => F.Pi (X, eta)) (𝓝[>] (0 : ℝ)) (𝓝 (F.axisDatum eta))` | ⚠️ YES |
| `analytic_axis_datum` | `AnalyticOnNhd ℂ (SchedulePressure.complexAxisPressure F.data) PressureDatum.stri` | no |

### `WaveData` in `NavierStokes\PhysicalStageBounds.lean` L51

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `lowerRadius` | `ℝ` | no |
| `upperRadius` | `ℝ` | no |
| `nativeWidth` | `ℝ` | no |
| `slowBound` | `ℝ` | no |
| `frequencyBound` | `ℝ` | no |
| `alpha` | `ℝ` | no |
| `shift` | `ℝ` | no |
| `harmonics` | `ℕ` | no |
| `gapBound` | `ℕ` | no |
| `lower_pos` | `0 < lowerRadius` | no |
| `width_nonneg` | `0 ≤ nativeWidth` | no |
| `slow_nonneg` | `0 ≤ slowBound` | no |
| `frequency_one_le` | `1 ≤ frequencyBound` | no |
| `strip` | `WeightedClasses.StripData D` | no |
| `weight` | `I → ℕ → D → ℝ` | no |
| `source` | `I → ℕ → D → ℂ` | no |
| `source_bounds` | `LocalPhysicalCopyBounds.LocalSourceBounds strip h alpha weight source` | no |
| `copies` | `J → PhysicalCopyBounds.CopyFamily harmonics K` | no |
| `cells` | `∀ i, PhysicalCopyBounds.SupportCells (copies i)` | no |
| `chart` | `∀ i, LocalPhysicalCopyBounds.CommonChart (copies i) (cells i)` | no |
| `chart_maps` | `∀ i k L, MapsTo ((chart i).map k L) ((chart i).domain k L) strip.domain` | no |
| `carrier` | `∀ i, PhysicalCopyBounds.CarrierBounds (copies i) (cells i)` | no |
| `support` | `∀ i, LocalPhysicalCopyBounds.SupportData (copies i)` | ⚠️ YES |
| `smooth` | `∀ i, LocalPhysicalCopyBounds.SmoothData (copies i) lowerRadius h nativeWidth` | ⚠️ YES |
| `frequencies` | `∀ i k L, |((copies i).carrier k L).angular| ≤ frequencyBound ∧` | no |

### `MeanData` in `NavierStokes\PhysicalStageBounds.lean` L154

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `firstBand` | `ℕ` | no |
| `gapBound` | `ℕ` | no |
| `region` | `Set PhysicalGraphBounds.Plane` | no |
| `lowerRadius` | `ℝ` | no |
| `upperRadius` | `ℝ` | no |
| `alpha` | `ℝ` | no |
| `slow` | `ℕ → ℝ` | no |
| `family` | `PhysicalMeanJetBounds.CoherentFamily h degree firstBand gapBound region ℝ` | no |
| `band_four` | `4 ≤ firstBand` | no |
| `lower_pos` | `0 < lowerRadius` | no |
| `radii_lt` | `lowerRadius < upperRadius` | no |
| `region_open` | `IsOpen region` | no |
| `region_covers` | `PhysicalMeanDomain.normalizedSlowDomain (2 * h) (1 / 4) 4 ⊆ region` | no |
| `smooth` | `∀ n ≥ firstBand, ContDiffOn ℝ ∞ (family.native n) (PhysicalMeanDomain.slowDomain` | ⚠️ YES |
| `support` | `PhysicalMeanJetBounds.NativeSupport h lowerRadius upperRadius firstBand region f` | ⚠️ YES |
| `slow_nonneg` | `∀ n ≥ firstBand, 0 ≤ slow n` | no |
| `slow_growth` | `∃ C : ℝ, 1 ≤ C ∧ ∃ p : ℕ, ∀ n ≥ firstBand, slow n ≤ C * ChartScales.S n ^ p` | no |
| `native_class` | `PhysicalMeanDomain.LocalBandJets region (ChartScales.epsilon h) slow alpha famil` | no |

### `SmoothHolomorphicSystem` in `NavierStokes\PositiveAxisExistence.lean` L173

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `smooth` | `SmoothCoefficientData T U A₀ A₁ f` | ⚠️ YES |
| `zeroth_holomorphic` | `∀ r ∈ radialDomain T, DifferentiableOn ℂ (A₀ r) U` | no |
| `first_holomorphic` | `∀ r ∈ radialDomain T, DifferentiableOn ℂ (A₁ r) U` | no |
| `forcing_holomorphic` | `∀ r ∈ radialDomain T, DifferentiableOn ℂ (f r) U` | no |
| `smooth` | `= {` | ⚠️ YES |
| `forcing` | `= fun i => (h.smooth.forcing i).mono hs` | no |
| `zeroth` | `= fun i j => (h.smooth.zeroth i j).mono hs` | no |
| `first` | `= fun i j => (h.smooth.first i j).mono hs }` | no |
| `zeroth_holomorphic` | `= fun r hr => h.zeroth_holomorphic r (radialDomain_mono hRT hr)` | no |
| `first_holomorphic` | `= fun r hr => h.first_holomorphic r (radialDomain_mono hRT hr)` | no |
| `forcing_holomorphic` | `= fun r hr => h.forcing_holomorphic r (radialDomain_mono hRT hr) }` | no |

### `NativeJets` in `NavierStokes\PrimaryCopyBounds.lean` L40

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `nonneg` | `∀ i x, x ∈ V.carrier i → 0 ≤ w i x` | ⚠️ YES |
| `smooth` | `∀ i, ContDiffOn ℝ ∞ (f i) (V.carrier i)` | ⚠️ YES |
| `bound` | `∀ m : ℕ, ∃ C : ℝ, 1 ≤ C ∧ ∃ p : ℕ, ∀ i x, x ∈ V.carrier i → ∀ j ≤ m,` | no |

### `PulseBounds` in `NavierStokes\PulseCovariance.lean` L130

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `radius_one_le` | `1 ≤ r` | no |
| `lower_pos` | `0 < a` | no |
| `upper_pos` | `0 < A` | no |
| `decay_pos` | `0 < b` | no |
| `lower_decay_pos` | `0 < B` | no |
| `cutoff_continuous` | `Continuous ψ` | ⚠️ YES |
| `component_continuous` | `Continuous x` | ⚠️ YES |
| `cutoff_abs_le` | `∀ v, |ψ v| ≤ 1` | no |
| `cutoff_zero` | `∀ v, v ∉ Icc (r ^ 2 / 6) (5 * r ^ 2 / 6) → ψ v = 0` | no |
| `cutoff_one` | `∀ v ∈ Icc (r ^ 2 / 3) (2 * r ^ 2 / 3), ψ v = 1` | no |
| `component_lower` | `∀ v ∈ Icc 0 (r ^ 2), a * gaussian B (r ^ 2 / 2) r v ≤ x v` | no |
| `component_upper` | `∀ v ∈ Icc 0 (r ^ 2), x v ≤ A * gaussian b (r ^ 2 / 2) r v` | no |

### `Cutoff` in `NavierStokes\R3PressureCommutator.lean` L19

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `radius_pos` | `0 < R` | no |
| `constant_ge_one` | `1 ≤ L` | no |
| `measurable` | `Measurable φ` | ⚠️ YES |
| `range` | `∀ x, φ x ∈ Icc (0 : ℝ) 1` | no |
| `difference` | `∀ x y, |φ x - φ y| ≤ L * (‖x - y‖ / R)` | no |
| `constant_nonneg` | `0 ≤ C` | no |
| `measurable` | `Measurable K` | ⚠️ YES |
| `bound` | `∀ z, z ≠ 0 → ‖K z‖ ≤ C * ‖z‖ ^ (-3 : ℝ)` | no |

### `Input` in `NavierStokes\ReferencePath.lean` L350

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `scale` | `ℝ` | no |
| `scale_pos` | `0 < scale` | no |
| `f` | `Field` | no |
| `U` | `Field` | no |
| `f_smooth` | `ContDiffOn ℝ ∞ f (NaturalProfile.domain scale)` | no |
| `U_smooth` | `ContDiffOn ℝ ∞ U (NaturalProfile.domain scale)` | no |
| `positive` | `∀ p ∈ NaturalProfile.domain scale, 0 ≤ scale * p.1 →` | ⚠️ YES |
| `scale` | `= Λ` | no |
| `scale_pos` | `= hΛ` | no |
| `f` | `= F.f` | no |
| `U` | `= F.U` | no |
| `f_smooth` | `= F.natural.f_smooth` | no |
| `U_smooth` | `= F.natural.U_smooth` | no |
| `positive` | `= F.positive` | ⚠️ YES |

### `ContextSupport` in `NavierStokes\SignedRequestContinuation.lean` L581

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `theta` | `Supported P.a P.b (OffplaneCorrectionExtensions.stableLength (2 * F.data.h)) W.c` | no |
| `axial` | `Supported P.a P.b (OffplaneCorrectionExtensions.stableLength (2 * F.data.h)) W.c` | no |
| `value` | `= d.state.thetaResidual (ActualCorrectionModels.context H v upper B index) n` | no |
| `smooth` | `= (thetaResidual_localShell W.lower_pos W.isOpen` | ⚠️ YES |
| `supported` | `= thetaResidual_supported W.isOpen` | no |
| `agrees` | `= thetaResidual_agrees W.isOpen (ActualCorrectionModels.context H v upper B inde` | no |
| `value` | `= d.state.axialResidual (ActualCorrectionModels.context H v upper B index) n` | no |
| `smooth` | `= (axialResidual_localShell W.lower_pos W.isOpen` | ⚠️ YES |
| `supported` | `= axialResidual_supported W.isOpen` | no |
| `agrees` | `= axialResidual_agrees W.isOpen (ActualCorrectionModels.context H v upper B inde` | no |

### `CircleDensity` in `NavierStokes\SmoothLoop.lean` L363

| Field | Type Preview | Proof Obligation? |
| --- | --- | --- |
| `rate` | `ℝ → ℝ` | no |
| `smooth` | `ContDiff ℝ (∞ : WithTop ℕ∞) rate` | ⚠️ YES |
| `positive` | `∀ θ, 0 < rate θ` | ⚠️ YES |
| `periodic` | `Function.Periodic rate (2 * Real.pi)` | no |
| `integral_one` | `(∫ θ in (0 : ℝ)..(2 * Real.pi), rate θ) = 1` | no |

## Validation update: review-side witness probes

The five review-side probes under `NavierStokesReview/src/probes/` were compiled
against the current checkout with `lake env lean` on 2026-10-01.

| Probe | Result | Interpretation |
|---|---|---|
| `WitnessIdentityProbe1_FinalPotentialExtensions.lean` | PASS | Checks the final-potential extension declarations used by the selected route. |
| `WitnessIdentityProbe2_SurjectiveNat.lean` | PASS | Confirms the inspected enumeration/surjectivity declarations. |
| `WitnessIdentityProbe3_AdmissibleScales.lean` | PASS | Confirms the nominal/modified scale declarations and their specification lemmas. |
| `WitnessIdentityProbe4_ChoiceNonempty.lean` | PASS after namespace correction | Confirms the production `ActualPrimary.choice` declarations. The parallel `CorrectionInitializationNoOptions` file is a standalone self-check, not an imported second production choice. |
| `WitnessIdentityProbe5_PreparedAndFallbacks.lean` | PASS | Confirms the inspected prepared-profile and fallback representative specifications. |

These are review probes, not counterexamples to the production theorem. Their
positive result narrows the static choice inventory: the reported repeated
selection candidates are not, by themselves, evidence that the selected route
uses unrelated witnesses. The remaining obligation is proof-relevant closure:
trace each selected constructor and fallback through the elaborated C/D proof
term, and prove the good branch or choice-independence theorem at every use.

No OpenAI source file was edited by this probe validation. The protected
untracked files `NavierStokes/R3/TestPressure.lean` and
`evidence/lean_environment_closure_ns_3d_2026-09-30.json` remain outside the
review commit.

## 4. Comparator Solution Verification

**File:** `NavierStokes/ComparatorSolution.lean`
**Imports:** `NavierStokes.ComparatorR3Theorem`, `NavierStokes.ComparatorTheorem`
**Theorems declared:** `navier_stokes_breakdown_R3`, `navier_stokes_breakdown_periodic`
**Contains sorry:** NO ✅

### Full source
```lean
import NavierStokes.ComparatorR3Theorem
import NavierStokes.ComparatorTheorem

/-!
# Navier–Stokes Comparator submission: options (C) and (D)

Expose the project's proof adapters under the reference theorem names.
The adapters import `ComparatorDefinitions`, never the challenge module.
-/

namespace NavierStokes.Comparator

local notation "ℝ³" => EuclideanSpace ℝ (Fin 3)

/-- (C) Breakdown of Navier–Stokes solutions on ℝ³. -/
theorem navier_stokes_breakdown_R3 (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionDecay u₀ ∧ ForceConditionDecay f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn nu u₀ f v p) := by
  exact ComparatorBridge.navier_stokes_breakdown_R3 nu hnu

/-- (D) Breakdown of Navier–Stokes solutions on ℝ³/ℤ³. -/
theorem navier_stokes_breakdown_periodic (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionPeriodic u₀ ∧ ForceConditionPeriodic f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessPeriodic nu u₀ f v p) := by
  exact ComparatorBridge.navier_stokes_breakdown_periodic nu hnu

end NavierStokes.Comparator

#print axioms NavierStokes.Comparator.navier_stokes_breakdown_R3
#print axioms NavierStokes.Comparator.navier_stokes_breakdown_periodic

```
