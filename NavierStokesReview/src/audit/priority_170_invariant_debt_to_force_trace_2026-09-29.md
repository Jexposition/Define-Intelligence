# Priority 170: invariant debt to selected force trace

Status: source-audited; no selected-field five-observable transport theorem located.

This tranche adjudicates the claim that the selected smooth-force construction is
an abstract `NativeBounds` assumption disconnected from the physical correction
machinery.

## 1. Manuscript correction

The supplied rebuttal overstates two points.

First, \(\lVert u(t)\rVert_\infty \to \infty\) does not logically imply that each summand in
\[
R(u,p)=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
\]
diverges. The manuscript itself says that the individual terms may diverge
while their sum and all derivatives extend smoothly (`docs/navier-stokes openai.txt:109-124`).
That is the stated cancellation problem, not a defect in the argument.

Second, the manuscript does not support the claim that the five moments are the
only cancellation mechanism. Section 3.2 uses profile matching and a stress
cone; Section 3.3 uses pulse covariance and the exact increment identity; the
residual cycle retains oscillatory interactions, curl and cutoff corrections,
then corrects waves, mean flow, pressure, and radial moments (`docs/navier-stokes openai.txt:440-500`, `:515-590`, `:760-783`).
The five moments are load-bearing constraints in this architecture, but the
source describes them as one component of a coupled cancellation construction.

## 2. Concrete Lean route

The selected route is not merely an arbitrary top-level rate oracle:

1. `ActualCandidateAssembly.estimates` constructs
   `GluedStageEstimates.actualStageEstimates` from actual cycle coherence,
   representations, and `physicalData`
   (`NavierStokes/ActualCandidateAssembly.lean:1079-1100`).
2. `actualStageEstimates` delegates its residual field to
   `ActualCycleResidualBounds.finite_residual_rates`, explicitly passing the
   actual invariant and physical data
   (`NavierStokes/GluedStageEstimates.lean:681-701`, `:436-440`).
3. `finite_residual_rates` invokes the invariant theorem
   `Invariant.residual_jetRate`
   (`NavierStokes/ActualCycleResidualBounds.lean:1190-1206`).
4. `residual_jetRate` uses `H.native_residual`, actual `PhysicalData`, exterior
   germs, and the base-exterior rate, rather than an unproved output force
   premise (`NavierStokes/ActualCycleResidualBounds.lean:1156-1172`).
5. `native_residual` decomposes the full residual into source, mean, excluded,
   alias, and base components, and derives their rate bound from the invariant
   (`NavierStokes/ActualCycleResidualBounds.lean:843-880`).
6. The analytic step consumes actual debt and mass data and produces
   cumulative, debt, rank, pressure, and residual outputs
   (`NavierStokes/CorrectionAnalyticStep.lean:584-629`). Its inputs include
   `H.masses`, `H.debt`, covariance data, and the rank geometry.
7. The actual invariant is propagated inductively by
   `state_runInvariant` and `state_invariant`
   (`NavierStokes/ActualCyclePreservation.lean:800-838`).
8. The resulting residual-rate data feed `physical_vanishingJointJets`, then
   `CandidateFromLimits.force_smooth`; the latter proves smoothness from actual
   locally uniform residual derivative limits, not from a bare `NativeBounds`
   field (`NavierStokes/MixedDiagonalResidual.lean:168-195`,
   `NavierStokes/CandidateFromLimits.lean:31-80`).

Therefore the statement “Lean merely assumes the rate bounds that make the
force smooth” is not supported by this selected proof route. The route proves a
concrete invariant-backed residual-flatness contract.

## 3. What remains absent

`ActualCandidateAssembly.Witness` packages the selected schedules, potential
sums, extensions, force, candidate properties, consequences, blow-up limit,
derivative decay, and boundary limits (`NavierStokes/ActualCandidateAssembly.lean:1121-1151`).
It does not state an equality of the form
\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
=(M,I,J,S,C_p),
\]
nor a theorem composing the profile/rank identities through
`potentialSum`, spatial curl, localisation, periodisation, and activation.

The source does contain genuine intermediate controls. For example,
`CorrectionAnalyticStep.step` uses `H.debt` and `H.masses`, while
`CorrectionState.rank_model_rows` and `MeanRankUpdate.physical_five_rows`
prove local five-row repair identities. Those facts establish indirect use of
moment/rank machinery. They do not establish the final selected Cartesian
observable identity.

## 4. Adjudication

The rebuttal is correct that the five-moment mechanism is mathematically
important and that its selected-field identification is still a paper-to-code
gap. It is incorrect to infer from that gap alone that the residual force is
nonsmooth, that the C-shaped proposition fails, or that the compiler accepted
an empty rate contract. The current defensible classification is:

- concrete invariant-backed residual-flatness and smooth-force route: established;
- final selected-field identification with the manuscript tuple: not established;
- selected nonzero moment defect or impossibility: not proved;
- literal Fefferman CMI failure or Lean kernel contradiction: not proved.

This is a correspondence failure for the claim that Lean verifies the
manuscript's complete five-moment physical mechanism, not a demonstrated
failure of the concrete formal C-shaped endpoint.
