import NavierStokes.R3.ProblemStatement
import NavierStokes.R3.WholeSpaceComparisonClosure
import NavierStokes.R3.PressureRecovery
import NavierStokes.R3.PressureFlux
import NavierStokes.R3.WholeSpaceUniqueness

/-!
Independent review probe for the already-built analytic comparison layer.
This deliberately does not import the exported Comparator solution or any
challenge file. Its output is evidence about intermediate dependencies only.
-/

#print axioms NavierStokesR3.WholeSpaceUniqueness.classical_uniqueness_on_Icc
#print axioms NavierStokesR3.WholeSpaceComparisonClosure.eq_of_pressure_flux_bound
#print axioms NavierStokesR3.PressureRecovery.gradient_recovery
#print axioms NavierStokesR3.PressureFlux.exists_uniform_actual_pressure_flux_bound
