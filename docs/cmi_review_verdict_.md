# Superseded provisional verdict: OpenAI Navier-Stokes formalisation

> **2026-09-29 source correction.** The earlier “missing five-moment transport”
> formulation is superseded. Raw inspection now establishes that profile
> moments and rank repair feed coefficient matching, finite Cartesian residual
> identities, residual estimates, and the selected candidate construction.
> The absence of a named `(M,I,J,S,C_p)` field in the final existential
> envelope is not, by itself, a failed CMI proof or a kernel refutation. The
> remaining review is the exact paper/CMI semantic crosswalk and any concrete
> mismatch or impossibility that can be proved from the selected fields.

This file is retained as supporting material. The active verdict is in
`OpenAI_NavierStokes_Peer_Review_v1.md`, and the active evidence ledger is in
`OpenAI_NavierStokes_Audit_Tracker.md`. Claims below are subordinate to those
documents and to `REVIEW_DOCUMENT_CONTROL.md`.

## Direct verdict on the published solution claim

OpenAI's paper claims a solution of the Navier–Stokes problem. The raw source
now establishes more than the earlier verdict credited: the profile moment
and rank-repair machinery feeds coefficient matching, finite Cartesian
residual identities, residual estimates, selected physical data, and the
candidate construction. The endpoint also proves its Lean-defined forced
breakdown proposition under the standard foundational dependencies.

The final existential envelope does not repeat the profile certificate as a
named `(M,I,J,S,C_p)` field. That is a packaging fact, not evidence that the
mechanism was omitted. The active verdict is therefore not “formally refuted
because the moment bridge is missing.” The remaining question is whether the
paper's full CMI interpretation and every advertised analytic consequence
have been proved for exactly the selected fields, pressure, force, support,
and endpoint. No concrete mismatch, impossibility theorem, or kernel-level
`False` has been established by the tuple omission.

## Verification correction: selected endpoint and temporal boundary

The source-backed audit confirms that the force is a residual-based construction, but the public CMI alternatives permit smooth forcing, so that fact alone is not a disqualification. The exact source boundary must be quoted: `CandidateFromLimits.force_zero_from` establishes the zero-force branch from `t ≥ 2`, while the activated residual branch is used for `t < 1`. The claim that the force is glued to zero from `t ≥ 1` is therefore incorrect.

Likewise, `finalPotential_smooth` is derived from smooth coefficient data, and `force_smooth` is conditional on residual-jet limits and away extensions. The unresolved issue is now the exact scope of the paper/CMI semantic crosswalk, not whether the moment/rank construction is present in the selected proof chain. No zero-sorry contradiction has yet been established.

This is not a repair request. The review does not credit the paper with a CMI
solution merely because the endpoint compiles, but it also does not call the
claim false on the basis of a missing named tuple. The remaining adverse
finding must be tied to a specific unmet CMI condition, paper consequence, or
proved selected-field mismatch. “No zero-sorry contradiction yet” describes
the present falsification status.

## 1. Executive Summary

The source establishes a residual-based forced-candidate architecture, but this
supporting note does not certify the complete CMI claim. The force is defined
from supplied fields and can be smooth only after the residual-jet and
extension hypotheses are established for those same selected fields. Calling
this a “valid exploit” would overstate what the inspected interfaces prove.

The construction is a residual-driven forced-candidate architecture: the
velocity field is designed to grow, and the force is obtained from a smooth
extension of the candidate residual once the residual-limit hypotheses are
supplied. That architecture is admissible in principle for a forced CMI
alternative, but the audit has not independently established that the
selected fields satisfy every required analytic and semantic premise. It is
therefore not correct to state that the code has already verified the literal
CMI claim merely because the force is residual-defined.

The peer review has uncovered a critical specification and traceability gap
between the human-readable paper and the Lean 4 formalisation regarding
moment transport, together with a narrower pressure-semantic gap.

The pressure objection remains an active attack surface. A failed
compact-support probe is not a clearance: the decisive missing premise is the
selected global pressure-Poisson equation. The force-jet attack has now been
tested on the selected endpoint and closes in the opposite direction: the
final force inherits the flat residual at the origin.
The new zero-sorry `SelectedWitnessInhabitationProbe` also shows that the
exported witness envelope carries no five-debt payload, so the selected
five-moment transport remains unverified at the type level.

