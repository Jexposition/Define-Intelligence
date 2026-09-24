# CMI-first implementation map

**Authority:** `REVIEW_DOCUMENT_CONTROL.md` and `OpenAI_NavierStokes_CMI_First_Review_Plan.md`.

**Scope:** test whether the published paper's five-moment and pressure claims are transported into the selected Lean witness. This map records actions and acceptance tests, not a chronological log.

| ID | Work package | Status | Acceptance test |
|---|---|---:|---|
| W1 | Freeze source commit, CMI statement, and active document map | [x] | Source paths and claim scope are recorded in the control map. |
| W2 | Map `selected_witness`, `StageEstimates`, germ assembly, residual, force, and origin blow-up | [x] | Selected endpoint trace has source anchors. |
| W3 | Extract five target moments and runtime three-debt engine | [x] | `physical_transport_bridge_spec_extraction_2026-09-24.md` records literal definitions and anchors. |
| W4 | Test whether generic `StageEstimates` determines five debt or blow-up | [x] | `StageEstimatesMomentBlindnessProbe.lean` compiles without `sorry`. |
| W5 | Locate selected-path five-moment transport theorem | [ ] | Theorem identifies actual selected-field integrals with `(M,I,J,S,C_p)`. |
| W6 | Connect pressure germ/base equation to global pressure semantics | [ ] | Either a contradiction is derived or the exact missing premise is documented. |
| W7 | Connect `VanishingJointJets` to the origin residual and blow-up | [ ] | A zero-sorry theorem derives `False` from selected premises, or the attempted implication is formally blocked. |
| W8 | Rewrite the peer review and research paper as human-readable papers | [~] | Findings are claim/evidence/conclusion prose, not task history. |
| W9 | Run all probes, lint documents, and package branch | [ ] | Probes pass; `git diff --check` passes; no tracked `.olean` or build output. |

## Formal target board

| ID | Target | Current result |
|---|---|---|
| CTR-005 | Selected five-moment transport | Open. No selected-field equality has been located. |
| CTR-037 | Generic stage interface encodes blow-up | Confirmed interface countermodel: zero stages satisfy the generic rate record but do not blow up. |
| CTR-039 | Generic stage interface determines five debt | Confirmed by `interface_does_not_determine_five_debt`; this is not yet a selected-witness refutation. |
| PRS-08 | Compact pressure support alone forces trivialisation | Rejected as a proof route; compact support alone is insufficient. |
| PRS-09 | Selected pressure has global Poisson semantics | Open; comparison lemmas do not supply the absolute selected-field premise. |

## Required source checks

1. `PositiveOrderMoments.lean`: preserve the literal `rowDensity`, `positiveIntegral`, `moments`, repair, and exact-repair definitions.
2. `FiveProfileMoments.lean`: record `physicalMoments_eq` and the derivative/positivity lemmas.
3. `FiveRowRank.lean` and `MeanRankUpdate.lean`: record the `Fin 3` debt, scaled update, five-row constraints, and promotion map.
4. `StateRealization`, `CandidateFromLimits`, and `GermCandidateAssembly`: test whether field-level moments, pressure semantics, and residual jets are linked.

## Evidence rules

- A generic interface countermodel is evidence against the interface implication only.
- A missing theorem is a correspondence objection, not a formal refutation by itself.
- `False` may be recorded only after a source-backed, zero-sorry Lean derivation from the selected witness and its actual premises.
- Agent notes are supporting material; source code and compiled probes control the verdict.

## Current next action

Inspect the selected import closure for a theorem whose conclusion mentions both the actual selected stages and `PositiveOrderMoments.moments`; if absent, write the smallest zero-sorry obstruction showing the selected endpoint type does not expose that equality.

**Last updated:** 2026-09-24
