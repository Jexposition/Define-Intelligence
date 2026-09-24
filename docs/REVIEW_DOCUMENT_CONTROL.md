# Navier–Stokes review document control

**Status:** active source-of-truth map  
**Updated:** 2026-09-24
**Review root:** `Define-Intelligence-github`

## Authority

The active review corpus is the fork at:

`D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github`

Its `docs/` directory is authoritative for current findings because its claims
are tied to the current fork, zero-sorry probes, evidence files, and exact source
paths. The sibling directory
`D:\Research Lab\Jexposition\Define Intelligence\docs` is a parent/staging
archive. It is not the active verdict surface and must not silently overwrite
the fork's documents.

## Active documents

| Document | Role | Rule |
|---|---|---|
| `OpenAI_NavierStokes_CMI_First_Review_Plan.md` | Executable review plan | Keep tasks, statuses, and decisive tests compact. |
| `OpenAI_NavierStokes_Audit_Tracker.md` | Evidence ledger | Record findings only with source/probe references. |
| `OpenAI_NavierStokes_Axiom_Ledger.md` | Axiom and admission inventory | Distinguish kernel axioms, hypotheses, `sorry`, and unverified interfaces. |
| `OpenAI_NavierStokes_Input_Document_Synthesis.md` | Controlled synthesis of supplied critiques | Preserve useful hypotheses, but label withdrawn or unsupported claims. |
| `OpenAI_NavierStokes_Peer_Review_v1.md` | Human-readable peer review | Report conclusions, limits, and required bridge theorems. |
| `OpenAI_NavierStokes_Research_Paper.md` | Human-readable research paper | Explain the argument; do not turn it into a chronological log. |
| `REVIEW_DOCUMENT_CONTROL.md` | This map | Prevent duplicate docs from becoming competing verdicts. |

`dependency_closure_validation.md` and the supporting diagnostic notes are
supporting material. They are not independent verdicts.

## Alignment check: 2026-09-24

The tracker names **CTR-005**, the missing selected-path transport of the
paper's `(M, I, J, S, C_p)` data and force, as the headline load-bearing
objection. The pure-axial/pure-swirl collapse hypothesis is explicitly marked
as a cleared and rejected attack surface in the tracker and in the supporting
solenoidal ledger. The pressure-trivialisation route remains open: compact
support alone is not the contradiction, and the missing global Poisson/Leray
premise must be formalised for the selected fields. The comparison-interface
probe leaves a live objection because the recovery chain is comparative and
does not, by its type, establish an absolute global Poisson representative for
the selected pressure.

The six core documents above are synchronised to that authority map. The
pressure result is sourced to
`NavierStokesReview/evidence/pressure_uniqueness_closure_audit_2026-09-24.md`
and
`NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean`;
the argument is in the peer review and research paper, while the plan and
tracker retain only compact status entries.

The 2026-09-24 authority map also includes
`NavierStokesReview/evidence/state_realization_axis_scope_audit_2026-09-24.md`.
That evidence proves a scope limitation: `StateRealization.chartIdentity` is
an off-axis, positive-radius identity and does not itself reach the origin
used by `origin_blowup`. `GlobalBaseError.actual_error_vanishingJointJets`
provides a separate origin error-limit route. The two routes have not been
proved contradictory.

## Supporting documents: disposition

| Document | Disposition | What survives |
|---|---|---|
| `germ_geometry_extraction.md` | Corrected supporting note | `GermCandidateAssembly` has no direct moment imports, but its active upstream chain reaches five-moment machinery. The valid issue is the missing explicit semantic transport theorem. |
| `base_profile_diagnostic.md` | Corrected supporting note | `finalPotential` uses a reduced axisymmetric profile but `AxisymmetricFields.potential` has three Cartesian components. A radial gauge anchor is not a global one-component claim. |
| `deep_semantics_audit.md` | Corrected supporting note | `force_smooth` is conditional on residual-jet limits and away-extension premises; it is not an unconditional smoothness axiom. |
| `cmi_review_verdict_.md` | Superseded provisional verdict | Retain its research questions only. Correct the zero-force boundary to `t ≥ 2` and do not call the C/D construction invalid merely because forcing is active. |
| `axisymmetric_rank_interface.md` | Lead only; overclaims quarantined | The missing selected-path bridge remains a valid target. Claims that the final field is globally pure axial, linear, or physically two-dimensional are not source-established. |
| `solenoidal_assembly_collapse.md` | Rejected as evidence | Its pure-axial premise conflicts with the source definition and the zero-sorry base-profile probe. Do not cite it as a disproof. |
| `dependency_closure_validation.md` | Corrected supporting note | The selected theorem passes through a generic existential witness, but that interface is not evidence of a hollow proof. Import separation supports a missing semantic bridge claim only. |
| `core_realization_bridge_audit.md` | Corrected supporting note | Native residual bounds are upstream of the selected witness. Lack of direct `FiveRowRank` imports supports a correspondence question, not a fake-field or lower-dimensionality theorem. |
| `implementation_plan.md` | Stale scaffold | Use the active CMI-first plan instead; retain this file only for historical context. |
| `Define intelligence Tree.md` | Generated inventory | Useful for navigation, not an argument or verdict. |

