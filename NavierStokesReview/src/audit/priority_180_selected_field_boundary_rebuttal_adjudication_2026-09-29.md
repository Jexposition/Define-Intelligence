# Priority 180: selected-field boundary and smooth-force rebuttal adjudication

**Date:** 2026-09-29  
**Status:** source-checked; `CTR-005` remains **NOT ESTABLISHED**; no selected
defect or literal C/D failure has been proved.

## Executive finding

## 0. Connected Fefferman adjudication: what is and is not falsified

The connected reading of Fefferman's statement changes the conclusion that may
be drawn from the missing selected-field moment identity. Fefferman's words
“physically reasonable” are operationalised by the surrounding specification:
for the whole-space branch, the data satisfy `(4),(5)` and an accepted global
solution satisfies `(6),(7)` in addition to `(1)--(3)`. The phrase
“Alternatively ... may look for” permits the periodic branch; it does not
waive its conditions, because “Thus”, “In place of”, and “We then accept” bind
`(8),(9)` and `(10),(11)` after that branch is chosen.

The inspected comparator definitions encode that whole-space package. In
`NavierStokes/ComparatorDefinitions.lean`,
`InitialVelocityConditionDecay` contains smoothness, divergence-freeness, and
all-order spatial decay corresponding to `(4)`; `ForceConditionDecay` contains
smoothness on the forward half-space and all-order space-time decay
corresponding to `(5)`; and
`NavierStokesExistenceAndSmoothnessRn` contains the PDE, incompressibility,
initial condition, global smoothness, square-integrability, and uniform
energy requirements corresponding to `(1)--(3),(6),(7)`. The theorem
`NavierStokes.Comparator.navier_stokes_breakdown_R3` then proves the matching
existential/nonexistence proposition from the constructed candidate.

Consequently, the following implication is not justified:

\[
\neg\,\texttt{WitnessMomentTransport}
\quad\Longrightarrow\quad
\neg\,\texttt{FeffermanC}.
\]

The missing moment theorem does not, by itself, falsify the operational C
predicate if the independently supplied Lean route really proves every C
condition above. The residual-defined-force concern also requires care. The
manuscript explicitly says that an external force can be defined as the
residual, and that the challenge is to arrange cancellation so the total
residual and all derivatives extend smoothly. Fefferman's displayed C
predicate requires a smooth force satisfying `(4),(5)`; it does not contain a
separate formal independence-from-the-selected-trajectory predicate. Thus
residual provenance is a serious physical-interpretation objection, but it is
not by itself a formal failure of C.

The audit therefore has two distinct verdicts:

1. **Operational C predicate:** established on the inspected Lean comparator
   path, subject to the recorded build and axiom-dependency checks.
2. **OpenAI manuscript-to-Lean proof identity:** not established. The source
   record has not located a theorem identifying the completed selected
   Cartesian velocity, pressure, force, and residual construction with every
   manuscript-level consequence of the five-moment mechanism after summation,
   curl, localisation, periodisation, averaging, and endpoint packaging.

The second verdict does not say that the C proposition is false. It says that
the repository may have proved the C proposition by a formally adequate route
without yet proving that the route is the manuscript's advertised
five-moment route. A literal C refutation still needs a failed connected
condition, a concrete selected mismatch, an impossibility theorem, or a
contradiction. This distinction is required by the source text and is not a
concession that Fefferman's physical wording is optional.

The latest rebuttal identifies the right scientific issue but overstates what
the source currently proves. The five equations

\[
(M,I,J,S,C_p)=0
\]

are load-bearing in the manuscript's profile matching and correction
architecture. However, the Lean endpoint does not derive smooth forcing from a
bare `NativeBounds` assumption. It constructs a concrete residual-limit route:

\[
H_{\rm selected}
\Longrightarrow J_{\rm flat}
\Longrightarrow F_{\rm smooth},
\]

where `H_selected` contains actual stage representations, physical residual
estimates, a selected schedule, and locally uniform limits for every residual
derivative. The unresolved correspondence is the separate implication

