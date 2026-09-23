import NavierStokes.ActualCandidateAssembly
import NavierStokes.DiagonalResidual
import NavierStokes.JointResidualLimits

open Filter
open NavierStokes
open NavierStokes.ProblemStatement
open scoped Topology

/-! Source probe for the filter used by the selected residual-limit path. -/

#check DiagonalResidual.JetRate
#check JointResidualLimits.past_filter_neBot

theorem selected_endpoint_filter_nontrivial :
    (nhdsWithin ((1 : ℝ), (0 : Space)) (SpacetimeEndpoint.openPast 1)).NeBot := by
  exact JointResidualLimits.past_filter_neBot 0

theorem selected_endpoint_filter_supports_instance :
    Nonempty (nhdsWithin ((1 : ℝ), (0 : Space)) (SpacetimeEndpoint.openPast 1)).NeBot := by
  exact ⟨selected_endpoint_filter_nontrivial⟩
