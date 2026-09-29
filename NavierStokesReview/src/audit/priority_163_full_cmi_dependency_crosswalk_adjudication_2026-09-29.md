# Priority 163: Full CMI dependency crosswalk adjudication

**Date:** 2026-09-29
**Status:** source-adjudicated; no formal refutation escalation

## Decision

The supplied five-step argument identifies a real correspondence risk, but it
does not prove that Fefferman Alternative (C) fails. The current record supports
three different conclusions that must not be collapsed:

1. The Lean repository proves a forced, whole-space existential proposition with
   Fefferman's smooth-force/decay and no-global-solution shape.
2. The manuscript makes the five reduced-profile quantities
   \((M,I,J,S,C_p)\) load-bearing for profile matching, correction, pressure,
   and stress propagation.
3. The inspected public endpoint does not expose a theorem identifying every
   one of those paper-level consequences with the completed selected Cartesian
   field. Exact paper-to-endpoint correspondence therefore remains
   **NOT ESTABLISHED**.

The missing endpoint identity is not, by itself, a proof that the selected
force is nonsmooth, that a selected moment defect is nonzero, or that the CMI
existential proposition is false.

## Crosswalk of the proposed five-step argument

### Step 1: Fefferman's force condition

This step is correct. The CMI source describes the force as given and
externally applied, imposes smoothness and rapid spatial/time decay, and asks
for one of the listed alternatives. Alternative (C) is an existential forced
breakdown statement, not a requirement to prove all four alternatives.

Evidence: `docs/navierstokes.txt:24-47,64-81`;
`NavierStokes/ComparatorDefinitions.lean:149-169`.

### Step 2: Residual-defined force

This is also a real semantic issue. The manuscript defines the force from the
chosen momentum residual before the singular time. That reverses the usual
explanatory direction of a forward Cauchy problem and remains a material
force-provenance objection. It is not, without more, a contradiction of an
existential statement asking for one admissible pair \((u_0,f)\).

### Step 3: blow-up does not imply termwise divergence

The proposed inference is invalid as a mathematical implication. From

\[
\|u(t)\|_{\infty}\to\infty
\]

one cannot infer that each of

\[
\partial_tu,\quad (u\cdot\nabla)u,\quad -\nu\Delta u,\quad \nabla p
\]

diverges at the same point or in the same norm. The residual is their signed
sum. Large summands can cancel, and proving or disproving that cancellation
requires estimates on the actual constructed field. A scalar analogy is

\[
A(t)=(1-t)^{-1},\qquad B(t)=-(1-t)^{-1}+1,
\qquad A(t)+B(t)=1.
\]

The example does not prove the Navier--Stokes construction works; it proves
only that blow-up of one object does not establish divergence of every term in
an expression containing cancellations. A selected-field lower-bound theorem
would be required for the stronger claim.

### Step 4: role of the five moments

The manuscript does make the five quantities load-bearing. Its extracted text
describes \(O(N^{-1})\) modulation errors, five correction bumps, exact
matching, and propagation to pressure/stress quantities. This supports the
claim that the moments are not optional notation.

The current source does **not** support the stronger wording that it states an
explicit Fredholm-adjoint-Laurent “if and only if” theorem or that the five
moments are the sole possible cancellation route. A direct source search found
no occurrences of `Fredholm`, `adjoint`, `Laurent`, or `if and only if`; other
residual operations and estimates are also described. The controlled claim is
therefore “load-bearing mechanism in the manuscript”, not “sole mechanism
proved by an iff theorem”.

Evidence: `docs/navier-stokes openai.txt:523-546,695-784,8091-8107,8451-8517`.

### Step 5: endpoint omission and force smoothness

The endpoint omission is genuine but the proposed implication is too strong.
`ActualCandidateAssembly.Witness` does not expose a named final equality of the
form

\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
 = (M,I,J,S,C_p).
\]

However, the inspected Lean route does not simply accept force smoothness from
an empty `NativeBounds` interface. The actual declarations show:

* `GluedStageEstimates.actualStageEstimates` consumes concrete physical-data
  and residual-bound records;
* `ActualStageEstimates` calls
  `ActualCycleResidualBounds.finite_residual_rates`;
* `CandidateFromLimits.tracedResidual_smooth` uses derivative recurrence and
  locally uniform boundary limits;
* `CandidateFromLimits.force_smooth` is then derived by smooth extension; and
* `ComparatorBridge.forceConditionDecay_of_compact` translates smooth compact
  force into Fefferman's force condition.

Thus the current source proves a concrete jet/force route, while leaving open
whether that route is the same as every five-moment argument claimed in the
manuscript after the full mixed Cartesian composition. `AX-033` proves only
that an abstract debt parameter is not entailed by the `Witness` proposition;
it is not a value-level proof that the selected physical integrals are wrong.

Evidence: `NavierStokes/CandidateFromLimits.lean:35-57,80-112,138-148`;
`NavierStokes/MixedPeriodicAssembly.lean:338-365`;
`NavierStokes/GluedStageEstimates.lean:684-725`;
`NavierStokes/ActualStageEstimates.lean:395-403`;
`NavierStokes/R3/ComparatorBridge.lean:22-45,77-88`;
`NavierStokes/ActualCandidateAssembly.lean:1079-1151`.

## What is and is not established

| Question | Current adjudication |
|---|---|
| Does the repository prove the declared Lean proposition whose predicates mirror the forced C clauses? | Yes, via the comparator theorem, subject to the recorded build caveat. This must not be reported as proof that the manuscript's connected physically reasonable construction has been verified. |
| Does the manuscript use the five moments as load-bearing repair/matching data? | Yes. |
| Does `Witness` export the complete selected-field five-observable identity? | Not found; correspondence remains not established. |
| Does AX-033 prove a nonzero selected physical moment defect? | No. |
| Does velocity blow-up prove termwise residual divergence? | No. |
| Does the current record prove force nonsmoothness or CMI (C) failure? | No. |
| Has a paper-level mismatch or impossibility theorem been ruled out? | No; it remains an active adverse audit target. |

## Formal endpoint evidence

`NavierStokesReview/src/extensions/CMIAlternativeCLiteralCrosswalk.lean`
restates the comparator-shaped Alternative (C) proposition. The target probe
was freshly compiled on 2026-09-29 and reported only
`propext`, `Classical.choice`, and `Quot.sound`. A repository-wide build was
not clean because the pre-existing user-owned
`NavierStokes/R3/TestPressure.lean:6` has a syntax error; that file was not
modified.

This establishes what the Lean endpoint says. It does not establish that the
endpoint is an exact formalisation of every paper-level five-moment
consequence. The two claims require separate evidence.

## Required next test

The next adverse test must trace the actual selected-field data through
`tsum`, curl, localisation, periodisation, pressure, residual, force, and
boundary limits, and must seek one of the following concrete outcomes:

1. a theorem identifying the relevant paper observables with the selected
   field;
2. a direct selected-field mismatch;
3. an impossibility theorem; or
4. failure of a mandatory CMI premise on the selected path.

Until one of (2)--(4) is proved, the defensible status is **NOT ESTABLISHED
AS COMPLETE PAPER-TO-CODE CORRESPONDENCE**, not **FORMALLY REFUTED**.