\[
J_{\rm flat}
\Longrightarrow
\operatorname{PaperMoments}(u_{\rm selected},p_{\rm selected})
 =(M,I,J,S,C_p),
\]

which was not located at the selected endpoint or in the inspected bridge
declarations.

This is a real paper-to-code gap. It is not evidence that the force theorem is
an empty interface proof, and it is not yet a proof that the selected force is
nonsmooth or that Fefferman Alternative (C) fails.

## 1. What the latest rebuttal gets right

The manuscript treats the five cumulative radial equations as substantive
correction data. It records the moment changes caused by modulation, restores
five quantities with five correction functions, and uses the correction cycle
alongside wave, covariance, auxiliary-time, pressure, cutoff, nonlinear, and
summation operations (`docs/navier-stokes openai.txt:523--546,695--784`).

Therefore the following inference is justified:

\[
\text{profile/correction identities}
\not\Rightarrow
\text{final selected Cartesian five-observable identity}
\]

unless the representation, convergence, localisation, averaging, radial
pullback, and axis-limit steps are connected by theorems for the selected
fields. The review must not describe the moments as optional notation or the
upstream correction branch as dead code.

## 2. The rebuttal's first overclaim: blow-up does not imply termwise divergence

The assertion

\[
\|u(t)\|_{\infty}\to\infty
\quad\Longrightarrow\quad
\partial_tu,\ (u\cdot\nabla)u,\ \Delta u,\ \nabla p
\text{ each diverge}
\]

does not follow from the norm limit. The residual is a sum, and cancellation
is a statement about that sum. For instance,

\[
T_1(t)=\frac1{1-t},\qquad
T_2(t)=-\frac1{1-t}+g(t)
\]

has divergent summands and a regular total. Conversely, an unbounded field
does not determine the behaviour of every differentiated component. The
manuscript itself states the weaker proposition that individual residual terms
may diverge while the total residual and its derivatives extend smoothly
(`docs/navier-stokes openai.txt:109--124`).

The source therefore supports **arranged cancellation**, not the stronger
claim that termwise divergence has already been proved for the selected field.

## 3. The rebuttal's second overclaim: the five equations are not shown to be
the only cancellation operation

The five-equation block is a necessary, load-bearing finite-dimensional block
within the manuscript's stated mechanism. It is not source-established as the
only operation that can yield a smooth total residual. The manuscript also
retains wave-amplitude equations, signed covariance correction, auxiliary-time
inversion, pressure reconstruction, cutoff commutator terms, full nonlinear
residual recomputation, shrinking-cutoff summation, and all-order flatness
(`docs/navier-stokes openai.txt:695--784,6101--6153`).

To prove “only mechanism” one would need a necessity theorem excluding those
other routes. Neither the cited manuscript passages nor the inspected Lean
declarations supplies that theorem. The defensible statement is:

> The five-moment mechanism is load-bearing in the manuscript, but the current
> audit has not proved that it is the sole possible route to residual
> regularity, nor that the selected field has a nonzero moment defect.

## 4. What Lean actually proves about the force

The selected endpoint contains a genuine chain, not a free-standing smoothness
axiom:

1. `ActualCandidateAssembly.physicalData` constructs `PhysicalData` from actual
   cycle representations and physical prefix fields
   (`NavierStokes/ActualCandidateAssembly.lean:1079--1088`).
2. `ActualCandidateAssembly.estimates` feeds those data into
   `GluedStageEstimates.actualStageEstimates`
   (`:1090--1098`).
3. `StageEstimates.exists_schedule` derives a schedule and
   `VanishingJointJets` from the finite residual estimates
   (`NavierStokes/MixedCandidateAssembly.lean:67--91`).
4. `CandidateFromLimits.tracedResidual_smooth` derives smoothness from the
   actual residual derivative recurrence and locally uniform endpoint limits
   (`NavierStokes/CandidateFromLimits.lean:45--66`).
