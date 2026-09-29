# Priority 168b: Fefferman physical admissibility and the selected force chain

**Date:** 2026-09-29
**Scope:** Fefferman's connected admissibility conditions, the OpenAI
manuscript's residual-defined force, and the selected Lean construction.
**Status:** source-checked adjudication; no refutation escalation.

## Finding

Fefferman's phrase **“physically reasonable”** is not an optional description
that can be detached from Alternatives (A)--(D).  In the supplied CMI text,
the Newton-law interpretation, the decay conditions (4)--(5), the accepted
solution conditions (6)--(7), and the periodic alternatives (8)--(11) define
the admissibility envelope.  The sentence that the four alternatives retain
the “heart of the problem” means that a submission must address the global
smoothness, incompressibility, initial-data, forcing, decay or periodicity,
and energy requirements stated in that envelope, not merely write a local PDE
identity.

The current source record therefore supports the following two conclusions at
once:

1. The selected Lean route is not shown to be a trivial wrapper or a free
   `NativeBounds` assumption.  It derives the smooth force from concrete
   residual-rate data and compatible endpoint limits.
2. The inspected record still does not contain a theorem identifying that
   completed selected construction with every load-bearing physical identity
   used in the manuscript, in particular the transport of
   \((M,I,J,S,C_p)\) through the selected Cartesian composition.

These are not contradictory.  The first is a positive result about the
formal residual/force chain.  The second is a negative result about the
paper-to-endpoint semantic identification.  Neither alone proves that the
selected force is nonsmooth or that Fefferman Alternative (C) is false.

## Exact Fefferman meaning

The local source `docs/navierstokes.txt` states, in sequence:

- Equation (1) is Newton's law for a fluid element subject to the externally
  applied force and pressure/friction forces.
- “For physically reasonable solutions” the data are restricted by (4) and
  (5), which impose rapid decay on all spatial derivatives of the initial
  velocity and on all space-time derivatives of the force.
- A solution is accepted only if (6) gives global \(C^\infty\) smoothness for
  \(p,u\), and (7) gives bounded kinetic energy for every \(t\geq0\).
- The periodic branch replaces the whole-space decay conditions with (8)--(9)
  and requires (10)--(11).
- The four alternatives are then stated using these conditions.  In (C), the
  data must satisfy (4)--(5), while every excluded global solution must satisfy
  (1)--(3), (6), and (7).  In (D), the corresponding periodic conditions are
  required.

Thus “physically reasonable” is a connected mathematical predicate.  It does
not mean that a blow-up construction is required to look like a particular
laboratory experiment, but it does require the stated globally smooth,
decaying or periodic data and the stated solution regularity and energy
conditions.  The external-force wording also supplies a physical provenance
interpretation.  The literal existential statement, however, does not by
itself add a formal independence quantifier saying that the force could not
have been designed from a target trajectory.

## Exact manuscript-to-Lean force chain

The OpenAI manuscript explicitly takes the residual-design route.  It says
that for a chosen incompressible flow and pressure one can define

\[
 f=\mathcal R(u,p)
 =\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p,
\]

and that the construction problem is to make the flow blow up while the
residual and all of its derivatives extend smoothly through the singular time.
The manuscript describes pulse fluxes, further corrections, localisation, and
flat residual estimates as parts of that construction.  The extracted source
does not justify the stronger claim that every residual summand must diverge,
nor does it establish in the inspected passages that the five moments are the
sole possible cancellation mechanism.

The selected Lean source gives a concrete route:

```text
ActualCandidateAssembly.physicalData
  -> ActualCycleResidualBounds.PhysicalData
  -> ActualStageEstimates.stageEstimates_of_representations
  -> StageEstimates.finite_residual
  -> StageEstimates.exists_schedule
  -> VanishingJointJets
  -> CandidateFromLimits.tracedResidual_smooth
  -> CandidateFromLimits.force_smooth
```

The relevant declarations are:

- `ActualCandidateAssembly.lean:1079-1098`, which obtains physical data and
  actual stage estimates;
- `ActualStageEstimates.lean:344-404`, where finite residual rates are derived
  from `ActualCycleResidualBounds.finite_residual_rates`;
- `ActualCycleResidualBounds.lean:1156-1210`, where the rate theorem consumes
  an invariant and physical data rather than an empty residual oracle;
- `MixedPeriodicAssembly.lean:310-366`, where vanishing joint jets yield
  locally uniform residual limits and a smooth candidate force;
- `CandidateFromLimits.lean:45-112`, where the residual recurrence and limits
  prove smoothness of the force and agreement with the activated residual;
- `ActualCandidateAssembly.lean:1121-1185`, where the resulting consequences
  are packaged into `Witness` and `selected_witness`.

This is a real formal chain.  It defeats the claim that the endpoint simply
assumes `NativeBounds` “out of thin air”.

