# Priority 176: selected field composition and observable-domain trace

**Date:** 2026-09-29
**Scope:** selected finite sums, Cartesian localisation, periodisation, time activation, and `barMoment`
**Status:** source-checked composition trace; value-level five-observable equality remains open

## Executive finding

The selected route is a genuine composed field construction. It is not merely
a label around generic estimates. The source defines the selected potential,
direct, and pressure sums, applies spatial localisation and periodisation,
adds the direct field, and then applies time activation:

\[
\begin{aligned}
 A_* &= \operatorname{potentialSum}(a,q,A_j),\\
 B_* &= \operatorname{potentialSum}(a,q,B_j),\\
 P_* &= \operatorname{potentialSum}(a,q,P_j),\\
 u_* &= \operatorname{activatedVelocity}
       \bigl(\operatorname{periodicVelocity}(A_*,B_*)\bigr),\\
 p_* &= \operatorname{activatedPressure}
       \bigl(\operatorname{periodicPressure}(P_*)\bigr).
\end{aligned}
\]

The source also proves smoothness, periodicity, divergence freedom, late-time
agreement, residual identities, and axis blow-up for this composed route.
That positive result must be preserved.

The remaining domain boundary is exact and material. `DefectIncrementBounds.barMoment`
has the type

\[
\texttt{barMoment}:
  \mathbb{N}\to \texttt{ScalarField (Point P)}
  \to \texttt{ScalarField P},
\]

and evaluates

\[
\texttt{barMoment}\ k\ f\ n\ p
 = \int r^k\,\operatorname{torusAverage}(f_n)(r,p)\,dr.
\]

No inspected declaration identifies that scalar pressure-stream input with a
component or derived observable of the final activated Cartesian velocity and
pressure. The missing theorem is therefore a representation/transport
identity, not the existence of the selected field itself.

## Source composition

### 1. Infinite stage sum

`SolenoidalDiagonal.potentialSum` is defined at
`NavierStokes/SolenoidalDiagonal.lean:37--38` as the `tsum` of the cut stages

\[
\operatorname{potentialSum}(a,q,A)(x)
 = \sum'_{j\in\mathbb{N}}
   \operatorname{scaledCutoff}(a_j,q(x))\,A_j(x).
\]

The same file proves local eventual equality to a finite prefix and smoothness
on positive-scale domains (`:46--126`). These are real convergence and
regularity results. They are not radial five-moment identities.

### 2. Selected sums

`LocalScheduleWitness.lean:22--34` defines the selected `potentialSum`,
`directSum`, and `pressureSum` from the actual selected stage families. The
selected schedule is retained; the construction does not silently replace it
with an unrelated witness.

### 3. Cartesian mixed field

`MixedPeriodicAssembly.lean:28--38` defines

\[
\operatorname{periodicVelocity}(A,B)
 = \operatorname{periodicVelocity}_{\mathrm{potential}}(A)
   + \operatorname{periodize}(\operatorname{cutPotential}(B)).
\]

The potential branch is expanded in
`SpatialLocalization.lean:210--217` as

\[
\operatorname{spatialCurl}
 \left(\operatorname{periodize}(\operatorname{cutPotential}(A))\right),
\]

while the pressure branch is

\[
\operatorname{periodize}(\operatorname{cutPressure}(P)).
\]

The source proves local agreement with the cut fields on the inner cube and
proves the corresponding residual agreement
(`SpatialLocalization.lean:264--296`). This establishes the actual
localisation/periodisation path, including the cutoff-gradient contribution
implicit in the curl of the cut potential.

### 4. Time activation

`TimeLocalization.lean:27--31` defines

\[
u_{\mathrm{act}}(t,x)=\chi_t(t)u_*(t,x),\qquad
p_{\mathrm{act}}(t,x)=\chi_t(t)p_*(t,x).
\]

The source proves late-time equality and residual equality
(`:74--96`, `:127--164`) and proves that activation preserves speed
unboundedness (`:172--193`). Thus the blow-up endpoint is not a claim about a
missing field; it is attached to the composed activated field.

### 5. Selected endpoint use

`LocalScheduleWitness.selected_periodic_candidate`
(`LocalScheduleWitness.lean:131--152`) feeds the same selected sums into
`CandidateProperties` and a smooth forcing theorem. The compact candidate
then packages those fields at `:156--163`. This confirms the positive
selected-field route and prevents the audit from calling the endpoint empty.

## Observable-domain boundary

`DefectIncrementBounds.lean:214--220` defines `barMoment` through
`CorrectionState.radialMoment` and `PressureStream.torusAverage`. Its formula
is a radial integral of a scalar pressure-stream field. The source proves
linearity, support/integrability, and slow-class estimates
(`:232--297`, `:607--619`), but no inspected theorem has the form

\[
\operatorname{barMoment}(\text{selected pressure data})
 = \operatorname{PaperMoments}(u_{\mathrm{act}},p_{\mathrm{act}})
 = (M,I,J,S,C_p).
\]

Nor has a theorem been found transporting the reduced profile moments through
the selected `tsum`, Cartesian curl, cutoff, periodisation, pressure, and
activation operations into that formula.

## Audit classification

* selected `ASum`/`BSum`/`PSum` composition: **source-bound and genuine**;
* selected smooth-force, residual, periodicity, divergence, and blow-up route:
  **established on the inspected path**;
* final selected-field identification with `(M,I,J,S,C_p)`:
  **NOT ESTABLISHED (CTR-005)**;
* selected nonzero defect, impossibility, force nonsmoothness, literal CMI
  failure, and Lean contradiction: **not proved**.

This is the precise boundary. It neither collapses the field construction into
an interface artefact nor credits the paper's five-observable mechanism
without the missing representation theorem.

## Source anchors

* `NavierStokes/SolenoidalDiagonal.lean:37--126`
* `NavierStokes/LocalScheduleWitness.lean:22--34,109--163`
* `NavierStokes/MixedPeriodicAssembly.lean:28--49`
* `NavierStokes/SpatialLocalization.lean:210--296`
* `NavierStokes/TimeLocalization.lean:27--31,74--193`
* `NavierStokes/DefectIncrementBounds.lean:214--297,607--619`
