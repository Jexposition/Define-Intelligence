# Priority 130: Euler comparator and cylinder-average source review

Date: 2026-09-28
Scope: 15 endpoint-external `Euler/` modules selected from the repository-wide
queue.
Navigation aid: `NavierStokesReview/evidence/source_tranche_euler_cylinder_2026-09-28.json`

## Why this tranche matters

The repository contains a separate Euler construction with its own curl,
angular-average, cylinder, and comparator machinery. These files must not be
treated as irrelevant merely because they are outside the captured
Navier--Stokes R3 endpoint closure. They are also not evidence for the
Navier--Stokes selected witness unless a declaration explicitly transports
them into that endpoint.

The adversarial question for this tranche was:

\[
\text{Does an Euler angular-average, curl-transport, or comparator theorem}
\quad\Longrightarrow\quad
\operatorname{barMoment}(u_{\rm selected})=(M,I,J,S,C_p)?
\]

The inspected source does not establish that implication.

## Source findings

### Euler curl transport

`Euler/CurlTransportAlgebra.lean:29-84` proves the ordinary Cartesian curl
identity for the Euler convection term and its divergence-free specialization.
`Euler/CurlTransportAlgebra.lean:92-114` proves that gradients have zero curl
and derives the Euler vorticity right-hand side. This is genuine differential
calculus, including off-diagonal derivative terms. It is not a radial
`barMoment` calculation and it is not connected here to the Navier--Stokes
`ActualCandidateAssembly.selected_witness`.

### Cylinder angular averaging

`Euler/CylinderAngleAverage.lean:21-90` defines a Bochner angular average as a
bounded linear operator and proves boundedness and translation intertwining.
`Euler/CylinderAngleAverage.lean:136-165` proves commutation with actual
linear/full operators; `:179-210` proves preservation of the supported
subspace. These are operator-level averaging facts, not the five radial
observables from the OpenAI Navier--Stokes paper.

`Euler/CylinderAngleAverageEvolution.lean:74-106` proves that the supported
Duhamel/evolution solution commutes with the average and that zero average of
the forcing and initial data propagates to zero average of the solution. This
is a real zero-mean transport theorem for the Euler cylinder evolution. It
does not identify the average with `(M,I,J,S,C_p)`, does not use the selected
Navier--Stokes field, and does not establish a Cartesian-to-radial global
limit.

`Euler/CylinderAngleAverageRepresentative.lean:32-94` relates the L² average
to continuous Sobolev representatives and characterises zero average through
an interval integral. Again, the target is an Euler cylinder average, not the
selected Navier--Stokes radial observable.

### Euler comparator and local evolution

`Euler/ComparatorEvolutionIdentification.lean:30-43` defines the local
evolution and compact-curl upgrade obligations. The subsequent theorem at
`:52-105` proves agreement with a comparator evolution under compact-vorticity
and local-evolution premises. The result is explicitly conditional and
concerns comparator evolution fields.

`Euler/ComparatorLocalEvolution.lean:30-76` constructs a recovered velocity
from compact vorticity and proves its field equality and uniform jet bound.
`:89-101` packages the local upgrade. This is a valid Euler comparator bridge,
not selected Navier--Stokes endpoint transport.

`Euler/ComparatorIdentification.lean:17-38` identifies maximal velocity under
the local-evolution upgrade. `Euler/ComparatorMaximalSolution.lean:17-107`
packages maximal Sobolev derivative/velocity fields and an existence
characterisation. `Euler/ComparatorSingularityNorms.lean:16-40` relates
vorticity and velocity norms. None has the selected NS field or a five-moment
tuple.

### Cylinder Dirichlet and continuous acceleration layers

`Euler/CylinderDirichletEquation.lean:28-82` proves almost-everywhere
coefficient-coordinate, physical velocity, derivative, and balance equations
for an explicitly parameterised cylinder system. The balance is a local
coefficient equation; it is not a global Cartesian pressure or radial moment
identity.

`Euler/CylinderDirichletPhysicalBounds.lean:66-106` provides block bounds for
the physical velocity and derivative. These are estimates for the cylinder
construction, not a selected Navier--Stokes C/D witness.

`Euler/ContinuousAccelerationForcing.lean:26-37`,
`Euler/ContinuousAccelerationGevrey.lean:32-52`, and
`Euler/ContinuousAccelerationSobolev.lean:26-67` define and bound a continuous
acceleration/forcing construction. They establish regularity and bounds, not
the selected-field five-observable composition.

## Adversarial conclusion

This tranche corrects two possible errors:

1. It would be wrong to call the Euler angular-average and curl theorems
   absent or vacuous. They are real, source-level theorems.
2. It would also be wrong to cite them as the missing Navier--Stokes bridge.
   Their types target Euler cylinder spaces, comparator fields, or local
   coefficient systems. No inspected declaration binds them to
   `NavierStokes.ActualCandidateAssembly.selected_witness`, the selected global
   Cartesian field, or the tuple `(M,I,J,S,C_p)`.

The correct status is therefore **external positive Euler evidence; no
Navier--Stokes endpoint transport established**. This tranche does not prove
`False`, a nonzero moment defect, impossibility, or formal refutation.

## Required follow-up

- Continue the repository-wide external queue rather than treating the Euler
  branch as dead or irrelevant.
- Keep Euler angular averages, zero-mean propagation, and curl identities in a
  separate semantic layer from the selected Navier--Stokes global observable.
- If a later bridge is claimed, require its exact type to contain the selected
  field, the target radial observable, and all domain/interchange hypotheses.
