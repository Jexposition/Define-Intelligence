import NavierStokes.R3.ConservativeDifference
import NavierStokes.R3.PressureRecoveryHelpers
import NavierStokes.R3.PressureRecovery
import NavierStokes.R3.RieszTestOperators

/-!
This probe records the pressure-recovery interfaces available in the source
tree. It deliberately does not claim that these comparison-level theorems are
instantiated by the selected candidate.
-/

open NavierStokes
open NavierStokesR3

#check NavierStokesR3.ConservativeDifference.weak_pressure_poisson
#check NavierStokesR3.PressureRecovery.gradient_recovery
#check NavierStokesR3.PressureRecovery.pressure_gradient_recovery
#check NavierStokesR3.RieszTestOperators.pressurePair_laplacianCLM
#check NavierStokesR3.RieszTestOperators.laplacian_rieszTest

theorem pressure_recovery_infrastructure_probe : True := by
  trivial
