# Deep Semantic Audit Evidence — OpenAI Navier-Stokes Repository

**Generated:** 2026-10-01T04:12:06.940010+00:00
**Scope:** `NavierStokes/`, `Euler/`, `ComparatorChallenges/`
**Script:** `NavierStokesReview/tools/deep_semantic_audit.py`

## Summary Statistics

| Metric | Count |
| --- | ---: |
| Total .lean files scanned | 2658 |
| Total lines of Lean | 644005 |
| Total bytes | 33722325 |
| Trust-escape hits (non-comment, all dirs) | 4 |
| Trust-escape hits (NavierStokes/ only) | 0 |
| `Classical.choose` occurrences | 55 |
| `Classical.choice` occurrences | 151 |
| Fallback-to-zero patterns | 18 |
| Structure declarations | 402 |
| `noncomputable def` declarations | 5828 |
| `noncomputable section` declarations | 2619 |

## 1. Kernel Trust-Escape Scan

**WARNING: 4 trust-escape hits found (excluding comments):**

### `sorry` in `ComparatorChallenges\Euler.lean` line 88
```lean
    ∃ u₀ : ℝ³ → ℝ³, InitialVelocityConditionDecay u₀ ∧
      ¬ (∃ v p, EulerExistenceAndSmoothnessR3 u₀ v p) := by
  sorry

/-!
```

### `sorry` in `ComparatorChallenges\Euler.lean` line 184
```lean
      (∫⁻ t in Ico (0 : ℝ) Tstar, vorticityNorm (v · t)) = ⊤ ∧
      ¬ (∃ w q, EulerExistenceAndSmoothnessR3 u₀ w q) := by
  sorry

end Euler
```

### `sorry` in `ComparatorChallenges\NavierStokes.lean` line 277
```lean
    InitialVelocityConditionDecay u₀ ∧ ForceConditionDecay f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn nu u₀ f v p) := by
  sorry

/-- (D) Breakdown of Navier–Stokes Solutions on ℝ³/ℤ³. -/
```

### `sorry` in `ComparatorChallenges\NavierStokes.lean` line 284
```lean
    InitialVelocityConditionPeriodic u₀ ∧ ForceConditionPeriodic f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessPeriodic nu u₀ f v p) := by
  sorry

end NavierStokes.Comparator
```

### ComparatorChallenges `sorry` (expected by design)

4 `sorry` occurrences in ComparatorChallenges/ — these are intentional challenge placeholders per Comparator protocol.

- `ComparatorChallenges\Euler.lean` line 88: `sorry`
- `ComparatorChallenges\Euler.lean` line 184: `sorry`
- `ComparatorChallenges\NavierStokes.lean` line 277: `sorry`
- `ComparatorChallenges\NavierStokes.lean` line 284: `sorry`

## 2. Witness Selection Provenance (Classical.choose / Classical.choice)

| Category | Count |
| --- | ---: |
| `Classical.choose` occurrences | 55 |
| `Classical.choice` occurrences | 151 |

### Classical.choice witness selections (HIGH PRIORITY)

Each `Classical.choice` selects an arbitrary inhabitant of a `Nonempty` type.
Audit question: is the selected witness later proved independent of the choice,
or is it consumed as though canonical?

