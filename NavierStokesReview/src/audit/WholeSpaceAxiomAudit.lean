import NavierStokes.R3.Theorem
import NavierStokes.R3.WholeSpaceUniqueness
import NavierStokes.PeriodicPaperTheorem

/-!
  Audit surface for the whole-space and periodic no-global-solution endpoints.
  This file records the kernel dependency query; it does not alter the source
  construction or add premises to either endpoint.
-/

#print axioms NavierStokesR3.theorem_1_1
#print axioms NavierStokesR3.WholeSpaceUniqueness.classical_uniqueness_on_Icc
#print axioms NavierStokesR3.WholeSpaceUniqueness.candidate_global_agrees_before_one
#print axioms NavierStokes.PeriodicPaper.periodic_corollary
