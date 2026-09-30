import NavierStokes.ActualCyclePreservation
import NavierStokes.ActualCandidateAssembly

/-!
# Positive trace for the actual internal moment/debt invariant

This probe records the strongest source-supported positive result relevant to
CTR-005.  The actual cycle invariant carries two zero mean-mass identities and
three residual-debt classes.  This is not a claim that these five internal
coordinates are already identified with the manuscript's `(M,I,J,S,Cp)` after
the Cartesian curl, localisation, summation, and force export.
-/

noncomputable section

namespace NavierStokesReview.ActualMomentPreservationTrace

open NavierStokes
open NavierStokes.ActualCyclePreservation
open NavierStokes.CorrectionState
open NavierStokes.CorrectionStep
open NavierStokes.GaugeMassPreservation
open NavierStokes.WeightedClasses

theorem actual_state_carries_two_zero_mean_masses (B N0 j : ℕ)
    (hN : ActualCarrierGeometry.geometricThreshold ≤ N0) :
    ZeroMassesOn ActualInitialization.geometry.region.carrier
      (ActualCyclePreservation.state B N0 j).state :=
  (ActualCyclePreservation.state_runInvariant B N0 hN j).analytic.masses

theorem actual_state_carries_three_debt_classes (B N0 j : ℕ)
    (hN : ActualCarrierGeometry.geometricThreshold ≤ N0) (i : Fin 3) :
    UnweightedClass ActualInitialization.geometry.slowStrip
      (1 + ActualIterationLedger.sigma j)
      (fun n x => CorrectionState.debt
        (CorrectionInitialization.ActualPrimary.commonContext B)
        (ActualCyclePreservation.state B N0 j).state n x i) :=
  (ActualCyclePreservation.state_runInvariant B N0 hN j).analytic.debt i

theorem actual_cycle_invariant_contains_two_plus_three_coordinates
    (B N0 j : ℕ) (hN : ActualCarrierGeometry.geometricThreshold ≤ N0) :
    ZeroMassesOn ActualInitialization.geometry.region.carrier
        (ActualCyclePreservation.state B N0 j).state ∧
      (∀ i : Fin 3,
        UnweightedClass ActualInitialization.geometry.slowStrip
          (1 + ActualIterationLedger.sigma j)
          (fun n x => CorrectionState.debt
            (CorrectionInitialization.ActualPrimary.commonContext B)
            (ActualCyclePreservation.state B N0 j).state n x i)) := by
  exact ⟨actual_state_carries_two_zero_mean_masses B N0 j hN,
    actual_state_carries_three_debt_classes B N0 j hN⟩

end NavierStokesReview.ActualMomentPreservationTrace
