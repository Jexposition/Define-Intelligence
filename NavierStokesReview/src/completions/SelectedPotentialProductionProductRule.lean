import NavierStokes.SpatialLocalization
import NavierStokes.ActualCandidateAssembly

/-!
# Selected potential production product rule

The exported potential branch is spatially localised before it is
periodised.  This file instantiates the repository's product rule at the
selected potential sum.  It records the exact commutator term that must be
transported into any radial-moment calculation; it does not assign that term
a sign or a nonzero value.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialProductionProductRule

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.ProblemStatement

noncomputable def selectedPotentialSum (a : ℕ → ℕ) : VelocityField :=
  SolenoidalDiagonal.potentialSum (fun j => (a j : ℝ))
    (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
    selectedPotentialStages

theorem selected_potential_periodic_product_rule
    (a : ℕ → ℕ) (t : ℝ) {x : Space}
    (hx : ∀ i : Fin 3, |x i| ≤ 1 / 2)
    (hA : DifferentiableAt ℝ
      (fun y : Space => selectedPotentialSum a (t, y)) x) :
    SpatialLocalization.periodicVelocity (selectedPotentialSum a) (t, x) =
      SpatialLocalization.spatialCutoff x •
          SpatialCurl.spatialCurl (selectedPotentialSum a) (t, x) +
        SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff x).smulRight
            (selectedPotentialSum a (t, x))) := by
  have hi : x ∈ PeriodicLocalization.innerCube (1 / 4) := by
    intro i
    have hxi := hx i
    linarith
  calc
    SpatialLocalization.periodicVelocity (selectedPotentialSum a) (t, x) =
        SpatialLocalization.cutVelocity (selectedPotentialSum a) (t, x) :=
      (SpatialLocalization.periodicVelocity_eventuallyEq_cut
        (selectedPotentialSum a) (z := (t, x)) hi).self_of_nhds
    _ = SpatialLocalization.spatialCutoff x •
          SpatialCurl.spatialCurl (selectedPotentialSum a) (t, x) +
        SpatialCurl.curlLinear
          ((fderiv ℝ SpatialLocalization.spatialCutoff x).smulRight
            (selectedPotentialSum a (t, x))) :=
      SpatialLocalization.cutVelocity_product_rule
        (selectedPotentialSum a) t x hA

end NavierStokesReview.SelectedPotentialProductionProductRule
