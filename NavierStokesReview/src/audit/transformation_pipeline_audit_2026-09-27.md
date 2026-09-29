# Transformation-pipeline audit: selected moments and cutoff commutators

**Status:** active falsification target, not a completed refutation
**Date:** 2026-09-27
**Source tree:** `NavierStokes/` is read-only
**Review tree:** all new probes, calculations, and audit controls belong under `NavierStokesReview/`

## Question under test

The paper-level requirement is a value-level statement about the selected
whole-space field, not merely the existence of upstream profile certificates:

```text
barMoment(torusAverage(periodize(curl(tsum(potentialSum)) with localisation)))
  = (M, I, J, S, C_p)
```

The exact operators and domains must be instantiated from the live Lean source.
The expression above is therefore an audit target, not a definition silently
assumed to match the repository.

## Source-grounded ledger

| Layer | Direct source result | What it establishes | What it does not establish |
|---|---|---|---|
| Reduced profiles | `NavierStokes/NominalProfile.lean:2079-2145,2536-2541`; `PositiveOrderMoments.lean`; `FiveProfileMoments.lean` | Genuine reduced five-coordinate certificates and repair algebra exist | That the final selected Cartesian field has the same five observables |
| Correction state | `NavierStokes/CorrectionState.lean`; `DefectIncrementBounds.lean` | Local `FiveRows`, `barMoment`, pressure, and debt identities | A final-field evaluation of those identities |
| Cartesian lift | `NavierStokes/ActualPrimaryCoherence.lean`; `CyclePhysicalPrefixes.lean` | Smooth/divergence-free curl representations and finite-prefix identities | Infinite selected-field radial transport |
| Localisation | `NavierStokes/SpatialLocalization.lean`; `PeriodizedWaveBounds.lean` | Cutoff-before-curl product rule, commutator, support, periodicity, divergence, and residual transfer | A zero or nonzero integrated commutator for the selected field |
| Infinite assembly | `NavierStokes/SolenoidalDiagonal.lean`; `PotentialSeries.lean`; `ActualSlowBase.lean` | Locally finite or convergent sum-to-curl and jet estimates | Weighted radial tail convergence for all five observables |
| Averaging/pullback | `NavierStokes/PressureStream.lean`; `MeanResidual.lean`; `DefectIncrementBounds.lean` | Several typed averaging, flux, and `barMoment` interfaces | Equality between the final whole-space field and `(M,I,J,S,C_p)` |
| Endpoint | `NavierStokes/ActualCandidateAssembly.lean:1121-1181`; `R3/ProblemStatement.lean:92-109` | The exported `Witness`/`CandidateProperties` package schedules, fields, residual, support, energy, and blow-up properties | A final selected-field five-observable equality or a `FiveRows` premise |

## Calibrated interpretation

The following claims are **not** accepted as established merely from the
existence of a commutator:

1. `curl(c A) = c curl(A) + grad(c) × A` does not imply that its radial
   integral is nonzero. Exact cancellation remains possible.
2. The abstract `StageEstimates` interface is moment-blind by type, but the
   concrete `GluedStageEstimates.actualStageEstimates` construction consumes
   physical-data and `NativeBounds` results. The accurate claim is endpoint
   non-export of the final observable equality, not that the entire concrete
   construction ignores moment work.
3. `f := navierStokesResidual u p` and the fixed-force perturbation theorem
   establish provenance/path dependence. They do not, without an added
   force-independence predicate, derive `False` from the literal existential
   CMI endpoint.
4. Compact pressure support is a semantic pressure question. It is not by
   itself a contradiction while the formal force is unrestricted and no
   absolute selected-pressure Poisson representative has been required.

## Declared profile calculation versus selected-field evidence

The attached calculation in `scratch_space/notes3.md` is now implemented by
`NavierStokesReview/src/audit/cutoff_commutator_scan.py`. It is not a toy scan:
it reconstructs the exact `SpatialLocalization.spatialCutoff` on a 3D
Cartesian volume, evaluates a nonseparable axisymmetric stream profile
`S(r,z)`, builds `A_x,A_y,A_z`, evaluates the analytic curl and
`(grad c) x A` commutator, finite-differences the Cartesian curl independently,
records the divergence residual and full x-y moment slices, and sweeps
resolution, profile scale, and axial modulation.

CUDA is the primary execution backend through the canonical V-lab environment;
CPU is only a fallback when CUDA is unavailable. The run emits JSON, CSV,
Markdown, and a mandatory multi-panel plot. CPU/GPU comparison is not treated
as the result: the result is the 3D calculation itself.

The recorded CUDA run used the RTX 4060 Ti at 129/193/257 points, profile
scales `0.5, 1, 2`, modulations `0, 0.25`, and a fixed trusted-radius mask
`r > 0.1` for derivative validation. At 257 points the declared profile gave
nonzero `L∞` slice defects from about `0.244` to `0.364` and `L1` slice metrics
from about `0.0841` to `0.1337`. For the scale-1, zero-modulation control,
trusted finite-difference divergence and curl errors were about `2.94` and
`0.191`, while the product-rule residual was about `0.0449`. The refinement
run is useful numerical support for the explicit profile calculation, but it
does not identify that profile with the selected Lean field.

It is nevertheless profile-level evidence, not a selected-field result. The
notes table does not bind its displayed values to OpenAI's actual
`ASum`/`BSum`/`PSum`, `tsum`, periodisation, `barMoment` measure, or axis
totalisation. The generated report records the 3D diagnostic and its numerical
errors without promoting it to `Delta m != 0` for `selected_witness`. That
promotion still requires the exact Lean field route and a selected-field error
argument.

## Full-tree numerical source census

`selected_endpoint_source_census.py` scans the complete current repository
source set and writes
`NavierStokesReview/evidence/selected_endpoint_source_census_2026-09-27.json`
and `.md`. The verified run covers 2,790 Lean files, 649,366 source lines,
50,191 parsed declarations, and 588 modules reachable from
`NavierStokes.R3.Theorem` and `NavierStokes.ActualCandidateAssembly`. It finds
zero missing local imports and seven active declaration blocks containing both
moment/debt vocabulary and endpoint/field/rate vocabulary.

These numbers identify where exact manual inspection should concentrate. They
do not establish a bridge: lexical co-occurrence is not a theorem, and the
seven blocks must be checked for actual value-level transport rather than
counted as positive evidence.

## Escalation rules

`CTR-005` may be escalated only by one of these source-backed results:

- a zero-sorry theorem evaluating the actual selected field and proving
  `Delta m != 0` against a required zero invariant;
- a zero-sorry impossibility theorem showing that the required transport is
  incompatible with the selected field's proved properties; or
- a complete positive theorem transporting all required observables through
  the actual sum, curl, localisation, periodisation, averaging, radial,
  support, integrability, and axis domains.

Until then the classification remains **Not Established as paper-to-code
correspondence**, not `False` and not `Verified CMI solution`.

## Contributor contract

- Do not edit `NavierStokes/`.
- Put Lean probes in `NavierStokesReview/src/probes/`, completions in
  `src/completions/`, extensions in `src/extensions/`, external semantic
  assumptions in `src/external_semantic/` or `src/external-semantic/`, and
  refutation attempts in `src/refutations/`.
- Put parsers and reproducible calculations in `src/audit/`; put generated
  evidence in `NavierStokesReview/evidence/`.
- Every result must name exact source anchors, input functions, domains,
  assumptions, command, and exit status. No `sorry`, no inferred endpoint
  transport from imports, and no surrogate-profile result.
