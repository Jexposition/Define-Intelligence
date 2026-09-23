# Independent Peer Review of the OpenAI Navier–Stokes Formalisation

**Review type:** technical peer review of a formal proof claim
**Audited snapshot:** `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
**Review branch:** `review/cmi-first-navier-stokes-2026-09-22`
**Recommendation:** claim not established; further verification required

## 1. Summary judgement

The release demonstrates a substantial Lean development containing definitions and proof infrastructure for a forced Navier–Stokes breakdown construction. Existing independent Lean 4.34.0-rc2 reports support the theorem-level claim that the exported forced C/D-shaped propositions are accepted with the standard kernel axioms. The source-level theorem shape is consistent with alternatives C and D of the written Clay formulation, in which smooth external forcing is permitted. Compilation and ordinary kernel axioms establish only that Lean accepts the stated propositions under the imported environment.

The present evidence does not establish that the release is a verified solution to the Millennium Prize problem. The principal reasons are not that the code fails to compile and not that every engineered force is disallowed. The reasons are that the correspondence between the constructed fields and the analytic CMI conditions remains incompletely audited, the force is defined a posteriori from the momentum residual, and a genuine vacuity hazard exists in the asymptotic interface.

No valid Lean contradiction against the headline theorem has yet been found. The appropriate recommendation is therefore **claim not established**, not **formalisation refuted**.

## 2. Major comments

### 2.1 The alternative being addressed must be stated precisely

The source should not be described as proving autonomous or unforced blow-up. The unforced alternatives A and B require `f = 0`; the inspected construction instead routes through forced alternatives C and D. The review must keep the R3 and periodic routes separate and must identify the exact force, domain, time interval, decay, energy, and singularity predicates used by each comparator theorem.

This distinction is substantive. A result in C or D could be valid under the written formulation while still failing to establish A or B. It is also possible for a theorem to be C/D-shaped while still failing because its force or regularity bridge is incomplete. Both questions must be answered independently.

### 2.2 The force is residual-defined and active through the collapse interval

`CandidateFromLimits.lean` constructs the force using a smooth extension of the traced momentum residual. On `0 ≤ t < 1`, the source identifies the force with the activated residual. The source proves vanishing for `t ≤ 0` and `t ≥ 2`; it does not establish an interval of deactivation before the singular time `t = 1`.

This corrects the earlier narrative that the force switches off before the blow-up. The construction is therefore a continuously tracking forced evolution through the approach to the endpoint. That fact does not, by itself, contradict C or D, because the written forced alternatives allow a smooth force. It does prevent the result from being presented as a spontaneous singularity of an unforced fluid. The source also does not impose functional independence of `f` from `u`; the force is selected after the candidate fields and residual are specified.

The remaining internal question is exact: does the smooth extension satisfy every derivative and decay clause of the comparator force predicate at the temporal cutoffs and at spatial infinity?

### 2.3 The finite-stage interface is not the same as assuming the final theorem

The generic candidate assembly consumes a `StageEstimates` structure containing finite background and residual rate bounds. A superficial reading could therefore mistake the interface for an assumption of the desired conclusion. The selected path, however, constructs `actualStageEstimates` from `ActualCycleResidualBounds.PhysicalData`; the residual rate is derived through the invariant, native residual bound, and local/exterior germs.

The correct criticism is narrower and stronger: the invariant-to-rate derivation is load-bearing and must be checked field by field. The present audit has not shown that the final candidate theorem simply assumes its own conclusion, and the peer review should not make that claim without a dependency proof.

### 2.4 `JetRate` admits a real bottom-filter vacuity

`DiagonalResidual.JetRate` has the form of an eventual derivative bound over a filter but does not require `NeBot`. On `Filter.bot`, every eventual proposition is true. The zero-sorry probe `JetRateVacuityProbe.lean` proves that arbitrary rate claims can therefore be established on the bottom filter.

This is a formal specification hazard. It becomes a defect in the claimed theorem only if the selected construction uses a bottom derived filter, or if a headline result consumes a rate proposition without proving non-vacuity. The endpoint filter `originPast` has separately been shown nontrivial. The exact selected filter `GlobalBaseError.originPast ⊓ 𝓟 activeᶜ` remains the required target. Until that target is resolved, the filter issue is open rather than a demonstrated refutation.

### 2.5 The five-row moment repair is present, but its meaning must be reported exactly

The source contains `FiveProfileMoments`, `LocalizedMomentRepair`, and `FiveRowRank`, and these modules are imported into the construction. The five rows include two normalisation/constraint rows, a pressure row, an angular row, and an axial row. Rank and determinant facts support invertibility.

No row-drop defect has been found. However, the paper must not collapse the system into an unqualified statement that it proves “zero angular momentum” unless it supplies the exact equivalence between that phrase and the implemented rows. A Level A covariance or moment repair result is not automatically a Level B proof that an exact nonlinear velocity field realises the desired stress with all residuals flattened.

### 2.6 Pressure and path names require direct source tracing

Several early review drafts named files that do not exist in the audited snapshot, including `Forcing/Smoothness.lean`, `Pressure/LerayProjection.lean`, and `Scaling/SingularLimits.lean`. Their absence cannot support a conclusion that forcing, pressure, or singular limits are unimplemented. The actual source contains a pressure recovery and comparison hierarchy.

The correct audit is to inspect the hypotheses of the actual pressure, flux, Riesz, uniqueness, and comparison-closure lemmas, including domains and energy bounds. A path-name mismatch is a documentation error, not a mathematical counterexample.

## 3. Minor comments

1. The four `sorry` occurrences in the Comparator challenge area must be reported with import reachability. A lexical scan alone cannot show that the headline theorem depends on them.
2. A clean current `#print axioms` report should be regenerated under the repository’s pinned toolchain. The existing archived reports should be cited as formal-trust evidence, not as a substitute for a fresh rebuild.
3. The repository’s Lean 4.34.0-rc2 pin must not be conflated with the separate 4.32 package directory used for compatibility probing.
4. Physical tests using Ladyzhenskaya stress laws or hypo-dissipation are valuable robustness questions, but they are not internal Lean failures of the Newtonian forced theorem unless those laws are part of its statement.

## 4. Required revisions and tests

Before a stronger claim is made, the authors or auditors should provide:

- an exact theorem-to-CMI correspondence table for C and D;
- a complete force proof covering smooth extension, support, decay, and the active interval;
- a selected-path proof that every load-bearing filter is nontrivial;
- a dependency report showing whether challenge `sorry` declarations reach the headline theorem;
- a row-by-row moment and pressure audit with all interface hypotheses discharged.

If a missing condition is found, the review should add the smallest zero-sorry Lean witness that demonstrates the mismatch. If no such witness exists, the finding should remain an open audit obligation rather than being promoted to a refutation.

## 5. Final recommendation

The public claim should be described as a formalisation of a forced C/D-shaped theorem whose mathematical adequacy is still under independent review. It should not be described as a verified proof of unforced Navier–Stokes blow-up, nor as a completed solution to the Clay problem. The present peer-review disposition is:

> **CLAIM NOT ESTABLISHED. No formal refutation of the headline Lean theorem has yet been demonstrated.**
