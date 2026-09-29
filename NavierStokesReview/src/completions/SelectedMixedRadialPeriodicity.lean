import completions.SelectedMixedProductionTorusAverage

/-!
# Selected mixed production: radial periodicity

The selected mixed field is assembled from a unit-periodic Cartesian velocity,
but the radial observable integrates over an unbounded real variable.  This
file records the exact periodicity after the cylindrical radial-section
pullback.  It does not infer non-integrability or a contradiction without a
nonzero-value or support theorem.
-/

noncomputable section

namespace NavierStokesReview.SelectedMixedRadialPeriodicity

open NavierStokes
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ActualMeanStageData
open NavierStokes.DirectAngularDiagonal
open NavierStokes.PhysicalResidualBridge
open NavierStokes.ProblemStatement
open NavierStokesReview.SelectedMixedProductionRadialComponent
open NavierStokesReview.SelectedPotentialProductionRadialScalar
open NavierStokesReview.SelectedPotentialProductionProductRule
open scoped BigOperators

theorem selected_mixed_production_scalar_periodic_radius
    (a : ℕ → ℕ) (p : DirectAngularDiagonal.CylPoint) :
    selectedMixedProductionScalar a (p.1, (p.2.1 + 1, p.2.2)) =
      selectedMixedProductionScalar a p := by
  unfold selectedMixedProductionScalar
  have hp := MixedPeriodicAssembly.periodicVelocity_periodic
    (selectedPotentialSum a) (selectedDirectSum a) Set.univ
  have h := hp p.1 (by simp)
    (ActualMeanStageData.radialSection p).2 0
  have hx : (ActualMeanStageData.radialSection
      (p.1, (p.2.1 + 1, p.2.2))).2 =
      (ActualMeanStageData.radialSection p).2 + coordinateVector 0 := by
    ext i
    fin_cases i <;>
      simp [ActualMeanStageData.radialSection, AxisymmetricResidual.pack,
        coordinateVector]
  calc
    (MixedPeriodicAssembly.periodicVelocity
      (selectedPotentialSum a) (selectedDirectSum a)
      (ActualMeanStageData.radialSection
        (p.1, (p.2.1 + 1, p.2.2)))) 1 =
      (MixedPeriodicAssembly.periodicVelocity
        (selectedPotentialSum a) (selectedDirectSum a)
        (p.1, (ActualMeanStageData.radialSection
          (p.1, (p.2.1 + 1, p.2.2))).2)) 1 := by rfl
    _ = (MixedPeriodicAssembly.periodicVelocity
        (selectedPotentialSum a) (selectedDirectSum a)
        (p.1, (ActualMeanStageData.radialSection p).2 + coordinateVector 0)) 1 := by
      rw [hx]
    _ = (MixedPeriodicAssembly.periodicVelocity
        (selectedPotentialSum a) (selectedDirectSum a)
        (p.1, (ActualMeanStageData.radialSection p).2)) 1 :=
      congrArg (fun v : Space => v 1) h

theorem selected_mixed_barMoment_integrand_periodic
    (a : ℕ → ℕ) (p : PhysicalResidualBridge.Plane) (r : ℝ) :
    selectedMixedProductionScalar a
        (NavierStokesReview.SelectedPotentialProductionBarMomentSection.pointToCyl
          (r + 1, (p, (0, 0)))) =
      selectedMixedProductionScalar a
        (NavierStokesReview.SelectedPotentialProductionBarMomentSection.pointToCyl
          (r, (p, (0, 0)))) := by
  simpa [NavierStokesReview.SelectedPotentialProductionBarMomentSection.pointToCyl]
    using selected_mixed_production_scalar_periodic_radius a
      (NavierStokesReview.SelectedPotentialProductionBarMomentSection.pointToCyl
        (r, (p, (0, 0))))

end NavierStokesReview.SelectedMixedRadialPeriodicity
