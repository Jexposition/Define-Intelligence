# Hardened source and logic map

This report is generated from the extracted tree and the current checkout. Paths, imports, and hashes are evidence; declaration token edges are diagnostic only until replaced by Lean environment metadata.

## Inventory

- Extracted tree: `D:\Research Lab\Jexposition\tree-maker\Define inteligence tree.md`
- Tree SHA-256: `476cc9257bf6f3a8259fe78110bdcd9df170b8e265dabb6aeb13e850aa522d17`
- Tree entries / unique basenames: `3021` / `3008`
- Current files / Lean modules: `3090` / `2790`
- Current declarations: `50191`
- Duplicate tree basenames: `11`; duplicate checkout basenames: `11`

## Endpoint module closure

Roots: `NavierStokes.ActualCandidateAssembly, NavierStokes.R3.ActualCandidate, NavierStokes.R3.Theorem, NavierStokes.ActualCandidateConstruction, NavierStokes.PositiveOrderMoments, NavierStokes.FiveRowRank, NavierStokes.MeanRankUpdate`
Resolved modules at depth `100`: `588`
Resolved import edges: `1648`
Missing project imports: `0`

## Interpretation rule

A module being reachable does not prove that a declaration is used by an endpoint. Conversely, a declaration-level source-token edge is not a kernel dependency. The final declaration closure must come from Lean environment metadata, followed by `#print axioms` on each load-bearing endpoint.

## Next machine check

Export the selected endpoint's declaration environment from the compiled Lean project, compare it with this source map, and investigate every edge involving `barMoment`, `FiveRows`, `selected_witness`, `navierStokesResidual`, and `pressure_support`.
