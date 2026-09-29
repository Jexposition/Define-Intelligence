# Selected direct native prefix moment

## Result

The completion
`NavierStokesReview/src/completions/SelectedDirectNativePrefixMoment.lean`
proves two selected-path identities without `sorry`, custom axioms, or
`unsafe` code.

For every finite prefix `J` and moment index `n`, the native direct scalar
prefix telescopes exactly to the selected cycle state:

```lean
theorem selected_direct_native_scalar_prefix_eq_cycle_mean
    (J n : ℕ) :
    (fun z => ∑ j ∈ Finset.range (J + 1), selectedScalar j n z) =
      (selectedCycle J).state.mean.angular n
```

On the selected carrier, the corresponding order-two native radial moment is
zero:

```lean
theorem selected_direct_native_scalar_prefix_barMoment_zero
    (J n : ℕ) {s : PressureStream.Plane}
    (hs : ActualInitialization.geometry.region.carrier s) :
    DefectIncrementBounds.barMoment 2
        (fun m z => ∑ j ∈ Finset.range (J + 1), selectedScalar j m z)
        n s = 0
```

## Source anchors

| Item | Location |
|---|---|
| Native stage definition | `NavierStokes/ActualCandidateConstruction.lean:392-394` |
| Native successor identity | `NavierStokes/ActualCandidateConstruction.lean:406-411` |
| Cycle base and state update | `NavierStokes/ActualCandidateConstruction.lean:44-48` |
| New finite-prefix completion | `NavierStokesReview/src/completions/SelectedDirectNativePrefixMoment.lean:22-53` |
| Existing cycle moment transport | `NavierStokesReview/src/completions/SelectedDirectStageMomentTransport.lean:32-54` |

## Build

Focused verification:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean \
  NavierStokesReview/src/completions/SelectedDirectNativePrefixMoment.lean
exit status: 0
```

The file contains no `sorry`, custom axiom, or `unsafe` declaration.

## Scope

This is a selected native scalar result before the production spatial cutoff,
Cartesian curl branch, auxiliary torus average, and final natural-number
`tsum`. It clears the native direct prefix as the source of a remainder. It
does not prove that the exported mixed velocity has zero `barMoment`, does not
prove a nonzero remainder, and does not prove `False`.

The live calculation remains the exact transport of the cutoff-weighted direct
term and the curled potential term into the scalar consumed by `barMoment`.
