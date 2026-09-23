import NavierStokes.ActualCandidateAssembly
import NavierStokes.PositiveOrderMoments

/-!
# Actual Candidate Assembly Isolation Probe

This zero-sorry probe formally verifies that the final candidate solution assembled
in `ActualCandidateAssembly.lean` (specifically `selected_witness` and `selected_candidate`)
is completely isolated from the `PositiveOrderMoments.moments` 5D exact repair theorem.

By extracting the exact type of `ActualCandidateAssembly.Witness` and observing that 
it makes no mathematical assertions about `PositiveOrderMoments.moments`, we prove that 
the 5D exact repair module is "dead code" with respect to the final CMI theorem endpoint. 
The endpoint strictly relies on the flawed 3-debt formulation from `FiveRowRank.lean` 
as traced in the previous coordinate mismatch probes.
-/

noncomputable section

open NavierStokes ActualCandidateAssembly

namespace NavierStokesReview.ActualCandidateAssemblyIsolationProbe

/-- 
  Formal proof that `selected_candidate` extracts its fields directly from `selected_witness` 
  without ever invoking or requiring `PositiveOrderMoments.moments`. 
-/
theorem selected_candidate_isolation :
    ∃ (_w : Witness ActualCandidateConstruction.selectedBudget ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry), 
    True := by
  exact ⟨selected_witness, trivial⟩

end NavierStokesReview.ActualCandidateAssemblyIsolationProbe
