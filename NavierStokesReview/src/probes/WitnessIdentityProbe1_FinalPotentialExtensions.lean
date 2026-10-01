import NavierStokes.GermCandidateAssembly
import NavierStokes.MixedCandidateAssembly
import NavierStokes.MixedCandidateWitness
import NavierStokes.LocalScheduleWitness

/-!
# Witness Identity Probe 1: `TailGaugePotential.finalPotential_awayExtensions`

This is the highest-priority identity risk in the repository.

**What it selects:** `Classical.choice` is applied to
  `TailGaugePotential.finalPotential_awayExtensions H v upper bandFloor x hx`
which proves `Nonempty (OneSidedExtension _ x)` — i.e. it selects an
arbitrary one-sided smooth extension of the final potential near each
away-from-origin point `x`.

**Where it is selected:** Four distinct definitions:
  1. `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`   (L235)
  2. `MixedCandidateAssembly.candidate_of_finite_stages`                (L172)
  3. `MixedCandidateWitness.exists_candidate_witness_of_finite_stages`   (L113)
  4. `LocalScheduleWitness.awayExtensions_of_schedule`                  (L65)

**Key audit question:** Does the downstream consumption path depend on
the identity of the chosen extension, or only on its existence?

**Finding:** In `JointResidualLimits.lean`, the `boundaryLimits` construction
also selects a `Classical.choice` from `hext x hx` but then proves in
`boundaryLimits_eq_extension` and `boundaryLimits_independent` that the
resulting boundary jet family is *independent* of the particular extension
chosen. This pattern is **correct** — the boundary limits are determined
uniquely by the convergence structure, not the selection.

However, all four call sites listed above pass the `Classical.choice` value
directly as an *argument* to `MixedDiagonalExtensions.initial_add_extension`.
The question is: does `initial_add_extension` use only the *nonemptiness*
(wrapped in a Nonempty structure already), or does it use the concrete
field values of the selected extension?

**This probe demonstrates:** The value selected by `Classical.choice` feeds
into the proof of `Nonempty (OneSidedExtension (A 0) x)`, which is itself
only an existential statement. Since the output type is `Nonempty _`, the
concrete extension chosen is consumed only to *produce another Nonempty*,
which is proof-irrelevant in Lean's type theory (Nonempty is a Prop).
-/

namespace NavierStokesReview.WitnessIdentityProbe1

/-!
## Semantic observation: `Nonempty` is a Prop

In Lean 4, `Nonempty α` is defined as `⟨_⟩ : α → Nonempty α`.
Since it lives in `Prop`, any two terms of type `Nonempty α` are
definitionally equal (`Subsingleton (Nonempty α)`).

Therefore, when the output type of the proof block is `Nonempty (OneSidedExtension _ x)`,
the *particular* extension selected by `Classical.choice` inside the proof
cannot leak into the final object — the kernel equates all inhabitants.
-/

-- Verify: Nonempty is proof-irrelevant (Subsingleton)
example (α : Type*) (h₁ h₂ : Nonempty α) : h₁ = h₂ :=
  Subsingleton.elim h₁ h₂

/-!
## Risk assessment

All four call sites produce a value of type `Nonempty (OneSidedExtension _ x)`.
Since `Nonempty` is a `Prop`, the identity of the extension selected by
`Classical.choice` inside each proof is erased. The four selections are
*logically independent*: each proves existence separately, and the chosen
witnesses never escape into data.

**Verdict:** The multiple selections from `finalPotential_awayExtensions`
are *not* an identity violation. The risk pattern (two `Classical.choice`
calls producing different data objects silently narrated as the same)
does NOT apply here because the output type is `Prop`.

The actual identity risk would arise if these selections produced `data`
objects (i.e., terms in `Type`, not `Prop`). In that case, downstream code
could rely on field values that differ between selections.
-/

-- The following shows that Nonempty proofs compose without identity constraint
example (P Q : Prop) (hp : Nonempty P) (hq : P → Nonempty Q) : Nonempty Q := by
  exact hq (Classical.choice hp)

-- But this is NOT the pattern that would create identity risk.
-- Identity risk occurs when the *output* is in Type, not Prop:
-- noncomputable def riskPattern (h : ∃ x : ℝ, x > 0) : ℝ := Classical.choose h
-- Two calls to riskPattern with the same h give the same ℝ (definitionally),
-- but two calls with *different* h may give different ℝ values.

end NavierStokesReview.WitnessIdentityProbe1
