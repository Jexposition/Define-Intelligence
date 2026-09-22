import NavierStokes.DiagonalResidual

/-!
# Derived-filter audit

`JetRate` does not require its filter to be nontrivial.  The main endpoint
filter is separately proved nontrivial, but a conjunction with an arbitrary
principal complement is not nontrivial merely because the base filter is.
This probe records that distinction without asserting that the selected
construction actually uses a bottom derived filter.
-/

open Filter Set

namespace NavierStokesReview

example : (⊤ : Filter Unit).NeBot := by infer_instance

example : ¬ ((⊤ : Filter Unit) ⊓ 𝓟 (Set.univ : Set Unit)ᶜ).NeBot := by
  simp

example : ¬ ((⊥ : Filter Unit).NeBot) := by
  intro h
  exact h.ne (by simp)

end NavierStokesReview
