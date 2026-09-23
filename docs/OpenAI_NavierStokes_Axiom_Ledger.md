# Axiom and Assumption Ledger for the Navier–Stokes Review

**Purpose.** This ledger separates foundational Lean axioms, project declarations, theorem premises, interface contracts, and unresolved analytic obligations. “Axiom” is used narrowly for a declaration accepted without a proof term. A theorem premise or structure field is not automatically an axiom, but it can still be proof-relevant and must be audited.

**Audited snapshot:** upstream commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.
**Review branch:** `review/cmi-first-navier-stokes-2026-09-22`.

## 1. Verdict convention

| Label | Interpretation |
|---|---|
| **Kernel-foundational** | Standard Lean foundation used by ordinary formal mathematics. |
| **Declared project assumption** | A project-level declaration or admitted proof that must be exposed and justified. |
| **Interface premise** | A hypothesis supplied to a theorem or construction; its provenance must be traced. |
| **Proved source fact** | A proposition with a proof term in the audited source. This does not by itself establish that the proposition models the intended mathematics. |
| **Open obligation** | The present audit has not yet shown that the assumption is discharged on the selected path. |

## 2. Foundational kernel axioms

The project’s prior axiom reports identify the ordinary Lean foundations:

| Name | Role | Disposition |
|---|---|---|
| `propext` | Extensionality of propositions. | Kernel-foundational; not a project-specific Navier–Stokes assumption. |
| `Classical.choice` | Choice used by classical analysis and noncomputable constructions. | Kernel-foundational; its use does not make a theorem numerical or executable. |
| `Quot.sound` | Soundness of quotient identification. | Kernel-foundational. |

The review archive contains independent Lean 4.34.0-rc2 reports for the headline Navier–Stokes and Euler exports showing only these standard axioms. A clean rebuild and recapture from the current environment remains a reproducibility task. The archived reports establish the formal trust footprint of those exports; they do not establish the analytic truth of every imported premise.

## 3. Project declarations and admitted gaps

The source-level scan of the actual Navier–Stokes tree found no project declaration using the keywords `axiom`, `admit`, or `unsafe` in the load-bearing Navier–Stokes construction. The public tree does, however, retain four lexical `sorry` occurrences in the challenge area:

| Location | Nature | Relevance to headline theorem |
|---|---|---|
| `ComparatorChallenges/NavierStokes.lean` | Two intentional challenge stubs. | Must be checked for imports; not currently shown to be on the headline path. |
| `ComparatorChallenges/Euler.lean` | Two intentional challenge stubs. | Must be checked for imports; not currently shown to be on the headline path. |

The correct conclusion is therefore not “the repository contains no `sorry`.” The correct question is whether any admitted declaration is reachable from the claimed theorem. That reachability audit remains required.

## 4. Proof-relevant interfaces

### 4.1 Candidate properties

`CandidateProperties` packages the selected fields and their regularity, support, divergence, PDE, initial-data, energy, and endpoint consequences. It is a specification structure, not a proof of its own fields. Each field must be traced to the finite-stage construction or to a proved analytic lemma.

### 4.2 Finite-stage estimates

`StageEstimates` contains finite-background and finite-residual rate information used by the generic candidate assembly. The generic assembly is conditional on this object. The selected path is more specific: `GluedStageEstimates.actualStageEstimates` constructs a `StageEstimates` object from `ActualCycleResidualBounds.PhysicalData`, and `Invariant.residual_jetRate` derives the residual estimate from the invariant, native residual bound, and local/exterior field germs.

**Disposition:** the earlier statement that the headline theorem simply assumes its own final rate bound is not supported by the current dependency trace. The invariant-to-rate derivation is still a load-bearing analytic obligation.

### 4.3 Physical data and germs

`PhysicalData` contains local smoothness, field-germ, and exterior-equality information used to produce the selected residual bounds. The audit must verify that these fields are strong enough for the claimed global smoothness and decay, rather than treating the structure name as evidence of a completed PDE argument.

### 4.4 `JetRate`

`NavierStokes/DiagonalResidual.lean` defines a rate predicate of the form

```lean
∃ C, 0 ≤ C ∧ ∀ᶠ x in l,
  ‖iteratedFDeriv ℝ m f x‖ ≤ C * q x ^ r
```

No `NeBot l` hypothesis is part of this definition. Consequently, on `Filter.bot`, the eventual inequality is vacuous and `JetRate` can be proved for arbitrary data. The zero-sorry probe `NavierStokesReview/src/probes/JetRateVacuityProbe.lean` confirms this semantic fact.

This is a specification hazard, not yet a refutation. The selected endpoint filter `originPast` is separately proved nontrivial. The derived filter used by the selected residual path, `GlobalBaseError.originPast ⊓ 𝓟 activeᶜ`, still requires a direct non-vacuity proof or a proof that the theorem does not rely on a vacuous branch.

### 4.5 Force definition

`CandidateFromLimits.lean` defines the force through `SpacetimeGluing.smoothExtension 1 (tracedResidual u p L) ...`. On the active interval `0 ≤ t < 1`, the source identifies the force with the activated momentum residual. The source only proves the force is zero for `t ≤ 0` and `t ≥ 2`.

This is compatible with a literal forced C/D statement if smoothness and decay are proved. It is not evidence of autonomous, unforced blow-up, and no causal-independence condition appears in the force predicate inspected by the review.

### 4.6 Five-row moment repair

The five-row construction is real and imported into the actual path. The rows are ordered around the debt variables `(P, Jθ, Jz)` and include:

1. `∫ R² dv = 0`;
2. `∫ R ga = 0`;
3. a pressure row `∫ (2*V/R) * dv = -d0`;
4. an angular row `∫ R² * (G*dv + V*ga) = -d1`;
5. an axial row `∫ (2*R*G*ga - R*V*dv) = -d2`.

`FiveRowRank.lean` provides determinant and invertibility facts. No row-drop error has been located. The paper must describe these rows using their actual Lean definitions and must not replace them with the unqualified phrase “zero angular momentum” unless the relevant equivalence is proved.

### 4.7 Pressure hierarchy

The actual source contains pressure recovery, pressure flux, Riesz, whole-space uniqueness, and comparison-closure modules. The absence of earlier cited filenames such as `Pressure/LerayProjection.lean` is a path discrepancy, not a proof of missing pressure machinery. The remaining question is whether the hypotheses of the pressure and uniqueness lemmas are discharged by the selected candidate.

## 5. External mathematical conditions not encoded by the inspected predicates

The following are review criteria, not automatically Lean axioms:

- causal or functional independence of the force from the constructed velocity;
- stability under Ladyzhenskaya non-Newtonian stress laws;
- validity in a hypo-dissipative regime with exponent below one;
- physical interpretability of a residual-defined force;
- human intelligibility and independent mathematical verification.

Their absence does not refute a literal forced C/D theorem. It does prevent the source from being described as a proof of spontaneous unforced Navier–Stokes blow-up or as a physically robust singularity result.

## 6. Ledger conclusion

The present ledger finds no confirmed custom axiom or valid Lean contradiction on the headline path. It does find proof-relevant interfaces and a genuine bottom-filter vacuity hazard that require resolution. The appropriate global status is **CLAIM NOT ESTABLISHED**, pending a clean kernel report and completion of the selected-path non-vacuity and analytic-hypothesis audits.
