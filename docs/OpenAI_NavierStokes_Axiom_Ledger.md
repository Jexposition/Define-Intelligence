# OpenAI Navier–Stokes Axiom and Assumption Ledger

## Purpose

This ledger separates logical foundations, project-level premises, formal definitions, and physical requirements. A standard Lean axiom is not treated as a defect. A proposition imported as a premise, or a definition that is weaker than the paper's object, is a separate audit target.

## 1. Kernel-level foundations

The inspected endpoint reports:

```text
propext
Classical.choice
Quot.sound
```

These are standard Lean foundations. `#print axioms` on `NavierStokesR3.theorem_1_1`, `NavierStokesR3.theorem_1_1_with_initial_rest`, and `NavierStokesR3.ProblemStatement.breakdownStatement` found no named custom axiom. This finding is evidence about dependency hygiene only. It is not evidence that the definitions express the intended PDE construction.

## 2. Declared endpoint objects

`NavierStokes/R3/ProblemStatement.lean` declares:

- smooth velocity and pressure on the pre-singular whole-space domain;
- a globally smooth force with compact positive-time support;
- compact spatial support for each pre-singular slice;
- zero initial velocity, incompressibility, and the Newtonian equation;
- uniform finite energy and unbounded speed approaching time one;
- a global finite-energy comparison statement for the same force.

These declarations are materially closer to the official C/D statement than a periodic model. They must not be misreported as merely toy definitions.

## 3. Project-level assumptions and interfaces

| Interface | What it states | Audit status |
| --- | --- | --- |
| `FiveRowRank.Debt` | Three real residual debts | Abstract type; correspondence to `(P,Jθ,Jz)` and the paper's five cumulative moments is not shown here. |
| `FiveRowRank.FiveRows` | Five integral identities for angular and axial increments | Used by the physical rank-repair pipeline; its relation to `FiveProfileMoments` is not established. |
| `FiveProfileMoments` | Paper-shaped normalised moment map and five coefficient coordinates | Its exponent vectors match Appendix A when `b = -1/2 - λ`; its bridge to `FiveRowRank` is not established. |
| `MeanRankUpdate.physical_five_rows` | Scaled repair functions satisfy `FiveRows` | Formally checked, but only for the Lean row system. |
| `GlobalBaseError.originPast` | A concrete past-neighbourhood filter | Non-vacuity has a probe; downstream derived-filter audit remains open. |
| `JetRate` | A filter-based rate predicate | No `NeBot` parameter; generic `Filter.bot` vacuity is formally demonstrated. |
| `ActualCandidateAssembly.selected_witness` | Selected finite-stage data yield the candidate | Kernel accepted with standard axioms; load-bearing correspondence beneath it remains under review. |

## 4. The coordinate-level contradiction

The official paper's Appendix A gives the normalised intermediate blocks

```text
U: (0, -λ)
E: (1/2, -1/2 - λ, -3/2 - λ).
```

`FiveProfileMoments` gives those same blocks through:

```lean
axialPowers b   := ![0, b + 1 / 2]
angularPowers b := ![1 / 2, b, b - 1]
```

The separate `FiveRowRank` source gives:

```lean
angularPowers lam := ![2, -2 - 2 * lam, -2 * lam]
axialPowers lam   := ![1, 1 - 2 * lam]
```

`MomentCoordinateMismatchProbe.lean` proves the vector inequalities between these two source systems for every real `lam` by evaluating at index zero. This is a genuine zero-sorry theorem. It establishes that the code does not identify the two interfaces by definitional equality, even though one of them matches the paper's normalised blocks.

`MomentBridgeObstructionProbe.lean` strengthens this result. Its `DirectMomentBridge` structure requires both source power vectors to be equal, and `no_direct_moment_bridge` proves that structure impossible for arbitrary `lam` and `b`. The obstruction is therefore not a special-feature failure caused by the paper's substitution; it rules out the direct row-by-row reading of the declarations.

The probe also proves that the two debt spaces have no linear equivalence. `FiveRowRank.Debt` is `Fin 3 → ℝ`, while `FiveProfileMoments.Debt` is `Fin 5 → ℝ`. This is not a proof that no constrained or nonlinear correspondence can exist. It is a zero-sorry obstruction to claiming that the two full debt interfaces are the same linear coordinate space.

