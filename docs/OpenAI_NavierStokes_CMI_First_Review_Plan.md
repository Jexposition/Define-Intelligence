# CMI-first review plan: OpenAI Navier–Stokes claim

**Updated:** 2026-09-25
**Working verdict:** `NOT ESTABLISHED AS A CMI SOLUTION`.  The published
solution claim carries the burden of showing that the selected Lean fields
realise the advertised PDE construction.  A kernel-level `False` is a
separate, higher bar and must be proved on the selected dependency path.

This file is the compact navigation plan.  The chronology belongs in the
tracker; source extracts belong in `NavierStokesReview/evidence/`; human
argument belongs in the peer review and research paper.

## Status and decision rules

`[x]` source-checked and closed · `[~]` active · `[ ]` open · `[!]` selected
failure proved.

Do not promote a result to `False` merely because:

- a generic interface admits a countermodel;
- a force is defined from a candidate residual;
- a pressure slice has compact support;
- correction rows vanish;
- a fixed-force perturbation breaks the same trajectory; or
- a symbolic calculator returns a nonzero expression whose input has not been
  identified with the selected field.

The formal-disproof threshold is one zero-sorry Lean theorem proving, for the
actual selected path, that a required premise is false, the selected fields
fail the stated PDE or regularity predicate, or the paper's claimed identity
fails for those fields.

## Authority map and claim levels

| Level | Required proof | Status |
|---|---|---|
| Lean endpoint | Kernel checks the exported proposition and its declared axioms. | `[x]` on the inspected endpoint; axioms are standard Lean foundations. |
| Selected fields | The concrete `u`, `p`, and `f` satisfy every premise consumed by the endpoint. | `[~]` complete field-level composition remains to be exhibited. |
| Published construction | The selected fields implement the paper's five-moment `(M,I,J,S,C_p)` mechanism. | `[~]` CTR-005 remains load-bearing. |
| CMI solution | The published construction satisfies the relevant Fefferman alternative. | `[ ]` not established by the present audit. |
| Kernel refutation | A selected-path contradiction derives `False`. | `[ ]` none obtained. |

The literal forced alternatives permit a smooth external force; they do not,
by themselves, impose `∫ f = 0` or `∇ · f = 0`. Residual provenance and
fixed-force brittleness remain admissibility/provenance objections unless a
selected theorem converts them into a violated stated premise.

## Established source facts

| Area | Current result | Evidence / source anchor |
|---|---|---|
| Endpoint | `selected_witness` consumes actual schedules, stages, endpoint extensions, and axis conditions. | `END-01`–`END-05`; `selected_residual_endpoint_trace_2026-09-24.md` |
| Axioms | Inspected endpoint reports only `propext`, `Classical.choice`, and `Quot.sound`. | Axiom ledger; `#print axioms` records |
| Force | `PositiveTimeForce.force` is a wrapper; pressure enters `navierStokesResidual` in `CandidateFromLimits`. | `FORCE-01`–`FORCE-04` |
| Force limit | Selected origin composition gives residual/force tending to zero; no positive velocity-to-residual lower bound follows. | `selected_force_origin_composition_2026-09-24.md` |
| Temporal jets | Smooth cutoffs and all-order `VanishingJointJets` are present on the selected construction. | `GLU-01`, `vanishing_jets_localisation_trace_2026-09-24.md` |
| Incompressibility | Final curl-generated field has a divergence-free theorem under its stated hypotheses. | `SelectedDivergenceAudit.lean` |
| Stage recurrence | Selected stages satisfy the source `ZeroMassesOn` invariant. | `SelectedCycleMasses.lean`; `selected_cycle_mass_preservation_2026-09-25.md` |
| Selected finite prefix | `potentialSum` is locally finite before the terminal time, and all local jets use the same finite prefix. | `SelectedFieldFinitePrefix.lean`; `selected_field_finite_prefix_transport_2026-09-25.md` |
| Angular component | Positive-radius component recovery and the exact axis value are proved. | `SelectedAngularComponentFormula.lean`, `SelectedRadialSectionComponent.lean`, `SelectedRadialAxisBoundary.lean` |
| Scalar moments | Selected scalar cycle moments for the angular/axial rows vanish on their carrier. | `SelectedCycleMomentTransport.lean` |
| Curl product | The cutoff-gradient commutator is isolated exactly; its selected radial value is not known. | `SelectedCutoffCurlCommutator.lean` |
| Pressure | Compact support is a support predicate, not an absolute Poisson equation. Comparison recovery does not by itself supply selected absolute pressure semantics. | `PRS-04`–`PRS-10` |
| Active labels | Generic filter-vacuity concerns are not accepted as selected vacuity; constructive selected-stage inhabitation remains to be checked. | `CTR-019` lane |
| Euler | Companion interval and seam claims remain separate from Navier–Stokes and cannot refute it without a selected Euler contradiction. | Euler lane below |

