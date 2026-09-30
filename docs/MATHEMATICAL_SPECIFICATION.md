# Mathematical specification and audit navigation

## Historical audit state (2026-09-28)

Current register correction: **2,792 indexed modules, 588 captured
endpoint-closure modules, 745 evidence-inspected modules, 2,040
source-indexed modules queued, and 0 missing project import edges**. The
latest direct source review is
priority_135_external_moment_realization_junction_source_review_2026-09-28.md.
The older count and tranche sentence below is retained as historical wording.
Use `DOCUMENTATION_RECONCILIATION_2026-09-30.md` for the live pointer.

The authoritative semantic coverage register is [`REPOSITORY_SEMANTIC_COVERAGE_REGISTER.md`](REPOSITORY_SEMANTIC_COVERAGE_REGISTER.md). The 2026-09-28 snapshot recorded **2,792 indexed modules, 588 captured endpoint-closure modules, 745 evidence-inspected modules, 2,040 source-indexed modules queued, and 0 missing project import edges**. The latest source tranche in that snapshot is [`priority_135_external_moment_realization_junction_source_review_2026-09-28.md`](../NavierStokesReview/src/audit/priority_135_external_moment_realization_junction_source_review_2026-09-28.md). The evidence is intermediate: it confirms genuine reduced-profile repair and local Cartesian/pressure/residual infrastructure, but does not establish the final selected Cartesian `barMoment` / `(M,I,J,S,C_p)` theorem. The live 2026-09-30 state is controlled by the reconciliation document above.

> This is a reading layer over the captured Lean source and environment maps. It translates only metadata that was actually extracted. It is not a replacement proof and it does not infer a theorem from a filename.

## How to use this document

1. Start with the endpoint route below.
2. Read the plain-language layer description before opening Lean.
3. Follow the linked source spans and the interactive map for imports and users.
4. Treat every `UNAVAILABLE` or `NOT_CLASSIFIED` marker as an audit task, not as evidence of failure.

## Formal objects in ordinary notation

| Lean object or pattern | Reader notation | Status of translation |
|---|---|---|
| `Fin 3 → ℝ` | \(\mathbb{R}^3\) | syntax-level translation |
| `Fin 5 → ℝ` | \(\mathbb{R}^5\) | syntax-level translation |
| `VelocityField` | a time-space vector field \(u(t,x)\) | only when the captured type confirms it |
| `PressureField` | a scalar field \(p(t,x)\) | only when the captured type confirms it |
| `navierStokesResidual` | \(\mathcal{R}_{NS}(u,p)\) | notation aid; inspect the source definition for its exact terms |
| `FiveRows` / `Debt` / `barMoment` | finite-dimensional correction or moment data | names do not prove field-level transport |

## Endpoint route

```text
source inventory → Lean source declarations → compiled environment
                         ↓ exact-name join
                 selected_witness → CandidateProperties
                         ↓
                 theorem_1_1 / theorem_1_1_with_initial_rest
```

The graph distinguishes structural reachability from semantic identity. In particular, a reachable moment declaration does not by itself establish an equation of the form

\[\mathsf{Moment}_{\mathrm{paper}}(u,p)=\mathsf{Debt}_{\mathrm{runtime}}.\]

That equality is the field-level transport obligation tracked by CTR-005.

| Route target | Source span | Reachability |
|---|---|---|
| `NavierStokesR3.theorem_1_1` | `NavierStokes/R3/Theorem.lean:46-51` | True |
| `NavierStokes.ActualCandidateAssembly.selected_witness` | `NavierStokes/ActualCandidateAssembly.lean:1177-1182` | True |
| `NavierStokes.FiveRowRank.FiveRows` | `NavierStokes/FiveRowRank.lean:241-248` | True |
| `NavierStokes.FiveRowRank.Debt` | `NavierStokes/FiveRowRank.lean:22-24` | True |
| `NavierStokes.PositiveOrderMoments.Debt` | `NavierStokes/PositiveOrderMoments.lean:23-24` | True |
| `NavierStokes.MeanRankUpdate.scaleDebt` | `NavierStokes/MeanRankUpdate.lean:30-32` | True |
| `NavierStokes.MixedPeriodicAssembly.periodicVelocity` | `NavierStokes/MixedPeriodicAssembly.lean:36-39` | True |
| `NavierStokes.DefectIncrementBounds.barMoment` | `NavierStokes/DefectIncrementBounds.lean:214-217` | True |
| `NavierStokes.R3CompactCandidate.velocity` | `NavierStokes/R3CompactCandidate.lean:201-203` | True |
| `NavierStokesR3.ProblemStatement.CandidateProperties` | `NavierStokes/R3/ProblemStatement.lean:92-111` | True |

