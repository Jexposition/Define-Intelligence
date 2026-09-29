# Priority 185: adjudication of the five-moment smoothness rebuttal

**Date:** 2026-09-30
**Status:** source-checked; the rebuttal is partly correct, but its termwise-divergence, sole-mechanism, and bare-interface claims are not established

## Executive finding

The supplied rebuttal correctly treats the five radial quantities
\((M,I,J,S,C_p)\) as load-bearing in the manuscript. It is therefore wrong to
describe the audit as saying that the moments are optional or removable from
the published construction.

Three stronger statements in the rebuttal do not survive the source check:

1. \(\|u(t)\|_\infty\to\infty\) does not imply that every summand of
   \(\mathcal R(u,p)\) diverges. The manuscript explicitly describes
   cancellation between singular contributions and smooth extension of the
   total residual.
2. The manuscript does not say that the five equations are its only
   cancellation operation. It separately lists wave-amplitude equations,
   signed covariance corrections, auxiliary-time inversion, pressure
   reconstruction, nonlinear interaction estimates, cutoffs, summation, and
   flat-remainder estimates.
3. `CandidateFromLimits.force_smooth` is not obtained from a bare endpoint
   `NativeBounds` assumption. The selected path supplies concrete residual-rate
   data, derives a schedule with vanishing joint jets, transports those limits
   through the cut/periodic assembly, and then invokes the smooth extension
   theorem.

The adverse result remains exact and material:

\[
\text{the selected path proves residual-jet smoothness}
\quad\not\Rightarrow\quad
\operatorname{PaperMoments}(u_{\rm selected},p_{\rm selected})
=(M,I,J,S,C_p).
\]

No inspected declaration supplies that completed identity after the selected
`tsum`, curl, localisation, periodisation, torus averaging, radial integration,
and global integrability steps. The complete manuscript-to-endpoint claim is
therefore still **NOT ESTABLISHED (CTR-005)**. This is not yet a selected
nonzero defect, a force-nonsmoothness theorem, an impossibility theorem, a
literal CMI failure, or `False`.

## 1. What the manuscript actually establishes

The manuscript makes the moments consequential in at least three places:

| Manuscript passage | What it does | Audit interpretation |
|---|---|---|
| `docs/navier-stokes openai.txt:492--496` | Matching profiles and five radial integrals preserves the exterior fields and makes the annular stress vanish outside the joining region. | Load-bearing profile-matching identity. |
| `:539--546` | High-frequency modulation changes the five integrals by \(O(N^{-1})\), followed by a separate localised correction restoring all five. | Load-bearing modulation-repair step. |
| `:695--735` | Four distinct operations control different residual pieces; the fourth solves five radial equations, while the first three handle wave modes, covariance, and auxiliary-time/angular corrections. | The five-equation block is essential, but not the only operation in the residual architecture. |
| `:746--784` | Curl/cutoff terms, locally finite sums, residual comparison, repeated cycles, and flatness are retained before the smooth compactly supported force is formed. | The paper's cancellation chain is composite, not a single final tuple test. |

The mathematically correct dependency claim is therefore:

\[
\text{five-moment corrections are necessary components of the manuscript's
profile and compatibility construction},
\]

not the stronger source-free claim:

\[
\text{the five moments are the unique proof of every residual-jet and force
smoothness conclusion}.
\]

The latter would require a theorem from the manuscript showing that all other
operations are logically inert once the five equations are solved. The source
text does not provide that theorem; instead it explicitly assigns them
separate jobs.

## 2. Exact Lean dependency trace for smooth forcing

The current source does not show a force-smoothness shortcut. The selected
route is the following chain:

\[
\begin{aligned}
&\texttt{ActualCandidateAssembly.physicalData}\\
&\quad\Downarrow\ \texttt{ActualPhysicalPrefixFields.physicalFields\_all}\\
&\texttt{GluedStageEstimates.actualStageEstimates}\\
&\quad\Downarrow\ \texttt{ActualCycleResidualBounds.finite\_residual\_rates}\\
&\texttt{StageEstimates.exists\_schedule}\
  \Rightarrow \texttt{VanishingJointJets}\\
&\quad\Downarrow\ \texttt{MixedPeriodicAssembly.boundaryLimits\_locallyUniform}\\
&\texttt{MixedPeriodicAssembly.exists\_candidate\_force}\\
&\quad\Downarrow\ \texttt{CandidateFromLimits.force\_smooth}\\
&F\in C^\infty,\qquad F=\mathcal R(u,p)\text{ for }0\le t<1.
\end{aligned}
\]

The critical source points are:

- `NavierStokes/ActualCandidateAssembly.lean:1079--1098` constructs
  `physicalData` and passes it into the actual stage-estimate constructor.
- `NavierStokes/GluedStageEstimates.lean:684--725` constructs the complete
  `StageEstimates` record and proves its `finite_residual` field using
  `ActualCycleResidualBounds.finite_residual_rates`.
- `NavierStokes/ActualCycleResidualBounds.lean:1156--1172` derives a residual
  jet rate from the actual invariant, state realisation, native residual bound,
  physical data, exterior germs, and the base exterior estimate.
