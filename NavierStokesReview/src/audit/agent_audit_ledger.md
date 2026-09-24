# Navier-Stokes Claimed Proof Rigorous Audit Ledger

## 1. Goal
Rigorously review the source code comprising OpenAI's Navier-Stokes claimed proof. The primary objective is to verify structural integrity, scrutinize the mathematical foundations, and structurally falsify any claims that do not correspond between the documented mathematics and the Lean 4 formalization.

## 2. Methodology
- **File-by-file Semantic Review**: Tracing the mathematical models through their Lean representations, specifically the `ActualCandidateAssembly` dependency chain.
- **Axiom and Dependency Analysis**: Investigating whether unapproved axioms or 'sorry' statements bleed into the final exported candidates (`ActualCandidateAssembly.selected_witness`).
- **Endpoint Transport Verification**: Focusing on whether the paper-described mechanisms (e.g., the 5-dimensional moments) structurally correspond to the implemented endpoint data (the 3-dimensional debt).

## 3. Findings

### Finding 1: Type Disconnection in Repair Mechanism
- **Location**: `NavierStokes/ActualCandidateAssembly.lean` -> `NavierStokes/CorrectionState.lean` -> `NavierStokes/FiveRowRank.lean`
- **Status**: Correspondence gap; not a formal refutation
- **Description**: The paper claims a 5-dimensional moment repair defined by `(M, I, J, S, Cp)`. The repository provides a module for this (`PositiveOrderMoments.lean`). However, the actual endpoint relies on `CorrectionState.debt`, which is strictly a 3-dimensional quantity `Fin 3 → ℝ` representing `(P, Jθ, Jz)`. No theorem within the endpoint's dependency closure identifies the 5-dimensional moments with the 3-dimensional debt, meaning the paper's mechanism is not actually proven to be the one operating on the selected candidate. 
- **Evidence**: `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean`; the
  selected-path transport theorem remains open.

### Finding 2: Verification of Endpoint Properties
- **Location**: `NavierStokes/CandidateProperties.lean`, `NavierStokes/TimeLocalization.lean`
- **Status**: Verified Valid (No Sleight of Hand Found)
- **Description**: I reviewed the formal definitions of `SpeedUnboundedAtOne` and the construction `activatedVelocity(t) = timeSwitch(t) * u(t)`. 
  - The `timeSwitch` is correctly defined as `0` for $|t| \le 3/8$, satisfying the `zero_initial_velocity` constraint trivially and correctly matching `navier_stokes` at $t=0$ if the force is zero.
  - The cutoff smoothly scales to `1` near $t=1$, preserving the L-infinity `SpeedUnboundedAtOne` blowup.
  - The equations rely on standard smooth limits and standard topology. There is no artificial truncation of the blowup itself.

### Finding 3: Active Subtype Emptiness
- **Location**: `NavierStokes/ActualParticularStageControls.lean` (Line 941)
- **Status**: Verified Valid (No Vacuous Truth)
- **Description**: A potential loophole existed if the endpoint silently assumed the active subtype (`ActivePair B N0`) was inhabited. The review confirms it does NOT. The proof handles the empty case locally via `by_cases hne : Nonempty (ActivePair B N0)` and provides a valid empty bound in the False branch. It is completely safe.

### Finding 4: Axioms and 'Sorry' Bleed
- **Status**: Verified Valid
- **Description**: The four `sorry` placeholders located in `ComparatorChallenges/` do NOT bleed into the main `ActualCandidateAssembly`. The `selected_witness` only relies on `propext`, `Classical.choice`, and `Quot.sound`, which are standard Lean axioms.

## 4. Conclusion
The repository formalizes a forced blow-up proposition under `CandidateProperties`.
The inspected endpoint does not expose a theorem connecting the paper's
five-dimensional moment interpretation (`PositiveOrderMoments`) to the selected
mixed field and residual. That is a correspondence gap, not a kernel-certified
falsification of the endpoint.


## 7. Semantic Gap Audit

Compiled the independent \semantic-gap-audit\ against the current public OpenAI source closure (\9e8bc5\) utilizing Lean \4.34.0-rc2\. The verified compilation yielded zero custom axioms, showing that the semantic bridge from the \ComparatorOptionC/D\ to the CMI \ClaySpec.lean\ is proven entirely on standard Lean foundations (propext, Classical.choice, Quot.sound). No semantic trickery exists in the statement translation.

The verified axiom log is recorded at \NavierStokesReview/results/INDEPENDENT_CLAY_BRIDGE_CURRENT_2026-09-23.txt\.
### Finding 5: Endpoint does not expose the 5D repair payload
- **Location**: `NavierStokes/ActualCandidateAssembly.lean`
- **Status**: Endpoint transport unresolved
- **Description**: The formal endpoint definition for the candidate solution,
  `ActualCandidateAssembly.Witness`, does not expose an equality connecting
  `PositiveOrderMoments.moments` to the selected mixed fields. The repository
  also contains reachable five-moment and rank infrastructure. The source
  therefore establishes an endpoint transport gap, not that the upstream
  five-moment layer is dead code or that the selected endpoint is already
  inconsistent.
- **Evidence**: `src/probes/ActualCandidateAssemblyIsolationProbe.lean`

### Finding 6: Promotion map requires semantic interpretation
- **Location**: `NavierStokes/FiveRowRank.lean` and Implicit Equivalence Maps
- **Status**: Interpretation unresolved
- **Description**: The inspected promotion map inserts two zero coordinates in a
  five-coordinate representation of a three-debt update. This is evidence that
  the map needs a field-level interpretation theorem. It is not, without such
  a theorem, evidence that the selected Cartesian velocity is lower-dimensional
  or that the CMI premises are violated.
- **Evidence**: `src/probes/ManifoldDimensionalReductionProbe.lean`

