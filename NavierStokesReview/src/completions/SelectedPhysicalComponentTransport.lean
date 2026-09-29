import completions.SelectedDirectPrefixField
import completions.SelectedCylindricalComponentTransport

/-!
# Selected physical component transport

This completion exposes the component formula of the actual polar Cartesian
map used by the selected direct branch.  It keeps the map-level formula
separate from the scalar `barMoment` operator, whose input is a radial profile.
-/

noncomputable section

namespace NavierStokesReview.SelectedPhysicalComponentTransport

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction

theorem polar_velocity_map_component_one
    (a : ℝ) (i : PolarCharts.Index) (v : ProblemStatement.VelocityField)
    (w : ProblemStatement.SpaceTime) :
    (CyclePhysicalPrefixes.polarVelocityMap a i v w) 1 =
      Real.sin (PhysicalCurlCovariance.polarInput a i w).2 *
          (v (PhysicalCurlCovariance.polarCoordinates a i w)) 0 +
        Real.cos (PhysicalCurlCovariance.polarInput a i w).2 *
          (v (PhysicalCurlCovariance.polarCoordinates a i w)) 1 := by
  change (CylindricalResidual.frame (PhysicalCurlCovariance.polarInput a i w).2
    (v (PhysicalCurlCovariance.polarCoordinates a i w))) 1 = _
  rw [CylindricalResidual.frame_apply]
  simp only [AxisymmetricResidual.pack_one]

theorem selected_direct_stage_component_one_on_chart
    (j n : ℕ) {a : ℝ} (ha : 0 < a) (i : PolarCharts.Index)
    (hn : ActualCandidateConstruction.firstBand
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold ≤ n)
    {w : ProblemStatement.SpaceTime}
    (ht : PhysicalWaveSum.preterminal w)
    (hu : (PhysicalMeanJetBounds.graph CorrectionInitialization.ActualPrimary.h n
      ((ActualCandidateConstruction.meanAtlas
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold).gap n) w).2.1 ∈
      CorrectionInitialization.ActualPrimary.standardRegion.carrier)
    (hw : w ∈ ActualMeanPotentialRealization.cartesianDomain a i) :
    (ActualCandidateAssembly.selectedDirectStages j w) 1 =
      Real.cos (PhysicalCurlCovariance.polarInput a i w).2 *
        ((CyclePhysicalPrefixes.velocityMap
          (ActualCandidateConstruction.graph n)
          (fun x => ![0,
            ActualCandidateConstruction.angularNativeStages
              ActualCandidateConstruction.selectedBudget
              ActualCandidateConstruction.selectedThreshold j n x.1, 0]))
          (PhysicalCurlCovariance.polarCoordinates a i w)) 1 := by
  rw [NavierStokesReview.SelectedDirectPrefixField.selected_direct_stage_eq_chart
    j ha i n hn ht hu hw]
  rw [← ActualCandidateConstruction.angularNativeStages_chart
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold a i n j]
  rw [polar_velocity_map_component_one]
  simp only [CyclePhysicalPrefixes.velocityMap, LinearMap.coe_mk, AddHom.coe_mk,
    PhysicalResidualTZ.velocityTZ,
    PhysicalResidualBridge.ScaledGraph.velocity_apply,
    Matrix.cons_val_zero,
    Matrix.cons_val_one, mul_zero, zero_add]

theorem selected_direct_stage_component_one_scaled
    (j n : ℕ) {a : ℝ} (ha : 0 < a) (i : PolarCharts.Index)
    (hn : ActualCandidateConstruction.firstBand
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold ≤ n)
    {w : ProblemStatement.SpaceTime}
    (ht : PhysicalWaveSum.preterminal w)
    (hu : (PhysicalMeanJetBounds.graph CorrectionInitialization.ActualPrimary.h n
      ((ActualCandidateConstruction.meanAtlas
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold).gap n) w).2.1 ∈
      CorrectionInitialization.ActualPrimary.standardRegion.carrier)
    (hw : w ∈ ActualMeanPotentialRealization.cartesianDomain a i) :
    (ActualCandidateAssembly.selectedDirectStages j w) 1 =
      Real.cos (PhysicalCurlCovariance.polarInput a i w).2 *
        (ActualCandidateConstruction.graph n).velocityScale *
          ActualCandidateConstruction.angularNativeStages
            ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold j n
            (PhysicalResidualTZ.swapCylinder
              ((ActualCandidateConstruction.graph n).map
                (PhysicalCurlCovariance.polarCoordinates a i w))).1 := by
  rw [selected_direct_stage_component_one_on_chart j n ha i hn ht hu hw]
  simp only [CyclePhysicalPrefixes.velocityMap, LinearMap.coe_mk, AddHom.coe_mk,
    PhysicalResidualTZ.velocityTZ,
    PhysicalResidualBridge.ScaledGraph.velocity_apply,
    Matrix.cons_val_zero, Matrix.cons_val_one, mul_assoc]

end NavierStokesReview.SelectedPhysicalComponentTransport
