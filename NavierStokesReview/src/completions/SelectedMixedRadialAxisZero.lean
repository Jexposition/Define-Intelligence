import completions.SelectedMixedRadialSupportObstruction
import NavierStokes.LocalScheduleWitness

/-!
# Selected mixed radial pullback: asymptotic axis component

The selected origin blow-up is an axial norm blow-up.  The radial `barMoment`
pullback used by the review samples the first Cartesian component on the
section `radialSection`.  This completion transports the selected schedule to
the source axis representation and records the resulting asymptotic fact:
along the axis curve represented by `r = 0` and `p = (1 - t, 0)`, that sampled
component is eventually zero as `t` approaches one from below.

This is not a contradiction and it does not prove that the pullback is zero
off the axis.  It closes a specific invalid inference: the norm blow-up at the
origin cannot by itself supply the nonzero first-component premise required by
the periodic-support gate.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedRadialAxisZero

open NavierStokes
open NavierStokes.CorrectionInitialization.ActualPrimary
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedMixedRadialSupportObstruction
open NavierStokesReview.SelectedPotentialProductionBarMomentSection
open scoped Topology ContDiff BigOperators

theorem selected_mixed_radial_pullback_axis_zero_eventually :
    ∃ a : ℕ → ℕ,
      LocalScheduleWitness.Selected a ∧
        ∀ᶠ t in (𝓝[<] (1 : ℝ)),
          selectedMixedRadialPullback a (0, ((1 - t, 0) : PhysicalResidualBridge.Plane)) = 0 := by
  obtain ⟨a, ha, _, _, _, _, _, _, _⟩ := ActualCandidateAssembly.selected_witness
  have ha_selected := ha
  obtain ⟨_, _, _, _, hscale, _, _, _⟩ := ha
  have hbase := GermCandidateAssembly.origin_eventually_base
    certificate modulation upper ActualCandidateConstruction.selectedBudget
    (ActualCandidateConstruction.qbig_pos ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold)
    (ActualCandidateAssembly.initialPotential ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold)
    (ActualCandidateAssembly.positivePotential ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry)
    (ActualCandidateAssembly.directData ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry)
    (ActualCandidateAssembly.initialPotential_axisZeroOn
      ActualCandidateConstruction.selectedBudget ActualCandidateConstruction.selectedThreshold)
    (ActualCandidateAssembly.positivePotential_axisZeroOn
      ActualCandidateConstruction.selectedBudget ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry)
    hscale
  refine ⟨a, ha_selected, ?_⟩
  filter_upwards [hbase, self_mem_nhdsWithin] with t ht hbefore
  have hcomponent := congrArg (fun v : ProblemStatement.Space => v 1) ht
  have hselected :
      MixedPeriodicAssembly.periodicVelocity
          (SelectedPotentialProductionProductRule.selectedPotentialSum a)
          (SelectedMixedProductionRadialComponent.selectedDirectSum a)
          (t, 0) 1 = 0 := by
    rw [MixedPeriodicAssembly.periodicVelocity_origin]
    simpa [SelectedPotentialProductionProductRule.selectedPotentialSum,
      SelectedMixedProductionRadialComponent.selectedDirectSum,
      ActualCandidateAssembly.selectedPotentialStages,
      ActualCandidateAssembly.selectedDirectStages,
      ActualCandidateAssembly.potentialStages,
      ActualCandidateAssembly.directStages,
      GermCandidateAssembly.potentialStages,
      GermCandidateAssembly.initializedSeries,
      CorrectionInitialization.ActualPrimary.h,
      CorrectionInitialization.ActualPrimary.profile,
      ActualCandidateAssembly.initialPotential,
      ActualCandidateAssembly.positivePotential,
      ActualCandidateAssembly.directStages,
      ActualCandidateAssembly.directData,
      FinalSlowBase.origin certificate modulation upper
        ActualCandidateConstruction.selectedBudget hbefore,
      ProblemStatement.coordinateVector] using hcomponent
  simpa [selectedMixedRadialPullback, selectedMixedProductionScalar,
    AxisymmetricResidual.pack,
    SelectedPotentialProductionBarMomentSection.pointToCyl,
    ActualMeanStageData.radialSection,
    SelectedPotentialProductionProductRule.selectedPotentialSum,
    SelectedMixedProductionRadialComponent.selectedDirectSum,
    ActualCandidateAssembly.selectedPotentialStages,
    ActualCandidateAssembly.selectedDirectStages,
    ActualCandidateAssembly.potentialStages,
    ActualCandidateAssembly.directStages,
    GermCandidateAssembly.potentialStages,
    GermCandidateAssembly.initializedSeries,
    CorrectionInitialization.ActualPrimary.h,
    CorrectionInitialization.ActualPrimary.profile] using hselected

end NavierStokesReview.SelectedMixedRadialAxisZero
