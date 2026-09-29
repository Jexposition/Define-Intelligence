# Priority 7-61 source review: endpoint-adjacent packaging and R3 analytic support

Date: 2026-09-27
Scope: ten additional reachable source modules.
Method: direct source inspection of imports, definitions, theorem statements, and proof-facing hypotheses at the cited ranges.

## Executive result

This tranche confirms two things at once. First, the candidate packaging is
substantive: `MixedCandidateWitness` supplies a selected schedule, infinite
potential sums, away-axis extensions, activated velocity and pressure, force,
candidate properties, residual consequences, H³ blow-up, force derivative
bounds, and endpoint boundary limits. Secondly, the R3 comparison layer is
substantive: compact-support differentiation, heat-kernel inverse-cube bounds,
cutoff commutator cancellation, Fubini interchange, and weak time continuity
are explicitly formalised.

None of these declarations is a field-level theorem asserting that the final
activated Cartesian field has the paper's five cumulative radial observables.
The R3 bounds are analytic support for comparison/pressure estimates, not a
substitute for the selected-field moment composition.

## Module findings

### 1. `LoopVariance.lean`

- Defines the actual angular exponential-family measure and its Lebesgue
  moments (`LoopVariance.lean:24-50`).
- Proves derivative, analyticity, positivity, weighted-square, and determinant
  identities for the normaliser and variance (`:54-139`).
- This is an angular probability/moment subsystem. Its `moment` is not the
  paper's selected whole-space radial `barMoment` and it has no endpoint field
  parameter.

Classification: genuine local angular moment calculus; not selected-field
transport.

### 2. `JointODE.lean`

- Reparametrises a fixed interval to `[0,1]`, transports coefficient/source
  data, and proves smoothness of the reparametrised solution (`JointODE.lean:35-114`).
- Proves that the constructed solution agrees with the actual integral solution
  and is jointly smooth in parameters and current time (`:129-219`).
- The module explicitly concerns a linear ODE solution on a prescribed closed
  interval and does not claim smoothness of a clamped extension outside it.

Classification: time/ODE regularity; no Navier-Stokes endpoint observable.

### 3. `MixedCandidateWitness.lean`

- `SelectedSchedule` requires positive, increasing stage indices, growth,
  smooth mixed sums, and vanishing joint residual jets
  (`MixedCandidateWitness.lean:23-31`).
- `exists_candidate_witness_of_finite_stages` takes finite-stage potential and
  pressure inputs, support/extension hypotheses, and a `StageEstimates`
  premise (`:41-66`).
- It constructs `ASum`, `BSum`, `PSum`, away-axis extensions, activated fields,
  a force, `CandidateProperties`, candidate consequences, H³ blow-up, force
  derivative decay, and endpoint boundary limits (`:67-97`).
- The type has no equality of the final field with `(M,I,J,S,C_p)` and no
  `FiveRows` premise.

Classification: endpoint-adjacent candidate packaging. It strengthens the
positive record for the software witness while leaving CTR-005 unchanged.

### 4. `R3/CompactTimeIntegral.lean`

- Proves continuity of ordinary spatial integrals under uniform compact support
  and proves derivatives vanish outside the common support
  (`R3/CompactTimeIntegral.lean:47-68`).
- Proves differentiation under the ordinary integral for interior times and
  continuous-time integral identities on a closed time slab (`:69-170`).

Classification: real whole-space integration infrastructure; not radial moment
transport.

### 5. `R3/HeatKernelCancellation.lean`

- Defines the squared-cutoff difference and its time-integrated kernel
  (`R3/HeatKernelCancellation.lean:24-24, :105-113`).
- Proves the Lipschitz/minimum bound, diagonal cancellation, and an inverse-cube
  majorant for the absolute cancelled kernel (`:49-89, :124-166`).
- The cancellation is inserted before integration and is used to control a
  commutator kernel. It is not a claim that the selected field's radial
  moments vanish.

Classification: pressure/uniqueness commutator estimate; no endpoint moment
identity.

### 6. `R3/HeatKernelFubini.lean`

- Establishes absolute integrability of the cancelled space-time integrand
  using the radial commutator kernel in `L^(4/3)` and a test in `L^4`
  (`R3/HeatKernelFubini.lean:44-81`).
- Proves the corresponding time-space integral swap (`:83-107`).

Classification: genuine Fubini/commutator support for R3 comparison; no
selected Cartesian five-observable evaluation.

### 7. `R3/HeatKernelTimeBound.lean`

- Evaluates the inverse-time Gamma integrals and defines the nonnegative
  three-dimensional heat-kernel Hessian envelope
  (`R3/HeatKernelTimeBound.lean:33-80, :82-114`).
- Proves the envelope equals a universal constant times `r^-3`, then derives
  componentwise Hessian integrability and the inverse-cube absolute bound
  (`:157-214`).

Classification: rigorous R3 heat-kernel estimate. It supports pressure
comparison but is not a radial profile transport theorem.

### 8. `R3/WeakTimeContinuity.lean`

- Defines compactly truncated tests and proves integrability, uniform cutoff
  approximation, and compact-test continuity (`R3/WeakTimeContinuity.lean:44-119`).
- Upgrades the result to continuous pairings with continuous tests vanishing at
  infinity under uniform spatial `L¹` bounds (`:121-175`).

Classification: weak time continuity for whole-space pairings; no endpoint
five-moment identity.

### 9. `CoordinateAlgebra.lean`

- Checks manuscript coordinate identities, positivity, Jacobian determinant,
  inverse algebra, and chain-rule coefficients
  (`CoordinateAlgebra.lean:18-128, :138-214`).
- Its header explicitly says it does not construct a smooth inverse chart, a
  Navier-Stokes solution, or a singularity (`:5-12`).

Classification: algebraic coordinate check only; no semantic field transport.

### 10. `FlatCutoff.lean`

- Defines the exponential-flat cutoff `exp(-c/x²)` extended by zero and proves
  nonnegativity, smoothness, vanishing derivatives, and inverse-power quotient
  regularity (`FlatCutoff.lean:23-50, :66-131, :137-199`).
- The header explicitly limits the result to the scalar edge function and
  excludes stress factorisation, PDE estimates, and asserted force extension
  claims (`:5-17`).

Classification: genuine scalar cutoff regularity; no moment-preservation
theorem.

## Cross-layer disposition

| Question | Source-grounded answer |
|---|---|
| Is the software candidate packaging nonempty and explicit? | Yes. `MixedCandidateWitness` constructs the selected sums and consequences under its stated premises. |
| Do R3 files prove real whole-space analytic estimates? | Yes. Compact support, heat-kernel, commutator, Fubini, and weak-continuity results are explicit. |
| Do those R3 estimates prove the paper's five selected-field moments? | No. |
| Does this tranche prove a nonzero selected-field defect? | No. |
| Does this tranche prove impossibility or `False`? | No. |

## Controlled conclusion

The endpoint software proposition is stronger than a mere empty interface, and
the R3 analytic comparison layer is real. The unresolved issue is narrower and
more important: whether the intermediate profile/correction observables are
transported through the actual activated Cartesian sums, curl/localisation,
periodisation, and exported `Witness`. This tranche adds no proof of that
composition and no contradiction against it.
