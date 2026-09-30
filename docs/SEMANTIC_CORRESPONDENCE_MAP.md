# Semantic correspondence map: OpenAI paper to Lean endpoint

## Connected CMI crosswalk: Priority 200 (2026-09-30)

Priority 200 confirms that the Lean R3 theorem and comparator prove a formal
forced whole-space breakdown proposition matching the connected CMI target.
The manuscript's five-moment repair remains load-bearing in its written
construction, and the selected Lean path contains substantial upstream
physical-data and residual-rate machinery. The inspected `Witness` still does
not export a named final `(M,I,J,S,Cp)` identity, so complete
manuscript-to-selected-endpoint equivalence remains `CTR-005: NOT ESTABLISHED`.
This is neither a proof that the selected field is wrong nor a reason to call
the literal forced endpoint empty.


## Live declaration cross-check: Priority 199 (2026-09-30)

The current raw-source recheck is recorded in
`../NavierStokesReview/src/audit/priority_199_selected_endpoint_declaration_crosscheck_2026-09-30.md`
and its machine-readable evidence record. It confirms the calibrated split:
`physicalData`, concrete residual-rate proofs, recurrence limits, and force
extension feed the selected endpoint; `ActualCandidateAssembly.Witness` does
not export a named final equality identifying the selected Cartesian fields
with `(M,I,J,S,Cp)`. This preserves `CTR-005: NOT ESTABLISHED` for complete
paper-to-selected-endpoint correspondence, without asserting a selected-field
defect, force nonsmoothness, impossibility, a compiler escape, or `False`.


## Effective register and reconciliation control: 2026-09-30

Use [`DOCUMENTATION_RECONCILIATION_2026-09-30.md`](DOCUMENTATION_RECONCILIATION_2026-09-30.md)
and the 2026-09-29 full register as the live state. The current counts are
2,794 indexed modules, 588 captured endpoint modules, 906 evidence-inspected
rows, 1,881 queued rows, 0 missing project import edges, and 86 supplemental
records. The dated coverage sections below preserve review chronology and must
not be read as current totals.

**Updated:** 2026-09-30
**Purpose:** make the mathematical content of the Lean source reviewable without
requiring a reader to infer the construction from filenames or from a successful
build.

## Reading rule

The paper is the claimed mathematical specification. The Lean source is the
implementation to be checked against that specification. A file import, a
reachable declaration, or a successful theorem application proves only that a
formal object is connected to the endpoint. It does not prove that the object
has the interpretation assigned to it in the paper.

## Historical coverage state (2026-09-28)

