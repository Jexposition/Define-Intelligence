# Selected endpoint compile-boundary re-audit

Date: 2026-09-29
Scope: `NavierStokes.ActualCandidateAssembly.selected_witness` and the
exported R3 endpoint.  This report corrects an earlier overstatement that the
selected endpoint bypasses the five-moment machinery.

## Question under audit

How can the endpoint prove velocity blow-up if the exported `Witness` does not
contain a final equality identifying the selected Cartesian fields with
\((M,I,J,S,C_p)\)?  Does the absence of that equality mean that the endpoint
works without the paper's construction, or that a compiler escape has been
used?

## Direct source facts

1. `ActualCandidateAssembly.Witness` is a proposition packaging a schedule,
   three potential sums, away extensions, a forcing field,
   `CandidateProperties`, smoothness, `CandidateConsequences`, an H3-norm
   limit, force-jet decay, and boundary limits
   (`NavierStokes/ActualCandidateAssembly.lean:1121-1151`).  It does not contain
   a field of type
   `moments(selected_fields) = (M, I, J, S, C_p)`.

2. The selected proof is not a generic or empty inhabitance.  `witness`
   supplies `estimates B N0 hN` and actual physical premises to
   `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`
   (`ActualCandidateAssembly.lean:1153-1161`).  The definition of `estimates`
   calls `GluedStageEstimates.actualStageEstimates` with actual cycle coherence,
   signed wave inputs, representations, and `physicalData`
   (`ActualCandidateAssembly.lean:1090-1098`).

3. The formal blow-up premise has a separate, explicit route.  At
   `GermCandidateAssembly.lean:264-271`, the finite-stage witness constructs
   `haxis := origin_blowup ...` and passes it to
   `CandidateConsequences.mixed_exists_force_with_consequences`.  The local
   theorem `GermCandidateAssembly.origin_blowup` (`146-159`) transports the
   origin asymptotic to `FinalSlowBase.axis_tendsto`.  The latter is proved by
   `BaseResidual.baseVelocity_axis_tendsto_atTop` and the positive leading-axis
   coefficient (`FinalSlowBase.lean:372-378`).  Therefore the endpoint can prove
   speed blow-up as a direct consequence of the selected base-axis asymptotic,
   without the final result type containing a five-moment tuple.

4. `CandidateConsequences.Consequences` records maximal lifespan, admissible
   lifespan, H3 unboundedness, nonzero force, and force-jet decay
   (`NavierStokes/CandidateConsequences.lean:136-142`).  Its constructor obtains
   H3 unboundedness from `CandidateProperties`, and the mixed constructor
   obtains the endpoint H3 limit from the separate `haxis` premise
   (`CandidateConsequences.lean:144-180, 185-215`).

5. The active selected proof term does use genuine moment and rank machinery.
   Declaration-level closure from `selected_witness` contains
   `PositiveOrderMoments.moments`, `moments_repair`, and
   `weighted_moments_exact`; `FiveProfileMoments.physicalMoments` and
   `physicalMoments_eq`; `FiveRowRank.FiveRows`; `barMoment`; and the actual
   stage/physical-data declarations.  Source examples include
   `AssembledSlowBase.extended_axial_primitive_zero`
   (`AssembledSlowBase.lean:592-617`), `GlobalSlowProfiles.profiles_moments`
   (`GlobalSlowProfiles.lean:1043-1053`), `ModulatedHistories`' use of
   `FiveProfileMoments.physicalMoments_eq` (`ModulatedHistories.lean:736-738`),
   and `MeanRankUpdate.desired_mass_zero` (`MeanRankUpdate.lean:1235-1236`).

## Why the endpoint still compiles

Lean checks the proposition actually stated and the proof term supplied for it.
An intermediate lemma need not appear as a field of the final theorem.  A
five-moment identity may be used internally to construct profiles, prove rank
rows, establish primitive cancellation, or derive stage estimates.  The final
theorem can then return only the consequences needed by
`CandidateProperties`.

Formally, these are different propositions:

\[
  \exists u,p,f,K,\;\operatorname{CandidateProperties}(u,p,f,K)
\]

and

\[
  \exists u,p,f,K,\;\operatorname{CandidateProperties}(u,p,f,K)
  \land \operatorname{moments}(u,p,f)=(M,I,J,S,C_p).
\]

The first does not imply the second merely because the paper explains the
construction using the five moments.  Conversely, the absence of the second
from the result type does not imply that the first was proved without using
moment lemmas internally.

## What has and has not been established

| Question | Current source-level answer |
|---|---|
| Does the endpoint prove a formal blow-up predicate? | Yes. `CandidateProperties.speed_unbounded` is part of the selected candidate, and the selected axis limit is supplied by the explicit `haxis` route above. |
| Is the selected proof term moment-free? | No. The declaration closure and source declarations show active moment, rank, primitive, and `barMoment` dependencies. |
| Does `Witness` export the paper's final five-observable identity? | No such field or equality appears in `Witness`. |
| Does that omission prove the selected integrals are false? | No. It proves an information and correspondence limitation of the exported proposition, not a concrete mismatch. |
| Does the endpoint therefore prove the paper's exact five-moment explanation? | Not on the current record. No inspected theorem closes the complete selected mixed Cartesian velocity, pressure, residual, and force composition to the paper's five named observables. |
| Was a compiler escape found? | No. Fresh source scans found zero explicit `axiom`, `sorry`, `sorryAx`, `admit`, `unsafe`, or `implemented_by` declarations in `NavierStokes`. `noncomputable` and standard `Classical.choice` are present, but they are ordinary Lean mechanisms and do not bypass kernel checking. |

