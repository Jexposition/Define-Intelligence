# Priority 123: Selected Navier–Stokes endpoint junction review

Date: 2026-09-28
Scope: source-level review of eight non-obvious Navier–Stokes junctions that sit between profile/correction data and the periodic C/D endpoint.

## Purpose

This tranche tests the main blindside risk: treating the absence of a five-observable field in `ActualCandidateAssembly.Witness` as if the surrounding code were only a generic rate shell. The source shows a stronger and more precise picture. OpenAI's code contains real continuation, support, summability, physical-data, residual, and periodic-endpoint constructions. The unresolved question is narrower: whether those constructions prove the final selected Cartesian or periodic field identity for the five paper observables

\[
(M,I,J,S,C_p),
\]

or an equivalent `barMoment`/torus-average transport theorem.

## Source junction findings

| Source | What is actually proved | Relevance to the selected-field bridge |
|---|---|---|
| `NavierStokes/PeriodicPaperTheorem.lean` | Defines periodic `CandidateProperties` and `GlobalSmoothSolution`; `of_compact_candidate` and `periodic_corollary` transport smoothness, periodicity, fundamental-cube support, zero initial data, divergence, residual equality, and speed blow-up. | This is a real periodic C/D endpoint composition. Its candidate predicate contains no five-moment or `barMoment` field. |
| `NavierStokes/PeriodicPaperScalingSupport.lean` | Proves compression of velocity, pressure, and force support into a fundamental cube via `exists_compression_scale`. | Support transport is proved; support transport is not moment transport. |
| `NavierStokes/WholeDomainPhysicalStageTheorem.lean` | Proves concrete physical stage bounds, finite velocity/pressure bounds, residual bounds, and `paper_physical_loss` rate packages. | This corrects the overstatement that the endpoint uses only abstract rates. Concrete physical data feeds the rates. The theorem still exports no equality between the final field and `(M,I,J,S,C_p)`. |
| `NavierStokes/ActualParticularPhysicalData.lean` | Defines actual amplitude/pressure/potential data, `tsum` identities, summability, rotated sums, support/geometry, and native-to-physical bounds. | Genuine series and physical-field assembly exists. The inspected declarations do not provide a final selected-field `barMoment` tuple theorem. |
| `NavierStokes/MeanStageContinuation.lean` | Proves periodic algebra for radial/time/viscosity/residual operators and continuation identities for bases, profiles, sources, primitives, and debt/rank data. | Strong local continuation evidence; no inspected theorem transports the final selected Cartesian field to the five radial observables. |
| `NavierStokes/CycleContinuationInvariant.lean` | Packages periodic primitives/harmonics, axis-supported continuation, representation, and periodicity after particular, signed, temporal, and rank updates. | Shows that cycle continuation is not absent. It does not identify the final global `barMoment` values. |
| `NavierStokes/SignedRequestContinuation.lean` | Proves closure of supported triples under operations, smoothness, local-shell agreement, physical stress support, and actual-base identities. | Genuine support/agreement infrastructure; no final selected observable equality was located. |
| `NavierStokes/CorrectionInitializationNoOptions.lean` | Builds correction-initialisation data, support/cutoff facts, native bounds, `initialized_zeroMasses`, and radial residual data. | Genuine upstream correction and zero-mass machinery; no final Cartesian/periodic five-observable export. |

## Exact source anchors

