# Review mapping method

## Purpose

This method maps a large Lean repository without treating filenames, prose, or
identifier search as proof of theorem use. It keeps inventory, source
navigation, compiled reachability, and mathematical transport as separate
questions.

## Scoped reachability, not a validity judgement

`reachable` means reachable from the captured endpoint roots used for the current dependency audit. `unreachable` means not reached from those roots. The label is not synonymous with “dead code”, “irrelevant”, “not part of OpenAI’s formalisation”, or “not compiled by another target”. A file may be outside the selected Navier–Stokes endpoint closure while belonging to the companion Euler branch, a standalone comparator, an alternate theorem path, or an independent construction.

The full-review obligation therefore has two passes: (1) inspect the endpoint closure for transport into the public theorem; and (2) inspect every indexed module outside that closure for source content, paper correspondence, alternate entry points, admitted material, and isolation from the endpoint. Neither pass may silently substitute for the other.

## Authority order

1. **Inventory:** `D:\Research Lab\Jexposition\tree-maker\Define inteligence tree.md`
   is the captured tree snapshot. Its SHA-256 is recorded for reproducibility;
   its basename entries do not determine a current source path.
2. **Current contents:** the checkout supplies exact relative paths, byte
   counts, and SHA-256 hashes.
3. **Source navigation:** imports, namespace-aware declaration spans, and
   token references locate candidates. Token references are diagnostics only.
4. **Compiled reachability:**
   `EnvironmentDependencyExport.lean` follows elaborated `ConstantInfo`
   references from `NavierStokesR3.theorem_1_1`.
5. **Source join:**
   `join_environment_source_map.py` joins compiled names to source spans only
   by exact fully qualified declaration name. Ambiguous and unmatched nodes
   remain explicit uncertainty classes.
6. **Mathematical conclusion:** a field-level transport theorem must still be
   proved in Lean. Reachability of `FiveRows`, `barMoment`, or a pressure
   module is not such a theorem.

## Reproduction

Run:

```powershell
NavierStokesReview/src/audit/run_hardened_audit.ps1
```

The run regenerates the source map, Lean environment closure, exact-name join,
selected endpoint routes, and the validation bundle. The bundle records source
hash drift, required routes, reachable `sorryAx` users, and Git state.

## Current captured result

| Layer | Result |
|---|---:|
| Extracted-tree entries | 3,021 |
| Current checkout files | 3,058 |
| Lean modules | 2,790 |
| Source declarations | 50,191 |
| Source-token diagnostics | 186,194 |
| Compiled environment nodes | 30,721 |
| Compiled environment edges | 327,757 |
| Exact source-name matches | 22,958 |
| Ambiguous matches | 3 |
| Unmatched environment nodes | 7,760 |
| Joined edges | 227,128 |
| Reachable `sorryAx` users | 0 |

The selected routes reach `selected_witness`, `FiveRows`, both debt types,
`scaleDebt`, `periodicVelocity`, `barMoment`, and the R³ candidate packaging.
This removes any dead-code claim about those branches. The remaining CTR-005
obligation is value-level transport from the assembled Cartesian field through
localisation, curl, periodisation, summation, and radial observables.

## Tooling boundary

Lake is the build and target runner. Loogle is a theorem-search aid for finding
candidate Mathlib lemmas; it does not prove that a candidate lemma applies to
the selected field. Lean widgets and generated documentation can improve
navigation, but neither replaces the compiled environment export or a
zero-sorry transport theorem.

References: [Lake](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/),
[Loogle](https://loogle.lean-lang.org/), and
[Lean widget types](https://lean-lang.org/doc/api/Lean/Widget/Types.html).

## Inventory reconciliation and declaration queries

The tree-maker export is treated as an inventory snapshot, not as a path
authority. `tree_reconciliation.py` hashes the export, indexes the live
checkout, and resolves a tree entry only when its basename is unique in the
checkout. Ambiguous names remain unresolved instead of being assigned by
indentation heuristics. The captured run contains 3,021 tree file entries,
2,997 unique-basename resolutions, 24 ambiguous entries, and no missing
basenames. The live checkout contains 3,058 files.

`mapping_query.py` provides a bounded query layer over the exact source
declaration map and the compiled environment join. It reports source spans and
compiled dependency matches for a fully qualified declaration, but does not
infer theorem meaning. Raw compiled edges (327,757) and source-located joined
edges (227,128) are retained as separate observables.

Evidence: `NavierStokesReview/evidence/tree_reconciliation_2026-09-26.md` and
`NavierStokesReview/evidence/query_selected_witness_2026-09-26.md`.

## Claim register

`NavierStokesReview/config/review_claims.json` is the machine-readable
register for claims that depend on the map. `claim_register.py` validates
only structural prerequisites: source declarations, compiled routes, and
named evidence files. Its passing result supports MAP-001 and CTR-032,
records CTR-012 as conditional, and keeps CTR-005 open. It does not infer
field-level moment transport from reachability.

## Complete repository map

## External-tree structural profile

external_source_profile.py profiles every indexed Lean module outside the
currently captured endpoint closure. It records source hashes, imports,
declarations, marker families, and admitted-token locations, but it cannot
establish theorem meaning or prove that a marker participates in an endpoint.
Its rows must therefore remain labelled
structurally_profiled_not_semantically_reviewed until a direct source review
is recorded. This prevents endpoint closure metrics from being mistaken for
repository-wide coverage.

`repository_map.py` now consumes the source map, exact compiled-environment
join, and claim register to emit a complete catalogue rather than a route-only
report. Each current Lean module has a source hash, imports, declarations,
compiled declarations, endpoint status, and route membership.

The synchronized outputs are `hardened_source_map_2026-09-29.json` and `.md`,
with the exact endpoint closure recorded in
`direct_endpoint_closure_validation_2026-09-29.md`. The Markdown output is
the human reading view; the JSON is the machine evidence.
See `docs/REPOSITORY_MAP_GUIDE.md` for authority order and reproduction.

The complete map accounts for 2,790 of 2,790 Lean modules. A module outside
the selected endpoint environment is explicitly scoped endpoint information,
not a dead-code claim. Reachability remains distinct from semantic transport.
