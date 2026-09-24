# Navier–Stokes CMI review lane

This branch is the review workspace for the fork `Jexposition/Define-Intelligence`.
The upstream Lean source is the repository root (`NavierStokes/`, `Euler/`, and
`ComparatorChallenges/`). The downloaded comparison tree remains preserved at
`D:\Research Lab\Jexposition\Define Intelligence\NavierStokesAndEuler-main-open Ais solution`.

## Git snapshot

- Branch: `review/cmi-first-navier-stokes-2026-09-22`
- Base commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
- Review setup commit: `1bdc04e`
- Remote: `https://github.com/Jexposition/Define-Intelligence.git`

## Layout

- `src/audit/`: review scripts and non-upstream Lean harnesses.
- `src/probes/`: independent theorem and axiom probes.
- `src/completions/`: separate zero-sorry theorems that expose missing
  transport obligations or prove conditional obstructions without modifying
  the upstream construction.
- `evidence/`: manifests and source-level audit records.
- `results/`: retained census, proof-path, and probe outputs.
- `../docs/`: CMI plan, axiom ledger, audit tracker, and research paper.

The repository source is not edited by the review. Generated `.lake`, `build`,
Lean object, cache, and virtual-environment files are excluded by the root
`.gitignore`.

The current counter-paper target is CTR-005. The production cycle does prove
two local radial mass constraints, but the exported `Witness` does not expose
their identification with the paper's five moments. A formal disproof still
requires a zero-sorry contradiction on that selected endpoint.
