# Priority 184: selected-path foundation and smooth-force audit

**Date:** 2026-09-29
**Status:** source-checked; no selected-path compiler shortcut found; endpoint correspondence remains open

## Executive finding

The latest rebuttal correctly identifies a serious audit obligation, but it
overstates what follows from the missing five-observable export. The selected
Lean path is not proved by a bare `NativeBounds` assumption and is not an
axiom-backed empty shell. It constructs actual stage data, derives residual
jet rates and locally uniform limits, transports vanishing joint jets through
the cut/periodic assembly, and derives `force_smooth` from those premises.

At the same time, the source inspection still finds no theorem on the
selected endpoint identifying the completed Cartesian velocity, pressure, or
force with the manuscript's five reduced-profile observables
\((M,I,J,S,C_p)\). The two statements are compatible:

\[
 H_{\mathrm{selected}}
 \Longrightarrow J_{\mathrm{flat}}
 \Longrightarrow F\in C^\infty,
\]

does not establish

\[
 J_{\mathrm{flat}}
 \Longrightarrow
 \operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}})
 =(M,I,J,S,C_p).
\]

This remains `CTR-005`: the complete manuscript-to-endpoint correspondence
is **NOT ESTABLISHED**. It is not yet a proof that the selected force is
nonsmooth, that the selected moments are nonzero, or that Fefferman's
Alternative (C) is false.

## 1. Source checks performed

The audit inspected the selected-path modules without changing the OpenAI
source tree:

| Layer | Source evidence | Finding |
|---|---|---|
| Endpoint envelope | `NavierStokes/ActualCandidateAssembly.lean:1121--1151`, `:1177--1180` | `Witness` is a concrete proposition and `selected_witness` is proved from `witness`; its contract contains schedules, sums, extensions, candidate properties, residual/force conclusions, and blow-up data, but no named five-observable equality. |
| Residual-to-force bridge | `NavierStokes/CandidateFromLimits.lean:80--112` | `force_smooth` is derived from the residual field, hypotheses, boundary limits, and the Taylor--Borel-style construction; it is not a free theorem from a symbol named `NativeBounds`. |
| Cut and periodic assembly | `NavierStokes/MixedPeriodicAssembly.lean:231--237`, `:283--315`, `:339--365` | Vanishing joint jets and locally uniform boundary limits are transported through the cut/periodic residual assembly and then used in the candidate construction. |
| Classical construction | `NavierStokes/MixedPeriodicAssembly.lean:228--229` | `Classical.choice` selects extensions from existing `AwayExtensions` propositions. This is a standard Lean foundational dependency, not a custom axiom and not evidence of a compiler bypass. |
| Global radial observable | `NavierStokes/DefectIncrementBounds.lean:214--237` | `barMoment` is a noncomputable integral-valued definition. Integrability is supplied separately by `Shell.barIntegrable`; the definition itself does not assert the selected field's target five-tuple. |
| Completion probes | `NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean`, `SelectedMixedProductionBarMoment.lean`, `SelectedMixedProductionTorusAverage.lean` | The probes expose finite-prefix, torus-average, and `barMoment` interfaces, but no completed selected-field equality to the paper tuple. |

The targeted files contain `noncomputable` sections because they use
integrals, infinite sums, limits, and classical selections. The targeted
search found no explicit `axiom`, `sorry`, or `admit` in these selected-path
files. A fresh Lean rebuild was not claimed because `lean`, `lake`, and
`elan` are not available in the current shell.

## 2. Correction to the submitted five-step rebuttal

### Supported part

The manuscript makes the five radial corrections mathematically important.
It uses them for profile matching, shear-modulation restoration, and the
finite-dimensional compatibility corrections. Therefore, the review must not
describe the moments as optional notation or irrelevant scaffolding.

### Unsupported part

The following implication is not established by the supplied argument:

\[
 \|u(t)\|_{\infty}\to\infty
 \Longrightarrow
 \|\partial_tu\|,\|(u\cdot\nabla)u\|,\|\Delta u\|,\|\nabla p\|
 \to\infty.
\]

Velocity norm blow-up does not imply termwise divergence of every differential
summand. The residual is a sum, and the manuscript explicitly describes
arranged cancellation between singular contributions. Thus the correct
question is not whether cancellation is possible. It is whether the selected
Lean hypotheses proving flat residual jets are themselves connected to the
paper's five-observable identities after the selected curl, cutoff, series,
periodisation, averaging, and radial-integration operations.

The audit therefore rejects the stronger claim that `force_smooth` is merely
an assumed interface fact, but retains the narrower and source-supported
claim that the endpoint has not exported the paper-level identification.

## 3. Why this does not make the two conclusions contradictory

There are three different propositions:

1. **Selected software proposition:** the constructed selected objects satisfy
   the endpoint's residual, regularity, support, energy, and blow-up fields.
2. **Paper mechanism proposition:** the completed selected objects realise the
   manuscript's particular five-moment mechanism and its stated observable
   identities.
3. **Literal CMI proposition:** the selected data satisfy every condition of
   Fefferman's chosen alternative, including the required global smoothness,
   decay/periodicity, and energy conditions.

The source audit supports substantial parts of (1). It has not established
(2) at the selected-field export. It also cannot promote (3) to a failure
merely from the absence of a named moment theorem, because the current Lean
path separately proves smooth-force and endpoint properties from residual-jet
data. A failure of (3) would require a selected mismatch, a failed CMI
condition, an impossibility theorem, or a contradiction.

This is not a concession to OpenAI's claim. It is the exact boundary needed
to avoid replacing a correspondence failure with an unproved physical
refutation. The paper-to-code claim remains unestablished until the selected
observable transport theorem is found or its failure is proved at value level.

## 4. Required next gate

The next decisive theorem search must be value-level, not another interface
scan. It must inspect the selected composition

\[
 \operatorname{barMoment}\!\left(
 \operatorname{torusAverage}\!\left(
 \operatorname{periodise}\!\left(
 \operatorname{curl}(\operatorname{tsum}(A_j))\right)
 \right)\right)
\]

including cutoffs, pressure, integrability, and the paper's five target
coordinates. The admissible outcomes are:

- an explicit selected-field equality to \((M,I,J,S,C_p)\);
- a selected-field mismatch or impossibility proof;
- a source-grounded proof that the paper's five quantities are not intended
  as endpoint observables, accompanied by a revised correspondence claim.

Until one occurs, retain `CTR-005 = NOT ESTABLISHED`, not `[FORMALLY
REFUTED]` and not `VERIFIED CMI SOLUTION`.

## Evidence boundary

This report records a source audit, not a fresh Lean compilation. It does not
claim that `noncomputable` or `Classical.choice` is a loophole. It does not
claim that upstream moment identities are dead code. It does not claim that
the selected force is smooth for reasons unrelated to the physical
construction. It records that the actual selected residual-jet route is
substantive while the final named five-observable transport identity remains
unlocated.
