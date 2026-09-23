# Selected-endpoint composition audit

## Result

The source contains two related but distinct composition layers. The local
paper layer uses the selected raw-stage aliases and an explicit schedule. The
exported whole-space CMI endpoint is obtained from `ActualCandidateAssembly.Witness`
and then localised by `R3.ActualCandidate`. The repository proves that these
layers can be combined, but the inspected declarations do not provide a
single theorem identifying the paper's named five-moment data, the local
schedule, the exported force, and the final R³ candidate as one common object.

This is a correspondence failure to be repaired in the paper. It is not a
kernel contradiction to `selected_candidate`.

## Source map

| Layer | Source | What is actually stated |
|---|---|---|
| Raw selected stages | `NavierStokes/ActualCandidateAssembly.lean:1163-1175` | Three stage-history aliases are defined from the selected budget and threshold. |
| Exported witness | `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` existentially chooses a schedule, away extensions, force, `CandidateProperties`, generic consequences, growth, decay, and boundary jets. |
| Exported candidate | `NavierStokes/ActualCandidateAssembly.lean:1177-1185` | `selected_candidate` extracts a candidate from `selected_witness`; it does not mention the local paper theorem or a five-moment debt equality. |
| Local paper schedule | `NavierStokes/LocalResidualFlatness.lean:111-125` | A schedule is selected for the raw aliases and residual-rate statements. |
| Local paper properties | `NavierStokes/LocalPaperTheorem.lean:128-183` | Local properties are proved for the supplied schedule and selected raw-stage aliases. |
| Local-to-compact packaging | `NavierStokes/PaperLocalization.lean:28-45` | The combined theorem gives local velocity/pressure agreement on an open set for late times; its result does not state force equality or a five-moment identity. |

## Audit consequence

The earlier claim that the five-moment module was globally dead code was too
strong. The local layer consumes the selected aliases, and the repository also
contains a genuine positive-order five-component repair. The defensible
objection is narrower: the public endpoint needs an explicit transport theorem
showing that the named `(M, I, J, S, C_p)` quantities survive the move from the
local repair layer through the selected schedule, residual estimates, force,
and R³ comparator.

## Formal probe

`NavierStokesReview/src/probes/ActualCandidateAssemblyIsolationProbe.lean` was
corrected to record this type boundary without claiming that
`PositiveOrderMoments` is dead code. The probe is zero-sorry and is evidence
about the exported proposition's interface, not a substitute for the missing
transport theorem.