- `NavierStokes/MixedCandidateAssembly.lean:67--91` turns those finite-stage
  rates into a schedule and `VanishingJointJets`.
- `NavierStokes/GermCandidateAssembly.lean:264--271` feeds the selected
  schedule, extensions, vanishing jets, and axis blow-up into
  `CandidateConsequences.mixed_exists_force_with_consequences`.
- `NavierStokes/MixedPeriodicAssembly.lean:338--365` constructs the force from
  the actual mixed periodic fields and residual limits.
- `NavierStokes/CandidateFromLimits.lean:80--112` defines the smooth extension
  and proves `force_smooth` and agreement with the activated residual before
  the singular time.

This proves a real conditional chain. It does not prove that the chain is the
same chain as the manuscript's five-observable proof, because the named
selected-field moment identity is still absent.

## 3. What the endpoint does and does not export

`ActualCandidateAssembly.Witness` at `:1121--1151` exports the selected
schedules, three actual sums, away extensions, a forcing field,
`CandidateProperties`, smooth forcing, `CandidateConsequences`, Sobolev
blow-up, force-jet decay, and boundary jets. The selected blow-up is supplied
through `GermCandidateAssembly.origin_blowup` and `FinalSlowBase.axis_tendsto`.
That is why the endpoint can prove blow-up without placing a moment tuple in
the *type of the direct axis-asymptotic subtheorem*.

This does **not** mean that the published moment mechanism is dispensable.
It means only that the endpoint's current theorem contracts are strong enough
to derive the operational blow-up and smooth-force propositions through a
different visible interface. The missing correspondence is the implication

\[
J_{\rm flat}\Rightarrow
\operatorname{PaperMoments}(u_{\rm selected},p_{\rm selected})
=(M,I,J,S,C_p),
\]

not the already-present implication

\[
H_{\rm selected}\Rightarrow J_{\rm flat}\Rightarrow F\in C^\infty.
\]

The review-side theorem `SelectedEndpointMomentTransportObstruction` is
deliberately only type-level. Its nonzero `Debt` function is an omitted
payload, not a physical counterexample. It proves that `Witness` alone cannot
certify the five identities, not that the selected field violates them.

## 4. The remaining value-level gate

The review completions now expose increasingly concrete pieces:

- `SelectedPotentialProductionFinitePrefix.lean` expands finite prefixes and
  retains the cutoff-gradient curl commutator.
- `SelectedPotentialProductionTsumScope.lean` proves local all-jet equality
  between the selected potential sum and a finite prefix.
- `SelectedMixedProductionBarMoment.lean` gives a typed pullback to the
  scalar family consumed by `barMoment`.
- `SelectedMixedProductionTorusAverage.lean` reduces the auxiliary torus
  average pointwise.
- `SelectedCycleMomentTransport.lean` proves selected-cycle zero angular and
  axial mean moments.
- `SelectedDirectRadialMomentBridge.lean` proves a zero order-two moment for
  the direct native scalar branch.

These are real bridges, but they stop short of the full theorem. In
particular, no inspected completion proves the equality for the completed
mixed Cartesian field after the infinite sum, the cutoff commutator, the
periodised field, the global `barMoment` integral, and the five paper
coordinates. The next gate is therefore a value-level selected integral
theorem with explicit support, integrability, and axis hypotheses.

## 5. Adjudication

| Rebuttal statement | Finding |
|---|---|
| The five moments are load-bearing in the paper. | **Confirmed.** |
| Blow-up proves every residual summand diverges. | **Rejected.** The paper explicitly arranges cancellation in the total residual. |
| The five equations are the only cancellation mechanism. | **Not established and contradicted by the paper's four-operation residual discussion.** |
| `force_smooth` is a bare `NativeBounds` assumption. | **Rejected.** The selected path derives it from actual residual-jet premises and extension theorems. |
| `Witness` exports the paper's completed five-moment identity. | **Not established.** The inspected endpoint omits that identity. |
| The omitted identity proves the selected force is nonsmooth or CMI C fails. | **Not established.** A value mismatch, failed connected CMI condition, impossibility theorem, or contradiction is still required. |
| The endpoint proves the manuscript's complete physical argument. | **Not established (CTR-005).** |

The correct adversarial conclusion is consequently not a request for OpenAI
to repair its work. It is a failure to credit the headline paper-to-Lean
correspondence until the selected value-level transport theorem is present or
the selected mismatch is proved.

## Evidence boundary

This report is source-checked. It does not claim a fresh Lean rebuild because
the current shell lacks `lean`, `lake`, and `elan`. It does not modify the
OpenAI source tree. It does not turn `noncomputable`, `Classical.choice`, or
the omitted endpoint payload into a compiler-cheat allegation.

Evidence:

- `NavierStokesReview/src/audit/priority_184_selected_path_foundation_audit_2026-09-29.md`
- `NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean`
- `NavierStokesReview/src/completions/SelectedPotentialProductionTsumScope.lean`
- `NavierStokesReview/src/completions/SelectedMixedProductionTorusAverage.lean`
- `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
- `docs/navier-stokes openai.txt:109--124,492--496,539--546,695--784`
