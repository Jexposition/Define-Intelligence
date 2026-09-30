# Hardened source and logic map

This report is generated from the extracted tree and the current checkout. Paths, imports, and hashes are evidence; declaration token edges are diagnostic only until replaced by Lean environment metadata.

## Inventory

- Extracted tree: `D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github\docs\REPOSITORY_ARCHITECTURE_MAP.md`
- Tree SHA-256: `213e5411b7a6cc354220039bbe3ea5f8b46d67d9061304d3188421e6e1d22c09`
- Tree entries / unique basenames: `0` / `0`
- Current files / Lean modules: `3449` / `2797`
- Current declarations: `50208`
- Duplicate tree basenames: `0`; duplicate checkout basenames: `13`

## Endpoint module closure

Roots: `NavierStokes.ActualCandidateAssembly, NavierStokes.R3.ActualCandidate, NavierStokes.R3.Theorem, NavierStokes.ActualCandidateConstruction, NavierStokes.PositiveOrderMoments, NavierStokes.FiveRowRank, NavierStokes.MeanRankUpdate`
Resolved modules at depth `100`: `588`
Resolved import edges: `1648`
Missing project imports: `0`

## Interpretation rule

A module being reachable does not prove that a declaration is used by an endpoint. Conversely, a declaration-level source-token edge is not a kernel dependency. The final declaration closure must come from Lean environment metadata, followed by `#print axioms` on each load-bearing endpoint.

## Next machine check

Export the selected endpoint's declaration environment from the compiled Lean project, compare it with this source map, and investigate every edge involving `barMoment`, `FiveRows`, `selected_witness`, `navierStokesResidual`, and `pressure_support`.