- **`NavierStokes\ActualSlowAxis.lean`** L354: `Classical.choice (Classical.choose_spec (exists_tube_of_pressure_eq hp hP0 F hΛ hsmall hσ)).2`
- **`NavierStokes\AngularMomentReset.lean`** L453: `Classical.choice (exists_resetBranch lam hlam)`
- **`NavierStokes\CorrectionInitialization.lean`** L3929: `noncomputable def choice (B N0 : ℕ) : Choice B N0 := Classical.choice (choice_nonempty B N0)`
- **`NavierStokes\CorrectionInitializationNoOptions.lean`** L3940: `noncomputable def choice (B N0 : ℕ) : Choice B N0 := Classical.choice (choice_nonempty B N0)`
- **`NavierStokes\FinalSlowBase.lean`** L634: `noncomputable def actualProfile : ProfileData := Classical.choice profileData_nonempty`
- **`NavierStokes\GermCandidateAssembly.lean`** L235: `hInitial hx hxz (Classical.choice (TailGaugePotential.finalPotential_awayExtensions H v upper bandFloor x hx))`
- **`NavierStokes\GermCandidateAssembly.lean`** L239: `hpInitial hx hxz (Classical.choice ((SlowBaseEndpoint.final_fields_awayExtensions H v upper bandFloor).2 x hx))`
- **`NavierStokes\JointResidualLimits.lean`** L124: `ftaylorSeries ℝ (Classical.choice (hext x hx)).value (1, x)`
- **`NavierStokes\JointResidualLimits.lean`** L139: `exact (Classical.choice (hext x hx)).jet_tendsto n`
- **`NavierStokes\LocalPotentialRebundle.lean`** L265: `exact extension_sub (Classical.choice (eA x hx))`
- **`NavierStokes\LocalPotentialRebundle.lean`** L266: `(Classical.choice (removedPotential_awayExtensions x hx))`
- **`NavierStokes\LocalPotentialRebundle.lean`** L268: `exact extension_add (Classical.choice (eD x hx))`
- **`NavierStokes\LocalPotentialRebundle.lean`** L269: `(Classical.choice (extension_curl (Classical.choice (removedPotential_awayExtensions x hx))))`
- **`NavierStokes\LocalScheduleWitness.lean`** L65: `(Classical.choice (TailGaugePotential.finalPotential_awayExtensions`
- **`NavierStokes\LocalScheduleWitness.lean`** L72: `(Classical.choice ((SlowBaseEndpoint.final_fields_awayExtensions`
- **`NavierStokes\MatchingDebtBounds.lean`** L463: `Classical.choice (fixedBounds_exists F N)`
- **`NavierStokes\MixedCandidateAssembly.lean`** L172: `hInitial hx hxz (Classical.choice (TailGaugePotential.finalPotential_awayExtensions H v upper bandFloor x hx))`
- **`NavierStokes\MixedCandidateAssembly.lean`** L176: `hpInitial hx hxz (Classical.choice ((SlowBaseEndpoint.final_fields_awayExtensions H v upper bandFloor).2 x hx))`
- **`NavierStokes\MixedCandidateWitness.lean`** L113: `hInitial hx hxz (Classical.choice (TailGaugePotential.finalPotential_awayExtensions H v upper bandFloor x hx))`
- **`NavierStokes\MixedCandidateWitness.lean`** L117: `hpInitial hx hxz (Classical.choice ((SlowBaseEndpoint.final_fields_awayExtensions H v upper bandFloor).2 x hx))`
- **`NavierStokes\MixedDiagonalExtensions.lean`** L208: `· exact central_extension_local hh hh1 hqbig a hs hx hz (Classical.choice (he0 x hx hz))`
- **`NavierStokes\MixedPeriodicAssembly.lean`** L228: `exact ⟨cutResidualExtension (Classical.choice (eA x hx)) (Classical.choice (ev x hx))`
- **`NavierStokes\MixedPeriodicAssembly.lean`** L229: `(Classical.choice (ep x hx))⟩`
- **`NavierStokes\NominalConeAssembly.lean`** L990: `⟨A, c, D, hF, G.bound, Classical.choice (G.branches c.radius hr), hsep, hs⟩`
- **`NavierStokes\NominalProfile.lean`** L135: `Classical.choice (prep.entrances Λ (le_max_left _ _) C (le_max_left _ _))⟩,`
- **`NavierStokes\NominalProfile.lean`** L206: `noncomputable def resetSolver : ResetSolver := Classical.choice resetSolver_exists`
- **`NavierStokes\OffplaneCorrectionExtensions.lean`** L982: `let e : ∀ j, JointResidualLimits.OneSidedExtension (F j) x := fun j => Classical.choice (he j)`
- **`NavierStokes\ParametricRadialExtension.lean`** L58: `Classical.choice (exists_parameterWindow hS hI)`
- **`NavierStokes\PartitionedCovariance.lean`** L812: `Classical.choice (exists_slotSystem D h hh vr vt)`
- **`NavierStokes\PeriodicResidualLimits.lean`** L90: `exact ⟨cutResidualExtension (Classical.choice (hA x hx)) (Classical.choice (hp x hx))⟩`
- **`NavierStokes\PreparedOutgoing.lean`** L119: `noncomputable def prepared : PreparedProfile := Classical.choice exists_prepared`
- **`NavierStokes\PrimaryGeometryAssembly.lean`** L463: `Classical.choice (exists_prepared H v hcone upper B r0 hbox N0)`
- **`NavierStokes\ValidDyadicBandCover.lean`** L178: `apply MixedDiagonalExtensions.extension_of_eventuallyEq _ (Classical.choice (he n hn hl hr))`
- **`Euler\BaseLiteralFirstPacket.lean`** L51: `Classical.choice (exists_firstPacketChoice (X^(-2 : ℝ)) H.tilt_bound`
- **`Euler\CylinderSobolevSpace.lean`** L99: `(fun i => Classical.choice (ih (n + 1) (by omega) (Fin.cons i w))) ?_⟩`
- **`Euler\CylinderSobolevSpace.lean`** L105: `Classical.choice (word_has_jet period u q 0 (by omega) Fin.elim0)`
- **`Euler\H6Pressure.lean`** L62: `(Classical.choice h).sobolevNorm else 0`
- **`Euler\LinearFundamentalPath.lean`** L60: `Classical.choice (nonempty_fundamentalPath T hT B)`
- **`Euler\MeanPacketContract.lean`** L20: `exact ⟨(Classical.choice h).vector_angle_independent t x θ η,`
- **`Euler\MeanPacketContract.lean`** L21: `(Classical.choice h).scalar_angle_independent t x θ η⟩`
- **`Euler\MeanPacketContract.lean`** L26: `exact (Classical.choice h).inverse_vector_divergence t x θ`
- **`Euler\MeanPacketContract.lean`** L31: `exact (Classical.choice h).initial_vector_support θ`
- **`Euler\MeanPacketContract.lean`** L36: `exact (Classical.choice h).initial_vector_compact θ`
- **`Euler\MeanPacketContract.lean`** L41: `exact (Classical.choice h).vector_joint_continuous`
- **`Euler\MeanPacketContract.lean`** L47: `exact ⟨(Classical.choice h).vector_angle_jet t x θ, (Classical.choice h).scalar_angle_jet t x θ⟩`
- **`Euler\MeanPacketCylinderFields.lean`** L94: `((Classical.choice h).vectorCylinderField P).congr (fun _ _ _ => by`
- **`Euler\MeanPacketData.lean`** L123: `Classical.choice (sourceMeanSolver_strong D.T D.T_pos.le D.ℓ D.ℓ_pos`
- **`Euler\MeanPacketForcingAlgebra.lean`** L78: `(show Nonempty (Forcing D (raw i+∑ j ∈ s, raw j)) from ⟨(Classical.choice hi).add (Classical.choice hs)⟩)`
- **`Euler\MeanPacketInitialZero.lean`** L38: `exact (Classical.choice h).vector_initial_zero hL x θ`
- **`Euler\MeanPacketJets.lean`** L93: `exact (Classical.choice h).jet_equation t x θ`

### Classical.choose witness selections

#### `Euler\AllOrderCorrectionFamily.lean` (1 occurrences)
- L20: `Classical.choose (finite_exists period hT A B q hq)`

#### `Euler\AllOrderDriftFinite.lean` (1 occurrences)
- L52: `Classical.choose (finite_exists period hT A B q hq)`

#### `Euler\BoundedCoefficientSmooth.lean` (1 occurrences)
- L56: `field := boundedDerivative A.field A.smooth (Classical.choose (A.bounded 1)) (fun x => by`

#### `Euler\CorrectionAssemblyData.lean` (1 occurrences)
- L89: `solution q hq := Classical.choose (H q hq)`

