# Priority 183: force smoothness and five-moment rebuttal adjudication

**Date:** 2026-09-29
**Status:** source-checked; rebuttal partly rejected; `CTR-005` remains a
selected-field correspondence finding, not a selected-field contradiction.

## Executive finding

The submitted rebuttal correctly identifies the five-moment corrections as
load-bearing in the manuscript. It overstates three stronger conclusions:

1. \\(\\|u(t)\\|_\\infty\\to\\infty\\) does not imply that each term in
   \\(\\partial_tu+(u\\cdot\\nabla)u-\\Delta u+\\nabla p\\) diverges.
2. The manuscript does not establish that the five-moment block is the only
   mechanism contributing to residual regularity.
3. The Lean force theorem is not obtained from a bare `NativeBounds` contract.
   It is derived from actual residual derivative limits, although the review
   still has not located the final theorem identifying every completed
   Cartesian observable with the paper tuple \\(M,I,J,S,C_p\\).

The correct conclusion is therefore:

\\[
 H_{\\rm selected}
 \\Longrightarrow J_{\\rm flat}
 \\Longrightarrow F\\in C^\\infty,
 \\]

is source-supported, while the separate paper-correspondence implication

\\[
 J_{\\rm flat}
 \\Longrightarrow
 \\operatorname{PaperMoments}(u_{\\rm selected},p_{\\rm selected})
   =(M,I,J,S,C_p)
\\]

has not been established at the exported endpoint. This is a genuine
correspondence gap, not evidence that the force proof is an empty interface
construction.

## 1. What the manuscript actually says about cancellation

The manuscript directly states that the individual residual terms may diverge,
while the construction arranges cancellation in their sum and all derivatives
(`docs/navier-stokes openai.txt:109--124`). It then separates several
operations:

- averaged wave flux cancels the leading background stress divergence;
- angular harmonics, auxiliary means, and radial integral defects receive
  separate corrections (`:695--703`);
- wave-amplitude equations, covariance updates, auxiliary-time inversion, and
  the five radial equations handle different components of the cycle
  (`:711--731`);
- the full residual is recomputed, including curl, cutoff, nonlinear, and
  interaction terms (`:732--735`, `:761--784`).

The five equations are therefore substantive and load-bearing. They are not,
however, proved by these passages to be the sole mathematical route by which
the total residual can become smooth. The manuscript itself assigns distinct
roles to the other operations. A claim of uniqueness would require a theorem
excluding those routes; the submitted rebuttal supplies no such theorem.

The manuscript also makes the physical role of the moments clear: matching
the five radial integrals preserves the exterior fields and the functions
\\(Q_s,N_s\\) (`:492--496`, `:6965--6978`), and a localised correction restores
all five after shear modulation (`:539--546`, `:8245--8251`). This supports a
strong load-bearing claim without proving a final Cartesian identity by mere
terminology.

## 2. Why the termwise-divergence inference fails

From

\\[
 \\|u(t)\\|_\\infty\\to\\infty
\\]

one cannot infer

\\[
 \\|\\partial_tu\\|,\\quad
 \\|(u\\cdot\\nabla)u\\|,\\quad
 \\|\\Delta u\\|,\\quad
 \\|\\nabla p\\|
 \\	o\\infty
\\]

term by term. The norm limit gives no such derivative estimate. Moreover, the
residual is a sum, so singular summands can cancel. The manuscript's own
background calculation says that the background residual is unbounded, then
adds oscillatory pulses and further corrections to make the total residual
extend smoothly (`docs/navier-stokes openai.txt:118--124`). That is consistent
with arranged cancellation, not with a proof of divergence of every final
summand.

## 3. The actual Lean force path

The inspected declarations give the following dependency chain.

1. `ActualCandidateAssembly.estimates` is defined from
   `GluedStageEstimates.actualStageEstimates`, actual stage representations,
   and `physicalData` (`NavierStokes/ActualCandidateAssembly.lean:1079--1098`).
