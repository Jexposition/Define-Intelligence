# Claim cross-examination: selected endpoint and five-moment transport

**Date:** 2026-09-27  
**Scope:** raw source verification of the selected Navier–Stokes endpoint and the review claims made about it.

## 1. The endpoint is nontrivial, but `Witness` is not a structure

`NavierStokes/ActualCandidateAssembly.lean:1121-1151` defines
`Witness` as a `def ... : Prop` whose body is a nested existential and
conjunction, not as a Lean `structure`. Its exported payload is:

```lean
∃ a : ℕ → ℕ,
  SelectedSchedule ... ∧
  ∃ (ea : AwayExtensions ASum) (eb : AwayExtensions BSum)
    (ep : AwayExtensions PSum),
  ∃ forcing : VelocityField,
    CandidateProperties selectedVelocity selectedPressure forcing ∧
    ContDiff ℝ ∞ forcing ∧
    CandidateConsequences.Consequences selectedVelocity selectedPressure forcing ∧
    Tendsto derivativeH3Norm ... (𝓝[<] (1 : ℝ)) atTop ∧
    (∀ m K, ...) ∧
    (∀ n x, iteratedFDeriv forcing (1, x) = boundaryLimits ... x n)
```

There is no binder or conjunct for `PositiveOrderMoments.Debt`,
`FiveRowRank.FiveRows`, `barMoment`, or an equality identifying
`(M, I, J, S, C_p)` with values of the selected Cartesian fields. The
selected theorem at `ActualCandidateAssembly.lean:1177-1181` is simply
`selected_witness := witness ...`; it fixes the parameters but does not add a
five-moment transport conjunct.

This is a packaging-boundary result. It does not imply that the upstream
moment construction is false or unused.

## 2. What the selected route actually proves

The selected construction is not a hollow zero-field envelope. The source
route is:

```text
ActualCandidateConstruction
  -> ActualCandidateAssembly.witness
  -> GermCandidateAssembly.exists_candidate_witness_of_finite_stages
  -> StageEstimates.exists_schedule
  -> potentialSum/direct sum/pressure sum
  -> periodic velocity and pressure
  -> CandidateProperties and CandidateConsequences
  -> R3/ActualCandidate.of_localized_fields
  -> R3/Theorem.theorem_1_1
```

`MixedCandidateAssembly.StageEstimates` at `MixedCandidateAssembly.lean:29-65`
contains smoothness, raw stage bounds, finite background `JetRate`, and finite
residual `JetRate`. `StageEstimates.exists_schedule` starts at line 67.
The actual stage consumer calls `ActualCycleResidualBounds.finite_residual_rates`
from `ActualStageEstimates.lean:399-401`; that theorem consumes `NativeBounds`
through the actual cycle residual data in `ActualCycleResidualBounds.lean`.
The packaging boundary then consumes the resulting schedule and sums at
`ActualCandidateAssembly.lean:1125-1149`.

Therefore the accurate statement is not “the endpoint only uses generic rate
contracts” and not “the moment machinery is absent”. The accurate statement
is that the endpoint exports the assembled fields and rate/residual
consequences without exporting the value-level equality that identifies the
paper’s five moments with those fields.

## 3. Reachability is confirmed, but the probe names must be read precisely

The selected closure reaches `FiveRowRank`, `PositiveOrderMoments`,
`FiveProfileMoments`, `MeanRankUpdate`, `periodicVelocity`, and `barMoment` in
the compiled-environment/source join recorded in
`docs/dependency_closure_validation.md:68-73` and
`NavierStokesReview/evidence/selected_endpoint_routes_2026-09-26.md`.

However, `NavierStokesReview/src/probes/SelectedImportClosureProbe.lean:1-8`
only imports `NavierStokes.R3.Theorem` and runs two `#check` commands. It does
not itself prove that 507 modules are reachable. The 507 count comes from the
separate hardened closure analysis, not from that Lean probe.

`StageEstimatesMomentBlindnessProbe.lean:155-173` proves only that the
abstract `StageEstimates` interface does not determine an arbitrary
five-coordinate debt vector. It is a countermodel to an inference from that
interface, not a statement that the selected construction is a zero field.

`SelectedWitnessInhabitationProbe.lean:22-42` pairs the inhabited `Witness`
proposition with an unrelated nonzero ghost debt. This demonstrates that the
exported type does not constrain an extra debt variable; it does not evaluate
the selected field’s moments.

## 4. Pressure and force claims require the same calibration

`NavierStokes/R3/PressureRecovery.lean:33-45` defines a comparison hypothesis
over two velocity-pressure pairs. `gradient_recovery` at lines 407-414 and
`NavierStokes/R3/ActualPressureFlux.lean:36-58` derive comparison identities
for pressure differences using compact test functions. The probe
`PressureRecoveryAbsolutePremiseProbe.lean:28-66` shows that this comparison
interface accepts identical zero velocities with an arbitrary common smooth
pressure. That proves a limitation of the interface; it does not prove that
the selected pressure violates a global Poisson equation.

`NavierStokes/R3/ProblemStatement.lean:99-116` explicitly requires pressure
support, smoothness, periodicity, residual equality, divergence freedom,
energy boundedness, and speed blow-up in `CandidateProperties`. Any claim
that these properties are absent is false. The live pressure objection is
narrower: no selected-field theorem has been identified that supplies an
absolute global Poisson representative and transports the paper’s pressure
semantics into the endpoint.