#### `Euler\CylinderSmoothOrbit.lean` (1 occurrences)
- L108: `Classical.choose (exists_smooth_representative period u hu)`

#### `Euler\MeanInteriorCutoffs.lean` (1 occurrences)
- L18: `max 1 (Classical.choose (derivative_bound_exists f hc hs n))`

#### `Euler\MeanSmoothRepresentative.lean` (1 occurrences)
- L87: `Classical.choose (exists_smooth_representative u hu)`

#### `Euler\OrdinaryEulerLimit.lean` (1 occurrences)
- L88: `(eulerLimitData V hb h0).toEvolution hpos (Classical.choose (hb 3)) (Classical.choose_spec (hb 3))`

#### `Euler\OrdinaryEulerLocalExistence.lean` (2 occurrences)
- L112: `Classical.choose ((regularizer n).exists_smooth (regularizedTime A) (regularizedTime_pos A).le A hA)`
- L141: `(localLimit A hA).regularizedEvolution (Classical.choose (regularizedSolution_bounds A hA 4))`

#### `Euler\SobolevPointEvaluation.lean` (1 occurrences)
- L18: `Classical.choose (exists_continuous_representative period (value period u) (toJet period u))`

#### `Euler\SobolevProduct.lean` (1 occurrences)
- L48: `Classical.choose (exists_sobolev_product period hq L hL u v)`

#### `Euler\SobolevSmoothing.lean` (1 occurrences)
- L22: `Classical.choose (hD i f)`

#### `NavierStokes\ActualMeanPhysicalData.lean` (2 occurrences)
- L129: `ChartScales.Q (Classical.choose hz) ^ (-degree) *`
- L130: `f (Classical.choose hz) (A.chart (Classical.choose hz) z)`

#### `NavierStokes\ActualParticularPhysicalData.lean` (1 occurrences)
- L1700: `ActualParticularStageControls.Label B N0 := Classical.choose L.property`

#### `NavierStokes\ActualParticularStageControls.lean` (2 occurrences)
- L943: `let e : ℕ → ActivePair B N0 := Classical.choose (exists_surjective_nat (ActivePair B N0))`
- L1216: `let e : ℕ → ActivePair B N0 := Classical.choose (exists_surjective_nat (ActivePair B N0))`

#### `NavierStokes\ActualSignedExterior.lean` (1 occurrences)
- L116: `Label B N0 := Classical.choose L.mem`

#### `NavierStokes\ActualSignedGeometry.lean` (1 occurrences)
- L1278: `Classical.choose (exists_surjective_nat (ActivePair H v a reference chart))`

#### `NavierStokes\ActualSlowAxis.lean` (1 occurrences)
- L345: `noncomputable def tubeWidth : ℝ := Classical.choose (exists_tube_of_pressure_eq hp hP0 F hΛ hsmall hσ)`

#### `NavierStokes\BorelExtension.lean` (2 occurrences)
- L109: `Classical.choose (exists_template_bound j k v)`
- L178: `Classical.choose (exists_nat_gt ((2 : ℝ) ^ j * boundSum j (a j)))`

#### `NavierStokes\ConstructedSlowBase.lean` (2 occurrences)
- L612: `Classical.choose (exists_admissibleScales`
- L710: `Classical.choose (exists_admissibleScales`

#### `NavierStokes\EntranceAlignedBase.lean` (1 occurrences)
- L1019: `Classical.choose (exists_admissibleScales`

#### `NavierStokes\GaussianTailFlat.lean` (1 occurrences)
- L685: `let κ := Classical.choose (native_slot_length_lower r0 h hr0 hh)`

#### `NavierStokes\GlobalSlowProfiles.lean` (1 occurrences)
- L877: `Classical.choose (exists_step s hn previous)`

#### `NavierStokes\MatchingConeBounds.lean` (2 occurrences)
- L721: `(Classical.choose (actual_shape_source_threshold hj prep.sigma_pos (shapeConstant_one prep))))`
- L746: `have hM : Classical.choose`

#### `NavierStokes\OutgoingPulseBounds.lean` (2 occurrences)
- L771: `noncomputable def mainBound : ℝ := Classical.choose exists_mainPulse_bound`
- L1070: `noncomputable def templateJetBound (k : ℕ) : ℝ := 1 + Classical.choose (logTemplate_jet_bound k)`

#### `NavierStokes\OutgoingTail.lean` (1 occurrences)
- L73: `def stepBound : ℝ := Classical.choose exists_sigma_derivative_bound`

#### `NavierStokes\ParticularCopyBounds.lean` (3 occurrences)
- L318: `envelope n ((g n).coordinates (Classical.choose h) x.2).2 else 0`
- L329: `have hchoose : Classical.choose hex = k :=`
- L330: `K.unique n (Classical.choose hex) k x (Classical.choose_spec hex) hx`

#### `NavierStokes\PhysicalCurlCovariance.lean` (2 occurrences)
- L825: `cartesianPotential a (Classical.choose h) B x`
- L862: `· let j := Classical.choose h`

#### `NavierStokes\PhysicalWaveSum.lean` (1 occurrences)
- L561: `exact if hi : ∃ i : PolarCharts.Index, x ∈ PolarCharts.chartDomain a i then Classical.choose hi else 0`

#### `NavierStokes\PositiveRepresentatives.lean` (1 occurrences)
- L147: `exact if hp : p ∈ stableTarget a then Classical.choose hp else (1, p.2)`

#### `NavierStokes\PreparedOutgoing.lean` (2 occurrences)
- L45: `if hK : 0 < K then Classical.choose (caps K hK) else 1`
- L62: `have hFlam : F.data.core.lam < Classical.choose (caps K hK) := by`

#### `NavierStokes\PrimaryRepresentatives.lean` (1 occurrences)
- L95: `Classical.choose L.property.2`

#### `NavierStokes\PulseCone.lean` (1 occurrences)
- L784: `noncomputable def mainFirstBound : ℝ := 1 + Classical.choose`

