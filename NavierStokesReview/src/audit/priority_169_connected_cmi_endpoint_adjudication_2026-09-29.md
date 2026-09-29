# Priority 169: connected CMI endpoint adjudication

**Date:** 2026-09-29
**Scope:** Fefferman's connected physical-admissibility specification, the selected whole-space Lean path, and the manuscript's five-moment mechanism.
**Status:** source-level adjudication complete; full imported axiom replay remains a separate build item.

## Decision

The audit must keep two propositions separate:

\[
\begin{aligned}
P_{\mathrm{C}}^{\mathrm{Lean}} &: \text{the exported Lean route proves the declared C-shaped existential proposition},\\
P_{\mathrm{paper}} &: \text{the exported Lean route machine-checks the manuscript's stated five-moment construction}.
\end{aligned}
\]

The current source record supports the first proposition on the inspected path and does not establish the second. It does **not** support the stronger conclusion that Alternative (C) is false merely because the Witness proposition does not expose a named five-tuple.

This is not a retreat from the five-moment finding. It is the logically necessary distinction between a theorem proving a target proposition through a sufficient residual-flatness route and a theorem proving that the route is the same physical mechanism described in the manuscript.

## 1. Fefferman's connected admissibility specification

Fefferman first defines the PDE data and then connects them to physical reasonableness:

\[
\text{(1),(2),(3)}
\longrightarrow
\begin{cases}
\text{whole-space data (4),(5)}\\
\text{accepted solution class (6),(7)}
\end{cases}
\]

or, after choosing the periodic branch,

\[
\text{(1),(2),(3)}
\longrightarrow
\text{periodic data (8),(9)}
\longrightarrow
\text{accepted solution class (10),(11)}.
\]

The words “given, externally applied force”, “physically reasonable”, “only if”, “Alternatively”, “Thus, we assume”, “We then accept”, and “retaining the heart of the problem” must therefore be read as a connected semantic network. In the whole-space branch, (4), (5), (6), and (7) are not independent suggestions. In the periodic branch, (8), (9), (10), and (11) are mandatory after that branch is selected.

The phrase “we may look for spatially periodic solutions” is a branch choice, not a relaxation of the conditions after the choice. “Retaining the heart” identifies the purpose of the leeway: the solver may choose one of the four stated targets, but the chosen target still requires its complete displayed data and accepted-solution clauses.

The exact source is docs/navierstokes.txt, especially lines 25–81. The later discussion of finite blow-up and weak solutions reinforces that the problem concerns global smooth physically reasonable solutions, not merely a local identity for the differential operator.

## 2. What the selected Lean path actually proves

The selected path contains the following concrete chain:

\[
\begin{aligned}
&\text{ActualCandidateAssembly.physicalData}\\
&\quad\to \text{GluedStageEstimates.actualStageEstimates}\\
&\quad\to \text{ActualCycleResidualBounds.finite\_residual\_rates}\\
&\quad\to \text{StageEstimates.exists\_schedule}\\
&\quad\to \text{VanishingJointJets}\\
&\quad\to \text{CandidateFromLimits.tracedResidual\_smooth}\\
&\quad\to \text{CandidateFromLimits.force\_smooth}\\
&\quad\to \text{CandidateProperties}\\
&\quad\to \text{GlobalFiniteEnergySolution comparison}\\
&\quad\to \text{ComparatorR3Theorem.nav\_stokes\_breakdown\_R3}.
\end{aligned}
\]

The source-level details are:

1. ActualCandidateAssembly.physicalData obtains actual physical field representations through ActualPhysicalPrefixFields.physicalFields_all.
2. ActualCycleResidualBounds.finite_residual_rates uses the actual cycle invariant, StateRealization, native residual bounds, exterior germs, and base exterior estimates to prove the finite-stage residual jet rates.
3. MixedDiagonalResidual.exists_physical_schedule_residual_zero converts those rates into a common schedule with VanishingJointJets.
4. CandidateFromLimits.tracedResidual_smooth and force_smooth prove a globally smooth Taylor–Borel extension of the residual force. The force agrees with the activated residual for 0 ≤ t < 1 and has compact positive-time support in the candidate path.
5. CandidateProperties records pre-singular smoothness, compact velocity and pressure support, smooth force, positive-time force support, zero initial velocity, incompressibility, the Navier–Stokes residual identity, finite energy on [0,1), and speed unboundedness at time one.
6. The whole-space comparison module maps any global smooth finite-energy competitor with the same force and initial data to a contradiction with the pre-singular candidate blow-up. ComparatorR3Theorem.nav_stokes_breakdown_R3 then has the existential shape of Fefferman's Alternative (C), including force decay and nonexistence of a global accepted solution.

This means that the rate contracts are not shown to be fabricated or admitted through an empty NativeBounds premise. The selected construction has a real residual-flatness proof route.

## 3. Where the five-moment correspondence remains absent

The manuscript's Appendix C defines the five profile moments and uses exact restoration to preserve the exterior fields, pressure, heat exterior, and stress quantities. The upstream Lean source contains genuine corresponding profile and rank machinery, including FiveProfileMoments.physicalMoments, PositiveOrderMoments.moments_repair, FiveRowRank.FiveRows, and the intermediate CorrectionState.debt and ZeroMasses structures.

The inspected selected endpoint does not, however, contain a theorem of the following form:

\[
\operatorname{Moments}\!\left(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}}\right)
= (M,I,J,S,C_p),
\]

