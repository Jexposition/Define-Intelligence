# Priority 132: endpoint-external Navier--Stokes junction and H³/periodic candidate review

Date: 2026-09-28

## Scope

This tranche reviews fifteen current OpenAI source files that are outside the
captured dependency closure of `NavierStokesR3.theorem_1_1` but contain strong
endpoint, candidate, periodic, comparator, or H³ markers in the full source
profile. “Outside the captured closure” is a graph-scope fact only. It does
not mean dead, irrelevant, uncompiled, or semantically empty.

The exact line-addressed navigation index is
`NavierStokesReview/evidence/source_tranche_external_ns_junction_2026-09-28.json`.
The conclusions below are source-level classifications, not claims that a
missing theorem cannot exist elsewhere.

## File-by-file findings

| File | Exact declarations/anchors | Finding | Relation to paper-to-endpoint audit |
|---|---|---|---|
| `NavierStokes/CandidateAssembly.lean` | `assembledForce` 25; `assembledForce_eq_residual` 56; `assembled_candidate_properties` 186; `candidateStatement_of_late_force` 211 | Builds a conditional candidate from already supplied `u`, `p`, and future force `F`; proves the assembled force equals the residual on the PDE interval and packages `CandidateProperties`. It does not construct the input fields or a five-observable transport theorem. | Positive residual/packaging infrastructure; not a selected Cartesian `(M,I,J,S,C_p)` bridge. |
| `NavierStokes/R3/H3CandidateStrong.lean` | `strongSolution_of_compact_slab` 87; `candidate_classicalH3Solution` 111 | Converts `CandidateProperties` plus compact support and smoothness into a classical H³ solution on shorter intervals. | Downstream regularity packaging; it consumes candidate properties rather than proving their physical construction. |
| `NavierStokes/R3/H3Continuity.lean` | `H3ContinuousOn` 25; `h3ContinuousOn_of_compact_slab` 81; `candidate_h3ContinuousOn` 99 | Establishes continuity of H³-type quantities from compact slabs and smooth derivatives. | Supports candidate regularity; no radial moment observable or selected-field transport. |
| `NavierStokes/R3/H3CandidateUniqueness.lean` | `integral_inner_pressureGradient_zero` 20; `strong_unique` 45; `candidate_unique_on_Icc_h3` 90 | Proves pressure-pairing cancellation and weak-strong uniqueness under explicit hypotheses; derives force integrability from candidate support. | Genuine comparative uniqueness; does not give an absolute selected pressure representation or paper-profile moments. |
| `NavierStokes/ComparatorTheorem.lean` | `option_D_of_candidate` 25; `navier_stokes_breakdown_periodic` 47 | Converts a candidate satisfying the comparator predicate into the periodic option-D statement using rescaling and force-decay conditions. | A real alternate C/D packaging route; still inherits the supplied `CandidateProperties` and does not add moment transport. |
| `NavierStokes/LocalAngularGrowth.lean` | `selectedPotential` 138; `selectedVelocity` 146; `selectedVelocity_angularGrowth` 217; `selected_candidate_one_with_angular_growth` 238 | Constructs selected schedule aliases and proves an angular-growth candidate property from the existing `ActualCandidateAssembly.selected_witness` and residual-band data. | Concrete selected-path evidence for growth; no equality between final Cartesian observables and `(M,I,J,S,C_p)`. |
| `NavierStokes/LocalScheduleWitness.lean` | `potentialSum` 22; `Selected` 37; `selected_periodic_candidate` 129; `selected_compact_candidate` 156 | Defines potential/direct/pressure sums, a schedule predicate, and conditional periodic/compact candidate constructions. | Important local assembly junction; it packages sums and support but does not expose a five-moment field theorem. |
| `NavierStokes/PeriodicPaperTheorem.lean` | `CandidateProperties` 26; `GlobalSmoothSolution` 51; `CandidateProperties.no_global_solution` 65; `of_compact_candidate` 92; `periodic_corollary` 155 | Defines a periodic paper-level candidate predicate with smoothness, periodicity, fundamental-cube support, force time support, and residual equality. The “support” clauses are explicitly cube-intersection clauses for periodic lifts, not global compact support. | Corrects a potential pressure/support misreading; this alternate periodic predicate still contains no five-moment tuple. |
| `NavierStokes/R3/H3Blowup.lean` | `candidate_h3Norm_unbounded` 40; `candidate_no_h3_continuation` 53; `candidate_no_classicalH3_extension` 66 | Derives H³ norm unboundedness and non-continuation from the candidate’s origin-speed blow-up and compact-slab bounds. | Genuine consequence of the formal candidate predicate; not evidence that the paper’s profile repair identities reach the field. |
| `NavierStokes/PeriodicPaperComparator.lean` | `forceConditionPeriodic_of_paper_candidate` 21; `option_D_same_force_of_paper_candidate` 31; `option_D_of_paper_candidate` 45 | Transfers a periodic-paper candidate into the comparator’s periodic force condition and option-D statement using the same force. | Real comparator transport for the declared periodic predicate; no moment transport. |
| `NavierStokes/R3/H3CompactCurve.lean` | `continuous_compact_slices_toLp` 16; `h3Curve_of_compact_slab` 48; `candidate_h3Curve` 69 | Establishes compact-slab Lᵖ/H³ curve regularity for candidate fields. | Regularity only; no global radial observable. |
| `NavierStokes/PaperLocalization.lean` | `compact_pressure_eq_local` 20; `local_theorem_with_compact_candidate` 28 | Shows localized pressure agrees with a supplied pressure on the late-time local region and packages a local candidate. | Local agreement is positive evidence, but is not global transport through `tsum`, localisation, periodisation, and `barMoment`. |
| `NavierStokes/R3/H3MaximalLifespan.lean` | `candidate_agrees_with_classicalH3` 43; `candidate_classicalH3_lifespan_le_one` 57; `candidate_is_maximal_classicalH3` 76; `theorem_1_1_with_maximalH3` 109 | Defines and compares H³ lifespans and packages maximality at time one under the declared candidate assumptions. | Alternate maximal-H³ endpoint path; requires candidate properties and does not independently validate their paper semantics. |
| `NavierStokes/R3/ComparatorBridge.lean` | `forceConditionDecay_of_compact` 22; `globalSolutionOfComparator` 48; `comparator_of_breakdown` 77 | Converts compact force support into comparator decay and derives option C from candidate breakdown using the same force. | Genuine force/comparator bridge; still conditional on candidate properties and not a five-moment bridge. |
| `NavierStokes/R3/ViscousUniqueness.lean` | `candidate_unique_on_Icc_viscosity` 23 | Applies viscosity rescaling and comparison to establish uniqueness on pre-singular intervals. | Comparative uniqueness evidence; no absolute pressure or profile-moment transport. |