#### `NavierStokes\PulseLag.lean` (1 occurrences)
- L195: `noncomputable def mainSecondBound : ℝ := 1 + Classical.choose`

#### `NavierStokes\R3\ComparisonCutoffs.lean` (1 occurrences)
- L151: `def derivativeConstant (n : ℕ) : ℝ := Classical.choose (exists_derivative_bound n)`

#### `NavierStokes\R3\LocalizedFluxEstimates.lean` (1 occurrences)
- L184: `def weightSecondDerivativeConstant : ℝ := Classical.choose exists_weight_second_derivative_bound`

#### `NavierStokes\SimilarityCoordinates.lean` (1 occurrences)
- L126: `Classical.choose (exists_positive_solution hp.1 hp.2.1 hp.2.2 p.2)`

#### `NavierStokes\SpatialBorelExtension.lean` (2 occurrences)
- L137: `Classical.choose (exists_template_bound ha m j k)`
- L196: `def localScale (j : ℕ) : ℕ := Classical.choose (exists_nat_gt ((2 : ℝ) ^ j * boundSum a ha j))`

#### `NavierStokes\TailCone.lean` (1 occurrences)
- L866: `noncomputable def resetJetConstant : ℝ := Classical.choose relative_first_jet_bound`

#### `NavierStokes\UniformPrimaryWeights.lean` (1 occurrences)
- L85: `Classical.choose (exists_surjective_nat (ℕ × ι))`

#### `NavierStokes\ValidBandGluing.lean` (2 occurrences)
- L29: `exact if h : ∃ i, x ∈ U i then f (Classical.choose h) x else 0`
- L45: `exact hf (Classical.choose h) i ⟨Classical.choose_spec h, hx⟩`

#### `NavierStokes\WaveStageContinuation.lean` (1 occurrences)
- L1919: `· have hb : B (polarCoordinates delta (Classical.choose he) x) ≠ 0 := by`

## 3. Fallback Totalization Patterns

Definitions of the form `if h : P then intendedObject else 0`.
Each must be audited: is the intended branch always selected on the proof path?

**Total fallback-to-zero patterns found: 18**

### `NavierStokes\CompactSmoothFamily.lean` line 31
```lean
noncomputable def family (K : Set Z) (F : P × Z → E) (p : P) : C(K, E) := by
  classical
  exact if h : Continuous (fun z : K => F (p, z)) then ⟨_, h⟩ else 0

omit [NormedAddCommGroup P] [NormedSpace ℝ P] [NormedSpace ℝ Z] [NormedSpace ℝ E] in
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\DependentSignedPhysicalFamily.lean` line 92
```lean
    (value : NativeLabel f.active → V) (L : BandLabel) : V := by
  classical
  exact if hL : L ∈ f.active then value ⟨L.val, L.property, hL⟩ else 0

@[simp] theorem valueAt_active {V : Type*} [Zero V]
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\GlobalSlowProfiles.lean` line 780
```lean
noncomputable def previousBeta {S : Set ℝ} {h C : ℝ} (s : Scheme S h C) (n : ℕ)
    (previous : (j : ℕ) → j < n → Admissible s j) (j : ℕ) : EvenProfile S :=
  if hj : j < n then (previous j hj).data.beta else 0

noncomputable def previousSource {S : Set ℝ} {h C : ℝ} (s : Scheme S h C) (n : ℕ)
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\PhysicalWaveSum.lean` line 561
```lean
noncomputable def chooseChart (a : ℝ) (x : Plane) : PolarCharts.Index := by
  classical
  exact if hi : ∃ i : PolarCharts.Index, x ∈ PolarCharts.chartDomain a i then Classical.choose hi else 0

theorem chooseChart_valid {a b : ℝ} (ha : 0 < a) {x : Plane}
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\R3\H3Curve.lean` line 88
```lean
def velocityLp (h : H3Curve u s) (t : ℝ) : Lp Space 2 (volume : Measure Space) := by
  classical
  exact if ht : t ∈ s then (h.approximation t ht).memLp.toLp (fun x => u (t, x)) else 0

theorem velocityLp_eq (h : H3Curve u s) {t : ℝ} (ht : t ∈ s) :
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\SmoothPathFamily.lean` line 31
```lean
noncomputable def pathFamily (F : P × ℝ → E) (p : P) : C(Icc a b, E) := by
  classical
  exact if h : Continuous (fun t : Icc a b => F (p, t)) then ⟨_, h⟩ else 0

omit [NormedAddCommGroup P] [NormedSpace ℝ P] [NormedSpace ℝ E] in
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\UniformAngularReset.lean` line 303
```lean
      linarith
  choose f hf using hex
  let g : E → E := fun d => if hd : d ∈ Metric.ball (0 : E) ε then f ⟨d, hd⟩ else 0
  have hspec : ∀ d (hd : d ∈ Metric.ball (0 : E) ε),
      (‖g d‖ ≤ r ∧ quadraticMap B A (g d) = d) ∧
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\UniformQuadraticBranch.lean` line 163
```lean
      (2 * ν * δ) (by positivity) hs hdebt
  choose cp hcp using fun p hp => (hpoints p hp).exists
  let c : V → E := fun p => if hp : p ∈ S then cp p hp else 0
  have hc : ∀ p ∈ S, ‖c p‖ ≤ 2 * ν * δ ∧ B p (c p) + A p (c p) (c p) = d p := by
    intro p hp
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `NavierStokes\ValidBandGluing.lean` line 29
```lean
noncomputable def representative [Zero E] (U : ι → Set D) (f : ι → D → E) (x : D) : E := by
  classical
  exact if h : ∃ i, x ∈ U i then f (Classical.choose h) x else 0

theorem mem_domain_iff {U : ι → Set D} {x : D} : x ∈ domain U ↔ ∃ i, x ∈ U i :=
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\ComparatorMaximalFields.lean` line 18
```lean

def maximalVelocityExtension (x : Space) (t : ℝ) : Space :=
  if ht : t ∈ Ico (0 : ℝ) L.duration then L.maximalVelocity ⟨t, ht⟩ x else 0