## Load-bearing objection: CTR-005

The paper presents a five-coordinate physical repair system, while the
runtime rank interface is `FiveRowRank.Debt := Fin 3 → ℝ` and promotes it as
`(P,Jθ,Jz) ↦ (0,0,-P,-Jθ,-Jz)`.  The promotion and the two zero correction
rows are source-checked algebra.  What remains unproved is the affirmative
selected-field theorem identifying:

1. the Cartesian field exported by `selected_witness`;
2. its cylindrical/radial components and torus averages;
3. the five cumulative quantities `(M,I,J,S,C_p)`; and
4. the same identities after localisation, curl, summation, and endpoint
   passage.

This is a correspondence and burden-of-proof defect until a selected equality
or inequality fails. `FiveRows` constrains correction/profile data; it does not
automatically constrain total energy, total momentum, or the final Cartesian
field.

## Selected-field calculation route

The only active route to a selected `False` is the following composition:

```text
selected stage/potential
  → cutoff and Cartesian curl
  → cylindrical component or radial section
  → torus average
  → barMoment_apply
  → exact boundary terms at R = 0 and outer support
  → selected value or inequality Δm ≠ 0
  → FiveRows / correction invariant
  → False
```

| ID | Check | Status | Acceptance condition |
|---|---|---:|---|
| CALC-01 | Identify selected direct stages. | `[x]` | `directStages_eq` reaches `angularMeanStages`. |
| CALC-02 | Expose a selected finite prefix. | `[x]` | `SelectedDirectPrefixField.lean` gives the uncut chart/cycle identity. |
| CALC-03 | Retain cutoff and curl. | `[~]` | Expand `scaledCutoff`, `cut_angularField`, and `cartesianPotential_curl`; keep every derivative term. |
| CALC-04 | Build Cartesian-to-radial transport. | `[ ]` | Define the actual scalar input required by `barMoment_apply` and prove equality with the selected field. |
| CALC-05 | Evaluate axis and outer support. | `[~]` | Axis component-one value is proved; meridional, mixed, outer, and full boundary terms remain. |
| CALC-06 | Compute selected `Δm`. | `[ ]` | Prove a selected nonzero value or inequality after all cutoffs, curls, sums, averages, and boundaries. |
| CALC-07 | Derive `False`. | `[ ]` | Combine CALC-06 with the selected correction invariant in Lean without `sorry`. |
| CALC-08 | Verify recurrence/mass preservation. | `[x]` | `selected_cycle_zeroMasses` holds for every stage; do not call this total-field conservation. |
| CALC-09 | Compare scalar moments with Cartesian output. | `[~]` | Transport the scalar `barMoment` identities through the atlas frame, localisation, curl, and `tsum`. |
| CALC-10 | Verify finite-prefix/tail order. | `[x]` locally | Preterminal `tsum` tails are exactly zero after a finite index; terminal transport is still open. |

### Concrete subtargets