## What remains unproved at the semantic boundary

The positive chain above proves a rate/flatness route to a smooth residual
extension.  It does not, by itself, prove the stronger paper-correspondence
statement

\[
\operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},
f_{\mathrm{selected}})
=(M,I,J,S,C_p)
\]

after the selected finite stages, infinite sums, Cartesian curl,
cutoff-localisation, periodisation, pressure reconstruction, force extension,
and endpoint limits.  The source record contains genuine intermediate
correction data: `CorrectionState.debt` records the three-component defect
\((P,J_\theta,J_z)\), while `ZeroMasses` records two separate zero-mass
conditions.  The audit has not located a theorem proving that these
intermediate data are equivalent to the manuscript's five cumulative
observables for the final selected field.

The correct implication is therefore:

\[
\text{concrete invariant-backed residual rates}
\Longrightarrow
\text{vanishing residual jets}
\Longrightarrow
f\in C^\infty
\]

is source-supported, whereas

\[
\text{paper five-moment correction identities}
\Longrightarrow
\text{the exact selected Cartesian residual-rate chain}
\]

has not yet been located or proved on the inspected record.

## Scope of the encoded whole-space C-shaped proposition

The comparator route is also more than a bare existential wrapper.  The
inspected declarations state the following connected object:

```text
NavierStokesR3.theorem_1_1
  -> CandidateProperties u p f K
  -> compact, smooth force
  -> forceConditionDecay_of_compact
  -> no Nonempty (GlobalFiniteEnergySolution ν f)
  -> comparator_of_breakdown
  -> navier_stokes_breakdown_R3
```

`ComparatorR3Theorem.navier_stokes_breakdown_R3` explicitly quantifies a
decaying initial datum and force and excludes a comparator solution satisfying
the encoded whole-space equations, smoothness, and global bounded-energy
conditions.  `ComparatorR3Bridge.comparator_of_breakdown` proves the force
decay from smooth compact support and converts any comparator solution into a
`GlobalFiniteEnergySolution` with the same viscosity, force, and zero datum.
This establishes the scope of the formal C-shaped proposition on the
inspected Lean path.  It does not transform that proposition into a proof that
the manuscript's specific five-moment explanation has been transported to the
selected endpoint.

The second missing implication is a paper-to-code correspondence gap.  It is
not evidence that the first implication is false, and it is not evidence that
the selected force violates Fefferman's conditions.

## Adjudication matrix

| Claim | Current source status | Correct wording |
|---|---|---|
| Fefferman's “physically reasonable” conditions are connected requirements | Confirmed by the order and wording of the CMI text | Do not isolate a bare C-shaped wrapper from (4)--(7) or (8)--(11). |
| The manuscript uses five moments as load-bearing profile/correction data | Confirmed in the extracted manuscript | Do not call them optional notation. |
| OpenAI's selected force is derived from a free generic interface | Not supported; contradicted by the actual stage and residual-rate chain | Do not allege a compiler cheat or empty `NativeBounds`. |
| Lean derives force smoothness from the selected residual-rate route | Supported on the inspected path | This is a formal positive result, subject to the build and axiom ledger. |
| The selected endpoint exports the complete paper-level five-observable identity | Not located | Keep `CTR-005` as an unestablished paper-to-endpoint correspondence. |
| Missing explicit tuple alone proves force nonsmoothness or C failure | Not proved | Do not make that escalation without a direct selected-field mismatch or failed mandatory premise. |
| Residual-defined force matches the physical provenance language exactly | Not established; existential legality and physical provenance are distinct questions | Record `CTR-012` as a semantic provenance objection, not as `False`. |

## Required next audit

The remaining work is not another abstract interface countermodel.  It is a
source-level bridge search and, if necessary, a value-level calculation over
the actual selected declarations:

1. Identify the exact `Invariant`, `debt`, and `masses` fields consumed by the
   selected `finite_residual_rates` proof.
2. Search their transitive proof terms for definitions of the five manuscript
   observables, not only names containing `moment` or `debt`.
3. Trace those definitions through `potentialSum`, curl/localisation,
   periodisation, pressure, force, and endpoint limits.
4. Either record the exact bridge theorem, or record a bounded negative search
   with the declarations and transformations inspected.
5. Escalate only if the selected values directly violate a Fefferman premise,
   a selected identity is proved false, an impossibility theorem is obtained,
   or a selected-path contradiction is derived.

**Current verdict:** the connected formal CMI-shaped proposition and the
selected smooth-force route are source-supported; complete correspondence
between the manuscript's physical five-moment engine and the selected endpoint
remains **NOT ESTABLISHED**.  This is an adverse audit finding, not a repair
handoff to OpenAI and not a claim that the CMI proposition has already been
formally refuted.
