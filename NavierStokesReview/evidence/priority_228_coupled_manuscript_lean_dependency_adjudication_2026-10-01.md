# Evidence: coupled manuscript-to-Lean dependency adjudication

This evidence record accompanies
`../src/audit/priority_228_coupled_manuscript_lean_dependency_adjudication_2026-10-01.md`.

## Result

The repair engine is **not bypassed wholesale**. The live production source
positively traces actual five-row/rank correction results into the actual cycle
invariant, residual-rate construction, selected schedule, smooth force
extension, and the selected witness.

The repair engine is also **not shown fully transported** to the manuscript's
named final observables. No inspected production declaration was found that
identifies the completed selected Cartesian/localised/periodised/summed fields,
pressure, residual, and force with the manuscript's
`(M,I,J,S,C_p)` tuple and is consumed by `selected_witness`.

The controlled classification is therefore:

```text
internal repair integration:       ESTABLISHED
whole selected-field transport:    NOT ESTABLISHED
wholesale bypass:                  NOT SUPPORTED
concrete nonzero defect:           NOT PROVED
literal CMI failure:               NOT PROVED
```

## Positive source anchors

| Anchor | What it proves |
|---|---|
| `NavierStokes/DefectIncrementBounds.lean:635-682` | Five-row hypotheses prove two mass-preservation identities and three solved linear rows for the actual correction increment. |
| `NavierStokes/DefectIncrementBounds.lean:714-823` | The actual `rankStage` debt is identified with the updated defects, and the solved rows give the stronger remainder/debt statements. |
| `NavierStokes/CorrectionStep.lean:9408-9448` | The actual cycle invariant stores representation, residual, debt, primitive regularity, and exact masses together. |
| `NavierStokes/ActualCycleResidualBounds.lean:1150-1208` | The residual-rate theorem consumes the actual invariant and physical fields; the finite-stage theorem feeds those rates into the mixed assembly. |
| `NavierStokes/ActualStageEstimates.lean:350-429` | `stageEstimates_of_representations` constructs finite residual estimates from actual representations and calls `finite_residual_rates`; it does not take output residual estimates as a free premise. |
| `NavierStokes/GluedStageEstimates.lean:684-755` | The actual glued stage-estimate constructor consumes physical data and returns the concrete `StageEstimates` used by the candidate route. |
| `NavierStokes/LocalResidualFlatness.lean:88-141` | The selected schedule and all-order residual jet rates are derived from the stage-estimate record. |
| `NavierStokes/CandidateFromLimits.lean:33-118` | Smooth force and agreement with the activated residual are derived from actual residual limits and derivative recurrence. |
| `NavierStokes/ActualCandidateAssembly.lean:1079-1185` | Actual physical data and estimates feed the selected sums and the exported witness; `Witness` includes the actual activated fields, force, candidate consequences, decay, and boundary jets. |
| `NavierStokes/NominalProfile.lean:2079-2111,2536-2576` | The profile-level five-moment certificate is real, with exact integrability, zero-moment, pressure-datum, and matching statements. |
| `NavierStokes/FiveRowRank.lean:241-318` | The runtime rank layer has two exact zero rows and three debt rows, with compactly supported exact repair. |

## Negative endpoint finding

`ActualCandidateAssembly.Witness` contains the selected schedule, `ASum`,
`BSum`, `PSum`, away extensions, forcing, candidate properties, smooth force,
candidate consequences, H3 blow-up, derivative decay, and boundary limits.
It does not contain a field or premise of the form

\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  =(M,I,J,S,C_p).
\]

`DefectIncrementBounds.barMoment_apply` proves a lower-level torus-averaged
radial integral formula, but the inspected production chain does not continue
that formula through the selected `potentialSum`, mixed curl/localisation,
periodisation, activation, pressure, and force objects to a final five-tuple
identity.

This is a correspondence gap, not a value-level counterexample. The AX-033
style probes show only that an abstract debt parameter is absent from the
`Witness` contract; they do not identify that abstract parameter with the
selected physical integrals.

## Manuscript cross-check

The manuscript itself makes the dependency non-optional. Its Sections 4.2,
5, 8, 9 and Appendix A use the five profile integrals for exterior matching,
stress-tail removal, modulation restoration, and the two-plus-three correction
cycle. It also explicitly retains the curl, cutoff, nonlinear, and pressure
terms in the full residual. Therefore the correct criticism is not “the
moments are decorative” and not “the repair code is absent”. It is that the
source record currently establishes the internal repair/residual route more
strongly than it establishes the final semantic identification claimed by the
paper-level exposition.

## No stronger conclusion

This record does not prove:

- a nonzero selected moment defect;
- failure of force smoothness;
- a compiler cheat or hidden axiom;
- impossibility of a transport theorem;
- literal failure of Fefferman Alternative (C) or (D);
- `False` in Lean.

It does establish the adverse review finding that the complete
manuscript-to-selected-endpoint five-observable correspondence is not
established on the inspected production record.

## Reproduction

The source spans above were re-read from the private review checkout on
2026-10-01. The endpoint/axiom and selected-path compiler records remain those
linked from Priorities 212, 222, and 227. No OpenAI source file was edited.

The fresh hardened source census is
`priority_228_selected_transport_census_2026-10-01.md` with JSON at
`priority_228_selected_transport_census_2026-10-01.json`. It indexed 31,838
declarations, found 11 joint candidates and 3 manual candidates, all in the
review tree. It supplied no Lean environment closure, so it is source triage,
not a kernel nonexistence result.

The pinned replay compiled these six existing review/audit files with exit
code 0 under `leanprover/lean4:v4.34.0-rc2`:

- `SelectedEndpointMomentTransportObstruction.lean`
- `SelectedWitnessPathProbe.lean`
- `GlobalTransportBridgeProbe.lean`
- `ActualMomentPreservationTrace.lean`
- `SelectedMixedRadialAxisZero.lean`
- `WholeSpaceAxiomAudit.lean`

The axiom output for the queried endpoint roots was limited to
`propext`, `Classical.choice`, and `Quot.sound`. No `elan` or `lake` process
remained after the replay.
