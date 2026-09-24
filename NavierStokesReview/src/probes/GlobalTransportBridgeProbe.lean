import NavierStokes.CandidateConsequences
import extensions.SameDatumFixedForcePerturbation

noncomputable section

namespace NavierStokesReview.GlobalTransportBridgeProbe

open NavierStokes NavierStokes.ProblemStatement
open NavierStokes.CandidateConsequences
open NavierStokesReview.SameDatumFixedForcePerturbation

/-!
# Global consequence bundle versus fixed-data transport

`CandidateConsequences.mixed_exists_force_with_consequences` exports a force,
`CandidateProperties`, the maximal-lifespan/Sobolev/jet consequences, and the
boundary jet identity.  The exported consequence structure has no field for
the five named physical moments and no fixed-force perturbation predicate.

The theorem below tests the global bundle against the independently constructed
same-datum perturbation.  It proves that the two interfaces coexist: the
global PDE consequences are available while same-force stability fails.  This
is a contract-level result, not a claim that the literal existential C/D
statement is inconsistent.
-/

theorem selected_global_consequences_with_fixed_force_obstruction :
    ∃ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f ∧
      Consequences u p f ∧
      ¬ FixedForceSameDatumStable u p f := by
  obtain ⟨u, p, f, hc, hnot⟩ :=
    selected_candidate_fails_fixed_force_same_datum_stability
  exact ⟨u, p, f, hc, consequences_of_candidate hc, hnot⟩

theorem global_consequence_bundle_does_not_imply_fixed_force_stability :
    ¬ (∀ (u : VelocityField) (p : PressureField) (f : VelocityField),
      CandidateProperties u p f → Consequences u p f →
        FixedForceSameDatumStable u p f) := by
  intro h
  obtain ⟨u, p, f, hc, hcon, hnot⟩ :=
    selected_global_consequences_with_fixed_force_obstruction
  exact hnot (h u p f hc hcon)

end NavierStokesReview.GlobalTransportBridgeProbe
