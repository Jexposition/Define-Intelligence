# Full Verification Ledger

Total `.lean` files tracked (excluding `.lake`): 2696

## Hard Syntax Bypasses Found

### ComparatorChallenges.NavierStokes
- Line 153: For any derivative order $m$ and any decay rate $K$, there exists a constant $C$

### Euler.AllOrderCorrectionBudget
- Line 24: constant : ℝ
- Line 34: (A.metricBudget period hT.le metric (q+1)) ≤ constant
- Line 42: decay : ∀ q hq, 2*constant*((spatial q hq).B0+delta)*T ≤ initialRadius/2
- Line 46: small : ∀ q hq, 2*(spatial q hq).residual*Real.exp (3*constant*T) ≤ delta/2
- Line 48: radius_eq : ∀ q hq t, radius t=initialRadius-2*constant*((spatial q hq).B0+delta)*t.val
- Line 69: (A.metricBudget period hT.le B.metric (q+1)) B.constant B.delta B.initialRadius

### Euler.AngleMeanZeroPrimitive
- Line 10: zero integral of the forcing; subtracting the actual mean fixes the constant.

### Euler.BaseEulerLabelData
- Line 5: label bound with one explicit constant, independent of derivative order. -/

### Euler.BaseEulerState
- Line 5: compact β-family. A single positive time and a single label constant

### Euler.BaseInductionStageNoOptions
- Line 24: `Quot.sound` occur in its axiom dependencies.

### Euler.BoundedTensorCoordinates
- Line 7: reassembly constant. -/

### Euler.ContinuousBoundedTensor
- Line 7: and therefore has constant one. -/

### Euler.ContinuousForcingTranslation
- Line 82: ordinary L² spatial derivative with constant one. -/

### Euler.ContinuousSpatialFamily
- Line 10: constant. No uniform-path differentiability is assumed.

### Euler.CorrectionAssemblyPressureParity
- Line 61: In particular parity is an exact identity, not merely equality modulo a constant. -/

### Euler.CylinderDirichletSobolev
- Line 11: jets lift to L² operator paths with constant one, and the true fixed-space

### Euler.CylinderDirichletTimeBounds
- Line 13: jets lift to L² operator paths with constant one, and the true fixed-space

### Euler.CylinderEndpointData
- Line 10: spatially constant nonzero vector is silently treated as L² data.

### Euler.CylinderPathProductBounds
- Line 10: The only norm equivalence constant is the fixed size of the H6 array.

### Euler.DivCurlRecovery
- Line 173: constant is independent of the field and of the support of its Laplacian. -/

### Euler.DivCurlTensorRecovery
- Line 88: energies. The constant is fixed by the derivative order alone. -/

### Euler.EulerProof
- Line 14255: lower bound.  No numerical approximations occur in the constant. -/
- Line 14764: used before (32), with the explicit constant `20`. -/
- Line 16578: explicit constant and the power of Θ used in the source. -/
- Line 18262: global Lipschitz constant in the state variable.  Finite-interval solutions
- Line 19243: base constant; the previous frequency power; inverse support and spike scales;

### Euler.FieldTowerPointwiseGevrey
- Line 35: external Sobolev block, with a fixed base-order evaluation constant. -/

### Euler.FiniteEnergyTruncation
- Line 319: uniform finite-energy truncation. The numerical constant is inessential. -/

### Euler.H6PressureInverse
- Line 104: The constant depends on q and base coefficient bounds, and is independent of the external cutoff N. -/

### Euler.HilbertCoerciveGevrey
- Line 134: constant, not the derivative-order radius. -/

### Euler.HilbertQuadraticFlow
- Line 7: removes the normalization by a constant rescaling of time. -/

### Euler.IsometricActionWords
- Line 9: independent of the translation parameter, with constant one and no radius

### Euler.LinearDuhamelSobolevGevrey
- Line 10: shift at the same input/output radius. Every constant is a fixed polynomial

### Euler.LinearDuhamelWeighted
- Line 8: its constant directly from the relative homogeneous propagator bound. The
- Line 48: constant. Neither the maximum nor minimum of the profile appears. -/

### Euler.LpOperatorFieldPath
- Line 11: actual L² operators without a support-margin constant.

### Euler.LpSupportedConstructedEvolution
- Line 10: on this genuine homogeneous propagator and is then inherited with constant

### Euler.LpSupportedTranslation
- Line 12: margin is qualitative and does not occur in any operator-norm constant.

### Euler.MeanClassicalWordBounds
- Line 10: Hq sums and external ordered-word sums transfer with constant one, including
- Line 153: words with constant one, and without a radius change. -/

### Euler.MeanFixedTranslation
- Line 9: same constant throughout the translated coefficient family.

### Euler.MeanHarmonicInterior
- Line 6: The constant is built from fixed smooth cutoffs and the already proved Fourier

### Euler.MeanPacketBudget
- Line 113: period factors from averaging and constant extension cancel exactly. -/

### Euler.MeanPacketCylinderFields
- Line 6: # Actual mean outputs as constant-angle cylinder paths

### Euler.MeanTimeContinuousTranslation
- Line 10: or additional constant.

### Euler.MeanTranslatedInverse
- Line 8: coercivity constant. Its solution for translated forcing is exactly the

### Euler.NormalPacketFrequencyGuards
- Line 20: unfold sourceConstant EulerPacketParameterEnvelope.constant

### Euler.OrdinaryH3Energy
- Line 5: The pressure term vanishes exactly. The constant uses only the reference

### Euler.OrdinaryH3Products
- Line 5: distributions use H² point evaluation. The constant is independent of

### Euler.PacketCommonRadius
- Line 15: constant, and actual source solver is preserved. -/

### Euler.PacketCorrectionCoefficientBudget
- Line 6: Every constant is independent of the jet order, truncation level and frequency.

### Euler.PacketExactGlobalShear
- Line 6: only a fixed source constant divided by the frequency. -/

### Euler.PacketForwardGlobalShear
- Line 7: only a fixed source constant divided by the frequency. -/

### Euler.PacketForwardRadiusPolynomial
- Line 7: The homogeneous growth constant is arbitrary and remains an input. -/

### Euler.PacketGeometryInitialAmplitude
- Line 15: def constant : ℝ := coefficientCost polynomial
- Line 18: theorem constant_pos : 0 < constant := coefficientCost_pos _
- Line 24: theorem envelope_bound (X : ℝ) (hX : 1 ≤ X) : envelope X ≤ constant*X^degree := by
- Line 51: J.primaryAmplitude hball ≤ constant*X^degree*Real.exp (-x/8) := by
- Line 97: J.primaryAmplitude hball ≤ constant*X^degree*Real.exp (-x/8) := by

### Euler.PacketGeometryPressureCosts
- Line 94: cutoffBound*(8232*exp 9*P.horizon^5+4*P.horizon*(constant*1^degree)) := by

