import NavierStokes.ActualParticularStageControls

open Set

namespace NavierStokesReview.ActivePairEmptyBranchProbe

open NavierStokes.ActualParticularStageControls

theorem controlPatch_empty_of_not_nonempty {B N0 : ℕ}
    (hne : ¬ Nonempty (ActivePair B N0))
    (l : Label B N0) (n : ℕ) (k : NavierStokes.TorusInverse.Frequency) :
    controlPatch l n k = ∅ := by
  ext z
  constructor
  · intro hz
    exact (hne ⟨⟨(l, n), hz.1⟩⟩).elim
  · intro hz
    exact hz.elim

end NavierStokesReview.ActivePairEmptyBranchProbe