The 2026-09-28 register recorded 2,790 indexed modules, 588 reachable
modules, 613 evidence-inspected modules, 0 reachable modules still open, and 0
missing project import edges. Priority 114 completed the reachable closure:
[`priority_114_final_reachable_eight_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_114_final_reachable_eight_source_review_2026-09-28.md).
These eight modules add genuine reduced moment, curl, periodisation, and jet
results, but do not close the final selected Cartesian radial-observable
composition. The remaining work is the indexed-but-unreachable source tree
and the complete endpoint requirement cross-check.

For the live 2026-09-30 state, use
[`DOCUMENTATION_RECONCILIATION_2026-09-30.md`](DOCUMENTATION_RECONCILIATION_2026-09-30.md)
and the 2026-09-29 full semantic register. “Unreachable” in the historical
paragraph above is a scoped endpoint-closure label, not a dead-code claim.

This map therefore records, for every load-bearing part of the claim:

1. what the paper says the object means;
2. which Lean definitions actually construct or consume it;
3. what identity is proved at the selected endpoint;
4. what identity is still required for paper-to-code correspondence.

The source coordinates below refer to the current checkout. They are navigation
anchors, not substitutes for reading the declarations.

## CMI wording and paper-method nuance

The official Fefferman statement uses physical language describing `f` as a
given externally applied force, but Alternatives (C) and (D) are existential
mathematical propositions. The statement specifies smoothness, decay or
periodicity, divergence-free initial data, and the absence of a global smooth
physically reasonable solution. It does not add a syntactic Lean predicate
requiring `f` to be independent of the eventual `u`.

The OpenAI Navier--Stokes paper explicitly says that its construction chooses
the flow and pressure and then defines the residual force, with the central
technical task being smooth cancellation of the residual through the singular
time. Therefore residual-defined forcing is not recorded here as an automatic
CMI disproof. The audit target is the stronger paper-to-code question: does
the selected Lean field realise the paper's five moments, pressure, pulse and
correction construction, cutoffs, residual cancellation, and whole-space
obstruction? The checked-in source crosswalk is
`NavierStokesReview/evidence/paper_nuance_crosswalk_2026-09-27.md`.

The Euler paper likewise describes exact smooth parent/child stages and a
stability-based limiting argument. Nested intervals alone do not prove a
temporal discontinuity or a Zeno failure; those must be checked against the
actual stage-matching and summability theorems.

## One-page construction graph

```text
OpenAI paper: Theorem 1.1 / C-D claim
        |
        v
base profile + pressure + oscillatory pulses
        |
        v
finite correction rows and five cumulative moments
        |
        v
cycle/stage construction and temporal germs
        |
        v
potential tsum + direct branch + curl/localisation
        |
        v
periodic velocity, pressure, residual, and force
        |
        v
R3 localisation + support + energy packaging
        |
        v
selected_witness -> CandidateProperties -> theorem_1_1
```

The graph is a faithful description of the source route. The unresolved
question is the vertical transport across the middle of the graph: whether the
five named paper observables remain equal to the observables of the final
Cartesian field after summation, curl, localisation, periodisation, pressure
assembly, and R3 packaging.

## Paper anchors used by the comparison

The paper-side meanings are taken from the checked-in snapshot
`docs/navier-stokes openai.pdf` and should be read alongside the source spans:

| Paper location | Claimed object or step | Lean comparison route |
|---|---|---|
| Abstract and Theorem 1.1, pp. 1-2 | Smooth compactly supported force, incompressibility, finite energy, unbounded speed, and C/D conclusion. | `R3/ProblemStatement.lean`, `R3/ActualCandidate.lean`, `R3/Theorem.lean`. |
| Residual construction, p. 3 | Choose a flow/pressure template, define the residual force, and prove smooth cancellation. | `CandidateFromLimits.lean`, `PhysicalResidualJetBounds.lean`, `ActualCycleResidualBounds.lean`. |
| Pulse and correction construction, pp. 5-7 | Localised pulses and corrections control the residual and preserve the intended profile data. | `ParticularWave*`, `ActualCycle*`, `Correction*`, `FiveRowRank.lean`, `PositiveOrderMoments.lean`. |
| Stage-by-stage correction proposition, paper §9 | Four correction functions repair the required cumulative quantities at each stage. | `FiveRowRank.FiveRows`, `DefectIncrementBounds`, `MeanRankUpdate`, cycle-preservation modules. |
| Five-coordinate repair, Appendix A, pp. 126-128 | The named tuple `(M,I,J,S,C_p)` and its five equations/coefficients. | `PositiveOrderMoments`, `FiveProfileMoments`, and the runtime three-debt layer. |

The page references identify the paper’s asserted meaning. They do not imply
that a similarly named Lean declaration is already the same object. The right-
hand side of each row must be checked through the selected construction.

## Endpoint contract versus paper claim

| Mathematical question | Paper claim | Lean endpoint and source | What is actually exposed | Review status |
|---|---|---|---|---|
| What is being proved? | For every `ν > 0`, construct a smooth incompressible solution with smooth compactly supported force, finite kinetic energy, and finite-time unbounded speed, yielding C/D. | `NavierStokes/R3/ProblemStatement.lean:57-109`; `NavierStokes/R3/Theorem.lean:46-49, 66-79` | `CandidateProperties` requires smoothness, support, zero initial velocity, divergence-free velocity, residual equality on `0 < t < 1`, energy, and blow-up. The theorem packages the selected witness into that predicate. | Formal predicate confirmed; paper correspondence must be checked separately. |
| Which concrete objects are selected? | The paper’s constructed base, pulse, correction, pressure, and force fields. | `NavierStokes/ActualCandidateAssembly.lean:1121-1151, 1165-1185`; `NavierStokes/R3/ActualCandidate.lean:78-122, 127-151` | `Witness` contains a schedule, assembled potential/direct/pressure sums, extensions, forcing, `CandidateProperties`, consequences, blow-up, and jet-limit data. | Selected route identified. |
| What does `selected_witness` say about five moments? | The paper’s five cumulative moments `(M,I,J,S,C_p)` are transported through the correction scheme and final field. | `ActualCandidateAssembly.selected_witness` at `ActualCandidateAssembly.lean:1177-1182`; upstream moments in `PositiveOrderMoments.lean` and `FiveProfileMoments.lean` | The selected witness does not export an equality from the final Cartesian velocity/pressure to the five named moments. | **CTR-005 open.** |
| Is the final field three-dimensional and solenoidal? | The advertised field is a 3D incompressible velocity. | `ActualCandidateAssembly` assembles potential/direct branches; `R3/ActualCandidate.lean`; selected divergence results | The final field is curl-generated/assembled and the source contains divergence results. The old pure-axial-collapse objection is not source-supported. | Cleared attack surface; do not reuse as disproof. |
| Is the force smooth? | The paper requires a smooth compactly supported force and explains cancellation of divergent residual terms. | `CandidateFromLimits.lean:82-110`; `R3/PositiveTimeForce.lean`; `PhysicalResidualJetBounds.lean`; `ActualCycleResidualBounds.lean` | The force is selected from a residual construction, with endpoint jet/cancellation premises and a smooth positive-time cutoff. | Smoothness is a formal selected-path result; provenance remains a separate concern. |
| Is the pressure the global pressure determined by the selected velocity? | The paper uses pressure as part of the incompressible Navier–Stokes solution and its residual. | `NavierStokes/R3/PressureRecovery.lean`; `NavierStokes/R3/ActualPressureFlux.lean`; R3 pressure modules | Comparison and compact-test recovery identities are present. The selected endpoint does not, by its public `Witness` type, expose an absolute global pressure-Poisson/Leray identity tied to its final field. | **PRS-08 / CTR-039 open.** |
| Does the selected field satisfy the whole-space conditions? | The paper requires a whole-space field with compact support/decay and finite energy. | `NavierStokes/R3/ActualCandidate.lean:78-122`; `R3CompactCandidate.lean`; `R3/CompactEnergy.lean` | The R3 wrapper supplies the formal support, smoothness, divergence, residual, energy, and blow-up predicates. | Formal packaging confirmed; semantic field identity remains the review issue. |
| Does uniqueness rescue the interpretation? | A solution for the stated force should be a solution of the intended Cauchy problem. | `NavierStokes/R3/WholeSpaceUniqueness.lean`, `classical_uniqueness_on_Icc` | Uniqueness is relative to the same engineered force and solution class. It does not independently establish that the force is generated as an autonomous datum or that the paper’s five moments reach the endpoint. | Relative theorem; not a correspondence theorem. |

## Layer-by-layer source map

### 1. Formal problem and exported theorem

`R3/ProblemStatement.lean` defines the active R3 predicate. The residual at
line 57 contains the temporal derivative, nonlinear advection, viscosity, and
pressure-gradient terms. The `CandidateProperties` fields beginning at line 92
include the actual admissibility obligations used by the theorem. The theorem
at `R3/Theorem.lean:46-49` then packages the selected candidate into the
breakdown statement; the dissipation version at lines 66-79 adds its energy
consequences.

This is the correct formal target. It is not correct to claim that the theorem
has no energy or dissipation statement, and it is not correct to substitute a
remembered filename such as `SelectedCandidate.lean` for the active route.

### 2. Candidate assembly and the selected witness

`ActualCandidateAssembly.lean` is the main construction junction. The
`Witness` proposition around lines 1121-1151 binds the schedule, actual
potential/direct/pressure sums, away extensions, force, `CandidateProperties`,
and candidate consequences. The selected theorem around lines 1177-1182
chooses the concrete schedule and returns the witness consumed downstream.

The important negative fact is about the interface, not reachability: the
public witness contains no field-level equation of the form

```text
paperMoments (selectedVelocity, selectedPressure)
  = promotedDebt (selectedDebt)
```

Nor does it expose the equivalent five equalities separately. This is why the
review records a selected-path correspondence failure rather than claiming that
the upstream moment machinery is dead code.

### 3. Five moments, three debts, and corrections

The source has two distinct finite-dimensional interfaces:

| Interface | Source | Mathematical role |
|---|---|---|
| Five-coordinate debt | `PositiveOrderMoments.lean:23-24`; `FiveProfileMoments.lean:260-263` | Represents the paper-level five moment coordinates and profile identities. |
| Runtime three-coordinate debt | `FiveRowRank.lean:22-24`; `MeanRankUpdate.lean:24-32` | Drives the runtime rank update and `scaleDebt`. |
| Correction rows | `FiveRowRank.lean:241-248`; `DefectIncrementBounds.lean:621-650` | Constrains correction increments, including the two zero moment rows and three debt rows. |
| Scalar radial observable | `DefectIncrementBounds.lean:214-217` | Defines `barMoment` from a scalar field after torus averaging and radial integration. |

The exact three-to-five promotion can be algebraically valid while still not
being a field-level transport theorem. In particular, `FiveRows` constrains
the correction functions `dv` and `ga`; it does not, by its type alone, assert
that the total Cartesian field has zero mass or zero kinetic energy. The missing
theorem must therefore start with the actual selected field, perform the
coordinate projection and averaging, and only then identify its value with the
promoted debt.

### 4. Stage, cycle, and infinite-sum assembly

The stage and cycle modules prove useful local facts: schedule estimates,
stagewise chart identities, correction-row preservation, finite-prefix
identities, and jet bounds. `MixedPeriodicAssembly.lean:36-39` defines the
periodic velocity route. `SolenoidalDiagonal.potentialSum` supplies the
potential summation consumed by the selected construction.

The semantic audit must distinguish the following statements:

```text
each finite stage has property P
       !=
the infinite mixed Cartesian tsum has property P
```

To bridge that gap for the paper’s moments, the source needs an interchange
theorem covering the actual summation, curl/localisation commutator, torus
average, radial integral, boundary terms, and limit passage. The current
finite-prefix and stagewise results are positive evidence about the assembly;
they are not that final theorem.

### 5. Curl, localisation, and the radial observable

The production field has two branches: a curl of a localised potential and a
separately added direct branch. When the curl meets a cutoff, the product rule
has the form

\[
\operatorname{curl}(\chi A)
 = \chi\operatorname{curl}(A)
   + (\nabla\chi)\times A.
\]

The correction layer’s `barMoment` is a scalar radial operator. Therefore the
paper-to-code check must evaluate the selected Cartesian field after this
commutator term is present. A stage theorem about an unlocalised radial profile
does not automatically evaluate the final mixed field.

The live calculation route is:

```text
selected potential/direct stages
  -> localised Cartesian field
  -> spatial curl and cutoff commutator
  -> positive-radius physical component
  -> axis totalisation and boundary control
  -> torusAverage
  -> barMoment
  -> five-moment comparison
```

The first several arrows have selected finite-prefix evidence. The last three
arrows remain the load-bearing calculation required for an unconditional
field-level mismatch or confirmation.

### 6. Pressure and residual semantics

`CandidateFromLimits.lean:82-110` defines the residual-derived force route and
proves residual equality for the activated fields in its stated domain.
`R3/ProblemStatement.lean:57` shows where the pressure gradient enters the
formal residual. `R3/PressureRecovery.lean` and
`R3/ActualPressureFlux.lean` provide comparison/compact-test recovery
identities.

The correct conclusion is two-layered:

1. The selected force can be formally smooth and can satisfy the residual
   predicate, including endpoint cancellation data.
2. The source map does not thereby prove that the selected pressure is the
   absolute global representative determined by the final velocity through the
   whole-space pressure-Poisson/Leray semantics required by the paper’s physical
   interpretation.

This is a provenance and composition question. Compact pressure support alone
does not prove trivialisation, and residual-defined forcing alone does not prove
`False` for the literal existential C/D predicate.

### 7. Off-axis charts and the origin route

`PhysicalResidualJetBounds.lean` defines `StateRealization` around line 885 and
`ChartIdentity` around line 747. The chart identity uses a positive-radius
condition and therefore describes the off-axis route. The origin route is
handled separately by the `GlobalBaseError`/vanishing-jet construction.

The review obligation is not to call this split a contradiction merely because
there are two lemmas. It is to identify a theorem that proves the two routes
agree with the same selected field and all derivatives needed at the axis. If
that theorem is absent, the result is a domain-scope correspondence gap.

## Required transport theorems

These are the concrete obligations that would close the review’s main gap. They
are written mathematically rather than as guessed Lean code so that a human
reviewer can compare them directly with the paper.

### T1. Selected five-moment transport

For the actual selected fields, prove

\[
\bigl(M(u),I(u),J(u),S(u),C_p(u,p)\bigr)
 = \operatorname{promote}\bigl(d_0,d_1,d_2\bigr),
\]

with every integral defined on the actual Cartesian field exported by
`selected_witness`, including the localisation and summation limits.

### T2. Infinite-sum observable transport

Prove that the radial observable commutes with the selected construction:

\[
\operatorname{barMoment}_k(U_{\mathrm{selected}})
 = \lim_{N\to\infty}
   \operatorname{barMoment}_k(U_{\mathrm{selected}}^{(N)}),
\]

and account explicitly for the curl-cutoff commutator and both radial boundary
terms.

### T3. Absolute pressure semantics

Prove for the selected `(u,p)` the global pressure equation, gauge/normalisation,
decay class, and compatibility with the residual:

\[
-\Delta p = \partial_i\partial_j(u_i u_j)
\quad\text{on the stated whole-space domain},
\]

with the exact convention for the body force and pressure representative used
by the source.

### T4. Chart-to-axis compatibility

Prove that the off-axis chart field and the origin error-limit field are the
same selected field, with matching spatial and temporal jets at the axis.

### T5. Force provenance, if independence is claimed

State and prove the admissibility condition under which “given, externally
applied force” is being interpreted. If the intended condition is forward-data
independence or stability under a fixed-force perturbation, it must be present
as a formal predicate; it cannot be inferred from the existential type alone.

## Cleared or narrowed objections

The following are not valid unconditional disproofs on the current source
record:

- pure axial or zero-swirl collapse: the final field has three Cartesian
  components and is curl-generated;
- raw-stage divergence: raw stages are not the exported final field;
- discontinuous cutoff: the selected cutoff is smooth in the formal route;
- energy mismatch: the R3 energy/dissipation package is present;
- compact pressure support alone: no trivialisation theorem follows from that
  property by itself;
- mirror-force or fixed-force perturbation alone: these test a different input
  or a stability/provenance condition and do not negate the literal existential
  endpoint without an added admissibility premise.

These cleared routes do not clear the paper-level claim. They narrow the review
to the selected-field transport and composition obligations above.

## Verdict boundary

The source establishes a substantial formal construction and a reachable R3
candidate predicate. The current review does **not** establish that the Lean
endpoint is false. It does establish that the published solution claim is not
established as a paper-to-code CMI solution until the selected-field transport,
pressure composition, and any claimed force-provenance conditions are made
explicit and verified.

## Navigation

- [Architecture map](REPOSITORY_ARCHITECTURE_MAP.md)
- [Interactive architecture map](REPOSITORY_ARCHITECTURE_MAP.html)
- [Module explanations](LEAN_MODULE_EXPLANATIONS.md)
- [Declaration index](LEAN_DECLARATION_INDEX.md)
- [Active review plan](OpenAI_NavierStokes_CMI_First_Review_Plan.md)
- [Audit tracker](OpenAI_NavierStokes_Audit_Tracker.md)
- [Document control](REVIEW_DOCUMENT_CONTROL.md)

## Current source-review coverage: 2026-09-27

The full semantic register is synchronised at **2,790 indexed modules, 588
source-reachable modules, 199 explicit source-review records, and 414
reachable modules still awaiting declaration-level semantic classification**.
The latest direct source tranche is documented in
`NavierStokesReview/src/audit/priority_0_1_source_review_2026-09-27.md`.

Use the full-tree register at
`NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`,
`.md`, and `.html`, mirrored as
`REPOSITORY_SEMANTIC_COVERAGE_REGISTER.md` and `.html` in this directory.
The older `semantic_coverage_register_2026-09-27.*` artefacts are route-only
historical views and are not full-closure counts.

The new tranche confirms intermediate geometry, profile/Gaussian, covariance,
curl, reduced radial-flux, R3, regularity, and compatible-gluing results. It
does not add a selected-field theorem for

```text
barMoment(torusAverage(periodise(curl(tsum(potentialSum)) * cutoff)))
  = (M, I, J, S, C_p)
```

The selected-field defect remains an open calculation. No nonzero remainder,
impossibility result, or kernel-level `False` is inferred from this coverage
tranche.

## 2026-09-27 priority 135-139 synchronisation

The full register now contains **219 explicit source reviews** and **394
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_135_139_source_review_2026-09-27.md`.
It records substantive terminal-integral, pressure-stream, periodised-sum,
local curl-transport, harmonic residual, coherent-jet, and pulse-history
results. It does not establish the final selected Cartesian
`barMoment(...)= (M,I,J,S,C_p)` identity or a nonzero selected-field defect.
## 2026-09-27 priority 1-2 synchronisation

The full register now contains **229 explicit source reviews** and **384
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_1_2_source_review_2026-09-27.md`.
It identifies `CrossBasedMeanComposition.crossDefect` as a real intermediate
defect term and records that the later four-stage result requires zero
radial-moment hypotheses. No final selected-field transport theorem, concrete
selected-field `Delta m != 0`, impossibility theorem, or kernel-level `False`
is inferred.

## 2026-09-27 priority 3-6 synchronisation

The full register now contains **239 explicit source reviews** and **374
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_3_6_source_review_2026-09-27.md`.
It records an explicit earlier-band cross-defect and conditional tail
cancellation, plus real torus Haar-mean, profile-history, parity, support,
covariance, and coordinate results. No final selected-field transport theorem,
concrete selected-field `Delta m != 0`, impossibility theorem, or kernel-level
`False` is inferred.

## 2026-09-27 priority 61-64 localisation synchronisation

## 2026-09-27 priority 63-66 profile/axis synchronisation

## 2026-09-27 priority 133-141 signed-profile and prefix synchronisation

## 2026-09-27 priority 133-135 signed-dynamics synchronisation

## 2026-09-27 priority 133-134 curl/endpoint synchronisation

The full register now contains **299 explicit source reviews** and **314
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_133_134_curl_endpoint_source_review_2026-09-27.md`.
It records finite-label/harmonic bounds, an actual current-band Cartesian
curl bridge, initial native regularity, residual-limit construction, finite
particular assembly, concrete endpoint-input packaging, potential coherence,
and seed periodicity. No final selected-field `(M,I,J,S,C_p)` transport
theorem, concrete selected-field `Delta m != 0`, impossibility theorem, or
kernel-level `False` is inferred.

The full register now contains **289 explicit source reviews** and **324
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_133_135_signed_dynamics_source_review_2026-09-27.md`.
It records concrete signed common-wave equations, exact exterior zero/support
behaviour, mean-increment residual algebra, temporal-state naturality, current
support/zero lemmas, potential transport, valid-band wave compatibility, and
coefficient deck periodicity. No final selected-field `(M,I,J,S,C_p)` transport
theorem, concrete selected-field `Delta m != 0`, impossibility theorem, or
kernel-level `False` is inferred.

The full register now contains **279 explicit source reviews** and **334
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_133_141_source_review_2026-09-27.md`.
It records substantive signed profiles, covariance and scale identities,
actual wave/source bounds, periodic same-force uniqueness, physical sum
coherence, cycle periodicity, and finite-prefix Cartesian/polar field
agreement. `ActualPhysicalPrefixFields` supplies a finite-prefix `PhysicalData`
bridge. No final selected-field `(M,I,J,S,C_p)` transport theorem, concrete
selected-field `Delta m != 0`, impossibility theorem, or kernel-level `False`
is inferred.

The full register now contains **269 explicit source reviews** and **344
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_63_66_profile_axis_source_review_2026-09-27.md`.
It records actual covariance/inverse bounds, spatial Borel extension,
true-cone correction, Bochner transport primitives, Gaussian zero-germ coverage,
physical polar geometry, axis-preservation/origin results, natural-axis
reference positivity, implicit heat coordinates, and positive-time signed
localisation. No final selected-field `(M,I,J,S,C_p)` transport theorem,
concrete selected-field `Delta m != 0`, impossibility theorem, or kernel-level
`False` is inferred.

The full register now contains **259 explicit source reviews** and **354
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_61_64_localisation_source_review_2026-09-27.md`.
It records genuine Euclidean curl, preterminal copy, cutoff, spacetime-gluing,
zero-mean modulation, tangent ODE, and canonical copy-bridge results. No final
selected-field `(M,I,J,S,C_p)` transport theorem, concrete `Delta m != 0`,
impossibility theorem, or kernel-level `False` is inferred.

## 2026-09-27 priority 7-61 R3 synchronisation

The full register now contains **249 explicit source reviews** and **364
reachable modules still awaiting semantic inspection**, from **2,790 indexed**
and **588 reachable** modules. The tranche report is
`NavierStokesReview/src/audit/priority_7_61_r3_source_review_2026-09-27.md`.
It records endpoint-adjacent candidate packaging and substantive R3
compact-support, heat-kernel, cutoff-commutator, Fubini, weak-continuity,
coordinate, and flat-cutoff results. No final selected-field transport theorem,
concrete selected-field `Delta m != 0`, impossibility theorem, or kernel-level
`False` is inferred.

## 2026-09-27 priority 140-145 synchronisation

The full semantic coverage register now contains 209 explicit source reviews and 404 reachable modules still awaiting semantic inspection, from 2,790 indexed and 588 reachable modules. The new tranche report is `NavierStokesReview/src/audit/priority_140_145_source_review_2026-09-27.md`. It records genuine profile/history, pressure, covariance, axis, ODE, debt-update, and global-stress theorems. The map continues to distinguish those local or intermediate identities from the unestablished final selected Cartesian five-observable transport composition. No concrete selected-field \(\Delta m\neq0\) or `False` result is asserted.

## 2026-09-27 comparator/current-mode/heat-debt synchronisation

The full register now contains **305 explicit source reviews** and **308 reachable modules still awaiting semantic inspection**, from **2,790 indexed** and **588 reachable**. The tranche report is `NavierStokesReview/src/audit/priority_133_129_132_source_review_2026-09-27.md`.

The six reviewed modules prove genuine intermediate operator, mode, support, debt-jet, harmonic, and residual-naturality results. They do not supply the selected-field theorem transporting `(M,I,J,S,C_p)` through the final `tsum`/curl/localisation/periodisation composition. No concrete selected-field `Delta m != 0`, impossibility theorem, or kernel `False` is inferred.

## 2026-09-27 initial/comparator/heat-tail synchronisation

The full register now contains **311 explicit source reviews** and **302 reachable modules still awaiting semantic inspection**, from **2,790 indexed** and **588 reachable**. The tranche report is `NavierStokesReview/src/audit/priority_132_131_130_source_review_2026-09-27.md`.

The six reviewed modules add genuine initial/Gaussian bounds, comparator-side predicates, heat-tail debt and history limits, signed mean gain, and off-axis cylindrical residual transport. They do not supply the selected-field theorem transporting `(M,I,J,S,C_p)` through the final `tsum`/curl/localisation/periodisation composition. No concrete selected-field `Delta m != 0`, impossibility theorem, or kernel `False` is inferred.

## 2026-09-27 residual/rank bridge synchronisation

The full register now contains **317 explicit source reviews** and **296 reachable modules still awaiting semantic inspection**, from **2,790 indexed** and **588 reachable**. The tranche report is `NavierStokesReview/src/audit/priority_130_129_residual_rank_source_review_2026-09-27.md`.

The six reviewed modules add genuine local residual/coordinate bridges, transition-profile identities, cycle mean propagation, and exact intermediate `FiveRowRank` repair equations. They do not supply the selected-field theorem transporting `(M,I,J,S,C_p)` through the final composition. No concrete selected-field `Delta m != 0`, impossibility theorem, or kernel `False` is inferred.
## Latest source tranche: 2026-09-28

The correspondence map now includes six further direct source reviews. `ResidualStability` proves nonlinear residual-difference and flatness identities; `ParticularCopyBounds` proves finite-copy modal and pressure/velocity jet controls; `PastExtension` proves the zero-before-time extension and endpoint residual adapter; `LocalAxisymmetricResidual` proves the local profile-to-Cartesian residual identity; `PhysicalGraphBounds` provides axis-free chart and graph jet bounds; and `PrimaryPulseBounds` provides local pulse/curl/profile/covariance identities. None of these inspected modules supplies the final global `(M,I,J,S,Cp)` transport theorem.

The current generated coverage state is 588 reachable modules, 323 semantically inspected, and 290 still open. Reachability is not transport: importing or consuming local estimates does not establish equality of the final selected field with the paper-level observables.
## Latest source tranche: assembly, geometry, and axis series

The map now includes `PrimaryFieldAssembly`, `R3/ComparisonGronwall`, `UniformHarmonicInteraction`, `ActualCycleGeometry`, `ActualPolarCoverage`, and `AxisSeries`. These modules document real upstream periodisation, vector-mode/source/covariance assembly, comparison inequalities, harmonic interaction bounds, actual geometry aliases, axis-free coverage, and scalar Bessel/profile series. They still do not establish that the final selected Cartesian field has the paper-level `(M,I,J,S,Cp)` observables.

Coverage is 329 of 588 reachable modules inspected, with 284 reachable modules still open. This distinction remains enforced: module reachability and local field identities are not endpoint semantic transport.

## Latest source tranche: graph, interaction, axis, pulse, rebasing, and stress

The map now includes `GraphCalculus`, `LocalizedMeanInteraction`, `NaturalAxisRange`, `PulseGrowth`, `TorusMeanRequestRebase`, and `BaseStressClasses`. These modules document exact off-axis graph derivatives, local mean/wave interaction classes, axis-root and smooth-cutoff parameter control, scalar damping/growth signs, request-coordinate rebasing, and weighted base-stress classes. They still do not establish the final selected Cartesian `(M,I,J,S,C_p)` equality.

Coverage is 335 of 588 reachable modules inspected, with 278 reachable modules still open. No nonzero selected-field defect is inferred from these local results.

## Latest source tranche: scales, endpoint coordinates, and comparison estimates

The map now includes `ChartScales`, `EndpointCoordinates`, `R3/CompactComparisonBounds`, and `R3/ComparisonFiniteEnergy`. These modules document native scale/coefficient asymptotics, endpoint-to-Cartesian coordinate and jet agreement, compact comparison support and cutoff estimates, and finite-energy/tensor-difference bounds. They do not establish the final selected Cartesian `(M,I,J,S,C_p)` equality or a `tsum`-to-`barMoment` transport theorem.

Coverage is 339 of 588 reachable modules inspected, with 274 reachable modules still open. No nonzero selected-field defect is inferred from this tranche.

## Latest source tranche: R3 comparison energy and slot geometry

The map now includes `R3/ComparisonSetup`, `R3/LocalizedDifferenceEnergy`, `R3/LocalizedLaplacian`, `R3/SharpEnergyBound`, `R3/SpatialCauchySchwarz`, `R3/WholeSpaceEnergyLimit`, and `SlotGeometry`. These modules document weighted comparison energies, localized Laplacian/integration identities, scalar energy inequalities, spatial work bounds, whole-space cutoff limits, and torus-slot geometry. They do not establish the final selected Cartesian `(M,I,J,S,C_p)` equality or a `tsum`-to-`barMoment` transport theorem.

Coverage is 346 of 588 reachable modules inspected, with 267 reachable modules still open. No nonzero selected-field defect is inferred from this tranche.
### 2026-09-28 priority-69 source tranche: nine modules registered

Direct source review completed for `AnnularEndpoint.lean`, `AxisContraction.lean`, `PhysicalCopyBounds.lean`, `R3/LocalizedFluxEstimates.lean`, `ResetEnergyBounds.lean`, `ScaledActualParticularControl.lean`, `TerminalCone.lean`, `ViscousPropagator.lean`, and `VolterraAnalyticBounds.lean`. These modules add substantive support/germ, periodisation, reduced-axis, tail-energy, cone, coefficient-propagator, and analytic Volterra bounds. They do not state the final selected Cartesian `torusAverage`/`barMoment` transport theorem, and this tranche yields no nonzero defect, impossibility theorem, or kernel `False`.

The regenerated full semantic register now reports **355 evidence-inspected reachable modules** and **258 reachable modules still open**. The authoritative outputs are `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`, `.md`, and `.html`, mirrored under `docs/`. Detailed evidence is in `NavierStokesReview/src/audit/priority_69_annular_axis_copy_flux_reset_cone_propagator_source_review_2026-09-28.md`.

### Latest source tranche: activation, wave regularity, base context, and copy-solve transport

The map now includes `ActivationBounds`, `ActualWaveRegularity`, `CommonBaseContext`, and `CopySolveCompatibility`. These modules document activation-factor control, smooth actual-wave/curl/tsum regularity, common base/stress context, and generic copy-solve transport. They do not establish the final selected Cartesian `(M,I,J,S,C_p)` equality or a `tsum`-to-`barMoment` theorem.

Coverage is 359 of 588 reachable modules inspected, with 254 reachable modules still open. No nonzero selected-field defect is inferred from this tranche.

### Latest source tranche: pulse amplitude, primary geometry, time averages, and first-order edge

The map now includes `CorrectedPulseAmplitude`, `PrimaryGeometryAssembly`, `R3/ComparisonTimeAverages`, and `SlowFirstOrderEdge`. These modules provide corrected angular-energy/reset identities, reduced phase and chart geometry, finite-energy time-average estimates, and conditional radial-stress closure. `SlowFirstOrderEdge` explicitly delegates global moment closure to separate renormalized-moment and slow-order results. The tranche does not establish the final selected Cartesian `(M,I,J,S,C_p)` transport theorem.

Coverage is now 363 of 588 reachable modules inspected, with 250 reachable modules still open. No nonzero selected-field defect is inferred from this tranche.

### Latest source tranche: base velocity, representatives, context, and reserved patches

The priority-73 review covers `ActualBaseVelocityBounds`, `BaseContextAssembly`, `PhaseEstimates`, `PrimaryRepresentatives`, `PositiveRepresentatives`, and `ReservedPatches`. It records actual coefficient/support and rate results, reduced stress identities, representative geometry, and radial five-row patch identities. These are intermediate/reduced results, not final selected Cartesian `(M,I,J,S,C_p)` transport.

Coverage is now **369 of 588 reachable modules inspected**, with **244 reachable modules still open**. Evidence: `NavierStokesReview/src/audit/priority_73_base_representative_reserved_source_review_2026-09-28.md`.

### Latest source tranche: curl realization, diagonal extensions, carrier binding, and finite heads

The map now includes `LocalizedCurlRealization`, `MixedDiagonalExtensions`, `ActualCarrierTransport`, and `FiniteHeadClass`. These modules document patchwise curl/divergence and germ identities, potential-level support/extension, canonical carrier binding, and finite-prefix jet-class transfer. They do not establish the final selected Cartesian `(M,I,J,S,C_p)` equality or a `tsum`-to-`barMoment` theorem.

Coverage remains 359 of 588 reachable modules inspected, with 254 reachable modules still open. The unchanged count reflects prior register classification; the direct source review is recorded separately.

### Latest source tranche: activation, wave regularity, base context, and copy-solve transport

The map now includes `ActivationBounds`, `ActualWaveRegularity`, `CommonBaseContext`, and `CopySolveCompatibility`. These modules document activation-factor control, smooth actual-wave/curl/tsum regularity, common base/stress context, and generic copy-solve transport. They do not establish the final selected Cartesian `(M,I,J,S,C_p)` equality or a `tsum`-to-`barMoment` theorem.

Coverage is 359 of 588 reachable modules inspected, with 254 reachable modules still open. No nonzero selected-field defect is inferred from this tranche.
## Latest coverage state: 2026-09-28

The authoritative semantic register reports **2,790 indexed; 588 reachable; 375 evidence-inspected; 238 reachable still open; 0 missing project import edges**. The latest tranche classifies activation weights, particular controls, endpoint/dyadic extensions, local physical bounds, and moving-frame ODE code. These layers remain distinct from a proved selected Cartesian `(M,I,J,S,C_p)` transport theorem. See `NavierStokesReview/src/audit/priority_74_activation_control_extension_frame_source_review_2026-09-28.md`.
## Latest coverage state: 2026-09-28 cutoff/Volterra/wave-interaction tranche

The authoritative semantic register reports **2,790 indexed; 588 reachable; 381 evidence-inspected; 232 reachable still open; 0 missing project import edges**. The latest tranche records genuine cutoff, series, local-finite wave, angular-moment, tail-energy, and separated-curl identities. These partial identities must not be inflated into the complete selected Cartesian `(M,I,J,S,C_p)` transport theorem. See `NavierStokesReview/src/audit/priority_75_wave_cutoff_volterra_sum_loop_tail_interaction_source_review_2026-09-28.md`.
## Latest coverage state: 2026-09-28 radial/chart/integral tranche

The authoritative semantic register reports **2,790 indexed; 588 reachable; 392 evidence-inspected; 221 reachable still open; 0 missing project import edges**. The latest tranche records reduced/base radial realisation, actual radial aliases and integration-by-parts identities, chart jets, rephasing, and endpoint regularity. These partial results are not the complete selected Cartesian `(M,I,J,S,C_p)` transport theorem. See `NavierStokesReview/src/audit/priority_76_radial_chart_jets_extension_rephase_integral_source_review_2026-09-28.md`.

## Latest coverage state: 2026-09-28 axis/dilation/extension/ODE tranche

The authoritative semantic register reports **2,790 indexed; 588 reachable; 400 evidence-inspected; 213 reachable still open; 0 missing project import edges**. `OutgoingDilation` now records direct reduced-profile definitions and identities for `M`, `I`, `J`, `S`, `renormalizedI`, and `axisDatum`. The map therefore distinguishes genuine upstream moment evidence from the still-unresolved complete selected Cartesian endpoint transport. See `NavierStokesReview/src/audit/priority_77_axis_evaluation_resolvent_phase_gaussian_dilation_extension_ode_source_review_2026-09-28.md`.

### 2026-09-28 priority-78 phase/axis/weighted-integral update

The authoritative semantic register now reports **2,790 indexed; 588 reachable; 414 evidence-inspected; 199 reachable still open; 0 missing project import edges**. The latest source review maps phase-defect and phase-jet identities, axis harmonic algebra, coefficient/radial weights, edge and polar regularity, stress activation, and weighted Volterra integrals. These are positive intermediate layers; the complete selected Cartesian `(M,I,J,S,C_p)` transport remains unestablished. Evidence: `NavierStokesReview/src/audit/priority_78_phase_defect_axis_algebra_weighted_volterra_source_review_2026-09-28.md`.

### 2026-09-28 priority-79 axis/chart/covariance update

The authoritative semantic register now reports **2,790 indexed; 588 reachable; 420 evidence-inspected; 193 reachable still open; 0 missing project import edges**. The latest source review maps axis jet operators, actual chart/component identities, matching-cone bounds, physical coordinate scaling, signed covariance reconstruction, and moving radial-edge extensions. These are positive intermediate layers; complete selected Cartesian `(M,I,J,S,C_p)` transport remains unestablished. Evidence: `NavierStokesReview/src/audit/priority_79_axis_chart_matching_coordinate_covariance_edge_source_review_2026-09-28.md`.
## Priority 80: reduced radial bridges versus selected endpoint (2026-09-28)

Direct review of `BoundaryAxisJets`, `GenericEndpointExtension`, `PhaseJetBounds`, `RadialPullback`, `ReferencePath`, and `WeightedRadialPrimitive` is recorded in the NavierStokesReview audit report. The axis, gluing, phase-jet, and weighted-primitive files provide substantive local regularity and reduced integral transport. `RadialPullback.total_normalized_eq_radialIntegral` and `physicalCompact_eq_radialIntegral` are exact reduced radial identities; `WeightedRadialPrimitive` transports weighted `MeanClass` bounds; `ReferencePath.histories` rebuilds reduced pressure/moment state from `REF`.

The map must not collapse these results into a final-field theorem. No reviewed declaration composes them through the selected Cartesian curl/localisation/`tsum`/periodisation route into `barMoment` or the public `Witness`. Register status: CTR-005 remains open at the selected endpoint; no `Delta m != 0` is asserted.
## Priority 81: concrete residual and reduced-moment bridges (2026-09-28)

`R3CompactCandidate` transfers periodic local candidate properties to compact whole-space fields. `MixedDiagonalResidual` defines the residual from the actual potential sums and proves the corresponding original-residual identity and physical joint zero jets. `GaugeRadialResidualBounds.pressureDefect_eq_mass` identifies the pressure defect with the actual auxiliary-torus-averaged zeroth radial mass. `OutgoingSchedule` proves exact cancellation of two combined reduced log-radius moments at the endpoint.

These findings replace any blanket “no moment bridge exists” wording. The remaining gap is the full composition from these reduced identities to all five paper observables of the selected Cartesian field and their export through `ActualCandidateAssembly.Witness`.

## Priority 82: debt, exterior, scaling, and entrance bridges (2026-09-28)

`ActualIntermediateDebtBounds` derives concrete three-component intermediate debt from checked correction-step data. `ActualMeanExterior` proves annular support and exterior vanishing for actual mean/cycle families. The R³ scaling modules prove exact energy and support transformations, while `R3ActualCandidate` provides a direct selected-to-compact candidate wrapper. `NaturalEntrance` proves exact reduced angular and axial source-flux identities.

These results strengthen the positive intermediate correspondence record. They do not supply the missing composition from the final Cartesian curl/localisation/`tsum`/periodisation field to the complete `(M,I,J,S,C_p)` observable tuple at `Witness`.

## Priority 83: localisation, stress, signed requests, and covariance (2026-09-28)

`SquaredPartition` proves exact smooth squared-mask normalisation and finite-tail identities. `DirectAngularDiagonal` constructs the mixed potential-plus-angular field and proves divergence/axis-germ results. `GaussianTailFlat` proves compact derivative support and Gaussian domination of dyadic powers. `LeadingStressWeights` proves reduced stress edge/exterior and weighted bounds. `LocalSignedRequest` proves torus-average/profile transport, radial divergence, compact support, and zero adjusted moments. `PulseCovariance` proves actual covariance factorisation and strict-cone positivity.

These are substantive positive intermediate correspondences. They still do not establish the complete selected Cartesian `(M,I,J,S,C_p)` observable equality at `ActualCandidateAssembly.Witness`.

## Priority 84: axis, heat, release, and torus averages (2026-09-28)

`PositiveAxisExistence` proves actual positive-order axis profile existence and regularity. `PulseLag` proves the actual convolution/lag equations and reset estimates. `RadialHeatProfile` proves exact radial heat moment ODEs. `ReleaseMoments` and `RenormalizedHeatMoment` prove scheduled renormalised moment cancellation and heated physical axial-viscosity cancellation under explicit hypotheses. `TorusAverages` proves periodisation, Jacobian, native-chart, product-separation, and angular-average identities.

These are positive intermediate correspondences, not the complete selected Cartesian `(M,I,J,S,C_p)` observable equality. The authoritative register now reports 2,790 indexed, 588 reachable, 450 evidence-inspected, 163 reachable-open, and 0 missing project import edges. Evidence: `NavierStokesReview/src/audit/priority_84_axis_heat_release_torus_source_review_2026-09-28.md`.

## Priority 85: signed geometry and reduced five-row transport (2026-09-28)

`RepairConeBounds.actual_moments` is a genuine reduced five-coordinate equality to `freeRows`; `physical_rows`, `physical_stock_values`, `physical_transport`, `physical_lags`, and `physical_stocks` continue it through the explicit physical chart. `HeatSwitchCone` supplies compensated cone and exact change-row identities. `LabelSumBounds`, `CommonCoverClass`, `ActualSignedGeometry`, and `ActualSignedStageControls` supply actual finite-sum, common-cover, signed geometry, covariance, cutoff, and jet controls.

This corrects any repository-wide “no five-moment bridge” wording. The remaining map boundary is the composition from these reduced/physical values through the final Cartesian curl/localisation/`tsum`/periodisation/pressure-force construction into `ActualCandidateAssembly.Witness`. The authoritative register now reports 2,790 indexed, 588 reachable, 456 evidence-inspected, 157 reachable-open, and 0 missing project import edges. Evidence: `NavierStokesReview/src/audit/priority_85_signed_geometry_repair_cone_source_review_2026-09-28.md`.

## Priority 86: rank patch and cycle induction (2026-09-28)

`BaseRankPatch.five_rows` proves a direct local `FiveRowRank.FiveRows` theorem for the full final base on the mean patch. `ActualCycleExcluded` and `CorrectionAnalyticStep` preserve actual primitive, covariance, and cycle invariants; `RankStateBounds` supplies variable-gauge rank-increment bounds; `ParametricTerminalCompensation` supplies actual physical three-component compensation; and `ActualMeanStageData` supplies concrete mean-stage fields and shrinking supports.

These are positive local correspondences. The authoritative register now reports 2,790 indexed, 588 reachable, 462 evidence-inspected, 151 reachable-open, and 0 missing project import edges. The remaining boundary is the full composition into the final selected Cartesian field and `Witness`. Evidence: `NavierStokesReview/src/audit/priority_86_rank_cycle_compensation_source_review_2026-09-28.md`.

## Priority 87: residual grouping, diagonal rates, and compact force (2026-09-28)

`AxisymmetricResidualGrouping` and `LocalResidualGrouping` provide actual mode bookkeeping, finite disjoint-support residual sums, angular means, and reconstruction. `DiagonalResidual` provides stage-to-limit jet-rate transfer and a spatial-curl loss estimate, including order-by-order all-jet flatness. `CompactForceDecay`, `CompactSpatialForceDecay`, and `R3/CompactForceBound` provide temporal/spatial compact-force decay and a uniform \(R^3\) force \(L^2\) bound.

These are positive intermediate correspondences. They do not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. The authoritative register now reports 2,790 indexed, 588 reachable, 468 evidence-inspected, 145 reachable-open, and 0 missing project import edges. Evidence: `NavierStokesReview/src/audit/priority_87_residual_grouping_decay_compact_force_source_review_2026-09-28.md`.

## Priority 88: profile cones, covers, similarity, and mean updates (2026-09-28)

`AlignedProfileSpectralCone`, `ProfileSpectralCone`, `OutgoingCone`, and `OutgoingEntranceCone` connect actual reduced histories to spectral/true cones, stress margins, and entrance/exit bounds. `LoopMoments` and `RadialModulation` provide finite rephasing/variance algebra and smooth periodic modulation estimates. `AxisHolomorphic`, `SimilarityHomogeneity`, `SimilarityProfile`, and `HeatProfileExtension` provide analytic series, chart transitions, physical pullbacks, and all-jet heat-profile extension. `AxisymmetricFields` provides the explicit Cartesian curl lift and support bounds; `CommonCoverSolve` provides copy/deck/torus assembly; `TemporalMeanUpdate` provides zero-mean temporal inversion and supported mean updates.

These are positive intermediate correspondences. They do not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. The authoritative register now reports 2,790 indexed, 588 reachable, 483 evidence-inspected, 130 reachable-open, and 0 missing project import edges. Evidence: `NavierStokesReview/src/audit/priority_88_profile_cone_cover_similarity_mean_source_review_2026-09-28.md`.

## Priority 89 source correspondence update (2026-09-28)

The eleven-module tranche adds positive correspondences for compact/reduced moment repair, torus inverse and alias transport, stress algebra, local gauge-mass preservation, and Cartesian curl covariance. It does not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. The authoritative register now reports 2,790 indexed, 588 reachable, 494 evidence-inspected, 119 reachable-open, and 0 missing project import edges. Evidence: `NavierStokesReview/src/audit/priority_89_moment_repair_stress_alias_curl_source_review_2026-09-28.md`.

## Priority 90 source correspondence update (2026-09-28)

The five-module tranche adds positive correspondences for generalised-power/bump moment matrices, scheduled/prepared profiles, R3 Gaussian integrability, and smooth quadratic repair. It does not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. The authoritative register now reports 2,790 indexed, 588 reachable, 499 evidence-inspected, 114 reachable-open, and 0 missing project import edges. Evidence: `NavierStokesReview/src/audit/priority_90_moment_matrix_prepared_profiles_gaussian_solver_source_review_2026-09-28.md`.

## Priority 91 source correspondence update (2026-09-28)

## Priority 92 source correspondence update (2026-09-28)

The R3 tranche adds positive correspondence for force L2/cumulative norms, viscous energy and dissipation estimates, smooth positive-time force support, scalar forced Gronwall bounds, off-axis residual polar reconstruction, and uniform primary/curl rate classes. The authoritative register now reports 2,790 indexed, 588 reachable, 508 evidence-inspected, 105 reachable-open, and 0 missing project import edges. These results do not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. Evidence: `NavierStokesReview/src/audit/priority_92_r3_energy_force_polar_graph_uniform_weights_source_review_2026-09-28.md`.

`ParametricTorusInverse` supplies source-level correspondence for a smooth parametric torus inverse, Fourier multipliers, zero-mean periodic data, rapid-decay and finite-jet estimates, and inverse-multiplier application. `PeriodicPhaseAssembly` supplies source-level correspondence for compact clock windows, locally finite tsum periodisation, phase/angular-lift periodicity, geometry transport, and carrier-adapter germs/jets. The authoritative register now reports 2,790 indexed, 588 reachable, 501 evidence-inspected, 112 reachable-open, and 0 missing project import edges. These results do not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. Evidence: `NavierStokesReview/src/audit/priority_91_parametric_inverse_periodic_phase_source_review_2026-09-28.md`.
## Priority 93 source correspondence update (2026-09-28)

`JointResidualLimits`, `MatchingDebtBounds`, `MaximalLifespan`, `MeanBoundsReindex`, `PulseEnergyHistory`, and `RadialFluxResidual` provide source-level correspondence for smooth boundary limits and flat residual extensions, reduced debt matching, relative lifespan consequences, exact rate-class reindexing, pulse energy histories, and an off-axis radial residual identity. The authoritative register now reports 2,790 indexed, 588 reachable, 514 evidence-inspected, 99 reachable-open, and 0 missing project import edges. These results do not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. Evidence: `NavierStokesReview/src/audit/priority_93_limits_debt_lifespan_reindex_pulse_flux_source_review_2026-09-28.md`.
## Priority 94 source correspondence update (2026-09-28)

## Priority 95 source correspondence update (2026-09-28)

`ActualPressureFlux`, `PressureFluxIdentity`, `PressureFunctionals`, `PressureRecoveryHelpers`, and `PressureTemporalIdentity` provide source-level correspondence for compact-test relative pressure recovery, weak differentiated Poisson identities, canonical Riesz pairings, and temporal integration. The Riesz modules provide Fourier-symbol regularity, pairings, decay, heat representation, and L2/Sobolev estimates. `ViscosityScaling`, `NormalScaling`, `WholeSpaceComparisonClosure`, `ScalarParticularSupport`, and `TangentProjection` provide scaling, comparison, support, and finite-dimensional projection layers. The authoritative register now reports 2,790 indexed, 588 reachable, 539 evidence-inspected, 74 reachable-open, and 0 missing project import edges. These results do not provide an absolute selected pressure representative or the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. Evidence: `NavierStokesReview/src/audit/priority_95_r3_pressure_comparison_scaling_source_review_2026-09-28.md`.

`ModulatedHistories`, `ActualInitialMean`, `HarmonicSourceSupport`, `HarmonicFields`, `ActualExteriorPrefix`, `ActualParticularMeanGain`, and `ActualSignedFamilySupport` provide source-level correspondence for reduced history repair, initial mean/covariance/rank data, harmonic support and angular calculus, exterior prefix/germ agreement, local covariance gain, and signed potential/pressure support. The authoritative register now reports 2,790 indexed, 588 reachable, 521 evidence-inspected, 92 reachable-open, and 0 missing project import edges. These results do not provide the complete selected Cartesian `(M,I,J,S,C_p)` equality at `Witness`. Evidence: `NavierStokesReview/src/audit/priority_94_histories_means_harmonic_exterior_source_review_2026-09-28.md`.

## Priority 96 source correspondence update (2026-09-28)

## Priority 97 source correspondence update (2026-09-28)

The eleven-module review [`priority_97_local_curl_profile_moment_bridge_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_97_local_curl_profile_moment_bridge_source_review_2026-09-28.md) records genuine local curl/potential realisation and reduced/chart moment identities. These declarations are positive correspondence edges at intermediate layers. They do not by themselves establish the selected global-sum, localisation, periodisation, and endpoint-observable composition required for the final Cartesian `(M,I,J,S,C_p)` transport claim.

