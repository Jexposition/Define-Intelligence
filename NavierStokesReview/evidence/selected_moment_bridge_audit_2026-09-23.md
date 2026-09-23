# Selected-stage moment bridge audit

Date: 2026-09-23  
Repository: `Jexposition/Define-Intelligence`  
Branch: `review/cmi-first-navier-stokes-2026-09-22`  
Method: source inspection plus a zero-sorry Lean diagnostic probe

## Question

Does the selected endpoint use the five integral moment-repair system described in the paper, or are the first two zero-moment rows merely imposed as type-level data?

## Result

The “zero rows are hardcoded by definition” accusation is not supported by the source.

`NavierStokes/FiveRowRank.lean` defines `FiveRowRank.FiveRows` as a conjunction of five explicit integral equations. The first two equations are mass/zero-moment integrals, and `five_rows_on_patch` and `five_rows` prove them from the constructed repair functions. `CorrectionState.rank_rows_on_patch` and `DefectIncrementBounds.RankGeometry.fiveRows` further connect the rank rows to actual slow base fields and propagate mass preservation.

`NavierStokes/PositiveOrderMoments.lean` separately defines a `Fin 5 → ℝ` debt from actual radial integrals and proves exact five-moment repair through `exists_parameterized_exact_repair`.

The remaining problem is endpoint transport. `ActualCandidateAssembly.selected_witness` has result type `ActualCandidateAssembly.Witness ...`. The selected stage aliases have types

```text
ℕ → ProblemStatement.VelocityField
ℕ → ProblemStatement.VelocityField
ℕ → ProblemStatement.PressureField
```

The `Witness` result exposes a schedule, sums, smooth forcing, candidate properties, blow-up, decay, and boundary limits. The selected endpoint does not expose a `FiveRowRank.FiveRows` equality, a `PositiveOrderMoments.moments` equality, or a theorem identifying the paper’s `(M, I, J, S, C_p)` with `CorrectionState.debt` on those selected fields.

This is a material paper-to-code correspondence gap. It is not yet a formal contradiction: the absence of an exposed transport theorem does not prove that no transitive construction can supply the same mathematics. A formal disproof still requires either a false mandatory equality or a countermodel showing that the selected endpoint can satisfy its stated type while the claimed paper moment identities fail.

## Reproducible evidence

- `NavierStokesReview/src/probes/SelectedMomentBridgeAudit.lean` imports the selected assembly and both moment modules, prints their exact types, and proves by `rfl` that the selected names are raw stage aliases.
- It compiles with Lean `v4.34.0-rc2` through the workspace Lake environment.
- `NavierStokes/ActualCandidateAssembly.lean:1165-1185` contains the selected aliases and `selected_witness`.
- `NavierStokes/FiveRowRank.lean:241-310` contains the explicit five integral rows and their repair theorems.
- `NavierStokes/CorrectionState.lean:462-476` and `NavierStokes/DefectIncrementBounds.lean:775-813` contain the actual rank-row bridges.
- `NavierStokes/PositiveOrderMoments.lean:23` and `:916-960` contain the five-integral debt and exact repair theorem.

## Review consequence

Do not call the `FiveRows` zero equations “assumed by definition.” Require a source-linked theorem that transports the proved moment system to the selected endpoint. Until that theorem is shown, the paper’s claimed correspondence remains unverified; the formal endpoint remains not formally refuted by this test.