def maximalPressureExtension (x : Space) (t : ℝ) : ℝ :=
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\ComparatorMaximalFields.lean` line 21
```lean

def maximalPressureExtension (x : Space) (t : ℝ) : ℝ :=
  if ht : t ∈ Ico (0 : ℝ) L.duration then L.maximalPressure ⟨t, ht⟩ x else 0

theorem maximalVelocityExtension_eq (t : L.Time) :
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\ComparatorMaximalSolution.lean` line 35
```lean

def maximalDerivativeExtension (x : Space) (t : ℝ) : Space :=
  if ht : t ∈ Ico (0 : ℝ) L.duration then (maximalDerivativeField L ⟨t, ht⟩).field x else 0

theorem maximalDerivativeExtension_eq (t : L.Time) :
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\OrdinaryMaximalVorticityIntegral.lean` line 24
```lean
def maximalVorticityDensity (r : ℝ) : ℝ := by
  classical
  exact if hr : r ∈ Ico (0 : ℝ) L.duration then L.maximalVorticityNorm ⟨r,hr⟩ else 0

theorem maximalVorticityDensity_nonneg (r : ℝ) : 0 ≤ L.maximalVorticityDensity r := by
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\PacketProfileRecursion.lean` line 106
```lean
    (a : (i : ℕ) → i<p → Profile) : Profile :=
  if p=0 then 0 else if p=1 then primary else
    step O p (fun i => if hi : i<p then a i hi else 0)

/-- All finite profile families are restrictions of this one well-founded sequence. -/
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\SolutionDefinitions.lean` line 90
```lean
    Lp V 2 (volume : Measure ℝ³) := by
  classical
  exact if h : MemLp f 2 volume then h.toLp f else 0

/-- A spatially smooth path whose actual spatial derivative tensors belong to L²
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\TransverseHighSolveFields.lean` line 18
```lean
def highSolveDerivative : VectorField := by
  classical
  exact if h : Nonempty (Forcing P D raw) then (Classical.choice h).vectorDerivative I else 0

def highSolveCorrectorDerivative : VectorField := by
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `Euler\TransverseHighSolveFields.lean` line 22
```lean
def highSolveCorrectorDerivative : VectorField := by
  classical
  exact if h : Nonempty (Forcing P D raw) then (Classical.choice h).correctorDerivative I else 0

variable (h : Nonempty (Forcing P D raw))
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

### `ComparatorChallenges\Euler.lean` line 117
```lean
    Lp V 2 (volume : Measure ℝ³) := by
  classical
  exact if h : MemLp f 2 volume then h.toLp f else 0

