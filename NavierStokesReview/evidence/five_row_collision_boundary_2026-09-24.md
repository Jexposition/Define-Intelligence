# Five-row collision boundary

## Question

Does a compact perturbation automatically collide with the two zero rows of
`FiveRowRank.FiveRows`, force a nonzero mass or energy increment, and derive
`False` from the selected witness?

## Source facts

`NavierStokes/FiveRowRank.lean:21-22` defines

```lean
abbrev Debt := Fin 3 → ℝ
```

The predicate at `NavierStokes/FiveRowRank.lean:240-246` takes two correction
functions `dv` and `ga`. Its first two conjuncts are

```lean
(∫ R, R ^ 2 * dv R) = 0
(∫ R, R * ga R) = 0
```

The remaining three conjuncts use `d 0`, `d 1`, and `d 2`. They are equations
on the correction fields, not equations on the exported Cartesian velocity in
`ActualCandidateAssembly.Witness`.

The theorem `FiveRowRank.five_rows` at lines 279--284 proves these five rows
for every admissible `d : Fin 3 → ℝ`. In particular, the rank predicate is
not empty when the debt is nonzero.

The downstream preservation theorem
`DefectIncrementBounds.fiveRows_preserve_masses` at lines 635--646 proves
preservation of `barMoment 2` for the angular component and `barMoment 1` for
the axial component. `DefectIncrementBounds.zeroMasses` at lines 808--813
lifts this to `CorrectionState.ZeroMasses`. These are radial correction-state
invariants. The source does not identify them with a generic kinetic-energy
integral or with the selected Cartesian velocity without an additional
transport theorem.

Finally, `ActualCandidateAssembly.Witness` at lines 1121--1151 contains a
schedule, three raw stage sequences, away extensions, a force, candidate
properties, consequences, norm divergence, force decay, and endpoint jets.
It contains no `FiveRows`, `Debt`, `physicalMoments`, or equality to the
paper tuple `(M, I, J, S, C_p)`.

## Zero-sorry probe

`NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean` proves:

```lean
theorem fiveRows_admits_nonzero_debt :
  FiveRowRank.FiveRows (FiveRowRank.background 1 1) (fun _ => 0)
    nonzeroThreeDebt
    (FiveRowRank.deltaV 1 1 1 2 nonzeroThreeDebt)
    (FiveRowRank.gamma 1 1 1 2 nonzeroThreeDebt)
```

It also proves that `selected_witness` and a nonzero rank debt coexist as
separate propositions. The file compiles with Lean 4.34.0-rc2, exit code 0,
with no `sorry`, `axiom`, or `unsafe` declaration.

## Finding

The proposed direct collision is not established. The two zero rows constrain
the correction functions and are preserved by the rank-state update; they do
not by themselves constrain the selected velocity or its energy. The compact
fixed-force perturbation remains a valid fixed-data obstruction, but it does
not enter the selected rank state and therefore cannot be combined with these
rows to derive `False`.

The live falsification target remains `CTR-005`: a theorem is still required
that transports the paper's five named moments through the selected stage
fields, rank corrections, residual, pressure, and endpoint force. Until such
a theorem or a false selected premise is exhibited, the collision argument is
a rejected inference, not a disproof of the C/D endpoint.

