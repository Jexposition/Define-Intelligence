# CMI-First Review Plan for the OpenAI Navier–Stokes Formalisation

## 1. Objective

Determine, by direct inspection of the Lean source and its mathematical interfaces, whether the OpenAI release establishes a valid solution to the Clay Mathematics Institute Navier–Stokes problem. The review must distinguish:

1. what the Lean kernel checks;
2. what proposition the source actually states;
3. whether the selected construction supplies the premises of that proposition; and
4. whether the proposition corresponds to the claimed Clay alternative.

The target is not compilation alone. A successful compile is evidence about elaboration and kernel acceptance; it is not evidence that the formal definitions encode the intended PDE argument.

## 2. CMI criteria

The review uses the written Fefferman formulation as the primary specification. It must classify the result against all four alternatives rather than silently treating a forced construction as an unforced one.

| Alternative | Core question | Review requirement |
|---|---|---|
| A | Global smooth solution for unforced flow on `R³`. | Verify `f = 0`, all-time regularity, energy bounds, and the exact domain. |
| B | Global smooth solution for unforced periodic flow. | Verify periodicity, `f = 0`, and all-time regularity independently of A. |
| C | Breakdown for a smooth decaying force on `R³`. | Verify force class, PDE, initial data, divergence constraint, energy, and finite-time breakdown. |
| D | Periodic forced analogue. | Verify the periodic forced theorem separately. |

The official statement may permit smooth external forcing in C and D. Therefore “the force is engineered” is not by itself a formal mismatch with C or D. It is a causal and interpretive objection unless the formal force fails the stated smoothness, support, or decay conditions.

## 3. Evidence classes

Each conclusion receives one evidence label:

- **Kernel evidence:** theorem declaration, proof term, `#print axioms`, and import reachability.
- **Source-semantic evidence:** definitions, quantifiers, domain types, support predicates, and interface fields.
- **Mathematical adequacy evidence:** proofs that the constructed fields satisfy the analytic hypotheses used by the interfaces.
- **Interpretive evidence:** relation to autonomous dynamics, physical forcing, altered constitutive laws, and human-readable mathematical meaning.

Interpretive evidence may limit the claim, but it must not be presented as a Lean counterexample. Conversely, a kernel theorem cannot be treated as a mathematical solution until source-semantic and adequacy checks are complete.

## 4. Work packages

### WP-1: Provenance and reproducibility

Record the upstream commit, review-branch commits, file manifests, archive hashes, Lean toolchain, Mathlib revision, and Comparator revision. Keep the pinned 4.34.0-rc2 build distinct from the user-requested 4.32 package environment.

**Exit condition:** another reviewer can identify the exact source tree and reproduce each reported command.

### WP-2: Statement and quantifier audit

Trace `ProblemStatement`, `ComparatorDefinitions`, `ComparatorSolution`, `R3/Theorem`, and the periodic theorem. Construct a table for domain, time interval, viscosity, pressure, velocity, force, initial data, divergence, energy, decay, and singularity clauses.

**Exit condition:** every clause in the claimed C/D theorem is mapped to an explicit Lean proposition, with no inference from names or comments.

### WP-3: Candidate-construction audit

Trace `ActualCandidateAssembly` through `GermCandidateAssembly`, `GluedStageEstimates`, `ActualCycleResidualBounds`, `PhysicalData`, and the finite-stage invariant. Verify whether every rate and regularity field is constructed or merely passed as a premise.

**Exit condition:** a complete dependency diagram from finite-stage data to `CandidateProperties`.

### WP-4: Force and causality audit

Inspect `CandidateFromLimits` and the residual trace. Prove the exact intervals on which the force is zero, active, or identified with the residual. Audit smooth extension at the temporal cutoffs and derivative decay at spatial infinity. Separately record that no causal-independence predicate is present.

**Exit condition:** a formal force timeline and a classification as literal C/D compliance, causal concern, or actual predicate failure.

### WP-5: Filter and asymptotic audit

