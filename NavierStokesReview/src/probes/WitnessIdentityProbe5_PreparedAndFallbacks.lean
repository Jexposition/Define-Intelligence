import NavierStokes.PreparedOutgoing
import NavierStokes.PrimaryGeometryAssembly
import NavierStokes.ValidBandGluing
import NavierStokes.JointResidualLimits

/-!
# Witness Identity Probe 5: `exists_prepared` selected twice + fallback audit

**What it selects:** `Classical.choice exists_prepared` picks an inhabitant
of `PreparedProfile` — a structure with 9 fields (profile, bound, bound_pos,
specification, schedule, terminal, amplitude_lower, height_upper, clean).

**Where it is selected:**
  1. `PreparedOutgoing.prepared`                     (L119)
  2. `PrimaryGeometryAssembly.prepared`              (L463)

**Key distinction:** These select from DIFFERENT existence theorems.
  - `PreparedOutgoing.exists_prepared : Nonempty PreparedProfile`
  - `PrimaryGeometryAssembly.exists_prepared H v hcone upper B r0 hbox N0 :
      Nonempty (Prepared H v upper B r0 N0)`

The types are different! `PreparedOutgoing.PreparedProfile` ≠
`PrimaryGeometryAssembly.Prepared`. The provenance scanner matched on
the name `exists_prepared` but these are completely different theorems
in different namespaces.

**This is a FALSE POSITIVE from the name-based scanner.**
-/

namespace NavierStokesReview.WitnessIdentityProbe5

-- Verify: the two `prepared` defs have different types
#check @NavierStokes.PreparedOutgoing.prepared
  -- : NavierStokes.PreparedOutgoing.PreparedProfile

#check @NavierStokes.PrimaryGeometryAssembly.prepared
  -- : ... → NavierStokes.PrimaryGeometryAssembly.Prepared ...

/-!
## ValidBandGluing.representative fallback audit (bonus)

The fallback pattern `if h : ∃ i, x ∈ U i then f (Classical.choose h) x else 0`
is architecturally guarded by `representative_eq_of_mem`:

```
theorem representative_eq_of_mem (hf : Compatible U f) {i : ι} {x : D} (hx : x ∈ U i) :
    representative U f x = f i x
```

This theorem proves that on the valid domain (where some chart covers `x`),
the representative equals the chart value — regardless of which chart was
chosen by `Classical.choose`. The key insight: `Compatible U f` says all
charts agree on overlaps, so the choice of chart doesn't matter.

The zero branch is only reached when `x ∉ ⋃ i, U i`. The theorem
`representative_zero` explicitly states this:

```
theorem representative_zero (hx : x ∉ domain U) : representative U f x = 0
```

So the fallback is genuinely external to the valid domain, and the
`representative_contDiffOn` theorem only claims smoothness on `domain U`,
not on all of `D`. This is **correct totalization** — the zero value
is never consumed by any downstream smoothness or estimate theorem.
-/

-- Verify the guarding theorem exists and has the right type
#check @NavierStokes.ValidBandGluing.representative_eq_of_mem
#check @NavierStokes.ValidBandGluing.representative_zero
#check @NavierStokes.ValidBandGluing.representative_contDiffOn

/-!
## JointResidualLimits.boundaryLimits independence (bonus)

The `boundaryLimits` construction selects `Classical.choice (hext x hx)`
but then proves independence in two theorems:

1. `boundaryLimits_eq_extension`: the chosen tensor family equals any
   *other* extension's tensors at (1,x). This is proved by uniqueness
   of limits: both the chosen extension and any other extension converge
   to the same value, so their limits agree.

2. `boundaryLimits_independent`: given TWO different `AwayExtensions`
   proofs `h₁` and `h₂`, `boundaryLimits f h₁ = boundaryLimits f h₂`.

This is the **gold standard** for witness independence: the construction
explicitly proves it doesn't depend on which extension was chosen.
-/

#check @NavierStokes.JointResidualLimits.boundaryLimits_eq_extension
#check @NavierStokes.JointResidualLimits.boundaryLimits_independent

/-!
## Summary of all 5 probes

| Risk | Source | Verdict | Level |
| --- | --- | --- | --- |
| 1 | `finalPotential_awayExtensions` × 4 | All outputs are Prop (Nonempty) — erased | NONE |
| 2 | `exists_surjective_nat` × 4 | Locally scoped, only Surjective used | LOW |
| 3 | `exists_admissibleScales` × 3 | Different coefficient bundles — genuinely different | LOW |
| 4 | `choice_nonempty` × 2 | NoOptions is standalone audit file — never on proof path | NONE |
| 5 | `exists_prepared` × 2 | Different types, different namespaces — name collision | NONE |

**Overall:** No confirmed identity violations in the top-5 risks.
The scanner's name-matching heuristic produces false positives for
risks 4 and 5. Risks 1–3 are genuine multiple selections but are
architecturally safe.
-/

end NavierStokesReview.WitnessIdentityProbe5
