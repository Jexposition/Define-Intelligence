# What the OpenAI Navier–Stokes Formalisation Establishes

## Abstract

This paper examines the public Lean 4 formalisation released with OpenAI’s claimed finite-time Navier–Stokes breakdown construction. The central question is not whether the repository compiles. It is whether the propositions accepted by Lean, together with their definitions and interfaces, establish the mathematical claim made about the Clay Mathematics Institute problem.

The audit finds a substantial formal development whose theorem shape is directed at forced alternatives C and D of the written Fefferman formulation. Existing independent Lean 4.34.0-rc2 reports support the theorem-level formal claim for those forced exports under standard kernel axioms. The construction defines the external force from the momentum residual of a selected collapsing field and keeps that force active through the approach to the singular time. This is materially different from an autonomous, unforced blow-up argument, although residual-defined forcing is not automatically disallowed by alternatives C and D. The source also contains a genuine asymptotic-specification hazard: `JetRate` has no non-vacuity condition and is true on the bottom filter. The selected endpoint filter is nontrivial, but the derived filter used by the residual path remains to be audited.

The five-row moment-repair and pressure infrastructures are present; no row-drop or missing-pressure conclusion has been established. Conversely, the current review has not completed the analytic bridge from those modules to every required global condition. The responsible conclusion is therefore **claim not established**, not **formalisation refuted**.

## 1. Research question

OpenAI’s release is presented as a formal proof of finite-time breakdown for the three-dimensional Navier–Stokes equations. A peer review must answer two different questions:

1. What theorem does the Lean source actually prove?
2. Does that theorem satisfy the written CMI criteria and the mathematical meaning attributed to it?

These questions cannot be answered by compilation alone. Lean checks a proof term against a type. It does not decide whether a definition faithfully captures a PDE concept, whether a supplied interface premise has been established from the construction, or whether a force selected from a solution is physically independent of that solution.

## 2. Scope and source

The audited upstream snapshot is commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`. The independent review is maintained on branch `review/cmi-first-navier-stokes-2026-09-22` in the companion repository. The source is reviewed directly rather than through extracted PDF text or early filenames from secondary notes.

The main source areas are:

- `ComparatorDefinitions.lean` and `ComparatorSolution.lean` for the formal target;
- `NavierStokes/R3/Theorem.lean` and `NavierStokes/R3/ComparatorBridge.lean` for the whole-space route;
- `ActualCandidateAssembly.lean`, `GermCandidateAssembly.lean`, and `ActualCycleResidualBounds.lean` for candidate construction;
- `CandidateFromLimits.lean` for the force and endpoint construction;
- `DiagonalResidual.lean`, `FiveProfileMoments.lean`, `LocalizedMomentRepair.lean`, `FiveRowRank.lean`, and the pressure hierarchy for the load-bearing interfaces.

## 3. The CMI alternatives and the formal target

The unforced alternatives A and B concern global regularity for `f = 0`, respectively on Euclidean space and the periodic domain. The forced alternatives C and D permit a smooth external force subject to the stated decay and domain conditions. A theorem about a forced construction must therefore be classified as C or D unless the source separately proves that the force is identically zero.

The inspected comparator definitions encode smoothness, the Navier–Stokes equations, incompressibility, initial data, integrability, and energy conditions. The whole-space theorem quantifies over positive viscosity and is translated into a forced comparator statement. The periodic route is represented separately and cannot be inferred from the whole-space route.

This establishes the correct formal target: the release is not an A/B proof merely because the velocity becomes unbounded. The relevant question is whether its C/D theorem is complete and correctly connected to the construction.

## 4. The force is an a posteriori residual

In `CandidateFromLimits.lean`, the force is obtained through a smooth extension of the traced momentum residual:

\[
 f = \operatorname{smoothExtension}\bigl(\operatorname{tracedResidual}(u,p,L)\bigr).
\]

On the active interval `0 ≤ t < 1`, the source identifies the force with the activated residual of the selected fields. The source proves that the force is zero for `t ≤ 0` and `t ≥ 2`; it does not prove that the force is switched off on an interval before the singular time `t = 1`.

This has two consequences. First, the construction is a tracking-force construction: the forcing is selected after the candidate velocity and pressure have been specified so that the residual is supplied as the external term. It does not prove autonomous singularity formation. Second, the fact that the force is engineered is not, by itself, a formal violation of C or D, because those written alternatives allow an external force. The decisive internal test is whether the resulting force satisfies every smoothness, support, and derivative-decay condition in the comparator predicate.

The formal predicates inspected in `ComparatorDefinitions.lean` do not include a causal-independence condition requiring `f` to be chosen independently of `u`. That omission limits the physical interpretation of the result, even if the literal forced alternative is eventually verified.

## 5. From finite-stage data to the candidate

The generic assembly uses a `StageEstimates` interface containing finite background and residual rate bounds. It would be an overclaim to say that the final result simply assumes the desired conclusion: the selected path constructs `actualStageEstimates` from `ActualCycleResidualBounds.PhysicalData`. The residual rate is then derived from the invariant, native residual bound, and local/exterior field germs.

This does not remove the audit obligation. It relocates it. The review must verify that the invariant-to-rate derivation supplies all derivative orders, domains, and asymptotic exponents required by the candidate assembly. A structure field named “physical data” is not itself a proof that the intended PDE estimates hold globally.

The relevant distinction is between a conditional construction theorem and a completed application of that theorem. The source contains evidence for the latter’s dependency chain, but the independent audit has not yet discharged every analytic interface.

## 6. The filter non-vacuity problem

The asymptotic predicate `JetRate` is defined in `DiagonalResidual.lean` by an eventual derivative bound:

```lean
∃ C, 0 ≤ C ∧ ∀ᶠ x in l,
  ‖iteratedFDeriv ℝ m f x‖ ≤ C * q x ^ r
