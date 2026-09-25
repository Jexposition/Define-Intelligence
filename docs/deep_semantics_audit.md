# Deep Semantics Audit Log

## Verification correction: residual force regularity

The force is indeed constructed from a traced residual of already supplied velocity and pressure fields. However, the source does not make `force_smooth` an unconditional smoothness assertion: `CandidateFromLimits.tracedResidual_smooth` requires pre-singular regularity and locally uniform residual-jet limits, and the force also depends on away-extension premises. The audit target is whether those hypotheses are proved for the selected fields. This is stronger and more precise than calling the final theorem a tautology.

## 1. The Tensor Index Hole Search
**Target Files Analyzed:** All files exceeding 1,000 lines (e.g., `EulerProof.lean`, `CorrectionState.lean`, `CorrectionInitialization.lean`) and key structural modules (`PeriodicSobolev.lean`, `FiveRowRank.lean`, `CandidateFromLimits.lean`).
**Search Criteria:** `Fin.cast`, `Fin.cases`, array coercions, and structural downcasts from 5D to 3D.
**Findings:** 
* **Zero instances** of illegal index casting to drop off-diagonal terms.
* In Lean 4, the convective term `(u · ∇)u` is rigorously hardcoded in `ProblemStatement.lean` as `spatialDerivative u t x (u (t, x))`, which expands to all 9 terms of the $3 \times 3$ Jacobian.
* Because Lean's kernel checks equality by strict algebraic reduction (definitional equality), any internal helper lemma that dropped an off-diagonal term would fail to unify with the rigid global `navierStokesResidual` definition.
* **Verdict:** The tensor math is intact. There are no index holes or artificial term-dropping coercions.

## 2. Parameter Drift Analysis (Variable Shadowing)
**Target Parameters:** `selectedBudget`, `selectedThreshold`, `geometricThreshold`.
**Search Criteria:** Local `variable` declarations shadowing global parameters within large induction loops.
**Findings:** 
* A global scan of `ActualCandidateAssembly.lean`, `LocalScheduleWitness.lean`, and `LocalPotentialRebundle.lean` tracks `selectedBudget` through its entire lifecycle.
* Lean 4 strictly enforces variable contexts. Any local `variable (selectedBudget : ℝ)` that shadows an outer variable triggers a compiler warning or requires explicit namespacing. The parameters are passed explicitly as continuous functional arguments to the `StageEstimates` structures, rather than floating globally.
* `geometricThreshold` and `selectedThreshold` are structurally locked into the bounding integrals before the induction loops begin. There is no instance of them being locally overridden to `0` or `1`.
* **Verdict:** There is no parameter drift or variable shadowing. The parameters are conserved strictly across file boundaries.

## 3. Internal Tautology Detector
**Target File:** `CandidateFromLimits.lean` (223 lines).
**Search Criteria:** Algebraic circularity where velocity `u` and pressure `p` are defined in terms of each other, or where `force` is circularly defined to construct `u`.
**Findings:**
* **Line 28 (`tracedResidual`):** Extends the residual of `u` and `p`.
* **Line 82 (`force`):** Defines the external force strictly as `SpacetimeGluing.smoothExtension 1 (tracedResidual u p L)`.
* **Line 172 (`candidate_properties`):** Takes `u` and `p` as **given inputs** (via `CandidateProperties (activatedVelocity u) (activatedPressure p) (force u p ...)`). 
* The velocity field `u` is entirely constructed in `GermCandidateAssembly.lean` (via `potentialSum_eq_base_germ`) *before* the force is ever calculated.
* **Verdict:** There is no algebraic circular loop. The architecture is strictly sequential: 
  1. Construct singular `u` and `p`.
  2. Prove their limits evaluate to 0 (`VanishingJointJets`).
  3. Define `force := R(u, p)`.
  Because step 1 does not reference step 3, it is mathematically valid (this is exactly the Residual-Feedback Exploit we confirmed earlier).

---
### Summary
The Deep Semantics Audit confirms that the inspected FFI perimeter contains no
tensor truncation, variable shadowing, or circular algebraic loop. That is not
a certification of the complete CMI claim. The force result remains conditional
on the selected residual limits and extension data. The live objections are
the **Specification Drift (Missing Moment Transport Glue)** and the absence of
an absolute pressure-semantic bridge in the comparison interface.

The selected-closure census fixes the scope of that objection. The closure
rooted at `ActualCandidateAssembly.lean` reaches 507 local modules and contains
the upstream five-moment and rank machinery. The remaining issue is not an
algebraic circularity or a dead subsystem; it is the absence of an exposed
selected-field equality carrying the paper moments into the final residual and
force chain.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Source-trace correction: the five-moment machinery is active upstream

The 507-module selected closure reaches `PositiveOrderMoments`,
`GlobalSlowProfiles`, `AssembledSlowBase`, `FiveProfileMoments`, and
`FiveRowRank`. In particular, `PositiveOrderMoments.lean:76-85` defines the
five integrated rows, `GlobalSlowProfiles.lean:1043-1055` proves their
positive-order cancellation, and `AssembledSlowBase.lean:592-617` consumes
that result. The record therefore does not support a dead-code or absent-formula
objection.

The remaining load-bearing gap is at the selected mixed-field boundary:
`ActualCandidateAssembly.lean:515-523` assembles the final potential and
pressure fields, while `1121-1151` exports the `Witness` contract without a
field-level equality carrying the paper moments into the residual and force
claims. The publication verdict remains **NOT ESTABLISHED**, because the
paper markets those moments as part of the solution mechanism and the selected
endpoint does not expose their realisation.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.

## Selected Cartesian-to-radial checkpoint

The selected path contains substantive stage data and local moment
preservation. The unresolved semantic step is narrower and more concrete:
`barMoment` consumes scalar radial profiles, whereas the exported witness
contains Cartesian fields assembled by curl and `tsum`. The audit must now
evaluate the selected finite prefix, cutoff derivatives, and axis/tail terms.
No nonzero remainder is recorded until a Lean theorem identifies the resulting
profile with the selected field.

## Selected scalar moment result

The selected-cycle path now has a zero-sorry `barMoment` result for its scalar
mean profiles. This is a positive source fact and rules out a stage-iteration
leak as the explanation for any future mismatch. It does not settle the
Cartesian endpoint: the angular coefficient is transformed by the physical
atlas and frame before localisation and curl. The next contradiction target
must therefore be a proved field-level projection or boundary remainder, not a
generic claim that the moment system is absent.

Evidence: `NavierStokesReview/evidence/selected_scalar_barMoment_transport_2026-09-25.md`.

The selected radial section is now source-backed: component one recovers the
scalar angular coefficient for `r > 0`, while the axis is a separate zero-frame
branch. This narrows the remaining semantic question to the full selected
field composition rather than a generic coordinate objection.

The axis case is now proved for the selected direct stages: the first angular
component is exactly zero when the radial coordinates vanish. This is a
totalisation branch in the source, not a claim that the off-axis field fails to
extend smoothly. The unresolved semantic test remains the full radial moment
of the curl-generated mixed field.
