# Selected endpoint dependency routes

This compact report records exact compiled-environment routes from the exported endpoint to selected audit targets.
Routes are kernel-environment edges; source locations are attached only after exact declaration-name joining.

- Root: `NavierStokesR3.theorem_1_1`
- Environment nodes: `30721`
- Exact source matches: `22958`

| Target | Reachable | Source span | Edges |
|---|---:|---|---:|
| `NavierStokesR3.theorem_1_1` | `True` | `NavierStokes/R3/Theorem.lean:46-51` | `0` |
| `NavierStokes.ActualCandidateAssembly.selected_witness` | `True` | `NavierStokes/ActualCandidateAssembly.lean:1177-1182` | `3` |
| `NavierStokes.FiveRowRank.FiveRows` | `True` | `NavierStokes/FiveRowRank.lean:241-248` | `18` |
| `NavierStokes.FiveRowRank.Debt` | `True` | `NavierStokes/FiveRowRank.lean:22-24` | `12` |
| `NavierStokes.PositiveOrderMoments.Debt` | `True` | `NavierStokes/PositiveOrderMoments.lean:23-24` | `11` |
| `NavierStokes.MeanRankUpdate.scaleDebt` | `True` | `NavierStokes/MeanRankUpdate.lean:30-32` | `13` |
| `NavierStokes.MixedPeriodicAssembly.periodicVelocity` | `True` | `NavierStokes/MixedPeriodicAssembly.lean:36-39` | `3` |
| `NavierStokes.DefectIncrementBounds.barMoment` | `True` | `NavierStokes/DefectIncrementBounds.lean:214-217` | `16` |
| `NavierStokes.R3CompactCandidate.velocity` | `True` | `NavierStokes/R3CompactCandidate.lean:201-203` | `3` |
| `NavierStokesR3.ProblemStatement.CandidateProperties` | `True` | `NavierStokes/R3/ProblemStatement.lean:92-111` | `1` |

## Routes

### `NavierStokesR3.theorem_1_1`

`NavierStokesR3.theorem_1_1`

### `NavierStokes.ActualCandidateAssembly.selected_witness`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.ActualCandidateAssembly.selected_witness`

### `NavierStokes.FiveRowRank.FiveRows`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.ActualCandidateAssembly.directStages` -> `NavierStokes.ActualCandidateAssembly.directData` -> `NavierStokes.ActualCandidateAssembly.meanCycleInput` -> `NavierStokes.ActualCyclePreservation.state_invariant` -> `NavierStokes.ActualCyclePreservation.state_runInvariant` -> `NavierStokes.ActualCyclePreservation.initial_runInvariant` -> `NavierStokes.ActualCyclePreservation.initial_invariant` -> `NavierStokes.ActualCoreSupport.initial_invariant` -> `NavierStokes.ActualInitialization.initial_invariant` -> `NavierStokes.ActualInitialization.initial_cumulative` -> `NavierStokes.ActualInitialMean.initial_cumulative_bounds` -> `NavierStokes.ActualInitialMean.initial_bounds` -> `NavierStokes.ActualInitialMean.initial_bounds_of_primaryData` -> `NavierStokes.CorrectionInitialization.MovingInitialization.PrimaryMeanData.rank_zeroMasses` -> `NavierStokes.LocalRankDefect.RankGeometry.preserve_masses` -> `NavierStokes.FiveRowRank.FiveRows`

### `NavierStokes.FiveRowRank.Debt`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.ActualCandidateAssembly.potentialStages` -> `NavierStokes.ActualCandidateAssembly.initialPotential` -> `NavierStokes.ActualCandidateConstruction.streamMeanStages` -> `NavierStokes.ActualCandidateConstruction.streamNativeStages` -> `NavierStokes.ActualMeanPhysicalData.initialRankScalar` -> `NavierStokes.VariableGaugeMean.rankPotential` -> `NavierStokes.CorrectionState.rankDesiredAxial` -> `NavierStokes.MeanRankUpdate.desiredAxialFamily` -> `NavierStokes.MeanRankUpdate.Debt` -> `NavierStokes.FiveRowRank.Debt`

### `NavierStokes.PositiveOrderMoments.Debt`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.ActualCandidateAssembly.selected_witness` -> `NavierStokes.ActualCandidateAssembly.witness` -> `NavierStokes.GermCandidateAssembly.exists_candidate_witness_of_finite_stages` -> `NavierStokes.TailGaugePotential.finalPotential_awayExtensions` -> `NavierStokes.TailGaugePotential.realized_awayExtensions` -> `NavierStokes.ModulatedExterior.realized_exterior_coefficients` -> `NavierStokes.ModulatedExterior.realized_primitive_zero_all` -> `NavierStokes.AssembledSlowBase.extended_axial_primitive_zero` -> `NavierStokes.PositiveOrderMoments.Debt`

### `NavierStokes.MeanRankUpdate.scaleDebt`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.ActualCandidateAssembly.selected_witness` -> `NavierStokes.ActualCandidateAssembly.witness` -> `NavierStokes.ActualCandidateAssembly.initialPotential_support` -> `NavierStokes.ActualMeanStageData.initialRankSupport` -> `NavierStokes.ActualMeanPhysicalData.initialRankFamily` -> `NavierStokes.ActualMeanPhysicalData.initialRank_overlap` -> `NavierStokes.ActualMeanPhysicalData.Atlas.rank_overlap` -> `NavierStokes.RankStateCoherence.rankPotential_on` -> `NavierStokes.RankStateCoherence.rankDesiredAxial_on` -> `NavierStokes.RankStateCoherence.RankOn.desiredAxial` -> `NavierStokes.MeanRankUpdate.scaleDebt`

### `NavierStokes.MixedPeriodicAssembly.periodicVelocity`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.MixedPeriodicAssembly.periodicVelocity`

### `NavierStokes.DefectIncrementBounds.barMoment`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.ActualCandidateAssembly.directStages` -> `NavierStokes.ActualCandidateAssembly.directData` -> `NavierStokes.ActualCandidateAssembly.meanCycleInput` -> `NavierStokes.ActualCyclePreservation.state_waveData` -> `NavierStokes.ActualCyclePreservation.waveData_of_particular` -> `NavierStokes.ActualParticularMeanGain.postParticular_gain` -> `NavierStokes.CorrectionStep.waveStage_mean_gain` -> `NavierStokes.CorrectionStep.gaugeWaveStage_mean_from_covariance` -> `NavierStokes.GaugeDebtIncrement.waveStage_debt_change_mem` -> `NavierStokes.GaugeDebtIncrement.waveStage_debt_change_formula` -> `NavierStokes.GaugeDebtIncrement.debt_sub_eq` -> `NavierStokes.GaugeDebtIncrement.radialMoment_sub_on` -> `NavierStokes.LocalRankDefect.barMoment_sub_on` -> `NavierStokes.DefectIncrementBounds.barMoment`

### `NavierStokes.R3CompactCandidate.velocity`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.theorem_1_1_with_initial_rest` -> `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest` -> `NavierStokes.R3CompactCandidate.velocity`

### `NavierStokesR3.ProblemStatement.CandidateProperties`

`NavierStokesR3.theorem_1_1` -> `NavierStokesR3.ProblemStatement.CandidateProperties`
