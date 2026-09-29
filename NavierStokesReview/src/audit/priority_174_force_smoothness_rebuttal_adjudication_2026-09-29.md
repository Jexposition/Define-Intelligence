# Priority 174: Adjudication of the force-smoothness rebuttal

**Date:** 2026-09-29
**Scope:** `navier-stokes openai.txt`, `navierstokes.txt`, and the selected Lean path rooted at `ActualCandidateAssembly.selected_witness`
**Status:** source-checked adjudication; no selected-field mismatch or impossibility theorem claimed

## Executive finding

The supplied rebuttal is partly right about the importance of the five-moment mechanism, but its decisive logical conclusion is not established by the sources.

The selected Lean path does not merely assert `NativeBounds` and then obtain smooth forcing from an empty interface. The inspected route is:

\[
\begin{aligned}
&\texttt{ActualCandidateAssembly.physicalData} \\
&\quad\Longrightarrow \texttt{GluedStageEstimates.actualStageEstimates} \\
&\quad\Longrightarrow \texttt{MixedCandidateAssembly.exists\_physical\_schedule\_residual\_zero} \\
&\quad\Longrightarrow \texttt{SelectedSchedule.VanishingJointJets} \\
&\quad\Longrightarrow \texttt{CandidateFromLimits.tracedResidual\_smooth} \\
&\quad\Longrightarrow \texttt{CandidateFromLimits.force\_smooth}.
\end{aligned}
\]

That is a genuine source-level residual-flatness route. It does **not** establish the separate paper-to-code theorem

\[
\operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}})
  =(M,I,J,S,C_p),
\]

because the final `Witness` proposition contains no such equality and no declaration on the inspected selected path was found to define the paper tuple on the activated Cartesian field.

The defensible result is therefore:

> The Lean endpoint contains a concrete residual-jet and smooth-force construction, while the exact transport of the manuscript’s five cumulative observables into the final activated Cartesian field remains unestablished. This is a paper-to-endpoint correspondence failure (`CTR-005`), not a proved force singularity, not a proved selected-field mismatch, and not a kernel contradiction.

## 1. The rebuttal’s first error: velocity blow-up does not force every residual summand to diverge

Write

\[
R=T_1+T_2+T_3+T_4
  =\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p.
\]

The implication

\[
\|u(t)\|_{L^\infty}\to\infty
\quad\Longrightarrow\quad
\|T_i(t)\|\to\infty\text{ for every }i
\]

is false in general. A velocity can become large through one component or one scale without forcing every differentiated component to diverge. Even when several summands diverge, cancellation is possible; for example,

\[
T_1(t)=\frac1{1-t},\qquad
T_2(t)=-\frac1{1-t}+g(t),
\]

gives \(T_1+T_2=g\), which can be smooth at \(t=1\).

This is not an abstract objection imported from outside the manuscript. The manuscript itself says that individual residual terms can diverge while their sum and all derivatives are arranged to extend smoothly through the singular time (`docs/navier-stokes openai.txt:109–124`). Therefore the rebuttal’s Step 3 cannot be used as a proved premise.

## 2. The rebuttal’s second error: the manuscript does not say that five moments are the only cancellation operation

The five-moment system is load-bearing, but the manuscript describes a larger correction architecture. Its own proof outline states that:

* oscillatory pulses cancel the leading singular annular stress;
* further corrections remove remaining singular errors;
* the wave-flux, angular, auxiliary-mean, pressure, radial-integral, cutoff, and nonlinear terms are recomputed and corrected in successive stages.

The clearest source statement is the four-step correction list (`docs/navier-stokes openai.txt:695–733`). Step 4 solves the five radial moment equations, but Steps 1–3 separately handle stress realization, signed amplitudes, auxiliary-time inversion, and reconstruction remainders. The same section explicitly says that the full residual retains curl, cutoff, and flat reconstruction terms.

Thus the mathematically supportable statement is:

\[
\text{five moments are necessary conditions in a specified correction layer}
\]

not

\[
\text{five moments are the only mechanism that can make }R\text{ smooth}.
\]

The latter would require a theorem of necessity or an impossibility theorem for every other cancellation route. Neither the manuscript passages inspected nor the Lean audit supplies that theorem.

## 3. What the Lean force proof actually consumes

`CandidateFromLimits.lean` defines the force by extending the traced past residual:

* `tracedResidual` is built from `PastExtension.pastResidual` and the supplied derivative-limit series (`:28–31`);
* `tracedResidual_smooth` consumes the actual residual derivative recurrence and locally uniform limits (`:47–55`);
* `force` is the smooth extension of that traced residual (`:80–84`);
* `force_smooth` is derived from `tracedResidual_smooth` (`:86–87`);
* `force_eq_activated_residual` identifies the force with the activated Navier–Stokes residual for `0 ≤ t < 1` (`:108–112`);
* `candidate_properties` packages smoothness, periodicity, divergence freedom, residual equality, and speed unboundedness for the same fields (`:167–182`).