1. **Chart formula.** Use the existing positive-radius component theorem and
   `Atlas.field_on_chart` / `Atlas.angular_field` to expose one complete
   selected stage in chart coordinates.
2. **Commutator.** Carry
   $$
   \nabla\times(\chi A)=\chi(\nabla\times A)+(\nabla\chi)\times A
   $$
   through the selected prefix. The second term is a target, not evidence of
   non-vanishing until its selected radial value is calculated.
3. **Torus transport.** Check `PressureStream.torusAverage_physicalAlias`,
   `torusAverage_physicalCompact`, and the radial-section identities before
   asserting that the coordinate bridge is impossible.
4. **Boundary terms.** Evaluate the axis branch, outer support, integrability,
   and any chart exclusion together. Do not infer a delta term from the
   hypothesis `radius_ne` alone.
5. **Symbolic helper.** Run
   `NavierStokesReview/tools/radial_profile_integrals.py` only after Lean has
   supplied an exact selected profile. Calculator output is evidence only
   when its input is identified with the selected field.

## Five-dimensional transport lane

| ID | Required check | Status |
|---|---|---:|
| 5D-01 | Extract `PositiveOrderMoments` and `FiveProfileMoments` rows. | `[x]` |
| 5D-02 | Extract `FiveRowRank`, `scaleDebt`, fixed zero rows, and update laws. | `[x]` |
| 5D-03 | Verify the algebraic promotion template. | `[x]` |
| 5D-04 | Identify promotion with selected physical integrals. | `[ ]` |
| 5D-05 | Test direct type collision with `Witness`. | `[x]` no collision; `Witness` does not export rank debt. |
| 5D-06 | Preserve the conditional zero-row obstruction. | `[x]` `CorrectionInvariantScope.lean` proves it conditionally. |

Required bridge theorem shape:

```text
selectedFieldMoment j k = barMoment k (selected scalar field) j
```

with explicit atlas, torus, support, curl, and finite-prefix hypotheses. The
current code has not supplied this theorem.

## Pressure and force lanes

| ID | Question | Status / action |
|---|---|---|
| PRS-01 | Does compact `pressure_support` alone force pressure or velocity to vanish? | `[x]` No; cleared as a standalone contradiction. |
| PRS-02 | Does comparison recovery establish selected absolute Poisson semantics? | `[~]` Interface limitation recorded; connect `pressure_germ`/`base_equation` to the selected field. |
| PRS-03 | Can the selected pressure violate the actual global pressure identity? | `[ ]` Requires a selected absolute Poisson/normalisation equation and a contradictory selected value. |
| FORCE-01 | Is the external force smooth and correctly supported? | `[~]` Recheck selected endpoint predicates, not only wrapper smoothness. |
| FORCE-02 | Does residual provenance itself refute the existential claim? | `[x]` No. Preserve it as a causal/provenance objection unless an explicit admissibility premise is proved. |
| FORCE-03 | Do fixed-force perturbations refute the literal endpoint? | `[~]` They prove same-force path brittleness, not negation of `∃ f`. |

## Cleared or bounded attack surfaces

| Route | Disposition |
|---|---|
| Force must satisfy `∫ f = 0` or `∇·f = 0` | Not a CMI requirement without an additional theorem; do not use as a disproof. |
| Non-Newtonian/Ladyzhenskaya regularisation | External physical stability test, not the classical forced equation. |
| Smooth cutoff discontinuity | Cleared on the selected path where the source supplies smooth cutoffs and all-order jets. |
| Filter-bottom vacuity | Generic risk only; selected finite-prefix path is not thereby vacuous. |
| Zero correction rows = zero total energy | False inference; keep correction/profile moments separate from total Cartesian energy. |
| Pressure compact support = trivial pressure | False inference without the selected global elliptic identity. |
| Axis exclusion alone = discontinuity | Not proved; the axis branch now has an exact component-one value. |
| Mirror force `-f` | Smooth algebraic dual, but a different forced PDE; it does not refute the original existential witness. |

