# Priority 194: residual-cancellation and endpoint correspondence adjudication

Status: source-checked correction of the latest adversarial rebuttal.

## Question

Does the current source record establish that every summand of

\[
R(u,p)=\partial_tu+(u\cdot\nabla)u-\Delta u+\nabla p
\]

must diverge as \(t\uparrow1\), that the five radial moments are the only
cancellation mechanism in the manuscript, and that `force_smooth` is merely an
unlinked `NativeBounds` assumption at the selected Lean endpoint?

## Adjudication

No. Those three statements are stronger than the inspected sources support.
The correct conclusion is narrower and more precise:

1. The manuscript makes residual smoothness a connected requirement. It says
   that individual terms *can* diverge and that their sum and all derivatives
   must extend smoothly through the singular time.
2. The manuscript assigns distinct jobs to several mechanisms. Its correction
   cycle lists wave-amplitude equations, signed covariance/stress correction,
   auxiliary-time/angular-mean correction, and the five radial moment equations.
   The five moments are therefore load-bearing, but the source does not prove
   the stronger claim that they are the sole cancellation mechanism.
3. The selected Lean route is not a proof that arbitrary `NativeBounds` are
   sufficient by fiat. `ActualCandidateAssembly.estimates` consumes concrete
   `physicalData` through `GluedStageEstimates.actualStageEstimates`; the
   selected schedule supplies `VanishingJointJets`; `CandidateFromLimits`
   derives `tracedResidual_smooth` from the derivative recurrence and locally
   uniform residual-jet limits; `force_smooth` then follows from the smooth
   extension theorem.
4. This does not close the paper-to-endpoint gap. The exported `Witness` still
   does not state the field-level theorem identifying the final selected
   Cartesian velocity, pressure, residual, and force with the manuscript's
   \((M,I,J,S,C_p)\) observables and their transport through localisation,
   summation, periodisation, and pressure reconstruction.

## Source evidence

The manuscript's physical description states that individual residual terms
can diverge, while the sum and all derivatives must extend smoothly, and that
oscillatory pulses plus further corrections cancel the singular residual:

- `docs/navier-stokes openai.txt:109-124`
- `docs/navier-stokes openai.txt:252-304`

The proof outline separates background residual stress, pulse covariance,
linear and quadratic interaction terms, and later corrections:

- `docs/navier-stokes openai.txt:306-321`
- `docs/navier-stokes openai.txt:548-572`
- `docs/navier-stokes openai.txt:697-735`

The same source records the five radial equations as the fourth operation in
the correction cycle. That makes them load-bearing for the described repair,
but not a source-level proof that no other cancellation operation contributes.

The selected Lean force path is explicit:

- `NavierStokes/ActualCandidateAssembly.lean:1079-1098` constructs physical
  data and stage estimates from actual cycle representations.
- `NavierStokes/GluedStageEstimates.lean:684-744` constructs the mixed-stage
  estimate record from actual coherent cycle data.
- `NavierStokes/ActualCycleResidualBounds.lean:1190-1206` supplies finite
  residual rates.
- `NavierStokes/MixedCandidateWitness.lean:26-31` and
  `NavierStokes/MixedCandidateAssembly.lean:67-91` supply the schedule and
  `VanishingJointJets` contract.
- `NavierStokes/MixedPeriodicAssembly.lean:310-367` turns those limits into
  boundary control and invokes the candidate construction.
- `NavierStokes/CandidateFromLimits.lean:47-87` derives
  `tracedResidual_smooth`, defines the residual-designed force, and proves
  `force_smooth` from the smooth-extension theorem.

## What this does and does not prove

The selected Lean route proves an encoded forced candidate with smooth force
and velocity blow-up on the inspected path, conditional on the premises and
source constructions that feed that path. It does not, by itself, prove that
the endpoint is a complete formalisation of every load-bearing mechanism in
the manuscript.

Conversely, the missing final observable-identification theorem does not prove
that the selected force is nonsmooth, that the selected moments are nonzero, or
that Fefferman's literal connected C or D proposition is false. Those stronger
claims require a selected value-level mismatch, a failed connected condition,
an impossibility theorem, or a contradiction.

Therefore the correct audit classification remains:

\[
\boxed{\text{complete manuscript-to-selected-endpoint fidelity: NOT ESTABLISHED (CTR-005)}}
\]

This is not a concession that the five moments are optional. It is also not a
claim that the current Lean endpoint has already falsified the literal CMI
alternative. It is a separation between an established selected Lean route
and an unestablished paper-to-endpoint identification.
