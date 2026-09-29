import NavierStokes.ActualMeanPotentialRealization
import completions.SelectedBarMomentInterface

/-!
# Physical point compatibility for the selected moment interface

The source does contain a compatible point type: choosing `P := Plane` makes
`PressureStream.Lift P` definitionally equal to the physical `Lift` used by
the chart realization.  This completion records that fact explicitly.  It
does not claim that the selected post-curl, post-`tsum` field has already been
transported to a scalar profile on this point type.
-/

noncomputable section

namespace NavierStokesReview.SelectedPhysicalPointTransport

open NavierStokes
open NavierStokes.ActualMeanPotentialRealization
open NavierStokes.PhysicalResidualBridge
open NavierStokesReview.SelectedBarMomentInterface

abbrev PhysicalMomentPoint := ActualMeanPotentialRealization.Point

theorem physical_moment_point_defeq_pressure_stream_point :
    PhysicalMomentPoint = DefectIncrementBounds.Point PhysicalResidualBridge.Plane := rfl

theorem barMoment_transport_requires_selected_scalar
    (j : ℕ) (D : SelectedBarMomentTransportData (P := PhysicalResidualBridge.Plane) j)
    (k n : ℕ) (p : PhysicalResidualBridge.Plane) :
    DefectIncrementBounds.barMoment k D.scalarProfile n p =
      ∫ r, r ^ k * PressureStream.torusAverage
        (fun q => selectedPotentialComponent j (D.pointToSpaceTime q)) (r, p) := by
  exact selected_component_requires_transport_data j D k n p

end NavierStokesReview.SelectedPhysicalPointTransport
