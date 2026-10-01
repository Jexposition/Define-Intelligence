# Priority 241: A/B declaration closure and semantic-seam measurement

## Scope

This record is the first executed measurement under the Priority 241 control
lane. It treats the 8 September object
`8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538` as Submission A and the 10
September object `f9e8bc5b38b6e212696e8a30e3e91517af887bbd` as Submission B.
The source files were read directly from immutable Git objects. No OpenAI
source file was edited.

The machine-readable output is
`NavierStokesReview/evidence/priority_241_ab_declaration_closure_2026-10-01.json`.
The measurement script is
`NavierStokesReview/src/audit/ab_declaration_closure.py`.

## Measurement layers

Two graph types are kept separate.

1. **A/B source layer.** This follows project-local `import` edges from the
   headline C/D route modules and inventories declaration names using the raw
   source text. It is a reproducible source/provenance census, not an
   elaborated proof-term closure.
2. **Current B environment layer.** This follows the previously exported
   Lean declaration-use edges in
   `lean_environment_closure_ns_3d_2026-09-30.json`. It is stronger than an
   import graph, but it remains a declaration-use closure, not an independent
   semantic proof of the manuscript or a field-level observable identity.

The distinction matters mathematically:

\[
\text{import closure}
\subsetneq
\text{declaration-use closure}
\neq
\text{proof-term semantic closure}
\neq
\text{paper-to-field correspondence}.
\]

## Executed A/B result

| Layer | Submission A | Submission B | Interpretation |
|---|---:|---:|---|
| Route modules followed | 2 | 2 | C/D headline route roots |
| Source/import closure modules | 579 | 605 | B adds 27 modules and A has 1 module not in B |
| Shared source/import modules | 578 | 578 | Large common construction/import base |
| Source declaration names | 31,790 | 31,984 | Raw declaration census, not theorem validity |

The only A-only route module is `NavierStokes.ComparatorTheorem`. The 27 B-only
modules include the new paper-facing periodic route and R3 layers:

- `PeriodicPaperTheorem`, `PeriodicPaperSupport`,
  `PeriodicPaperScalingSupport`, `PeriodicViscosity`,
  `PeriodicViscosityUniqueness`, `PeriodizePDE`, and `PeriodizeLatticeCover`;
- `R3.Theorem`, `R3.ActualCandidate`, `R3.CandidateBreakdown`, and
  `R3.ComparatorBridge`;
- `R3.IntegratedDissipation`, `R3.ViscousEnergyBalance`,
  `R3.SharpEnergyBound`, `R3.ForceL2Norm`, `R3.ParabolicEnergy`,
  `R3.SpatialEnergyScaling`, `R3.SpatialCauchySchwarz`, and the associated
  parabolic, support, scaling, and delayed-extension modules.

This narrows the provenance question. The public route delta is not merely a
large undifferentiated tree: the source closure has a 578-module common base
and a 27-module B-only route expansion. It still does not determine whether
the B-only modules repair an A defect, strengthen an already available fact,
or aggregate a paper-facing statement.

## Current B elaborated-root result

The recorded environment closure contains no `sorryAx` nodes for the four
queried roots. Their declaration-use closure sizes are:

| Current B root | Declaration-use closure |
|---|---:|
| `NavierStokesR3.theorem_1_1` | 30,721 |
| `NavierStokes.ComparatorBridge.navier_stokes_breakdown_R3` | 30,771 |
| `NavierStokes.PeriodicPaper.periodic_corollary` | 30,840 |
| `NavierStokes.ActualCandidateAssembly.selected_witness` | 29,785 |

The direct environment references are also informative. The whole-space C
route calls `NavierStokesR3.theorem_1_1` and
`NavierStokesR3.comparator_of_breakdown`; the periodic route calls the R3
initial-rest theorem, parabolic scaling, periodisation, and
`CandidateProperties.no_global_solution`. `selected_witness` directly uses
`Witness`, the selected budget, selected threshold, and threshold geometry.
This confirms route composition, but a broad transitive closure containing
moment names is not the same thing as a selected field-level equality.

## Semantic interpretation

The measurement supports these statements:

1. A and B share a substantial source/import base.
2. B adds a targeted R3/paper-facing route layer containing explicit energy,
   force, periodisation, scaling, and comparison modules.
3. The current B headline roots resolve in the recorded elaborated environment
   without `sorryAx` nodes.
4. The current declaration-use closure is large enough that raw keyword hits
   cannot establish which exact theorem transports a manuscript observable.

It does **not** establish:

- that Submission A is false;
- that the B-only modules repair a known A failure;
- that A and B use definitionally or extensionally identical witness tuples;
- that the final selected Cartesian/localised/periodised/summed fields satisfy
  \(\operatorname{Obs}_{\rm paper}(u,p,f)=(M,I,J,S,C_p)\);
- reverse equivalence with Fefferman's complete specification;
- a selected nonzero defect, force nonsmoothness, literal CMI failure,
  impossibility theorem, compiler escape, or `False`.

The controlled scientific status therefore remains
**`CTR-005: NOT ESTABLISHED`** for complete paper-to-selected-endpoint
correspondence. The positive finding from Priorities 232--233 also remains:
the internal five-row/radial repair engine is consumed by the selected
production route and must not be called dead, generic, or bypassed wholesale.

## Next measurement

The next A/B task is not another keyword scan. It is to trace the exact
declaration references entering the C and D route roots, compare the witness
objects and premise directions, and identify which B-only declarations are
dominating route edges. In parallel, the selected-field transport, CUDA-first
3D commutator, pressure, energy, limit/interchange, and independent CMI lanes
remain open.
