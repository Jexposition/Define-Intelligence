# Exported result path map

Snapshot under review: public commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

This map records where the exported declarations obtain their content. It is a provenance map, not a correctness verdict.

## Whole-space Navier–Stokes

`NavierStokes.Comparator.navier_stokes_breakdown_R3`

→ `NavierStokes.ComparatorR3Theorem.navier_stokes_breakdown_R3`

→ `NavierStokes.R3.theorem_1_1` and `NavierStokes.R3.comparator_of_breakdown`

→ `NavierStokes.R3.ActualCandidate` construction and `R3.ProblemStatement` definitions.

The review must check that the candidate force is smooth and satisfies the CMI force conditions, that the initial velocity is smooth and divergence-free with the stated decay, and that the excluded global solution class is at least as strong as the CMI class rather than weaker.

## Periodic Navier–Stokes

`NavierStokes.Comparator.navier_stokes_breakdown_periodic`

→ `NavierStokes.ComparatorTheorem.navier_stokes_breakdown_periodic`

→ `PeriodicPaper.periodic_corollary`

→ periodic candidate, compression, parabolic scaling, and periodisation modules.

The review must separately check periodicity of velocity, pressure, and force, the initial-data and forcing quantifiers, and whether the final global-solution predicate matches the periodic CMI alternative.

## Euler result

`Euler.euler_breakdown_R3` and `Euler.exists_compact_smooth_euler_singularity`

→ `Euler.Solution`

→ `Euler.BaseInductionStageNoOptions` and the maximal-lifespan contradiction chain.

This is recorded as a separate mathematical result. Euler is not itself one of the Clay Navier–Stokes prize alternatives, so it cannot substitute for the Navier–Stokes CMI audit.

## Separate challenge files

`ComparatorChallenges/NavierStokes.lean` and `ComparatorChallenges/Euler.lean` contain intentional `sorry` placeholders in reference challenge statements. They are not treated as part of the exported theorem path unless the import graph or kernel dependency output proves otherwise.

## Required proof checks

1. Finish the declared Lean 4.34.0-rc2 build from a clean current clone.
2. Compile `src/probes/AxiomProbe.lean` against the built current clone.
3. Record the exact `#print axioms` sets and check for `sorryAx`, native-evaluation axioms, or custom axioms.
4. Compare each theorem’s actual proposition with the official CMI alternatives C and D.
5. Only then classify each route as aligned, misaligned, or unresolved.
