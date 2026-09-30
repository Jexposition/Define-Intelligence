# Priority 202: actual internal moment/debt invariant trace

Date: 2026-09-30
Status: positive production-path trace compiled
Controlled finding: `CTR-005` remains open, but the selected construction contains more moment transport than the earlier endpoint-only description stated

## Why this tranche is necessary

The Priority 201 census correctly found no production declaration whose
conclusion names a final selected-field identity with `(M,I,J,S,Cp)`. It did
not, however, settle whether the actual selected construction carries
moment-related invariants internally. The raw source shows that it does. This
tranche records that positive result so the audit does not understate the
formalisation.

## Exact internal invariant

`CorrectionState.radialMoment` is defined at
`NavierStokes/CorrectionState.lean:226`. The actual state debt is defined at
`CorrectionState.lean:242-246` as three components:

\[
D=(P,J_\theta,J_z),
\]

where the components are the pressure, angular, and axial radial defects.
`GaugeMassPreservation.ZeroMassesOn` at
`GaugeMassPreservation.lean:140-142` contains two additional zero identities:

\[
\operatorname{radialMoment}_2(u_{\mathrm{mean}}^\theta)=0,
\qquad
\operatorname{radialMoment}_1(u_{\mathrm{mean}}^z)=0.
\]

The actual cycle invariant at `CorrectionStep.lean:9408-9448` contains both:

- `debt : DefectBounds ...`, which supplies the three debt-component classes;
- `masses : GaugeMassPreservation.ZeroMassesOn ...`, which supplies the two
  conserved mean-mass identities.

`ActualCyclePreservation.state_runInvariant` at
`ActualCyclePreservation.lean:826-828` constructs this invariant for every
actual cycle stage. The compiled review probe
`NavierStokesReview/src/probes/ActualMomentPreservationTrace.lean:25-48`
re-exposes these two facts as explicit theorems.

## How the correction step uses the invariant

The production source proves that the rank stage preserves the two mean
masses:

- `DefectIncrementBounds.preserve_masses`,
  `DefectIncrementBounds.lean:799-805`;
- `DefectIncrementBounds.zeroMasses`,
  `DefectIncrementBounds.lean:808-813`;
- `CorrectionStep.next_preserve_masses`,
  `CorrectionStep.lean:5322-5342`.

The rank update also proves its three-row relation through
`FiveRowRank.FiveRows` and records the resulting debt through
`DefectIncrementBounds.rankStage_debt_eq` at lines 714 onward. The resulting
`rankStage_defect_class` and `rankStage_defectBounds` are at lines 856-870.
These are genuine actual-field correction and residual-debt results, not
uninhabited `NativeBounds` placeholders.

## What this proves, and what it does not prove

The current source therefore supports the following implication chain:

\[
\text{actual cycle state}
\Longrightarrow
\text{two preserved mean masses plus three residual-debt components}
\Longrightarrow
\text{actual stage and residual-rate machinery}.
\]

It does not yet provide the stronger chain:

\[
\text{actual internal }(2+3)\text{ invariant}
\Longrightarrow
\text{paper's }(M,I,J,S,C_p)
\Longrightarrow
\text{final Cartesian curl/localisation/tsum field}
\Longrightarrow
\text{exported Witness identity}.
\]

The distinction is mathematical, not merely syntactic. The internal objects
are auxiliary-torus mean fields, pressure defects, covariance terms, and
three-coordinate debt. The paper's five quantities are its named cumulative
profile observables. A correspondence theorem must specify the coordinate
map, the scalar/vector projection, the pressure term, the integration measure,
and the effect of curl, localisation, periodisation, and infinite summation.
The compiled probe does not assert those identifications.

## Revised disposition

The positive result changes the wording that is permitted:

- It is false to describe the selected path as carrying no moment-related
  mechanism.
- It is false to describe `NativeBounds` as an unsupported smoothness
  assumption.
- It remains accurate that the exported `Witness` at
  `ActualCandidateAssembly.lean:1121-1151` does not name a final
  `(M,I,J,S,Cp)` identity.
- It remains unproved that the final selected Cartesian field has a nonzero
  moment defect.
- It remains unproved that the force is nonsmooth or that the literal forced
  CMI endpoint is false.

The controlled conclusion is therefore:

> OpenAI's Lean source contains a genuine internal two-mass plus three-debt
> correction invariant that feeds the actual cycle and residual construction.
> The current audit has not located the additional theorem identifying that
> invariant with the manuscript's named five-moment observables after the
> final physical-field transformations and exported endpoint. Complete
> manuscript-to-selected-endpoint correspondence remains `CTR-005: NOT
> ESTABLISHED`.

## Verification

Compiled with:

```text
lake env lean NavierStokesReview/src/probes/ActualMomentPreservationTrace.lean
```

The command exited successfully under the project toolchain
`leanprover/lean4:v4.34.0-rc2`.

Evidence:

- `evidence/source_tranche_priority_202_actual_moment_invariant_trace_2026-09-30.json`
- `src/probes/ActualMomentPreservationTrace.lean`
- `NavierStokes/CorrectionState.lean:226-250`
- `NavierStokes/GaugeMassPreservation.lean:140-142`
- `NavierStokes/CorrectionStep.lean:9408-9448`
- `NavierStokes/ActualCyclePreservation.lean:826-828`
