# Current Lean and review-document audit

**Date:** 26 September 2026  
**Scope:** current checkout, selected R³ endpoint, compiled declarations, review map, and active review documents.

## Status

The selected R³ endpoint and the review library compile when targeted. The full
`lake build NavierStokes NavierStokesReview` command is currently blocked by an
untracked scratch file, `NavierStokes/R3/TestPressure.lean:6:60`, which Lean
reports as `expected token`. This is a workspace hygiene/build-scope issue, not
an error reported by the selected endpoint:

| Check | Result | Meaning |
|---|---|---|
| `lake build NavierStokes.R3.Theorem` | passed, 9350 jobs | Active R³ theorem target elaborates. |
| `lake build NavierStokesReview` | passed, 9345 jobs | Review-side library elaborates. |
| `lake build NavierStokes NavierStokesReview` | blocked at `TestPressure.lean:6:60` | Full source census includes an untracked malformed scratch module. |
| `WholeSpaceAxiomAudit.lean` | passed | Selected endpoint reports only `propext`, `Classical.choice`, and `Quot.sound`. |
| hardened audit bundle | passed | Source/environment map is structurally reproducible; it does not prove semantic transport. |

The full-build blocker should be repaired or excluded before claiming a green
repository-wide build. The file is untracked and was not altered by this audit.

## Endpoint map

1. `NavierStokes/R3/Theorem.lean:46-49` exports `NavierStokesR3.theorem_1_1`.
   It obtains a candidate from the R³ wrapper and returns the literal
   `breakdownStatement`.
2. `NavierStokes/R3/ProblemStatement.lean:92-109` defines the active
   `CandidateProperties` record. It explicitly requires pre-singular smoothness,
   compact spatial support, globally smooth compact-positive-time forcing,
   zero initial velocity, divergence-freeness, residual equality, bounded
   kinetic energy, and unbounded speed.
3. `NavierStokes/ActualCandidateAssembly.lean:1121-1151` defines `Witness`.
   Its exported fields are schedules, three potential/direct/pressure sums,
   away extensions, a force, `CandidateProperties`, `CandidateConsequences`,
   H³ growth, force-jet decay, and endpoint jets. The `Witness` type does not
   contain a field asserting the paper tuple `(M,I,J,S,C_p)` for the final
   Cartesian fields.
4. `NavierStokes/ActualCandidateAssembly.lean:1177-1185` fixes the selected
   witness and projects `CandidateProperties` into `selected_candidate`.
5. `NavierStokes/PhysicalResidualJetBounds.lean:885-925` defines the
   `StateRealization` structure. `StateRealization.chartIdentity` is at
   `927-1000` and is proved under `radius_ne`; it is not a standalone
   `StateRealization.lean` module.

## Moment route

| Layer | Source fact | Audit interpretation |
|---|---|---|
| Physical rank debt | `FiveRowRank.lean:22` defines `Debt := Fin 3 → ℝ`. | Runtime rank debt has three coordinates. |
| Five-row predicate | `FiveRowRank.lean:241-246` constrains correction functions `dv` and `ga`; its first two equations set their two radial correction moments to zero. | These are increment constraints, not automatically total-field identities. |
| Scaling | `MeanRankUpdate.lean:30-32` scales the three-coordinate debt with distinct powers. | This is active upstream algebra, not a field-level Cartesian moment theorem. |
| Five-coordinate repair | `PositiveOrderMoments.lean:23` defines a separate `Fin 5 → ℝ` debt. | The five-coordinate machinery exists and must not be called dead code. |
| Radial observable | `DefectIncrementBounds.lean:214-220` defines `barMoment` through `CorrectionState.radialMoment` and a torus-average integral. | `barMoment` acts on scalar correction data; a selected Cartesian-to-radial equality is still required. |

The compiled route map confirms that `FiveRows`, both debt types,
`scaleDebt`, and `barMoment` are reachable upstream of the selected endpoint.
Reachability does not supply the missing value theorem: the `Witness` signature
does not quantify a `barMoment` equality or expose the five named paper moments.
Therefore the controlled finding remains CTR-005, a selected-field transport
obligation rather than a type-level contradiction.

## Pressure route

`NavierStokes/R3/PressureRecovery.lean:33-44` defines comparison hypotheses
for two velocity-pressure pairs. Its `gradient_recovery` theorem at
`407-415` derives a compact-test pressure-gradient identity from equality of
the two residuals. `NavierStokes/R3/ActualPressureFlux.lean` then derives a
comparison flux identity. These are positive, active results.

They do not, by their signatures alone, identify the selected pressure with an
absolute globally normalised Poisson representative. `CandidateProperties`
requires pressure support and residual equality, but no separately named
selected-field pressure-Poisson transport theorem. Compact support alone is
not a proof that the pressure or velocity is zero.

## Coordinate scope

The `StateRealization` record requires `radius_ne : ∀ x ∈ U, x.1.1 ≠ 0`.
The chart identity therefore proves the Cartesian reconstruction on an
off-axis domain. The selected construction also has a separate origin-limit
route. The evidence supports a chart-scope/transport question; it does not
support a claim that the selected field is discontinuous or that the endpoint
has already yielded `False`.

## Document corrections found

- The new workspace goal index initially named a nonexistent
  `NavierStokes/StateRealization.lean`; it now points to the actual structure
  in `NavierStokes/PhysicalResidualJetBounds.lean`.
- The same index now distinguishes the active R³ predicate in
  `NavierStokes/R3/ProblemStatement.lean` from the shared definitions in
  `NavierStokes/ProblemStatement.lean`.
- The active peer review and research paper already use the calibrated verdict:
  the published solution claim is **not established on the inspected record**;
  the selected endpoint is **not formally refuted** because no selected-path
  zero-sorry `False` theorem has been obtained.

## Next required proof target

The next substantive task is not another reachability census. It is one exact,
zero-sorry selected-path theorem of the form

\[
  (M,I,J,S,C_p)_{ \text{paper}}
  = \operatorname{barMoment}\bigl(
      \operatorname{torusAverage}(\nabla\times A_{\text{selected}})
    \bigr),
\]

or a source-backed proof that one required equality is false. Until that
calculation is completed, the review should retain the present distinction
between a publication-critical correspondence failure and a kernel-level
refutation.
