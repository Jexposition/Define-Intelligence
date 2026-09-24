# Vanishing-jets and localisation source trace

## Disposition

The selected `VanishingJointJets` premise is not an undischarged field in the
final theorem. It is derived from finite residual-rate obligations supplied by
the selected cycle invariant and then consumed by the candidate-consequence
layer. The finite-rate obligations are substantial premises of the actual
stage-estimate construction. The source therefore proves an all-orders
residual limit conditional on those selected analytic estimates; it does not
derive the estimates from the paper's five moment identities in the same
theorem.

## Jet definition and orientation

`NavierStokes/JointResidualLimits.lean:67-86` defines the endpoint object:

```lean
def VanishingJointJets (f : SpaceTime → V) : Prop :=
  ∀ n : ℕ, Tendsto (iteratedFDeriv ℝ n f)
    (𝓝[SpacetimeEndpoint.openPast 1] ((1 : ℝ), (0 : Space))) (𝓝 0)
```

The quantifier is over every `n : ℕ`, so this is not an `H^3` truncation.
The same file derives all-order consequences through
`OneSidedExtension.jets_eventuallyEq` (`:99-106`), `boundaryLimits_joint`
(`:130-139`), and the locally uniform and compact versions (`:141-160`).
The selected endpoint filter is explicitly nonempty by `past_filter_neBot`
(`:162-165`).

## Where the selected premise is derived

| Source location | Declaration | Role |
|---|---|---|
| `ActualCycleResidualBounds.lean:1158-1172` | `Invariant.residual_jetRate` | Derives each finite `JetRate` from the invariant, physical data, state-realisation, native residual, and exterior estimates. |
| `ActualCycleResidualBounds.lean:1190-1206` | `finite_residual_rates` | Supplies the finite residual-rate field used by the actual stage estimates. |
| `ActualStageEstimates.lean:347-403` | `stageEstimates_of_representations` | Constructs `StageEstimates`; its `finite_residual` field is filled by `finite_residual_rates`. |
| `MixedCandidateAssembly.lean:67-90` | `StageEstimates.exists_schedule` | Passes the finite rates to the schedule theorem. |
| `MixedDiagonalResidual.lean:200-232` | `exists_physical_schedule_residual_zero` | Returns a schedule and `VanishingJointJets` for the mixed residual; its proof applies `SimilarityApproach.jet_tendsto_zero` for each natural derivative order (`:186-195`). |
| `GermCandidateAssembly.lean:223-224` | schedule extraction | Consumes the schedule and its all-order jet premise in the selected witness construction. |
| `CandidateConsequences.lean:185-215` | `mixed_exists_force_with_consequences` | Consumes `hz : VanishingJointJets originalResidual` to construct the final force and boundary jets. |

The remaining semantic limitation is precise: the exported
`VanishingJointJets` type does not contain the paper tuple `(M,I,J,S,C_p)` or
an equality identifying those moments with the residual. That is the remaining
CTR-005 bridge.

## Time activation audit

`NavierStokes/SmoothCutoffs.lean:245-285` defines the smooth switch and proves
that it is zero through the initial plateau, one from `t = 3/4` onwards, and
has zero derivatives of every positive order on the late side:

```lean
def timeSwitch (t : ℝ) : ℝ := 1 - scaledCutoff (4 / 3) t

theorem timeSwitch_contDiff : ContDiff ℝ ∞ timeSwitch

theorem timeSwitch_one_of_three_quarters_le {t : ℝ}
    (ht : 3 / 4 ≤ t) : timeSwitch t = 1

theorem timeSwitch_iteratedDeriv_late (n : ℕ) {t : ℝ}
    (ht : 3 / 4 < t) :
    iteratedDeriv (n + 1) timeSwitch t = 0
```

`TimeLocalization.lean:33-41` proves global smoothness of the activated
fields, while `:74-96` proves pointwise and local spacetime equality on the
late side. The strict inequality in the eventual-equality lemmas gives a
neighbourhood on which the switch is identically one; it is not a bare value
identity. `:127-143` records the transition formula, including the temporal
switch derivative and the full advection term. No temporal jump or truncated
derivative check was found.

## Spatial localisation audit

`NavierStokes/MixedPeriodicAssembly.lean:35-49` defines the periodic, cut, and
original residuals. The localisation uses the full residual operator:

```lean
def cutResidual (A v : VelocityField) (p : PressureField) : VelocityField :=
  fun z => navierStokesResidual (cutVelocity A v)
    (SpatialLocalization.cutPressure p) z.1 z.2

def periodicResidual (A v : VelocityField) (p : PressureField) : VelocityField :=
  fun z => navierStokesResidual (periodicVelocity A v)
    (SpatialLocalization.periodicPressure p) z.1 z.2
```

`periodicResidual_eventuallyEq_cut` (`:91-95`) and
`cutResidual_eventuallyEq_original` (`:97-101`) use
`ResidualRegularity.residual_eventuallyEq` (`NavierStokes/ResidualRegularity.lean:263-267`). That theorem compares the complete
time derivative, advection, Laplacian, and pressure-gradient expression. It
does not project onto selected Cartesian components or remove off-diagonal
shear terms. The plateau identity is an equality on a neighbourhood, so all
local derivatives of the residual agree there. At the origin,
`SpatialLocalization.zero_mem_plateau` supplies the required hypothesis.

## Debt/import boundary

`TimeLocalization.lean` imports `SmoothCutoffs`, `ResidualCalculus`, and
`ProblemStatement`; `MixedPeriodicAssembly.lean` imports
`PeriodicResidualLimits` and `DirectAngularDiagonal`. Neither file takes a
`FiveRowRank.Debt`, `PositiveOrderMoments.Debt`, or `(M,I,J,S,C_p)` argument.
The localisation theorems therefore do not transport, constrain, or erase the
debt vector. They are debt-blind field identities. This is not a proof that
the selected fields violate the moment equations; it is evidence that the
localisation step cannot supply the missing moment-realisation theorem.

## Review result

The flat origin force limit is supported by an all-orders `VanishingJointJets`
definition and by smooth local time and spatial equality, not by an `H^3`
shortcut or a value-only cutoff. The remaining adverse result is narrower and
stronger: the selected residual/force construction is not visibly connected to
the paper's five-moment transport and absolute pressure semantics. No temporal
discontinuity or dropped residual component was established by this trace.
