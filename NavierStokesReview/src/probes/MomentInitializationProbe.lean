import NavierStokes.ActualInitialization

/-!
This probe records the source-level outcome of the proposed preserved-moment
objection.  It is deliberately only an alias of the repository theorem: it
does not add an assumption or re-prove a stronger claim.
-/

namespace NavierStokesReview

theorem selected_initial_masses_are_zero (B N0 : ℕ) :
    NavierStokes.GaugeMassPreservation.ZeroMassesOn
      NavierStokes.ActualInitialization.geometry.region.carrier
      (NavierStokes.ActualInitialization.initialState B N0) :=
  NavierStokes.ActualInitialization.initial_zeroMasses B N0

end NavierStokesReview
