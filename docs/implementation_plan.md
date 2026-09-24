# CMI-first implementation map

**Authority:** `REVIEW_DOCUMENT_CONTROL.md` and `OpenAI_NavierStokes_CMI_First_Review_Plan.md`.

**Scope:** test whether the published paper's five-moment and pressure claims are transported into the selected Lean witness. This map records actions and acceptance tests, not a chronological log.

| ID | Work package | Status | Acceptance test |
|---|---|---:|---|
| W1 | Freeze source commit, CMI statement, and active document map | [x] | Source paths and claim scope are recorded in the control map. |
| W2 | Map `selected_witness`, `StageEstimates`, germ assembly, residual, force, and origin blow-up | [x] | Selected endpoint trace has source anchors. |
| W3 | Extract five target moments and runtime three-debt engine | [x] | `physical_transport_bridge_spec_extraction_2026-09-24.md` records literal definitions and anchors. |
| W4 | Test whether generic `StageEstimates` determines five debt or blow-up | [x] | `StageEstimatesMomentBlindnessProbe.lean` compiles without `sorry`. |
| W5 | Locate selected-path five-moment transport theorem | [~] | Generic stage estimates do not provide it. The new zero-sorry probe proves the exported `Witness` does not entail an arbitrary five-debt certificate; field-level violation is still unproved. |
| W6 | Connect pressure germ/base equation to global pressure semantics | [ ] | Either a contradiction is derived or the exact missing premise is documented. Pressure comparison alone is insufficient. |

| W7 | Re-audit live upstream five-moment construction against selected mixed endpoint | [x]/[ ] | Upstream identities and base blow-up compile; final mixed-sum transport remains open. |
| W8 | Connect `VanishingJointJets` to the origin residual and blow-up | [~] | `SelectedWitnessAttackBoundaryProbe.lean` proves the scalar endpoint predicates are compatible; a PDE-specific residual lower bound remains the required attack theorem. |
| W9 | Rewrite the peer review and research paper as human-readable papers | [x] | The research paper is now a single coherent argument; the peer review retains its evidence findings and states the same verdict boundary. |
| W10 | Run all probes, lint documents, and package branch | [ ] | Probes pass; `git diff --check` passes; no tracked `.olean` or build output; final status is clean after commit. |

## Formal target board

| ID | Target | Current result |
|---|---|---|
| CTR-005 | Selected five-moment transport | Open. No selected-field equality has been located. |
| CTR-037 | Generic stage interface encodes blow-up | Confirmed interface countermodel: zero stages satisfy the generic rate record but do not blow up. |
| CTR-039 | Generic stage interface determines five debt | Confirmed by `interface_does_not_determine_five_debt`; this is not yet a selected-witness refutation. |
| CTR-040 | Residual flatness contradicts origin blow-up | Residual-flatness compatibility probe blocks this implication without PDE coupling; selected endpoint contradiction remains open. |
| CTR-041 | Selected residual lower-bound obstruction | Zero-sorry conditional contradiction is proved. The selected source currently supplies upper jet rates, not the required positive lower bound. |
| PRS-08 | Compact pressure support alone forces trivialisation | Open attack. Compact support is not itself the contradiction; the required global Poisson/Leray premises must be formalised against the selected fields. |
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
- Supporting notes are secondary; source code and compiled probes control the verdict.

## Current next action

Inspect the selected import closure for a theorem whose conclusion mentions both the actual selected stages and `PositiveOrderMoments.moments`; if absent, write the smallest zero-sorry obstruction showing the selected endpoint type does not expose that equality.

## 5D target specification and runtime engine

| Item | Status | Acceptance test |
|---|---:|---|
| 5D-01 | [x] | Literal `PositiveOrderMoments` rows, integrals, and exact repair lemmas extracted. |
| 5D-02 | [x] | `FiveProfileMoments` paper-shaped debt and exponent vectors extracted. |
| 5D-03 | [x] | `FiveRowRank` five-row proposition and distinct `Fin 3 → ℝ` debt recorded. |
| 5D-04 | [x] | `MeanRankUpdate.scaleDebt` coefficients and update laws recorded. |
| 5D-05 | [x] | `promoteDebt : (Fin 3 → ℝ) → (Fin 5 → ℝ)` template recorded; promotion is not selected-field transport. |
| 5D-06 | [ ] | Prove selected-field equality between the five physical moments and promoted runtime rows. |
| 5D-07 | [ ] | Carry that equality through `StateRealization.chartIdentity`, pressure data, residual estimates, and `VanishingJointJets`. |

| FJ-01 | [~] | Attack force smoothness by proving the selected residual derivatives cannot have the `hlim` endpoint family despite velocity blow-up. The scalar implication is blocked; source-specific coupling is required. |
| FJ-02 | [~] | Add the missing global pressure-Poisson/Leray equation and derive a selected pressure/support contradiction if the hypotheses really force one. |
| FJ-03 | [x] | `SelectedWitnessAttackBoundaryProbe` proves the exported `Witness` does not entail zero for every five-debt payload. This is a type-level gap, not yet a field-level violation. |
| FJ-04 | [~] | Trace `ActualCandidateAssembly.Witness` through `R3/ActualCandidate.of_localized_fields` and `R3/Theorem`; test whether any five-moment equality is consumed. |
| FJ-05 | [~] | Attack `CandidateFromLimits.hlim` at the selected origin by expanding the actual residual against `origin_blowup`; generic predicate incompatibility is not sufficient. |
| FJ-06 | [~] | Add the selected-field pressure-Poisson/Leray identity as a proof target and test it against compact localisation; compact support alone is not a contradiction. |
| FJ-08 | [x]/[~] | The companion probes prove that `c * ‖u‖ ≤ ‖residual‖` would force `False`, while a scalar countermodel shows blow-up plus flat residual is otherwise consistent. Source inspection has not found the selected premise. |

**Last updated:** 2026-09-24

## Selected-witness attack board

| ID | Status | Acceptance test |
|---|---:|---|
| SW-01 | [~] | Derive the selected positive velocity-to-residual lower bound. |
| SW-02 | [~] | Derive the selected global pressure-Poisson/Leray identity and test support. |
| SW-03 | [x]/[~] | Interface moment blindness is proved; concrete selected-field violation remains open. |
| SW-04 | [ ] | Close one attack with a zero-sorry `False` theorem from `selected_witness`. |
