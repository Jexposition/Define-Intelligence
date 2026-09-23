# Selected endpoint incompressibility audit

## Result

The proposed attack on `selectedPotentialStages` does not currently produce a
formal failure. Those objects have type `ℕ → VelocityField`, but they are
intermediate potential fields. The selected CMI obligation is imposed on the
final velocity field returned by the witness, not on each raw potential stage.

The source path is:

1. `SolenoidalDiagonal.velocitySum` constructs the velocity from the stage
   data.
2. `SolenoidalDiagonal.divergence_velocitySum_on` proves zero spatial
   divergence under the stated openness, positivity, smoothness, and schedule
   hypotheses.
3. `CandidateProperties.divergence_free` records the corresponding property of
   the selected final candidate.

The zero-sorry probe
`NavierStokesReview/src/probes/SelectedDivergenceAudit.lean` compiles and
extracts the selected witness from
`ActualCandidate.selected_candidate_one_with_early_zero`, then returns
`hc.divergence_free` as the required divergence theorem. Its compiler output is
stored in
`NavierStokesReview/results/selected_divergence_audit_2026-09-23.txt`.

## Adjudication

This closes the narrow claim that the selected endpoint is visibly
compressible merely because the raw potential stages were not separately shown
to be divergence-free. A direct theorem asserting zero divergence of every
potential stage would test the wrong semantic object.

This does not independently validate the analytic estimates, pressure
construction, endpoint limits, or paper-to-code moment correspondence. A
formal refutation still requires a zero-sorry contradiction on one of those
mandatory selected-path obligations.

**Status:** raw-stage divergence objection closed; final-candidate
incompressibility confirmed on the exported witness path.
