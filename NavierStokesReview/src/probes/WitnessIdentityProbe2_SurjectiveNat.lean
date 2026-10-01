import NavierStokes.UniformPrimaryWeights
import NavierStokes.ActualParticularStageControls

/-!
# Witness Identity Probe 2: `exists_surjective_nat` selected 4 times

**What it selects:** `Classical.choose (exists_surjective_nat α)` picks an
arbitrary surjection `ℕ → α` (or `ℕ → ℕ × ι`). The Mathlib theorem
`exists_surjective_nat` guarantees existence for any countable type.

**Where it is selected:**
  1. `ActualParticularStageControls.raw_jets`         (L943)
  2. `ActualParticularStageControls.cutoff_jets`       (L1216)
  3. `ActualSignedGeometry.activeEnumeration`          (L1278)
  4. `UniformPrimaryWeights.enumeration`               (L85)

**Key audit question:** Do downstream proofs rely on the *specific*
enumeration order, or only on surjectivity (i.e. that every element
is eventually hit)?

**Architecture observation:** In each case, the chosen surjection is
used as a local `let` binding inside a proof, paired immediately with
`Classical.choose_spec` to extract the `Surjective` property. The
surjection itself is never stored as a field of a data structure —
it lives inside a proof term.

**Risk classification:** LOW.
- Each selection is scoped to a different definition.
- The surjectivity is the only property consumed.
- Two different surjections of the same type are both surjective,
  which is all that matters.
- There is no theorem in the repository claiming two of these enumerations
  are equal, nor any definition that consumes values from two different
  enumeration selections simultaneously.
-/

namespace NavierStokesReview.WitnessIdentityProbe2

-- Key structural fact: two surjections on ℕ → α are both surjective,
-- but their *particular function values* differ. This is fine as long
-- as no downstream theorem compares f(n) between two surjections.

-- Demonstrate: surjectivity is the consumed property, not values
example {α : Type*} [Countable α] [Nonempty α] :
    ∃ f : ℕ → α, Function.Surjective f :=
  exists_surjective_nat α

-- The risk pattern that does NOT exist here:
-- If two defs both defined `let e := Classical.choose (exists_surjective_nat α)`
-- and then a third theorem used `e` from def₁ and `e` from def₂ as if they
-- were the same function, that would be an identity violation.
-- But each usage is locally scoped inside a proof, so this cannot happen.

-- Verify: UniformPrimaryWeights.enumeration stores the surjection as data
-- (it is a noncomputable def, not a proof). But its only consumer is
-- `enumeration_surjective`, which extracts `Surjective`.

#check @NavierStokes.UniformPrimaryWeights.enumeration
#check @NavierStokes.UniformPrimaryWeights.enumeration_surjective

/-!
**Verdict:** The four selections from `exists_surjective_nat` are independent
local enumerations. No downstream theorem connects them. The identity of the
chosen surjection does not leak into data fields consumed by the endpoint.

**Residual risk:** If `enumeration` (being a `noncomputable def` in `Type`)
were consumed by two different constructions that later needed to agree on
specific values `enumeration n`, that would be an identity risk. But
`enumeration_surjective` is the only consumer, which is a Prop.
-/

end NavierStokesReview.WitnessIdentityProbe2
