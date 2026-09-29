# Priority 147 source review: external semantic bridge and Euler drift-pressure tranche

Date: 2026-09-29
Scope: direct source review of two audit-semantics files and ten Euler correction, pressure, parity, and residual files.
Method: declarations, imports, theorem bodies, endpoint symbols, and explicit absence checks were read from the current checkout.  This is a source review, not a claim that a file outside the captured Navier-Stokes endpoint closure is dead.

## Files reviewed

Audit semantics:

- `NavierStokesReview/src/external-semantic/ClaySpec.lean`
- `NavierStokesReview/src/external-semantic/Gap.lean`

Euler drift and pressure:

- `Euler/AllOrderDriftEquation.lean`
- `Euler/AllOrderDriftFieldDecomposition.lean`
- `Euler/AllOrderDriftResidualBounds.lean`
- `Euler/CorrectionResidualCancellation.lean`
- `Euler/MeanPressureRepresentative.lean`
- `Euler/PacketAngularPressureStepBound.lean`
- `Euler/PacketFiniteParity.lean`
- `Euler/PacketForwardPressureBudgets.lean`
- `Euler/PacketForwardPressureRemainder.lean`
- `Euler/PacketInitializedPressureRemainder.lean`

## Direct findings

### 1. The audit semantic layer is an explicit bridge, not an OpenAI endpoint

`ClaySpec.lean:28-32` defines the audit-side spaces and fields.  `ClaySpec.lean:53-55` models smoothness as `ContDiffOn ℝ ∞` on the closed nonnegative-time set.  `ClaySpec.lean:88-114` defines spatial and temporal within-derivatives, divergence, the component Laplacian, convection, and equation (1).  `ClaySpec.lean:117-122` defines incompressibility and the initial trace.

The data predicates are explicit:

- `ClaySpec.lean:130-145`: initial divergence-free and rapid-decay conditions, together with joint space-time force decay.
- `ClaySpec.lean:147-165`: spatial periodicity and periodic force decay.
- `ClaySpec.lean:168-171`: a global bounded-energy predicate.
- `ClaySpec.lean:174-195`: the R3 and periodic solution predicates.
- `ClaySpec.lean:197-210`: admissible data predicates.
- `ClaySpec.lean:215-226`: the audit-side alternatives C and D.

`Gap.lean` then proves coordinate and derivative translation lemmas and packages the result into the comparator structures:

- `Gap.lean:274-286`: comparator admissible R3 data imply `ClaySpec.AdmissibleDataR3`.
- `Gap.lean:288-303`: comparator periodic data imply `ClaySpec.AdmissibleDataPeriodic`.
- `Gap.lean:525-541`: component equations are converted into the comparator vector equation.
- `Gap.lean:543-569`: a `ClaySolutionR3` is converted into the comparator existence structure.
- `Gap.lean:571-597`: the periodic analogue is converted, including periodic pressure.
- `Gap.lean:602-617`: comparator-side alternatives C and D are defined.
- `Gap.lean:619-642`: the two statement-level implications are proved and their axioms are printed.

This is useful audit infrastructure.  It does not inspect, import, or prove the OpenAI selected Navier–Stokes witness.  The bridge proves an implication from the audit comparator language to the audit `ClaySpec` language.  It does not establish that `NavierStokesR3.theorem_1_1` inhabits either audit-side alternative, and it contains no five-moment, `barMoment`, `CandidateProperties`, or `selected_witness` transport theorem.

### 2. Semantic-model boundary requiring continued scrutiny

The source definitions are internally explicit, but the existence of a bridge is not the same as independent validation of the model against Fefferman's PDF.  In particular, the audit must keep checking:

1. whether the `ClaySpec` quantifier order and data conditions exactly match the frozen CMI source;
2. whether `ContDiffOn` on the closed half-space is the intended smoothness notion at the initial boundary;
3. whether the global `BoundedEnergy` predicate has the same time and integrability scope as the CMI statement;
4. whether the periodic pressure condition follows the official erratum rather than only an informal reading; and
5. whether the comparator definitions being bridged are themselves the definitions used by the active endpoint.

These are validation obligations, not findings of falsity in this tranche.  No theorem here proves a pressure-Poisson representative, autonomous-force predicate, or field-level five-observable equality.

### 3. Euler all-order drift construction is substantive and conditional

`Euler/AllOrderDriftEquation.lean:33-68` defines an approximation residual and corrected field and pressure towers.  Theorems at lines 71-137 prove initial agreement, divergence-free membership, gradient-space pressure membership, an error-energy estimate, and derivative identities.  The endpoint theorem at `AllOrderDriftEquation.lean:141-166` constructs an existential exact lifted solution from a `Budget` and an `ApproximationResidual`.