## Parent-directory documents

The parent copies are retained as archival/staging material. In particular,
`cmi_review_verdict_v1.md` contains useful early objections but also stale or
overstrong statements, including a zero-force cutoff at `t ≥ 1` and a stronger
conclusion than the current source audit supports. The parent `implementation_plan.md`
is likewise superseded. The parent directory has no current equivalent of
`OpenAI_NavierStokes_Input_Document_Synthesis.md`.

If a parent note contains a new claim, it must be rechecked against the fork
before entering an active document. Do not merge by filename alone.

## Current conclusion boundary

The review has established a serious, source-backed correspondence objection:
the selected endpoint contains five-moment machinery upstream, while the
generic germ/stage interface does not expose a theorem transporting the
paper's named moments into the selected velocity, pressure, residual, and
force endpoint. This is a missing load-bearing bridge, not yet a formal
contradiction.

The following claims are currently **not established** as disproofs:

- that the selected final velocity is non-solenoidal;
- that compact pressure support alone forces pressure or velocity to vanish;
- that the comparative pressure-recovery chain proves an absolute global
  Poisson representative for the selected pressure;
- that the selected endpoint exploits `Filter.bot` vacuity;
- that the force is nonsmooth merely because it is residual-defined;
- that the whole `WholeDomain*` branch is dead code globally;
- that a dimension count alone disproves the five-moment construction;
- that the off-axis `chartIdentity` limitation alone refutes the selected
  origin residual estimate;
- that the explicit three-to-five promotion is the selected endpoint's
  physical moment identity.

The pure-axial and zero-helicity collapse hypothesis is explicitly cleared as
an attack surface: `AxisymmetricFields.potential` has three Cartesian
components and the selected final velocity is curl-generated. The supporting
solenoidal-collapse note is retained only as a rejected hypothesis.

Any future “refuted” or “definitive failure” label requires a source-backed
counterexample or a zero-sorry Lean theorem closing the relevant contradiction.

The selected-witness attack is not cleared by a weak interface test. The new
`SelectedWitnessInhabitationProbe` proves that the exported `Witness` type can
coexist with an arbitrary nonzero five-debt payload because the type contains
no field-level debt equality. This keeps the five-moment falsification lane
active; it does not yet prove that the actual selected fields violate the
moments.

## Evidence entry rule

Every active claim must point to at least one of:

1. an exact source path and line range;
2. a zero-sorry probe and its recorded result; or
3. a primary external specification, clearly separated from repository facts.

Compilation is evidence that Lean accepted a term. It is not, by itself,
evidence that the term has the intended Navier–Stokes semantics.

The new zero-sorry theorem
`StageEstimatesMomentBlindnessProbe.interface_does_not_determine_five_debt`
is controlled as an interface result. It confirms that the generic stage-rate
record cannot determine the paper's five-coordinate debt, but it does not by
itself refute the selected witness. The selected-path transport theorem and
the residual/origin contradiction remain open.

## Final authority-map verification: 2026-09-24

- [x] `CTR-005` remains the headline, load-bearing finding in the tracker:
  the selected endpoint still lacks an explicit theorem transporting the
  paper's named five moments into the selected field, residual, pressure, and
  force chain.
- [x] The pure-axial and zero-helicity hypotheses are cleared as attack
  surfaces. Compact-support trivialisation is rejected only in its narrow
  form; absolute pressure semantics remain active under CTR-039.
- [x] The six core documents are present under this `docs/` authority map:
  plan, tracker, axiom ledger, input synthesis, peer review, and research
  paper. Each points back to this control file.
- [x] `solenoidal_assembly_collapse.md`,
  `dependency_closure_validation.md`, and
  `core_realization_bridge_audit.md` are supporting notes only and use the
  corrected, narrower conclusion.