## Cross-file result

This tranche closes a possible naming/branch oversight: there are several
alternate candidate, periodic, H³, comparator, and local-angular constructions
outside the captured endpoint closure. They are not dead code. They contain
real conditional theorem chains, including:

\[
\text{CandidateProperties}
\longrightarrow
\text{H}^3\text{ regularity/blow-up}
\longrightarrow
\text{periodic/comparator option C/D packaging}.
\]

The source reviewed here still does not expose a declaration of the form

\[
\operatorname{barMoment}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
  = (M,I,J,S,C_p),
\]

nor a theorem transporting the five reduced-profile quantities through the
actual selected Cartesian sums, curl, localisation, periodisation, and
infinite-sum limits. This report therefore strengthens the positive record of
OpenAI’s alternate candidate/comparator infrastructure while leaving CTR-005
as a correspondence question, not a kernel contradiction.

## Scope limits and next checks

1. The files are now source-reviewed, but their full transitive proof bodies
   still require the compiled declaration-dependency join for any claim about
   endpoint use.
2. `CandidateProperties` inheritance is not by itself a proof that the field
   construction matches the paper’s reduced profile mechanism.
3. The periodic support wording must remain cube-relative; it must not be
   paraphrased as global compact support of a nonzero periodic lift.
4. The two standalone `ComparatorChallenges` files remain a separate metadata
   audit lane because they contain admitted tokens outside the active endpoint.
