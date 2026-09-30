# Priority 195: Four-operation residual control and force-smoothness adjudication

Date: 2026-09-30
Status: source-adjudicated, not a final refutation
Issue: latest claim that five-moment transport is the sole justification for `force_smooth`

## Finding

The latest rebuttal correctly treats the five cumulative quantities
\((M,I,J,S,C_p)\) as load-bearing mathematics in the manuscript. It is not
correct, however, to infer from that importance that the five moments are the
only cancellation mechanism, or that omission of a final selected-field
moment equality proves that Fefferman's smooth-force condition fails.

The manuscript's own residual-control passage lists four operations. The first
three address wave flux, signed covariance/stress, and auxiliary-time/angular
mean defects. The fourth solves the five radial moment equations. The same
passage says that the full residual is recomputed after each operation,
including the new interaction and remainder terms. Source: `docs/navier-stokes
openai.txt:695-735`.

This gives the following audit abstraction, which is explanatory notation and
not a quotation of a single source equation:

\[
 R = R_{\mathrm{wave}}+R_{\mathrm{cov}}+R_{\mathrm{aux}}
     +R_{\mathrm{radial\ moments}}+R_{\mathrm{remainder}}.
\]

The five-moment equations constrain a specific finite-dimensional radial defect
and preserve specified integral quantities. They are indispensable to the
paper's claimed repair architecture, but the inspected source does not prove
the stronger biconditional

\[
 f\in C^\infty \quad\Longleftrightarrow\quad
 (M,I,J,S,C_p)=0
\]

for the complete final Cartesian residual. Nor does \(\|u(t)\|_\infty\to\infty\)
logically imply that each summand in

\[
R(u,p)=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
\]

diverges. The manuscript expressly allows singular pieces whose total
residual is made smooth by the combined construction.

## Lean source crosswalk

The inspected selected path is not a free `NativeBounds` premise:

\[
\begin{aligned}
&\texttt{PhysicalData}
\to \texttt{actualStageEstimates}
\to \texttt{finite\_residual\_rates}\\
&\to \texttt{VanishingJointJets}
\to \texttt{boundaryLimits\_locallyUniform}
\to \texttt{tracedResidual\_smooth}
\to \texttt{force\_smooth}.
\end{aligned}
\]

Relevant declarations are:

- `NavierStokes/ActualCandidateAssembly.lean:1079-1098,1121-1151,1177-1185`;
- `NavierStokes/GluedStageEstimates.lean:684-744`;
- `NavierStokes/ActualCycleResidualBounds.lean:1015-1037,1142-1171,1190-1206`;
- `NavierStokes/CandidateFromLimits.lean:39-55,80-112`;
- `NavierStokes/GermCandidateAssembly.lean:146-158,164-304`.

`ActualCycleResidualBounds.Invariant.residual_jetRate` consumes identified
physical data and derives residual rates from the state realisation, native
residual, and exterior germs. `finite_residual_rates` then supplies the
diagonal residual rate used downstream. `CandidateFromLimits.force_smooth`
follows from the smooth extension of the traced actual residual. This is a
real encoded forced endpoint on the inspected path, not evidence that the
compiler accepted an arbitrary smoothness assertion.

## What remains unestablished

`ActualCandidateAssembly.Witness` does not export a theorem identifying the
final selected Cartesian velocity, pressure, residual, or force with the
manuscript's five observable quantities. The source therefore supports the
following precise separation:

| Proposition | Current record |
| --- | --- |
| The selected Lean path has its encoded residual, smooth-force, and blow-up contracts from its supplied physical and jet hypotheses. | Supported on the inspected path. |
| The selected endpoint is proved to realise the manuscript's final \((M,I,J,S,C_p)\) observables after all lifts, curls, localisation, summation, and pressure updates. | Not established. |
| The selected force violates Fefferman's smoothness/decay condition. | Not established. |
| The literal connected C/D proposition is false. | Not established. |

The `StageEstimates` and selected-witness non-implication probes prove a
contract limitation: the public envelope does not entail an arbitrary abstract
five-debt parameter is zero. They do not prove that the concrete selected
field has non-zero physical moment debt. That stronger conclusion needs a
value-level identity, a proved mismatch, or an impossibility theorem.

## Audit conclusion

The correct criticism is therefore **CTR-005: NOT ESTABLISHED** for complete
manuscript-to-selected-endpoint fidelity. It is not accurate to call the
current record a proof that `force_smooth` is circular or that Fefferman's
condition is violated. It is equally inaccurate to call the paper's moment
mechanism irrelevant. The five-moment bridge is a substantive, unresolved
paper-to-endpoint obligation inside a broader residual-cancellation chain.

This finding supersedes the stronger claims that (i) every residual summand
must diverge, (ii) the five moments are the sole cancellation route, or (iii)
the endpoint omission alone proves a failed CMI alternative.
