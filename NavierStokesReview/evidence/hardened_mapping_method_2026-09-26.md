# Hardened source and Lean mapping method

## Purpose

This review uses two separate evidence layers. The extracted tree is the inventory baseline; the live checkout is the source-of-record for contents and hashes. A source-text reference is never treated as proof of Lean dependency reachability.

## Evidence layers

| Layer | Input | Output | Authority |
|---|---|---|---|
| A | `tree-maker/Define inteligence tree.md` plus the live checkout | path-aware file inventory, duplicate-name report, SHA-256 hashes, exact import resolution | file/path claims |
| B | current `.lean` source | declaration names, source imports, raw `axiom`/`sorry`/`unsafe`/`admit` flags, token-reference diagnostics | navigation only |
| C | compiled Lean environment after importing `NavierStokes.R3.Theorem` | `ConstantInfo` types/values, `Expr.getUsedConstants`, endpoint declaration closure | declaration dependency claims |
| D | `#print axioms` on named declarations | foundational/custom axiom report | axiom claims |

Layer B intentionally cannot certify elaborated references: notation, namespaces, macros, generated terms, and overload resolution make token matching insufficient. Layer C is therefore the load-bearing dependency graph for the selected endpoint.

## Reproduction

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File NavierStokesReview/src/audit/run_hardened_audit.ps1
```

The historical script produced the dated 2026-09-26 exports listed in the
original run record. The current reconciled outputs are:

- `NavierStokesReview/evidence/hardened_source_map_2026-09-29.json`
- `NavierStokesReview/evidence/hardened_source_map_2026-09-29.md`
- `NavierStokesReview/evidence/direct_endpoint_closure_validation_2026-09-29.md`
- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-29.json`

The Lean exporter is `NavierStokesReview/src/audit/EnvironmentDependencyExport.lean`. It starts at `NavierStokesR3.theorem_1_1`, follows project-namespace constants appearing in the elaborated type and value expressions, and records the referenced declaration names and types. External Mathlib declarations are intentionally excluded from the project closure and remain part of the toolchain/axiom audit.

## Recorded run

On 2026-09-26, the source mapper recorded 3,021 extracted-tree entries, 3,008 unique basenames, 3,047 live files, 2,790 current Lean modules, 50,191 source declarations, and 186,194 diagnostic token edges. The compiled endpoint exporter recorded 30,721 project declarations and 227,128 joined environment-to-source edges in the corrected join, with zero reachable nodes marked as using `sorryAx`.

The source-token edge count is a diagnostic index over source text. The compiled exporter records 327,757 raw environment edges; after exact source-span joining, 227,128 edges have both endpoints mapped to source declarations. These counts are not interchangeable. The compiled environment is the correct basis for elaborated declaration reachability; the joined edge count is the basis for source-located route reports.

## Exact source-span join

`join_environment_source_map.py` joins compiled declarations to source spans
only when their fully qualified declaration names match exactly. It records
three outcomes separately: one exact source match, more than one source match,
or no source match. Unmatched nodes are not guessed from basenames. This is
important because imported library declarations, generated declarations, and
namespace-normalised names may not have a source record in the project scan.

The corrected join contains 30,721 environment nodes, 22,958 exact source
matches, 3 ambiguous matches, 7,760 unmatched nodes, and 227,128 edges whose
two endpoints both have exact source spans. It marks zero joined nodes as
using `sorryAx`. The earlier lower join counts were caused by a namespace and
section parser defect and are superseded. These counts are a mapping
diagnostic, not a claim that unmatched nodes are absent or invalid.

## Selected endpoint route ledger

The compact route report is
`NavierStokesReview/evidence/selected_endpoint_routes_2026-09-26.md`.
It records exact compiled-environment paths from
`NavierStokesR3.theorem_1_1` to the selected witness, both debt interfaces,
`FiveRows`, `scaleDebt`, `barMoment`, mixed periodic velocity, the R³ packaging,
and `CandidateProperties`. The routes establish reachability. They do not by
themselves establish a value-level theorem identifying the paper’s five named
moments with the final Cartesian fields.

## Limits and review rules

1. A reachable declaration is not by itself a proof that the human paper’s interpretation is represented.
2. A missing source-token edge is not proof of semantic absence.
3. A zero `sorryAx` result is scoped to the exported environment closure and does not establish repository-wide metadata claims.
4. Source line locations still require a separate declaration-to-file locator; the environment graph establishes names and dependencies, not a source span for every elaborated constant.
5. Any claimed field-level contradiction must still be proved by a zero-sorry Lean theorem on the selected path.
6. A source span joined to an endpoint declaration identifies where the
   declaration is written; it does not prove that the declaration's informal
   interpretation matches the paper.

## Tooling basis

The method follows Lean’s documented environment API (`Environment.find?`,
`ConstantInfo`, and expression constant extraction) and Lake’s project/build
model. `doc-gen4` is suitable for a human-readable declaration catalogue, but
it is a presentation layer, not a replacement for the compiled dependency
export. `lake check --paranoid` is a useful additional replay gate where the
platform supports it; it does not replace source-to-paper transport proofs.

## Inventory reconciliation and bounded queries

`tree_reconciliation.py` compares the extracted tree with the live checkout
using hashes and unique-basename resolution. The captured run has 3,021 tree
file entries, 2,997 unique resolutions, 24 ambiguities, and zero missing
basenames. `mapping_query.py` reports source spans and exact compiled joins
for a fully qualified declaration. Neither tool promotes an ambiguous path,
token match, or dependency edge into a semantic theorem.
