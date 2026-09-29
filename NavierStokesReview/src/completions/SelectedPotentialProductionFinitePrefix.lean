import completions.SelectedPotentialProductionBarMomentSection
import completions.SelectedPotentialStagewiseCurlOnPhysicalDomain
import NavierStokes.ActualMeanStageData

/-!
# Selected potential production: finite prefix

This file fixes the finite object that must be integrated before any passage
to the selected `tsum`.  It expands the localised partial potential through
the Cartesian curl and retains the derivative-of-cutoff commutator.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialProductionFinitePrefix

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ActualMeanPotentialRealization
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokes.PhysicalResidualTZ
open NavierStokes.ProblemStatement
open NavierStokesReview.SelectedPotentialProductionBarMomentSection
open scoped BigOperators ContDiff Topology

noncomputable def selectedPotentialPartial (a : ℕ → ℕ) (N : ℕ) : VelocityField :=
  SolenoidalDiagonal.partialPotential
    (fun j => (a j : ℝ))
    (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
    selectedPotentialStages N

theorem selected_potential_partial_curl_eq_stage_sum
    (a : ℕ → ℕ) (N : ℕ) (z : SpaceTime)
    (hq : ContDiffAt ℝ ∞
      (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h) z)
    (hA : ∀ j, ContDiffAt ℝ ∞ (selectedPotentialStages j) z) :
    SpatialCurl.spatialCurl (selectedPotentialPartial a N) z =
      ∑ j ∈ Finset.range N,
        SpatialCurl.spatialCurl
          (SolenoidalDiagonal.cutStage
            (fun j => (a j : ℝ))
            (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
            selectedPotentialStages j) z := by
  exact SolenoidalDiagonal.spatialCurl_partialPotential hq hA N

theorem selected_potential_partial_cut_product_rule
    (a : ℕ → ℕ) (N : ℕ) (t : ℝ) {x : Space}
    (hA : DifferentiableAt ℝ
      (fun y : Space => selectedPotentialPartial a N (t, y)) x) :
    SpatialLocalization.cutVelocity (selectedPotentialPartial a N) (t, x) =
      SpatialLocalization.spatialCutoff x •
          SpatialCurl.spatialCurl (selectedPotentialPartial a N) (t, x) +
        SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff x).smulRight
            (selectedPotentialPartial a N (t, x))) := by
  exact SpatialLocalization.cutVelocity_product_rule
    (selectedPotentialPartial a N) t x hA

theorem selected_potential_partial_production_expansion
    (a : ℕ → ℕ) (N : ℕ) (t : ℝ) {x : Space}
    (hq : ContDiffAt ℝ ∞
      (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
      (t, x))
    (hA : ∀ j, ContDiffAt ℝ ∞ (selectedPotentialStages j) (t, x))
    (hpartial : DifferentiableAt ℝ
      (fun y : Space => selectedPotentialPartial a N (t, y)) x) :
    SpatialLocalization.cutVelocity (selectedPotentialPartial a N) (t, x) =
      SpatialLocalization.spatialCutoff x •
          (∑ j ∈ Finset.range N,
            SpatialCurl.spatialCurl
              (SolenoidalDiagonal.cutStage
                (fun j => (a j : ℝ))
                (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
                selectedPotentialStages j) (t, x)) +
        SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff x).smulRight
            (selectedPotentialPartial a N (t, x))) := by
  rw [selected_potential_partial_cut_product_rule a N t hpartial]
  rw [selected_potential_partial_curl_eq_stage_sum a N (t, x) hq hA]

noncomputable def selectedPotentialPartialProductionScalar
    (a : ℕ → ℕ) (N : ℕ) (p : DirectAngularDiagonal.CylPoint) : ℝ :=
  (SpatialLocalization.periodicVelocity (selectedPotentialPartial a N)
    (ActualMeanStageData.radialSection p)) 1

