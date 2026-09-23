import NavierStokes.MixedCandidateAssembly

/-!
# Stage-estimate interface countermodel

This probe is deliberately narrow.  It does not attack the selected witness,
which has additional base and angular hypotheses.  It shows that the generic
`StageEstimates` interface by itself can be inhabited by identically zero
velocity and pressure stages.  Therefore that interface cannot, on its own,
encode the paper's nonzero five-moment repair system or the blow-up mechanism.
-/

noncomputable section

namespace NavierStokesReview.StageEstimatesMomentBlindnessProbe

open Set Filter NavierStokes NavierStokes.ProblemStatement
open NavierStokes.MixedCandidateAssembly
open scoped Topology ContDiff

def zeroVelocityStages : ℕ → VelocityField := fun _ _ => 0

def zeroPressureStages : ℕ → PressureField := fun _ _ => 0

def zeroGain : ℕ → ℝ := fun j => (j : ℝ)

def zeroLoss : ℕ → ℝ := fun _ => 0

def zeroConstant : ℕ → ℕ → ℝ := fun _ _ => 0

def zeroLog : ℕ → ℕ → ℝ := fun _ _ => 0

theorem zero_stage_estimates :
    Nonempty (StageEstimates (1 / 4 : ℝ) 1 zeroVelocityStages zeroVelocityStages
      zeroPressureStages) := by
  refine ⟨{
    potential_smooth := ?_
    direct_smooth := ?_
    pressure_smooth := ?_
    gain := zeroGain
    gain_zero := ?_
    gain_pos := ?_
    gain_mono := ?_
    gain_top := ?_
    potentialLoss := zeroLoss
    directLoss := zeroLoss
    pressureLoss := zeroLoss
    potentialConstant := zeroConstant
    directConstant := zeroConstant
    pressureConstant := zeroConstant
    potentialLog := zeroLog
    directLog := zeroLog
    pressureLog := zeroLog
    potential_bound := ?_
    direct_bound := ?_
    pressure_bound := ?_
    backgroundLoss := zeroLoss
    residualLoss := zeroLoss
    finite_background := ?_
    finite_residual := ?_ }⟩
  · intro j
    exact contDiffOn_const
  · intro j
    exact contDiffOn_const
  · intro j
    exact contDiffOn_const
  · norm_num [zeroGain]
  · intro j hj
    change 0 < (j : ℝ)
    exact_mod_cast (show 0 < j by omega)
  · intro i j hij
    change (i : ℝ) ≤ (j : ℝ)
    exact_mod_cast hij
  · change Tendsto (fun j : ℕ => (j : ℝ)) atTop atTop
    exact
      (tendsto_natCast_atTop_atTop : Tendsto (fun j : ℕ => (j : ℝ)) atTop atTop)
  · intro j hj m x hx hq
    have hz : iteratedFDeriv ℝ m (zeroVelocityStages j) x = 0 := by
      change iteratedFDeriv ℝ m (fun _ : SpaceTime => (0 : Space)) x = 0
      simp only [iteratedFDeriv_fun_zero, Pi.zero_apply]
    rw [hz]
    simp [zeroConstant, zeroLog, zeroLoss]
  · intro j hj m x hx hq
    have hz : iteratedFDeriv ℝ m (zeroVelocityStages j) x = 0 := by
      change iteratedFDeriv ℝ m (fun _ : SpaceTime => (0 : Space)) x = 0
      simp only [iteratedFDeriv_fun_zero, Pi.zero_apply]
    rw [hz]
    simp [zeroConstant, zeroLog, zeroLoss]
  · intro j hj m x hx hq
    have hz : iteratedFDeriv ℝ m (zeroPressureStages j) x = 0 := by
      change iteratedFDeriv ℝ m (fun _ : SpaceTime => (0 : ℝ)) x = 0
      simp only [iteratedFDeriv_fun_zero, Pi.zero_apply]
    rw [hz]
    simp [zeroConstant, zeroLog, zeroLoss]
  · intro J m
    have hpref : DiagonalJetBounds.uncutPrefix zeroVelocityStages (J + 1) =
        (fun _ : SpaceTime => (0 : Space)) := by
      funext z
      simp [DiagonalJetBounds.uncutPrefix, zeroVelocityStages]
    have hu : MixedDiagonalResidual.uncutVelocity zeroVelocityStages zeroVelocityStages J =
        (fun _ : SpaceTime => (0 : Space)) := by
      funext z
      change SpatialCurl.spatialCurl
          (DiagonalJetBounds.uncutPrefix zeroVelocityStages (J + 1)) z +
        DiagonalJetBounds.uncutPrefix zeroVelocityStages (J + 1) z = 0
      rw [hpref]
      simp [MixedDiagonalResidual.uncutVelocity, SpatialCurl.spatialCurl,
        SpatialCurl.curl, SpatialCurl.curlLinear]
    refine ⟨0, le_rfl, ?_⟩
    filter_upwards [] with z
    rw [hu]
    simp [zeroLoss]
  · intro J m
    have hpref : DiagonalJetBounds.uncutPrefix zeroVelocityStages (J + 1) =
        (fun _ : SpaceTime => (0 : Space)) := by
      funext z
      simp [DiagonalJetBounds.uncutPrefix, zeroVelocityStages]
    have hu : MixedDiagonalResidual.uncutVelocity zeroVelocityStages zeroVelocityStages J =
        (fun _ : SpaceTime => (0 : Space)) := by
      funext z
      change SpatialCurl.spatialCurl
          (DiagonalJetBounds.uncutPrefix zeroVelocityStages (J + 1)) z +
        DiagonalJetBounds.uncutPrefix zeroVelocityStages (J + 1) z = 0
      rw [hpref]
      simp [MixedDiagonalResidual.uncutVelocity, SpatialCurl.spatialCurl,
        SpatialCurl.curl, SpatialCurl.curlLinear]
    have hp : DiagonalJetBounds.uncutPrefix zeroPressureStages (J + 1) =
        (fun _ : SpaceTime => (0 : ℝ)) := by
      funext z
      simp [DiagonalJetBounds.uncutPrefix, zeroPressureStages]
    refine ⟨0, le_rfl, ?_⟩
    filter_upwards [] with z
    have hres : (fun z => navierStokesResidual
        (MixedDiagonalResidual.uncutVelocity zeroVelocityStages zeroVelocityStages J)
        (DiagonalJetBounds.uncutPrefix zeroPressureStages (J + 1)) z.1 z.2) =
        (fun _ : SpaceTime => (0 : Space)) := by
      funext y
      rw [hu, hp]
      simp [NavierStokes.ProblemStatement.navierStokesResidual,
        NavierStokes.ProblemStatement.temporalDerivative,
        NavierStokes.ProblemStatement.advection,
        NavierStokes.ProblemStatement.spatialLaplacian,
        NavierStokes.ProblemStatement.spatialDerivative,
        NavierStokes.ProblemStatement.pressureGradient]
    rw [hres]
    simp [zeroGain, zeroLoss]

theorem interface_does_not_encode_blowup :
    ¬ SpeedUnboundedAtOne (fun _ => 0) := by
  intro h
  obtain ⟨t, x, ht, hnear, hlarge⟩ := h 1 zero_lt_one 1 zero_lt_one
  have : (1 : ℝ) < 0 := by simpa using hlarge
  linarith

end NavierStokesReview.StageEstimatesMomentBlindnessProbe
