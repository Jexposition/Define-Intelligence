import NavierStokes.R3.ComparatorBridge

/-!
# Independent CMI force-class probe

This probe checks the exact bridge used by the whole-space CMI route.  It does
not inspect compilation as a mathematical result: it asks Lean to elaborate
the theorem that a globally smooth compactly supported force has the full
Comparator `ForceConditionDecay` predicate, and that the selected zero datum
has the required initial-data predicate.
-/

namespace NavierStokesReview

open NavierStokes
open NavierStokesR3
open scoped ContDiff

example {f : NavierStokesR3.ProblemStatement.VelocityField}
    (hf : ContDiff ℝ ∞ f) (hs : HasCompactSupport f) :
    Comparator.ForceConditionDecay (ComparatorBridge.toComparator f) :=
  forceConditionDecay_of_compact hf hs

example : Comparator.InitialVelocityConditionDecay
    (fun _ : EuclideanSpace ℝ (Fin 3) => (0 : EuclideanSpace ℝ (Fin 3))) :=
  ComparatorBridge.zero_initial_condition_decay

end NavierStokesReview
