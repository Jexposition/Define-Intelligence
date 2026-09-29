import completions.SelectedPotentialProductionProductRule
import completions.SelectedFieldFinitePrefix
import NavierStokes.ActualMeanStageData

/-!
# Selected potential production radial scalar

This file transports the selected localised potential production field to the
positive-radial section used by the source construction.  It exposes the
first Cartesian component after the cutoff/curl product rule.  The result is
deliberately conditional on the source differentiability and unit-cube
hypotheses; it does not invent a global inverse for the `barMoment` domain or
assign a sign to the shell term.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialProductionRadialScalar

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ProblemStatement
open NavierStokesReview.SelectedPotentialProductionProductRule
open Filter
open scoped Topology ContDiff

noncomputable def selectedPotentialProductionScalar (a : ℕ → ℕ)
    (p : DirectAngularDiagonal.CylPoint) : ℝ :=
  (SpatialLocalization.periodicVelocity (selectedPotentialSum a)
    (ActualMeanStageData.radialSection p)) 1

theorem selected_potential_sum_spatial_differentiableAt
    (a : ℕ → ℕ)
    (ha : Tendsto (fun j => (a j : ℝ)) atTop atTop)
    (p : DirectAngularDiagonal.CylPoint)
    (hp : ActualMeanStageData.radialSection p ∈
      ActualCandidateConstruction.physicalDomain
        ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold) :
    DifferentiableAt ℝ
      (fun y : Space => selectedPotentialSum a
        ((ActualMeanStageData.radialSection p).1, y))
      (ActualMeanStageData.radialSection p).2 := by
  let U := ActualCandidateConstruction.physicalDomain
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
  have hU : IsOpen U := ActualCandidateConstruction.physicalDomain_open
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
  have hqpos : ∀ z ∈ U,
      0 < PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h z := by
    intro z hz
    exact PhysicalWaveSum.physicalQ_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hz.1
  have hq : ContDiffOn ℝ ∞
      (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h) U := by
    intro z hz
    exact (PhysicalWaveSum.physicalQ_smoothAt
      CorrectionInitialization.ActualPrimary.outgoing.data.h_pos
      CorrectionInitialization.ActualPrimary.outgoing.data.h_lt_half hz.1).contDiffWithinAt
  have hstages := ActualCandidateAssembly.stages_smooth
    ActualCandidateConstruction.selectedBudget
    ActualCandidateConstruction.selectedThreshold
    ActualCandidateConstruction.selectedThreshold_geometry
  have hsum : ContDiffOn ℝ ∞ (selectedPotentialSum a) U := by
    exact SolenoidalDiagonal.potentialSum_contDiffOn ha hU hqpos hq hstages.1
  have hz : ContDiffAt ℝ ∞ (selectedPotentialSum a)
      (ActualMeanStageData.radialSection p) := by
    apply hsum.contDiffAt
    exact hU.mem_nhds hp
  have hslice : ContDiffAt ℝ ∞
      (fun y : Space => selectedPotentialSum a
        ((ActualMeanStageData.radialSection p).1, y))
      (ActualMeanStageData.radialSection p).2 :=
    hz.comp (f := fun y : Space =>
      ((ActualMeanStageData.radialSection p).1, y))
      (ActualMeanStageData.radialSection p).2
      (contDiffAt_const.prodMk contDiffAt_id)
  exact hslice.differentiableAt (by simp)

theorem selected_potential_production_radial_scalar_eq
    (a : ℕ → ℕ) (p : DirectAngularDiagonal.CylPoint)
    (hcoord : ∀ i : Fin 3,
      |(ActualMeanStageData.radialSection p).2 i| ≤ 1 / 2)
    (hA : DifferentiableAt ℝ
      (fun y : Space => selectedPotentialSum a
        ((ActualMeanStageData.radialSection p).1, y))
      (ActualMeanStageData.radialSection p).2) :
    selectedPotentialProductionScalar a p =
      SpatialLocalization.spatialCutoff
          (ActualMeanStageData.radialSection p).2 *
          (SpatialCurl.spatialCurl (selectedPotentialSum a)
            (ActualMeanStageData.radialSection p)) 1 +
        (SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff
            (ActualMeanStageData.radialSection p).2).smulRight
            (selectedPotentialSum a (ActualMeanStageData.radialSection p)))) 1 := by
  have hproduct := selected_potential_periodic_product_rule a
    (ActualMeanStageData.radialSection p).1 hcoord hA
  have hcomponent := congrArg (fun v : Space => v 1) hproduct
  simpa only [selectedPotentialProductionScalar, ActualMeanStageData.radialSection,
    PiLp.add_apply,
    PiLp.smul_apply, smul_eq_mul] using hcomponent

theorem selected_witness_production_radial_scalar_transport :
    ∃ a : ℕ → ℕ,
      MixedCandidateWitness.SelectedSchedule
        CorrectionInitialization.ActualPrimary.h
        (ActualCandidateConstruction.qbig
          ActualCandidateConstruction.selectedBudget
          ActualCandidateConstruction.selectedThreshold)
        selectedPotentialStages selectedDirectStages selectedPressureStages a ∧
      ∀ (p : DirectAngularDiagonal.CylPoint),
        ActualMeanStageData.radialSection p ∈
          ActualCandidateConstruction.physicalDomain
            ActualCandidateConstruction.selectedBudget
            ActualCandidateConstruction.selectedThreshold →
        (∀ i : Fin 3,
          |(ActualMeanStageData.radialSection p).2 i| ≤ 1 / 2) →
        selectedPotentialProductionScalar a p =
          SpatialLocalization.spatialCutoff
              (ActualMeanStageData.radialSection p).2 *
              (SpatialCurl.spatialCurl (selectedPotentialSum a)
                (ActualMeanStageData.radialSection p)) 1 +
            (SpatialCurl.curlLinear
              ((fderiv ℝ SpatialLocalization.spatialCutoff
                (ActualMeanStageData.radialSection p).2).smulRight
                (selectedPotentialSum a (ActualMeanStageData.radialSection p)))) 1 := by
  rcases NavierStokesReview.SelectedFieldFinitePrefix.selected_schedule_exists with
    ⟨a, ha⟩
  refine ⟨a, ha, ?_⟩
  intro p hp hcoord
  exact selected_potential_production_radial_scalar_eq a p hcoord
    (selected_potential_sum_spatial_differentiableAt a
      ha.2.2.2.2.1 p hp)

end NavierStokesReview.SelectedPotentialProductionRadialScalar
