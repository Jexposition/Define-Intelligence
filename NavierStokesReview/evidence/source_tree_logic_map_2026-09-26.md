# Source-tree and logic map

Status: current inventory and dependency map. It is not, by itself, a proof of a semantic mismatch or a derivation of `False`.

## Inventory authority

- Extracted inventory: `D:/Research Lab/Jexposition/tree-maker/Define inteligence tree.md`.
- Current-content authority: the checked-out filesystem and the `import` declarations in the Lean files.
- The extracted tree has 3,021 file entries and 3,008 unique basenames. The current checkout has 3,029 files excluding `.git` and `.lake`, including 2,788 Lean modules.
- The tree records both `NavierStokes/R3/` implementation modules and root-level `NavierStokes/R3*.lean` wrappers. These are distinct paths, not duplicate claims about one file.
- The inventory/parser output is machine-readable at `source_tree_logic_map_2026-09-26.json`; it records imports, declarations, symbol hits, and a bounded dependency subgraph.

## Current path map

| Layer | Current source path | Role | Anchors |
|---|---|---|---|
| Problem contract | `NavierStokes/ProblemStatement.lean` | Defines `navierStokesResidual`, `CandidateProperties`, and `candidateStatement`. | residual 81–85; properties 101–114; existential statement 120–122 |
| Candidate assembly | `NavierStokes/ActualCandidateAssembly.lean` | Builds the physical data, stage fields, witness, and selected stage aliases. | stage definitions 531–540; `Witness` 1121; witness 1153; selected aliases 1165–1173; `selected_witness` 1177 |
| Candidate construction | `NavierStokes/ActualCandidateConstruction.lean` | Supplies the construction-side cycle, debt, state, and mixed assembly inputs. | import/declaration map in JSON; inspect source before assigning field-level semantics |
| R3 packaging | `NavierStokes/R3/ActualCandidate.lean` | Converts the periodic/local candidate into whole-space candidate properties and selects the exported fields. | `of_localized_fields` 78–122; selected candidate 127–139 |
| R3 endpoint | `NavierStokes/R3/Theorem.lean` | Exports the existential C/D statements and the dissipation package. | `theorem_1_1` 46–49; dissipation theorem 66–79 |
| Pressure recovery | `NavierStokes/R3/PressureRecovery.lean` | Proves comparison pressure-gradient identities against compact smooth tests under explicit comparison hypotheses. | recovery 388–438; no absolute selected-pressure representative is introduced in this module |
| Pressure flux | `NavierStokes/R3/ActualPressureFlux.lean` | Converts the comparison pressure difference into a canonical Riesz-pairing flux identity. | 36–58; all compact-support assumptions shown are test/cutoff assumptions |
| Five-moment layer | `NavierStokes/PositiveOrderMoments.lean`, `FiveProfileMoments.lean` | Defines five-coordinate debt/moment and repair machinery. | `Debt := Fin 5 → ℝ` in `PositiveOrderMoments`; exact anchors are in the JSON symbol/declaration index |
| Runtime rank layer | `NavierStokes/FiveRowRank.lean`, `MeanRankUpdate.lean` | Defines the rank/update interfaces used by construction-side modules. | imports and reachable edges are recorded in the JSON map |
| Radial audit layer | `NavierStokesReview/src/completions/` | Review-side definitions and conditional theorems for the Cartesian-to-radial observable route. | mixed `barMoment` linearity, torus-average reduction, radial periodicity, and finite-prefix scope files |

## Exported contract versus upstream machinery

The root contract is explicit. `CandidateProperties` exports smoothness, spatial periodicity, zero initial velocity, positive-time force support, divergence-freeness, the residual equation, and unbounded speed. It does not contain fields named `M`, `I`, `J`, `S`, or `C_p`, nor a theorem asserting that the five radial moments of the exported Cartesian fields equal the upstream debt coordinates.

The R3 wrapper does prove the concrete candidate properties. In particular, `of_localized_fields` constructs the force as `PositiveTimeForce.force (R3CompactCandidate.compactForce f)` and proves the residual equality, smoothness, support, divergence, and finite-energy bound. The exported theorem then obtains the witness through `ActualCandidateAssembly.selected_witness` and packages it into the R3 contract.

This establishes a precise audit target:

$$
\text{upstream five-moment data}
\longrightarrow
\text{selected Cartesian }(u,p,f)
\longrightarrow
\text{exported }\texttt{CandidateProperties}
$$

The source map locates the first and last layers. It does not find, and does not claim to have found, a field-level theorem transporting the five named moments through the selected infinite assembly. That theorem remains the proof target under CTR-005.

## Pressure-chain classification

`PressureRecovery.pressure_gradient_recovery` assumes two velocity fields, two pressure fields, divergence hypotheses, equal residuals, and uniform finite energy. It proves a gradient-difference identity tested against compactly supported spatial functions. `ActualPressureFlux.pressure_flux_eq_canonical` uses that comparison result to identify a pressure-difference flux. These are active, typed comparison theorems.

They should not be described as absent pressure mathematics. Conversely, their signatures do not by themselves provide an absolute global statement that the selected pressure is the canonical representative determined by the selected velocity through a whole-space Poisson/Leray construction. Any such objection must therefore be stated as a missing selected-path semantic theorem, not as a contradiction from compact support alone.

## Concrete proof route still open

The review-side radial route currently proves only conditional or finite-prefix facts:

1. the mixed production scalar splits into potential and direct branches;
2. `barMoment` is additive when the required integrability/shell premises are supplied;
3. the torus average reduces to the radial pullback for the audited representative;
4. periodicity plus a bounded radial support premise forces a scalar representative to vanish;
5. finite cutoff prefixes eventually become active near the endpoint.

The missing load-bearing step is an exact value or sign for the complete selected mixed weighted integral, or a source-backed theorem that makes the required premises true for the complete infinite sum. No `Δm ≠ 0`, selected five-moment failure, or kernel-level `False` is claimed until that step is proved without `sorry`.

## Reproduction

From the repository root:

```powershell
python NavierStokesReview/src/audit/source_tree_map.py `
  --repo . `
  --tree 'D:\Research Lab\Jexposition\tree-maker\Define inteligence tree.md' `
  --output NavierStokesReview/evidence/source_tree_logic_map_2026-09-26.json `
  --depth 2
```

The parser excludes `.git` and `.lake`, parses only explicit Lean `import` lines and top-level declaration forms, and treats basename differences as diagnostic rather than path identity.

## Full transitive closure refresh

The same parser was rerun at import depth `100` against the extracted tree supplied from `tree-maker`:

```text
NavierStokesReview/evidence/source_tree_full_logic_map_2026-09-26.json
```

The refresh records 2,788 Lean modules, 797 modules reachable from the seven audit roots, and 2,378 import edges. No reachable import beginning with `NavierStokes` is missing from the current checkout. The remaining reported missing imports are library modules outside this repository scan, not missing repository source files. The four root R3 wrapper modules are present and mapped separately from their `NavierStokes/R3/` implementation modules.