At the selected assembly boundary, `ActualCandidateAssembly.physicalData` supplies `ActualCycleResidualBounds.PhysicalData` from `ActualPhysicalPrefixFields.physicalFields_all` (`ActualCandidateAssembly.lean:1079–1088`). `estimates` then calls `GluedStageEstimates.actualStageEstimates` with the actual run data, coherent cycle data, representations, and that physical-data theorem (`:1090–1098`). The selected schedule is subsequently required to contain `VanishingJointJets` (`MixedCandidateWitness.lean:26–31`), and the physical schedule theorem supplies that property (`MixedCandidateAssembly.lean:76–88`).

This refutes the specific assertion that `force_smooth` is proved only from a free-standing, unlinked `NativeBounds` assumption. The route has concrete upstream premises and actual residual fields.

It does **not** refute `CTR-005`. The type of `Witness` still packages schedules, sums, extensions, forcing, `CandidateProperties`, `CandidateConsequences`, derivative limits, and blow-up (`ActualCandidateAssembly.lean:1121–1151`) without a final equality identifying the selected Cartesian field’s paper moments.

## 4. Why the missing moment theorem still matters

The omission is material because the manuscript’s five moments are not decorative. The manuscript uses them for profile modulation, exact restoration, exterior matching, and radial defect correction. The Lean source also contains genuine intermediate moment and rank theorems, including `FiveRows`, `barMoment`, debt variables, zero-mass identities, and physical rank updates.

However, an intermediate identity has a different type from the endpoint identity. In particular, `DefectIncrementBounds.barMoment` is an integral over a `PressureStream` average (`DefectIncrementBounds.lean:214–220`). It is not definitionally an observable of the final `TimeLocalization.activatedVelocity` used by `Witness`. A valid endpoint bridge would need to prove, at minimum, the relevant pullback/component identity, convergence and integrability through the sums and cutoffs, and equality of the resulting final-field observables with the manuscript’s five quantities.

The audit found no such declaration on the inspected selected path. That establishes non-verification of the advertised paper-specific correspondence. It does not establish that the actual selected integrals are nonzero.

## 5. Fefferman compliance: the correct logical conclusion

Fefferman’s text imposes force decay/smoothness conditions (4)–(5), accepts only globally smooth bounded-energy solutions under (6)–(7), and states the forced breakdown alternative using existential quantifiers (`docs/navierstokes.txt:35–46`, `:74–81`). Therefore there are three distinct propositions:

1. **Lean endpoint proposition:** the selected formal theorem supplies a smooth residual-designed force, a pre-singular solution, bounded pre-singular energy, and speed blow-up on the inspected path.
2. **Paper-specific correspondence proposition:** the final selected Cartesian fields realise the manuscript’s five-moment mechanism and all of its stated transport identities.
3. **Literal CMI Alternative (C):** there exist admissible smooth data and force for which no global smooth bounded-energy solution exists.

The current source record supports proposition 1 on the inspected Lean path and does not establish proposition 2. Proposition 3 is not disproved merely because proposition 2 is absent, nor is it proved by the label `Witness` alone. The correct audit finding is:

\[
\boxed{\text{paper-specific machine-checked correspondence: NOT ESTABLISHED (CTR-005)}}
\]

with the narrower formal C-shaped endpoint kept separate. A future value-level mismatch, impossibility theorem, or proof that the residual bounds are not actually discharged would justify escalation. The present rebuttal does not supply one.

## Evidence ledger

* `docs/navier-stokes openai.txt:109–124` — residual terms may diverge while the summed residual extends smoothly.
* `docs/navier-stokes openai.txt:695–733` — multi-stage correction architecture and five radial equations as one correction step.
* `docs/navier-stokes openai.txt:6131–6150` — localisation residual and smooth force-extension requirements.
* `docs/navierstokes.txt:35–46, 74–81` — Fefferman conditions and Alternatives (C)/(D).
* `NavierStokes/CandidateFromLimits.lean:28–55, 80–112, 167–182` — traced residual, smooth extension, residual agreement, and candidate properties.
* `NavierStokes/ActualCandidateAssembly.lean:1079–1107, 1121–1151, 1177–1180` — physical-data route, estimates, endpoint `Witness`, and selected witness.
* `NavierStokes/MixedCandidateWitness.lean:26–31, 41–90` — selected schedule and physical finite-stage construction.
* `NavierStokes/DefectIncrementBounds.lean:214–220, 773–797` — intermediate `barMoment` and `FiveRows` identities.
