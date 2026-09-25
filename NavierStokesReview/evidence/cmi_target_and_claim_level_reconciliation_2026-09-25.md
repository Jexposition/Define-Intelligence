# CMI target and claim-level reconciliation

## Finding

The inspected source supports two different review questions, which must not be
collapsed into one verdict.

1. Does the exported R³ theorem state the literal C/D proposition? **Yes, at
   the source level inspected.**
2. Does the source export the paper's entire five-moment construction as an
   identity for the final selected fields? **Not shown.**

The second finding is a paper-to-code correspondence objection. It is not,
without an additional field-level mismatch, a contradiction of the first.

## Fefferman target

The official problem statement defines alternatives (C) and (D) using a smooth
force satisfying the stated spatial and temporal decay conditions. It does not
add a formal predicate saying that the force must be independent of the
velocity as a functional object. The words “given, externally applied” describe
the PDE data; they do not by themselves add a Lean-level perturbation-stability
axiom to an existential alternative.

The whole-space target is explicit in
`NavierStokes/R3/ProblemStatement.lean`:

- `CompactPositiveTimeSupport` implies a compactly supported smooth force and
  therefore the required rapid decay;
- `CandidateProperties` requires smooth velocity and pressure on the
  pre-singular domain, incompressibility, the residual equation, zero initial
  velocity, bounded kinetic energy, and pointwise speed blow-up;
- `breakdownStatement` additionally requires nonexistence of a global smooth
  finite-energy competitor with the same force and datum.

## Selected endpoint

The endpoint chain is:

```text
ActualCandidateAssembly.selected_witness
  -> NavierStokesR3.ActualCandidate.selected_candidate_one
  -> NavierStokesR3.theorem_1_1_with_initial_rest
  -> NavierStokesR3.theorem_1_1
  -> ProblemStatement.breakdownStatement
```

The relevant source locations are:

| Source | Location | What it establishes |
|---|---:|---|
| `NavierStokes/R3/ActualCandidate.lean` | 79–118 | Localises the periodic candidate, preserves the residual equation, and supplies compact support and energy bounds. |
| `NavierStokes/R3/ActualCandidate.lean` | 130–145 | Extracts the selected whole-space candidate. |
| `NavierStokes/R3/Theorem.lean` | 27–53 | Scales the candidate to every positive viscosity and proves `breakdownStatement`. |
| `NavierStokes/R3/ProblemStatement.lean` | 83–150 | Defines the C/D target and the global competitor class. |

The recorded `#print axioms` result for the exported theorem contains only
`propext`, `Classical.choice`, and `Quot.sound`. The selected R³ theorem is
therefore not being rejected here for a hidden custom axiom or a missing
existential witness.

## Remaining paper-to-code objection

The OpenAI paper gives the five quantities

$$
(M,I,J,S,C_p)
$$

a load-bearing role in its construction. The source does contain genuine
five-moment definitions and upstream cancellation theorems:

- `PositiveOrderMoments.lean:76-85` defines the five rows;
- `GlobalSlowProfiles.lean:1043-1055` proves positive-order cancellation;
- `AssembledSlowBase.lean:592-617` uses that cancellation;
- `FiveRowRank.lean:241-284` and `MeanRankUpdate.lean:163-168` prove the
  constrained correction rows.

The selected export at `ActualCandidateAssembly.lean:1121-1151` does not state
an equality identifying the final mixed velocity, pressure, residual, or force
with those five quantities. That is a genuine correspondence and disclosure
gap. It is not the same as proving the literal C/D target false.

## Review consequence

The counter-paper must use a split conclusion:

- **Literal formal target:** established by the inspected R³ theorem, subject
  to the correctness of the imported analytic lemmas and definitions.
- **Published five-moment construction claim:** not independently established
  by the exported selected-field interface because the required composition
  theorem is not exposed.
- **Formal refutation:** not obtained by the residual-feedback, mirror-force,
  pressure-support, or generic moment-blindness arguments alone.

The burden remains on the authors to make the selected-field five-moment
transport explicit if that mechanism is part of the advertised proof. The
review must not convert that missing exposition/identification into a false
claim that the C/D theorem itself has already been contradicted.