## Critical logical correction: local independence is not constructional independence

The statement that `origin_blowup` does not take a final five-moment equality as
an argument must not be read as saying that the paper's restoration mechanism
is dispensable. It is a statement about one sub-proof, not about the selected
candidate as a whole.

Write

\[
  H_{\rm axis}:=\operatorname{Tendsto}
    \bigl(t\mapsto\|u(t,0)\|\bigr)_{t\to1^-}\;\mathrm{atTop},
\]

and let \(R\) denote the remaining candidate obligations: smoothness,
support, incompressibility, residual equality, energy, force regularity, and
the selected assembly data. The source constructs the endpoint in the logical
shape

\[
  H_{\rm axis}\;\land\;R,
\]

where `H_axis` is supplied by the explicit `origin_blowup` route, while the
construction of \(R\) consumes `estimates`, `physicalData`, correction rows,
primitive identities, and stage coherence. The declaration closure reaches
`PositiveOrderMoments`, `FiveProfileMoments`, `FiveRowRank`, `barMoment`, and
the actual physical-data modules. Therefore the present source does **not**
support the counterfactual claim

\[
  \text{“remove the five-moment and repair mathematics and the same selected
  candidate still follows.”}
\]

That counterfactual has not been proved and should not be inferred from the
local proof of \(H_{\rm axis}\). If the paper uses the five-moment identities
to justify \(R\), then the final CMI construction relies on them indirectly,
even though the axis-limit lemma does not repeat them in its local type.

The distinct unresolved proposition is the field-level semantic identification

\[
  E_{\rm paper}:\quad
  \operatorname{moments}
    (u_{\rm selected},p_{\rm selected},f_{\rm selected})
  =(M,I,J,S,C_p),
\]

after the selected Cartesian lift, curl, localisation, summation,
periodisation, and residual/force construction. The current endpoint proves a
formal candidate with blow-up and uses moment-dependent upstream machinery,
but the inspected `Witness` does not export \(E_{\rm paper}\), nor has the
audit established it by an equivalent theorem. Thus the correct conclusion is
not “the moments are optional” and not “the selected integrals are false”. It
is: the formal record does not yet identify the CMI witness with the complete
five-moment mechanism described by the paper.

## Adjudication

The earlier wording “the endpoint bypasses the five-moment machinery” was too
strong and is withdrawn. The endpoint is a nonempty, standard-axiom Lean proof
of the formal C/D-shaped candidate proposition. Its blow-up conclusion is
supported by an explicit base-axis asymptotic route, while its residual and
support obligations are supplied through the selected stage and physical-data
assembly, which itself depends on substantial upstream moment and rank work.

The remaining adverse finding is narrower and stronger than an import or
dead-code objection: the current exported record does not identify the final
selected mixed fields with the five global observables used as the paper's
load-bearing explanation. The paper-to-endpoint correspondence is therefore
not established by the inspected record. A concrete field-level mismatch,
impossibility theorem, or false mandatory premise would be required before
escalating this finding to a kernel-level formal refutation.

Evidence used: the fresh endpoint axiom replay, the declaration closure
`lean_environment_closure_2026-09-26.json`, and the source declarations cited
above. The review library build completed 3,700 jobs and built the six
endpoint-adjacent bridge modules used in this audit. One separate draft,
`SelectedDirectCutoffMomentBoundary.lean`, remains a review-workspace compile
failure because it refers to an undeclared `selectedDirectStages` symbol; that
failure is not part of the OpenAI endpoint and is recorded separately rather
than used as evidence for CTR-005. This report does not treat the finding as a
request for OpenAI to repair the work; it records the present evidentiary
status of the advertised CMI claim.

## 2026-09-30 endpoint axiom replay

The tracked audit surface `NavierStokesReview/src/audit/WholeSpaceAxiomAudit.lean`
was replayed from the repository root with:

```text
lake env lean NavierStokesReview/src/audit/WholeSpaceAxiomAudit.lean
```

The compiler reported the following axiom footprints:

```text
NavierStokesR3.theorem_1_1:
  [propext, Classical.choice, Quot.sound]
NavierStokesR3.WholeSpaceUniqueness.classical_uniqueness_on_Icc:
  [propext, Classical.choice, Quot.sound]
NavierStokesR3.WholeSpaceUniqueness.candidate_global_agrees_before_one:
  [propext, Classical.choice, Quot.sound]
NavierStokes.PeriodicPaper.periodic_corollary:
  [propext, Classical.choice, Quot.sound]
```

No `sorryAx`, custom axiom, `unsafe`, or `implemented_by` declaration was
introduced by this replay. This supports the narrow axiom-integrity claim for
the queried endpoints. It does not prove the complete manuscript
correspondence or supply the missing selected-field five-observable identity.
The replay left no `lake`, `elan`, `lean`, or `dotnet` process running.
