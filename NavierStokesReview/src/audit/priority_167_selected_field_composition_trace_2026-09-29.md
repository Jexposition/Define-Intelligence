# Priority 167: selected-field composition trace

**Date:** 2026-09-29\r\n**Status:** source-traced; final observable transport remains unestablished

## Decision

The selected endpoint is a genuine composition, not an empty rate wrapper. The
source path constructs the three selected stage sums, applies the mixed spatial
curl and localisation operations, periodises the fields, activates them in
time, and derives a smooth residual force from vanishing joint jets. The trace
does not, however, locate a theorem identifying the completed Cartesian fields
or their residual force with the manuscript's five cumulative observables
\((M,I,J,S,C_p)\).

The bounded conclusion is therefore:

> The selected Lean path proves smoothness, residual flatness, support,
> incompressibility, and axis blow-up through concrete rate and extension
> obligations. The inspected endpoint does not export the separate semantic
> theorem transporting the manuscript's five-observable identities through the
> completed `tsum`/curl/localisation/periodisation/pressure/force composition.

This is a contract-level correspondence gap under `CTR-005`. It is not a
proof that the selected observables are nonzero, that the force is nonsmooth,
or that Fefferman Alternative (C) is false.

## 1. The selected stage records

`ActualCandidateAssembly.physicalData` constructs physical residual data for
the actual cycle state, uncut mixed velocity, and pressure prefix
(`ActualCandidateAssembly.lean:1079-1088`). The selected estimate record is
then constructed by `GluedStageEstimates.actualStageEstimates`, with concrete
coherent cycle state, representations, and `physicalData`
(`ActualCandidateAssembly.lean:1090-1098`).

The `StageEstimates` structure itself contains smoothness, raw stage bounds,
finite background rates, and finite residual rates
(`MixedCandidateAssembly.lean:27-65`). It does not contain a five-observable
field or an equality to the paper's tuple.

## 2. Rates to vanishing joint jets

`StageEstimates.exists_schedule` consumes the three raw stage bounds and finite
residual rates. It calls
`MixedDiagonalResidual.exists_physical_schedule_residual_zero`, which returns
both a schedule and

\[
\texttt{JointResidualLimits.VanishingJointJets}
\bigl(\texttt{MixedDiagonalResidual.residual}(a,q,A,B,P)\bigr)
\]

(`MixedCandidateAssembly.lean:67-91`; `MixedDiagonalResidual.lean:197-268`).
The theorem is a rate-to-flatness result. Its inputs are `JetRate` bounds, not
the manuscript's final five-observable equality.

This distinction corrects two opposite descriptions:

* the route is not an unsupported `NativeBounds` premise;
* the rate-to-flatness theorem is not, by its type, a proof of final
  \((M,I,J,S,C_p)\) transport.

## 3. The actual `tsum` and mixed field construction

The selected witness defines

\[
\begin{aligned}
 A_{\Sigma}&=\texttt{SolenoidalDiagonal.potentialSum}(a,q,A),\\
 B_{\Sigma}&=\texttt{SolenoidalDiagonal.potentialSum}(a,q,B),\\
 P_{\Sigma}&=\texttt{SolenoidalDiagonal.potentialSum}(a,q,P).
\end{aligned}
\]

This occurs in `ActualCandidateAssembly.Witness` (`:1121-1133`). The
`potentialSum` is an actual `tsum` of cutoff stages
(`SolenoidalDiagonal.lean:31-42`). On the positive-scale domain,
`potentialSum_eventuallyEq_partial` and
`potentialSum_allJets_eventuallyEq_sum` establish local finite-prefix and
all-jet identities (`SolenoidalDiagonal.lean:56-75,140-178`). These are
meaningful smoothness results. No moment functional or five-observable
identity occurs in those declarations.

The velocity then follows the mixed construction:

\[
\texttt{periodicVelocity}(A_{\Sigma},B_{\Sigma})
 = \texttt{periodicVelocity}(A_{\Sigma})
   +\operatorname{periodize}(\operatorname{cutPotential}(B_{\Sigma})),
\]