- [x] The transitive-import recheck corrected stale wording in the supporting
  notes: `ActualCandidateAssembly` reaches `FiveProfileMoments` and
  `FiveRowRank` through `InitialPhysicalData` and `MeanRankUpdate`, and reaches
  `PositiveOrderMoments` through the physical-prefix/profile chain. The open
  issue is semantic transport into the residual endpoint, not dead code or
  total import separation.
- [~] The branch has no tracked `.olean` or `.lake` files. The current working
  tree is intentionally dirty while the 2026-09-24 attack ledger and probes
  are being packaged; final clean-status validation remains pending.

## Five-row collision boundary: 2026-09-24

- [x] The proposed compact-perturbation collision was tested in
  `FiveRowCollisionBoundaryProbe.lean` with no `sorry`, `axiom`, or `unsafe`.
- [x] The probe confirms that `FiveRowRank.five_rows` admits nonzero
  three-coordinate debt and that `Witness` carries no debt or perturbation
  field. The requested `False` therefore does not follow by type collision.

## Correction-row transport closure: 2026-09-24

- [x] The generic `FiveRows` consequence and rank-stage preservation are
  compiled in `CorrectionInvariantScope.lean` without `sorry`, `axiom`, or
  `unsafe`.
- [x] The exact invariant is recorded as two radial correction moments.
- [x] The conditional nonzero-moment contradiction is recorded.
- [ ] The selected endpoint still lacks the theorem transporting a compact
  Cartesian perturbation into `rankIncrement` with a nonzero corresponding
  moment.
- [ ] No kinetic-energy conclusion is authorised from the zero rows.

Evidence authority:
`NavierStokesReview/evidence/correction_moment_transport_audit_2026-09-24.md`.
- [x] The first two rows are controlled as correction-state radial moment
  invariants, not as a selected Cartesian energy identity. The headline issue
  remains CTR-005: transport of the paper's five moments into the selected
  endpoint is not exhibited.

Evidence: `NavierStokesReview/evidence/five_row_collision_boundary_2026-09-24.md`.

## Conditional correction-moment obstruction: 2026-09-24

- [x] `CorrectionInvariantScope.lean` compiles with no `sorry`, `axiom`, or
  `unsafe`.
- [x] It proves that `FiveRows` forces the two correction moments to zero and
  derives `False` from either corresponding nonzero increment hypothesis.
- [ ] The selected-path transport of an independent Cartesian perturbation into
  the constrained correction increment is still missing. Keep this under
  CTR-005; do not relabel the conditional theorem as an endpoint refutation.

Evidence: `NavierStokesReview/evidence/correction_invariant_scope_2026-09-24.md`.

## Selected-cycle invariant refinement: 2026-09-24

- [x] `ActualCyclePreservation.Invariant` is confirmed to contain a
  `masses` field, and `state_invariant` propagates `ZeroMassesOn` through every
  actual cycle stage.
- [x] `SelectedCycleMomentTransport.lean` exposes that invariant for the
  selected cycle and derives `False` from a nonzero corresponding moment.
- [ ] The internal two-moment invariant is still not identified with the
  published five-moment tuple or exposed as an equality for the mixed
  `Witness` endpoint.

The active counter-paper claim is therefore narrower than “the cycle has no
mass constraints”: the cycle has two local radial constraints, while the
paper-to-endpoint five-moment transport remains unproved.

