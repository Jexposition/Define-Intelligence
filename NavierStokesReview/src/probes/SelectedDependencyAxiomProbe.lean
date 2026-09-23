import NavierStokes.ActualCandidateAssembly
import NavierStokes.GluedStageEstimates
import NavierStokes.ActualCycleResidualBounds

/-!
# Axiom and dependency checkpoint for the selected witness

This probe does not claim that the exported theorem is semantically correct.
It records the kernel-level dependency status of the selected witness and of
the two moment consumers that feed it.
-/

#print axioms NavierStokes.ActualCandidateAssembly.selected_witness
#print axioms NavierStokes.ActualCandidateAssembly.physicalData
#print axioms NavierStokes.GluedStageEstimates.actualStageEstimates
#print axioms NavierStokes.ActualCycleResidualBounds.Invariant.residual_jetRate
