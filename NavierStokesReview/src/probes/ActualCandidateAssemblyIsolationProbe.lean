import NavierStokes.ActualCandidateAssembly
import NavierStokes.PositiveOrderMoments

/-!
# Actual Candidate Assembly Interface Probe

This zero-sorry probe records the exact type-level boundary of the exported
candidate. It does not prove that `PositiveOrderMoments` is dead code: the
repository contains a genuine five-coordinate repair theorem and imports it in
the wider construction. It also does not prove that the exported candidate is
false. The point is narrower: the proposition returned by `selected_witness`
does not expose a theorem identifying its selected fields with the named
`PositiveOrderMoments` rows.
-/

noncomputable section

open NavierStokes ActualCandidateAssembly

namespace NavierStokesReview.ActualCandidateAssemblyIsolationProbe

/-- The exported candidate is obtained from the `Witness` proposition. -/
theorem selected_candidate_isolation :
    ∃ (_w : Witness ActualCandidateConstruction.selectedBudget ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry), 
    True := by
  exact ⟨selected_witness, trivial⟩

/- The omitted bridge is a proposition-level observation, not a theorem that
   the upstream candidate is invalid. The exported `Witness` type contains
   the schedule, away extensions, forcing, `CandidateProperties`, generic
   consequences, derivative growth, and boundary jets. It does not contain a
   field of type `PositiveOrderMoments.Debt` or an equality relating such a
   debt to the selected sums. -/

end NavierStokesReview.ActualCandidateAssemblyIsolationProbe