## Priority 98 source correspondence update (2026-09-28)

The eleven-module review [`priority_98_signed_gauge_copy_support_axis_transport_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_98_signed_gauge_copy_support_axis_transport_source_review_2026-09-28.md) adds positive correspondence edges for signed regularity, gauge/alias coherence, copy transport, support preservation, reduced exterior matching, axis pressure data, signed stage data, pressure-kernel estimates, and tangent scaling. These edges remain intermediate and do not supply the final selected global observable theorem.

## Priority 109 source correspondence update (2026-09-28)

The twelve-module review [`priority_109_carrier_cycle_signed_axis_pressure_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_109_carrier_cycle_signed_axis_pressure_source_review_2026-09-28.md) adds positive edges for current-band support, signed `tsum` transport, cycle/copy coherence, angular curl invariance, dependent-family periodisation, reduced natural-axis transport, future pressure integrals, physical-stage bounds, and comparative pressure flux. These are not the final selected Cartesian observable edge: `barMoment` / `(M,I,J,S,C_p)` transport remains unestablished.

## Priority 110 source correspondence update (2026-09-28)

The four-module review [`priority_110_cycle_initial_particular_pressure_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_110_cycle_initial_particular_pressure_source_review_2026-09-28.md) adds positive edges for initialized states, coherent cycle iteration, particular native source/pressure data, and reduced corrected-pressure matching. These do not supply the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` edge.

## Priority 111 source correspondence update (2026-09-28)

`ActualCyclePreservation`, `ActualParticularRealization`, and `ActualParticularCoherence` supply real cycle-state, curl, pressure, germ, cutoff, support, periodicity, and domain-equality transport. The map therefore records a populated intermediate path rather than a blank bridge. The selected global radial-observable composition remains `CORRESPONDENCE_GAP` until a declaration links the final field to `barMoment` / `(M,I,J,S,C_p)`.

## Priority 112 source correspondence update (2026-09-28)

`ActivationStocks`, `DiagonalJetBounds`, and `ExtendedHeatedOutgoing` add positive correspondence for reduced activation stocks, locally finite `tsum` derivative/tail estimates, and compensated outgoing-profile pressure/energy/zero-moment identities. The selected global radial-observable composition remains `CORRESPONDENCE_GAP`; no nonzero defect, impossibility theorem, or `False` result is asserted. The authoritative register reports 2,790 indexed, 588 reachable, 602 evidence-inspected, 11 reachable-open, and 0 missing project import edges.

## Priority 113 source correspondence update (2026-09-28)

`HeatedOutgoing`, `ModeSolenoidalReindex`, and `ShapedWaitBounds` add positive correspondence for reduced compensation rows, local mode-level solenoidal reindexing, and temporal hold/wait and decay estimates. These remain intermediate edges and do not close the final selected Cartesian localisation/periodisation-to-`barMoment` composition. The authoritative register reports 2,790 indexed, 588 reachable, 605 evidence-inspected, 8 reachable-open, and 0 missing project import edges. No nonzero defect, impossibility theorem, or `False` result is asserted.

`ActualCoreSupport`, the signed/unmasked and uniform-block bound layers, `TimeLocalization`, `ConservativeDifference`, `PressureFluxTest`, `PressureRecovery`, `RieszTestOperators`, `SchedulePressure`, and `TailCone` provide source-level correspondence for concrete support, switched residuals, comparative weak pressure/Poisson identities, compact pressure tests, Riesz regularity, reduced axis pressure, tail/cone bounds, and uniform rate classes. The authoritative register now reports 2,790 indexed, 588 reachable, 558 evidence-inspected, 55 reachable-open, and 0 missing project import edges. These results do not provide an absolute selected pressure representative or the complete selected Cartesian `(M,I,S,J,C_p)` equality at `Witness`. Evidence: `NavierStokesReview/src/audit/priority_96_core_support_pressure_recovery_localization_source_review_2026-09-28.md`.