## Review lanes

| Lane | Mathematical question | Evidence boundary |
|---|---|---|
| CTR-005 | Do the five named paper moments reach the selected Cartesian fields after correction, localisation, curl, periodisation, summation, and R³ packaging? | `CORRESPONDENCE_GAP` means the selected-path transport theorem is not in the captured endpoint contract; it is not a kernel contradiction. |
| CTR-012 | Is the force treated as a prescribed datum, or is its provenance residual-defined? | A residual provenance trace is a provenance concern; it does not alone negate an existential formal statement. |
| Pressure | Is there an absolute global Poisson/Leray identity, or only comparison/support/flux facts? | Read exact pressure declarations and hypotheses. |
| Energy | What domain and interval do the energy estimates cover? | Do not infer a global statement from a candidate consequence name. |
| Axis/chart | Do off-axis chart identities transport to the on-axis route? | Record the excluded domain and the separate endpoint theorem. |
| Axiom hygiene | Does the selected endpoint use `sorryAx`? What is the repository-wide source count? | Keep endpoint dependency scope separate from repository metadata. |

## Selected declaration index

The rows below are the declarations most relevant to the current review register. The complete machine dataset retains every source declaration and every compiled edge.
The table is deliberately reader-facing: long elaborated Lean terms are not useful as prose. Each exact captured type remains available in the interactive map and in `repository_audit_graph_2026-09-26_full.json.gz`; the ordinary JSON is the compact query graph.

| Declaration | What it does in the construction | Captured type | Source | Status |
|---|---|---|---|---|
| `NavierStokesR3.theorem_1_1` | Exported R³ breakdown proposition. This is the endpoint whose dependency scope must be checked against the CMI statement. | `NavierStokesR3.ProblemStatement.breakdownStatement` | [`NavierStokes/R3/Theorem.lean:46-51`](../NavierStokes/R3/Theorem.lean) | `VERIFIED_STANDARD_AXIOM_SCOPE` |
| `NavierStokesR3.theorem_1_1_with_initial_rest` | Existential R³ candidate package with the initial-rest and endpoint consequences shown in its formal type. | `captured; full elaborated type in the audit graph` | [`NavierStokes/R3/Theorem.lean:26-45`](../NavierStokes/R3/Theorem.lean) | `NOT_CLASSIFIED` |
| `NavierStokes.ActualCandidateAssembly.selected_witness` | Concrete witness bundle consumed by the candidate theorem. Follow its fields before interpreting the public existential result. | `NavierStokes.ActualCandidateAssembly.Witness NavierStokes.ActualCandidateConstruction.selectedBudget NavierStokes.ActualCandidateConstruction.selectedThreshold NavierStokes.ActualCandidateConstruction.selectedThreshold_geometry` | [`NavierStokes/ActualCandidateAssembly.lean:1177-1182`](../NavierStokes/ActualCandidateAssembly.lean) | `CORRESPONDENCE_GAP` |
| `NavierStokesR3.ProblemStatement.CandidateProperties` | Admissibility predicate for velocity, pressure, force, support, regularity, divergence, residual, energy, and blow-up conditions. | `Real -> NavierStokesR3.ProblemStatement.VelocityField -> NavierStokesR3.ProblemStatement.PressureField -> NavierStokesR3.ProblemStatement.VelocityField -> (Set.{0} NavierStokesR3.ProblemStatement.Space) -> Prop` | [`NavierStokes/R3/ProblemStatement.lean:92-111`](../NavierStokes/R3/ProblemStatement.lean) | `PROVENANCE_CONDITIONED` |
| `NavierStokes.FiveRowRank.FiveRows` | Finite correction-row predicate. It constrains the correction object; it is not automatically a theorem about the assembled Cartesian velocity field. | `(Real -> Real) -> (Real -> Real) -> NavierStokes.FiveRowRank.Debt -> (Real -> Real) -> (Real -> Real) -> Prop` | [`NavierStokes/FiveRowRank.lean:241-248`](../NavierStokes/FiveRowRank.lean) | `CORRESPONDENCE_GAP` |
| `NavierStokes.PositiveOrderMoments.Debt` | Upstream finite-dimensional moment/debt type used by the positive-order repair branch. | `Type` | [`NavierStokes/PositiveOrderMoments.lean:23-24`](../NavierStokes/PositiveOrderMoments.lean) | `CORRESPONDENCE_GAP` |
| `NavierStokes.MeanRankUpdate.scaleDebt` | Runtime transformation that rescales or updates a debt vector between correction stages. | `Real -> Real -> NavierStokes.MeanRankUpdate.Debt -> NavierStokes.MeanRankUpdate.Debt` | [`NavierStokes/MeanRankUpdate.lean:30-32`](../NavierStokes/MeanRankUpdate.lean) | `CORRESPONDENCE_GAP` |
| `NavierStokes.DefectIncrementBounds.barMoment` | Scalar/radial moment operator at the correction interface. Its domain and relation to the final Cartesian field require source-level inspection. | `forall {P : Type}, Nat -> (NavierStokes.DefectIncrementBounds.ScalarField (NavierStokes.DefectIncrementBounds.Point P)) -> (NavierStokes.DefectIncrementBounds.ScalarField P)` | [`NavierStokes/DefectIncrementBounds.lean:214-217`](../NavierStokes/DefectIncrementBounds.lean) | `CORRESPONDENCE_GAP` |

