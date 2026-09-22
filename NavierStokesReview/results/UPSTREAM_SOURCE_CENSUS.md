# Upstream source census

Generated: `2026-09-22T12:22:40.736404+00:00`
Repository: `D:\Research Lab\Jexposition\Define Intelligence\NavierStokesReview\src\upstream-current`

This is a lexical and provenance census, not a proof verdict. Token counts include comments and strings; each candidate must be checked through imports and kernel output.

## Inventory

- Files: 2669 total, 2659 Lean, 2 Markdown.
- Manifest files: `formalization.yaml`, `lake-manifest.json`, `lakefile.toml`, `lean-toolchain`.

## Raw lexical totals

- `sorry`: 5
- `admit`: 1
- `axiom`: 11
- `opaque`: 1
- `unsafe`: 0
- `noncomputable`: 8486
- `#print axioms`: 4

## Main declaration locations

- `ComparatorChallenges/Euler.lean`: `euler_breakdown_R3` at line 85; `exists_compact_smooth_euler_singularity` at line 93; `exists_compact_smooth_euler_singularity` at line 170
- `ComparatorChallenges/NavierStokes.lean`: `navier_stokes_breakdown_R3` at line 45; `navier_stokes_breakdown_R3` at line 273; `navier_stokes_breakdown_periodic` at line 46; `navier_stokes_breakdown_periodic` at line 280
- `Euler/EulerSingularity.lean`: `exists_compact_smooth_euler_singularity` at line 133
- `Euler/Solution.lean`: `euler_breakdown_R3` at line 33; `euler_breakdown_R3` at line 73; `exists_compact_smooth_euler_singularity` at line 43; `exists_compact_smooth_euler_singularity` at line 75
- `NavierStokes/ComparatorR3Theorem.lean`: `navier_stokes_breakdown_R3` at line 38
- `NavierStokes/ComparatorSolution.lean`: `navier_stokes_breakdown_R3` at line 16; `navier_stokes_breakdown_R3` at line 20; `navier_stokes_breakdown_R3` at line 31; `navier_stokes_breakdown_periodic` at line 23; `navier_stokes_breakdown_periodic` at line 27; `navier_stokes_breakdown_periodic` at line 32
- `NavierStokes/ComparatorTheorem.lean`: `navier_stokes_breakdown_periodic` at line 47

## Downloaded copy versus current clone

- Old files: 2496
- Current files: 2669
- Added in current clone: 173
- Removed in current clone: 0
- SHA-256 changed common files: 2496

## Interpretation guardrails

1. A zero `sorry` count is not sufficient: the theorem statement, imports, definitions, and `#print axioms` output must all be inspected.
2. `axiom`, `opaque`, and `noncomputable` lexical hits require declaration-level classification; comments and documentation can produce false positives.
3. CMI alignment is separate from Lean soundness: a kernel-checked theorem can still formalise a weaker or different PDE problem.
