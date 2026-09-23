# The Final Dependency Closure Validation Ledger
**Target Modules:** `NavierStokes/R3/Theorem.lean`, `NavierStokes/R3/ActualCandidate.lean`, Import Graph History

## Verification correction: existential assembly is not a hollow proof

The selected theorem does unpack a generic existential witness, but that is the
declared `Witness` interface. `ActualCandidateAssembly.selected_witness` is
constructed from the actual stage-estimate and germ/residual chain before it
is consumed by `R3/ActualCandidate` and `R3/Theorem`. The unpacking operation
does not establish that the fields are geometrically fake.

The defensible finding is narrower: the selected public witness does not expose
the paper's five named moments as a field, and the selected residual interface
does not visibly import `FiveRowRank` as a semantic identity. That is a missing
paper-to-code bridge, not proof of a compiler illusion.

## 1. The Hollow Type Inhabitation Proof
**Target Definitions:** `selected_candidate_one_with_initial_rest` (Line 148 of `NavierStokes/R3/ActualCandidate.lean`) and `theorem_1_1_with_initial_rest` (Line 32 of `NavierStokes/R3/Theorem.lean`).
**Analysis:** 
The final proof structure explicitly unpacks the constructed variables using the `obtain` tactic:
`obtain ⟨a, _, ea, eb, ep, forcing, hc, hf, _⟩ := ActualCandidateAssembly.selected_witness`
* **The Compiler Acceptance:** The Lean 4 compiler accepts this unpack purely because `selected_witness` successfully inhabits the `Witness` existential type. 
* **The actual limitation:** The public witness does not expose a theorem
  identifying its fields with the paper's five named moments or with a
  `FiveRowRank` matrix. That is a missing semantic bridge, not a hollow
  existential assertion or evidence that the geometry is fake.

## 2. The Explicit Import Graph Closure
**Target Interface:** The unbroken import chain from the final theorem to the realization core.
**Analysis:** 
The exact file chain is:
`Theorem.lean` ➔ `ActualCandidate.lean` ➔ `ActualCandidateAssembly.lean` ➔ `ActualCycleResidualBounds.lean` ➔ `PhysicalResidualJetBounds.lean`.
* **The transport gap:** Across this inspected import chain, no direct
  inclusion or merging of `FiveRowRank.lean` was found.
* **The interface boundary:** `selected_witness` is consumed as a generic
  `CandidateProperties` structure. This hides the construction history from
  the public endpoint, but does not prove that the underlying fields violate
  the PDE or that every moment constraint was discarded. The missing item is
  an explicit theorem exposing and transporting the paper's five moments.

## 3. The Chronological Override Statement
**Target History:** Git chronolog of `WholeDomain*` dead code branch (CTR-011).
**Analysis:** 
A review of the repository's git commit timestamps confirms a deliberate architectural override.
* **The Abandonment:** The `WholeDomain*` branch (e.g., `WholeDomainStageBounds.lean`, `WholeDomainPhysicalStageTheorem.lean`) was created on `2026-09-10`. 
* **Correction:** The import separation shows that some `WholeDomain*`
  modules are not on the selected-witness path. It does not establish motive,
  chronology, abandonment because of failed physics, or a purely topological
  result. Those claims require evidence beyond file timestamps and are not
  used in the active verdict.

***
### Dependency Validation Summary
The validated conclusion is narrower: the final public witness does not expose
the paper's five-moment realisation as a selected-path theorem. Its pressure
comparison infrastructure likewise does not expose an absolute global
Poisson representative for the selected pressure. These are material
paper-to-code correspondence objections. They are not irrefutable formal
disproofs, and they do not establish that the endpoint contains no 3D
Navier–Stokes fields.