2. `ActualCycleResidualBounds.Invariant.residual_jetRate` derives the physical
   residual jet rate from an actual invariant, the state-realisation theorem,
   and concrete `PhysicalData`, rather than accepting a future force
   (`NavierStokes/ActualCycleResidualBounds.lean:1156--1173`).
3. `finite_residual_rates` lifts those actual cycle bounds into the finite
   mixed-diagonal residual used by stage assembly (`:1187--1206`).
4. `StageEstimates.exists_schedule` turns the stage estimates into a selected
   schedule and `VanishingJointJets`
   (`NavierStokes/MixedCandidateAssembly.lean:67--77`).
5. `CandidateFromLimits.tracedResidual_smooth` uses the actual residual
   derivative recurrence and supplied locally uniform limits
   (`NavierStokes/CandidateFromLimits.lean:39--66`).
6. `force_smooth` is then a theorem about the Taylor--Borel extension, and
   `force_eq_activated_residual` identifies that force with the actual
   activated residual for `0 ≤ t < 1`
   (`NavierStokes/CandidateFromLimits.lean:80--112`).

The logical form is consequently:

\\[
 \\text{actual residual-rate and limit premises}
 \\Longrightarrow F\\in C^\\infty
 \\land
 \\bigl(F=R(u,p)\\text{ on }0\\le t<1\\bigr).
\\]

It is not accurate to say that Lean merely assumes `NativeBounds` and thereby
assumes force smoothness. It is accurate to say that the endpoint does not
export a separate theorem identifying the completed field's paper-level five
observables with the reduced-profile moment tuple.

## 4. Where the five-moment dependency actually appears upstream

The source contains more than an import edge. For example,
`ConstructedSlowBase.nominal_finiteIdentities` proves the finite residual
identity and `nominal_jetRate` and `nominal_allJetsFlat` consume it
(`NavierStokes/ConstructedSlowBase.lean:224--256`). The modified construction
has the analogous chain (`:351--383`). This is evidence that the repaired
profile identities feed residual flatness upstream.

That fact does not settle the remaining endpoint question. The exported
`ActualCandidateAssembly.Witness` does not state a named equality of the
completed Cartesian field to the five paper observables. The missing bridge
still includes the selected `tsum`, spatial curl and cutoff terms,
periodisation, torus averaging, radial pullback, integrability/support, and
the exact identification of the paper's functions with the endpoint fields.

## 5. Adjudication of the submitted rebuttal

| Submitted claim | Finding |
|---|---|
| The five moments are load-bearing | **Supported.** The manuscript explicitly uses them for exterior matching, shear restoration, and three compatibility corrections. |
| They are the only cancellation mechanism | **Not established.** The manuscript separately assigns roles to wave flux, covariance, auxiliary-time, pressure, cutoff, nonlinear, and summation steps. |
| Blow-up proves all residual summands diverge | **False inference.** Norm blow-up alone gives no termwise derivative conclusion. |
| `force_smooth` is an abstract jet substitute unlinked to physical data | **Too strong.** The inspected Lean chain derives actual residual rates and limits from concrete cycle/invariant data. |
| No final named five-moment endpoint identification has been found | **Supported.** This remains `CTR-005`. |
| The selected force is therefore proven nonsmooth or CMI C is refuted | **Not proved.** That requires a selected mismatch, failed C condition, impossibility theorem, or contradiction. |

## Audit status

`CTR-005` remains **NOT ESTABLISHED** for the complete manuscript-to-endpoint
correspondence. This classification means the published paper's full
five-observable explanation has not been shown to be the exact theorem proved
by the exported endpoint. It does not mean that the selected residual-rate
route is empty, that `force_smooth` is an axiom, or that a selected force
defect has already been proved.

**Current next gate:** locate or rule out a theorem connecting the completed
selected Cartesian field and force to the paper's five radial observables after
the actual `tsum`, curl, localisation, periodisation, averaging, and radial
integration operations. Until that gate is closed, do not upgrade the finding
to a literal CMI failure or `[FORMALLY REFUTED]`.
