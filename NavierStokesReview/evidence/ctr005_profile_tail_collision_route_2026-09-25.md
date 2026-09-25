# CTR-005 profile-tail collision route

**Date:** 2026-09-25

**Scope:** `FiveRowRank`, `DefectIncrementBounds`, selected cycle, and final
`ActualCandidateAssembly.Witness`

**Result:** the proposed route identifies a valid missing bridge, but its
current nonzero-remainder premise is not proved.

## What the source actually proves

`NavierStokes/FiveRowRank.lean:22` defines the runtime debt as
`Fin 3 → ℝ`. `FiveRows` is defined at `:241-247` with correction profiles
`dv` and `ga` as its final arguments. Its first two equations are therefore
zero moments of those correction profiles, not zero total-field moments.

`NavierStokes/DefectIncrementBounds.lean:214-219` defines `barMoment` as a
function-valued radial integral:

```lean
barMoment k f n p =
  ∫ r, r ^ k * PressureStream.torusAverage (f n) (r, p)
```

It returns a scalar field over the remaining index `n` and parameter `p`.
It is not a total Cartesian integral of the assembled `VelocityField`, and it
does not state a kinetic-energy identity.

The source proves the correction scope directly at `:621-633` and preserves
the two designated moments under an update at `:635-645`. The selected cycle
also exposes a genuine zero-moment invariant in
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean:33-58`.

## Review-side zero-sorry check

`NavierStokesReview/src/refutations/CTR005ProfileTailCollisionScope.lean`
builds the following results:

1. `five_rows_are_increment_scoped`: the first two rows constrain only the
   correction functions `dv` and `ga`.
2. `nonzero_runtime_debt_compatible_with_zero_correction_rows`: a nonzero
   three-coordinate debt is compatible with those two zero correction rows;
   the concrete repair is supplied by `MeanRankUpdateAudit`.
3. `selected_cycle_zero_rows_are_not_total_field_moments`: the selected cycle
   carries its actual local two-moment invariant.
4. `barMoment_is_radial_profile_quantity`: the exact radial/toroidal type of
   `barMoment` is exposed in the review namespace.

The review library builds successfully under Lean 4.34.0-rc2 with 3,693 jobs.
The new module contains no `sorry`, `axiom`, or `unsafe` declaration.

## Consequence for the proposed `False` route

The conditional obstruction is valid:

$$
\text{FiveRows}(dv,ga)\ \land\ \bar M_2(ga)\ne0
\quad\Longrightarrow\quad \bot.
$$

But the selected endpoint currently supplies neither a theorem that its
Cartesian `tsum` has this `barMoment` representation nor a theorem that the
corresponding selected moment is nonzero. The proposed theorem
`∃ Δm, moments = Δm` would be tautological and supplies no mismatch.

The surviving research target is therefore exact: construct a source-backed
map from the selected mixed Cartesian fields and pressure to the radial
history/profile inputs of `PositiveOrderMoments` or `DefectIncrementBounds`,
then evaluate one selected component. Until a nonzero remainder or another
false selected premise is proved, CTR-005 remains a publication-level
failure of selected-field correspondence, not a kernel-level `False`.
