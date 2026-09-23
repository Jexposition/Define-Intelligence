# OpenAI Navier–Stokes Audit Tracker

**Review status:** Active independent review
**Review branch:** `review/cmi-first-navier-stokes-2026-09-22`
**Upstream snapshot:** `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
**Scope:** proposition-level, dependency-level, and semantic audit of the Lean formalisation and its claimed correspondence with the Clay formulation.

## 1. Disposition legend

| Status | Meaning |
|---|---|
| **CONFIRMED** | Directly established by source inspection or a completed zero-sorry probe. |
| **OPEN** | A proof-relevant obligation remains; the present evidence is insufficient for a conclusion. |
| **NOT ESTABLISHED** | The public materials do not yet justify the claimed mathematical conclusion. This is not a formal refutation. |
| **OVERCLAIM CORRECTED** | An earlier review statement was stronger than the source evidence supports. |
| **NOT A DEFECT** | A proposed criticism does not follow because the cited premise is permitted or the cited file is not in the audited snapshot. |

## 2. Current disposition

The review does **not** report a valid Lean contradiction in the upstream theorem. It reports that the claim of a verified solution to the Millennium Prize problem is **not established by the present audit**.

The strongest confirmed findings are:

1. The exported theorem is shaped around forced alternatives C and D, not the unforced alternatives A and B.
2. The force in the candidate construction is defined from the momentum residual of the selected fields and is active up to the singular endpoint in the source-level construction. The code does not impose causal independence of the force from the velocity.
3. `JetRate` has no `NeBot` premise, and a zero-sorry probe proves that `JetRate` is true on `Filter.bot`. The selected endpoint filter is separately nontrivial, but the derived filter containing `activeᶜ` still requires a proof of non-vacuity.
4. The five-row moment-repair infrastructure is present and imported into the construction. No row-drop defect has been found. Its mathematical adequacy still depends on the surrounding analytic interfaces.
5. Earlier references to `Forcing/Smoothness.lean`, `Pressure/LerayProjection.lean`, and `Scaling/SingularLimits.lean` do not describe the audited source tree. Their absence is not evidence that the corresponding obligations are absent.

## 3. Formal audit matrix

| ID | Question | Evidence | Disposition | Next proof obligation |
|---|---|---|---|---|
| AUD-001 | What source is being reviewed? | Review branch and upstream commit recorded above. | CONFIRMED | Preserve commit hashes with each future result. |
| AUD-002 | Is the local source current? | Upstream `main` is `f9e8bc5...`; local extraction and public tree differ in file count and imports. | OPEN | Complete normalised file-by-file comparison. |
| AUD-003 | Do C and D permit forcing? | Official Clay statement and `ComparatorDefinitions.lean`. | CONFIRMED | Verify the exact force decay predicate used by the bridge. |
| AUD-004 | What does the whole-space theorem return? | `NavierStokes/R3/Theorem.lean`. | CONFIRMED at source level | Complete kernel and transitive dependency audit. |
| AUD-005 | How is the C bridge formed? | `NavierStokes/R3/ComparatorBridge.lean`. | CONFIRMED at source level | Audit every conversion hypothesis. |
| AUD-006 | Are challenge files admitted? | Four `sorry` lines remain in `ComparatorChallenges`. | CONFIRMED lexical | Establish that no headline theorem imports them. |
| AUD-007 | Are `#print axioms` commands themselves axioms? | `ComparatorSolution.lean` contains reporting commands, not declarations. | CONFIRMED | Capture clean current outputs. |
| AUD-008 | Is the toolchain reproducible? | Repository pins Lean 4.34.0-rc2; requested package root is 4.32. | OPEN | Run a clean pinned build and a separately labelled 4.32 compatibility probe. |
| AUD-009 | Is the archive identical to the checkout? | Zip and extracted tree have not been fully normalised and hashed. | OPEN | Produce archive/check-out manifest. |
| AUD-010 | Are domains and quantifiers preserved? | R3 problem statement, comparator bridge, endpoint clauses. | OPEN | Build a domain-and-quantifier correspondence table. |
| AUD-011 | Does compact support imply the stated force decay? | `CompactSpatialForceDecay` and R3 bridge. | OPEN | Verify all derivative and time quantifiers. |
| AUD-012 | Is the periodic route independently established? | `PeriodicPaperTheorem.lean`, `PeriodicPaperComparator.lean`. | OPEN | Audit it separately from the R3 route. |
| AUD-013 | Are independent comparator tools available? | Comparator challenge instructions are separate from the exported-result probes; the exported results have independent standard-only axiom reports. | CONFIRMED for exported-result scope | Keep challenge placeholders separate from the headline theorem. |
| AUD-014 | Does uniqueness close analytically? | `R3/WholeSpaceUniqueness.lean`; pressure recovery, flux, comparison, closure. | OPEN | Audit each imported theorem and its hypotheses. |
| AUD-015 | Is the candidate assembled from supplied finite-stage data? | `ActualCandidateAssembly.lean`, `GermCandidateAssembly.lean`. | CONFIRMED at source level | Map the invariant-to-rate chain. |
| AUD-016 | Is forcing selected a posteriori? | Candidate witness returns `forcing` after candidate fields and residual consequences. | CONFIRMED | Test smoothness, support, decay, and exact residual identity. |
| AUD-017 | Does the R3 force bridge meet the comparator class? | `ComparatorBridge.lean`, `CompactSpatialForceDecay.lean`. | OPEN | Prove the exact implication, not merely compact support informally. |
| AUD-018 | Is positive-viscosity scaling preserved? | `R3/ViscosityScaling.lean`. | OPEN | Check transformed velocity, pressure, force, support, and energy. |
| AUD-019 | Does the periodic theorem have its own proof? | Periodic theorem and comparator files. | OPEN | Complete the periodic audit. |
| AUD-020 | Do supplied critiques distinguish defects from robustness? | Review drafts and formal source. | CONFIRMED disposition | Keep altered-PDE tests as robustness evidence, not Lean counterexamples. |
| AUD-021 | Is a clean current axiom run available? | Earlier transcripts exist; current cache/toolchain run is not yet clean. | OPEN | Produce a reproducible `#print axioms` report. |
| AUD-056 | Can `JetRate` be vacuous? | `DiagonalResidual.lean`; `JetRateVacuityProbe.lean`. | CONFIRMED hazard; path impact OPEN | Prove non-bottomness of the exact selected derived filter. |
| AUD-057 | Are CMI procedural conditions met? | CMI rules require qualifying publication, two years, and general acceptance. | NOT MET as procedural gate | Track procedure separately from Lean validity. |
| AUD-058 | Are inverse-domain call sites empty? | `GaugeAliasDecay.lean` and call-site map. | CONFIRMED locally | Trace local estimates into the selected physical witness. |
| AUD-081 | Is the force active before blow-up? | `CandidateFromLimits.lean`, force equals activated residual on `0 ≤ t < 1`; zero only shown for `t ≤ 0` and `t ≥ 2`. | CONFIRMED | State as causality/interpretation issue, not automatic C/D contradiction. |
| AUD-082 | Is the finite-stage interface merely assumed? | `StageEstimates`, `GluedStageEstimates`, `ActualCycleResidualBounds`. | OVERCLAIM CORRECTED | Audit whether invariant-to-rate derivation supplies every estimate. |
| AUD-083 | Does the actual path use the five-row system? | `FiveProfileMoments.lean`, `LocalizedMomentRepair.lean`, `FiveRowRank.lean`. | CONFIRMED | Map each debt row to the paper's moment language. |
| AUD-084 | Is pressure absent or represented by missing files? | Actual pressure hierarchy exists; early cited filenames do not. | OVERCLAIM CORRECTED | Audit pressure hypotheses and whole-space bounds directly. |
| AUD-085 | Does `JetRate` vacuity refute the theorem? | Bottom-filter probe succeeds; endpoint `originPast` probe succeeds; `activeᶜ` intersection unresolved. | NOT ESTABLISHED | Do not label as refutation until the selected filter is proved bottom or the theorem is shown to consume vacuity. |