The separate CTR-019 sweep finds a real generic empty-branch behaviour but not
a selected-path vacuity. A zero-sorry review construction uses
`slowMask_sum_sq = 1` to obtain an active label at every positive band, then
chooses a band above `prepared.N` to construct
`Nonempty (ActualPrimary.Label B N0)` and `Nonempty (ActivePair B N0)`. The
diagonal `potentialSum` is independently a natural-indexed `tsum`. CTR-019 is
therefore cleared as a selected-path contradiction. The verdict remains
`NOT ESTABLISHED` for the separate CTR-005 missing field-level five-moment
transport theorem.

## 2 Blow-Up Mechanism (Audit of `PeriodicSobolev.lean`)

A deep dive into `PeriodicSobolev.lean` reveals exactly how the codebase sidesteps the LPS regularity firewalls. The authors do not accidentally trap themselves in an LPS-compliant bounded space. 

Instead, the codebase explicitly forces the velocity to infinity at the spatial origin (the z-axis). In `GermCandidateAssembly.lean`, the theorem `origin_blowup` delegates directly to `FinalSlowBase.axis_tendsto`, which formally proves that the magnitude of the velocity goes to infinity as $t \to 1$. 

Then, `PeriodicSobolev.lean` uses coordinate-wise Fundamental Theorem of Calculus (FTC) estimates to prove `speed_unbounded_implies_derivativeH3_unbounded`. This theorem rigorously establishes that the pointwise singularity at the origin forcibly drags the global $H^3$ energy norm to infinity. Thus, the singularity is mathematically sound and strictly violates global regularity bounds.

## 3. Spacetime Regularity of the Residual Force at $t=1$

The most precarious mathematical boundary in the residual-feedback construction
is whether the force remains smooth ($C^\infty$) at the exact temporal
interface $t=1$. Velocity growth alone does not imply that the residual
components $(\partial_t u + u \cdot \nabla u - \Delta u)$ blow up, because
the construction may cancel them. The selected zero-sorry composition probe
shows precisely such cancellation at the origin.

The source isolates the endpoint requirement in the `VanishingJointJets`
hypothesis and uses `SpacetimeGluing.smoothExtension`. The generic theorem
then derives `ContDiff ℝ ∞` and the zero branch from `t ≥ 2`. This is a
conditional construction: it does not, by itself, prove that the selected
fields satisfy the required residual limits or that their pressure has the
paper's global semantics.

The zero-sorry probe
`PressureRecoveryAbsolutePremiseProbe.lean` adds a separate limitation. The
comparison hypotheses accept identical zero velocities and any common smooth
pressure, so the comparison chain establishes pressure differences but does
not encode an absolute pressure-Poisson representative.

## 4. Historical provisional finding (superseded): endpoint moment glue

The earlier wording treated the absence of a named five-debt field in the
existential envelope as evidence that the construction had dropped its repair
mechanism. That inference is withdrawn. The aligned and modulated construction
proves five-row identities and finite residual identities for the same base
profile that supplies the origin growth, and the selected proof term consumes
those consequences. The generic interface probe remains valid as a statement
about the interface, but it is not a countermodel of the concrete selected
witness.

**Current verdict:** the review has not established the exact end-to-end
paper/CMI semantic crosswalk, and it has a formal conditional residual
provenance objection, but it has not proved a zero-sorry `False` theorem from
the actual selected witness. The remaining work is to test a concrete
paper-level consequence against the selected fields, pressure, residual,
force, support, and endpoint limits. Tuple omission alone is not that test.

This is not a presumption in favour of the authors. The burden of establishing
the paper's stronger construction claim remains with OpenAI. A missing
selected-field bridge and missing analytic composition theorem are affirmative
reasons not to accept that claim, even though the narrower literal endpoint
has not yet been formally refuted. See
`NavierStokesReview/evidence/burden_of_proof_underclaim_audit_2026-09-24.md`.

## 5. Pressure and mirror-force checks

The equal-and-opposite pressure proposal does not produce that contradiction.
The compiled `PressureResidualNonCancellationProbe` proves that a pressure
perturbation enters the residual as `pressureGradient q`; it is not forced to
cancel the residual-derived force. The forced divergence identity would also
retain the `div f` term unless an additional divergence-free-force hypothesis
were proved.

The compiled `MirrorForceSymmetryProbe` proves that `-f` remains smooth, but it
is a different prescribed-force problem. The same fields can satisfy both
equations only if `f = -f` pointwise. The uniqueness module compares solutions
with the same force and therefore cannot turn the mirror construction into a
refutation of the original existential claim.

