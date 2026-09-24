# Correction-invariant scope

## Question

Do the first two conjuncts of `FiveRowRank.FiveRows` force a compact
perturbation of the selected Cartesian velocity to have zero mass or zero
energy?

## Result

No direct selected-field conclusion follows. The predicate is declared in
`NavierStokes/FiveRowRank.lean:241-246` as a proposition about the two radial
correction functions `dv` and `ga`:

```lean
(∫ R, R ^ (2 : ℕ) * dv R) = 0
(∫ R, R * ga R) = 0
```

The three remaining rows solve for a `Debt := Fin 3 → ℝ`. The runtime theorem
`FiveRowRank.five_rows` at lines 280-284 proves the predicate for arbitrary
debt, including nonzero debt.

The exact correction-state consequence is
`DefectIncrementBounds.fiveRows_preserve_masses` at lines 635-646:

```lean
barMoment 2 (updated m h).angular = barMoment 2 m.angular
barMoment 1 (updated m h).axial = barMoment 1 m.axial
```

`DefectIncrementBounds.RankGeometry.preserve_masses` at lines 799-805 and
`zeroMasses` at lines 808-813 lift this to the correction state. Neither
theorem mentions the selected Cartesian velocity, kinetic energy, or the
paper tuple `(M, I, J, S, C_p)`.

## Machine check

`NavierStokesReview/src/completions/CorrectionInvariantScope.lean` compiles
without `sorry`, `axiom`, or `unsafe`. It proves the genuine conditional
obstruction:

```lean
barMoment 2 h.angular ≠ 0 → False
barMoment 1 h.axial ≠ 0 → False
```

under the full `FiveRows` hypotheses. This is the theorem needed if an
independent perturbation is first transported into one of those correction
increments with a nonzero radial moment. The missing transport theorem is
exactly the remaining CTR-005 obligation.

## Audit consequence

The valid finding is narrower than “the zero rows contradict the selected
witness”: they make a nonzero correction increment impossible. To refute the
selected C/D endpoint, one must still prove that the proposed perturbation
changes one of these correction moments and that the selected endpoint is
required to absorb that perturbation through the same `FiveRows` instance.
