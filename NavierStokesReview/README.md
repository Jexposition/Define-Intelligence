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
- `evidence/`: manifests and source-level audit records.
- `results/`: retained census, proof-path, and probe outputs.
- `../docs/`: CMI plan, axiom ledger, audit tracker, and research paper.

The repository source is not edited by the review. Generated `.lake`, `build`,
Lean object, cache, and virtual-environment files are excluded by the root
`.gitignore`.
