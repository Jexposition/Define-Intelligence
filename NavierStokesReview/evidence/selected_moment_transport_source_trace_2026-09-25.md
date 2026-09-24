# Selected-moment transport source trace

## Purpose

OpenAI's paper presents the five cumulative quantities
$$
(M,I,J,S,C_p)
$$
as load-bearing data: the moment equations remove the pressure and stress
tails and preserve the exterior profile. This record checks the actual source
path used by `ActualCandidateAssembly` against that published claim.

## Source ledger

| Source location | What is proved or constructed | Consequence for the published claim |
|---|---|---|
| `NavierStokes/PositiveOrderMoments.lean:76-85` | `rowDensity` has five entries and `moments` integrates those entries over `Ioi 0`. The entries are the radial velocity, angular profile, pressure-gradient, mixed Cauchy, and stress-correction terms. | The repository does contain a paper-shaped five-coordinate moment definition. The earlier claim that these formulas were absent or intrinsically mismatched is withdrawn. |
| `NavierStokes/GlobalSlowProfiles.lean:1043-1055` | `profiles_moments` proves the five actual total rows vanish for each positive order of the profile sequence. | The upstream slow-profile construction has a genuine five-row cancellation theorem. |
| `NavierStokes/AssembledSlowBase.lean:592-617` | `extended_axial_primitive_zero` uses `profiles_moments` to derive a zero primitive for the extended axial stream. | The five-row result is used in the assembled slow-base layer, not merely declared as dead code. |
| `NavierStokes/CorrectionInitialization.lean:1943-1976` | `zeroMean_debt_mem` bounds the three incoming debts obtained from the initial state's radial moments. | The three-debt rank interface is a real correction-layer interface, but it is not itself the paper's five-coordinate tuple. |
| `NavierStokes/ActualCandidateAssembly.lean:515-523` | `positivePotential` and `positivePressure` combine particular, signed, and mean-stage fields. | This is the selected mixed field boundary at which the upstream moment construction must be connected to the final candidate. |
| `NavierStokes/ActualCandidateAssembly.lean:531-534` | `potentialStages` passes `positivePotential` into `GermCandidateAssembly`. | The selected velocity stages are defined from the mixed field, not directly from `PositiveOrderMoments.moments`. |
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` requires the selected sums, extensions, a smooth force, `CandidateProperties`, `CandidateConsequences`, blow-up, decay, and endpoint jets. | The exported theorem contract does not contain a field-level equality identifying the selected velocity/pressure/residual/force with `(M,I,J,S,C_p)`. |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1185` | `selected_witness` supplies `Witness`; `selected_candidate` then extracts the generic candidate statement. | The public endpoint is connected to the selected construction, but the published five-moment semantics are not exported at this final boundary. |
| `NavierStokes/FiveRowRank.lean:21-22, 93-97` | `FiveRowRank.Debt` is `Fin 3 → ℝ`; its angular and axial correction vectors have fixed zero coordinates and three live debt coordinates. | A separate three-debt correction interface exists. A promotion map or shared label is not a proof that it equals the five moments used by the paper. |

## Closure result

The import closure rooted at `ActualCandidateAssembly` contains the upstream
five-moment and rank modules. The live objection is therefore not dead code,
unreachable imports, or an alleged absence of the five formulas.

The unresolved requirement is more specific:

> Prove, for the selected mixed fields in `ActualCandidateAssembly`, that the
> five radial integrals used by the paper are exactly the quantities whose
> vanishing is used in the residual, pressure, exterior, and force estimates.

The current `Witness` type does not state that equality. The existing
review-side interface probes prove only non-implication: the exported
`PhysicalData` contract can coexist with an arbitrary abstract five-debt
payload because that payload is not a field of the record. They do not prove
that the concrete selected integrals are numerically false.

## Publication consequence

OpenAI's paper claims a solution, not merely a library of useful lemmas. Since
the paper makes the five-moment cancellation part of the construction's
mathematical explanation, the missing selected-field transport theorem is a
load-bearing omission. On the present record, the advertised solution claim
is **NOT ESTABLISHED**. A direct Lean `False` theorem would be a stronger
result, but it is not necessary to withhold acceptance of an affirmative
solution claim whose stated mechanism is not connected to its exported
selected endpoint.