Audit every `JetRate` consumer. Add zero-sorry probes for bottom-filter vacuity, endpoint non-vacuity, and the exact derived filter in the selected path. Determine whether a bottom filter is possible and whether any headline theorem consumes a proposition that becomes vacuous there.

**Exit condition:** either a proved `NeBot` result for every load-bearing filter or a formally demonstrated vacuity path.

### WP-6: Moment, pressure, and PDE interface audit

Map the five moment rows, determinant/invertibility facts, pressure recovery, pressure flux, Riesz hierarchy, whole-space uniqueness, and comparison closure. Test that the hypotheses are attached to the correct functions and domains.

**Exit condition:** no unexplained interface boundary between stress matching, exact velocity construction, residual flattening, pressure recovery, and final non-existence.

### WP-7: Axiom and contradiction audit

Run `#print axioms` on the headline exports under the pinned toolchain. Search actual imports for `sorry`, custom axioms, and admitted declarations. If a proposition mismatch is found, write the smallest zero-sorry Lean witness that derives the contradiction or exhibits the vacuity. Do not add a theorem that merely restates a criticism in prose.

**Exit condition:** every stronger negative claim is backed by a source proposition, a reproducible command, and, where possible, a checked Lean witness.

## 5. File-to-question map

| Review question | Primary files | Required result |
|---|---|---|
| What is claimed? | `ComparatorDefinitions.lean`, `ComparatorSolution.lean`, `R3/Theorem.lean` | Exact theorem and alternative classification. |
| Is the force admissible? | `CandidateFromLimits.lean`, `ComparatorBridge.lean`, `CompactSpatialForceDecay.lean` | Smoothness, support, decay, and force timeline. |
| Is the candidate actually constructed? | `ActualCandidateAssembly.lean`, `GermCandidateAssembly.lean`, `GluedStageEstimates.lean` | Interface-premise provenance. |
| Can asymptotics be vacuous? | `DiagonalResidual.lean`, `ActualCycleResidualBounds.lean`, review probes | Non-vacuity or checked vacuity path. |
| Are moments repaired? | `FiveProfileMoments.lean`, `LocalizedMomentRepair.lean`, `FiveRowRank.lean` | Row-by-row semantic mapping and rank audit. |
| Is pressure closed? | pressure recovery, pressure flux, Riesz, uniqueness, comparison files | Hypothesis and domain closure. |
| Does the result reach CMI? | `PeriodicPaperTheorem.lean`, `PeriodicPaperComparator.lean`, R3 comparator files | Separate C and D dispositions. |

## 6. Contradiction protocol

A formal disproof is warranted only when the source exposes a proposition that cannot meet the claimed criterion. The sequence is:

1. isolate the exact definition or theorem;
2. identify the missing, false, or vacuous condition;
3. write the smallest zero-sorry Lean probe;
4. verify whether the probe is on the headline dependency path;
5. state the result as a formal failure only if reachability and relevance are proved.

The `JetRate` bottom-filter theorem already establishes a real local semantic hazard. It does not yet establish that the selected candidate theorem is vacuous. The next formal target is the exact `originPast ⊓ 𝓟 activeᶜ` filter.

## 7. Acceptance criteria

The review can declare the claim formally established only if the source supplies a checked theorem whose type matches the intended CMI alternative, all interface premises are discharged on the selected path, no relevant admitted declaration is reachable, every load-bearing asymptotic filter is nontrivial, and the force/domain/regularity conditions are exact.

The review can declare a formal failure only if a checked contradiction, a reachable admitted gap, a false theorem premise, or a proposition-to-criterion mismatch is demonstrated. Otherwise the correct status is **NOT ESTABLISHED**, with the unresolved obligations named explicitly.

## 8. Deliverables

- this plan as the method and acceptance standard;
- the axiom ledger as the assumption inventory;
- the audit tracker as the evidence and status record;
- `OpenAI_NavierStokes_Peer_Review_v1.md` as the formal referee report;
- `OpenAI_NavierStokes_Research_Paper.md` as the human-readable synthesis.
