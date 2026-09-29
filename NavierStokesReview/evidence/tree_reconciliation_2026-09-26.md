# Tree reconciliation

The extracted tree is an inventory snapshot. Current checkout paths are authoritative; unique basenames are used only to reconcile inventory entries, never to manufacture a path from an ambiguous name.

## Inputs

- Tree: `D:\Research Lab\Jexposition\tree-maker\Define inteligence tree.md`
- Tree SHA-256: `476cc9257bf6f3a8259fe78110bdcd9df170b8e265dabb6aeb13e850aa522d17`

## Counts

| Quantity | Count |
|---|---:|
| Tree entries | `3042` |
| Tree file entries | `3021` |
| Current checkout files | `3088` |
| Unique-basename resolutions | `2997` |
| Ambiguous basename entries | `24` |
| Missing current basenames | `0` |
| Duplicate current basenames | `11` |

## Interpretation

A resolved entry establishes only that the named file exists at the unique current path. It does not establish import reachability or theorem use. Ambiguous and missing entries are retained as review obligations.

## Ambiguous entries

- line `5` `Euler.lean`: `ComparatorChallenges/Euler.lean, Euler.lean`
- line `7` `NavierStokes.lean`: `ComparatorChallenges/NavierStokes.lean, NavierStokes.lean`
- line `8` `README.md`: `ComparatorChallenges/README.md, NavierStokesReview/README.md, NavierStokesReview/src/external-semantic/README.md, README.md`
- line `10` `Euler.lean`: `ComparatorChallenges/Euler.lean, Euler.lean`
- line `1831` `WeakTimeContinuity.lean`: `Euler/WeakTimeContinuity.lean, NavierStokes/R3/WeakTimeContinuity.lean`
- line `1852` `NavierStokes.lean`: `ComparatorChallenges/NavierStokes.lean, NavierStokes.lean`
- line `2022` `ComparatorBridge.lean`: `NavierStokes/ComparatorBridge.lean, NavierStokes/R3/ComparatorBridge.lean`
- line `2339` `ProblemStatement.lean`: `NavierStokes/ProblemStatement.lean, NavierStokes/R3/ProblemStatement.lean`
- line `2359` `ComparatorBridge.lean`: `NavierStokes/ComparatorBridge.lean, NavierStokes/R3/ComparatorBridge.lean`
- line `2432` `ProblemStatement.lean`: `NavierStokes/ProblemStatement.lean, NavierStokes/R3/ProblemStatement.lean`
- line `2441` `SchwartzCompactApproximation.lean`: `NavierStokes/R3/SchwartzCompactApproximation.lean, NavierStokes/SchwartzCompactApproximation.lean`
- line `2455` `WeakTimeContinuity.lean`: `Euler/WeakTimeContinuity.lean, NavierStokes/R3/WeakTimeContinuity.lean`
- line `2536` `SchwartzCompactApproximation.lean`: `NavierStokes/R3/SchwartzCompactApproximation.lean, NavierStokes/SchwartzCompactApproximation.lean`
- line `2672` `README.md`: `ComparatorChallenges/README.md, NavierStokesReview/README.md, NavierStokesReview/src/external-semantic/README.md, README.md`
- line `2862` `lake-manifest.json`: `lake-manifest.json, NavierStokesReview/src/audit/lean32-preflight/lake-manifest.json`
- line `2863` `lakefile.toml`: `lakefile.toml, NavierStokesReview/src/audit/lean32-preflight/lakefile.toml`
- line `2864` `lean-toolchain`: `lean-toolchain, NavierStokesReview/src/audit/lean32-preflight/lean-toolchain`
- line `2937` `README.md`: `ComparatorChallenges/README.md, NavierStokesReview/README.md, NavierStokesReview/src/external-semantic/README.md, README.md`
- line `2938` `deep_semantics_audit.md`: `docs/deep_semantics_audit.md, NavierStokesReview/src/external-semantic/deep_semantics_audit.md`
- line `3005` `README.md`: `ComparatorChallenges/README.md, NavierStokesReview/README.md, NavierStokesReview/src/external-semantic/README.md, README.md`