The structural duality probe verifies the strongest unconditional mirror
statements: smoothness survives (f\mapsto-f), local work changes sign, and
the two forces cancel pointwise when superposed. It does not prove that the
selected velocity solves the zero-force equation, because nonlinear advection
and the selected schedule are not linear in the force. The remaining formal
target is therefore a selected-path perturbation or a force-independent
admissibility premise, not the mirror identity itself.

## Selected-closure correction

The five-moment implementation is present in the selected transitive closure.
The closure rooted at `ActualCandidateAssembly.lean` reaches 507 local modules,
including `PositiveOrderMoments`, `FiveProfileMoments`, `FiveRowRank`, and
`CorrectionState.debt`. The surviving defect is that `Witness` does not expose
the theorem identifying those upstream quantities with the final mixed fields,
residual, and force. This is a selected-endpoint correspondence failure, not
a claim that the repository contains no five-moment construction.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Internal-cycle qualification

The production recurrence does contain a proved two-moment invariant:
`ActualCyclePreservation.Invariant` includes `masses`, and the selected-cycle
completion exposes its `ZeroMassesOn` consequence. Thus the counter-paper does
not rely on the claim that the correction cycle ignores every mass constraint.
The unresolved defect is the missing theorem carrying these internal radial
identities into the exported mixed `Witness` and identifying them with the
paper's complete five-moment system. Evidence:
`NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.

## Whole-space uniqueness qualification

The whole-space no-global-solution argument has been audited through its
actual source path. `classical_uniqueness_on_Icc` derives the comparison from
the two residual equations, incompressibility, smoothness, finite-energy
bounds, compact reference support, and compact-test pressure recovery.
`candidate_global_agrees_before_one` and `no_global_solution_one` then apply
that result to the selected candidate.

Accordingly, the review withdraws any suggestion that the R³ endpoint is only
an existential candidate shell or that compact pressure support alone forces a
trivial pressure. The pressure chain still leaves absolute selected-pressure
semantics unexposed, so CTR-005 remains live. The uniqueness audit itself
does not yield a selected-witness `False`.

Evidence: `NavierStokesReview/evidence/whole_space_uniqueness_audit_2026-09-24.md`.

## Burden-of-proof correction: 2026-09-24

The final classification must not understate the review's adverse result. The
exported endpoint is materially populated and formally C/D-shaped. The
unresolved defect concerns the stronger public claim that the selected endpoint
is the five-moment construction described in the paper. The repository defines
the relevant moment systems, but no selected-path theorem located in
`Witness` identifies `(M,I,J,S,C_p)` with the final mixed fields and residual.

Accordingly, the authors have not discharged the burden for the stronger
published solution description. This is a substantive “not established”
finding, not a request that the reviewer prove a universal negation. A literal
Lean `False` remains a separate threshold and has not been claimed here.

Evidence: `NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md`.

## Source-trace correction

The five-moment construction is active upstream rather than absent. The exact
rows are defined in `PositiveOrderMoments.lean:76-85`, cancelled for the slow
profile sequence in `GlobalSlowProfiles.lean:1043-1055`, and consumed by the
assembled slow base in `AssembledSlowBase.lean:592-617`. The unresolved issue
is the selected mixed-field transport at `ActualCandidateAssembly.lean:515-523`
and the exported `Witness` contract at `1121-1151`: no field-level equality is
stated there for the paper tuple
$$
(M,I,J,S,C_p).
$$
The affirmative solution claim therefore remains **NOT ESTABLISHED**. This
does not assert that the upstream five-row identities are false.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.

## Whole-space claim-level correction

The source also contains a distinct R³ endpoint. `NavierStokes/R3/Theorem.lean`
exports `NavierStokesR3.theorem_1_1`, whose proposition directly includes the
compact positive-time force, smooth pre-singular fields, incompressibility,
bounded kinetic energy, speed blow-up, and nonexistence of a global smooth
finite-energy competitor. The present CTR-005 verdict must therefore be read
as a failure to establish the paper's five-moment mechanism at the selected
field boundary, not as a completed contradiction of the literal C/D endpoint.

Evidence: `NavierStokesReview/evidence/cmi_target_and_claim_level_reconciliation_2026-09-25.md`.

## Release-integrity qualification

The fork also records a concrete repository-wide defect: `ComparatorChallenges`
is a default Lake target, and Lean's `#print axioms` reports `sorryAx` for its
two Navier–Stokes and two Euler challenge declarations. This defeats an
unqualified zero-sorry release description. The evidence does not place those
declarations on the selected R³ solution path, so the selected endpoint and
the repository-wide admission census remain separate findings.