### Euler.PacketInitialInput
- Line 94: (A.parent.ell⁻¹)^s*k^s*(EulerPacketInitialAmplitude.constant*EulerPacketInitialCost.sourceConstant s*

### Euler.PacketInitializedPointwiseChoice
- Line 36: The radius 4/ρ0 and amplitude constant depend only on the fixed source data. -/

### Euler.PacketInitialSummability
- Line 29: (EulerPacketInitialAmplitude.constant*EulerPacketInitialCost.sourceConstant s)

### Euler.PacketKnownTermSums
- Line 6: mean force, and the angle-constant BB term is absent from the high force.

### Euler.PacketLiftedCurl
- Line 4: Curl in the constant lifted directions `(κ eᵢ, m₀ᵢ)` on the actual periodic

### Euler.PacketParameterEnvelope
- Line 16: def constant (Cθ CB Cξ : ℝ) : ℝ := 8+1120*(2*Cθ)^10+CB+Cξ
- Line 19: 0 < constant Cθ CB Cξ := by
- Line 20: unfold constant
- Line 38: parameterEnvelope J (constant Cθ CB Cξ) c 20 1000 X n := by
- Line 96: constant Cθ CB Cξ*(F*E) := by
- Line 97: unfold parameterSize constant

### Euler.PacketParentLabelBounds
- Line 8: coefficient bounds.  The embedding constant is independent of the external

### Euler.PacketParentLabelCoefficients
- Line 61: its constant identity, without making the identity an L² datum. -/

### Euler.PacketParentTransverseCosts
- Line 7: no inverse solver norm or forcing-dependent constant appears in the final

### Euler.PacketShortTimePropagator
- Line 8: The resulting forward budget has constant profile one and propagator cost two. -/

### Euler.PacketSourceParameterScales
- Line 5: Polynomial factors include the growing base core constant and inverse

### Euler.PacketSourcePropagator
- Line 164: physical propagator constant C becomes the polynomial 3 F³ C in H3. -/

### Euler.PacketTerminalDatum
- Line 6: has period 2π.  The constant vector is multiplied by the spatial cutoff

### Euler.ParameterSobolevInverse
- Line 7: indices. The resulting constant is a fixed polynomial recursion in the

### Euler.ParentForwardRadiusPolynomial
- Line 8: propagator constant is retained, without replacing the growth profile. -/

### Euler.ParentGeometryInitialBounds
- Line 64: J.primaryAmplitude hball ≤ EulerPacketInitialAmplitude.constant*
- Line 80: (G.ell⁻¹)^s*k^s*(EulerPacketInitialAmplitude.constant*EulerPacketInitialCost.sourceConstant s*
- Line 104: _ ≤ (G.ell⁻¹)^s*k^s*(EulerPacketInitialAmplitude.constant*

### Euler.ParentNeighborThreshold
- Line 15: def forwardThreshold : ℝ := constant*4^degree
- Line 18: (constant*(2*(1+CM+CH))^degree)*4^degree
- Line 52: L.strainDifferenceCost ≤ constant*(1+L.K)^degree := by
- Line 64: have hb := polynomial_le_monomial constant L.K 0 0 k 1 degree 80 c

### Euler.ParentNormalPacketParameters
- Line 21: EulerPacketParameterEnvelope.constant C (boundaryConstant gradientConstant) terminalCap

### Euler.ParentPacketBadRatioPolynomial
- Line 8: interval keeps its absolute size constant. -/
- Line 98: def constant : ℝ := coefficientCost polynomial
- Line 101: theorem constant_pos : 0 < constant := coefficientCost_pos _
- Line 110: envelope K Ti Hi CM CH ≤ constant*(1+K+Ti+Hi+CM+CH)^degree := by
- Line 133: def badConstant : ℝ := cutoffBound*(8232*Real.exp 9+4*constant)
- Line 140: cutoffBound*(8232*Real.exp 9*Θ^5+4*Θ*(constant*X^degree)) ≤ badConstant*X^degree*Θ^5 := by
- Line 149: have hsecond : 4*Θ*(constant*X^degree) ≤ 4*constant*(X^degree*Θ^5) := by
- Line 151: _ ≤ 4*Θ^5*(constant*X^degree) := by gcongr; positivity [constant_pos]
- Line 154: _ ≤ cutoffBound*(8232*Real.exp 9*(X^degree*Θ^5)+4*constant*(X^degree*Θ^5)) :=
- Line 208: constant*(1+L.K+Ti+P.shear⁻¹+A.CM+A.CH)^degree :=
- Line 226: 4*P.horizon*(constant*(1+L.K+Ti+P.shear⁻¹+A.CM+A.CH)^degree))*Real.exp (-(1/(4*P.sigma))) := by

### Euler.ParentPacketForwardInput
- Line 7: the constant one, proved by the actual tangent equation. -/

### Euler.ParentPacketFrames
- Line 45: (SmoothTimeField.constant (ContinuousLinearMap.id ℝ Space)).add

### Euler.ParentPacketHistoryPolynomial
- Line 5: polynomial dependence on the parent label constant and reciprocal

### Euler.ParentPacketNeighborBounds
- Line 6: its computed Lipschitz constant retains that factor as well. -/

### Euler.ParentPacketNeighborPolynomial
- Line 32: def constant : ℝ := coefficientCost polynomial
- Line 35: theorem constant_pos : 0 < constant := coefficientCost_pos _
- Line 62: envelope K Ti Ei Hi CM CH ≤ constant*(1+K+Ti+Ei+Hi+CM+CH)^degree := by
- Line 183: EulerParentNeighborCost.constant*
- Line 192: (EulerParentNeighborCost.constant*
- Line 204: (EulerParentNeighborCost.constant*(2*(1+CM+CH))^EulerParentNeighborCost.degree)*
- Line 221: _ ≤ EulerParentNeighborCost.constant*
- Line 224: _ ≤ EulerParentNeighborCost.constant*
- Line 231: ((EulerParentNeighborCost.constant*(2*(1+CM+CH))^EulerParentNeighborCost.degree)*

### Euler.ParentPacketNeighborScaleGuard
- Line 5: majorant under fixed degree and constant guards. Thus the small support
- Line 54: (hcost : (EulerParentNeighborCost.constant*(2*(1+CM+CH))^degree)*4^degree ≤ k)
- Line 61: (EulerParentNeighborCost.constant*(2*(1+CM+CH))^degree)
- Line 72: (hcost : (EulerParentNeighborCost.constant*(2*(1+CM+CH))^degree)*4^degree ≤

### Euler.ParentRenewalScaleCosts
- Line 5: envelope uses the constant sequence a=2, so its summability does not assume

### Euler.ParentShortForwardRadius
- Line 7: polynomial, using its proved constant profile and physical propagator cost 2. -/

### Euler.PolynomialCostMajorant
- Line 6: x ≥ 1. This extracts an actual degree and constant for scalar cost formulas. -/

### Euler.ShortTimeLinearGrowth
- Line 5: constant is two under the stated smallness condition. -/

### Euler.SmallCorrectionScales
- Line 5: growth constant belongs to the identity-metric equation, not to an

### Euler.SmoothCoefficientTimeRestriction
- Line 58: derivative bound with exactly the same constant. -/

### Euler.SmoothFlowDeformation
- Line 59: (SmoothTimeField.constant (ContinuousLinearMap.id ℝ E)).add

### Euler.SmoothTimeFieldBilinear
- Line 32: def constant (v : V) : SmoothTimeField K E V where
- Line 44: (constant (K := K) (E := E) v).field t x = v := rfl

### Euler.SmoothTimeFieldDerivativeBounds
- Line 4: constant, and the bound is uniform in both the time and label variables. -/

### Euler.StageDisplacementBound
- Line 37: needed; the transported quantity need not be constant along trajectories. -/

### Euler.TensorCoordinateEnergyBound
- Line 7: therefore gives a finite constant converting the sum of the scalar coordinate
- Line 40: scalar coordinate evaluations, with a constant depending only on its order. -/

### Euler.TimeWeakDerivative
- Line 158: representative: a terminal primitive plus a constant. -/

### Euler.TransverseEndpointCoordinates
- Line 9: explicit affine constant minus the same fixed-space variational correction.

### Euler.TransverseGevreyInverse
- Line 7: Every constant is an explicit polynomial in the interval length, frame
- Line 180: with only the fixed coefficient multiplication constant. -/

### Euler.TransverseStrongEstimates
- Line 6: These bounds use the lower frame constant and coefficient norms. In particular

### Euler.VolumeSobolevComposition
- Line 5: of variables, with an explicit finite-order composition constant. -/

### NavierStokes.ActiveAnnulusWeight
- Line 423: positive lower constant for the explicit product weight. -/
- Line 541: profile chart. The lower constant and the weight are independent of order. -/

### NavierStokes.ActualCandidateConstruction
- Line 353: pressure; no new integration constant or choice enters a later stage. -/

### NavierStokes.ActualCurrentParticularBounds
- Line 871: The constant is chosen before the label, current band, and physical point.

### NavierStokes.ActualCyclePeriodicity
- Line 69: theorem constant {f : D → ℂ} (hf : TranslationOn U v f) :
- Line 100: exact ha.sub (constant (ha 0))
- Line 149: ((CoefficientsTranslation.constant (hg.radius.map (fun R => ((R⁻¹ : ℝ) : ℂ)))).mul hr)).add
- Line 150: ((CoefficientsTranslation.constant (hg.radius.map (fun R => (((R ^ 2)⁻¹ : ℝ) : ℂ)))).mul
- Line 170: ((CoefficientsTranslation.constant (hg.radius.map (fun R => (((R ^ 2)⁻¹ : ℝ) : ℂ)))).mul
- Line 171: (((CoefficientsTranslation.constant (TranslationOn.const (2 : ℂ))).mul
- Line 181: (((ha 1).mul (CoefficientsTranslation.constant (hg.radius.map (fun R => (R : ℂ)⁻¹)))).mul
- Line 192: · exact (CoefficientsTranslation.constant (hg.radius.map (fun R => ((R⁻¹ : ℝ) : ℂ)))).mul
- Line 204: ((CoefficientsTranslation.constant (TranslationOn.const (g.viscosity : ℂ))).mul
- Line 231: fun i => CoefficientsTranslation.constant ((hB.component i).map₂ (hM.component i) (· + ·))

### NavierStokes.ActualGaussianCoverage
- Line 869: ⟨hreal.constant, hreal.constant_ge_one, hreal.coordinate_power, hreal.coordinate_bound⟩)
- Line 1328: ⟨hreal.constant, hreal.constant_ge_one, hreal.coordinate_power, hreal.coordinate_bound⟩)

### NavierStokes.ActualInitialExcluded
- Line 589: constant := 1

### NavierStokes.ActualParticularControl
- Line 45: error constant work for all nonzero harmonics, without a bound on `j`. -/
- Line 517: with one constant before both.  This never infers uniformity over an
- Line 657: constant := K

### NavierStokes.ActualParticularGaussian
- Line 31: constant := 1
- Line 227: all-power estimate.  Its finite modal sum changes the constant, not its

### NavierStokes.ActualPhaseJetBounds
- Line 459: derivative. Only the constant and the slow power depend on its order. -/

### NavierStokes.ActualPrimaryBounds
- Line 1210: bound, with the constant chosen before the index. -/

### NavierStokes.ActualPrimaryCovariance
- Line 759: exponent.  The new constant is one finite sum of powers of the original

### NavierStokes.ActualSignedControl
- Line 559: one constant before both the label and the copy. -/

### NavierStokes.ActualSignedGaussian
- Line 138: constant := 1

### NavierStokes.ActualSignedStageControls
- Line 582: single derivative constant still precedes every label, band and copy. -/

### NavierStokes.AllBandBaseJets
- Line 71: all positive scales, with the same constant. -/

### NavierStokes.AnnularEndpoint
- Line 77: the same outer support constant.  No sign or size assumption on `C` is needed. -/

### NavierStokes.AppendixHeatResults
- Line 88: The explicit constant is independent of the argument on the whole half-line. -/
- Line 142: explicit remainder constant and no analyticity assumption. -/

### NavierStokes.AppendixJoiningResults
- Line 39: constant angular source. This keeps its margin on the full printed range. -/

### NavierStokes.AssembledSlowBase
- Line 639: phi := constant S C * radialPullback P.f P.f_smooth hD

### NavierStokes.AxisContraction
- Line 586: not a hypothesis about the nonlinear map's Lipschitz constant. -/

### NavierStokes.AxisEvaluation
- Line 414: coefficient space. The constant is uniform in the parameter coordinate. -/

### NavierStokes.AxisInverseFactors
- Line 104: inserted before that inverse, with one algebra constant. -/
- Line 188: operator to a zero-constant inverse. These coefficients need not themselves
- Line 209: algebra constant apiece in the mixed derivative estimate. -/
- Line 252: or radial averaging, acquires the same one-constant-per-factor bound. -/

### NavierStokes.AxisResolvent
- Line 475: map to the constant coefficient representing `1`. -/

### NavierStokes.AxisWeightEstimates
- Line 481: constant 5120/ε. Neither individual derivative is assumed bounded. -/

### NavierStokes.BandReindexedSignedMeanGain
- Line 70: so none of its uniform coefficient bounds acquire a label-dependent constant. -/

### NavierStokes.BaseChartJets
- Line 526: of `BasePhaseGeometry`. The constant is chosen before the band or label. -/
- Line 858: constant on every actual enlarged positive-time cell above one band.

### NavierStokes.BasePhaseGeometry
- Line 299: constant and does not strengthen this geometric input. -/

### NavierStokes.BaseResidual
- Line 153: power per derivative. The constant is derived by compactness and scaling. -/
- Line 249: radius adds a constant but no further loss of powers. -/

### NavierStokes.BlowupImplication
- Line 132: positive multiplicative constant must diverge as well. An actual Sobolev

### NavierStokes.CandidateFromLimits
- Line 151: directions and every output component. The constant is uniform in these choices. -/

### NavierStokes.ClosedIntervalCkOperators
- Line 182: def constant (k : ℕ) (a : E) : CK (E := E) k :=
- Line 185: @[simp] theorem constant_value (k : ℕ) (a : E) (x : I) : value k (constant k a) x = a := rfl
- Line 187: theorem norm_constant_zero (a : E) : ‖constant 0 a‖ = ‖a‖ := by
- Line 194: · have he := ((value 0 (constant 0 a)).norm_coe_le_norm leftEndpoint).trans
- Line 195: (norm_value_le (constant 0 a))
- Line 202: have he := ((value 0 (coefficientOperator 0 B hB (constant 0 a))).norm_coe_le_norm x).trans
- Line 204: rw [coefficientOperator_value 0 B hB (constant 0 a) x, constant_value] at he
- Line 206: (coefficientOperator 0 B hB).le_opNorm (constant 0 a))
- Line 215: have he := ((value 0 (quadraticOperator 0 A hA (constant 0 a) (constant 0 b))).norm_coe_le_norm x).trans
- Line 217: rw [quadraticOperator_value 0 A hA (constant 0 a) (constant 0 b) x,
- Line 220: (quadraticOperator 0 A hA).le_opNorm₂ (constant 0 a) (constant 0 b))

### NavierStokes.ClosedIntervalJetAlgebra
- Line 246: | constant : ℝ → PolynomialExpression ι
- Line 257: | constant c => fun _ => c
- Line 264: | constant c => (|c|, 0)
- Line 276: | constant c => exact ⟨abs_nonneg c, le_rfl⟩
- Line 286: | constant c => exact PairBound.const k c ε

### NavierStokes.CompactForceDecay
- Line 194: every output component, with the same constant as the full derivative bound. -/

### NavierStokes.ComparatorDefinitions
- Line 127: For any derivative order $m$ and any decay rate $K$, there exists a constant $C$

### NavierStokes.ConstructedSlowBase
- Line 805: This fixes the first-order integration constant; the actual modulation

### NavierStokes.CorrectedPulseAmplitude
- Line 8: Its signed reset energy is retained in the constant coefficient, and the

### NavierStokes.CurrentPhysicalChartJets
- Line 202: operator.  The same constant works for every chart and free coordinate. -/
- Line 233: for the actual rotated coefficient, including order zero.  The constant is

### NavierStokes.CutStageEstimates
- Line 210: cut-stage bounds.  The constant and logarithmic exponent are independent of

### NavierStokes.EndpointLimits
- Line 25: at the endpoint. Values to the right are also set to that constant, but no

### NavierStokes.EntranceAlignedBase
- Line 613: including its actual integration constant. -/

### NavierStokes.FirstOrderBaseEdge
- Line 12: agreement of velocities alone does not fix the constant of integration.

### NavierStokes.FiveRowRank
- Line 442: space. The geometric constant is independent of the nonzero amplitude `C`; all
- Line 473: has a single constant valid for all amplitudes in that range. -/

### NavierStokes.Flatness
- Line 99: subtracting a fixed natural loss. Each stage has its own constant and eventual

### NavierStokes.FlatPrimitive
- Line 203: for `j = 3`, the remaining smooth factor is the constant `1 / (2c)`. -/

### NavierStokes.FourierAlias
- Line 559: the frequency. The constant precedes the frequency, point, and jet index. -/

### NavierStokes.GaugeAliasDecay
- Line 245: the auxiliary slow cutoff enters the constant. -/
- Line 374: strictly positive weight. This lemma constructs its enlarged constant. -/

### NavierStokes.GaugeMomentBalances
- Line 691: axial derivative, so replacing it by a constant would change the identity. -/

### NavierStokes.GaussianTailFlat
- Line 473: constant : ℝ
- Line 474: constant_one_le : 1 ≤ constant
- Line 476: slow_le : ∀ n, s.slow n ≤ constant * (1 + ChartScales.S n) ^ degree
- Line 555: refine ⟨A * B * scales.constant ^ p * C, by positivity, scales.degree * p, ?_⟩
- Line 575: have hK0 : 0 ≤ scales.constant := zero_le_one.trans scales.constant_one_le
- Line 577: scales.constant ^ p * (1 + ChartScales.S n) ^ (scales.degree * p) := by
- Line 580: (A * B * scales.constant ^ p) * ChartScales.Q n ^ (scales.power * α) *
- Line 597: (scales.constant ^ p * (1 + ChartScales.S n) ^ (scales.degree * p))) * B *
- Line 604: _ = (A * B * scales.constant ^ p) * (1 + ChartScales.S n) ^ (scales.degree * p) *
- Line 607: _ ≤ (A * B * scales.constant ^ p) * (1 + ChartScales.S n) ^ (scales.degree * p) *

### NavierStokes.GenericRealization
- Line 144: (hconst : ContDiffOn ℝ ∞ P.constant U)

### NavierStokes.GenericSummationRealization
- Line 85: (hconst : ContDiffOn ℝ ∞ P.constant U) (hc : ∀ t ∈ P.terms, ContDiffOn ℝ ∞ t.1 U)

### NavierStokes.GenericSupportedPolynomial
- Line 173: constant : D → ℝ
- Line 185: fun x => P.constant x + evalTerms u P.terms x
- Line 201: (hconst : ContDiffOn ℝ ∞ P.constant U)
- Line 262: (hconst : ContDiffOn ℝ ∞ P.constant U)
- Line 277: let hp := (TailRates.fixed P.constant).add ht hU hlU hq hconst

### NavierStokes.GenericSupportLocalCoefficients
- Line 191: (hconst : ContDiffOn ℝ ∞ P.constant U)
- Line 221: let hp := (TailRates.fixed P.constant).add ht hU hlU hq hconst hs (fun _ => hconst) hss

### NavierStokes.GenericSupportLocalSummation
- Line 31: (hconst : ContDiffOn ℝ ∞ P.constant U)
- Line 77: (hconst : ContDiffOn ℝ ∞ P.constant U)
- Line 115: (hconst : ContDiffOn ℝ ∞ P.constant U)

### NavierStokes.GenericTupleRealization
- Line 181: (hconst : ContDiffOn ℝ ∞ P.constant U)

### NavierStokes.GenericTupleSupport
- Line 167: (hconst : ContDiffOn ℝ ∞ P.constant U) (hc : ∀ t ∈ P.terms, ContDiffOn ℝ ∞ t.1 U)

### NavierStokes.GlobalBaseError
- Line 213: the supplied constant, never on the physical point, derivative order, or `q`. -/

### NavierStokes.GlobalSlowProfiles
- Line 94: noncomputable def constant (S : Set ℝ) (c : ℝ) : EvenProfile S :=
- Line 97: @[simp] theorem constant_apply (S : Set ℝ) (c : ℝ) (w : ℝ × ℝ) : constant S c w = c := rfl
- Line 210: inverse (1 - constant S (2 * h) * parameter S ^ 2)
- Line 219: (constant S 2 * parameter S * u -
- Line 220: constant S (2 * (PositiveAxisSystem.dScale h + lam)) * parameter S * massAverage d.isOpen u -
- Line 249: (-constant S b * f + constant S (SimilarityProfile.D h) * parameter S *
- Line 254: (constant S (2 * b) * parameter S * f + (1 - parameter S ^ 2) * etaDerivative d.isOpen f -
- Line 255: constant S 2 * parameter S * radiusSquared S * xDerivative d.isOpen f) * inverseDenominator d
- Line 271: (beta ij.1 * (constant S (1 / 2) * beta ij.2 + radiusSquared S * xDerivative d.isOpen (beta ij.2)) +
- Line 273: (constant S 4 * xDerivative d.isOpen (beta k) + constant S 2 * radiusSquared S *
- Line 289: constant S (C ^ 2)⁻¹ * (∑ i ∈ Finset.range (n + 1), phi i * phi (n - i)) -
- Line 290: constant S (1 / 2) * omega
- Line 520: (beta ij.1 * (constant S (1 / 2) * beta ij.2 + radiusSquared S * xDerivative d.isOpen (beta ij.2)) +
- Line 955: (beta ij.1 * (constant S (1 / 2) * beta ij.2 + radiusSquared S * xDerivative d.isOpen (beta ij.2)) +
- Line 958: (beta' ij.1 * (constant S (1 / 2) * beta' ij.2 + radiusSquared S * xDerivative d.isOpen (beta' ij.2)) +
- Line 1208: xProfile (constant S c) w = c := rfl

### NavierStokes.GraphRestriction
- Line 16: constant function one on a prescribed graph.

### NavierStokes.HarmonicSourceSupport
- Line 71: theorem constant (f : D → ℂ) : NonzeroSupported K (constantCoefficient f) := by
- Line 139: ((NonzeroSupported.constant _).mul (hc.differentiate hK g.radial k Φ))).add
- Line 140: ((NonzeroSupported.constant _).mul ((hc.angular kp).angular kp)) |>.add
- Line 148: ((NonzeroSupported.constant _).mul (((NonzeroSupported.constant _).mul
- Line 158: (((ha 1).mul (NonzeroSupported.constant _)).mul
- Line 169: · exact (NonzeroSupported.constant _).mul (hp.angular kp)
- Line 180: ((NonzeroSupported.constant _).mul (vectorLaplacian_supported hK g k Φ kp ha i))).add
- Line 203: nonlinearResidual_supported hK _ _ _ _ (fun _ => NonzeroSupported.constant _)
- Line 290: nonlinearResidual_supported hK _ _ _ _ (fun _ => NonzeroSupported.constant _) hv hp
- Line 659: theorem constant (f : D → ℂ) : NonzeroSupportedOn U K (constantCoefficient f) :=
- Line 660: of_global (NonzeroSupported.constant f)
- Line 906: on the full angular lift.  It has every exponent with constant zero, and

### NavierStokes.HeatSwitchCone
- Line 725: pressure primitive, not an independently chosen pressure constant. -/
- Line 1017: the previously fixed coefficient constant `C`. -/

### NavierStokes.HeatTailEdit
- Line 561: heat solution with a positive constant normalization. -/

### NavierStokes.InitialDyadicSource
- Line 214: theorem constant {f : D → ℂ} (hf : ContDiffAt ℝ ∞ f x) :
- Line 393: SmoothCoefficientsAt.constant (Complex.ofRealCLM.contDiff.contDiffAt.comp x
- Line 398: SmoothCoefficientsAt.constant (Complex.ofRealCLM.contDiff.contDiffAt.comp x
- Line 421: ((FlatCoefficients.mul_left (SmoothCoefficientsAt.constant contDiffAt_const)
- Line 469: (FlatCoefficients.mul_left (SmoothCoefficientsAt.constant contDiffAt_const)
- Line 487: (fun i => SmoothCoefficientsAt.constant (hbackground i))

### NavierStokes.IntegratedMeanBalances
- Line 617: `(R,(T,Z))`; `ε` is constant on a chart. The supplied fluxes are full averages

### NavierStokes.JetBounds
- Line 223: constant uniform in derivative order. -/

### NavierStokes.JointResidualLimits
- Line 256: closed-side extension is constant in time with the constructed boundary trace. -/

### NavierStokes.LabelCounting
- Line 79: Coordinates of radius zero make only a constant contribution to this bound. -/
- Line 148: bounded chart set. The one constant works in every positive band. -/
- Line 194: a constant number of grid indices per band contribute at a point. -/
- Line 230: enlargement of the mesh boxes. The constant is also independent of `D`. -/

### NavierStokes.LabelSumBounds
- Line 370: exponent and polynomial degree. The coefficient constant is multiplied

### NavierStokes.LocalizedGaussianBounds
- Line 166: refine ⟨A * B * scales.constant ^ p * C, by positivity, scales.degree * p, ?_⟩
- Line 184: have hK0 : 0 ≤ scales.constant := zero_le_one.trans scales.constant_one_le
- Line 186: scales.constant ^ p * (1 + ChartScales.S n) ^ (scales.degree * p) := by
- Line 189: (A * B * scales.constant ^ p) * ChartScales.Q n ^ (scales.power * α) *
- Line 205: (scales.constant ^ p * (1 + ChartScales.S n) ^ (scales.degree * p))) * B *
- Line 211: _ = (A * B * scales.constant ^ p) * (1 + ChartScales.S n) ^ (scales.degree * p) *
- Line 214: _ ≤ (A * B * scales.constant ^ p) * (1 + ChartScales.S n) ^ (scales.degree * p) *

### NavierStokes.LocalizedWaveBounds
- Line 26: Every constant precedes the band, label, copy, and evaluation point. -/

### NavierStokes.LoopVariance
- Line 416: Only `t≥1` is required, and every constant is explicit. -/

### NavierStokes.MatchingConeBounds
- Line 9: than estimated by an absolute constant.

### NavierStokes.MatchingDebtBounds
- Line 613: inverse.  The constant depends only on the requested order and that inverse.

### NavierStokes.MaximalLifespan
- Line 43: time-dependent spatially constant normalization. -/

### NavierStokes.MeanIncrementBounds
- Line 822: constant comes from its actual jets and the positive weight on its support. -/

### NavierStokes.MeanRankUpdate
- Line 809: bounded, with no band in either the coefficient or the constant. -/

### NavierStokes.MixedDiagonalExtensions
- Line 98: The constant is shared by all positive stages in the central-plane theorem. -/

### NavierStokes.ModulatedCone
- Line 524: nominal true-cone patch (the constant periodic-loop case). -/
- Line 670: difference; the pressure constant is retained exactly. -/

### NavierStokes.ModulatedExterior
- Line 7: The pressure constant is obtained from the restored integral of the squared
- Line 9: swirl alone would not determine this constant.
- Line 92: constant.  The existing finite-modification certificate already retains mass. -/
- Line 125: the exterior.  Its integration constant was fixed by the restored row. -/

### NavierStokes.ModulatedProfileAssembly
- Line 13: axis, including the pressure constant, are preserved.  The separate angular

### NavierStokes.ModulatedProfileJetRates
- Line 11: orders. Only the asymptotic threshold and constant may depend on the order. -/
- Line 29: The solver is chosen before the derivative order, frequency, and constant. -/

### NavierStokes.ModulatedStockBounds
- Line 302: threshold and the stock constant are conclusions. -/

### NavierStokes.MovingFrameODE
- Line 651: Taking `η = C / S` gives the required `O(1/S)` with the displayed constant.

### NavierStokes.NaturalAxisBridge
- Line 713: `Λ`, uniformly over all radially constant angular amplitudes in a fixed norm

### NavierStokes.NaturalEntrance
- Line 739: reference slope, with the coefficient-space error constant. -/

### NavierStokes.NaturalExitBounds
- Line 153: constant and every fixed parameter-jet constant are chosen before Λ and C;

### NavierStokes.OutgoingEntranceCone
- Line 501: the true source. The constant is absolute and uniform in `P, λ, h, m`. -/

### NavierStokes.OutgoingNegativeSlopeCone
- Line 74: negative, one unit before the constant-slope interval begins. -/

### NavierStokes.OutgoingProfile
- Line 217: clock time. No finite-prefix constant is an additional assumption. -/

### NavierStokes.ParametricHeatTail
- Line 974: exactly a constant times `s^(-A) H(2 tau / s)`. -/

### NavierStokes.ParametricRadialExtension
- Line 14: values.  No constant continuation at negative `X` is differentiated.

### NavierStokes.ParametricTorusInverse
- Line 653: The constant is independent of the parameter set and the function. -/

### NavierStokes.ParticularCopyBounds
- Line 27: Every quantitative constant precedes the band and lattice copy. -/
- Line 53: constant : ℝ
- Line 54: constant_ge_one : 1 ≤ constant
- Line 56: length_bound : ∀ n, L n ≤ constant * s.slow n
- Line 57: exponential_bound : ∀ n, Real.exp (errorRate n * L n) ≤ constant
- Line 58: coordinate_bound : ∀ n, CommonCoverClass.argumentCost (g n) ≤ constant * s.slow n ^ coordinate_power
- Line 99: let K := C + h.constant + 1
- Line 102: have hK₀K : h.constant ≤ K := by dsimp [K]; linarith
- Line 107: have hK₀ : 0 ≤ h.constant := zero_le_one.trans h.constant_ge_one
- Line 108: refine ⟨ambientJetConstant N * B ^ (N + 1) * K * h.constant ^ N,
- Line 144: have hcg : CommonCoverClass.argumentCost (g n) ≤ h.constant * s.growth n p ^ h.coordinate_power :=
- Line 149: h.constant ^ N * s.growth n p ^ (h.coordinate_power * N) := by
- Line 151: _ ≤ (h.constant * s.growth n p ^ h.coordinate_power) ^ j := pow_le_pow_left₀
- Line 153: _ ≤ (h.constant * s.growth n p ^ h.coordinate_power) ^ N := pow_le_pow_right₀
- Line 162: (K * s.growth n p ^ m) * (h.constant ^ N * s.growth n p ^ (h.coordinate_power * N)) := by
- Line 168: (K * s.growth n p ^ m) * (h.constant ^ N * s.growth n p ^ (h.coordinate_power * N)) := by
- Line 392: constant : ℝ
- Line 393: constant_ge_one : 1 ≤ constant
- Line 395: length_bound : ∀ l n, L l n ≤ constant * s.slow n
- Line 396: exponential_bound : ∀ l n, Real.exp (errorRate l n * L l n) ≤ constant
- Line 397: coordinate_bound : ∀ l n, CommonCoverClass.argumentCost (g l n) ≤ constant * s.slow n ^ coordinate_power
- Line 442: constant := h.constant

### NavierStokes.ParticularWaveBounds
- Line 579: constant : ℝ
- Line 580: constant_ge_one : 1 ≤ constant
- Line 582: length_bound : ∀ n, L n ≤ constant * s.slow n
- Line 583: exponential_bound : ∀ n, Real.exp (errorRate n * L n) ≤ constant
- Line 584: coordinate_bound : ∀ n, CommonCoverClass.argumentCost (g n) ≤ constant * s.slow n ^ coordinate_power
- Line 1312: constant : ℝ
- Line 1313: constant_ge_one : 1 ≤ constant
- Line 1315: length_bound : ∀ n, L n ≤ constant * s.slow n
- Line 1316: exponential_bound : ∀ n, Real.exp (errorRate n * L n) ≤ constant
- Line 1317: coordinate_bound : ∀ n, CommonCoverClass.argumentCost (g n) ≤ constant * s.slow n ^ coordinate_power
- Line 1354: let K := C + h.constant + 1
- Line 1357: have hK₀K : h.constant ≤ K := by dsimp [K]; linarith
- Line 1362: have hK₀ : 0 ≤ h.constant := zero_le_one.trans h.constant_ge_one
- Line 1363: refine ⟨ambientJetConstant N * B ^ (N + 1) * K * h.constant ^ N,
- Line 1397: have hcg : CommonCoverClass.argumentCost (g n) ≤ h.constant * s.growth n p ^ h.coordinate_power :=
- Line 1402: h.constant ^ N * s.growth n p ^ (h.coordinate_power * N) := by
- Line 1404: _ ≤ (h.constant * s.growth n p ^ h.coordinate_power) ^ j := pow_le_pow_left₀
- Line 1406: _ ≤ (h.constant * s.growth n p ^ h.coordinate_power) ^ N := pow_le_pow_right₀
- Line 1415: (K * s.growth n p ^ m) * (h.constant ^ N * s.growth n p ^ (h.coordinate_power * N)) := by

### NavierStokes.PeriodicPhaseAssembly
- Line 764: function identity under the constant lattice translation. -/

### NavierStokes.PeriodizedWaveBounds
- Line 540: refine ⟨A * B * scales.constant ^ p * C, by positivity, scales.degree * p, ?_⟩
- Line 558: have hK0 : 0 ≤ scales.constant := zero_le_one.trans scales.constant_one_le
- Line 560: scales.constant ^ p * (1 + ChartScales.S n) ^ (scales.degree * p) := by
- Line 563: (A * B * scales.constant ^ p) * ChartScales.Q n ^ (scales.power * α) *
- Line 579: (scales.constant ^ p * (1 + ChartScales.S n) ^ (scales.degree * p))) * B *
- Line 585: _ = (A * B * scales.constant ^ p) * (1 + ChartScales.S n) ^ (scales.degree * p) *
- Line 588: _ ≤ (A * B * scales.constant ^ p) * (1 + ChartScales.S n) ^ (scales.degree * p) *

### NavierStokes.PhaseJetBounds
- Line 754: constant and one power of S.  The constant is independent of the slot time. -/
- Line 974: It is constant in the chart variables even when it jumps across labels. -/
- Line 989: uniformly bounded label constant.  Thus no factor k is lost in slow jets. -/

### NavierStokes.PhysicalCoordinateBounds
- Line 536: same explicit loss `n`. The constant depends only on the fixed geometry

### NavierStokes.PhysicalGraphBounds
- Line 788: Its exponent can contain the stage gain; only the constant changes. -/
- Line 805: fixed power loss; the constant may depend on the slow power. -/
- Line 1344: the final constant. The phase class is supplied by `liftedPhase_power_bound`. -/

### NavierStokes.PhysicalResidualJetBounds
- Line 274: constant. The displayed loss retains the exact physical scaling degree. -/
- Line 502: the spatial sum. The constant multiplier is the proved overlap `2250`. -/

### NavierStokes.PhysicalResidualNaturality
- Line 94: theorem constant {U : Set D} {e : D ≃L[ℝ] E} {a : ℝ}
- Line 218: apply CoefficientsOn.constant
- Line 231: apply CoefficientsOn.constant
- Line 280: CoefficientsOn.constant (by intro x hx; simp)
- Line 456: apply CoefficientsOn.constant

### NavierStokes.PhysicalStageSupport
- Line 9: outer-support constant for every stage. Coherent means are represented in
- Line 394: same outer constant as the wave increments. -/

### NavierStokes.PhysicalWaveSum
- Line 186: to the stripped constant. -/
- Line 824: stripped-class degrees affect its constant only. -/

### NavierStokes.PolarCharts
- Line 367: The constant is chosen before `Q`, the chart, and the evaluation point. -/

### NavierStokes.PrimaryCopyBounds
- Line 9: constant is chosen before that label, its band, and the lattice copy.  The
- Line 909: constant still preceding the native label. -/

### NavierStokes.PrimaryGeometryAssembly
- Line 606: reselect a target direction, parameter constant, representative, or

### NavierStokes.PrimaryPulseBounds
- Line 1442: representative choices stay constant within each label. -/

### NavierStokes.ProblemStatement
- Line 8: `candidateStatement` is a proposition, not an axiom or a proved theorem.
- Line 117: There is no proof, witness, or axiom asserting this proposition in this module.

### NavierStokes.PulseAmplitude
- Line 14: The pulse constant is the integral of the constructed smooth pulse from

### NavierStokes.PulseLag
- Line 751: first derivative at most one. The common lag constant is independent of

### NavierStokes.R3PressureKernel
- Line 8: The manuscript's pressure commutator is bounded by a constant times
- Line 112: `global:kernel-bound`, with an exact constant independent of `R`. -/

### NavierStokes.R3RieszKernel
- Line 9: bounded by a constant times `|x|⁻³` away from the origin.

### NavierStokes.RadialModulation
- Line 312: uniformly on compact radius/parameter sets and all angles. The constant is

### NavierStokes.RadialPullback
- Line 672: constant, with all product-rule terms retained. -/

### NavierStokes.RadialSchedule
- Line 15: energy term in equation (13), and the constant-coefficient lag equation.

### NavierStokes.ReferenceEndpointRate
- Line 122: The natural coefficient constant displayed on the right does not depend on `Λ`. -/
- Line 155: one joining constant chosen before amplitude and the transition widths. -/

### NavierStokes.ResidualStability
- Line 71: constant may depend on the derivative order, but not on the point. -/

### NavierStokes.ScaledActualParticularControl
- Line 203: constant := K
- Line 425: The constant uses only the already selected scale bounds and gap budget. -/

### NavierStokes.SeedHandbackJets
- Line 66: private def c (x : ℝ) : Expr := .constant x
- Line 268: The same pressure integration constant is used for both profiles. -/

### NavierStokes.ShapedWaitBounds
- Line 7: The two decaying modes are kept separate, so no inverse small-slope constant
- Line 1218: derivatives, with one displayed constant depending only on the earlier `P,m`. -/
- Line 1261: history, including its harmless linear factor, with no hidden `λ` constant. -/

### NavierStokes.ShapeTransition
- Line 103: open constant-profile regions as well. -/
- Line 1396: hypothesis occurs. The constant `shapeJetConstant` is independent of `C`. -/

### NavierStokes.SlowRecursion
- Line 1177: the axis. No free integration constant survives the regular zero trace. -/

### NavierStokes.SlowStressSupport
- Line 844: stress norm bound is an input. The constant may depend on the derivative order. -/

### NavierStokes.SmoothFamilyTorusInverse
- Line 864: constant is chosen before the source, parameter set, or input bound. -/

### NavierStokes.SmoothFourierData
- Line 367: `TorusInverse`. The lattice constant is finite by `summable_weight_inv_four`. -/

### NavierStokes.StressActivation
- Line 260: the ramp length: its constant is only a bound for the reference coefficient. -/
- Line 851: history. This includes the pressure constant and all four moment histories. -/

### NavierStokes.TailGaugePotential
- Line 9: removes every radial integration constant, including those of the positive

### NavierStokes.TangentODE
- Line 143: Lipschitz constant. The resulting extension is differentiable at the endpoints too. -/

### NavierStokes.TemporalMeanUpdate
- Line 843: The constant is obtained from the derivative product rule on the compact annulus. -/
- Line 967: the corresponding normalized alias estimate. The transfer constant is fixed

### NavierStokes.TerminalHistoryBridge
- Line 1245: axial integration constant; the pressure is the actual canonical pressure. -/

### NavierStokes.TransitionRamp
- Line 540: activation width plus the retained constant control. -/

### NavierStokes.TransportPrimitive
- Line 769: and cutoff derivative bounds. The constant contains no translation parameter. -/

### NavierStokes.UniformAngularReset
- Line 828: power bound for the actual waiting duration. The constant is universal. -/

### NavierStokes.UniformHarmonicInteraction
- Line 418: zero constant mode and the original carrier. This is independent of the

### NavierStokes.UniformPrimaryWeights
- Line 11: constant is chosen before both the original band and the label.

### NavierStokes.VariableGaugeMean
- Line 815: constant is chosen before the domain, scale function, frequency and source. -/
- Line 1534: The constant precedes all frequencies, sources, amplitudes and evaluation points. -/

### NavierStokes.VolterraAnalyticBounds
- Line 513: radial, and strip-gap constant. There is no smallness assumption. -/
- Line 523: majorant constant, so the entire Picard layer is still summable. -/

### NavierStokes.WaveEdgeExtension
- Line 313: bound is absorbed into the constant. -/
- Line 562: bounded by the radial logarithmic factor, with constant exactly one. -/

### NavierStokes.WaveStageContinuation
- Line 263: theorem constant {f g : D → ℂ} (hfg : EqOn f g U) :
- Line 574: apply CoeffEqOn.constant

### NavierStokes.WeightedQuotients
- Line 12: pointwise estimate is constant in the differentiation variable: no regularity

### NavierStokes.WeightedRadialPrimitive
- Line 474: The extra constant is only the fixed upper radial endpoint b. -/
- Line 680: compactified transport primitive. All shifts are quantified after the constant. -/

### NavierStokes.WholeDomainCompactBounds
- Line 10: the actual derivatives, and allows a different local constant at every point.

### NavierStokes.WholeDomainPhysicalStageTheorem
- Line 113: increment obey one common constant and logarithmic power. -/

### NavierStokes.WholeDomainStageBounds
- Line 96: unit sublevel. Its constant may depend on the order and power, but its

### NavierStokes.ZerothStressIdentity
- Line 9: endpoint fixes the constant and identifies the constructed stress.

### NavierStokes.R3.ComparisonGronwall
- Line 118: share the same constant in the numerator. -/

### NavierStokes.R3.ComparisonYoung
- Line 22: small multiple of the square, with a constant independent of the argument. -/
- Line 70: arbitrarily small square coefficient and makes the constant decay as `1 / R`. -/
- Line 146: constant works for every nonnegative gradient norm and every radius at least

### NavierStokes.R3.H3Embedding
- Line 70: constant independent of the support or of the chosen point. -/

### NavierStokes.R3.HeatKernelPairedBound
- Line 126: the precise `R^(-3/4)` decay and a universal positive constant. -/

### NavierStokes.R3.LocalizedTensorBounds
- Line 169: It has the same constant for every pair of indices. -/

### NavierStokes.R3.PressureFunctionals
- Line 168: norm, with a constant depending only on the given coefficients. -/

### NavierStokes.R3.ScalarEnergyBound
- Line 10: the energy plus a constant. Only derivatives in the interior of the time

### NavierStokes.R3.SchwartzCompactApproximation
- Line 9: by a fixed constant divided by R. Consequently compactly supported Schwartz

### NavierStokes.R3.WeightedSobolev
- Line 218: cutoff is isolated in the derivative bound `L`; the constant is fixed. -/

### NavierStokesReview.src.external-semantic.ClaySpec
- Line 165: one constant `C` bounds the energy for every `t ≥ 0`, as required by the words

### NavierStokesReview.src.probes.HeadlineAxiomProbe
- Line 6: the means of obtaining the transitive axiom report.

## Import Closure Anomalies (Dead Code/Disconnected Modules)

Found 2108 modules disconnected from the main endpoints.

- ComparatorChallenges.Euler
- ComparatorChallenges.NavierStokes
- Euler
- Euler.AllOrderCorrectionBudget
- Euler.AllOrderCorrectionCoherence
- Euler.AllOrderCorrectionData
- Euler.AllOrderCorrectionFamily
- Euler.AllOrderCorrectionStability
- Euler.AllOrderDriftBudget
- Euler.AllOrderDriftCorrection
- Euler.AllOrderDriftEquation
- Euler.AllOrderDriftFieldDecomposition
- Euler.AllOrderDriftFinite
- Euler.AllOrderDriftGraph
- Euler.AllOrderDriftPointwiseBounds
- Euler.AllOrderDriftPressure
- Euler.AllOrderDriftPressureBounds
- Euler.AllOrderDriftRadiusBounds
- Euler.AllOrderDriftResidualBounds
- Euler.AllOrderLiftedCorrection
- Euler.AllOrderPressureCoherence
- Euler.AllOrderSmoothPressure
- Euler.AngleMeanZeroPrimitive
- Euler.AnglePrimitiveBounds
- Euler.AnglePrimitiveKernel
- Euler.AnglePrimitiveMap
- Euler.AnglePrimitiveParity
- Euler.AnglePrimitiveSpatialRegularity
- Euler.AnglePrimitiveTranslation
- Euler.AsymmetricTransport
- Euler.BaseEulerDatum
- Euler.BaseEulerFlowL2
- Euler.BaseEulerGevrey
- Euler.BaseEulerGuards
- Euler.BaseEulerInput
- Euler.BaseEulerLabelData
- Euler.BaseEulerParent
- Euler.BaseEulerParity
- Euler.BaseEulerSign
- Euler.BaseEulerSobolev
- Euler.BaseEulerState
- Euler.BaseEulerUniform
- Euler.BaseFirstPacket
- Euler.BaseFirstPacketChoice
- Euler.BaseFirstPacketChoiceNoOptions
- Euler.BaseFirstPacketEvolution
- Euler.BaseFirstPacketEvolutionNoOptions
- Euler.BaseFirstPacketFrame
- Euler.BaseFirstPacketScales
- Euler.BaseFirstPacketSupport
- Euler.BaseInductionStage
- Euler.BaseInductionStageNoOptions
- Euler.BaseLiteralFirstPacket
- Euler.BasePacketFrameValues
- Euler.BasePacketFrequencyCost
- Euler.BasePacketLowBounds
- Euler.BasePacketSetup
- Euler.BasePacketUniformCosts
- Euler.BasePressureCommutator
- Euler.BaseSmoothState
- Euler.BaseStaticEuler
- Euler.BaseTransportCommutator
- Euler.BaseTransportL2
- Euler.BaseWordMetric
- Euler.BoundedCoefficientJets
- Euler.BoundedCoefficientSmooth
- Euler.BoundedEvaluationDifferentiation
- Euler.BoundedFieldCalculus
- Euler.BoundedFieldForwardGenerator
- Euler.BoundedFieldGramGevrey
- Euler.BoundedFieldGramInverse
- Euler.BoundedFieldMultilinear
- Euler.BoundedFieldPullback
- Euler.BoundedFieldTimeDerivative
- Euler.BoundedFlowContinuity
- Euler.BoundedFlowPeriodicity
- Euler.BoundedInverseGevrey
- Euler.BoundedLipschitzFlow
- Euler.BoundedMildContinuation
- Euler.BoundedPathFamily
- Euler.BoundedTensorCoordinates
- Euler.CanonicalGraphPotential
- Euler.CanonicalPacketHorizons
- Euler.CanonicalVorticityConfinement
- Euler.ChildParticleFieldBounds
- Euler.ChildParticleFieldTime
- Euler.ChildParticleJacobian
- Euler.ChildParticleSourceBound
- Euler.ChildParticleTime
- Euler.ClassicalBridge
- Euler.ClassicalDivergence
- Euler.ClassicalPressureCurl
- Euler.ClosedIntervalDerivativeExtension
- Euler.ClosedTranslationGraph
- Euler.CoefficientCostMonotone
- Euler.CoefficientJetPressureBounds
- Euler.CoefficientPathBounds
- Euler.CoefficientPathOrbit
- Euler.CoefficientPathPressureBounds
- Euler.CoefficientPathSmooth
- Euler.CoefficientPathSobolev
- Euler.CoefficientPathWeightedBounds
- Euler.CoerciveEndpointBounds
- Euler.CommonPressureRepresentative
- Euler.CompactCurlBounds
- Euler.CompactParameterIntegral
- Euler.CompactPressurePairing
- Euler.CompactProjectedEulerLaw
- Euler.CompactProjectedPairing
- Euler.CompactSmoothBounds
- Euler.CompactSmoothL2Bounds
- Euler.CompactSmoothTimeField
- Euler.CompactSolenoidalDensity
- Euler.CompactSpatialJets
- Euler.CompactSupportBoundedPath
- Euler.CompactVorticityContradiction
- Euler.CompactVorticityTimeUpgrade
- Euler.ComparatorEvolutionIdentification
- Euler.ComparatorIdentification
- Euler.ComparatorLocalCompactVorticity
- Euler.ComparatorLocalEvolution
- Euler.ComparatorMaximalFields
- Euler.ComparatorMaximalSolution
- Euler.ComparatorSingularityNorms
- Euler.ComparatorSobolevEvolution
- Euler.ComparatorTimeShift
- Euler.ComparatorTruncationFamily
- Euler.ComparatorUniformSpatialJets
- Euler.ConstantCorrectionData
- Euler.ConstantEulerGraph
- Euler.ContinuousAccelerationForcing
- Euler.ContinuousAccelerationGevrey
- Euler.ContinuousAccelerationSobolev
- Euler.ContinuousBoundedTensor
- Euler.ContinuousForcingTimeLp
- Euler.ContinuousForcingTranslation
- Euler.ContinuousGramAcceleration
- Euler.ContinuousGramGevrey
- Euler.ContinuousGramPath
- Euler.ContinuousGramSobolev
- Euler.ContinuousInverseDerivative
- Euler.ContinuousPathCalculus
- Euler.ContinuousPathComposition
- Euler.ContinuousSpatialFamily
- Euler.ContinuousTimeIntegral
- Euler.ContinuousTimeWeight
- Euler.CorrectionAssemblyCommon
- Euler.CorrectionAssemblyCompatibility
- Euler.CorrectionAssemblyData
- Euler.CorrectionAssemblyParity
- Euler.CorrectionAssemblyPressure
- Euler.CorrectionAssemblyPressureParity
- Euler.CorrectionAssemblyRealizations
- Euler.CorrectionAssemblyReconstruction
- Euler.CorrectionAssemblySourceTower
- Euler.CorrectionAssemblyTime
- Euler.CorrectionBudgetRestriction
- Euler.CorrectionContinuation
- Euler.CorrectionDifference
- Euler.CorrectionDifferenceMetric
- Euler.CorrectionDifferencePDE
- Euler.CorrectionEnergyBootstrap
- Euler.CorrectionEnergyBound
- Euler.CorrectionEnergyData
- Euler.CorrectionEnergyMajorants
- Euler.CorrectionEnergyRestriction
- Euler.CorrectionEnergyScalar
- Euler.CorrectionEnergyTime
- Euler.CorrectionFamilyCompactness
- Euler.CorrectionLimitDerivative
- Euler.CorrectionLimitEquation
- Euler.CorrectionLimitPathDerivative
- Euler.CorrectionLowerData
- Euler.CorrectionMildEnergy
- Euler.CorrectionMildEquation
- Euler.CorrectionOperators
- Euler.CorrectionParity
- Euler.CorrectionResidualCancellation
- Euler.CorrectionSmoothTimeField
- Euler.CorrectionSourceRestriction
- Euler.CorrectionStabilityBudget
- Euler.CorrectionStabilityConstants
- Euler.CorrectionTime
- Euler.CorrectionTimeRestriction
- Euler.CorrectionViscosityStability
- Euler.CurlMatrixSymmetry
- Euler.CurlSupport
- Euler.CurlTimeDerivative
- Euler.CurlTransportAlgebra
- Euler.CylinderActionWords
- Euler.CylinderAngleAverage
- Euler.CylinderAngleAverageEvolution
- Euler.CylinderAngleAverageRepresentative
- Euler.CylinderAngleAverageTime
- Euler.CylinderAngleEvolution
- Euler.CylinderAnglePrimitive
- Euler.CylinderAngleRepresentative
- Euler.CylinderAngleWordBounds
- Euler.CylinderBoundedCover
- Euler.CylinderClassicalSolenoidal
- Euler.CylinderClassicalWordBounds
- Euler.CylinderCompactBounds
- Euler.CylinderCompactTranslation
- Euler.CylinderConstantMap
- Euler.CylinderConstantMapBounds
- Euler.CylinderCorrectorMeanZero
- Euler.CylinderCoverDescent
- Euler.CylinderCoverTensor
- Euler.CylinderCoveringDerivative
- Euler.CylinderDescentJets
- Euler.CylinderDirichletData
- Euler.CylinderDirichletEquation
- Euler.CylinderDirichletMean
- Euler.CylinderDirichletNaturality
- Euler.CylinderDirichletParity
- Euler.CylinderDirichletPhysicalBounds
- Euler.CylinderDirichletRegularity
- Euler.CylinderDirichletSobolev
- Euler.CylinderDirichletSupport
- Euler.CylinderDirichletTimeBounds
- Euler.CylinderDirichletTranslation
- Euler.CylinderEndpointBounds
- Euler.CylinderEndpointBudget
- Euler.CylinderEndpointData
- Euler.CylinderEndpointEquation
- Euler.CylinderEndpointForcing
- Euler.CylinderEndpointLabels
- Euler.CylinderEndpointParity
- Euler.CylinderEndpointPointwise
- Euler.CylinderEndpointRegularity
- Euler.CylinderEndpointSupport
- Euler.CylinderEndpointUnitBounds
- Euler.CylinderFieldReflection
- Euler.CylinderForwardParity
- Euler.CylinderGradientEmbedding
- Euler.CylinderGraphAffine
- Euler.CylinderGraphDerivative
- Euler.CylinderGraphGevrey
- Euler.CylinderGraphPath
- Euler.CylinderGraphRealization
- Euler.CylinderHeatEquation
- Euler.CylinderHeatLaplacian
- Euler.CylinderJetGraphTrace
- Euler.CylinderJetLp
- Euler.CylinderJetLpAlgebra
- Euler.CylinderJetLpMap
- Euler.CylinderLocalSupport
- Euler.CylinderMeasureDescent
- Euler.CylinderOrbitSobolev
- Euler.CylinderPathAdvection
- Euler.CylinderPathBilinear
- Euler.CylinderPathBilinearBounds
- Euler.CylinderPathDerivativeProduct
- Euler.CylinderPathIntegral
- Euler.CylinderPathProduct
- Euler.CylinderPathProductBounds
- Euler.CylinderPathProductSupport
- Euler.CylinderPathWords
- Euler.CylinderPeriodicFlow
- Euler.CylinderPhysicalTensor
- Euler.CylinderPhysicalTensorDifference
- Euler.CylinderPhysicalTensorLp
- Euler.CylinderPotentialPath
- Euler.CylinderPotentialTime
- Euler.CylinderPotentialTimeWeight
- Euler.CylinderPotentialWeight
- Euler.CylinderRawSupport
- Euler.CylinderReflection
- Euler.CylinderRetractRepresentative
- Euler.CylinderScalarAverage
- Euler.CylinderScalarClassical
- Euler.CylinderScalarParity
- Euler.CylinderScalarPrimitive
- Euler.CylinderScalarRepresentative
- Euler.CylinderScalarTime
- Euler.CylinderSliceRepresentatives
- Euler.CylinderSlowCurl
- Euler.CylinderSlowCurlBounds
- Euler.CylinderSlowCurlTime
- Euler.CylinderSlowCurlWeight
- Euler.CylinderSmoothOrbit
- Euler.CylinderSmoothTimeField
- Euler.CylinderSobolevDensity
- Euler.CylinderSobolevDerivatives
- Euler.CylinderSobolevEmbedding
- Euler.CylinderSobolevOperators
- Euler.CylinderSobolevOrbit
- Euler.CylinderSobolevSpace
- Euler.CylinderSobolevWordBounds
- Euler.CylinderSpatialEmbedding
- Euler.CylinderSpatialMean
- Euler.CylinderSpatialMeanPath
- Euler.CylinderSpatialMeanRepresentative
- Euler.CylinderSpatialMeanTime
- Euler.CylinderTerminalAmplitude
- Euler.CylinderTimeGradient
- Euler.CylinderTimePrecomposition
- Euler.CylinderTimeRegularity
- Euler.CylinderTimeWords
- Euler.CylinderTranslationAdjoint
- Euler.CylinderViscousEnergy
- Euler.DeformationTimeInverse
- Euler.DevelopmentBridge
- Euler.DirichletEndpointReduction
- Euler.DivCurlRecovery
- Euler.DivCurlTensorRecovery
- Euler.DivergenceFreeHeat
- Euler.DriftCorrectionBootstrap
- Euler.DriftCorrectionBudget
- Euler.DriftCorrectionEnergyBound
- Euler.DriftCorrectionForcing
- Euler.DriftCorrectionMildEnergy
- Euler.DriftEnergyConstants
- Euler.DriftEnergyMajorants
- Euler.DriftGevreyInviscidEnergyCompactness
- Euler.DriftGlobalGevreyCorrection
- Euler.DriftGlobalInviscidGevrey
- Euler.DriftMetricForcing
- Euler.DriftNonlinearEstimate
- Euler.DriftPartialCorrectionBootstrap
- Euler.DriftPreservingTransport
- Euler.DriftViscousCorrectionFamily
- Euler.DuhamelDifferentiation
- Euler.DuhamelEquation
- Euler.DuhamelPasting
- Euler.ElapsedTimePathGluing
- Euler.ElapsedTimePathNaturality
- Euler.ElapsedTimePathWeight
- Euler.EnergyForcingIdentity
- Euler.EnergyMetricPaths
- Euler.EnergyWordCoordinates
- Euler.EulerC1Breakdown
- Euler.EulerC1Limsup
- Euler.EulerCorrectionEquation
- Euler.EulerCorrectionLocal
- Euler.EulerFiniteLifespan
- Euler.EulerProof
- Euler.EulerSingularity
- Euler.EulerSpatialRescaling
- Euler.EulerTimeRescaling
- Euler.EvolutionTimeShift
- Euler.ExactLiftedGraphPressure
- Euler.ExactLiftedJointDifferentiability
- Euler.ExactLiftedPointwise
- Euler.ExternalScalarCommutator
- Euler.ExternalTransportCommutator
- Euler.FamilyNormTime
- Euler.FieldTowerAlgebra
- Euler.FieldTowerCanonicalGraph
- Euler.FieldTowerGraph
- Euler.FieldTowerGraphDerivative
- Euler.FieldTowerGraphGevrey
- Euler.FieldTowerJetLp
- Euler.FieldTowerPhysicalContinuity
- Euler.FieldTowerPhysicalL2
- Euler.FieldTowerPointwiseGevrey
- Euler.FieldTowerRepresentative
- Euler.FieldTowerSmoothTimeField
- Euler.FieldTowerTimeRestriction
- Euler.FieldTowerVolumeSobolev
- Euler.FiniteEnergyTruncation
- Euler.FiniteGradeAlgebra
- Euler.FiniteGradeAssembly
- Euler.FiniteGradeDiagonal
- Euler.FiniteGradeSupport
- Euler.FiniteGradeTriangular
- Euler.FiniteIntervalFlow
- Euler.FiniteMetricEnergy
- Euler.FinitePathTensor
- Euler.FinitePathTensorIntegral
- Euler.FiniteQuadraticCauchy
- Euler.FixedEndpointClassical
- Euler.FixedEndpointForcing
- Euler.FixedEndpointStrong
- Euler.FixedEvolutionNaturality
- Euler.FixedEvolutionRegularity
- Euler.FixedEvolutionSobolev
- Euler.FixedFrameNaturality
- Euler.FlowEscapeBound
- Euler.FlowL2Transport
- Euler.FrameEndpointUniqueness
- Euler.FrameWronskian
- Euler.FrozenEvolutionGevrey
- Euler.FunctionalVelocity
- Euler.GainedMildFormula
- Euler.GainedMildPasting
- Euler.GaussianCylinderHeat
- Euler.GaussianHeatDerivative
- Euler.GaussianHeatGenerator
- Euler.GaussianHeatSmoothing
- Euler.GaussianHeatTotal
- Euler.GeneralCylinderAlgebra
- Euler.GeneralRealCylinderAlgebra
- Euler.GevreyBaseTransport
- Euler.GevreyCompactProduct
- Euler.GevreyComposition
- Euler.GevreyCompositionLp
- Euler.GevreyCompositionPartitions
- Euler.GevreyContinuationNorm
- Euler.GevreyCorrectionBound
- Euler.GevreyCorrectionForcing
- Euler.GevreyCorrectionSourceBounds
- Euler.GevreyCorrectionSplit
- Euler.GevreyDifferentiatedEquation
- Euler.GevreyEnergyCutoff
- Euler.GevreyEnergyLimit
- Euler.GevreyEnergyPathLimit
- Euler.GevreyFamilyCompactness
- Euler.GevreyFixedShift
- Euler.GevreyFlowBootstrap
- Euler.GevreyFlowFinite
- Euler.GevreyFlowLpIntegration
- Euler.GevreyForcingComponents
- Euler.GevreyGeneratingAlgebra
- Euler.GevreyGeneratingComposition
- Euler.GevreyGeneratingDerivatives
- Euler.GevreyGeneratingDerivativesNoOptions
- Euler.GevreyGrowthBudget
- Euler.GevreyGrowthCoefficient
- Euler.GevreyInverseMap
- Euler.GevreyInversePartitions
- Euler.GevreyInviscidEnergyCompactness
- Euler.GevreyJetCompositionLp
- Euler.GevreyLowNorms
- Euler.GevreyMetricComparison
- Euler.GevreyMetricEstimate
- Euler.GevreyMetricForcing
- Euler.GevreyNonlinearEstimate
- Euler.GevreyOrderZero
- Euler.GevreyPathNorm
- Euler.GevreyPressureComplete
- Euler.GevreyPressureEnergy
- Euler.GevreyPressureShifted
- Euler.GevreyPressureTransport
- Euler.GevreyProductLp
- Euler.GevreyRadiusReduction
- Euler.GevreyRestriction
- Euler.GevreyStabilityBudget
- Euler.GevreyTransportCommutator
- Euler.GevreyUniformConstants
- Euler.GlobalGevreyCorrection
- Euler.GlobalInviscidGevrey
- Euler.GradientReflection
- Euler.GramNaturality
- Euler.GraphDivergence
- Euler.GraphInvariantFlow
- Euler.GraphPressurePotential
- Euler.GraphVelocityTrace
- Euler.H3CurlConvergence
- Euler.H5CylinderAlgebra
- Euler.H5RealCylinderAlgebra
- Euler.H6NonlinearPressure
- Euler.H6NonlinearProduct
- Euler.H6Pressure
- Euler.H6PressureCommutator
- Euler.H6PressureConstants
- Euler.H6PressureInverse
- Euler.H6TransportSource
- Euler.HeatAllOrders
- Euler.HeatGradientEnergy
- Euler.HeatGradientIntegral
- Euler.HeatHessianEnergy
- Euler.HeatMaximalCauchy
- Euler.HeatMaximalEstimate
- Euler.HeatMaximalRegularity
- Euler.HeatRegularizedPaths
- Euler.HeatRestart
- Euler.HilbertCoerciveGevrey
- Euler.HilbertCoerciveParameter
- Euler.HilbertCoerciveTransport
- Euler.HilbertProductSubspaceRetraction
- Euler.HilbertQuadraticFlow
- Euler.InitialDataBridge
- Euler.InitialH1OperatorProduct
- Euler.InitialTimePrimitive
- Euler.InjectivePathDerivative
- Euler.InjectivePathDerivativeWithin
- Euler.IntegralEnergyBootstrap
- Euler.IntegralPathLimit
- Euler.IntervalPathConcatenation
- Euler.InverseMapJetContinuity
- Euler.InviscidCorrectionCompatibility
- Euler.InviscidCorrectionParity
- Euler.InviscidCorrectionRestriction
- Euler.InviscidCorrectionUniqueness
- Euler.InviscidDifferencePDE
- Euler.InviscidSobolevEvolution
- Euler.IsometricActionCalculus
- Euler.IsometricActionDerivativeBound
- Euler.IsometricActionWords
- Euler.LiftedSmoothTimeField
- Euler.LiftedSmoothTimeFieldBounds
- Euler.LiftedTransportComponents
- Euler.LiftedTransportTrace
- Euler.LiftedVelocitySplit
- Euler.LinearDuhamel
- Euler.LinearDuhamelFrozenGevrey
- Euler.LinearDuhamelFrozenOperator
- Euler.LinearDuhamelGevrey
- Euler.LinearDuhamelNaturality
- Euler.LinearDuhamelOperator
- Euler.LinearDuhamelParameter
- Euler.LinearDuhamelSobolevGevrey
- Euler.LinearDuhamelSymmetry
- Euler.LinearDuhamelWeighted
- Euler.LinearDuhamelWeightedNaturality
- Euler.LinearEvolutionDeterminant
- Euler.LinearFundamentalExistence
- Euler.LinearFundamentalPath
- Euler.LocalFlowTrap
- Euler.LogarithmicCutoffOptimization
- Euler.LowerTransportSource
- Euler.LpBochnerRealization
- Euler.LpCompactTranslation
- Euler.LpCylinderCoefficientTime
- Euler.LpCylinderCoefficientTimeInvestigation
- Euler.LpCylinderCoefficients
- Euler.LpCylinderFullTime
- Euler.LpCylinderNormalBounds
- Euler.LpCylinderOrbit
- Euler.LpCylinderPathBounds
- Euler.LpCylinderPaths
- Euler.LpCylinderRectangular
- Euler.LpCylinderRectangularRegularity
- Euler.LpCylinderRegularCoefficient
- Euler.LpCylinderRegularForward
- Euler.LpCylinderRegularSobolev
- Euler.LpCylinderSolutionTranslation
- Euler.LpCylinderTimeWeight
- Euler.LpCylinderTranslation
- Euler.LpCylinderUnweightedForward
- Euler.LpDerivativeBundling
- Euler.LpDerivativeMap
- Euler.LpDominatedConvergence
- Euler.LpDominatedDerivative
- Euler.LpFiniteTensorReconstruction
- Euler.LpMultilinearBundling
- Euler.LpOperatorField
- Euler.LpOperatorFieldAlgebra
- Euler.LpOperatorFieldPath
- Euler.LpParameterIntegral
- Euler.LpPointwiseMultiplier
- Euler.LpSmoothApproximation
- Euler.LpSmoothCoefficientContinuity
- Euler.LpSmoothCoefficientProduct
- Euler.LpSmoothFamily
- Euler.LpSmoothFamilyJets
- Euler.LpSmoothField
- Euler.LpSmoothFieldAlgebra
- Euler.LpSmoothFieldJets
- Euler.LpSmoothJetField
- Euler.LpSpatialCutoff
- Euler.LpSupportedConstructedEvolution
- Euler.LpSupportedEvolution
- Euler.LpSupportedMultiplier
- Euler.LpSupportedSubspace
- Euler.LpSupportedTranslation
- Euler.LpTranslation
- Euler.MaximalTopCauchy
- Euler.MeanAccelerationGevrey
- Euler.MeanAccelerationSobolev
- Euler.MeanBoundaryCoercivity
- Euler.MeanBoundaryDerivative
- Euler.MeanBoundaryDifference
- Euler.MeanBoundaryFrechet
- Euler.MeanBoundaryGevrey
- Euler.MeanBoundaryIterated
- Euler.MeanBoundaryLocalization
- Euler.MeanBoundaryMixed
- Euler.MeanBoundaryOperator
- Euler.MeanBoundaryPhysicalSupport
- Euler.MeanBoundaryReflection
- Euler.MeanBoundaryTranslation
- Euler.MeanClassicalConstraints
- Euler.MeanClassicalSpatialTime
- Euler.MeanClassicalTime
- Euler.MeanClassicalWordBounds
- Euler.MeanCoefficientFrame
- Euler.MeanCoefficientMultipliers
- Euler.MeanCoefficientPath
- Euler.MeanCoefficientPathJets
- Euler.MeanCoefficientSpatial
- Euler.MeanCoefficientTime
- Euler.MeanConcreteTranslation
- Euler.MeanContinuousAcceleration
- Euler.MeanContinuousPhysical
- Euler.MeanContinuousPressure
- Euler.MeanContinuousSobolev
- Euler.MeanContinuousVelocity
- Euler.MeanCoordinatePath
- Euler.MeanCurlIntegration
- Euler.MeanCurlTensor
- Euler.MeanCutoffCurlBound
- Euler.MeanCutoffDifferenceBound
- Euler.MeanCutoffTaylor
- Euler.MeanCylinderSolenoidal
- Euler.MeanCylinderWordBounds
- Euler.MeanDisplacementRegularity
- Euler.MeanFixedCoefficientGevrey
- Euler.MeanFixedCoefficientRegularity
- Euler.MeanFixedFrameTransport
- Euler.MeanFixedReflection
- Euler.MeanFixedSobolevGevrey
- Euler.MeanFixedSpaceInverse
- Euler.MeanFixedTranslation
- Euler.MeanForcingTranslation
- Euler.MeanFormGevrey
- Euler.MeanFrameCoefficients
- Euler.MeanGradientTestSpace
- Euler.MeanGramTranslation
- Euler.MeanHarmonicComponents
- Euler.MeanHarmonicCutoffEnergy
- Euler.MeanHarmonicDecomposition
- Euler.MeanHarmonicDerivatives
- Euler.MeanHarmonicEnergy
- Euler.MeanHarmonicH2
- Euler.MeanHarmonicInterior
- Euler.MeanHarmonicInteriorEnergy
- Euler.MeanHarmonicLaplacian
- Euler.MeanHarmonicScaling
- Euler.MeanHarmonicSmallBall
- Euler.MeanInteriorCutoffs
- Euler.MeanL2Scaling
- Euler.MeanLocalL2Energy
- Euler.MeanLocalizedQuadraticBound
- Euler.MeanMollificationHarmonic
- Euler.MeanMollifierLimit
- Euler.MeanMomentumBoundary
- Euler.MeanMomentumRegularity
- Euler.MeanOperatorReflection
- Euler.MeanOperatorTranslation
- Euler.MeanOrbitSmoothL2Field
- Euler.MeanOrbitSobolev
- Euler.MeanOrdinaryLift
- Euler.MeanPacketAngularForcing
- Euler.MeanPacketBudget
- Euler.MeanPacketConstraints
- Euler.MeanPacketContract
- Euler.MeanPacketCylinderFields
- Euler.MeanPacketData
- Euler.MeanPacketEnvelopeBounds
- Euler.MeanPacketEnvelopeBoundsNoOptions
- Euler.MeanPacketForcing
- Euler.MeanPacketForcingAlgebra
- Euler.MeanPacketForcingProduct
- Euler.MeanPacketHomogeneity
- Euler.MeanPacketInitialZero
- Euler.MeanPacketJets
- Euler.MeanPacketNonlinearForcing
- Euler.MeanPacketOrbitForcing
- Euler.MeanPacketParity
- Euler.MeanPacketPathEnvelope
- Euler.MeanPacketPressureForcing
- Euler.MeanPacketProvider
- Euler.MeanPacketReflection
- Euler.MeanPacketSobolevData
- Euler.MeanPacketZeroForcing
- Euler.MeanPathLpBlocks
- Euler.MeanPathSpatialRepresentative
- Euler.MeanPathTimeDerivative
- Euler.MeanPhysicalTranslation
- Euler.MeanPointwiseGramTranslation
- Euler.MeanPressurePotential
- Euler.MeanPressureRepresentative
- Euler.MeanPressureSobolev
- Euler.MeanScalarMollification
- Euler.MeanScalarProductDerivatives
- Euler.MeanScalarSobolev
- Euler.MeanScaledBoundaryGevrey
- Euler.MeanScaledCutoff
- Euler.MeanSmoothRepresentative
- Euler.MeanSobolevBoundedField
- Euler.MeanSolenoidalReflection
- Euler.MeanSolenoidalSpace
- Euler.MeanSolenoidalTranslation
- Euler.MeanSourceFixedInverse
- Euler.MeanSourceGevrey
- Euler.MeanSourceOperatorRegularity
- Euler.MeanSourcePressureSobolev
- Euler.MeanSourceSobolev
- Euler.MeanSourceSpatialRegularity
- Euler.MeanSourceStrongInverse
- Euler.MeanSourceStrongSobolev
- Euler.MeanSourceTimeSobolev
- Euler.MeanSourceVariationalInverse
- Euler.MeanSpatialDerivative
- Euler.MeanSpatialEvaluation
- Euler.MeanSpatialTimeDerivative
- Euler.MeanStrongContinuousGevrey
- Euler.MeanStrongCoordinates
- Euler.MeanStrongEquation
- Euler.MeanStrongEstimates
- Euler.MeanStrongGevrey
- Euler.MeanStrongInverse
- Euler.MeanStrongSobolev
- Euler.MeanTimeContinuousTranslation
- Euler.MeanTimeReflection
- Euler.MeanTimeSobolev
- Euler.MeanTimeTranslation
- Euler.MeanTranslatedGevrey
- Euler.MeanTranslatedInverse
- Euler.MeanVariationalInverse
- Euler.MeanVariationalOperator
- Euler.MeanVectorIdentities
- Euler.MeanVelocityOperator
- Euler.MeanVelocityPressure
- Euler.MeanWeakCurl
- Euler.MeanWeakHarmonicInterior
- Euler.MeanWeakHarmonicScaling
- Euler.MetricHeatEnergy
- Euler.MetricPathConvergence
- Euler.MetricRootLimit
- Euler.MildEquationBridge
- Euler.MildMajorantEnergy
- Euler.MildTopWord
- Euler.MildWordEquation
- Euler.MixedH5Product
- Euler.MixedWordProduct
- Euler.MovingNormalProjection
- Euler.NoIncomingVorticity
- Euler.NonlinearEnergyConstants
- Euler.NonlinearPressureLower
- Euler.NonnegativeImproperIntegral
- Euler.NonnegativeLogConvex
- Euler.NormalPacketFrequencyGuards
- Euler.OperatorGevreyCalculus
- Euler.OrdinaryAdvectionLimit
- Euler.OrdinaryBKMReduction
- Euler.OrdinaryCauchyInterpolation
- Euler.OrdinaryEulerBKM
- Euler.OrdinaryEulerCauchy
- Euler.OrdinaryEulerClassicalClass
- Euler.OrdinaryEulerConcatenation
- Euler.OrdinaryEulerContinuation
- Euler.OrdinaryEulerDifference
- Euler.OrdinaryEulerEndpoint
- Euler.OrdinaryEulerGradientControl
- Euler.OrdinaryEulerHigherEnergy
- Euler.OrdinaryEulerKineticEnergy
- Euler.OrdinaryEulerL2Stability
- Euler.OrdinaryEulerLifespan
- Euler.OrdinaryEulerLimit
- Euler.OrdinaryEulerLocalCauchy
- Euler.OrdinaryEulerLocalExistence
- Euler.OrdinaryEulerLogarithmicControl
- Euler.OrdinaryEulerMaximal
- Euler.OrdinaryEulerNontriviality
- Euler.OrdinaryEulerRescaling
- Euler.OrdinaryEulerRestriction
- Euler.OrdinaryEulerSobolevClass
- Euler.OrdinaryEulerStability
- Euler.OrdinaryEulerUniqueness
- Euler.OrdinaryEulerVaryingHorizon
- Euler.OrdinaryEulerVorticity
- Euler.OrdinaryFieldAlgebra
- Euler.OrdinaryFieldScaling
- Euler.OrdinaryGradientEnergy
- Euler.OrdinaryGradientInterpolation
- Euler.OrdinaryGradientLimit
- Euler.OrdinaryGradientProducts
- Euler.OrdinaryGradientStability
- Euler.OrdinaryH3Commutator
- Euler.OrdinaryH3Energy
- Euler.OrdinaryH3Envelope
- Euler.OrdinaryH3Norms
- Euler.OrdinaryH3Products
- Euler.OrdinaryHelmholtzField
- Euler.OrdinaryL2Integration
- Euler.OrdinaryLogarithmicGradient
- Euler.OrdinaryMaximalVorticity
- Euler.OrdinaryMaximalVorticityIntegral
- Euler.OrdinaryMollifier
- Euler.OrdinaryPerturbedEnergy
- Euler.OrdinaryPressureCancellation
- Euler.OrdinaryQuadraticControl
- Euler.OrdinaryQuadraticStability
- Euler.OrdinaryRegularizationError
- Euler.OrdinaryRegularizedCauchy
- Euler.OrdinaryRegularizedEnergy
- Euler.OrdinaryRegularizedEquation
- Euler.OrdinaryRegularizedFlow
- Euler.OrdinaryRegularizer
- Euler.OrdinarySmoothLimit
- Euler.OrdinarySmoothWords
- Euler.OrdinarySmoothingOperator
- Euler.OrdinarySobolevL4
- Euler.OrdinarySobolevTower
- Euler.OrdinaryStrongTime
- Euler.OrdinaryTameEnergy
- Euler.OrdinaryTameProduct
- Euler.OrdinaryTransportCancellation
- Euler.OrdinaryVariableGronwall
- Euler.OrdinaryVorticityCoordinates
- Euler.OrdinaryWordBounds
- Euler.OrdinaryWordConstraints
- Euler.OrdinaryWordInterpolation
- Euler.OrdinaryWordTime
- Euler.PDEEnergyLimit
- Euler.PDEMajorantLimit
- Euler.PDESubintervalEnergyLimit
- Euler.PacketActivationConstructed
- Euler.PacketActivationData
- Euler.PacketActivationFrame
- Euler.PacketActivationHistory
- Euler.PacketActivationInitial
- Euler.PacketActivationLipschitz
- Euler.PacketActivationNeighbor
- Euler.PacketActivationRay
- Euler.PacketActivationScales
- Euler.PacketActivationSourceData
- Euler.PacketActualFrameEstimates
- Euler.PacketAmplitudeBounds
- Euler.PacketAngularPotential
- Euler.PacketAngularPressureStepBound
- Euler.PacketApproximationBounds
- Euler.PacketApproximationNormalization
- Euler.PacketBaseGuardScales
- Euler.PacketBeforeTargetSize
- Euler.PacketBudgetTimeChange
- Euler.PacketChildFieldMatch
- Euler.PacketChildLowBounds
- Euler.PacketCoarseMajorant
- Euler.PacketCoefficientLipschitz
- Euler.PacketCoefficientMotion
- Euler.PacketCoefficientTower
- Euler.PacketCoefficientTowerBounds
- Euler.PacketCofactorGevrey
- Euler.PacketCofactorOperator
- Euler.PacketCommonRadius
- Euler.PacketCommonScaleChoice
- Euler.PacketConstructedPiola
- Euler.PacketConstructedProfiles
- Euler.PacketContinuousInverse
- Euler.PacketControlledPropagator
- Euler.PacketConvolutionBounds
- Euler.PacketCoordinateJets
- Euler.PacketCoordinateResidual
- Euler.PacketCoordinateSobolev
- Euler.PacketCorrectionCoefficientBudget
- Euler.PacketCorrectionCoefficientParity
- Euler.PacketCorrectionConstants
- Euler.PacketCorrectionGrowth
- Euler.PacketCorrectionMetric
- Euler.PacketCorrectionMetricBounds
- Euler.PacketCorrectionMetricBudget
- Euler.PacketCorrectionMetricTime
- Euler.PacketCorrectionOutputPolynomial
- Euler.PacketCorrectionPrimitiveBounds
- Euler.PacketCorrectionPrimitivePolynomial
- Euler.PacketCorrectionRapidDecay
- Euler.PacketCorrectionScalar
- Euler.PacketCorrectionSourceData
- Euler.PacketCrossProduct
- Euler.PacketCurlCoordinates
- Euler.PacketCurlTime
- Euler.PacketCurlTransport
- Euler.PacketCylinderAngularRegularity
- Euler.PacketCylinderBoundTransfer
- Euler.PacketCylinderCoefficientBounds
- Euler.PacketCylinderCoefficientData
- Euler.PacketCylinderConvolution
- Euler.PacketCylinderField
- Euler.PacketCylinderFieldAdvection
- Euler.PacketCylinderFieldAlgebra
- Euler.PacketCylinderFieldAverage
- Euler.PacketCylinderFieldBounds
- Euler.PacketCylinderFieldProducts
- Euler.PacketCylinderFieldSupport
- Euler.PacketCylinderFieldUnique
- Euler.PacketCylinderFieldWeight
- Euler.PacketCylinderForcingParity
- Euler.PacketCylinderHighForcing
- Euler.PacketCylinderHighMean
- Euler.PacketCylinderHighParity
- Euler.PacketCylinderHighPartBounds
- Euler.PacketCylinderHighSupport
- Euler.PacketCylinderJetOperations
- Euler.PacketCylinderJetParity
- Euler.PacketCylinderKnownForce
- Euler.PacketCylinderKnownJets
- Euler.PacketCylinderLinearTermBudget
- Euler.PacketCylinderMeanParity
- Euler.PacketCylinderMeanSolenoidal
- Euler.PacketCylinderMeanStep
- Euler.PacketCylinderParity
- Euler.PacketCylinderPiolaCorrector
- Euler.PacketCylinderPiolaPair
- Euler.PacketCylinderPrefixLocality
- Euler.PacketCylinderPressureLocality
- Euler.PacketCylinderProfileChange
- Euler.PacketCylinderRecursiveAdmissibility
- Euler.PacketCylinderScalarGradient
- Euler.PacketCylinderScalarGradientBounds
- Euler.PacketCylinderScalarGradientWeight
- Euler.PacketCylinderSpatialInvariance
- Euler.PacketCylinderSpatialJet
- Euler.PacketCylinderTermBudget
- Euler.PacketCylinderTimeParity
- Euler.PacketCylinderTimeUnique
- Euler.PacketCylinderWeightedAdvection
- Euler.PacketCylinderWeightedLinear
- Euler.PacketCylinderWeightedProduct
- Euler.PacketEarlyPhysical
- Euler.PacketEulerianRegularity
- Euler.PacketExactEulerianField
- Euler.PacketExactGlobalChoice
- Euler.PacketExactGlobalShear
- Euler.PacketExactPhysicalDivergence
- Euler.PacketExactPhysicalEuler
- Euler.PacketExactPhysicalMomentum
- Euler.PacketExactPressureError
- Euler.PacketExactShearError
- Euler.PacketExactSourceEquation
- Euler.PacketExponentialTail
- Euler.PacketFieldDrift
- Euler.PacketFieldGraphBounds
- Euler.PacketFieldJetLp
- Euler.PacketFieldMap
- Euler.PacketFieldParityAlgebra
- Euler.PacketFieldPhysicalSobolev
- Euler.PacketFieldSmoothTimeField
- Euler.PacketFieldSobolev
- Euler.PacketFieldSobolevBudget
- Euler.PacketFieldTensorBounds
- Euler.PacketFieldTimeFreeze
- Euler.PacketFieldTower
- Euler.PacketFiniteApproximationBounds
- Euler.PacketFiniteAssemblyBounds
- Euler.PacketFiniteCoarseBounds
- Euler.PacketFiniteFieldAlgebra
- Euler.PacketFiniteFrequencyBounds
- Euler.PacketFiniteLifespan
- Euler.PacketFiniteParity
- Euler.PacketFiniteProfileBounds
- Euler.PacketFiniteProfileFields
- Euler.PacketFiniteRemainderBounds
- Euler.PacketFiniteSumBounds
- Euler.PacketFiniteVelocityBounds
- Euler.PacketFirstLowBounds
- Euler.PacketFirstPressureSign
- Euler.PacketFirstStageSupport
- Euler.PacketFiveCostGuards
- Euler.PacketFiveCostPolynomial
- Euler.PacketForcingBounds
- Euler.PacketForwardApproximationBounds
- Euler.PacketForwardCanonicalRadius
- Euler.PacketForwardChildLowBounds
- Euler.PacketForwardCoefficientBudgets
- Euler.PacketForwardCommonRadius
- Euler.PacketForwardExactFields
- Euler.PacketForwardExactPressureError
- Euler.PacketForwardFactorization
- Euler.PacketForwardForcedBounds
- Euler.PacketForwardGeometryAssembly
- Euler.PacketForwardGeometryData
- Euler.PacketForwardGeometryLowBounds
- Euler.PacketForwardGlobalShear
- Euler.PacketForwardHessianError
- Euler.PacketForwardInitialSupport
- Euler.PacketForwardInitializedAllOrderBudget
- Euler.PacketForwardInitializedBounds
- Euler.PacketForwardInitializedChildShear
- Euler.PacketForwardInitializedCorrectionChoice
- Euler.PacketForwardInitializedCorrectionData
- Euler.PacketForwardInitializedCorrectionEstimates
- Euler.PacketForwardInitializedCorrectionNorms
- Euler.PacketForwardInitializedCorrectionParity
- Euler.PacketForwardInitializedExactLifted
- Euler.PacketForwardInitializedFieldParity
- Euler.PacketForwardInitializedFlowAndShear
- Euler.PacketForwardInitializedFlowBounds
- Euler.PacketForwardInitializedPressure
- Euler.PacketForwardInitializedProfiles
- Euler.PacketForwardInitializedProfilesParity
- Euler.PacketForwardInitializedResidualEquation
- Euler.PacketForwardInitializedSolenoidal
- Euler.PacketForwardInitializedSpatialBudget
- Euler.PacketForwardInitializedTimeBounds
- Euler.PacketForwardOutputCosts
- Euler.PacketForwardPressureBudgets
- Euler.PacketForwardPressureRemainder
- Euler.PacketForwardPrimary
- Euler.PacketForwardPrimaryBounds
- Euler.PacketForwardPrimaryShear
- Euler.PacketForwardRadiusPolynomial
- Euler.PacketForwardRemainder
- Euler.PacketForwardResidualBounds
- Euler.PacketForwardScalarPressureGrade
- Euler.PacketForwardStepBudget
- Euler.PacketForwardSuccessor
- Euler.PacketForwardUniformBudget
- Euler.PacketForwardUniformChild
- Euler.PacketForwardUniformCosts
- Euler.PacketForwardUniformFlow
- Euler.PacketForwardUniformProfiles
- Euler.PacketFrameCoefficients
- Euler.PacketFrameRenewalAlgebra
- Euler.PacketGeometryAssembly
- Euler.PacketGeometryControlledGrowth
- Euler.PacketGeometryData
- Euler.PacketGeometryGuards
- Euler.PacketGeometryInitialAmplitude
- Euler.PacketGeometryJoinedBudget
- Euler.PacketGeometryLowBounds
- Euler.PacketGeometryPressureCosts
- Euler.PacketGeometryProfileEnvelope
- Euler.PacketGeometrySourceGrowth
- Euler.PacketGevreyProfileChoice
- Euler.PacketGradeAbsorption
- Euler.PacketGraphFlowExplicitBounds
- Euler.PacketGraphFlowFieldBounds
- Euler.PacketGraphFlowFrequency
- Euler.PacketGraphFlowSupBounds
- Euler.PacketGraphHessian
- Euler.PacketHorizonSize
- Euler.PacketIdealSize
- Euler.PacketInductionScaleBounds
- Euler.PacketInductionScales
- Euler.PacketInductionStage
- Euler.PacketInfiniteConstruction
- Euler.PacketInitialAmplitude
- Euler.PacketInitialBounds
- Euler.PacketInitialCostPolynomial
- Euler.PacketInitialDatumSupport
- Euler.PacketInitialExactLimit
- Euler.PacketInitialFields
- Euler.PacketInitialGeometry
- Euler.PacketInitialInput
- Euler.PacketInitialPhysical
- Euler.PacketInitialPolynomialBounds
- Euler.PacketInitialScaleSummability
- Euler.PacketInitialSmoothFields
- Euler.PacketInitialSmoothLimit
- Euler.PacketInitialSummability
- Euler.PacketInitialSupport
- Euler.PacketInitializedAllOrderBudget
- Euler.PacketInitializedBounds
- Euler.PacketInitializedCanonicalRadius
- Euler.PacketInitializedChildBounds
- Euler.PacketInitializedCorrectionBounds
- Euler.PacketInitializedCorrectionChoice
- Euler.PacketInitializedCorrectionData
- Euler.PacketInitializedCorrectionEstimateChoice
- Euler.PacketInitializedCorrectionNorms
- Euler.PacketInitializedCorrectionParity
- Euler.PacketInitializedExactLifted
- Euler.PacketInitializedFieldParity
- Euler.PacketInitializedFlowAndShear
- Euler.PacketInitializedHessianChoice
- Euler.PacketInitializedHessianError
- Euler.PacketInitializedInitial
- Euler.PacketInitializedInitialExact
- Euler.PacketInitializedOutputCosts
- Euler.PacketInitializedParameterBounds
- Euler.PacketInitializedPhysicalChoice
- Euler.PacketInitializedPhysicalFieldsChoice
- Euler.PacketInitializedPointwiseChoice
- Euler.PacketInitializedPressureBudgets
- Euler.PacketInitializedPressureRemainder
- Euler.PacketInitializedProfiles
- Euler.PacketInitializedProfilesParity
- Euler.PacketInitializedRadius
- Euler.PacketInitializedRadiusPolynomial
- Euler.PacketInitializedRemainder
- Euler.PacketInitializedResidualEquation
- Euler.PacketInitializedSolenoidal
- Euler.PacketInitializedSpatialBudget
- Euler.PacketInitializedTimeBounds
- Euler.PacketInitializedUniformBounds
- Euler.PacketInitializedUniformBudget
- Euler.PacketInitializedUniformChild
- Euler.PacketInitializedUniformCosts
- Euler.PacketInitializedUniformFlow
- Euler.PacketInverseFlowContinuity
- Euler.PacketInverseFlowGevrey
- Euler.PacketInverseFlowSobolevBound
- Euler.PacketJetAssembly
- Euler.PacketJoinedApproximationBounds
- Euler.PacketJoinedCoefficientBudgets
- Euler.PacketJoinedGradeBounds
- Euler.PacketJoinedPressureAssembly
- Euler.PacketJoinedProfilesParity
- Euler.PacketJoinedProfilesRegularity
- Euler.PacketJoinedResidualBounds
- Euler.PacketJoinedResidualFields
- Euler.PacketJoinedSourceConstraints
- Euler.PacketJoinedSourceEquations
- Euler.PacketJoinedSourceOperators
- Euler.PacketJoinedSourcePiola
- Euler.PacketJoinedSourceProfiles
- Euler.PacketJoinedSourceRegularity
- Euler.PacketJoinedSourceResidual
- Euler.PacketJoinedSourceSolenoidal
- Euler.PacketJoinedStepBudget
- Euler.PacketJoinedStepParity
- Euler.PacketJoinedStepRegularity
- Euler.PacketJoinedSuccessor
- Euler.PacketJoinedUniformProfiles
- Euler.PacketKnownDecomposition
- Euler.PacketKnownGrade
- Euler.PacketKnownPieceBounds
- Euler.PacketKnownPieceScales
- Euler.PacketKnownPieces
- Euler.PacketKnownTermBounds
- Euler.PacketKnownTermFields
- Euler.PacketKnownTermProfiles
- Euler.PacketKnownTermScales
- Euler.PacketKnownTermSums
- Euler.PacketLiftedCoefficient
- Euler.PacketLiftedCoefficientBounds
- Euler.PacketLiftedCurl
- Euler.PacketLiftedFlowData
- Euler.PacketLiftedParity
- Euler.PacketLiftedPiola
- Euler.PacketLiftedSmallness
- Euler.PacketLiftedTimeBounds
- Euler.PacketLinearCostAbsorption
- Euler.PacketLowBoundPropagation
- Euler.PacketLowConstants
- Euler.PacketLowGrades
- Euler.PacketMajorantShift
- Euler.PacketMaskedProductBounds
- Euler.PacketMatchingFamily
- Euler.PacketMatrixCoefficientAlgebra
- Euler.PacketMatrixCoefficientGevrey
- Euler.PacketMatrixContinuity
- Euler.PacketMatrixNormalization
- Euler.PacketMeanGradeBounds
- Euler.PacketMeanPressureGradient
- Euler.PacketMeanPressureStepBound
- Euler.PacketMomentumExpansion
- Euler.PacketMovingFrame
- Euler.PacketMovingRay
- Euler.PacketMovingVelocity
- Euler.PacketNeighborControlled
- Euler.PacketNeighborInitial
- Euler.PacketNeighborStability
- Euler.PacketNestedHorizons
- Euler.PacketNormalDriftBounds
- Euler.PacketNormalTimeMap
- Euler.PacketNormalizedPrimary
- Euler.PacketOrientedCoordinates
- Euler.PacketParameterEnvelope
- Euler.PacketParentCoefficientBounds
- Euler.PacketParentFlowDifferentiation
- Euler.PacketParentForwardBudget
- Euler.PacketParentJacobiCoefficient
- Euler.PacketParentJoinedBudget
- Euler.PacketParentLabelBounds
- Euler.PacketParentLabelBudgets
- Euler.PacketParentLabelCoefficients
- Euler.PacketParentMeanBudget
- Euler.PacketParentMeanCoercivity
- Euler.PacketParentNormalBudget
- Euler.PacketParentPhysicalBudgets
- Euler.PacketParentTransverseCosts
- Euler.PacketPeriodicPotential
- Euler.PacketPhysicalCoefficients
- Euler.PacketPhysicalCompression
- Euler.PacketPhysicalCorrectionPotential
- Euler.PacketPhysicalCostPolynomial
- Euler.PacketPhysicalEulerTransform
- Euler.PacketPhysicalFamily
- Euler.PacketPhysicalFieldTower
- Euler.PacketPhysicalFrameRenewal
- Euler.PacketPhysicalFrequencyBounds
- Euler.PacketPhysicalGevrey
- Euler.PacketPhysicalLowBounds
- Euler.PacketPhysicalNeighbor
- Euler.PacketPhysicalNormBounds
- Euler.PacketPhysicalPressureGevrey
- Euler.PacketPhysicalPropagator
- Euler.PacketPhysicalSign
- Euler.PacketPhysicalSize
- Euler.PacketPhysicalStage
- Euler.PacketPiola
- Euler.PacketPiolaAlgebra
- Euler.PacketPiolaPair
- Euler.PacketPointJets
- Euler.PacketPotentialMultiplier
- Euler.PacketPotentialNormalMap
- Euler.PacketPotentialParity
- Euler.PacketPotentialRegularity
- Euler.PacketPressureCovector
- Euler.PacketPressureFastBounds
- Euler.PacketPressureFastHessian
- Euler.PacketPressureJet
- Euler.PacketPressureRemainder
- Euler.PacketPressureScaleCosts
- Euler.PacketPressureSeries
- Euler.PacketPressureSymmetry
- Euler.PacketPressureWitness
- Euler.PacketPrimaryCommonRadius
- Euler.PacketPrimaryDynamics
- Euler.PacketPrimaryFactorization
- Euler.PacketPrimaryFullShear
- Euler.PacketPrimaryGlobalShear
- Euler.PacketPrimaryGradeBounds
- Euler.PacketPrimaryParity
- Euler.PacketPrimaryPressureShear
- Euler.PacketPrimaryRegularity
- Euler.PacketPrimaryScaling
- Euler.PacketPrimaryShearIdentity
- Euler.PacketPrimarySourceParity
- Euler.PacketPrimarySourceRegularity
- Euler.PacketPrimaryUncut
- Euler.PacketProfileBudget
- Euler.PacketProfileBudgetTimeChange
- Euler.PacketProfileBudgetTransport
- Euler.PacketProfileCoarseBounds
- Euler.PacketProfileEnvelope
- Euler.PacketProfileParity
- Euler.PacketProfileRecursion
- Euler.PacketProfileRegularity
- Euler.PacketProfileStepParity
- Euler.PacketProfileStepRegularity
- Euler.PacketProfileTailEstimates
- Euler.PacketProfileTailGrade
- Euler.PacketProfilesParity
- Euler.PacketProfilesRegularity
- Euler.PacketPropagationTime
- Euler.PacketRadiusCostPolynomial
- Euler.PacketRecursionAlgebra
- Euler.PacketRecursiveBase
- Euler.PacketRecursiveCancellation
- Euler.PacketRecursiveForcing
- Euler.PacketRecursiveResidual
- Euler.PacketReferenceRatio
- Euler.PacketRemainderBounds
- Euler.PacketResidualGrades
- Euler.PacketResidualTailActual
- Euler.PacketResidualTailDecomposition
- Euler.PacketResidualTailFields
- Euler.PacketScalarPressureGrade
- Euler.PacketScalarPressureGradient
- Euler.PacketScalarUniqueness
- Euler.PacketScaledRay
- Euler.PacketScaledVelocity
- Euler.PacketScaledVelocityAlgebra
- Euler.PacketScaledVelocitySystem
- Euler.PacketShearMotion
- Euler.PacketShiftArithmetic
- Euler.PacketShiftArithmeticNoOptions
- Euler.PacketShiftedTimeGluing
- Euler.PacketShortTimePhysicalGrowth
- Euler.PacketShortTimePropagator
- Euler.PacketSizeComparison
- Euler.PacketSlicedAssembly
- Euler.PacketSlicedJets
- Euler.PacketSlicedResidual
- Euler.PacketSourceCoefficientBudget
- Euler.PacketSourceCoefficientGevrey
- Euler.PacketSourceCorrectionCoefficients
- Euler.PacketSourceEquations
- Euler.PacketSourceFrequency
- Euler.PacketSourceGeometryAssembly
- Euler.PacketSourceGeometryData
- Euler.PacketSourceGeometryGrowth
- Euler.PacketSourceInitialMean
- Euler.PacketSourceMeanZero
- Euler.PacketSourceOperators
- Euler.PacketSourceParameterScales
- Euler.PacketSourceParity
- Euler.PacketSourcePiola
- Euler.PacketSourcePressureAssembly
- Euler.PacketSourcePrimitiveBounds
- Euler.PacketSourceProfiles
- Euler.PacketSourcePropagator
- Euler.PacketSourceRadiusPolynomial
- Euler.PacketSourceRegularity
- Euler.PacketSourceResidual
- Euler.PacketSourceResidualFields
- Euler.PacketSourceScaleActual
- Euler.PacketSourceScaleBounds
- Euler.PacketSourceScaleChoice
- Euler.PacketSourceScaleFromCosts
- Euler.PacketSourceScaleGuards
- Euler.PacketSourceScaleSequence
- Euler.PacketSourceScaleShift
- Euler.PacketSourceSmoothField
- Euler.PacketSourceSolenoidal
- Euler.PacketSourceUniformEnvelope
- Euler.PacketSourceVolumeSobolev
- Euler.PacketStageContradiction
- Euler.PacketStageEstimates
- Euler.PacketStageGeometry
- Euler.PacketStageGrowth
- Euler.PacketStageGuards
- Euler.PacketStageInitialLimit
- Euler.PacketStageInputs
- Euler.PacketStageLocalExistence
- Euler.PacketStageLowPropagation
- Euler.PacketStagePhysicalBounds
- Euler.PacketStageRestriction
- Euler.PacketTailBase
- Euler.PacketTailBound
- Euler.PacketTailGradeBounds
- Euler.PacketTailLinearBounds
- Euler.PacketTailNonlinearBounds
- Euler.PacketTailNormalization
- Euler.PacketTailProductBounds
- Euler.PacketTailSumBounds
- Euler.PacketTangentInvariant
- Euler.PacketTangentNorm
- Euler.PacketTargetAmplification
- Euler.PacketTerminalAdmissible
- Euler.PacketTerminalDatum
- Euler.PacketTerminalDatumBounds
- Euler.PacketTerminalEnvelope
- Euler.PacketTerminalInitialData
- Euler.PacketTerminalPrimaryBudget
- Euler.PacketTerminalPrimaryFields
- Euler.PacketTimeAlgebra
- Euler.PacketTimePathGluing
- Euler.PacketTimeProfileArithmetic
- Euler.PacketTimeProfiles
- Euler.PacketTimeWordGluing
- Euler.PacketTriangular
- Euler.PacketUniformFrequencyMargin
- Euler.PacketUniformFrequencyScales
- Euler.PacketUniformInitialBounds
- Euler.PacketUniversalFrequency
- Euler.PacketUnweightedAdvection
- Euler.PacketVelocityPropagator
- Euler.PacketVolumeDivergence
- Euler.PacketWeightedPhysicalErrors
- Euler.PacketWithinRay
- Euler.PacketWithinStage
- Euler.ParameterNestedWordSum
- Euler.ParameterSobolevAcceleration
- Euler.ParameterSobolevBlocks
- Euler.ParameterSobolevCoefficient
- Euler.ParameterSobolevCommutator
- Euler.ParameterSobolevCostMonotone
- Euler.ParameterSobolevFiniteSum
- Euler.ParameterSobolevGevrey
- Euler.ParameterSobolevGevreyAt
- Euler.ParameterSobolevInverse
- Euler.ParameterSobolevLinear
- Euler.ParameterSobolevLocal
- Euler.ParameterSobolevOperations
- Euler.ParameterSobolevPair
- Euler.ParameterSobolevProductAt
- Euler.ParameterSobolevProductGevrey
- Euler.ParameterSobolevScaling
- Euler.ParameterSobolevTensorInverse
- Euler.ParameterWordCalculus
- Euler.ParameterWordGevrey
- Euler.ParameterWordHigher
- Euler.ParameterWordInverse
- Euler.ParameterWordLocal
- Euler.ParameterWordProduct
- Euler.ParameterWordRestriction
- Euler.ParentChildEulerMatch
- Euler.ParentChoiceInitialSupport
- Euler.ParentCoefficientPolynomial
- Euler.ParentCorrectionCostEnvelope
- Euler.ParentEulerChild
- Euler.ParentEulerEndpoints
- Euler.ParentEulerLowBounds
- Euler.ParentEulerParity
- Euler.ParentEulerSobolev
- Euler.ParentEulerSobolevChild
- Euler.ParentEulerState
- Euler.ParentFirstPacketLowGuards
- Euler.ParentForwardGeometryGuards
- Euler.ParentForwardGeometryInput
- Euler.ParentForwardInitialSupport
- Euler.ParentForwardNormalParameters
- Euler.ParentForwardRadiusPolynomial
- Euler.ParentForwardUniformCosts
- Euler.ParentFrameReframe
- Euler.ParentGeometryChoiceCenter
- Euler.ParentGeometryChoiceInitial
- Euler.ParentGeometryChoiceLow
- Euler.ParentGeometryChoiceRenewal
- Euler.ParentGeometryForwardChoice
- Euler.ParentGeometryForwardChoiceNoOptions
- Euler.ParentGeometryInitialBounds
- Euler.ParentGeometryJoinedChoice
- Euler.ParentGeometryJoinedChoiceInvestigation
- Euler.ParentHistoryCostPolynomial
- Euler.ParentHistoryFrequencyGuard
- Euler.ParentHomogeneousPacketLowBounds
- Euler.ParentInitializedRadiusPolynomial
- Euler.ParentInitializedState
- Euler.ParentInitializedUniformCosts
- Euler.ParentLagrangianEuler
- Euler.ParentNeighborThreshold
- Euler.ParentNormalPacketParameters
- Euler.ParentNormalizedEuler
- Euler.ParentNormalizedGeometry
- Euler.ParentOrdinaryEvolution
- Euler.ParentPacketBadRatioPolynomial
- Euler.ParentPacketChildChoice
- Euler.ParentPacketChildLowGuards
- Euler.ParentPacketCorrectionParity
- Euler.ParentPacketExactDivergence
- Euler.ParentPacketExactEuler
- Euler.ParentPacketExactPressure
- Euler.ParentPacketForwardChildChoice
- Euler.ParentPacketForwardInput
- Euler.ParentPacketFrames
- Euler.ParentPacketGeometryFrame
- Euler.ParentPacketGeometryGuards
- Euler.ParentPacketGeometryInput
- Euler.ParentPacketHessianSymmetry
- Euler.ParentPacketHistoryLowBounds
- Euler.ParentPacketHistoryNeighbor
- Euler.ParentPacketHistoryPolynomial
- Euler.ParentPacketInitialLowBounds
- Euler.ParentPacketJoinedInput
- Euler.ParentPacketLabelData
- Euler.ParentPacketNeighborBounds
- Euler.ParentPacketNeighborPolynomial
- Euler.ParentPacketNeighborScaleGuard
- Euler.ParentPacketParameterCaps
- Euler.ParentPacketParity
- Euler.ParentPacketPhysicalCoefficients
- Euler.ParentPacketPhysicalFrame
- Euler.ParentPacketPrimaryCenter
- Euler.ParentPacketRestriction
- Euler.ParentPacketScaledBounds
- Euler.ParentPacketSobolevFields
- Euler.ParentPacketSourceData
- Euler.ParentPacketStateGeometry
- Euler.ParentPacketStrainEvolution
- Euler.ParentParticleInverse
- Euler.ParentParticleRegularity
- Euler.ParentRenewalParameters
- Euler.ParentRenewalPrefix
- Euler.ParentRenewalScaleApplication
- Euler.ParentRenewalScaleCosts
- Euler.ParentShortForwardRadius
- Euler.ParentStageDirection
- Euler.ParentStageHorizon
- Euler.ParentState
- Euler.ParentStateGeometry
- Euler.ParentTargetRenewal
- Euler.ParentUniformForwardChild
- Euler.ParentUniformJoinedChild
- Euler.PartialCorrectionBootstrap
- Euler.PeriodicDerivativeMean
- Euler.PhysicalChildFields
- Euler.PhysicalChildPacketMatch
- Euler.PhysicalChildParent
- Euler.PhysicalChildSourceBound
- Euler.PhysicalChildStructure
- Euler.PhysicalChildVelocity
- Euler.PhysicalGraphFlowBounds
- Euler.PhysicalGraphFlowSupBounds
- Euler.PhysicalGraphGevrey
- Euler.PhysicalGraphTimeFields
- Euler.PhysicalL2Scaling
- Euler.PolynomialCostMajorant
- Euler.PressureCommutatorWeights
- Euler.ProjectedEnergyForcing
- Euler.ProjectedEulerPairing
- Euler.ProjectedForcingFields
- Euler.QuadraticCauchy
- Euler.QuadraticCoefficients
- Euler.QuadraticHeatConstraint
- Euler.QuadraticHeatLocal
- Euler.QuadraticMildPasting
- Euler.QuadraticSource
- Euler.QuadraticSourceLimit
- Euler.RadialPotentialL2
- Euler.RegularizedEnergyFamily
- Euler.RegularizedForcingRepresentative
- Euler.RegularizedForcingWord
- Euler.RegularizedMetricPaths
- Euler.RegularizedMildEquation
- Euler.RegularizedTopBlocks
- Euler.RegularizedWordConvergence
- Euler.RegularizedWordEquation
- Euler.RegularizedWordTime
- Euler.ResolventCalculus
- Euler.ReversedVorticityTransport
- Euler.ScalarEulerVorticity
- Euler.SeparatingTimeDerivative
- Euler.ShortTimeLinearGrowth
- Euler.SmallCorrectionBounds
- Euler.SmallCorrectionBudget
- Euler.SmallCorrectionParity
- Euler.SmallCorrectionResidual
- Euler.SmallCorrectionScales
- Euler.SmoothBanachFlow
- Euler.SmoothCoefficientPath
- Euler.SmoothCoefficientPathMap
- Euler.SmoothCoefficientTimeRestriction
- Euler.SmoothCylinderAccelerationComposition
- Euler.SmoothCylinderAccelerationLp
- Euler.SmoothCylinderComposition
- Euler.SmoothCylinderFlow
- Euler.SmoothCylinderGevrey
- Euler.SmoothCylinderJets
- Euler.SmoothEulerEvolution
- Euler.SmoothFieldSobolevTime
- Euler.SmoothFlowAcceleration
- Euler.SmoothFlowCoefficientPaths
- Euler.SmoothFlowDeformation
- Euler.SmoothFlowGevrey
- Euler.SmoothFlowJacobian
- Euler.SmoothFlowJets
- Euler.SmoothFlowJoint
- Euler.SmoothFlowParity
- Euler.SmoothFlowTimeGevrey
- Euler.SmoothFlowVolume
- Euler.SmoothGraphFlow
- Euler.SmoothImplicitLift
- Euler.SmoothInequalityTransfer
- Euler.SmoothL2ClassicalBounds
- Euler.SmoothL2CoefficientPath
- Euler.SmoothL2Gevrey
- Euler.SmoothL2GevreyCalculus
- Euler.SmoothL2ScalingContinuity
- Euler.SmoothL2Series
- Euler.SmoothPathJoint
- Euler.SmoothPathSuperposition
- Euler.SmoothPathTimeJets
- Euler.SmoothPhysicalGraphFlow
- Euler.SmoothScaledFlow
- Euler.SmoothTimeAmplitudeBounds
- Euler.SmoothTimeAmplitudeScaling
- Euler.SmoothTimeField
- Euler.SmoothTimeFieldAlgebra
- Euler.SmoothTimeFieldBilinear
- Euler.SmoothTimeFieldChain
- Euler.SmoothTimeFieldComposition
- Euler.SmoothTimeFieldDerivativeBounds
- Euler.SmoothTimeFieldFromPaths
- Euler.SmoothTimeFieldJoint
- Euler.SmoothTimeFieldLinear
- Euler.SmoothTimeFieldOrdinary
- Euler.SmoothTimeFieldParity
- Euler.SmoothTimeFieldPrecomp
- Euler.SmoothTimeFieldRestriction
- Euler.SmoothTimeFieldSecondJoint
- Euler.SmoothTimeFieldTimeJets
- Euler.SmoothTimeSuperposition
- Euler.SobolevBaseCommutator
- Euler.SobolevCauchyInterpolation
- Euler.SobolevCoefficientPressure
- Euler.SobolevCorrectionCompatibility
- Euler.SobolevDifferenceEnergy
- Euler.SobolevDriftNorm
- Euler.SobolevDriftTransport
- Euler.SobolevEllipticBound
- Euler.SobolevEnergyPaths
- Euler.SobolevGevreyOperators
- Euler.SobolevGevreyProduct
- Euler.SobolevHeat
- Euler.SobolevHeatDerivativeCommutation
- Euler.SobolevHeatGenerator
- Euler.SobolevHeatKernel
- Euler.SobolevHeatVolterra
- Euler.SobolevInterpolation
- Euler.SobolevJointEvaluation
- Euler.SobolevL2Product
- Euler.SobolevL2Stability
- Euler.SobolevLaplacian
- Euler.SobolevMaximalRegularity
- Euler.SobolevMetricTransport
- Euler.SobolevNonlinearCompatibility
- Euler.SobolevOperatorCoordinates
- Euler.SobolevParityOperators
- Euler.SobolevPathInterpolation
- Euler.SobolevPathLimits
- Euler.SobolevPointEvaluation
- Euler.SobolevPointMultiplication
- Euler.SobolevPressureResolvent
- Euler.SobolevPressureTime
- Euler.SobolevProduct
- Euler.SobolevProductApproximation
- Euler.SobolevProductJet
- Euler.SobolevReflection
- Euler.SobolevRestriction
- Euler.SobolevSmoothApproximation
- Euler.SobolevSmoothProduct
- Euler.SobolevSmoothing
- Euler.SobolevSourceExponent
- Euler.SobolevTimeRegularization
- Euler.SobolevTopBlocks
- Euler.SobolevTranslationDifferentiation
- Euler.SobolevTransport
- Euler.SobolevTransportCommutator
- Euler.SobolevTransportCompatibility
- Euler.SobolevViscousEnergy
- Euler.SobolevWordBlockCoordinates
- Euler.SobolevWordBlocks
- Euler.SobolevWordConstraints
- Euler.SobolevWordLevel
- Euler.SobolevWordValueIdentity
- Euler.Solution
- Euler.SolutionDefinitions
- Euler.SourceCylinderClassical
- Euler.SourceCylinderClassicalEquation
- Euler.SourceCylinderDerivativeBounds
- Euler.SourceCylinderDerivativeWeight
- Euler.SourceCylinderEquation
- Euler.SourceCylinderForcing
- Euler.SourceCylinderForward
- Euler.SourceCylinderForwardSobolev
- Euler.SourceCylinderMeanZero
- Euler.SourceCylinderParity
- Euler.SourceCylinderPressureField
- Euler.SourceCylinderPressureMean
- Euler.SourceCylinderPressureRegularity
- Euler.SourceCylinderPressureSource
- Euler.SourceCylinderPressureWeight
- Euler.SourceCylinderRegularity
- Euler.SourceCylinderTimeBounds
- Euler.SourceCylinderWeight
- Euler.SourceForwardCoefficient
- Euler.SourceNormalCoefficient
- Euler.SourceNormalResidualBounds
- Euler.SourcePotentialCoefficient
- Euler.SourcePotentialTime
- Euler.SourcePotentialTimeCoefficient
- Euler.SourcePotentialTimePath
- Euler.SquaredMetricStability
- Euler.StageDisplacementBound
- Euler.StageDisplacementConfinement
- Euler.StageInitialSupport
- Euler.StageVorticityConfinement
- Euler.StaticCylinderField
- Euler.StaticEulerCorrection
- Euler.StaticEulerForceField
- Euler.StaticEulerGevrey
- Euler.StaticEulerParity
- Euler.StaticEulerRegularity
- Euler.StaticEulerSolution
- Euler.StaticEulerTime
- Euler.StaticEulerWeightedBounds
- Euler.StrongOperatorDerivative
- Euler.TensorCoordinateEnergyBound
- Euler.TerminalLayerRamp
- Euler.TerminalProjectionTrial
- Euler.TerminalTimePrimitive
- Euler.TimeContinuousPrimitive
- Euler.TimeCorrectionRestriction
- Euler.TimeCorrectionSource
- Euler.TimeCorrectionStrongIdentity
- Euler.TimeEndpointEnergyUniqueness
- Euler.TimeFamily
- Euler.TimeForcingRepresentative
- Euler.TimeH1ContinuousDerivative
- Euler.TimeH1FieldProduct
- Euler.TimeH1FrameTransport
- Euler.TimeH1GeneratorBounds
- Euler.TimeH1OperatorProduct
- Euler.TimeH1PointwiseBounds
- Euler.TimeH1Reconstruction
- Euler.TimeH1ReconstructionNaturality
- Euler.TimeH1SobolevReconstruction
- Euler.TimeH1WeakPairing
- Euler.TimeIntervalGlue
- Euler.TimeLp
- Euler.TimeLpAccelerationForcing
- Euler.TimeLpAccelerationSobolev
- Euler.TimeLpBoundedMap
- Euler.TimeLpCoefficientGevrey
- Euler.TimeLpCoefficientMap
- Euler.TimeLpGramGevrey
- Euler.TimeLpGramInverse
- Euler.TimeLpGramSobolev
- Euler.TimeLpLinearity
- Euler.TimeLpMap
- Euler.TimeLpMultiplier
- Euler.TimeLpObservation
- Euler.TimeLpPairing
- Euler.TimeLpStrongContinuity
- Euler.TimeLpStrongOperators
- Euler.TimeLpSubinterval
- Euler.TimeLpSubintervalBound
- Euler.TimePathApply
- Euler.TimePathGluing
- Euler.TimeSobolevTransport
- Euler.TimeWeakBoundary
- Euler.TimeWeakDerivative
- Euler.TopBlockCauchy
- Euler.TopBlockTimeNorm
- Euler.TransportL2Bilinear
- Euler.TransportL2Time
- Euler.TransverseActivationSelection
- Euler.TransverseActivationTrial
- Euler.TransverseBoundedFrame
- Euler.TransverseBoundedGeometry
- Euler.TransverseCoefficientGevrey
- Euler.TransverseCoordinateRegularity
- Euler.TransverseEndpointBounds
- Euler.TransverseEndpointCoordinates
- Euler.TransverseEndpointDifference
- Euler.TransverseEndpointDifferentiation
- Euler.TransverseEndpointEnergy
- Euler.TransverseEndpointEquation
- Euler.TransverseEndpointGreen
- Euler.TransverseEndpointMomentum
- Euler.TransverseEndpointParameter
- Euler.TransverseEndpointUniqueness
- Euler.TransverseEndpointVelocity
- Euler.TransverseFixedClassical
- Euler.TransverseFixedEndpoint
- Euler.TransverseFixedEvolution
- Euler.TransverseFixedSobolev
- Euler.TransverseFixedSpaceInverse
- Euler.TransverseFixedStrong
- Euler.TransverseForwardCoefficientGevrey
- Euler.TransverseForwardInverse
- Euler.TransverseForwardRegularity
- Euler.TransverseFrameCoordinates
- Euler.TransverseGeneratorDifference
- Euler.TransverseGevreyInverse
- Euler.TransverseGramInverse
- Euler.TransverseGramPath
- Euler.TransverseHighSolveFields
- Euler.TransverseHistoryBounds
- Euler.TransverseHistoryLipschitz
- Euler.TransverseHistoryParentCost
- Euler.TransverseHistoryPolynomialCost
- Euler.TransverseInitialCoordinates
- Euler.TransverseInitialInverse
- Euler.TransverseMomentumRegularity
- Euler.TransverseNormalResidual
- Euler.TransversePacketAmplitude
- Euler.TransversePacketBudget
- Euler.TransversePacketCoefficientBounds
- Euler.TransversePacketCorrector
- Euler.TransversePacketCorrectorBounds
- Euler.TransversePacketCorrectorMean
- Euler.TransversePacketCorrectorNoOptions
- Euler.TransversePacketCorrectorOperator
- Euler.TransversePacketCorrectorParity
- Euler.TransversePacketCorrectorSupport
- Euler.TransversePacketCylinderFields
- Euler.TransversePacketData
- Euler.TransversePacketEndpoint
- Euler.TransversePacketEndpointPointwise
- Euler.TransversePacketForcing
- Euler.TransversePacketForwardBounds
- Euler.TransversePacketForwardBudget
- Euler.TransversePacketForwardFullBounds
- Euler.TransversePacketForwardGradeBounds
- Euler.TransversePacketForwardNorms
- Euler.TransversePacketHistory
- Euler.TransversePacketHistoryBounds
- Euler.TransversePacketHistoryData
- Euler.TransversePacketHistoryParity
- Euler.TransversePacketHistoryPressure
- Euler.TransversePacketHomogeneity
- Euler.TransversePacketInitial
- Euler.TransversePacketInitialRepresentative
- Euler.TransversePacketIntervalData
- Euler.TransversePacketIntervalForcing
- Euler.TransversePacketJets
- Euler.TransversePacketJoinedBounds
- Euler.TransversePacketJoinedCorrector
- Euler.TransversePacketJoinedCorrectorBounds
- Euler.TransversePacketJoinedCorrectorSupport
- Euler.TransversePacketJoinedEquation
- Euler.TransversePacketJoinedField
- Euler.TransversePacketJoinedFullBounds
- Euler.TransversePacketJoinedParity
- Euler.TransversePacketJoinedPaths
- Euler.TransversePacketJoinedPressure
- Euler.TransversePacketJoinedProvider
- Euler.TransversePacketJoinedSupport
- Euler.TransversePacketJoinedUnitBounds
- Euler.TransversePacketLocalHistory
- Euler.TransversePacketMatching
- Euler.TransversePacketNormalBudget
- Euler.TransversePacketPairAmplitude
- Euler.TransversePacketParity
- Euler.TransversePacketPiolaData
- Euler.TransversePacketPressureGradient
- Euler.TransversePacketPressureGradientBounds
- Euler.TransversePacketPressureGradientProperties
- Euler.TransversePacketPressureParity
- Euler.TransversePacketPrimaryBounds
- Euler.TransversePacketPrimaryBudget
- Euler.TransversePacketPrimaryCorrector
- Euler.TransversePacketPrimaryEquation
- Euler.TransversePacketPrimaryField
- Euler.TransversePacketPrimaryFullBounds
- Euler.TransversePacketPrimaryHistory
- Euler.TransversePacketPrimaryHomogeneity
- Euler.TransversePacketPrimaryMatching
- Euler.TransversePacketPrimaryParity
- Euler.TransversePacketPrimaryPaths
- Euler.TransversePacketPrimaryPressure
- Euler.TransversePacketPrimaryRadius
- Euler.TransversePacketPrimaryUnitBounds
- Euler.TransversePacketProvider
- Euler.TransversePacketRegularity
- Euler.TransversePacketTimeData
- Euler.TransversePacketTraceMatching
- Euler.TransverseParameterRegularity
- Euler.TransverseSolutionHomogeneity
- Euler.TransverseSourceCoefficientPath
- Euler.TransverseSourceFrame
- Euler.TransverseStrongAlgebra
- Euler.TransverseStrongEquation
- Euler.TransverseStrongEstimates
- Euler.TransverseVariationalInverse
- Euler.TransverseVariationalOperator
- Euler.TruncatedBackwardFlow
- Euler.TruncationFamily
- Euler.TruncationFamilySmooth
- Euler.UniformHeatLocal
- Euler.UnshiftedPressure
- Euler.UnshiftedProducts
- Euler.ViscosityCauchy
- Euler.ViscosityDefect
- Euler.ViscousCorrectionFamily
- Euler.ViscousPathDerivative
- Euler.ViscousSourcePathLimit
- Euler.VolterraConvolution
- Euler.VolterraFixedPoint
- Euler.VolterraUniqueness
- Euler.VolumeSobolevComposition
- Euler.VolumeSobolevPath
- Euler.VorticityTransport
- Euler.WeakHilbertODE
- Euler.WeakTimeContinuity
- Euler.WeightedCylinderEnergy
- Euler.WeightedForcingAlgebra
- Euler.WeightedForcingTime
- Euler.WeightedRootLimit
- Euler.WeightedSobolevEnergy
- Euler.WeightedSobolevMajorant
- Euler.WholeSpaceGaussian
- Euler.WholeSpaceGaussianElliptic
- Euler.WholeSpaceGaussianEvolution
- Euler.WholeSpaceGaussianFields
- Euler.WholeSpaceGaussianHigh
- Euler.WholeSpaceGaussianIntegration
- Euler.WholeSpaceGaussianKernel
- Euler.WholeSpaceGaussianLow
- Euler.WholeSpaceGaussianScale
- Euler.WholeSpaceGaussianTimeKernel
- Euler.WholeSpaceLogarithmic
- Euler.WindowSource
- NavierStokes
- NavierStokes.ActualBasePressureBounds
- NavierStokes.ActualCorrectionModels
- NavierStokes.ActualParticularDynamicsNoOptions
- NavierStokes.ActualParticularPhysicalData
- NavierStokes.AppendixHeatResults
- NavierStokes.AppendixJoiningResults
- NavierStokes.AxisAnalyticCoefficients
- NavierStokes.AxisAnalyticRadialSeries
- NavierStokes.AxisInverseFactors
- NavierStokes.AxisJointAnalytic
- NavierStokes.AxisModelBounds
- NavierStokes.AxisRootPressureBounds
- NavierStokes.BaseAngularGrowth
- NavierStokes.BaseWitnessClosure
- NavierStokes.BoundaryCoordinates
- NavierStokes.CandidateAssembly
- NavierStokes.ClosedIntervalCk
- NavierStokes.ClosedIntervalCkOperators
- NavierStokes.ClosedIntervalJetAlgebra
- NavierStokes.ClosedIntervalMomentRepair
- NavierStokes.CommonCoverWithin
- NavierStokes.CompactHolomorphicFamily
- NavierStokes.ComparatorR3Bridge
- NavierStokes.ComparatorR3Theorem
- NavierStokes.ComparatorSolution
- NavierStokes.ComparatorTheorem
- NavierStokes.CorrectionInitializationNoOptions
- NavierStokes.CurrentPhysicalRadialClosure
- NavierStokes.CycleContinuationInvariant
- NavierStokes.DiagonalJetBoundsNoOptions
- NavierStokes.EndpointLimits
- NavierStokes.ExponentialMomentMatrix
- NavierStokes.FlatPrimitivePaper
- NavierStokes.GenericAngularRecovery
- NavierStokes.GenericDiagonalSchedule
- NavierStokes.GenericDifferentialPolynomial
- NavierStokes.GenericFactorSupport
- NavierStokes.GenericJetRateAlgebra
- NavierStokes.GenericRealization
- NavierStokes.GenericRealizationBounds
- NavierStokes.GenericSolenoidalRealization
- NavierStokes.GenericSummationRealization
- NavierStokes.GenericSupportLocalCoefficients
- NavierStokes.GenericSupportLocalSummation
- NavierStokes.GenericSupportedPolynomial
- NavierStokes.GenericTupleRealization
- NavierStokes.GenericTupleSupport
- NavierStokes.GenericVelocityRates
- NavierStokes.GraphRestriction
- NavierStokes.HolomorphicFamilyAnalytic
- NavierStokes.InitialDyadicSource
- NavierStokes.InitialHarmonicContinuation
- NavierStokes.LabelCounting
- NavierStokes.LabelCountingFinite
- NavierStokes.LocalAngularGrowth
- NavierStokes.LocalAngularScalar
- NavierStokes.LocalHeatExterior
- NavierStokes.LocalHeatFormula
- NavierStokes.LocalHeatPressure
- NavierStokes.LocalJetBounds
- NavierStokes.LocalPaperDomain
- NavierStokes.LocalPaperHeat
- NavierStokes.LocalPaperTheorem
- NavierStokes.LocalPotentialRebundle
- NavierStokes.LocalResidualFlatness
- NavierStokes.LocalScaleApproach
- NavierStokes.LocalScaleGeometry
- NavierStokes.LocalScheduleAngular
- NavierStokes.LocalScheduleWitness
- NavierStokes.MeanLocalCoefficient
- NavierStokes.MeanLocalDefectBounds
- NavierStokes.MeanStageContinuation
- NavierStokes.ModulatedProfileJetRates
- NavierStokes.MomentRepairPicard
- NavierStokes.MomentRepairPicardConvergence
- NavierStokes.NativeDyadicRegularity
- NavierStokes.NaturalAxisJointAnalytic
- NavierStokes.NaturalExitBounds
- NavierStokes.NaturalExitParameterJets
- NavierStokes.OutgoingNegativeSlopeCone
- NavierStokes.PaperAdditionalResults
- NavierStokes.PaperLocalization
- NavierStokes.PaperResults
- NavierStokes.ParameterizedMomentRepair
- NavierStokes.ParticularOneSided
- NavierStokes.ParticularWithinBounds
- NavierStokes.ParticularWithinPressure
- NavierStokes.PeriodicComparatorSolution
- NavierStokes.PeriodicPaperComparator
- NavierStokes.PeriodicPaperScalingSupport
- NavierStokes.PeriodicPaperSupport
- NavierStokes.PeriodicPaperTheorem
- NavierStokes.PeriodicViscosity
- NavierStokes.PeriodicViscosityUniqueness
- NavierStokes.PeriodizeLatticeCover
- NavierStokes.PeriodizePDE
- NavierStokes.PositiveAxisDifferential
- NavierStokes.QuadraticLinearization
- NavierStokes.R3
- NavierStokes.R3.ComparatorBridge
- NavierStokes.R3.DelayedExtension
- NavierStokes.R3.H3Approximation
- NavierStokes.R3.H3Blowup
- NavierStokes.R3.H3BoxIntegral
- NavierStokes.R3.H3CandidateStrong
- NavierStokes.R3.H3CandidateUniqueness
- NavierStokes.R3.H3CompactCurve
- NavierStokes.R3.H3CompactHelpers
- NavierStokes.R3.H3Comparison
- NavierStokes.R3.H3Continuity
- NavierStokes.R3.H3Curve
- NavierStokes.R3.H3Definitions
- NavierStokes.R3.H3DivCurlFourier
- NavierStokes.R3.H3Embedding
- NavierStokes.R3.H3Energy
- NavierStokes.R3.H3MaximalLifespan
- NavierStokes.R3.H3Operations
- NavierStokes.R3.H3PressureDistribution
- NavierStokes.R3.H3PressureOrthogonality
- NavierStokes.R3.H3Products
- NavierStokes.R3.H3StrongSolution
- NavierStokes.R3.H3Transport
- NavierStokes.R3.H3UniformApproximation
- NavierStokes.R3.H3WeakEmbedding
- NavierStokes.R3.H3WeakStrong
- NavierStokes.R3.L2TimeDerivative
- NavierStokes.R3.ParabolicCalculus
- NavierStokes.R3.ParabolicDefinitions
- NavierStokes.R3.ParabolicEnergy
- NavierStokes.R3.ParabolicScaling
- NavierStokes.R3.ParabolicSupport
- NavierStokes.R3.ViscousUniqueness
- NavierStokes.R3AbsorbedBoundary
- NavierStokes.R3CompactEnergy
- NavierStokes.R3CompactIntegration
- NavierStokes.R3CompactParametricIntegral
- NavierStokes.R3ConvolutionYoung
- NavierStokes.R3CutoffSobolev
- NavierStokes.R3CutoffTestFields
- NavierStokes.R3DifferenceStress
- NavierStokes.R3EnergyAbsorption
- NavierStokes.R3EnergyBoundary
- NavierStokes.R3EnergyNorms
- NavierStokes.R3FiniteEnergyComparison
- NavierStokes.R3GaussianPressure
- NavierStokes.R3HarmonicPressure
- NavierStokes.R3LocalEnergyEvolution
- NavierStokes.R3LocalizedEnergyLimit
- NavierStokes.R3LocalizedPressure
- NavierStokes.R3LocalizedPressureTests
- NavierStokes.R3PhysicalPressureBound
- NavierStokes.R3PositiveTests
- NavierStokes.R3PressureCommutator
- NavierStokes.R3PressureCutoff
- NavierStokes.R3PressureFlux
- NavierStokes.R3PressureFourier
- NavierStokes.R3PressureKernel
- NavierStokes.R3PressureNearKernel
- NavierStokes.R3PressurePairing
- NavierStokes.R3RieszApproximation
- NavierStokes.R3RieszKernel
- NavierStokes.R3SmoothPressure
- NavierStokes.R3SpaceTime
- NavierStokes.R3SpaceTimeApproximation
- NavierStokes.R3SpaceTimeCalculus
- NavierStokes.R3SpaceTimeHarmonic
- NavierStokes.R3SpaceTimePressure
- NavierStokes.R3SpatialConvolution
- NavierStokes.R3StressPressureEstimate
- NavierStokes.R3TimeLocalization
- NavierStokes.R3UniformBounds
- NavierStokes.R3WeakPressure
- NavierStokes.R3WeightedLp
- NavierStokes.RadialPrimitive
- NavierStokes.ReferenceEndpointRate
- NavierStokes.ReferenceUniformJets
- NavierStokes.ReferenceUniformStocks
- NavierStokes.RegularSingularIntegral
- NavierStokes.SchwartzCompactApproximation
- NavierStokes.SeedConePaper
- NavierStokes.SeedHandbackJets
- NavierStokes.SharpActualStageBounds
- NavierStokes.SharpCommonGraphJets
- NavierStokes.SharpCurrentModeJets
- NavierStokes.SharpCurrentParticularBounds
- NavierStokes.SharpCurrentPhysicalPhase
- NavierStokes.SharpGeometricModeJets
- NavierStokes.SharpGluedStageBounds
- NavierStokes.SharpGraphBounds
- NavierStokes.SharpLogWeights
- NavierStokes.SharpMeanJetBounds
- NavierStokes.SharpMeanStageBounds
- NavierStokes.SharpParticularGluing
- NavierStokes.SharpParticularStageBounds
- NavierStokes.SharpPhaseJetAlgebra
- NavierStokes.SharpPhysicalCarrier
- NavierStokes.SharpPhysicalCopyBounds
- NavierStokes.SharpPhysicalLogBounds
- NavierStokes.SharpPhysicalLoss
- NavierStokes.SharpPhysicalPhase
- NavierStokes.SharpWaveStageBounds
- NavierStokes.SignedRequestContinuation
- NavierStokes.SmoothExponentialMomentMatrix
- NavierStokes.SmoothPowerMomentMatrix
- NavierStokes.SmoothQuadraticBranch
- NavierStokes.SupportedActualContext
- NavierStokes.SupportedParameterExtension
- NavierStokes.TerminalEdgePaper
- NavierStokes.TorusCoverDegree
- NavierStokes.TorusCoverLattice
- NavierStokes.TrueConeLoopPaper
- NavierStokes.UniformQuadraticBranch
- NavierStokes.WaveDataReindex
- NavierStokes.WaveStageContinuation
- NavierStokes.WholeDomainActualStageBounds
- NavierStokes.WholeDomainBaseBounds
- NavierStokes.WholeDomainCompactBounds
- NavierStokes.WholeDomainHeatBounds
- NavierStokes.WholeDomainHeatCompact
- NavierStokes.WholeDomainHeatGeometry
- NavierStokes.WholeDomainHeatScaling
- NavierStokes.WholeDomainInitializationBounds
- NavierStokes.WholeDomainPhysicalCompact
- NavierStokes.WholeDomainPhysicalStageTheorem
- NavierStokes.WholeDomainPrefixBounds
- NavierStokes.WholeDomainStageBounds
- NavierStokes.WithinJointODE
- NavierStokes.WithinPathFamily
- NavierStokesReview.src.audit.agent_check_axioms
- NavierStokesReview.src.audit.lean32-preflight.Main
- NavierStokesReview.src.external-semantic.Adapter
- NavierStokesReview.src.external-semantic.ClaySpec
- NavierStokesReview.src.external-semantic.Gap
- NavierStokesReview.src.probes.ActivePairEmptyBranchProbe
- NavierStokesReview.src.probes.ActualCandidateAssemblyIsolationProbe
- NavierStokesReview.src.probes.AnalyticObjectionsProbe
- NavierStokesReview.src.probes.AxiomProbe
- NavierStokesReview.src.probes.CMIForceBridgeProbe
- NavierStokesReview.src.probes.CMIQuantifierProbe
- NavierStokesReview.src.probes.DerivedFilterAudit
- NavierStokesReview.src.probes.EulerAxiomProbe
- NavierStokesReview.src.probes.FilterNonVacuityAudit
- NavierStokesReview.src.probes.FiveRowPositiveOrderBridgeProbe
- NavierStokesReview.src.probes.FiveRowsStructureProbe
- NavierStokesReview.src.probes.ForceActivityProbe
- NavierStokesReview.src.probes.HeadlineAxiomProbe
- NavierStokesReview.src.probes.IntermediateAxiomProbe
- NavierStokesReview.src.probes.JetRateVacuityProbe
- NavierStokesReview.src.probes.MainAxiomProbe
- NavierStokesReview.src.probes.ManifoldDimensionalReductionProbe
- NavierStokesReview.src.probes.MomentBridgeObstructionProbe
- NavierStokesReview.src.probes.MomentCoordinateMismatchProbe
- NavierStokesReview.src.probes.MomentInitializationProbe
- NavierStokesReview.src.probes.MovingFieldRowNonImplicationProbe
- NavierStokesReview.src.probes.OpenPastNeBotProbe
- NavierStokesReview.src.probes.OriginPastNeBotProbe
- NavierStokesReview.src.probes.PreExportAxiomProbe
- NavierStokesReview.src.probes.R3ComparisonPremiseProbe
- NavierStokesReview.src.probes.SelectedBudgetProbe
- NavierStokesReview.src.probes.SelectedDependencyAxiomProbe
- NavierStokesReview.src.probes.SelectedDivergenceAudit
- NavierStokesReview.src.probes.SelectedImportClosureProbe
- NavierStokesReview.src.probes.SelectedMomentBridgeAudit
- NavierStokesReview.src.probes.agent_moment_bridge
- NavierStokesReview.src.probes.agent_reachability