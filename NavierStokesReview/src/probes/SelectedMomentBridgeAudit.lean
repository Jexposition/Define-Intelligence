import NavierStokes.ActualCandidateAssembly
import NavierStokes.FiveRowRank
import NavierStokes.PositiveOrderMoments

/-!
# Selected-endpoint moment bridge audit

This is a diagnostic probe, not a replacement theorem.  It records the exact
types exposed by the selected endpoint and the two separate moment-repair
modules.  The audit question is whether `selected_witness` carries a theorem
that identifies its selected stage fields with either repair system.
-/

open NavierStokes

#check ActualCandidateAssembly.selected_witness
#check ActualCandidateAssembly.selectedPotentialStages
#check ActualCandidateAssembly.selectedDirectStages
#check ActualCandidateAssembly.selectedPressureStages
#check ActualCandidateAssembly.endpoints
#check FiveRowRank.FiveRows
#check FiveRowRank.five_rows
#check PositiveOrderMoments.moments
#check PositiveOrderMoments.exists_parameterized_exact_repair

/- The selected aliases are raw stage histories, not debt-bearing records. -/
example : ActualCandidateAssembly.selectedPotentialStages =
    ActualCandidateAssembly.potentialStages
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry := by
  rfl

example : ActualCandidateAssembly.selectedDirectStages =
    ActualCandidateAssembly.directStages
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry := by
  rfl

example : ActualCandidateAssembly.selectedPressureStages =
    ActualCandidateAssembly.pressureStages
      ActualCandidateConstruction.selectedBudget
      ActualCandidateConstruction.selectedThreshold
      ActualCandidateConstruction.selectedThreshold_geometry := by
  rfl

/- The selected theorem exposes `Witness`; it does not expose a FiveRows or
   PositiveOrderMoments equality as part of its result type. -/
#check ActualCandidateAssembly.Witness

