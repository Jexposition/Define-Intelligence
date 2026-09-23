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
