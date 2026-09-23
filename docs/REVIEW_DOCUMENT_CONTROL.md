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

`dependency_closure_validation.md` and the Agent 2 diagnostic notes are
supporting material. They are not independent verdicts.

## Alignment check: 2026-09-24

The tracker names **CTR-005**, the missing selected-path transport of the
paper's `(M, I, J, S, C_p)` data and force, as the headline load-bearing
objection. The pure-axial/pure-swirl collapse hypothesis is explicitly marked
as a cleared and rejected attack surface in the tracker and in the supporting
solenoidal ledger. The pressure-trivialisation route is rejected only in its
narrow form: compact support alone does not imply a zero pressure slice. The
comparison-interface probe leaves a separate live objection because the
recovery chain is comparative and does not, by its type, establish an
absolute global Poisson representative for the selected pressure.

The six core documents above are synchronised to that authority map. The
pressure result is sourced to
`NavierStokesReview/evidence/pressure_uniqueness_closure_audit_2026-09-24.md`
and
`NavierStokesReview/src/probes/PressureRecoveryAbsolutePremiseProbe.lean`;
the argument is in the peer review and research paper, while the plan and
tracker retain only compact status entries.

## Agent 2 documents: disposition

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
- that a dimension count alone disproves the five-moment construction.

The pure-axial and zero-helicity collapse hypothesis is explicitly cleared as
an attack surface: `AxisymmetricFields.potential` has three Cartesian
components and the selected final velocity is curl-generated. The Agent 2
solenoidal-collapse note is retained only as a rejected hypothesis.

Any future “refuted” or “definitive failure” label requires a source-backed
counterexample or a zero-sorry Lean theorem closing the relevant contradiction.

## Evidence entry rule

Every active claim must point to at least one of:

1. an exact source path and line range;
2. a zero-sorry probe and its recorded result; or
3. a primary external specification, clearly separated from repository facts.

Compilation is evidence that Lean accepted a term. It is not, by itself,
evidence that the term has the intended Navier–Stokes semantics.

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
- [x] Agent 2's `solenoidal_assembly_collapse.md`,
  `dependency_closure_validation.md`, and
  `core_realization_bridge_audit.md` are supporting notes only and use the
  corrected, narrower conclusion.
- [x] The transitive-import recheck corrected stale wording in the supporting
  notes: `ActualCandidateAssembly` reaches `FiveProfileMoments` and
  `FiveRowRank` through `InitialPhysicalData` and `MeanRankUpdate`, and reaches
  `PositiveOrderMoments` through the physical-prefix/profile chain. The open
  issue is semantic transport into the residual endpoint, not dead code or
  total import separation.
- [x] The branch has no tracked `.olean` or `.lake` files, and the working
  tree is clean after packaging. Ignored local build output is not part of the
  review release.
