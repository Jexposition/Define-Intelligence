# Priority 169: declaration-level adjudication of the five-moment force-smoothness rebuttal

Date: 2026-09-29
Status: source-checked, adverse correspondence finding retained

## Executive result

The supplied rebuttal is partly right about the importance of the five cumulative
quantities, but it overstates three conclusions:

1. velocity blow-up does not imply that every summand of the momentum residual
   diverges;
2. the manuscript does not present the five moments as its only residual
   cancellation operation; and
3. the selected Lean force route is not an empty NativeBounds assumption.

The source trace confirms a material remaining issue. The selected endpoint
contains a concrete cycle-invariant and residual-rate route to VanishingJointJets
and a smooth force, but the inspected public Witness and the declarations feeding
it do not state a theorem identifying the completed activated Cartesian fields with
the manuscript's named tuple (M,I,J,S,Cp).

The correct classification is:

> CTR-005: complete paper-to-endpoint correspondence NOT ESTABLISHED.

This is not a proof of a nonzero selected-field defect, nonsmooth force, or literal
failure of Fefferman Alternative (C). Those stronger conclusions require a direct
selected-field mismatch, impossibility theorem, failed mandatory CMI premise, or
selected-path False.

## 1. Source correction to the rebuttal's PDE logic

The manuscript itself states that the individual terms in the momentum residual
may diverge while their sum and all derivatives extend smoothly through the
singular time (docs/navier-stokes openai.txt:108-113). It then says that the
background residual is unbounded, that oscillatory pulses cancel its singular
part, and that further corrections remove the remaining singular errors
(docs/navier-stokes openai.txt:118-124).

Consequently, the implication

  ||u(t)||_infinity -> infinity
  implies divergence of every one of
  partial_t u, (u dot grad)u, Delta u, and grad p

does not follow. The residual is a sum,

  f = partial_t u + (u dot grad)u - nu Delta u + grad p,

and singular summands may cancel. The paper's burden is to prove the cancellation
and smooth extension, not to infer termwise divergence from the velocity norm.

## 2. The five moments are load-bearing, but not the sole cancellation route

Section 3.4 separately lists:

1. inhomogeneous wave-amplitude equations for supported nonzero angular modes;
2. signed-amplitude covariance correction for the averaged stress;
3. auxiliary-time inversion for the angularly averaged residual; and
4. the five radial moment equations for pressure, tangential momentum, and
   preserved integrals.

The source is explicit that these operations control different classes of terms
(docs/navier-stokes openai.txt:711-735). The five equations are indispensable
within the profile and mean-correction architecture, but the proposition that
they are the only cancellation mechanism is not source-supported.

Appendix C confirms a narrower fact: radial modulation creates O(N^-1) moment
errors, and five compact bumps restore those profile moments exactly
(docs/navier-stokes openai.txt:8391-8518). This proves load-bearing profile
matching. It does not by itself prove that the same identities have been
transported through the final Cartesian tsum, curl, localisation, periodisation,
pressure, and force-extension composition.

## 3. Exact selected Lean route inspected

The selected path is not an unproved rate contract. The declarations give this
proof-term route:

| Layer | Source declaration | What it proves or consumes |
|---|---|---|
| Cycle invariant | CorrectionStep.lean:9408-9461, CycleAnalyticInvariant | Representation, bands, supports, smoothness, solenoidal modes, cumulative bounds, covariance, residual classes, three-component debt, reconstruction, and two zero-mass constraints. |
| Run invariant | ActualCyclePreservation.lean:768-771, RunInvariant | Packages analytic, coherence, and periodic invariants. |
| Induction | ActualCyclePreservation.lean:800-833 | Derives each actual cycle state from the preceding state and constructed particular data. |
| Concrete physical data | ActualCycleResidualBounds.lean:1015-1030, PhysicalFields | Requires smoothness, differentiability, physical germs, exterior germs, and related stage regularity. |
| Physical residual bridge | ActualCycleResidualBounds.lean:1089-1105, Invariant.stateRealization | Converts invariant and physical data into StateRealization; no named FiveProfileMoments equality occurs in this type. |
| Residual rates | ActualCycleResidualBounds.lean:1158-1172, Invariant.residual_jetRate | Consumes stateRealization, native_residual, physical data, exterior germs, and base-exterior estimates. |
| Finite stage rates | ActualCycleResidualBounds.lean:1190-1206, finite_residual_rates | Applies residual_jetRate for every cycle index. |
| Selected estimates | ActualStageEstimates.lean:347-403 | Builds StageEstimates from finite residual rates, broad_invariant, and concrete physical data. |
| Actual endpoint estimates | ActualCandidateAssembly.lean:1090-1096 | Instantiates actual stage estimates with runData, coherent cycles, signed inputs, representations, and physicalData. |
| Flat residual | MixedDiagonalResidual.lean:168-266, physical_vanishingJointJets | Derives vanishing joint residual jets from stage smoothness and quantitative rate bounds. |
| Smooth force | CandidateFromLimits.lean:47-87 | Extends the residual across the endpoint using compatible derivative limits. |
| Selected envelope | ActualCandidateAssembly.lean:1121-1151, Witness | Exports selected sums, extensions, activated fields, force regularity, consequences, blow-up, decay, and endpoint derivative limits. |