The endpoint is conditional on those upstream structures and returns an Euler `FieldTower`, not an OpenAI Navier–Stokes `ActualCandidateAssembly.Witness`.  It does not mention the selected Navier–Stokes field, `CandidateProperties`, `barMoment`, or the five tuple `(M, I, J, S, Cp)`.

`AllOrderDriftFieldDecomposition.lean:18-43` supplies equality and point-field decompositions for the corrected field and pressure tower.  These are exact Euler graph or packet identities, not a selected Navier–Stokes global-field transport theorem.

### 4. Residual bounds are real bounds, but their observables are local weighted norms

`AllOrderDriftResidualBounds.lean:17-36` defines a nonnegative residual envelope and bounds it by the target.  `AllOrderDriftResidualBounds.lean:39-72` bounds the field and first spatial derivative through `weightedNorm` at a reduced radius.  `AllOrderDriftResidualBounds.lean:75-105` defines a source cost.  `AllOrderDriftResidualBounds.lean:109-151` derives pressure and time-derivative weighted-norm bounds from the field residual estimates.

These theorems are meaningful quantitative control.  They are not radial integral identities and do not imply preservation of `(M, I, J, S, Cp)` under curl, localisation, periodisation, or infinite summation.  This is an important distinction for the main CTR-005 audit.

### 5. Correction cancellation is algebraically exact within its Euler abstract setting

`CorrectionResidualCancellation.lean:22-53` defines the nonlinear increment and proves the raw-source residual identity and cancellation identity.  `CorrectionResidualCancellation.lean:55-86` defines the corrected path and proves initial agreement, divergence-free closure, gradient-space pressure closure, and the derivative equation under explicit hypotheses.

This is not a weakness by itself.  It demonstrates genuine correction algebra.  It also does not transport reduced profile moments to the selected Cartesian Navier–Stokes witness.

### 6. Pressure representatives and packet pressure remainders are explicit but scoped

`MeanPressureRepresentative.lean:29-90` constructs a path representative from a continuous `L2` pressure path and proves smoothness, almost-everywhere agreement, continuity, and the representative equation.  `MeanPressureRepresentative.lean:96-156` defines a scalar pressure/profile and proves the physical-gradient and scalar-equation identities.

`PacketAngularPressureStepBound.lean:15-95` constructs an angular pressure step under explicit budget hypotheses.  `PacketForwardPressureBudgets.lean:17-214` constructs forward angular and initialized pressure budgets.  `PacketForwardPressureRemainder.lean:37-155` and `PacketInitializedPressureRemainder.lean:37-157` prove gradient decompositions and quantitative covector-remainder bounds.

These results show substantial pressure engineering in the Euler branch.  They do not prove an absolute global Leray or Poisson representation for the selected Navier–Stokes pressure, and they do not connect to `ActualCandidateAssembly.Witness`.

### 7. Parity is proved for finite and tail fields, but is not the missing bridge

`PacketFiniteParity.lean:19-143` propagates joint oddness through scalar multiplication, finite sums, matrix application, truncation, assembly, field sums, pressure, nonlinear grades, velocity, and residual tails.  This is a genuine symmetry result in the Euler packet branch.  It is not evidence that the final Navier–Stokes Cartesian field satisfies the five cumulative radial observables.

## Cross-file endpoint search

The reviewed tranche was searched for the principal selected Navier–Stokes endpoint symbols and bridge targets.  No declaration in these twelve files was found that mentions `ActualCandidate`, `selected_witness`, `CandidateProperties`, `NavierStokesR3.theorem_1_1`, `FiveRowRank`, `PositiveOrderMoments`, `barMoment`, or an equality to `(M, I, J, S, Cp)`, except that `Gap.lean` necessarily names the audit comparator structures it is designed to bridge.

The absence is scoped: it proves only that this tranche is not the selected-field bridge.  It does not prove that no such declaration exists elsewhere.  The repository-wide source register remains the authoritative queue for that question.

## Audit classification

| Area | Classification | Evidence boundary |
|---|---|---|
| `ClaySpec` and `Gap` | Audit semantic bridge | Explicit comparator-to-spec implications; fidelity to the frozen CMI source still requires cross-document validation. |
| Euler all-order correction | Genuine conditional construction | Exact corrected towers and derivative identities; Euler branch, not selected NS endpoint. |
| Euler residual bounds | Genuine quantitative control | Weighted local norms and source costs; no radial five-observable transport. |
| Euler pressure/parity | Genuine scoped lemmas | Pressure representatives, decompositions, budgets, and parity; no absolute selected NS pressure theorem. |
| Main CTR-005 question | Still open | This tranche neither proves nor disproves final selected-field transport. |

## Next action

Continue the register queue with the next unreviewed source tranche, while separately validating `ClaySpec` against the exact CMI PDF language.  Do not escalate CTR-005 to a nonzero defect or `False` from these files alone.
