import completions.SelectedPotentialProductionFinitePrefix

/-!
# Selected potential production: local scope of the infinite sum

The source defines the selected potential by an actual `tsum`.  Its
`SolenoidalDiagonal` API proves that, at a positive scale and under the
required convergence hypotheses, every derivative is locally represented by
one finite prefix.  This completion specialises that theorem to the selected
production stages.  It does not pass the local equality through
`torusAverage`, `barMoment`, or the radial integral; those remain separate
global transport obligations.
-/

noncomputable section

namespace NavierStokesReview.SelectedPotentialProductionTsumScope

open NavierStokes
open NavierStokes.ActualCandidateAssembly
open NavierStokes.ActualCandidateConstruction
open NavierStokes.CorrectionInitialization
open NavierStokes.PhysicalWaveSum
open NavierStokes.ProblemStatement
open NavierStokes.SolenoidalDiagonal
open Filter
open scoped Topology

theorem selected_potential_sum_all_jets_eventuallyEq_partial
    (a : ℕ → ℝ) (ha : Tendsto a atTop atTop)
    {z : ProblemStatement.SpaceTime}
    (hq : ContinuousAt
      (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h) z)
    (hscale : 0 <
      PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h z) :
    ∃ N : ℕ, ∀ k : ℕ,
      iteratedFDeriv ℝ k
          (SolenoidalDiagonal.potentialSum a
            (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
            ActualCandidateAssembly.selectedPotentialStages) =ᶠ[𝓝 z]
        iteratedFDeriv ℝ k
          (SolenoidalDiagonal.partialPotential a
            (PhysicalWaveSum.physicalQ CorrectionInitialization.ActualPrimary.h)
            ActualCandidateAssembly.selectedPotentialStages N) := by
  exact SolenoidalDiagonal.potentialSum_allJets_eventuallyEq_partial
    (A := ActualCandidateAssembly.selectedPotentialStages) ha hq hscale

end NavierStokesReview.SelectedPotentialProductionTsumScope
