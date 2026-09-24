# Same-datum fixed-force obstruction

## Result

`NavierStokesReview/src/extensions/SameDatumFixedForcePerturbation.lean`
compiles with Lean 4.34.0-rc2 and contains no `sorry`, `admit`, or `unsafe`
declarations.
The dedicated axiom audit reports only `[propext, Classical.choice, Quot.sound]`.

The extension repairs a limitation in the earlier fixed-force probe. The earlier
perturbation was smooth, compactly supported on each spatial slice, and
divergence-free, but it did not preserve the selected zero initial datum. The
new perturbation does.

## Exact construction

For an interior time `t₀`, the perturbation is

```lean
def sameDatumCompactPerturbation (t₀ : ℝ) : VelocityField :=
  fun z => (z.1 * (z.1 - t₀)) • compactCurlField z
```

The factor `t (t - t₀)` gives both

```lean
sameDatumCompactPerturbation t₀ (0, x) = 0
sameDatumCompactPerturbation t₀ (t₀, x) = 0
```

while its temporal derivative at `t₀` is

```lean
t₀ • compactCurlField (t₀, x)
```

The source locations are:

| Lines | Verified content |
|---:|---|
| 23--36 | Definition, global smoothness, and compact spatial slices |
| 38--40 | Preservation of the zero initial datum |
| 42--56 | Slice-wise divergence-free property |
| 58--72 | Vanishing value, spatial derivative, and spatial Laplacian at `t₀` |
| 74--87 | Exact temporal derivative at `t₀` |
| 89--105 | Residual defect identity at the switch |
| 106--119 | Nonzero defect at the spatial origin when `t₀ ≠ 0` |
| 121--139 | Same-datum admissibility predicate and proof |
| 141--196 | Selected-candidate fixed-force obstruction |

At the origin, `compactCurlField (t₀, 0)` is the first coordinate vector.
Therefore the defect at the switch is `t₀ • coordinateVector 0`, which is
nonzero for `t₀ ≠ 0`.

## Formal scope

The theorem

```lean
selected_candidate_fails_fixed_force_same_datum_stability
```

proves that the selected candidate does not satisfy the stronger predicate
`FixedForceSameDatumStable`: no smooth, compactly supported, divergence-free
perturbation preserving `u(0, ·) = 0` can be added while keeping the same
pressure, force, and residual equation at every spacetime point.

This is a stronger and cleaner provenance objection than the earlier probe. It
still does not by itself prove `False` from the literal CMI alternatives, which
are existential and do not contain a perturbation-stability or force-
independence predicate. The result becomes a literal disproof only if the
published claim is formalised with that additional forward-data requirement, or
if an independent theorem identifies that requirement as part of the endpoint
being claimed.
