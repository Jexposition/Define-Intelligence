# Germ Geometry Core Extraction Ledger

## Verification correction: scope of the geometry claim

The direct import observation is valid: `GermCandidateAssembly.lean` does not import `PositiveOrderMoments` or `FiveProfileMoments`. The stronger conclusion that the selected construction is entirely independent of five-moment machinery is not valid, because the active upstream chain reaches that machinery through `GlobalSlowProfiles`, `NominalProfile`, and `ModulatedProfileAssembly`. The defensible finding is narrower: the generic germ/summation interface does not expose a theorem transporting the five named physical moments into the selected endpoint.

## 1. The Geometric Specification Drift (The Component Count)
**Target Definition:** `potentialSum_eq_base_germ` (Lines 75-96 in `GermCandidateAssembly.lean`)
**Analysis:** 
Your hypothesis correctly anticipated a semantic shift, but the reality is even starker. `potentialSum_eq_base_germ` is **not** an algebraic vector construction lemma; it is a purely topological equivalence theorem.
* **Component Count Evaluated:** **Zero explicit components.** The lemma does not build a 3D matrix, a `Triple`, or any geometric vectors. It operates entirely on abstract functions of type `VelocityField` (which maps `SpaceTime → Space`). 
* **The Mechanism:** The lemma merely proves that because the `initial` and `stages j` fields are constructed to be strictly zero in a neighborhood of the origin (via `hInitial` and `hStages`), the infinite sum `SolenoidalDiagonal.potentialSum` collapses algebraically to exactly the `base` germ near the origin. 
* **Corrected verdict:** The lemma is agnostic about component formulas because its type is `VelocityField`. The three-dimensional geometry is supplied upstream by `TailGaugePotential.finalPotential` and the solenoidal/curl construction. Thus the lemma proves localisation of the series, not omission of cross-components. Its audit consequence is narrower: the localisation lemma carries no five-moment payload.

## 2. The Holomorphic/Analytic Envelope (The Scaling Factor)
**Target Definition:** `exists_candidate_witness_of_finite_stages` (Lines 164-271 in `GermCandidateAssembly.lean`)
**Analysis:** 
The series convergence does **not** rely on a hard-coded geometric decay rate (like $2^{-j}$). Instead, it uses a dynamically generated, infinitely accelerating sequence.
* **The Scaling Factor (`ar : ℕ → ℝ`):** At Line 225, the scale is defined as `let ar : ℕ → ℝ := fun j => (a j : ℝ)`.
* **The Bounding Lemma:** The sequence `a j` is forcibly extracted from `E.exists_schedule` (Line 224), which takes the `StageEstimates` (the massive inductive bounds proven in earlier files) and generates an integer sequence that guarantees the supports of the fluid stages shrink fast enough to sum cleanly.
* **Corrected verdict:** The schedule is selected to satisfy analytic estimates; it is not evidence of physical energy dissipation. No invalidity follows from the schedule alone. The live question is whether the selected schedule also preserves the paper's five moment identities and the residual estimates required by the PDE interpretation.

## 3. The Missing Balance Refutation
**Target Cross-Reference:** `GermCandidateAssembly.lean` vs. `PositiveOrderMoments.lean`
**Analysis:** 
I executed a strict dependency search for `PositiveOrderMoments` within the import closure and namespace of `GermCandidateAssembly.lean`.
* **Occurrences Found:** **Zero.**
* **Verdict:** `GermCandidateAssembly` compiles its infinite series (via
  `potentialSum_eq_base_germ` and `exists_candidate_witness_of_finite_stages`)
  without directly importing or invoking the five-moment evaluation functions.
* **Conclusion:** This supports CTR-005 in its narrower form: the generic germ
  interface does not expose a theorem transporting the named five moments into
  the selected velocity and residual endpoint. The import closure nevertheless
  reaches five-moment modules upstream, so this is not evidence that those
  modules are dead code or that the final field is independent of them.

*** 
### Extraction Summary
This extraction isolates a review target. Topological localisation
(`potentialSum_eq_base_germ`) and the schedule theorem (`E.exists_schedule`)
construct the germ and convergence interfaces, while the selected path also
contains upstream five-moment machinery. The remaining question is whether an
explicit selected-path theorem connects those moments to the physical residual;
the present note does not establish an architectural severing.
