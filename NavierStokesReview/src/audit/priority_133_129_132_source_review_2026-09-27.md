# Priority 133/129/132 source review: comparator, current modes, heat debt, and residual naturality

Date: 2026-09-27
Scope: six reachable OpenAI source modules selected from the live semantic-coverage register.
Method: direct source inspection of imports, definitions, structures, and theorem statements.
Status: evidence for the reviewed modules only; this is not a completion claim for the repository.

## Executive result

This tranche strengthens the positive side of the audit. The source contains real coordinate bridges, native-scale cancellation, common-lift mode germs, heat-tail debt jets, harmonic solenoidal preservation, and residual naturality under explicit linear charts. These are not empty names.

It does not close the selected-field correspondence question. None of the six reviewed modules states a theorem identifying the final activated Cartesian field after `tsum`, curl, localisation, and periodisation with the paper tuple

\[
(M,I,J,S,C_p),
\]

nor does any reviewed declaration prove a concrete non-zero selected-field defect \(\Delta m\neq 0\). The correct classification remains: substantial intermediate mathematics is verified, while the endpoint transport claim is not established by these modules.

## 1. `ComparatorBridge.lean`

Source anchors: `NavierStokes/ComparatorBridge.lean:5-10,20-58,60-134,144-221`.

The module header says that it translates the project's physical differential operators to the comparator convention and normalises positive viscosity to one. The definitions `toComparator` and `fromComparator` only change argument order (`:20-26`). Theorems `divergence_eq`, `gradient_eq`, `laplacian_eq`, and `temporalDerivative_eq` establish operator correspondence (`:28-58`).

The rescaling block proves smoothness, periodicity, support, and derivative scaling for `rescale` and `rescaledForce` (`:60-174`). `forceConditionPeriodic_of_decay` converts smoothness, periodicity, and decay bounds into the comparator's force condition (`:117-134`). `GlobalSolutionOne` packages smoothness, periodicity, zero initial velocity, divergence freedom, and the residual equation (`:191-199`).

Audit result: this is a genuine comparator and operator bridge. It does not transport any radial profile observable into the comparator or endpoint package. It therefore supports the formal C/D packaging layer but does not resolve CTR-005.

## 2. `CurrentParticularPhysicalCoherence.lean`

Source anchors: `NavierStokes/CurrentParticularPhysicalCoherence.lean:5-10,21-50,52-68`.

The module's own description states that native potential and pressure transformation laws imply equality of actual physical modes after cancelling the native scale (`:5-10`). `unscale_of_ratioPower` proves the algebraic scale cancellation (`:21-28`). `localPotentialMode_eq_of_native` proves equality of two local potential modes when an explicit native transformation hypothesis is supplied (`:30-50`). `localPressureMode_eq_of_native` provides the corresponding pressure equality (`:52-68`).

Audit result: this is a real band-level coherence theorem. It concerns local modes and native-scale hypotheses. It does not assert a whole-space integral, a `barMoment` equality, or a final selected-field transport theorem.

## 3. `CurrentPhysicalModeGerms.lean`

Source anchors: `NavierStokes/CurrentPhysicalModeGerms.lean:5-10,23-70,670-777`.

The module constructs common-lift indices and proves common chart identities (`:23-70`). It defines the positive-radius set `positiveLift` and proves it open (`:670-673`). The `BandCoherence` structure explicitly records target/reference frames, base and mean transport, and block-field coherence (`:675-693`). Its comment limits these fields to primitive field, phase, and operator identities and does not present solved-wave or residual equality as an assumption.

`BandCoherence.source_on` and `source_eq` transport the residual source on the positive-radius region and its complement using support-zero hypotheses (`:694-757`). `residualBandAmplitude_eq` and `residualBandPressure_eq` identify band amplitudes and pressure once that source equality is established (`:758-777`).

Audit result: this closes genuine local source and mode coherences, including an explicit positive-radius domain split. It does not bridge the local germs to the final global Cartesian five-observable tuple, and it does not prove \(\Delta m\neq0\).

## 4. `ExtendedHeatDebts.lean`

Source anchors: `NavierStokes/ExtendedHeatDebts.lean:82-121,283-378,433-510,736-812,1022-1110,1173-1191`.

The module defines scalar correction, edit, square-edit, weighted debt jets, and their bounds. It proves differentiability, integrability, continuity, dominated convergence inputs, and iterated-derivative identities for these objects (`:82-121,283-378`). It then defines `physicalEdit`, `physicalPressure`, `physicalEnergy`, and `physicalAngular`, with equalities and original-data reductions (`:433-510`).

The later block proves existence of physical debt jet bounds and normalised C1 bounds (`:736-812`). The final blocks establish physical debt integrability and derivative-integral identities (`:1022-1110`) together with joint smoothness and original-value equalities (`:1173-1191`).

Audit result: this is substantive intermediate profile/debt analysis. It is not endpoint transport. The source statements are scalar/profile-level and do not expose the final Cartesian `tsum`/curl/localisation field or a theorem of the form

\[
\operatorname{moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})=(M,I,J,S,C_p).
\]

## 5. `HarmonicStructurePreservation.lean`

Source anchors: `NavierStokes/HarmonicStructurePreservation.lean:23-81,83-131,147-168`.

The module proves algebraic addition and carrier identities for harmonic blocks (`:23-55`), smoothness of amplitude, mode, pressure, and phase (`:61-106`), and cylindrical-divergence and solenoidal preservation for added blocks (`:83-131`). It also proves zero-mode and zero-pressure preservation under addition and carriers (`:147-168`).

Audit result: these are useful local harmonic and incompressibility invariants. They do not quantify over the selected endpoint field or identify global radial moments.

## 6. `PhysicalResidualNaturality.lean`

Source anchors: `NavierStokes/PhysicalResidualNaturality.lean:56-199,201-319,532-553,678-777,1029-1158,1162-1195`.

The module defines coefficient fields, frames, and state coherence under continuous-linear equivalences. `FrameOn` proves naturality of inverse-radius, scalar/vector Laplacian, gradient, linear residual, and nonlinear residual operators (`:201-319`). `residualSource_naturality` transports source terms under the same frame hypotheses (`:532-553`).

`BandCoherence` and `PositiveSupport` provide local frame, base, mean, block, and support hypotheses (`:678-736`), then derive source, amplitude, and pressure transport (`:694-777`). `StateOn` proves naturality for angular, axial, radial, reduced mean, source, and good residuals (`:1029-1158`). `stateView` constructs a pulled-back state and `stateView_coherent` proves the corresponding local coherence (`:1162-1195`).

Audit result: this is a substantial local residual-naturality layer. It proves transport of residual/state expressions under explicit chart hypotheses. It does not prove transport of the paper's five global radial observables through the final infinite sum, spatial localisation, or endpoint packaging.

## Cross-module classification

| Question | Result from this tranche |
|---|---|
| Are these modules empty or fake? | No. They contain substantive operator, mode, debt, support, solenoidal, and residual theorems. |
| Do they prove local transport/coherence? | Yes, under explicit chart, scale, support, and regularity hypotheses. |
| Do they prove final `(M,I,J,S,Cp)` transport? | Not in the inspected declarations. |
| Do they prove a concrete selected-field `Δm ≠ 0`? | No. |
| Do they derive `False` for the active endpoint? | No. |
| Does this alter the audit verdict? | It narrows the negative claim: intermediate layers are real; endpoint paper-to-code transport remains unestablished. |

## Register action

The six path-qualified modules are added to `semantic_coverage_register.py` and will be regenerated into the JSON, Markdown, and HTML registers. The counts must be read from the regenerated authoritative JSON, not inferred from this report.