Evidence: `NavierStokesReview/evidence/repository_admission_axiom_log_2026-09-25.md`.

## Selected production cutoff calculation: 2026-09-25

`SelectedProductionDirectPrefixCutoff.lean` proves that the exported direct
branch is cutoff-weighted and records the exact finite-prefix shell defect

$$
\sum_{j\leq J}(\chi u_j)_1-\sum_{j\leq J}(u_j)_1
=(\chi-1)\sum_{j\leq J}(u_j)_1.
$$

This strengthens CTR-005 to a concrete selected calculation target. The
weighted radial integral and a selected nonzero value remain unproved. The
controlled verdict is still **NOT ESTABLISHED**, with no kernel `False` claim.

Evidence: `NavierStokesReview/evidence/selected_production_direct_prefix_cutoff_2026-09-25.md`.

## Selected scalar moment update: 2026-09-25

The selected-cycle completion now proves the two local scalar identities in the
same `barMoment` notation used by the correction system. For every selected
stage, the angular second moment and axial first moment of the cycle mean state
vanish on the carrier. This removes any claim that the active recurrence loses
those moments merely through iteration.

The remaining adverse finding is at the exported field boundary: the selected
direct prefix is a Cartesian velocity formed from an atlas coefficient, angular
frame, localisation, and curl. The source still does not prove that this
Cartesian field has the paper's radial profile moments after all cutoffs and
boundary terms. The paper claim remains **NOT ESTABLISHED**, but no selected
`Delta m ≠ 0` or kernel `False` is asserted.

Evidence: `NavierStokesReview/evidence/selected_scalar_barMoment_transport_2026-09-25.md`.

The current source correction is that the exported mixed velocity is not one
combined curl. It is a curl-generated potential branch plus a direct angular
branch. The selected Cartesian-to-radial moment calculation is therefore open
for both branches. The paper claim remains **NOT ESTABLISHED**, while no
selected `False` theorem is claimed.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.

## Positive-radius component transport: 2026-09-25

The selected-chart completion now proves the exact first Cartesian component
of the polar-frame velocity and transports it through the source
`velocity_polar_forward` theorem. This is a local coordinate result. It does
not identify the final mixed field with the scalar `barMoment` input and does
not supply a selected nonzero remainder. The verdict therefore remains
**NOT ESTABLISHED**, with no selected kernel `False` claimed.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

## Selected direct component transport: 2026-09-25

The selected direct branch is now source-resolved one step further. Its first
Cartesian component contains the polar rotation, graph scale, and
`swapCylinder` reindexing before any scalar radial comparison. This strengthens
the correspondence objection but is not a selected nonzero moment or a kernel
contradiction. The verdict remains **NOT ESTABLISHED**.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

The direct branch now has a source-backed zero radial moment after its
Cartesian component is identified with the native scalar.  This removes that
branch as the current source of a selected nonzero remainder; the mixed
potential/curl field remains unresolved.  The verdict remains
**NOT ESTABLISHED**, not formally refuted.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

The current verdict is sharpened by the rank/stream trace. The rank identity
is genuinely used in `rankPotential`, and the selected stream is assembled
from temporal and rank families before curl. The remaining failure of
establishment is the missing selected transport from that curled mixed field
to the scalar torus-average input of `barMoment`. The verdict remains
**NOT ESTABLISHED**, pending either that equality or a proved contradictory
selected remainder.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

The current selected-field evidence now includes a compiled component-level
cutoff identity. It strengthens the burden on the claimed five-moment bridge,
but does not by itself establish a contradictory value.

## Selected production direct branch

The selected production field is not definitionally the native direct scalar
used by the zero-moment theorem. On the unit cube the source identity is

$$
u_{\mathrm{prod}}=u_{\mathrm{periodic}}+\chi v,
$$

with periodisation applied to the cutoff branch. The review therefore requires
a cutoff-weighted radial calculation. This strengthens CTR-005 from a generic
bridge request to a concrete selected-field obligation, but no nonzero
remainder or kernel contradiction has yet been established.