/-- A spatially smooth path whose actual spatial derivative tensors belong to L²
```
**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.

## 4. Noncomputable Definition Classification

| Classification | Count | Audit Priority |
| --- | ---: | --- |
| conditional_fallback | 6 | VERY HIGH |
| existential_witness_selection | 37 | HIGH |
| arbitrary_extension | 1 | VERY HIGH |
| suprema_infima_selection | 5 | MEDIUM-HIGH |
| choice_with_spec | 2 | MEDIUM (lower if spec checked) |
| analytic | 5777 | LOW |

### conditional_fallback (6 defs)

- **`NavierStokes\CompactSmoothFamily.lean`** L29 `family`: `noncomputable def family (K : Set Z) (F : P × Z → E) (p : P) : C(K, E) := by`
- **`NavierStokes\DependentSignedPhysicalFamily.lean`** L89 `valueAt`: `noncomputable def valueAt {V : Type*} [Zero V]`
- **`NavierStokes\GlobalSlowProfiles.lean`** L778 `previousBeta`: `noncomputable def previousBeta {S : Set ℝ} {h C : ℝ} (s : Scheme S h C) (n : ℕ)`
- **`NavierStokes\SmoothPathFamily.lean`** L29 `pathFamily`: `noncomputable def pathFamily (F : P × ℝ → E) (p : P) : C(Icc a b, E) := by`
- **`Euler\SolutionDefinitions.lean`** L87 `toL2`: `noncomputable def toL2 {V : Type*} [NormedAddCommGroup V] (f : ℝ³ → V) :`
- **`ComparatorChallenges\Euler.lean`** L114 `toL2`: `noncomputable def toL2 {V : Type*} [NormedAddCommGroup V] (f : ℝ³ → V) :`

### existential_witness_selection (37 defs)

- **`NavierStokes\ActualMeanPhysicalData.lean`** L125 `Atlas`: `noncomputable def Atlas.physical {h : ℝ} {N Δ : ℕ} (A : Atlas h N Δ)`
- **`NavierStokes\ActualParticularPhysicalData.lean`** L1698 `actualIndex`: `noncomputable def actualIndex`
- **`NavierStokes\ActualSignedExterior.lean`** L115 `actualLabel`: `noncomputable def actualLabel (L : ActualSignedPhysicalData.NativeLabel (labels B N0)) :`
- **`NavierStokes\ActualSignedGeometry.lean`** L1277 `activeEnumeration`: `noncomputable def activeEnumeration : ℕ → ActivePair H v a reference chart :=`
- **`NavierStokes\ActualSlowAxis.lean`** L345 `tubeWidth`: `noncomputable def tubeWidth : ℝ := Classical.choose (exists_tube_of_pressure_eq hp hP0 F hΛ hsmall hσ)`
- **`NavierStokes\ActualSlowAxis.lean`** L352 `constructedTube`: `noncomputable def constructedTube : InitialTube (ReferenceJetBounds.referenceInput F hΛ) h P0 (5 / Λ)`
- **`NavierStokes\ConstructedSlowBase.lean`** L611 `nominalScales`: `noncomputable def nominalScales : ℕ → ℕ :=`
- **`NavierStokes\ConstructedSlowBase.lean`** L709 `modifiedScales`: `noncomputable def modifiedScales : ℕ → ℕ :=`
- **`NavierStokes\CorrectionInitialization.lean`** L3929 `choice`: `noncomputable def choice (B N0 : ℕ) : Choice B N0 := Classical.choice (choice_nonempty B N0)`
- **`NavierStokes\CorrectionInitializationNoOptions.lean`** L3940 `choice`: `noncomputable def choice (B N0 : ℕ) : Choice B N0 := Classical.choice (choice_nonempty B N0)`
- **`NavierStokes\EntranceAlignedBase.lean`** L1018 `scales`: `noncomputable def scales (c : ℝ) (hc : 0 < c) (upper : ℝ) (B : ℕ) : ℕ → ℕ :=`
- **`NavierStokes\FinalSlowBase.lean`** L634 `actualProfile`: `noncomputable def actualProfile : ProfileData := Classical.choice profileData_nonempty`
- **`NavierStokes\GaussianTailFlat.lean`** L683 `actualSlotFamily`: `noncomputable def actualSlotFamily (s : StripData D) (r0 h : ℝ)`
- **`NavierStokes\GlobalSlowProfiles.lean`** L875 `step`: `noncomputable def step {S : Set ℝ} {h C : ℝ} (s : Scheme S h C) {n : ℕ} (hn : 0 < n)`
- **`NavierStokes\JointResidualLimits.lean`** L120 `boundaryLimits`: `noncomputable def boundaryLimits (f : SpaceTime → V) (hext : AwayExtensions f)`
- **`NavierStokes\MatchingConeBounds.lean`** L716 `shapeScale`: `noncomputable def shapeScale {F : OutgoingProfile.Profile} {j : ℝ}`
- **`NavierStokes\MatchingDebtBounds.lean`** L462 `fixedBounds`: `noncomputable def fixedBounds (F : OutgoingProfile.Profile) (N : ℕ) : FixedBounds F N :=`
- **`NavierStokes\NominalConeAssembly.lean`** L986 `assemble`: `noncomputable def assemble {D : ℝ} (hF : OutgoingProfile.Specification F D)`
- **`NavierStokes\NominalProfile.lean`** L206 `resetSolver`: `noncomputable def resetSolver : ResetSolver := Classical.choice resetSolver_exists`
- **`NavierStokes\OutgoingPulseBounds.lean`** L771 `mainBound`: `noncomputable def mainBound : ℝ := Classical.choose exists_mainPulse_bound`
- **`NavierStokes\OutgoingPulseBounds.lean`** L1070 `templateJetBound`: `noncomputable def templateJetBound (k : ℕ) : ℝ := 1 + Classical.choose (logTemplate_jet_bound k)`
- **`NavierStokes\ParametricRadialExtension.lean`** L56 `parameterWindow`: `noncomputable def parameterWindow {S : Set ℝ} (hS : IsOpen S)`
- **`NavierStokes\ParticularCopyBounds.lean`** L314 `nativeEnvelope`: `noncomputable def nativeEnvelope (K : Cells (P × Plane) Frequency)`
- **`NavierStokes\PartitionedCovariance.lean`** L811 `constructedSlotSystem`: `noncomputable def constructedSlotSystem (D h : ℝ) (hh : 0 ≤ h) (vr vt : Plane) : SlotSystem D h vr vt :=`
- **`NavierStokes\PhysicalCurlCovariance.lean`** L820 `globalCartesianPotential`: `noncomputable def globalCartesianPotential (a : ℝ) (B : SpaceTime → ComplexVector)`
- **`NavierStokes\PhysicalWaveSum.lean`** L556 `CarrierData`: `noncomputable def CarrierData.withChart (c : CarrierData) (i : PolarCharts.Index) : CarrierData :=`
- **`NavierStokes\PhysicalWaveSum.lean`** L559 `chooseChart`: `noncomputable def chooseChart (a : ℝ) (x : Plane) : PolarCharts.Index := by`
- **`NavierStokes\PositiveRepresentatives.lean`** L145 `stableInverse`: `noncomputable def stableInverse (a : ℝ) (p : ℝ × ℝ) : ℝ × ℝ := by`
- **`NavierStokes\PreparedOutgoing.lean`** L119 `prepared`: `noncomputable def prepared : PreparedProfile := Classical.choice exists_prepared`
- **`NavierStokes\PrimaryGeometryAssembly.lean`** L459 `prepared`: `noncomputable def prepared (hcone : LeadingStressWeights.FullTrueCone v)`
- … and 7 more

### arbitrary_extension (1 defs)

- **`NavierStokes\WaveDataReindex.lean`** L22 `zeroExtend`: `noncomputable def zeroExtend {V : Type*} [Zero V] (e : I ↪ I') (f : I → V) : I' → V :=`

## 5. Structure Definitions

Structures can act as semantic laundering boundaries: a field stored
as a constructor parameter may never be independently proved for the
final selected witness.

**Total structure declarations: 402**

### Structures with ≥ 3 fields (370 total, showing top 40)

| File | Structure | Fields | Field Names |
| --- | --- | ---: | --- |
| `Euler\ParentPacketSourceData.lean` | `LowBounds` | 69 | Be, Bc, L, r, K, Be_nonneg, Bc_nonneg, L_lower … (+61) |
| `Euler\PacketGeometryData.lean` | `PhysicalGeometryData` | 62 | center, B, B₁, M, E, m, v, r … (+54) |
| `NavierStokes\HeatedOutgoing.lean` | `Specification` | 54 | angular_smooth, axial_smooth, momentum_smooth, pressure_smooth, angular_positive, axial_unchanged, mass_unchanged, angular_unchanged … (+46) |
| `NavierStokes\GlobalSlowProfiles.lean` | `Scheme` | 52 | domain, nonzero_scale, lam, lam_pos, a, b, B, a_pos … (+44) |
| `NavierStokes\ExtendedHeatedOutgoing.lean` | `Specification` | 50 | neighborhood_open, neighborhood_contains, fields_smooth, angular_positive, axial_unchanged, mass_unchanged, angular_unchanged, mass_integrable … (+42) |
| `NavierStokes\OutgoingDilation.lean` | `DilatedSpecification` | 46 | angular_smooth, axial_smooth, momentum_smooth, pressure_smooth, angular_positive, mass_integrable, angular_integrable, mass_zero … (+38) |
| `NavierStokes\PrimaryPulseBounds.lean` | `PhaseConstruction` | 45 | phase, V, openV, lam, c0, u, L, viscosity … (+37) |
| `NavierStokes\ActivationStocks.lean` | `SmoothPair` | 42 | actual, reference, factor, actual_smooth, reference_smooth, factor_smooth, difference, actual … (+34) |
| `Euler\MeanPacketData.lean` | `Data` | 35 | T, T_pos, ℓ, ℓ_pos, ℓ_le_one, F, F₁, F₂ … (+27) |
| `Euler\BaseEulerParent.lean` | `Input` | 34 | T, T_pos, field, derivative, time_derivative, divergence, B, R … (+26) |
| `Euler\PacketInductionScales.lean` | `Scales` | 34 | J, D, X, δ, stage_large, base_power, x_large, delta_pos … (+26) |
| `Euler\PacketSourceGeometryData.lean` | `Guards` | 33 | CM, CH, ζ, radius, y, δ, hchild, CM_nonneg … (+25) |
| `NavierStokes\ModulatedProfileAssembly.lean` | `NominalBounds` | 32 | modulation, after_initial, before_repair, relaxed, true_boundary, true_following, parameter, etaRadius … (+24) |
| `Euler\TransversePacketBudget.lean` | `Budget` | 31 | g, positive, initial_one, neighborhood, neighborhood_measurable, neighborhood_open, support_subset, neighborhood_halfball … (+23) |
| `NavierStokes\StressAlgebra.lean` | `AxialMomentData` | 30 | W, Wx, U, Ux, Uη, E, Eη, P … (+22) |
| `NavierStokes\SignedMeanGain.lean` | `NativeData` | 28 | width, exponent, vr, vt, slots, determinant, index, index_pos … (+20) |
| `NavierStokes\ModulatedProfileAssembly.lean` | `LoopData` | 26 | parameter, etaRadius, one_lt_etaRadius, etaRadius_lt_target, modulation, after_initial, before_repair, a … (+18) |
| `Euler\PacketInductionStage.lean` | `Stage` | 26 | parent, state, low, time, time_nonneg, time_zero, time_lower, horizon_eq … (+18) |
| `Euler\TransversePacketForwardBudget.lean` | `Budget` | 26 | g, positive, initial_one, neighborhood, neighborhood_measurable, neighborhood_open, support_subset, neighborhood_halfball … (+18) |
| `NavierStokes\PhysicalStageBounds.lean` | `WaveData` | 25 | lowerRadius, upperRadius, nativeWidth, slowBound, frequencyBound, alpha, shift, harmonics … (+17) |
| `Euler\PacketInitialInput.lean` | `Input` | 25 | parent, label, low, normal, normal_unit, coordinates, support, support_compact … (+17) |
| `Euler\PacketInitializedRadiusPolynomial.lean` | `RadiusPrimitives` | 25 | one, total_time, mean_time, history_inverse_time, mean_inverse_time, history_gram, original_joined, original_mean … (+17) |
| `Euler\PhysicalGraphFlowBounds.lean` | `Data` | 25 | time_nonneg, A, A₁, time_derivative, periodic, periodic_time, divergence, B … (+17) |
| `NavierStokes\OffplaneCorrectionExtensions.lean` | `SupportedContinuation` | 24 | value, smooth, supported, agrees, value, smooth, supported, agrees … (+16) |
| `NavierStokes\PrimaryGeometryAssembly.lean` | `Prepared` | 24 | N, threshold, M, u, eta, target, one_le_M, u_pos … (+16) |
| `NavierStokes\CorrectionStep.lean` | `NativeControl` | 23 | cells, phasePatch, background, frame, envelope, realControl, imagControl, envelope_nonneg … (+15) |
| `NavierStokes\LiftedMeanResidual.lean` | `MeanHypotheses` | 23 | isOpen, radius_smooth, radius_ne, profile_smooth, base_smooth, mean_smooth, pressure_smooth, oscillation_smooth … (+15) |
| `NavierStokes\OutgoingProfile.lean` | `Specification` | 23 | amplitude_smooth, angular_smooth, axial_smooth, momentum_smooth, pressure_smooth, angular_positive, amplitude_bounds, mass_integrable … (+15) |
| `Euler\MeanPacketSobolevData.lean` | `SobolevData` | 23 | Rc, M, CF, CF₁, CH, CM, Cf, radius_lower … (+15) |
| `NavierStokes\StressAlgebra.lean` | `AngularMomentData` | 22 | W, Wx, H, Hx, Hη, U, Uη, I … (+14) |
| `Euler\ParentPacketLabelData.lean` | `LabelData` | 22 | K, K_one, displacement, velocity, acceleration, displacement_match, velocity_match, acceleration_match … (+14) |
| `NavierStokes\ActualStageEstimates.lean` | `RunData` | 21 | invariant, step, particular, particularPotential, signedPotential, particularPressure, signedPressure, particularPotential_exponent … (+13) |
| `NavierStokes\SignedMeanGain.lean` | `Geometry` | 21 | coord, region, patch, leftWeight, rightWeight, left_pos, right_pos, epsilon … (+13) |
| `Euler\ChildParticleFieldBounds.lean` | `Data` | 21 | parentDisplacement, parentVelocity, parentAcceleration, K, K_one, parentDisplacement_bound, parentVelocity_bound, parentAcceleration_bound … (+13) |
| `Euler\PacketForwardRadiusPolynomial.lean` | `RadiusPrimitives` | 21 | one, total_time, mean_time, mean_inverse_time, original_forward, original_mean, forward_radius, forward_frame … (+13) |
| `NavierStokes\ActualCycleExcluded.lean` | `SimilarityData` | 20 | h, h_pos, inner, outer, inner_pos, inner_lt_outer, leftWeight, rightWeight … (+12) |
| `NavierStokes\AxisOperators.lean` | `BoundedBilinearJetFamily` | 20 | value, boundConstant, bound_nonneg, cont, deriv, add_left, smul_left, add_right … (+12) |
| `NavierStokes\CorrectionInitialization.lean` | `PrimaryMeanData` | 20 | exponent_pos, gauge_length, operators, base, localOperators, base_smooth, profile, mean_zero … (+12) |
| `NavierStokes\CorrectionInitializationNoOptions.lean` | `PrimaryMeanData` | 20 | exponent_pos, gauge_length, operators, base, localOperators, base_smooth, profile, mean_zero … (+12) |
| `NavierStokes\CycleContinuationInvariant.lean` | `MeanConfiguration` | 20 | time, clock, patch, coordinate, inner, outer, length, exponent … (+12) |

## 6. Custom Metaprogramming and Notation

**No custom syntax/macro/elab declarations found.** This is positive evidence.

**`letI`/`haveI` instance overrides:** 0 (review for hidden typeclass manipulation)

**`@[simp]` lemma registrations:** 1267

**`abbrev` declarations:** 894 (abbreviations are definitionally transparent)

## 7. Build Configuration Audit

**Lean toolchain:** `leanprover/lean4:v4.34.0-rc2`

### `lakefile.toml` (SHA256: `2245aa9f247507d8…`)
```
name = "NavierStokesAndEuler"
version = "0.1.0"
defaultTargets = ["NavierStokes", "Euler", "ComparatorChallenges"]

[[require]]
name = "mathlib"
scope = "leanprover-community"
git = "https://github.com/leanprover-community/mathlib4.git"
rev = "v4.34.0-rc2"

[[require]]
name = "Comparator"
scope = "leanprover"
git = "https://github.com/leanprover/comparator.git"
rev = "v4.34.0-rc2"

[[lean_lib]]
name = "NavierStokes"
globs = ["NavierStokes", "NavierStokes.+"]

[[lean_lib]]
name = "Euler"
leanOptions = { autoImplicit = false, warningAsError = true }
globs = ["Euler", "Euler.+"]

[[lean_lib]]
name = "ComparatorChallenges"
globs = ["ComparatorChallenges.+"]

[[lean_lib]]
name = "NavierStokesReview"
srcDir = "NavierStokesReview/src"
globs = ["extensions.+", "external_semantic.+", "completions.+", "refutations.+"]

```

### Dependencies (lake-manifest.json)

| Package | Type | URL/Path | Rev |
| --- | --- | --- | --- |
| `Comparator` | git | `https://github.com/leanprover/comparator.git` | `19e111e2141c…` |
| `mathlib` | git | `https://github.com/leanprover-community/mathlib4.git` | `85e3a25e006c…` |
| `lean4export` | git | `https://github.com/leanprover/lean4export` | `cacf989bd75f…` |
| `plausible` | git | `https://github.com/leanprover-community/plausible` | `d9598f07b1bc…` |
| `LeanSearchClient` | git | `https://github.com/leanprover-community/LeanSearchClient` | `ba67e212be11…` |
| `importGraph` | git | `https://github.com/leanprover-community/import-graph` | `d8823026ac7e…` |
| `proofwidgets` | git | `https://github.com/leanprover-community/ProofWidgets4` | `a8acbfd87375…` |
| `aesop` | git | `https://github.com/leanprover-community/aesop` | `18889deb9e83…` |
| `Qq` | git | `https://github.com/leanprover-community/quote4` | `507746ab8f4b…` |
| `batteries` | git | `https://github.com/leanprover-community/batteries` | `d54dddc581e0…` |
| `Cli` | git | `https://github.com/leanprover/lean4-cli` | `ab3a82db9fea…` |

### Comparator Configurations

#### `Euler.json`
```json
{
  "challenge_module": "ComparatorChallenges.Euler",
  "solution_module": "Euler.Solution",
  "enable_nanoda": true,
  "theorem_names": [
    "Euler.euler_breakdown_R3",
    "Euler.exists_compact_smooth_euler_singularity"
  ],
  "permitted_axioms": [
    "propext",
    "Quot.sound",
    "Classical.choice"
  ]
}

```

#### `NavierStokes.json`
```json
{
  "challenge_module": "ComparatorChallenges.NavierStokes",
  "solution_module": "NavierStokes.ComparatorSolution",
  "enable_nanoda": true,
  "theorem_names": [
    "NavierStokes.Comparator.navier_stokes_breakdown_R3",
    "NavierStokes.Comparator.navier_stokes_breakdown_periodic"
  ],
  "permitted_axioms": [
    "propext",
    "Quot.sound",
    "Classical.choice"
  ]
}

```

## 8. Function.extend / Arbitrary Extension Patterns

**1 `Function.extend` occurrences:**

- `NavierStokes\WaveDataReindex.lean` L23: `Function.extend e f 0`
  ```lean
  /-- An injective extension with a specified zero value off the image. -/
  noncomputable def zeroExtend {V : Type*} [Zero V] (e : I ↪ I') (f : I → V) : I' → V :=
    Function.extend e f 0
  
  @[simp] theorem zeroExtend_apply {V : Type*} [Zero V] (e : I ↪ I') (f : I → V) (i : I) :
  ```

## 9. Filter.bot Occurrences (Vacuity Risk)

**0 `Filter.bot` references (each could make a limit statement vacuous)**


## Conclusion

This scan is a regex-level pre-audit. It identifies locations for deeper
semantic inspection but cannot distinguish benign from load-bearing uses.
Each high-priority item requires manual or Lean-level verification that:

1. Every `Classical.choice`/`choose` witness is either proved independent
   of the selection or consumed with the correct identity.
2. Every fallback-to-zero definition has its good branch selected on the
   complete endpoint path.
3. Every structure field is independently proved (not just stored as a
   constructor parameter) for the final selected witness.
4. No build-level plugin, generated file, or patched dependency injects
   trust outside the audited source.