## Companion Euler lane

Keep Euler independent from the Navier–Stokes verdict. Audit:

1. parent-child interval definitions and whether the horizons sum to a finite
   terminal time;
2. actual value and derivative matching at each seam;
3. all-order jet matching, not merely open-interval smoothness; and
4. whether the coupled unforced Euler equation is preserved across the child
   insertion.

The Zeno and seam-discontinuity proposals remain hypotheses until exact source
lemmas or a zero-sorry selected contradiction are obtained. Use the supplied
`docs/euler.pdf` and companion paper as source context only; do not transfer an
Euler finding to the forced Navier–Stokes claim.

## Selected labels and global transport

| Lane | Current requirement |
|---|---|
| CTR-016 global germ transport | Check whether `CandidateConsequences` and `ActualCandidateAssembly` export a field-level link from `PhysicalData` to the five moments. |
| CTR-019 selected-label inhabitation | Find constructive nonemptiness for every selected stage; do not infer empty limits from generic subtype/filter concerns. |
| Axis scope | Keep `StateRealization.chartIdentity` off-axis and `GlobalBaseError.originPast` separate until an explicit crossing theorem is proved. |
| Temporal patching | Preserve the source-backed smoothness result; search only for an actual selected unmatched jet. |

## Evidence and document synchronisation

After every source-backed result, update:

- `docs/OpenAI_NavierStokes_Audit_Tracker.md`;
- `docs/OpenAI_NavierStokes_Axiom_Ledger.md`;
- `docs/OpenAI_NavierStokes_Peer_Review_v1.md`;
- `docs/OpenAI_NavierStokes_Research_Paper.md`;
- `docs/OpenAI_NavierStokes_Input_Document_Synthesis.md`;
- `README.md`; and
- `docs/REVIEW_DOCUMENT_CONTROL.md`.

Every evidence entry must state: commit/tree, exact file and line anchors,
Lean theorem or source proposition, build command/result, and whether the
result is selected-path evidence, a conditional result, or an unresolved
proposal. Never describe a generic probe as a selected contradiction.

## Tooling and release gates

| Gate | Acceptance test | Status |
|---|---|---:|
| Lean review tree | `lake build NavierStokesReview` under Lean `v4.34.0-rc2`; no errors, `sorry`, custom axioms, or `unsafe` in new review modules. | `[x]` 3701 jobs |
| Build hygiene | No tracked `.olean`, `.ilean`, `.c`, or `.lake` outputs. | `[x]` |
| Python helper | Run the radial helper with the canonical V-lab interpreter after its path is repaired. | `[ ]` |
| Documentation | New evidence cited in tracker, axiom ledger, synthesis, peer review, paper, README, control map, and this plan. | `[x]` through axis-boundary update |
| Release | Commit and push only review source, evidence, and documents; leave supplied PDFs and scratch space untracked. | `[x]` at `c874c5e` |

## Immediate execution order

1. Trace `Atlas.physical` → `physicalPoint` → torus-average invariance for one
   selected positive-radius stage.
2. Expand the selected cutoff/curl commutator and identify its actual radial
   operator input.
3. Prove the first selected `barMoment_apply` equality with all integrability
   and boundary hypotheses explicit.
4. Calculate `Δm`; only then attempt the zero-sorry `False` theorem.
5. Record the result across the evidence ledger and active counter-paper.

**Current stopping point:** no selected nonzero remainder and no selected
kernel contradiction have yet been proved. The active burden remains the
Cartesian-to-radial transport calculation, not a generic restatement of the
missing bridge.

## Source anchors

- CMI problem statement: `docs/navier-stokes.pdf`.
- OpenAI paper: `docs/navier-stokes openai.pdf`.
- Public repository: `NavierStokes/` and its Lean import closure.
- Primary review theorem tree: `NavierStokesReview/src/completions/`.
- Evidence ledger: `NavierStokesReview/evidence/`.