noncomputable def selectedPotentialPartialProductionPointScalar
    (a : ℕ → ℕ) (N : ℕ) :
    DefectIncrementBounds.ScalarField MomentPoint :=
  fun _ q => selectedPotentialPartialProductionScalar a N (pointToCyl q)

theorem selected_potential_partial_production_point_barMoment_apply
    (a : ℕ → ℕ) (N k n : ℕ) (p : PhysicalResidualBridge.Plane) :
    DefectIncrementBounds.barMoment k
        (selectedPotentialPartialProductionPointScalar a N) n p =
      ∫ r, r ^ k * PressureStream.torusAverage
        ((selectedPotentialPartialProductionPointScalar a N) n) (r, p) := by
  exact DefectIncrementBounds.barMoment_apply k
    (selectedPotentialPartialProductionPointScalar a N) n p

theorem selected_potential_partial_production_point_scalar_physical_pullback
    (h : ℝ) (a : ℕ → ℕ) (N : ℕ)
    {p : DirectAngularDiagonal.CylPoint} (hp : 0 < p.2.1) :
    selectedPotentialPartialProductionPointScalar a N 0
        (PhysicalMeanJetBounds.physicalPoint h
          (ActualMeanStageData.radialSection p)) =
      selectedPotentialPartialProductionScalar a N p := by
  rw [show selectedPotentialPartialProductionPointScalar a N 0
        (PhysicalMeanJetBounds.physicalPoint h
          (ActualMeanStageData.radialSection p)) =
      selectedPotentialPartialProductionScalar a N
        (pointToCyl (PhysicalMeanJetBounds.physicalPoint h
          (ActualMeanStageData.radialSection p))) by rfl]
  rw [pointToCyl_physicalPoint_radialSection h hp]

theorem selected_potential_partial_production_radial_scalar_eq
    (a : ℕ → ℕ) (N : ℕ) (p : DirectAngularDiagonal.CylPoint)
    (hcoord : ∀ i : Fin 3,
      |(ActualMeanStageData.radialSection p).2 i| ≤ 1 / 2)
    (hpartial : DifferentiableAt ℝ
      (fun y : Space => selectedPotentialPartial a N
        ((ActualMeanStageData.radialSection p).1, y))
      (ActualMeanStageData.radialSection p).2) :
    selectedPotentialPartialProductionScalar a N p =
      SpatialLocalization.spatialCutoff
          (ActualMeanStageData.radialSection p).2 *
          (SpatialCurl.spatialCurl (selectedPotentialPartial a N)
            (ActualMeanStageData.radialSection p)) 1 +
        (SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff
            (ActualMeanStageData.radialSection p).2).smulRight
            (selectedPotentialPartial a N
              (ActualMeanStageData.radialSection p)))) 1 := by
  have hi : (ActualMeanStageData.radialSection p).2 ∈
      PeriodicLocalization.innerCube (1 / 4) := by
    intro i
    have hxi := hcoord i
    linarith
  calc
    selectedPotentialPartialProductionScalar a N p =
        (SpatialLocalization.cutVelocity (selectedPotentialPartial a N)
          (ActualMeanStageData.radialSection p)) 1 :=
      congrArg (fun v : Space => v 1)
        (SpatialLocalization.periodicVelocity_eventuallyEq_cut
          (selectedPotentialPartial a N)
          (z := ActualMeanStageData.radialSection p) hi).self_of_nhds
    _ = SpatialLocalization.spatialCutoff
          (ActualMeanStageData.radialSection p).2 *
          (SpatialCurl.spatialCurl (selectedPotentialPartial a N)
            (ActualMeanStageData.radialSection p)) 1 +
        (SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff
            (ActualMeanStageData.radialSection p).2).smulRight
            (selectedPotentialPartial a N
              (ActualMeanStageData.radialSection p)))) 1 := by
      rw [selected_potential_partial_cut_product_rule a N
        (ActualMeanStageData.radialSection p).1 hpartial]
      rfl

end NavierStokesReview.SelectedPotentialProductionFinitePrefix