## Coverage and limitations

The source map contains **2790 modules**, **50191 source declarations**, **30721 compiled environment declarations**, and **227128 source-located joined edges**. Exact source joins: **22958**. Reachable `sorryAx` users at the selected endpoint: **0**.

The full audit graph is a separate, wider view: it contains the joined source declarations, **7760 compiled-only declarations**, **30725 typed graph nodes**, and **334042 edges** consisting of **327757 generic compiled-use edges** plus **6285 module-import edges**. These totals are not interchangeable with the source-located joined-edge count above.

### Coverage matrix

| Audit layer | Captured result | What a mathematician may conclude |
|---|---:|---|
| Source modules | 2790 | Every indexed Lean module has a source path, import list, flags, and declaration inventory. |
| Source declarations | 50191 | Every declaration found by the source parser is searchable and linked to a source span. |
| Exact source/environment joins | 22958 | These names have an exact source/environment match; this is not a claim that their theorem meanings have been transported. |
| Source declarations with captured types | 22965 | These source declarations have captured elaborated types; the remainder are explicit type-coverage gaps. |
| Compiled-only declarations with captured types | 7760 | These environment declarations have no joined current-source declaration in this capture. |
| Total typed graph nodes | 30725 | This is the source-plus-compiled typed population in the full graph, not the number of mathematical propositions proved. |
| Source declarations without captured types | 27226 | No type should be inferred from a name, role label, or import edge. |
| Declaration docstrings | 0 captured | Reader descriptions are navigation aids, not source-authored theorem explanations. |
| Fine-grained call/type/coercion/instance edges | not captured | Generic compiled-use edges are shown; the four finer categories are deliberately not guessed. |

The source map does not capture declaration docstrings or every elaborated type. Those fields remain explicit `null` in the JSON graph. A human-readable translation therefore distinguishes syntax-level notation, exact environment types, and unresolved semantic obligations. The repository review should not convert any of these metadata gaps into a claim about mathematical invalidity without a declaration-level theorem or counterexample.

Companions: [interactive architecture map](REPOSITORY_ARCHITECTURE_MAP.html), [module explanations](LEAN_MODULE_EXPLANATIONS.md), [declaration index](LEAN_DECLARATION_INDEX.md), [review method](REVIEW_MAPPING_METHOD.md), [raw graph](../NavierStokesReview/evidence/repository_audit_graph_2026-09-26.json), and [full exact-type graph](../NavierStokesReview/evidence/repository_audit_graph_2026-09-26_full.json.gz).
