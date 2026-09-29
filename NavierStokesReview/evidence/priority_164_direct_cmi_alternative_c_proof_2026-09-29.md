# Priority 164: direct proof of Fefferman Alternative (C)

Date: 2026-09-29
Status: source- and kernel-verified positive result

## Result

The repository proves the following forced whole-space proposition for every
positive viscosity \(\nu\):

\[
\exists u_0,f,
\quad \mathrm{InitialVelocityConditionDecay}(u_0)
\land \mathrm{ForceConditionDecay}(f)
\land
\neg\exists v,p\,
  \mathrm{NavierStokesExistenceAndSmoothnessRn}(\nu,u_0,f,v,p).
\]

This is the formal comparator version of Fefferman's Alternative (C). It is
not merely a type restatement. The proof destructures the repository's actual
candidate theorem and applies the source bridge that derives the comparator
conditions and transfers any hypothetical global comparator solution back to a
`GlobalFiniteEnergySolution`.

## Proof chain

1. `NavierStokesR3.theorem_1_1` supplies, for \(\nu>0\), the same velocity,
   pressure, force, support, and `CandidateProperties` package, together with
   `¬ Nonempty (GlobalFiniteEnergySolution ν f)`.
2. `CandidateProperties` contains the pre-singular smoothness, compact support,
   initial datum, incompressibility, residual equation, energy bound, and
   speed-unboundedness clauses.
3. `NavierStokesR3.comparator_of_breakdown` chooses \(u_0=0\), converts the
   selected force to the comparator representation, and proves Fefferman's
   force smoothness and decay condition from compact smooth support.
4. If a global comparator solution existed, `globalSolutionOfComparator` would
   construct a global whole-space finite-energy solution for the same force,
   contradicting the candidate's no-global-solution theorem.

## Exact declarations

- `NavierStokes/R3/ProblemStatement.lean:92-153`
- `NavierStokes/R3/ComparatorBridge.lean:22-88`
- `NavierStokes/R3/Theorem.lean:26-49`
- `NavierStokes/ComparatorR3Theorem.lean:37-44`
- `NavierStokesReview/src/completions/SelectedFeffermanAlternativeCProof.lean`

## Fresh kernel check

The completion was compiled with:

```text
lake env lean NavierStokesReview/src/completions/SelectedFeffermanAlternativeCProof.lean
```

The result was exit code 0. The printed axiom dependency was:

```text
[propext, Classical.choice, Quot.sound]
```

No `sorryAx` appeared in the successful run. The repository-wide build remains
blocked by the pre-existing user-owned syntax error at
`NavierStokes/R3/TestPressure.lean:6`; that file was not modified.

## What this proves, and what it does not

This proves the formal forced CMI (C) proposition as encoded by the repository.
It does not prove that every explanatory dependency in OpenAI's manuscript has
been formalised under the same definitions. In particular, the manuscript's
five-moment matching and correction mechanism is load-bearing, while the
public `Witness` proposition does not expose a separate final-Cartesian
identity identifying every such consequence. That is a distinct
paper-to-code fidelity question. It cannot be used to reverse the positive
Alternative (C) theorem into a contradiction without a direct selected-field
mismatch, an impossibility theorem, or failure of a mandatory CMI premise.