`CandidateFromLimits.force_eq_activated_residual` at
`CandidateFromLimits.lean:108-112` and `candidate_properties` at
`CandidateFromLimits.lean:165-182` do establish the residual equality for the
constructed force on the pre-singular interval. The fixed-force perturbation
extension proves trajectory dependence under a new perturbation; it does not
refute the literal existential C/D proposition.

## 5. Current classification

| Claim | Source result | Classification |
|---|---|---|
| Five-moment files are absent or dead | False; selected closure reaches them | Retracted |
| `Witness` exports the paper’s five moments | No such conjunct at `ActualCandidateAssembly.lean:1121-1151` | Confirmed correspondence gap |
| `StageEstimates` alone determines five moments | Zero-field interface countermodel disproves this inference | Confirmed interface blindness |
| The selected field is zero or non-Newtonian | Not shown by these probes | Open, not established |
| Pressure recovery is an absolute selected pressure theorem | Comparison theorem only | Confirmed limitation |
| Compact pressure support alone forces triviality | No proof found | Retracted as an unconditional claim |
| Residual forcing is literally forbidden by CMI C/D | Not proved; C/D is existential | Retracted as a kernel disproof |
| Fixed-force perturbation changes the residual | Proved for the explicit compact divergence-free perturbation | Confirmed operator-level path dependence |

The remaining load-bearing calculation is the selected value-level transport
from the full Cartesian `tsum` through curl, localisation, periodisation,
`torusAverage`, and `barMoment`. Until that equality or a selected nonzero
remainder is proved, the correct publication verdict is **not established as
a CMI solution**, not `False`.

## 7. Fresh import-closure cross-check

A fresh source-only breadth-first traversal beginning at
`NavierStokes.ActualCandidateAssembly` found 507 reachable `NavierStokes.*`
modules. The relevant paths are:

```text
ActualCandidateAssembly
  -> ActualPhysicalPrefixFields -> TailGaugePotential -> ModulatedExterior
  -> BaseExterior -> AssembledSlowBase -> GlobalSlowProfiles
  -> PositiveOrderMoments

ActualCandidateAssembly
  -> InitialPhysicalData -> ActualPrimaryBounds -> CorrectionInitialization
  -> MeanRankUpdate -> FiveProfileMoments -> FiveRowRank
```

This is direct evidence against the claim that the five-moment files are dead
or unreachable. It is not evidence that their identities are transported to
the exported field. A source search over the full `NavierStokes` tree found no
declaration text joining `potentialSum` to `PositiveOrderMoments`,
`periodicVelocity` to `barMoment`, or `CandidateProperties` to `FiveRows`.
That negative search is a screening result, not a proof of absence; the
required next step remains declaration-level inspection of every candidate
bridge in the joined environment map.

## 8. Route meaning after direct source inspection

The reachable routes have different mathematical scopes and must not be
collapsed into one claim:

| Route | Direct source consumer | What is established | What is not established |
|---|---|---|---|
| `PositiveOrderMoments.Debt` | `AssembledSlowBase.extended_axial_primitive_zero` | Positive-order debt/moment identities are used in slow-base and exterior primitive arguments. | Equality of those moments with the final `ASum`, `BSum`, or `PSum` Cartesian observables. |
| `FiveRowRank.FiveRows` | `ActualCyclePreservation` through correction and rank-invariant declarations | The finite correction/update branch uses five-row constraints on its correction data. | A theorem identifying those correction rows with the final assembled velocity field's five paper moments. |
| `barMoment` | `GaugeDebtIncrement` and `LocalRankDefect` correction routes | The radial observable is used to express correction/debt changes. | A theorem applying `barMoment` to `MixedPeriodicAssembly.periodicVelocity` or the final `Witness` field. |
| `selected_witness` | `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` | The selected sums receive schedule, extension, residual, smoothness, force, energy, and blow-up consequences. | A named moment/debt equality in the exported proposition. |

The endpoint constructor passes the selected sums to
`CandidateConsequences.mixed_exists_force_with_consequences` with hypotheses
for smoothness, divergence, joint residual jets, away extensions, and the
origin blow-up. No `Debt`, `FiveRows`, `barMoment`, or five-tuple equality is
an input to that final constructor. This is a source-level scope result, not a
claim that the upstream correction mathematics is unused everywhere.

## 9. Partial bridge inventory and corrected negative claim

The review-side completion modules contain real partial transport results.
They prove finite-prefix curl expansions, cutoff-gradient commutator formulas,
local radial scalar identities, torus-average reductions, and typed
`barMoment` pullbacks. In particular, `SelectedPotentialProductionRadialScalar`
and `SelectedMixedProductionTorusAverage` reach selected production
expressions under explicit hypotheses. The earlier screening statement must
therefore not be read as “no theorem applies `barMoment` to any selected
expression”.

The narrower, source-supported result is:

> No inspected declaration exports the final equality identifying the named
> paper tuple \((M,I,J,S,C_p)\), or an equivalent promoted debt invariant, with
> the fully assembled selected Cartesian field after `potentialSum`, curl,
> localisation, periodisation, `torusAverage`, radial pullback, and `barMoment`.

The bridge inventory, including exact declaration coordinates and the six
remaining value-level obligations, is recorded in
`NavierStokesReview/evidence/selected_transport_bridge_inventory_2026-09-27.md`.
This correction removes an overbroad absence claim; it does not convert the
partial identities into the missing final equality.

The proposed files `StateRealization.lean` and `PhysicalFields.lean` are not
current standalone paths in this checkout. The chart declaration is in
`PhysicalResidualJetBounds.lean:927`, while physical germ transport is in
`ActualPhysicalPrefixFields.lean`. Any future search must use those live paths
and must not infer source facts from stale filenames.