Evidence: `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.

## Research-paper and attack-boundary update: 2026-09-24

- [x] `OpenAI_NavierStokes_Research_Paper.md` has been rewritten as a coherent
  paper with a single verdict, rather than a chronological audit log.
- [x] `SelectedWitnessAttackBoundaryProbe.lean` compiles without `sorry`.
  It proves the witness envelope does not entail a five-debt certificate and
  records the scalar compatibility of blow-up with a flat residual.
- [x] The force-jet route is closed as a force-explosion argument. The selected
  force tends to zero at the origin despite selected speed blow-up; no residual
  explosion is inferred from velocity growth.
- [x] The pressure route remains a missing global Poisson/Leray transport
  objection. Compact support alone is not recorded as a contradiction.
- [~] A selected-path zero-sorry `False` theorem has still not been obtained.

## Selected force-origin composition: 2026-09-24

- [x] `SelectedForceOriginCompositionProbe.lean` compiles without admitted
  declarations and extracts the actual selected witness.
- [x] The probe identifies the final force with the periodic and original
  residuals at the origin for late times, then proves

  $$
  \lVert f(t,0)\rVert\to0\quad(t\to1^-).
  $$

- [x] The force-explosion objection is closed. The selected speed still tends
  to infinity, so the source exhibits cancellation rather than a lower-bound
  contradiction.
- [~] CTR-005 remains the headline issue: the five-moment and absolute
  pressure semantics are not exposed as transport premises of the selected
  residual/force theorem.

Evidence: `NavierStokesReview/evidence/selected_force_origin_composition_2026-09-24.md`.

## Vanishing-jets and localisation trace: 2026-09-24

- [x] `JointResidualLimits.VanishingJointJets` is an all-orders definition:
  `∀ n : ℕ, Tendsto (iteratedFDeriv ℝ n f) ... (𝓝 0)`, not an `H^3`
  truncation.
- [x] The selected source derives the premise through
  `ActualCycleResidualBounds.Invariant.residual_jetRate`,
  `finite_residual_rates`, `ActualStageEstimates.stageEstimates_of_representations`,
  `StageEstimates.exists_schedule`, and
  `MixedDiagonalResidual.exists_physical_schedule_residual_zero`.
- [x] `timeSwitch` is globally `ContDiff`, equals one on the late side of
  `t = 3/4`, and has zero positive-order derivatives there. The late activation
  lemmas prove neighbourhood equality, not only pointwise equality.
- [x] `MixedPeriodicAssembly` transports the complete residual operator through
  neighbourhood equalities. No Cartesian component projection or advection
  cross-term deletion was found.
- [~] The localisation files take no `FiveRowRank.Debt`,
  `PositiveOrderMoments.Debt`, or named paper moments. They are therefore
  debt-blind field identities and do not supply the missing selected moment
  transport theorem.

Evidence: `NavierStokesReview/evidence/vanishing_joint_jets_and_localisation_trace_2026-09-24.md`.

## Upstream moment-chain correction

The five-moment repair identities are live in the upstream aligned and
modulated construction. `SelectedBaseMomentCompatibilityProbe.lean` verifies
the moment identity, finite residual identity, and base blow-up without
`sorry`. The controlled objection is therefore narrower: the selected mixed
endpoint still lacks an exhibited theorem transporting those identities into
the actual residual, pressure, force, and `VanishingJointJets` data. This
correction supersedes any wording that calls the entire five-moment branch dead
or disconnected.

## Selected-witness attack control: 2026-09-24

The force lane now has a selected-path cancellation result: the selected
origin speed tends to infinity while the selected raw mixed residual tends to
zero. Therefore a fixed positive velocity-to-residual lower bound is
impossible for that raw residual. The pressure attack is limited to the
missing selected global Poisson/Leray transport; compact support alone is not
recorded as a contradiction. The moment-blindness probe is an interface
countermodel only. These findings sharpen CTR-005 but do not yet prove `False`
for the final C/D endpoint.

Evidence: `NavierStokesReview/evidence/selected_witness_boundary_attack_status_2026-09-24.md`.

## Endpoint residual control: 2026-09-24

`SelectedWitnessEndpointResidualProbe.lean` is now the active force-attack
artifact. It extracts the selected schedule, proves origin speed blow-up, and
proves that the selected raw mixed residual tends to zero. It also contains
the conditional contradiction obtained if a positive velocity-to-residual
lower bound is imposed. CTR-005 remains the headline correspondence finding;
`SelectedForceOriginCompositionProbe.lean` now proves that the raw residual is
explicitly composed with the final force at the origin and that the final force
tends to zero there. The force-explosion route is closed.

Evidence: `NavierStokesReview/evidence/selected_witness_endpoint_residual_probe_2026-09-24.md` and
`NavierStokesReview/evidence/selected_force_origin_composition_2026-09-24.md`.

## Independent-data and mirror checks: 2026-09-24

- [x] `IndependentDataPerturbationProbe.lean` derives the fixed-force
  perturbation defect.
- [x] The same probe supplies a globally smooth, spatially divergence-free
  affine-time field with an explicitly nonzero defect for every nonzero
  amplitude.
- [x] `FixedForcePerturbationCompletion.lean` packages the result for the
  positive-time force wrapper.
- [x] `StructuralDualityMirrorProbe.lean` proves mirror smoothness, local work
  sign reversal, and pointwise force cancellation.
- [~] Neither probe proves that `exists_schedule` fails after an arbitrary
  perturbation or after replacing the force by its negative. Those would
  require an admissible selected-path perturbation theorem and a theorem
  relating the new force to the original solution.

These results strengthen CTR-012 as a causality and correspondence objection.
They do not replace the selected-witness standard for a formal `False` result.

Evidence: `NavierStokesReview/evidence/independent_data_perturbation_2026-09-24.md`;
`NavierStokesReview/evidence/mirror_force_symmetry_2026-09-24.md`.

## Compact fixed-force theorem: 2026-09-24

- [x] `CompactFixedForcePerturbation.lean` constructs a smooth compactly
  supported spatial curl perturbation.
- [x] The perturbation is divergence-free on every time slice.
- [x] Its switch-time residual defect at the origin is the nonzero coordinate
  vector `coordinateVector 0`.
- [x] `compactPerturbation_breaks_any_fixed_force_at_origin` compiles without
  `sorry`, `axiom`, or `unsafe` and rejects simultaneous satisfaction of the
  same fixed-force equation by the base and perturbed fields.
- [~] This remains an operator-level causality result. It is not a direct
  contradiction of the existential C/D endpoint until an independence or
  stability premise is shown to be part of that endpoint.

Evidence: `NavierStokesReview/evidence/compact_fixed_force_perturbation_2026-09-24.md`.

## Source-line verification record: 2026-09-24

`IndependentDataPerturbationProbe.lean` was recompiled at exit code 0. The
current source coordinates are:

| Lines | Verified item |
|---:|---|
| 26--34 | smooth affine-time field and zero spatial divergence |
| 36--66 | exact fixed-force perturbation identity |
| 68--84 | nonzero-defect impossibility theorem |
| 86--109 | affine defect calculation; derivative proof at 96--99 |
| 111--150 | fixed-force failure theorem; corrected derivative proof at 122--127 |

The earlier shorthand references to lines 25, 30, 85, 96, and 121 are retained
only as historical pointers. The table above is the authoritative coordinate
record for the current source snapshot.

The compact localised theorem is in
`CompactFixedForcePerturbation.lean`: smoothness and compact support are at
lines 23--37 and 77--105, divergence freedom at lines 107--121, and the final
same-force obstruction at lines 185--226.

## Release verification: 2026-09-24

The review branch is `review/cmi-first-navier-stokes-2026-09-22` at commit
`d2e6be7` (`Add compact fixed-force obstruction audit`). Its parent
`967da70` (`Add explicit fixed-force perturbation obstruction`) is retained in
the branch history. The current source, not the historical shorthand, is the
authority for line coordinates.

| Check | Result |
|---|---|
| `IndependentDataPerturbationProbe.lean` compiled with Lean 4.34.0-rc2 | PASS, exit code 0 |
| `sorry`, `axiom`, and `unsafe` scan for the review modules | PASS, no matches |
| tracked `.olean`, `.ilean`, and `.lake` artefacts | PASS, none tracked |
| `git diff --check` | PASS |
| branch compared with origin | PASS, clean and synchronised at `d2e6be7` |

The current probe coordinates are 26--34 for smoothness and divergence
freedom, 36--66 for the fixed-force identity, 68--84 for the general
nonzero-defect obstruction, 86--109 for the affine defect computation, and
111--151 for the concrete fixed-force failure. Lines 25, 30, 85, 96, and 121
are retained as historical navigation points from the parent commit; they are
not substituted for the current theorem ranges.

This release record does not promote CTR-012 to a literal C/D refutation. It
records exactly what is proved: the selected residual construction is
path-dependent under a fixed-force perturbation. A further theorem connecting
that admissible perturbation or independence requirement to the published C/D
endpoint is still required for a kernel-level `False` result.

## Temporal-patching control: 2026-09-24

- [x] `GermCandidateAssembly.initializedSeries` is recorded as an indexed
  selector, not as a temporal piecewise glue.
- [x] `TimeLocalization` smoothness and late derivative agreement are recorded
  from the actual source theorems.
- [ ] A selected-field temporal discontinuity has not been proved. Do not turn
  the absence of an adjacent-stage matching premise into an endpoint failure.
- [x] The raw interface test is recorded: a concrete zero-sorry family has
  unequal entries at indices zero and one, but the source provides no theorem
  identifying those indices with temporal intervals.
- [x] The Euler paper's parent-child time construction is kept separate from
  the Navier--Stokes Lean stage indexing.
- [x] External CMI/OpenAI wording is tracked in
  `docs/OpenAI_NavierStokes_Source_Context_Register.md`.

Evidence: `NavierStokesReview/evidence/temporal_patching_audit_2026-09-24.md`.