- `PeriodicPaperTheorem.lean:9-15`: periodic lifts to \(\mathbb R^3\) and support restricted to the closed fundamental cube; this does not claim that a nonzero periodic lift is compactly supported on all of \(\mathbb R^3\).
- `PeriodicPaperTheorem.lean:24-47`: periodic `CandidateProperties` fields, including smoothness, periodicity, cube support, residual, divergence, and speed blow-up.
- `PeriodicPaperTheorem.lean:51-73`: fixed-force global competitor predicate and relative no-global-solution consequence.
- `PeriodicPaperTheorem.lean:89-144`: compact-to-periodic transport; no moment clause.
- `PeriodicPaperTheorem.lean:148-162`: periodic breakdown statement and corollary.
- `PeriodicPaperScalingSupport.lean:15-109`: velocity, pressure, force support scaling and cube compression.
- `WholeDomainPhysicalStageTheorem.lean:29-132`: finite-field and physical-stage bounds.
- `WholeDomainPhysicalStageTheorem.lean:154-208`: exact physical loss and paper-loss inequalities.
- `WholeDomainPhysicalStageTheorem.lean:243-280`: concrete potential/direct/pressure stage rates, finite-field bounds, residual bounds, and logarithmic rate packages.
- `ActualParticularPhysicalData.lean:56-161`: actual amplitude/pressure/potential sums and summability identities.
- `ActualParticularPhysicalData.lean:678-718`: native potential and physical bounds.
- `ActualParticularPhysicalData.lean:728-872`: support and geometry declarations.
- `ActualParticularPhysicalData.lean:1148-1150`: physical estimates supplied by `WaveData`'s native-to-physical theorem; physical jet bounds are not an input.
- `ActualParticularPhysicalData.lean:1226-1255`: physical potential and pressure bounds.
- `MeanStageContinuation.lean:140-192; 209-339; 465-478; 596-647`: periodic operator/continuation and debt/rank identities.
- `CycleContinuationInvariant.lean:411-420; 447-491; 567-652`: invariant structure and periodicity after cycle updates.
- `SignedRequestContinuation.lean:26-220; 323-377; 411-499; 535-557; 581-743`: supported operations, shell agreement, physical stress, and actual-base continuation.
- `CorrectionInitializationNoOptions.lean:81-97; 124-289; 1212-1245`: correction pieces, support/cutoff data, zero-mass initialization, and radial residual data.

## Hardened logical classification

### Established by this tranche

1. The selected endpoint is not merely a name-matched existential shell. It has real physical stage data, summability, support, periodicity, residual, and rate constructions.
2. The periodic theorem is a genuine C/D packaging path. Its support semantics are correctly phrased on a fundamental cube, not as compact support of a nonzero periodic lift over all of \(\mathbb R^3\).
3. Upstream correction and continuation layers contain real moment-adjacent data, including zero-mass and debt/rank identities.

### Not established by this tranche

1. No inspected declaration proves
   \[
   \operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p),
   \]
   nor an equivalent theorem transporting those observables through the selected Cartesian/periodic construction.
2. No inspected declaration proves that the curl, localisation, periodisation, and `tsum` operations preserve the paper's five observables.
3. No inspected declaration proves a nonzero defect, impossibility theorem, or kernel-level `False`.

## Corrections to earlier audit wording

The following stronger claims are not justified and must not be used:

- “The endpoint uses only generic rates.” The source shows that concrete physical data and `tsum`/summability results feed the rate packages.
- “The five-moment machinery is absent from the selected construction.” The source shows genuine upstream correction, continuation, and physical-data machinery.
- “Curls or cutoffs necessarily destroy the moments.” Commutator and boundary terms create an obligation to calculate; they do not by themselves prove a nonzero defect.

The defensible CTR-005 statement is narrower and stronger: **the inspected selected endpoint proves many physical and analytic properties, but the audited junctions do not expose a field-level theorem identifying the final selected Cartesian/periodic observables with the paper's five-moment tuple.** Repository-wide absence is not declared until the remaining source and declaration closure is searched.

## Next adversarial test

The next probe must search declaration signatures and theorem bodies, not filenames, for a composition of the form

\[
\texttt{potentialSum/tsum}
\to \texttt{curl/localisation}
\to \texttt{periodicVelocity}
\to \texttt{torusAverage/barMoment}
\to (M,I,J,S,C_p).
\]

A positive result downgrades CTR-005. A theorem proving a nonzero selected-field defect escalates the classification. A missing theorem remains a correspondence gap, not a refutation.