## 4. Required evidence before a stronger verdict

The review may issue a formal failure finding only if one of the following is established:

- a theorem used by the headline endpoint has a false or mismatched type;
- a required force, domain, regularity, decay, or initial-data condition is absent from the actual witness;
- the selected proof path consumes a vacuous proposition through a bottom filter;
- an admitted declaration or unproved custom axiom is imported into the headline theorem; or
- the Lean theorem proves a statement that is formally incompatible with the claimed CMI alternative.

The current record establishes audit targets and semantic limitations, but none of these five failure conditions has yet been proved for the headline theorem.

## 5. Evidence protocol

Every new entry must name the commit, source file and line range, proposition or definition, test command, and status. A mathematical conclusion must be separated from a source-level observation and from a physical robustness objection. The paper and peer-review report cite this tracker; they do not reproduce its chronology.

## 6. Historical continuity

The previous tracker contained a longer sequence of records, including repeated build, axiom, bridge, and semantic checks. The present document consolidates those records by question so that the tracker remains readable without erasing their decision-bearing conclusions. The following historical findings remain active:

| Historical records | Consolidated conclusion |
|---|---|
| `AUD-009`, `AUD-022`–`AUD-029` | Archive/check-out comparison, theorem-shape checks, environment facts, and lexical scans were recorded as source or environment evidence. |
| `AUD-030`–`AUD-036` | Proposition-shape and formal-trust checks were confirmed; analytic peer review remained open. |
| `AUD-037`–`AUD-045` | Analytic and environment questions were kept open or closed only as environment conditions; they were not silently converted into theorem failures. |
| `AUD-047`–`AUD-055` | Pre-export, headline, Euler, force-bridge, semantic-matrix, boundary-convention, and construction-provenance evidence was recorded as positive formal evidence with analytic obligations still open. |
| `AUD-059`–`AUD-068` | Endpoint non-vacuity, semantic interfaces, final verdict, forced C/D classification, and certificate provenance were recorded. These establish formal scope, not an unforced A/B result. |
| `AUD-069`–`AUD-080` | Independent Clay-bridge, force timing, five-row, pressure provenance, model-scope, division, filter, and row-label findings were recorded. |

The historical source records remain recoverable from the parent review commit in Git. New work must update the consolidated entries above or add a new numbered entry; it must not reintroduce a daily diary into the paper or peer-review report.
