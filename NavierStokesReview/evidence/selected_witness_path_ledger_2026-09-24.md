# Selected-witness path ledger

Date: 2026-09-24
Status: active falsification lane; no selected-field contradiction has yet been proved.

## Exact endpoint path

| Source | Footprint | Audit consequence |
|---|---|---|
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` quantifies a schedule, three away extensions, a force, periodic `CandidateProperties`, force smoothness, consequences, H3 blow-up, force decay, and boundary jets. | The proposition contains no `PositiveOrderMoments.Debt`, `moments`, `FiveRows`, or equality connecting those objects to the fields. |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1185` | `selected_witness` is obtained from `witness`; `selected_candidate` projects only the fields and `CandidateProperties`. | The public endpoint erases the construction schedule and all auxiliary transport data at the existential projection. |
| `NavierStokes/R3ActualCandidate.lean:18-21` | `selected_compact_candidate` applies `R3CompactCandidate.of_localized_fields` to the selected periodic candidate. | The whole-space object is a localisation wrapper, not a five-moment transport theorem. |
| `NavierStokes/R3/ActualCandidate.lean:78-122` | `of_localized_fields` preserves the residual identity, divergence-free property, support, energy, and blow-up while replacing the force by `PositiveTimeForce.force (compactForce f)`. | The force is permitted to absorb the residual after localisation; no pressure-Poisson or five-moment premise is introduced. |
| `NavierStokes/R3/Theorem.lean:26-62` | `theorem_1_1` and `candidateStatement` consume only the R3 `CandidateProperties` record. | The final R3 theorem does not consume `PositiveOrderMoments`, `FiveProfileMoments`, or `FiveRowRank` data. |

## Zero-sorry probe results

`NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean` compiles with no `sorry` and proves:

1. the selected periodic candidate properties are exported;
2. the selected path reaches the R3 envelope through localisation;
3. that R3 envelope can be paired with a nonzero five-coordinate debt because the debt is absent from the envelope type.

This is a type-level noninterference result. It does not prove that the selected velocity has a nonzero physical debt. The unresolved theorem is field-level:

$$
\text{selected five physical moments}
  = \text{promoted runtime debt}
\quad\text{or its negation.}
$$

## Active attack obligations

- **Force jets:** derive a lower bound on a selected component of `navierStokesResidual` that cannot be cancelled by pressure or viscosity, contradicting the supplied `hlim` family. `SpeedUnboundedAtOne` alone is insufficient.
- **Pressure:** prove the selected fields satisfy the global pressure-Poisson/Leray equation, then test whether compact localisation is compatible with that equation. The current support predicates do not provide this equation.
- **Moments:** connect the actual selected fields to the five integrals in `PositiveOrderMoments.rowDensity` or `FiveProfileMoments.physicalMoments`; only then can the three-debt promotion be used in a contradiction.

## Verdict boundary

The selected-witness path is formally inhabited and its exported types are weaker than the paper's five-moment narrative. That is a load-bearing correspondence failure. It is not yet a kernel-certified `False` theorem about the selected fields.
