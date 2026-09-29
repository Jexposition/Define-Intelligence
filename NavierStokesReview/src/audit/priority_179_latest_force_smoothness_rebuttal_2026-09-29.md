# Priority 179: adjudication of the latest force-smoothness rebuttal

**Date:** 2026-09-29
**Scope:** supplied rebuttal concerning residual-term divergence, five-moment cancellation, `force_smooth`, and `CTR-005`
**Status:** source-checked; no selected-field mismatch, impossibility theorem, or literal C/D failure claimed

## Finding

The rebuttal identifies a genuine issue: the manuscript treats the five
cumulative radial equations as a load-bearing correction block, while the
exported `Witness` does not expose a theorem identifying the completed
activated Cartesian field with the manuscript observables

\[
(M,I,J,S,C_p).
\]

Its stronger conclusion is not established. The raw manuscript and Lean
source support a more precise dependency statement:

\[
H_{\mathrm{selected}}
\Longrightarrow J_{\mathrm{flat}}
\Longrightarrow F_{\mathrm{smooth}},
\]

where `H_selected` denotes the concrete selected physical data, residual-rate
and schedule hypotheses, \(J_{\mathrm{flat}}\) denotes the compatible limits
of all residual derivatives, and \(F_{\mathrm{smooth}}\) denotes the smooth
force extension. The manuscript's five-moment correction is one load-bearing
route inside the construction of \(H_{\mathrm{selected}}\) and the residual
estimates. The current audit has not proved either

\[
J_{\mathrm{flat}}\Longrightarrow
\operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}})
=(M,I,J,S,C_p)
\]

or the converse. This is why the final paper-specific correspondence remains
**NOT ESTABLISHED (CTR-005)** without asserting that the force is singular.

## 1. What the rebuttal gets right

The manuscript explicitly says that cumulative radial integrals control
pressure, radial velocity, and stress, and that modulation changes those
integrals by \(O(N^{-1})\) before a local correction restores all five
(`docs/navier-stokes openai.txt:523--546`). The correction cycle also contains
five radial equations for preserving two integrals and cancelling three radial
defects (`:695--731`). These are not optional notation.

The endpoint audit therefore retains the adverse correspondence finding:

\[
\text{profile/correction identities}
\not\Rightarrow
\text{final activated Cartesian five-observable identity}
\]

unless the intervening representation, convergence, support, averaging, and
axis-limit steps are proved for the selected fields.

## 2. Why the termwise-divergence claim is not proved

The rebuttal asserts that \(\|u(t)\|_{L^\infty}\to\infty\) forces the
individual terms in

\[
R(u,p)=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
\]

to diverge. That implication is invalid without additional estimates. For
example,

\[
T_1(t)=\frac{1}{1-t},\qquad
T_2(t)=-\frac{1}{1-t}+g(t)
\]

has divergent summands but a regular sum \(g(t)\). Conversely, an unbounded
velocity norm does not determine the behaviour of every differentiated
component. The manuscript itself makes the weaker and correct statement that
individual residual terms can diverge while their sum and all derivatives are
arranged to extend smoothly (`docs/navier-stokes openai.txt:109--124`).

The source therefore supports “cancellation must be arranged”, not the
rebuttal's stronger premise that each summand is known to diverge.

## 3. Why “the only cancellation mechanism” is too strong

The manuscript describes a connected multi-operation correction cycle:

1. wave-amplitude equations cancel supported nonzero angular sources;
2. signed amplitudes correct averaged stress through covariance;
3. auxiliary-time inversion corrects the averaged residual and supplies the
   axial increment;
4. five radial equations correct the remaining specified radial defects
   (`docs/navier-stokes openai.txt:695--731`).

It then states that the full updated products, pressure, curls, cutoffs, and
nonlinear remainders are retained (`:732--735`). The summation step applies
shrinking cutoffs, compares the full residual with finite stages, and proves
flatness and smooth fields (`:746--757`). The figure-level summary separately
lists full residual recomputation, correction cycles, summation, and force
extension (`:761--784`).

Thus the supported claim is:

> The five-moment equations are a necessary and load-bearing finite-dimensional
> correction block in the written mechanism.

The unsupported claim is:

> They are the only mathematical operation capable of producing a smooth
> total residual.

The latter would require a necessity theorem excluding the other correction,
reconstruction, cutoff, and flat-tail mechanisms. Neither the cited manuscript
passages nor the inspected Lean declarations supplies that theorem.

## 4. What `force_smooth` actually proves

The selected Lean route is not an empty `NativeBounds` interface:

* `ActualCandidateAssembly.lean:1079--1098` constructs physical data and
  actual stage estimates from the selected cycle representations;
* `MixedCandidateAssembly.lean:67--90` derives a schedule and
  `VanishingJointJets` from `StageEstimates` and finite residual estimates;
* `CandidateFromLimits.lean:47--55` derives smoothness of the traced residual
  from derivative recurrence and locally uniform endpoint limits;
* `CandidateFromLimits.lean:80--87` defines the smooth force extension and
  proves `force_smooth`;
* `CandidateFromLimits.lean:97--112` proves agreement with the activated
  residual for the pre-terminal interval.

The selected construction therefore proves a real rate-to-flatness-to-force
route on its declared objects. The missing result is different: no inspected
declaration identifies the completed selected Cartesian field and pressure
with the manuscript's five reduced-profile observables after `tsum`, curl,
localisation, periodisation, averaging, radial integration, and axis
totalisation.

## 5. Meaning of the abstract debt obstruction

The review-side `AX-033`/selected-endpoint obstruction proves a type-level
non-entailment: an independent abstract five-debt parameter is not part of the
`Witness` contract. It does **not** construct a second selected velocity,
pressure, residual, or force with physically nonzero debt. Calling it a
physical countermodel would overstate the theorem.

The correct inference is:

\[
\texttt{Witness}
\not\vdash
\operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}})
=(M,I,J,S,C_p).
\]

That is sufficient for a paper-to-endpoint non-verification finding, but not
for \(\Delta m\ne0\), force nonsmoothness, impossibility, or `False`.

## Adjudicated status

| Question | Current source-grounded result |
| --- | --- |
| Are the five moments load-bearing in the manuscript? | Yes, within the profile and correction architecture. |
| Does velocity blow-up prove termwise residual divergence? | No. |
| Does the manuscript establish that five moments are the only cancellation route? | No. It describes several coupled correction and flatness operations. |
| Is `force_smooth` merely assumed at the selected endpoint? | No. The inspected path derives it from concrete residual limits. |
| Does `Witness` export the final selected-field five-moment identity? | Not located; `CTR-005` remains **NOT ESTABLISHED**. |
| Has a selected nonzero defect or literal C/D failure been proved? | No. |

## Evidence anchors

* `docs/navier-stokes openai.txt:109--124,523--546,695--735,746--784,6101--6153`
* `NavierStokes/ActualCandidateAssembly.lean:1079--1098,1121--1151,1177--1180`
* `NavierStokes/MixedCandidateAssembly.lean:67--90`
* `NavierStokes/CandidateFromLimits.lean:47--55,80--112`
* `NavierStokes/DefectIncrementBounds.lean:214--220`
* `NavierStokesReview/src/audit/priority_176_selected_field_composition_domain_trace_2026-09-29.md`
* `NavierStokesReview/src/audit/priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.md`
