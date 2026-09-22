import NavierStokes.GlobalBaseError
import NavierStokes.JointResidualLimits

/-!
The principal endpoint filter is checked separately because `JetRate` itself
does not carry a `NeBot` assumption.
-/

open Filter

example : NavierStokes.GlobalBaseError.originPast.NeBot := by
  rw [NavierStokes.GlobalBaseError.originPast]
  exact NavierStokes.JointResidualLimits.past_filter_neBot 0