```

There is no `NeBot l` hypothesis. In Lean’s filter semantics, `Filter.bot` represents an empty eventuality context. Every eventual proposition holds on that filter. A zero-sorry probe in the review repository proves that arbitrary `JetRate` claims can therefore be constructed when `l = Filter.bot`.

This result is mathematically specific and should not be overstated. It proves a local specification hazard. It does not prove that the headline theorem is vacuous, because the selected endpoint filter `originPast` has separately been shown nontrivial. The remaining load-bearing object is the derived filter used by the residual path,

\[
  \texttt{GlobalBaseError.originPast}\;\sqcap\;\mathcal{P}(\texttt{active}^{c}).
\]

The current source does not yet provide the required direct proof that this exact filter is non-bottom, nor does it establish that the headline theorem is independent of a potentially vacuous branch. This is the strongest current formal audit target. A final negative conclusion requires either a checked bottomness result on the selected path or a proof that the main theorem consumes a vacuous rate proposition.

## 7. Moment repair and the distinction between stress and velocity

The five-row moment infrastructure is present in the actual source path. `FiveProfileMoments.lean`, `LocalizedMomentRepair.lean`, and `FiveRowRank.lean` implement and analyse a five-dimensional repair map. The rows include two normalisation or constraint conditions, a pressure row, an angular row, and an axial row. Determinant and rank results support local invertibility.

The implementation should be described using its actual row definitions. In particular, the paper must not identify the entire system with a single informal phrase such as “zero angular momentum” unless an explicit equivalence is proved. Nor does invertibility alone establish that an exact nonlinear velocity field realises the target covariance while all higher-order PDE residuals vanish.

This is the difference between two levels of claim:

- **Level A:** the target stress or moment data lie in an admissible finite-dimensional repair system;
- **Level B:** the repaired data are realised by a global smooth velocity and pressure satisfying the exact nonlinear PDE and all endpoint estimates.

The Lean modules provide evidence for a Level A mechanism and interfaces toward Level B. The independent review must not silently treat the former as the latter.

## 8. Pressure and source-tree corrections

Early review drafts referred to files such as `Forcing/Smoothness.lean`, `Pressure/LerayProjection.lean`, `Scaling/SingularLimits.lean`, and `EnergyDefect.lean`. Those paths are not present in the audited commit. Their absence is not a proof of missing functionality. The actual source contains pressure recovery, pressure flux, Riesz, whole-space uniqueness, and comparison-closure modules.

The correct question is whether those actual modules have the hypotheses required for the claimed conclusion: whole-space domains, pressure normalisation, energy bounds, comparison fields, and all relevant regularity assumptions. A filename discrepancy is a documentation error and has been recorded as such in the audit tracker.

## 9. Axiom and build status

The ordinary Lean foundations reported for the project are `propext`, `Classical.choice`, and `Quot.sound`. Existing independent reports for the headline exports contain only these standard axioms. These are standard foundations, not evidence that the Navier–Stokes mathematics is correct. The public source also contains four intentional `sorry` occurrences in Comparator challenge files. Their lexical presence does not show that they are imported into the headline theorem; import reachability must be checked.

The repository pins Lean 4.34.0-rc2, while the shared package directory requested for auxiliary work is based on 4.32. The review archive contains independent 4.34.0-rc2 axiom reports for the headline exports, while a clean rebuild and recapture from the current environment remains an explicit reproducibility task. The reports support formal trust of the exported declarations; they do not establish the analytic truth of every imported premise.

## 10. Discussion

Several proposed objections are valuable but have different logical status. Ladyzhenskaya non-Newtonian stress, hypo-dissipative exponents, and physical stability tests examine robustness under altered equations. They are not counterexamples to a theorem whose statement contains only the Newtonian Laplacian. They may nevertheless show that the construction should not be described as a physically universal mechanism.

Similarly, the absence of a causal-independence predicate does not falsify a literal forced C/D proposition. It does show that the proposition is weaker than a claim of spontaneous blow-up and that the force must be described as an engineered external input rather than an emergent physical driver.

The filter issue is different: it concerns the truth conditions of a Lean predicate itself. That is why it is a formal audit target. Yet even here, the correct conclusion depends on the selected filter’s reachability and non-vacuity. A local vacuity theorem is not automatically a global refutation.

## 11. Conclusion

The OpenAI release contains a serious Lean development aimed at a forced Navier–Stokes breakdown theorem. The inspected source does not establish an unforced A/B result. Its force is defined a posteriori from the momentum residual and remains active through the approach to the singular time. The five-row moment and pressure infrastructures are present, and no confirmed row-drop or missing-pressure defect has been found.

The outstanding proof-relevant issues are the exact force-class bridge, the invariant-to-rate construction, the non-vacuity of the selected derived filter, the reachability of admitted challenge declarations, and the complete analytic closure of the pressure and uniqueness interfaces. Until those obligations are resolved, the appropriate scientific statement is:

> **At theorem level, the forced C/D-shaped exports are formally supported. The claim of a verified Clay solution is not established by the present independent audit, and no formal contradiction of the headline Lean theorem has yet been demonstrated.**

This conclusion is deliberately narrower than a rejection of the entire formalisation and stronger than a compilation report. It identifies precisely what is established, what is not, and what would be required for the verdict to change.

## References

1. OpenAI source snapshot, `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.
2. Clay Mathematics Institute, *Existence and Smoothness of the Navier–Stokes Equation*, official problem statement: <https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf>.
3. Review repository documents: `OpenAI_NavierStokes_Audit_Tracker.md`, `OpenAI_NavierStokes_Axiom_Ledger.md`, and `OpenAI_NavierStokes_Peer_Review_v1.md`.
