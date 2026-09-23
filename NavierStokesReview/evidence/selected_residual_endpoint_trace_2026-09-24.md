# Selected residual endpoint trace

**Scope:** `ActualCandidateAssembly.selected_witness` and the premises used to
construct its force and blow-up conclusions.

## Result

The selected path does derive a joint residual-limit premise from the generic
stage estimates. The source does not, however, expose a theorem saying that
the paper's five moment quantities are the quantities whose residual is being
flattened. This is a live correspondence objection, not yet a contradiction
to the selected theorem.

## Dependency chain

1. `MixedCandidateAssembly.StageEstimates` (`MixedCandidateAssembly.lean:29-65`)
   records smoothness, raw stage bounds, finite background JetRates, and finite
   residual JetRates. It has no fields for `(M, I, J, S, C_p)`.

2. `StageEstimates.exists_schedule`
   (`MixedCandidateAssembly.lean:67-91`) calls
   `MixedDiagonalResidual.exists_physical_schedule_residual_zero` and returns
   a scale sequence together with
   `VanishingJointJets` for the mixed residual.

3. `MixedDiagonalResidual.physical_vanishingJointJets`
   (`MixedDiagonalResidual.lean:168-195`) derives the joint jet limit from a
   positive-order `JetRate` and the fact that the physical scale tends to zero.
   The proof is rate-based; its hypotheses contain no named moment tuple.

4. `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`
   (`GermCandidateAssembly.lean:223-271`) consumes the schedule result as
   `hz`, constructs away extensions, and passes `hz` to
   `CandidateConsequences.mixed_exists_force_with_consequences`.

5. `CandidateConsequences.mixed_exists_force_with_consequences`
   (`CandidateConsequences.lean:185-215`) constructs the force from the
   residual extension and derives the smooth force, energy/blow-up
   consequences, and endpoint force jets. The theorem requires `hz` and
   `haxis`, but does not require or return a five-moment realisation theorem.

6. `ActualCandidateAssembly.selected_witness`
   (`ActualCandidateAssembly.lean:1153-1181`) supplies the actual finite-stage
   estimates, endpoint extensions, axis-zero conditions, and the generic germ
   theorem. Its public `Witness` record contains no field identifying the five
   paper moments with the selected residual or pressure.

## Pressure consequence

`StateRealization.chartIdentity` (`PhysicalResidualJetBounds.lean:927-966`)
is a local Cartesian residual identity. Its `base_equation` and
`pressure_germ` premises (`PhysicalResidualJetBounds.lean:898-924`) identify
local germs and a local base residual, but do not state an absolute global
pressure-Poisson equation or a pressure normalisation. The
`PressureRecoveryAbsolutePremiseProbe.lean` zero-sorry result independently
shows that the comparison record accepts identical zero velocities and any
common smooth pressure.

## Falsification status

The strongest honest conclusion is:

> The selected endpoint has a source-backed residual-limit construction, but
> the public proof path does not exhibit the paper-to-code transport theorem
> that makes its five moment system and global pressure semantics the same
> objects as those used in the residual-limit argument.

To upgrade this to a formal disproof, a zero-sorry probe must either expose a
false selected premise or derive an incompatibility between the selected
`haxis`, `VanishingJointJets`, pressure semantics, and the stated force
predicates. The generic comparison limitation alone does not supply that
contradiction.

The companion zero-sorry probes for the comparison limitation, the algebraic
three-to-five promotion, and the generic stage interface all compile under the
repository's pinned Lean toolchain. No `sorry`, `axiom`, or `unsafe` token is
present in those probe files. Their results are deliberately separated: they
establish interface limitations and algebraic facts, not a contradiction to
`ActualCandidateAssembly.selected_witness`.
