import NavierStokes.R3.ComparatorBridge

/-!
# CMI comparator class-inclusion probe

This review-owned probe records the exact direction used by the R3 breakdown
adapter.  It is deliberately narrower than an equivalence claim: a comparator
solution is transported into the R3 `GlobalFiniteEnergySolution` class, which
is the direction needed to turn `¬ Nonempty GlobalFiniteEnergySolution` into
the comparator nonexistence conclusion.  No converse is asserted here.
-/

namespace NavierStokesReview

open NavierStokes
open NavierStokesR3

theorem comparator_solution_in_global_class
    {ν : ℝ} {f : NavierStokesR3.ProblemStatement.VelocityField}
    {v : NavierStokesR3.ProblemStatement.Space → ℝ →
      NavierStokesR3.ProblemStatement.Space}
    {p : NavierStokesR3.ProblemStatement.Space → ℝ → ℝ}
    (h : Comparator.NavierStokesExistenceAndSmoothnessRn ν
      (fun _ => 0) (ComparatorBridge.toComparator f) v p) :
    Nonempty (ProblemStatement.GlobalFiniteEnergySolution ν f) := by
  exact ⟨NavierStokesR3.globalSolutionOfComparator h⟩

theorem comparator_nonexistence_follows_from_global_nonexistence
    {ν : ℝ} {f : NavierStokesR3.ProblemStatement.VelocityField}
    (hglobal : ¬ Nonempty
      (NavierStokesR3.ProblemStatement.GlobalFiniteEnergySolution ν f)) :
    ¬ (∃ v p,
      Comparator.NavierStokesExistenceAndSmoothnessRn ν
        (fun _ => 0) (ComparatorBridge.toComparator f) v p) := by
  rintro ⟨v, p, h⟩
  exact hglobal (comparator_solution_in_global_class h)

end NavierStokesReview