Evidence: `NavierStokesReview/evidence/selected_production_direct_cutoff_2026-09-25.md`.

The atlas selector has also been checked directly. The zero-sorry completion
`SelectedAtlasPhysicalErasure.lean` proves that the selected physical value
depends only on valid chart samples. This strengthens the transport objection
because the native `barMoment` integral ranges over the full scalar-family
domain. It remains an unresolved selected bridge, not a proof of a nonzero
remainder or `False`.

## Selected production potential boundary

The latest zero-sorry completion proves a concrete exported-field identity:

$$
V_{\mathrm{prod}}=\chi\,\operatorname{curl}(A)
 +\operatorname{curlLinear}(D\chi\,A).
$$

The cutoff/curl commutator is therefore a real selected transport obligation.
It is not yet a contradiction: no selected radial integral or nonzero sign has
been proved. The verdict remains **NOT ESTABLISHED**, with the live target
being transport of this term through the atlas, torus average, `barMoment`,
and the final `tsum`.

Evidence: `NavierStokesReview/evidence/selected_potential_production_product_rule_2026-09-25.md`.

The subsequent completion `SelectedPotentialProductionRadialScalar.lean`
derives the first component of this localised field on the actual
positive-radial section, using the selected schedule for differentiability.
This is selected transport evidence, not a nonzero moment or contradiction.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

The finite-prefix scalar now has an exact torus-average reduction and an
exact weighted radial-integral form. This is a genuine local completion of
the selected calculation, but it supplies neither a value nor a sign and it
does not identify the scalar with the complete selected Cartesian `tsum`.
The controlled verdict remains **NOT ESTABLISHED** rather than `False`.

Evidence: `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md`.

## Finite-prefix endpoint qualification: 2026-09-26

The review completion `SelectedFiniteCutoffEndpoint.lean` proves that each
fixed finite stage prefix has a cutoff plateau at the axis as the similarity
scale tends to zero. The result does not commute the endpoint limit with the
infinite selected sum and does not change the controlled verdict:
**NOT ESTABLISHED**, not `False`.

Evidence: `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md`.

## Mixed endpoint qualification: 2026-09-26

The review-side completion gives the selected mixed component a well-typed
`barMoment` representation and proves its positive-radius physical pullback.
It does not determine the weighted integral, prove `Δm ≠ 0`, or change the
controlled verdict: **NOT ESTABLISHED**, not a kernel-level `False` result.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

The new reduction exposes the actual mixed weighted radial integral but does
not evaluate it. The verdict remains **NOT ESTABLISHED**, not `False`.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The new periodicity result is conditional evidence about the radial observable,
not an unconditional `False`: bounded support is not a selected-witness
premise, and nonvanishing has not been proved.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

## Source-path reconciliation: 2026-09-26

The active source tree contains no `SelectedCandidate.lean` module. The
selected witness and candidate are defined at
`NavierStokes/ActualCandidateAssembly.lean:1177-1184`; the whole-space wrapper
is at `NavierStokes/R3/ActualCandidate.lean:127-151`; and the exported theorem
and dissipation theorem are at `NavierStokes/R3/Theorem.lean:26-80`. The
finite-energy lemma is present at `NavierStokes/R3/CompactEnergy.lean:343`.
This corrects a source-name error without changing the substantive verdict.

The periodic mixed field used in the review calculation is an intermediate
object. `R3CompactCandidate` then cuts it to a compact whole-space field and
uses local agreement on the inner cube. A theorem transporting the global
periodic radial `barMoment` of the intermediate field to the final compact
R³ candidate has not been identified. This is a load-bearing correspondence
obligation, not a kernel contradiction.

Evidence: `NavierStokesReview/evidence/source_path_reconciliation_2026-09-26.md`;
`NavierStokesReview/evidence/periodic_global_integral_semantics_2026-09-26.md`.

The support calculation is likewise a transport boundary, not a contradiction.
The compact support theorem applies before lattice periodisation, while the
selected mixed field is unit-periodic and the source `barMoment` integrates over
the full real radial coordinate. A selected-path support or integrability
theorem is still required before the conditional periodic obstruction can be
used against the exported witness.

## Mapping control update

The current route ledger confirms that the named upstream moment and radial
modules are reachable from the exported endpoint. The review therefore makes
no dead-code or missing-file claim. The unresolved issue is the selected-value
transport theorem: reachability does not establish equality between the final
assembled Cartesian witness and the paper's five named moments.
