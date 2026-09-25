# Superseded provisional verdict: OpenAI Navier-Stokes formalisation

This file is retained as supporting material. The active verdict is in
`OpenAI_NavierStokes_Peer_Review_v1.md`, and the active evidence ledger is in
`OpenAI_NavierStokes_Audit_Tracker.md`. Claims below are subordinate to those
documents and to `REVIEW_DOCUMENT_CONTROL.md`.

## Direct verdict on the published solution claim

OpenAI's paper claims a solution of the Navier–Stokes problem. That claim is
**not accepted on the inspected record**. The source contains a substantial
R³ C/D-shaped theorem, but the exported endpoint does not expose the
selected-field transport theorem identifying it with the five-moment
construction used in the paper's proof narrative. This is a failure of the
affirmative solution record, not an optional implementation criticism. The
absence of a kernel-level `False` is recorded only as a narrower status of the
current contradiction search.

## Verification correction: selected endpoint and temporal boundary

The source-backed audit confirms that the force is a residual-based construction, but the public CMI alternatives permit smooth forcing, so that fact alone is not a disqualification. The exact source boundary must be quoted: `CandidateFromLimits.force_zero_from` establishes the zero-force branch from `t ≥ 2`, while the activated residual branch is used for `t < 1`. The claim that the force is glued to zero from `t ≥ 1` is therefore incorrect.

Likewise, `finalPotential_smooth` is derived from smooth coefficient data, and `force_smooth` is conditional on residual-jet limits and away extensions. The unresolved issue is whether the selected endpoint proves the paper's five-moment transport and all those analytic premises for the same fields. No zero-sorry contradiction has yet been established.

This does not shift the proof burden to the review. The published claim remains
unestablished until the authors exhibit the selected-path correspondence and
discharge its analytic premises. “No zero-sorry contradiction yet” describes
only the narrower status of the current falsification attempt.

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

## 4. Critical Defect: Missing Moment Transport Glue

The five-moment machinery is live upstream: the aligned and modulated
construction proves five-row identities and finite residual identities for the
same base profile that supplies the origin growth. The surviving defect is
narrower and more serious than a dead-code allegation. The selected witness
endpoint consumes generic stage-rate records and local physical-field germs;
those interfaces do not expose an equality transporting the named moments to
the final mixed velocity, pressure, residual, and force. The zero-sorry
interface probe proves that the witness envelope itself carries no such
five-debt payload.

**Verdict:** the review has a source-backed selected-endpoint correspondence
failure and a formal conditional residual obstruction, but not yet a
zero-sorry `False` theorem from the actual selected witness. The CMI claim is
therefore **not established** by this audit; the remaining work is to derive a
concrete selected-field moment, pressure, or residual contradiction.

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
