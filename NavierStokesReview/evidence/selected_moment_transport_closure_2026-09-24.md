# Selected-moment transport closure

**Date:** 2026-09-24
**Scope:** transitive local-import closure rooted at
`NavierStokes/ActualCandidateAssembly.lean`
**Purpose:** determine whether the five-moment construction is absent, or
whether it exists upstream without a theorem identifying it with the selected
mixed endpoint.

## Closure census

A read-only import traversal over local `NavierStokes.*` imports reaches 507
Lean modules from `ActualCandidateAssembly.lean`. Literal occurrence counts in
that closure are:

| Symbol or module name | Occurrences |
|---|---:|
| `PositiveOrderMoments` | 154 |
| `FiveProfileMoments` | 146 |
| `FiveRowRank` | 104 |
| `FiveRows` | 44 |
| `physicalMoments` | 42 |
| `CorrectionState.debt` | 44 |

This directly rejects the broad claim that the five-moment branch is globally
dead or absent from the selected import closure. It does not show that every
occurrence contributes to the final endpoint.

## Upstream identities that are actually proved

`NavierStokes/PositiveOrderMoments.lean:192-257` defines the five-coordinate
weighted density and proves `weighted_moments_exact`, `moments_repair`, and the
associated exact repair step. In particular, the five coordinates are actual
positive-radius integrals, not an uninterpreted vector.

`NavierStokes/FiveRowRank.lean:21` defines the runtime debt as
`Fin 3 → ℝ`. `FiveRowRank.FiveRows` at lines 241–247 is a conjunction of five
integral equations: two zero constraints followed by three debt equations.
`five_rows` then proves those equations for the constructed repair profiles.
The first two rows are therefore explicit equations, not axioms hidden in the
type of `Debt`.

`NavierStokes/MeanRankUpdate.lean:1226-1228` applies
`physical_five_rows` to the runtime family. `NavierStokes/CorrectionState.lean:453-476`
transports the rank rows to the actual base state through
`rank_model_rows` and `rank_rows_on_patch`. The active upstream construction
does carry genuine rank data.

`NavierStokes/ActualStageEstimates.lean:116-123` also consumes
`CorrectionState.debt` through `RunData.rank_class`. Thus the correct statement
is not that the production path never sees debt data.

## The selected endpoint boundary

`NavierStokes/ActualCandidateAssembly.lean:1121-1151` defines `Witness`. Its
result contains a schedule, three raw stage sequences, three away extensions,
a forcing field, `CandidateProperties`, `CandidateConsequences`, the H³
blow-up limit, force derivative decay, and endpoint boundary jets.

The result type does **not** contain an equality of the selected mixed sums
with any of:

* `PositiveOrderMoments.moments`;
* `FiveProfileMoments.physicalMoments`;
* `FiveRowRank.FiveRows`; or
* the paper tuple `(M, I, J, S, C_p)`.

`selected_witness` at lines 1177–1180 is only the instantiation of this
generic `Witness`. `GermCandidateAssembly.lean:192-266` constructs the same
kind of endpoint from stage estimates, localisation, extensions, and the
origin blow-up input; its result likewise exposes no five-moment equality.

The fact that `GermCandidateAssembly.lean` does not directly import the
five-moment files is therefore informative only about that interface boundary.
The transitive selected closure reaches the five-moment modules upstream.

## Falsification status

The source establishes a substantive paper-to-endpoint correspondence gap:
the upstream five-moment identities are real, but the inspected selected
endpoint does not expose the theorem that transports them into the final mixed
velocity, pressure, residual, force, and `VanishingJointJets` premises.

This is stronger than a documentation complaint because the missing theorem is
load-bearing for the paper's interpretation of the endpoint. It is not yet a
Lean proof of `False`: no actual selected field has been shown to violate a
five-moment identity, and the endpoint theorem does not state that identity as
a premise that can simply be contradicted.

## Required next theorem

The decisive source-level target is a theorem of the following shape, with the
actual selected sums rather than arbitrary placeholder fields:

```lean
theorem selected_mixed_moments_transport :
  PositiveOrderMoments.moments selectedOrder
    selectedHistoryU selectedHistoryE selectedProfile =
      paperMomentsOfSelectedFields ∧
  paperMomentsOfSelectedFields = promotedRuntimeDebt ... ∧
  selectedResidualAndForceUse promotedRuntimeDebt := by
  ...
```

If the repository supplies this theorem, CTR-005 is resolved at the
correspondence level and the audit must move to the theorem's analytic
premises. If the theorem is false for the concrete selected fields, a
zero-sorry counterexample to one of its equalities would be a genuine formal
refutation. Until then, the correct paper verdict is **not established as
claimed**, not “the five-moment branch is dead”.
