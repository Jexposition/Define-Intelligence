# Adjudication of the Five-Moment / Jet-Smoothness Rebuttal

Status: source-checked adjudication, 2026-09-29.

## Decision

The supplied rebuttal is partly correct but overstates three conclusions. The defensible finding is:

> The paper-to-endpoint identification of the final Cartesian field with the paper's five reduced-profile observables is not established by the inspected `Witness` contract. However, the current record does not prove that the selected force is nonsmooth, that the selected field has nonzero five-moment debt, or that Fefferman Alternative (C) fails.

This is a material correspondence failure, not a proved kernel contradiction.

## 1. What the manuscript actually says

The OpenAI manuscript explicitly rejects the inference that velocity blow-up forces every residual summand to diverge. It says that individual terms can diverge while their sum and all derivatives extend smoothly through the singular time (`docs/navier-stokes openai.txt:108-113`). It then gives a multi-part cancellation architecture:

1. Oscillatory pulses cancel the leading singular background stress (`:118-123`).
2. The pulse flux is selected through the stress-cone construction (`:287-293`).
3. Heat-exterior localisation and cutoff terms are controlled (`:298-319`).
4. The correction cycle solves four classes of tasks, including the five radial moment equations (`:670-735`, especially the numbered operations in `:704-721`).

The paper therefore makes the five-moment system important, but the source does not support the stronger statement that it is the only residual-cancellation mechanism. The moments are a load-bearing compatibility and matching component inside a larger construction.

## 2. What Fefferman actually requires

The supplied CMI transcription states that the force and initial data satisfy rapid spatial decay (`docs/navierstokes.txt:25-40`), and that a physically reasonable solution is smooth and has bounded energy (`:41-47`). Alternative (C) asks for the existence of smooth data and force satisfying those data conditions for which no global smooth bounded-energy solution exists (`:74-77`).

The phrase “given, externally applied force” supplies the forward-problem interpretation (`:25-26`), but the Alternative (C) proposition itself is existential. The current text does not add a formal independence predicate forbidding an author from designing a force from a selected trajectory. That remains a physical-provenance objection, not a proved logical contradiction.

## 3. What the Lean endpoint contains and omits

`ActualCandidateAssembly.Witness` is a `Prop` packaging the selected schedule, three potential sums, extensions, a forcing field, `CandidateProperties`, `ContDiff` of the force, `CandidateConsequences`, an H3 blow-up limit, decay estimates, and boundary-limit identities (`NavierStokes/ActualCandidateAssembly.lean:1121-1151`). It does not visibly contain a named equality of the form

\[
\operatorname{Moments}(u_{\rm selected},p_{\rm selected},f_{\rm selected})
  =(M,I,J,S,C_p).
\]

That omission proves a contract-level non-entailment: the endpoint does not, by its type alone, certify the paper's advertised final-observable identification. It does **not** prove that the actual selected integrals are nonzero or that the construction's internal correction data are unused.

## 4. Why the “unlinked jet assumption” claim is too strong

The selected path is not built from an empty `NativeBounds` placeholder.

* `ActualCandidateAssembly.estimates` calls `GluedStageEstimates.actualStageEstimates` with `ActualCyclePreservation.state_coherent`, concrete representations, and `physicalData` (`NavierStokes/ActualCandidateAssembly.lean:1089-1099`).
* `GluedStageEstimates.actualStageEstimates` consumes `PhysicalData` and constructs the stage estimate record (`NavierStokes/GluedStageEstimates.lean:681-701`).
* `ActualStageEstimates.stageEstimates_of_representations` calls `ActualCycleResidualBounds.finite_residual_rates` (`NavierStokes/ActualStageEstimates.lean:347-354`, `:399-403`).
* `finite_residual_rates` consumes an invariant for every cycle and physical residual data, then obtains the residual jet rate from `(H J).residual_jetRate` (`NavierStokes/ActualCycleResidualBounds.lean:1190-1206`).
* `CycleAnalyticInvariant` contains concrete wave, mean, debt, reconstruction, and mass-preservation fields (`NavierStokes/CorrectionStep.lean:9408-9461`). Its `debt` is a three-coordinate defect record, while `masses` is a separate exact zero-mass invariant (`NavierStokes/CorrectionState.lean:242-250`; `NavierStokes/CorrectionStep.lean:9443-9449`).
* `CandidateFromLimits.force_smooth` is derived from `tracedResidual_smooth`, and the force agrees with the activated residual throughout the past (`NavierStokes/CandidateFromLimits.lean:80-112`).

Thus the correct statement is not “Lean assumed smoothness from a disconnected generic interface”. The correct statement is “Lean proves a concrete residual-jet and force-smoothness route, but the inspected endpoint does not identify that route with the paper's final five-observable tuple.”

## 5. What `AX-033` does and does not prove

The non-implication probe is useful, but its logical scope must remain exact:

\[
\neg\bigl(\texttt{Witness}\Rightarrow
  \forall d:\mathrm{Fin}(5)\to\mathbb R,\ d=0\bigr)
\]

shows that the `Witness` proposition does not entail an independently supplied abstract debt parameter. It does not construct a physical field with nonzero `(M,I,J,S,C_p)`; it demonstrates missing payload in the contract. Treating it as a selected-field counterexample is an invalid strengthening.

## 6. Final audit classification

| Question | Supported conclusion |
|---|---|
| Are the five moments used in the paper's profile matching and correction mechanism? | Yes. |
| Are they the manuscript's only cancellation mechanism? | No. The manuscript explicitly adds pulse-flux cancellation, pressure reconstruction, auxiliary inversion, Fourier-mode corrections, and higher-order residual control. |
| Does `Witness` export a final Cartesian five-moment identity? | Not located in the inspected endpoint. |
| Are the selected residual rates derived from actual cycle data? | Yes, on the traced path. |
| Does the current record prove a nonzero selected moment defect? | No. |
| Does the current record prove the force is not smooth? | No. |
| Does the current record prove literal Alternative (C) is false? | No. The endpoint has a separately verified C-shaped existential route; exact paper correspondence remains unestablished. |

The review should therefore retain `CTR-005` as **Not Established as complete paper-to-Lean correspondence**, while removing the stronger unsupported claims that the five moments are the sole cancellation route, that the jet interface is unlinked to concrete cycle data, or that Fefferman Alternative (C) has already been formally refuted.