5. `CandidateFromLimits.force_smooth` then proves smoothness of the Taylor--Borel
   force extension, and `force_eq_activated_residual` identifies it with the
   activated residual for \(0\le t<1\) (`:80--112`).
6. `ActualCandidateAssembly.Witness` packages the resulting force, smoothness,
   `CandidateConsequences`, blow-up, and boundary jets
   (`NavierStokes/ActualCandidateAssembly.lean:1121--1151`), and
   `selected_witness` specialises the proposition (`:1177--1181`).

Thus the accurate logical form is:

\[
\text{concrete residual-limit premises}
\Longrightarrow
F\in C^\infty
\quad\text{and}
\quad
F=R(u,p)\text{ on }0\le t<1.
\]

The endpoint does not, however, contain the additional theorem

\[
\operatorname{PaperMoments}(u,p)=(M,I,J,S,C_p).
\]

That omission prevents a claim that Lean has verified the manuscript's complete
five-moment explanation. It does not convert the smooth-force proof into an
unproved `NativeBounds` assumption.

## 5. Why the type boundary still matters

`Witness` contains actual fields and consequences, but its proposition has no
`Debt`, `FiveRows`, `barMoment`, or paper-observable equality. The selected
potential is an actual `tsum` (`NavierStokes/SolenoidalDiagonal.lean:31--67`),
the selected velocity is obtained by spatial curl
(`:186--222`), and the localisation layer exposes the cutoff-gradient
commutator (`NavierStokes/SpatialLocalization.lean:165--207`). Yet the
observable interface remains a different domain:

\[
\texttt{barMoment}:
\texttt{ScalarField (Point P)}\to\texttt{ScalarField P},
\]

whereas the endpoint field is an activated Cartesian `VelocityField`. A bridge
must still prove the scalar lift, coordinate pullback, integrability, finite
prefix to `tsum` passage, torus-average interchange, commutator contribution,
direct-field contribution, and axis-inclusive identification with the named
paper observables. The existing review completions prove several local or
conditional pieces, not this complete equality.

## Adjudication

| Claim | Result |
| --- | --- |
| Five moments are load-bearing in the manuscript | **Confirmed** |
| Velocity blow-up proves every residual summand diverges | **Not proved; overclaim** |
| Five moments are the only residual-cancellation operation | **Not proved; overclaim** |
| `force_smooth` is a free-standing generic-rate assumption | **False on the inspected path** |
| The selected endpoint exports the final paper five-observable identity | **Not located; `CTR-005` remains** |
| A selected nonzero defect, force nonsmoothness, impossibility, or `False` has been proved | **No** |

## Current conclusion

The latest rebuttal should be corrected, not accepted wholesale. The strongest
source-grounded conclusion is:

> OpenAI's Lean path proves a substantive conditional forced candidate and a
> smooth residual-designed force from concrete residual-limit data. The
> manuscript's five-moment repair system is load-bearing, but the inspected
> endpoint does not identify those paper observables with the final selected
> Cartesian field. Therefore complete paper-to-endpoint verification remains
> **NOT ESTABLISHED (`CTR-005`)**. This is a correspondence failure, not yet a
> selected-field mismatch or a literal proof that Alternative (C) is false.

## Evidence anchors

- `docs/navier-stokes openai.txt:109--124,523--546,695--784,6101--6153`
- `NavierStokes/ActualCandidateAssembly.lean:1079--1098,1121--1151,1177--1181`
- `NavierStokes/MixedCandidateAssembly.lean:67--91`
- `NavierStokes/CandidateFromLimits.lean:45--112`
- `NavierStokes/SolenoidalDiagonal.lean:31--67,186--222`
- `NavierStokes/SpatialLocalization.lean:165--207`
- `NavierStokes/DefectIncrementBounds.lean:214--220`
- `NavierStokesReview/src/audit/priority_179_latest_force_smoothness_rebuttal_2026-09-29.md`