nor a definitionally equivalent theorem transporting the five profile integrals through the selected potential sums, Cartesian curl, localisation, periodisation, infinite summation, pressure assembly, residual extension, and force construction.

The type-level boundary is visible in ActualCandidateAssembly.Witness: it packages the selected schedule, three sums, away extensions, forcing, CandidateProperties, CandidateConsequences, the H3 blow-up limit, force decay, and boundary jets. It does not carry a named final five-observable equality. The zero-sorry interface probes therefore establish a real non-entailment result: the endpoint contract is insufficient by itself to certify the manuscript's five-coordinate identity. They do **not** establish that the concrete selected integrals are numerically nonzero.

## 4. Why this does not produce a contradiction

The logical implication is:

\[
\text{missing exported moment identity}
\;\Longrightarrow\;
\text{paper-to-endpoint five-moment correspondence is not established},
\]

but not:

\[
\text{missing exported moment identity}
\;\Longrightarrow\;
\text{no smooth force or no CMI Alternative (C)}.
\]

The latter would require an additional theorem showing that the concrete selected residual-flatness route cannot hold without the transported five moments, or a direct selected-field mismatch, or a failed Fefferman premise. The current source record does not contain that theorem. It contains a different formal route: it proves the residual jet limits as concrete consequences of the cycle invariant and physical-data records.

This is the point that must not be expressed ambiguously. A proof of the same target proposition can be logically valid while failing to demonstrate that it formalises the paper's advertised proof mechanism. Conversely, if the paper's five-moment argument is indispensable to the mathematical justification of the concrete rate records, that dependency still needs to be reconstructed and checked. The current endpoint does not make that dependency visible or prove it by a selected-field transport theorem.

## 5. Force provenance and the word “external”

The manuscript openly uses the inverse residual construction

\[
f=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p,
\]

and states that the challenge is to choose a blowing-up flow for which the residual extends smoothly. Fefferman's prose calls f a “given, externally applied force”, which supplies a physical interpretation and makes provenance a legitimate audit issue. However, the displayed existential statement (C) does not add a formal independence predicate saying that f must be chosen without reference to the selected trajectory. Therefore:

- residual-defined forcing is a causal and physical-provenance concern;
- it is not, by itself, a formal contradiction of the existential C predicate;
- it becomes a CMI failure only if the constructed force fails the explicit smoothness and decay conditions or the no-global-solution conclusion fails.

The correct adverse conclusion is consequently that the public claim “Lean machine-checks the manuscript's complete physical proof” is not established by the current selected endpoint. The stronger claim “the formal C-shaped proposition is false” is not supported by the present evidence.

## 6. Controlling status matrix

| Claim | Current status | Reason |
|---|---|---|
| Fefferman's physical-admissibility clauses are connected requirements | **Established** | Exact wording and branch structure in docs/navierstokes.txt |
| Concrete selected residual-flatness route exists | **Established on source path** | PhysicalData → finite residual rates → vanishing jets → smooth force |
| Smooth force and pre-singular candidate properties are exported | **Established on source path** | CandidateProperties and CandidateFromLimits |
| Formal C-shaped existential proposition is derived | **Established on inspected source path** | comparator bridge and ComparatorR3Theorem |
| Selected endpoint transports (M,I,J,S,Cp) through the full Cartesian construction | **Not established** | No located selected-field identity or definitionally equivalent bridge |
| The selected force is actually nonsmooth because moments are absent | **Not proved** | Requires a selected-value defect or impossibility theorem |
| Alternative (C) is false solely because the endpoint omits the tuple | **Rejected as an unsupported inference** | The endpoint has an independent residual-flatness route |
| OpenAI's complete paper-to-code claim is established | **Not established** | The advertised five-moment mechanism is not connected to the exported selected fields |

## 7. Build and axiom caveat

On 2026-09-29, direct compilation succeeded for:

- NavierStokes/ComparatorR3Theorem.lean;
- NavierStokes/ActualCandidateAssembly.lean.

The imported HeadlineAxiomProbe.lean replay could not complete because building NavierStokes.ComparatorSolution exceeded the 124-second command limit. The associated Lean processes were cleared. This update therefore does not reassert a fresh transitive axiom report; it records the source-level theorem path and the exact replay limitation separately.

## Evidence links

- [Priority 168: Fefferman physical admissibility and force chain](priority_168_fefferman_physical_admissibility_and_force_chain_2026-09-29.md)
- [Selected-field composition trace](priority_167_selected_field_composition_trace_2026-09-29.md)
- [Selected endpoint moment transport obstruction](../../evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md)
- [Fefferman connected semantic crosswalk](../../../docs/CMI_OpenAI_Full_Semantic_Crosswalk.md)
