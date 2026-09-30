# Priority 198: adjudication of the latest five-moment rebuttal

Date: 2026-09-30
Status: source-adjudicated; no final CMI refutation asserted

## Question audited

The latest rebuttal argues that the five radial quantities
\((M,I,J,S,C_p)\) are the only mechanism that can make the residual force
smooth, and that the selected Lean endpoint is therefore circular because
`Witness` does not export a final five-moment transport equality.

## Findings

The rebuttal contains a valid correspondence criticism and several unsupported
strengthenings.

### Finding 1: the valid part

The manuscript gives the five radial equations a substantive role in the
profile and correction architecture. The selected exported proposition does
not contain a theorem of the form

\[
  \operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  =(M,I,J,S,C_p).
\]

This remains `CTR-005`: complete manuscript-to-selected-endpoint fidelity is
not established. That is a stronger and more useful finding than calling the
upstream moment code dead or claiming that the endpoint is empty.

### Finding 2: the latest “sole mechanism” claim is not supported

The manuscript's residual-control passage lists four coupled operations. The
first three concern wave-amplitude balance, signed covariance/stress
correction, and auxiliary-time/angular mean correction. The fourth solves the
five radial moment equations. The passage then says that the full residual is
recomputed after each operation, including interaction and remainder terms,
and that pressure reconstruction and curl/cutoff corrections remain in the
updated residual. Source: `docs/navier-stokes openai.txt:695-735`.

Thus the source supports “load-bearing finite-dimensional radial correction”;
it does not support “the five moments are the only residual-cancellation
mechanism” or the stronger biconditional

\[
  f\in C^\infty
  \quad\Longleftrightarrow\quad
  (M,I,J,S,C_p)=0
\]

for the complete final Cartesian residual.

### Finding 3: velocity blow-up does not imply summandwise divergence

The manuscript explicitly states that individual terms in the momentum
residual can diverge while the sum and all derivatives are arranged to extend
smoothly through the singular time. Therefore

\[
  \|u(t)\|_\infty\to\infty
\]

does not, by itself, imply that each of
\(\partial_tu\), \((u\cdot\nabla)u\), \(\nu\Delta u\), and \(\nabla p\)
diverges. The latest rebuttal reverses the paper's stated cancellation logic
when it treats that implication as established.

### Finding 4: the inspected Lean path is not a free smoothness assumption

The selected path inspected in the source is:

\[
\texttt{PhysicalData}
\to\texttt{actualStageEstimates}
\to\texttt{finite\_residual\_rates}
\to\texttt{VanishingJointJets}
\to\texttt{boundaryLimits\_locallyUniform}
\to\texttt{tracedResidual\_smooth}
\to\texttt{force\_smooth}.
\]

Relevant declarations:

- `NavierStokes/ActualCandidateAssembly.lean:1079-1098,1121-1151,1177-1185`;
- `NavierStokes/GluedStageEstimates.lean:684-744`;
- `NavierStokes/ActualCycleResidualBounds.lean:1015-1037,1142-1171,1190-1206`;
- `NavierStokes/CandidateFromLimits.lean:39-55,80-112`;
- `NavierStokes/GermCandidateAssembly.lean:146-158,164-304`.

The source therefore supports a real encoded forced endpoint whose smooth-force
claim is derived from concrete physical-data and residual-jet premises. It
does not follow that this chain is equivalent to the manuscript's complete
five-moment mechanism. The correct criticism is a missing correspondence
identification, not a demonstrated circular proof.

## Logical separation

Let

\[
\begin{aligned}
P_1 &: \text{the selected Lean path satisfies its encoded residual, smooth-force,
and blow-up contracts};\\
P_2 &: \text{the selected path is proved to realise the manuscript's final
five observables after all transformations}.
\end{aligned}
\]

The inspected record supports \(P_1\) on its supplied premises and does not
establish \(P_2\). It also does not establish \(\neg P_1\), a nonzero selected
moment defect, force nonsmoothness, or a false connected CMI proposition.

This is not a defence of OpenAI's paper. It is the narrow source-backed
statement that the current evidence proves an encoded endpoint while failing
to establish complete paper-to-endpoint fidelity.

## Controlled verdict

`CTR-005: NOT ESTABLISHED` remains the correct status for the complete
manuscript-to-selected-endpoint correspondence. The latest rebuttal should be
retained as a challenge document, but its claims that the five moments are the
sole cancellation route, that every residual summand diverges, and that
`force_smooth` is thereby circular are not accepted without a new source-level
theorem or a value-level counterexample.

## Evidence crosswalk

- `NavierStokesReview/evidence/priority_195_four_operation_force_smoothness_adjudication_2026-09-30.json`;
- `NavierStokesReview/evidence/selected_transport_audit_2026-09-28.md`;
- `NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`;
- `NavierStokesReview/evidence/global_cross_layer_audit_2026-09-27.md`;
- `docs/OpenAI_NavierStokes_Research_Paper.md`;
- `docs/OpenAI_NavierStokes_Peer_Review_v1.md`.