The correct conclusion is a missing cross-layer account, not an automatic refutation of every possible rescaling. The source must be credited with `PositiveOrderMoments.weighted_moments_exact`, `moments_repair_target`, and `GlobalSlowProfiles.profiles_moments`, which prove an exact five-coordinate repair in the recursive slow-profile layer. The remaining question is whether that layer is explicitly connected to the nominal `FiveProfileMoments` debt and to the later `FiveRowRank` physical inputs. `SelectedDependencyAxiomProbe.lean` confirms that the selected witness and stage-estimate interfaces do not rely on a visible custom axiom, so the remaining adverse target is semantic correspondence rather than kernel admission. Without an explicit staging and correspondence account, the public claim that the complete mixed pipeline directly verifies one coherent Appendix A system is unsupported.

## 5. Physical requirements that are not kernel axioms

The following are relevant to scientific interpretation but are not silently promoted to formal contradictions:

- a posteriori residual forcing versus an autonomous driver;
- stability under Ladyzhenskaya non-Newtonian stress;
- behaviour under fractional hypo-dissipation;
- pressure bounds on unbounded domains;
- smoothness of temporal and spatial cutoffs at the singular time;
- the distinction between Level A stress-cone matching and Level B exact PDE realisation.

Each requires its own theorem or counterexample. None follows merely from the presence of a smooth force in a C/D statement.

## 6. Ledger conclusion

The standard kernel report is not the end of the audit. The selected candidate also carries a substantive, non-axiomatic consequence: its force is nonzero at some time strictly before one. This belongs in the semantic ledger because it describes the witness actually constructed, not an additional axiom.

## 7. Selected-witness force consequence

`NavierStokes/CandidateConsequences.lean` proves

```lean
CandidateProperties u p f →
  ∃ t ∈ Set.Ioo (0 : ℝ) 1, ∃ x, f (t, x) ≠ 0
```

The review probe is `NavierStokesReview/src/probes/ForceActivityProbe.lean`. The proposition is compatible with alternatives (C) and (D), which permit a smooth time-dependent force. It does, however, rule out describing this witness as an autonomous collapse after the force has been removed. That is a semantic correction to the physical narrative, not a new kernel axiom and not, by itself, a CMI contradiction.

The command `lake env lean NavierStokesReview/src/probes/ForceActivityProbe.lean` succeeds, and `#print axioms force_nonzero_before_one_probe` reports only `propext`, `Classical.choice`, and `Quot.sound`.

## 8. Correspondence status

The ledger now distinguishes three claims that must not be conflated:

1. `#print axioms` reports only Lean's standard foundations on the inspected endpoints.
2. The selected force remains active before the singular time.
3. The direct row-by-row identification of the nominal and physical moment declarations is impossible without an additional transformation theorem.

Only the third is a formal correspondence obstruction. None of the three, standing alone, proves that the final C/D proposition is false.

No custom axiom has been found at the inspected headline or selected-witness interfaces. A zero-sorry formal obstruction has been found to a direct identification of the nominal five-coordinate interface with the physical three-debt interface, but a separate exact five-coordinate `PositiveOrderMoments` repair is present and load-bearing. The outstanding question is whether the repository proves the required maps and staging relations among all three layers. Until answered, the claim of complete direct formal verification must be reported as not established.

## 9. Exact shape of the physical five-row predicate

The source-level declaration `FiveRowRank.FiveRows` must be read literally. It takes `Debt := Fin 3 → ℝ`, not a five-coordinate debt. Its conjunction is structured as two fixed zero-moment equations followed by three equations whose right-hand sides are `-(d 0)`, `-(d 1)`, and `-(d 2)`. `FiveRowsStructureProbe.lean` compiles these projections without assumptions beyond the declaration itself.

This is not a contradiction: the first two rows can be invariants established independently, and the source proves them for the constructed bumps. It is, however, a correction to any statement that this declaration alone implements an arbitrary five-equation, five-unknown inverse. The ledger therefore records the issue as a specification and correspondence obligation, not as a final C/D refutation.

## 10. Whole-space endpoint provenance

The whole-space endpoint is not an isolated wrapper around an unrelated witness. `NavierStokes/R3/Theorem.lean` obtains the viscosity-one candidate from `ActualCandidateAssembly.selected_witness`. `NavierStokes/R3/ActualCandidate.lean` then applies the proved spatial localisation, positive-time force cutoff, and compact-support energy estimate. `NavierStokes/R3/ViscosityScaling.lean` transports the candidate from viscosity one to every positive viscosity and proves the residual scaling identity.

This closes a separate provenance objection: the R³ theorem is connected to the selected construction at source level. It does not close the moment objection. The endpoint provenance passes through interfaces whose physical meaning still depends on the missing correspondence account among `FiveProfileMoments`, `PositiveOrderMoments`, and `FiveRowRank`.
