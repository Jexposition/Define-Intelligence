import NavierStokes.ActualCandidateAssembly
import NavierStokes.DefectIncrementBounds

/-!
# Selected field to `barMoment` interface

The production candidate is a Cartesian vector field on `SpaceTime`, whereas
`barMoment` consumes a scalar family on `PressureStream.Lift P`.  This file
formalises the pullback that must be supplied before the two constructions can
be compared.  It deliberately proves only the transport identity induced by
that pullback; it does not invent axis, support, or nonzero-remainder facts.
-/

noncomputable section

namespace NavierStokesReview.SelectedBarMomentInterface

open NavierStokes
open NavierStokes.ProblemStatement
open NavierStokes.DefectIncrementBounds
open NavierStokes.PressureStream

/- The first Cartesian component of a selected potential stage. -/
noncomputable def selectedPotentialComponent (j : ℕ) : SpaceTime → ℝ :=
  fun z => (ActualCandidateAssembly.selectedPotentialStages j z) 1

/- Pull a spacetime scalar field back to the scalar-family domain of `barMoment`. -/
noncomputable def pullbackScalar {P : Type}
    (φ : Point P → SpaceTime) (g : SpaceTime → ℝ) : ScalarField (Point P) :=
  fun _ q => g (φ q)

theorem selected_component_barMoment_apply
    {P : Type} [NormedAddCommGroup P] [NormedSpace ℝ P]
    (φ : Point P → SpaceTime) (j k n : ℕ) (p : P) :
    barMoment k (pullbackScalar φ (selectedPotentialComponent j)) n p =
      ∫ r, r ^ k * PressureStream.torusAverage
        (fun q => selectedPotentialComponent j (φ q)) (r, p) := by
  rw [barMoment_apply]
  rfl

/-
The exact data needed for a selected-field `barMoment` comparison is explicit:
one must provide a point-to-spacetime map and a scalar pullback.  The
production `selected_witness` does not export either object as a field.
-/
structure SelectedBarMomentTransportData
    {P : Type} [NormedAddCommGroup P] [NormedSpace ℝ P] (j : ℕ) where
  pointToSpaceTime : Point P → SpaceTime
  scalarProfile : ScalarField (Point P)
  scalarProfile_eq_selected :
    ∀ n q, scalarProfile n q =
      selectedPotentialComponent j (pointToSpaceTime q)

theorem selected_component_requires_transport_data
      {P : Type} [NormedAddCommGroup P] [NormedSpace ℝ P] (j : ℕ)
    (D : SelectedBarMomentTransportData j) (k n : ℕ) (p : P) :
    barMoment k D.scalarProfile n p =
      ∫ r, r ^ k * PressureStream.torusAverage
        (fun q => selectedPotentialComponent j (D.pointToSpaceTime q)) (r, p) := by
  rw [barMoment_apply]
  have hprofile : D.scalarProfile n =
      (fun q => selectedPotentialComponent j (D.pointToSpaceTime q)) := by
    funext q
    exact D.scalarProfile_eq_selected n q
  rw [hprofile]

end NavierStokesReview.SelectedBarMomentInterface