This route disproves the narrower assertion that force_smooth is obtained by
simply assuming an empty NativeBounds interface. It does not close the separate
paper-fidelity question.

## 4. What the invariant's five-looking controls do and do not show

The cycle invariant contains related controls. In CorrectionStep.lean:9408-9461,
CumulativeBounds contains three mean-class bounds. In CorrectionState.lean:242-248,
DefectBounds is a three-component defect (P,J_theta,J_z). In
CorrectionState.lean:250-252, ZeroMasses contains two zero radial moments.
GaugeMassPreservation.lean:140-142 states the corresponding ZeroMassesOn
conditions.

There is also a genuine row-level bridge: CorrectionState.lean:449-458 proves
FiveRowRank.FiveRows for the rank increment, and
StateMomentBalances.lean:956-1007 proves radial moment identities for the
constructed axial flux and pressure recipe.

These are important positive findings. The review must not say that the
five-coordinate correction machinery is dead, absent, or unrelated to the
selected cycle construction.

They do not yet prove the stronger endpoint statement

  Moments(u_selected,p_selected,f_selected) = (M,I,J,S,Cp),

because the inspected residual-rate declarations consume the invariant and
physical-data records without exposing that final observable map, and the public
Witness type contains no such equality. Related correction-state controls are not
automatically identical to the manuscript's five reduced-profile observables after
infinite summation, Cartesian curl, localisation, periodisation, pressure assembly,
and force extension.

## 5. Why the formal endpoint can compile without this named equality

There is no logical contradiction in these two statements:

  Lean proves the declared forced endpoint E.
  The public endpoint does not expose the manuscript's named observable map B.

The declared endpoint is a proposition built from regularity, residual, support,
periodicity, energy, and blow-up predicates. Its construction uses a concrete
rate-to-flatness route. A named equality B is not required by the type unless a
theorem explicitly uses it. Thus E does not imply B, but E is not thereby false.
Conversely, proving E does not establish B unless the proof term or an exported
theorem connects them.

The endpoint's axis blow-up comes from the origin_blowup route in
GermCandidateAssembly.lean:164-304. Force smoothness comes from
physical_vanishingJointJets and CandidateFromLimits.force_smooth. This explains
how the formal proposition can be inhabited. It does not show that the manuscript's
complete five-moment explanation has been transported to the exported field.

## 6. Adjudication

| Rebuttal claim | Adjudication |
|---|---|
| Blow-up forces every residual summand to diverge | Rejected. Contradicted by the manuscript's explicit cancellation description. |
| Five moments are the only cancellation route | Rejected. Section 3.4 lists four connected correction operations. |
| force_smooth is merely an abstract NativeBounds assumption | Rejected. Concrete invariant and physical-data declarations feed residual rates and flatness. |
| Five moments are load-bearing in the manuscript | Confirmed. Matching, pressure/stress propagation, modulation repair, and cycle compatibility depend on them. |
| Witness exposes the complete selected-field five-observable identity | Not located. This remains CTR-005. |
| The selected field has a nonzero moment defect or the force is nonsmooth | Not proved. No selected value-level mismatch was found in this tranche. |
| Literal Alternative (C) is formally false | Not proved. The compiled endpoint contains the relevant formal regularity, residual, and blow-up predicates. |

## 7. Required next test

The next test must be declaration-level:

1. identify every theorem used to construct H.debt, H.masses, and the FiveRowRank
   rows;
2. follow those values through the actual stage sequence into physicalData;
3. calculate or prove the corresponding observable after potentialSum, curl,
   localisation, periodisation, and activation; and
4. compare that value with the manuscript's (M,I,J,S,Cp) definitions.

Until that map is proved or disproved, the accurate adverse conclusion is that the
paper's complete five-moment mechanism is not established as the semantics of the
exported endpoint. The audit must not replace that conclusion with either a
compiler-cheat allegation or an unsupported formal refutation.
