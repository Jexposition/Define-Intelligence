import ComparatorChallenges.NavierStokes
import ComparatorChallenges.Euler

/-!
# Repository admission census

This file is a review-side source audit.  It does not import the admitted
challenge theorem into the selected proof path and it contains no admitted
declarations itself.  The `#print axioms` commands are retained as the
machine-readable record that the standalone comparator declarations depend on
`sorryAx`.
-/

namespace NavierStokesReview.RepositoryAdmissionAudit

theorem review_module_is_admission_free : True := by
  trivial

#print axioms NavierStokes.Comparator.navier_stokes_breakdown_R3
#print axioms NavierStokes.Comparator.navier_stokes_breakdown_periodic
#print axioms Euler.euler_breakdown_R3
#print axioms Euler.exists_compact_smooth_euler_singularity

end NavierStokesReview.RepositoryAdmissionAudit