as defined in `MixedPeriodicAssembly.lean:27-49`.

## 4. Curl, cutoff, periodisation, and time activation

`SpatialLocalization.cutVelocity_product_rule` explicitly expands the cutoff
commutator:

\[
\operatorname{curl}(cA)
 =c\,\operatorname{curl}(A)+(\nabla c)\times A.
\]

The corresponding Lean identity is
`SpatialLocalization.lean:199-207`. The periodic velocity is the curl of the
periodised cut potential (`SpatialLocalization.lean:209-217`). On the cutoff
plateau, the source proves local equality of the periodised and original
fields, their jets, and their residuals
(`SpatialLocalization.lean:312-365`; `MixedPeriodicAssembly.lean:67-101`).

Those theorems establish local agreement and regularity. They do not state
that a radial integral functional is invariant under the cutoff-gradient
commutator, the `tsum`, or periodisation. Time activation is then applied to
the periodic mixed fields in `ActualCandidateAssembly.Witness:1135-1141`.

## 5. Force construction and endpoint packaging

The selected schedule's vanishing-jets result is passed through the mixed
force construction. `MixedPeriodicAssembly.exists_candidate_force` accepts
`VanishingJointJets`, away extensions, divergence data, and the axis blow-up
limit, then constructs a force with `ContDiff` regularity
(`MixedPeriodicAssembly.lean:336-368`). `CandidateFromLimits.force_smooth`
derives smoothness from `tracedResidual_smooth`, which itself uses the
derivative recurrence and locally uniform limits
(`CandidateFromLimits.lean:35-57,80-112`).

The public `Witness` packages the resulting forcing field, `CandidateProperties`,
`CandidateConsequences`, the H3 blow-up limit, derivative decay, and boundary
jets (`ActualCandidateAssembly.lean:1121-1151`). It contains no named
conjunct of the form

\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
 =(M,I,J,S,C_p).
\]

## 6. Bounded negative search

The selected-path files searched for the symbols
`FiveProfileMoments`, `PositiveOrderMoments`, `FiveRowRank`,
`physicalMoments`, and a final `Moments(...)` equality were:

* `ActualCandidateAssembly.lean`;
* `GermCandidateAssembly.lean`;
* `MixedCandidateAssembly.lean`;
* `MixedPeriodicAssembly.lean`;
* `CandidateFromLimits.lean`;
* `GermEndpointInputs.lean`;
* `ActualEndpointInputs.lean`;
* `TimeLocalization.lean`;
* `SpatialLocalization.lean`; and
* `SolenoidalDiagonal.lean`.

No occurrence was found in that bounded selected-path search. This does not
prove that no differently named theorem exists anywhere in the repository. It
proves only that the inspected endpoint composition does not expose the
required identity under the searched declarations and names.

## 7. Audit status

| Question | Result |
|---|---|
| Are the selected sums and field operations genuine? | Yes. |
| Are the rates and force smoothness derived from concrete upstream data? | Yes, on the traced path. |
| Is the cutoff commutator represented? | Yes, explicitly. |
| Is a five-observable identity exported after the full composition? | Not located. |
| Is a selected nonzero moment defect proved? | No. |
| Is force nonsmoothness proved? | No. |
| Is literal Alternative (C) proved false? | No. |
| Is complete paper-to-endpoint correspondence established? | No. `CTR-005` remains open. |

## Source ledger

* `NavierStokes/ActualCandidateAssembly.lean:1079-1151`
* `NavierStokes/MixedCandidateAssembly.lean:27-91`
* `NavierStokes/MixedDiagonalResidual.lean:197-268`
* `NavierStokes/GermCandidateAssembly.lean:161-271`
* `NavierStokes/SolenoidalDiagonal.lean:31-178`
* `NavierStokes/SpatialLocalization.lean:164-217,312-365`
* `NavierStokes/MixedPeriodicAssembly.lean:27-101,231-368`
* `NavierStokes/CandidateFromLimits.lean:35-57,80-112`
