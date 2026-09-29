# Priority 164: Cycle invariant to residual-jet trace

**Date:** 2026-09-29
**Status:** source-adjudicated; correspondence gap remains open

## Decision

The selected residual-rate route is materially grounded in actual correction
state. It is not an empty `NativeBounds` assumption. However, the exact
`CycleAnalyticInvariant` contract is not the paper's final five-observable
identity, and no source declaration inspected here identifies its post-curl,
post-localisation, periodised Cartesian field with
\((M,I,J,S,C_p)\).

The correct statement is therefore:

> The Lean endpoint has a real moment/rank-dependent upstream engine feeding
> residual estimates and force smoothness, but the inspected endpoint still
> lacks the final semantic identification needed to claim that the exported
> CMI witness is the paper's complete five-moment construction.

This finding corrects two opposite errors: calling the rate contract
``generic`` in the sense of being unsupported, and treating upstream
moment/rank dependence as proof of final selected-field transport.

## Exact declarations

### 1. The invariant is substantive

`NavierStokes/CorrectionStep.lean:9405-9462` defines
`CycleAnalyticInvariant` with fields for:

* an actual `CycleRepresentation`;
* coefficient bands, support, smoothness, solenoidality, periodicity, and
  carrier compatibility;
* cumulative bounds and mean-residual hypotheses;
* `debt : DefectBounds ...`;
* `masses : GaugeMassPreservation.ZeroMassesOn ...`;
* residual classes and reconstructed state;
* oscillatory and pressure regularity.

The record is therefore not a hollow shell. It contains actual correction
state and defect-control obligations.

### 2. What its ``five'' correction data actually are

`NavierStokes/CorrectionState.lean:225-251` defines three radial defects:

\[
 d=(P,J_\theta,J_z),
\]

where `pressureDefect`, `thetaDefect`, and `axialDefect` are radial moments of
the stored mean/covariance fields. The separate `ZeroMasses` predicate is the
two-component condition

\[
 \operatorname{radialMoment}_2(u_{\theta})=0,
 \qquad
 \operatorname{radialMoment}_1(u_z)=0.
\]

`CorrectionState.lean:449-476` then feeds this defect vector into
`FiveRowRank.FiveRows` and proves the rank-model/patch row equations. This is
genuine five-row correction algebra, but its contract is expressed as three
defect coordinates plus two mass constraints, not as a final tuple equality
for the completed Cartesian field.

### 3. The data feed the residual-rate path

The selected route is materially connected:

\[
\begin{aligned}
&\texttt{initial\_invariant}
\to \texttt{CycleAnalyticInvariant}\,(\texttt{debt},\texttt{masses},\texttt{residual})\\
&\to \texttt{ActualCycleResidualBounds.finite\_residual\_rates}\
text{ (with physical data)}\\
&\to \texttt{ActualStageEstimates.stageEstimates\_of\_representations}\
\to \texttt{GluedStageEstimates.actualStageEstimates}\\
&\to \texttt{ActualCandidateAssembly.estimates}\
\to \texttt{selected\_schedule}\
\to \texttt{VanishingJointJets}\
\to \texttt{force\_smooth}.
\end{aligned}
\]

Evidence locations:

* `ActualInitialization.lean:1376-1389,1425-1458` constructs the initial
  invariant from concrete cumulative, mean, debt, and zero-mass results.
* `ActualCycleResidualBounds.lean:1156-1203` uses the invariant and physical
  data to produce finite residual rates.
* `ActualStageEstimates.lean:347-403` places those rates into `StageEstimates`.
* `ActualCandidateAssembly.lean:1079-1098` supplies concrete physical data and
  those estimates to the selected assembly.
* `CandidateFromLimits.lean:35-57,80-112` derives smooth residual extension
  and force agreement from recurrence and boundary-limit data.

Consequently, the claim that Lean simply assumes `force_smooth` from an empty
rate interface is false on the inspected path.

## What this does not prove

The invariant's `debt` and `masses` fields are not, by themselves, the theorem

\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
=(M,I,J,S,C_p).
\]

They are properties of the correction-cycle state and its radial defect
operators. The final `Witness` still has no named field or conjunct proving
that the completed selected field, after the actual sums, curl lift,
localisation, periodisation, pressure construction, and force extension,
realises the manuscript's five observables.

Therefore:

* **Established:** real moment/rank data feed concrete residual estimates;
* **Established:** the selected force-smoothness route is not an unsupported
  empty interface;
* **Not established:** final paper-level five-observable transport;
* **Not established:** a nonzero selected moment defect;
* **Not established:** force nonsmoothness or literal CMI Alternative (C)
  failure.

The adverse audit remains `CTR-005: NOT ESTABLISHED AS COMPLETE
PAPER-TO-CODE CORRESPONDENCE`, not a proven `False` result.
