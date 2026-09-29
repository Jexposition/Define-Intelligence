# Full external-source structural profile

This report profiles every indexed Lean file outside the captured
Navier--Stokes endpoint import closure. `outside_captured_endpoint_closure`
is a scoped graph fact, not a dead-code or irrelevance claim.
The report is source-accounting evidence, not a semantic theorem and not
a proof that any marker is used by a mathematical claim.

- Source root: `.`
- Register input: `NavierStokesReview\evidence\semantic_coverage_register_full_2026-09-28.json`
- Files profiled: **2204**
- Files containing admitted-token matches: **2**

## Branch counts

| Branch | Files |
|---|---:|
| `ComparatorChallenges` | 2 |
| `Euler` | 1839 |
| `Euler.lean` | 1 |
| `NavierStokes` | 229 |
| `NavierStokes.lean` | 1 |
| `NavierStokesReview` | 132 |

## Marker-family counts

| Family | Files |
|---|---:|
| `cmi_paper` | 55 |
| `comparison` | 176 |
| `endpoint` | 48 |
| `geometry` | 1223 |
| `moments` | 130 |
| `periodicity` | 662 |
| `pressure` | 722 |
| `regularity_energy` | 1818 |
| `residual_force` | 2202 |
| `series_limits` | 1560 |
| `support_localisation` | 864 |

## Highest-review-risk structural rows

This queue is prioritisation only. Every row remains unreviewed semantically
until a bounded source report records the declarations and proof obligations.

| Path | Branch | Lines | Decls | Marker families | Admitted tokens |
|---|---|---:|---:|---|---:|
| `ComparatorChallenges/Euler.lean` | `ComparatorChallenges` | 186 | 13 | cmi_paper, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 2 |
| `ComparatorChallenges/NavierStokes.lean` | `ComparatorChallenges` | 286 | 18 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force | 2 |
| `NavierStokes/CandidateAssembly.lean` | `NavierStokes` | 231 | 16 | cmi_paper, endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3CandidateStrong.lean` | `NavierStokes` | 123 | 8 | comparison, endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3Continuity.lean` | `NavierStokes` | 108 | 6 | cmi_paper, comparison, endpoint, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3CandidateUniqueness.lean` | `NavierStokes` | 116 | 4 | comparison, endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/ComparatorTheorem.lean` | `NavierStokes` | 55 | 2 | cmi_paper, comparison, endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` | `NavierStokesReview` | 321 | 31 | endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/LocalAngularGrowth.lean` | `NavierStokes` | 251 | 18 | endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/LocalScheduleWitness.lean` | `NavierStokes` | 165 | 9 | cmi_paper, endpoint, geometry, periodicity, pressure, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/PeriodicPaperTheorem.lean` | `NavierStokes` | 164 | 7 | cmi_paper, endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/audit/EnvironmentDependencyExport.lean` | `NavierStokesReview` | 86 | 5 | cmi_paper, comparison, endpoint, periodicity, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3Blowup.lean` | `NavierStokes` | 78 | 4 | comparison, endpoint, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean` | `NavierStokesReview` | 139 | 4 | endpoint, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/PeriodicPaperComparator.lean` | `NavierStokes` | 54 | 3 | cmi_paper, comparison, endpoint, periodicity, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokes/R3/H3CompactCurve.lean` | `NavierStokes` | 76 | 3 | comparison, endpoint, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/PaperLocalization.lean` | `NavierStokes` | 52 | 2 | cmi_paper, comparison, endpoint, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3MaximalLifespan.lean` | `NavierStokes` | 118 | 12 | cmi_paper, comparison, endpoint, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokes/R3/ComparatorBridge.lean` | `NavierStokes` | 90 | 3 | comparison, endpoint, geometry, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/extensions/SameDatumFixedForcePerturbation.lean` | `NavierStokesReview` | 198 | 15 | endpoint, geometry, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokes/R3/ParabolicScaling.lean` | `NavierStokes` | 141 | 10 | endpoint, geometry, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokes/R3/ParabolicCalculus.lean` | `NavierStokes` | 87 | 9 | endpoint, geometry, pressure, residual_force, series_limits, support_localisation | 0 |
| `NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean` | `NavierStokesReview` | 201 | 6 | cmi_paper, endpoint, periodicity, pressure, residual_force, series_limits | 0 |
| `NavierStokes/PeriodicPaperScalingSupport.lean` | `NavierStokes` | 111 | 4 | cmi_paper, endpoint, periodicity, pressure, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/probes/AnalyticObjectionsProbe.lean` | `NavierStokesReview` | 58 | 3 | endpoint, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean` | `NavierStokesReview` | 49 | 3 | endpoint, moments, periodicity, pressure, residual_force, support_localisation | 0 |
| `NavierStokes/ComparatorR3Theorem.lean` | `NavierStokes` | 46 | 2 | comparison, endpoint, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/probes/SelectedForceOriginCompositionProbe.lean` | `NavierStokesReview` | 148 | 2 | endpoint, periodicity, pressure, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/ViscousUniqueness.lean` | `NavierStokes` | 59 | 1 | comparison, endpoint, geometry, pressure, regularity_energy, residual_force | 0 |
| `NavierStokesReview/src/external_semantic/FixedForcePerturbationStability.lean` | `NavierStokesReview` | 39 | 4 | endpoint, geometry, pressure, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean` | `NavierStokesReview` | 85 | 3 | endpoint, pressure, regularity_energy, residual_force, series_limits | 0 |
| `NavierStokesReview/src/probes/SelectedWitnessAttackBoundaryProbe.lean` | `NavierStokesReview` | 49 | 3 | cmi_paper, endpoint, moments, residual_force, series_limits | 0 |
| `NavierStokesReview/src/refutations/SelectedPeriodicSupportTransportGate.lean` | `NavierStokesReview` | 61 | 2 | endpoint, geometry, periodicity, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/audit/WholeSpaceAxiomAudit.lean` | `NavierStokesReview` | 14 | 0 | cmi_paper, comparison, endpoint, periodicity, residual_force | 0 |
| `NavierStokesReview/src/probes/HeadlineAxiomProbe.lean` | `NavierStokesReview` | 12 | 0 | cmi_paper, comparison, endpoint, periodicity, residual_force | 0 |
| `NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean` | `NavierStokesReview` | 49 | 4 | endpoint, moments, pressure, residual_force | 0 |
| `NavierStokesReview/src/probes/SelectedMomentBridgeAudit.lean` | `NavierStokesReview` | 51 | 3 | endpoint, moments, pressure, residual_force | 0 |
| `NavierStokesReview/src/probes/GlobalTransportBridgeProbe.lean` | `NavierStokesReview` | 45 | 2 | endpoint, pressure, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/extensions/EndpointContractNonImplication.lean` | `NavierStokesReview` | 27 | 1 | endpoint, pressure, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/probes/SelectedDivergenceAudit.lean` | `NavierStokesReview` | 32 | 1 | endpoint, geometry, pressure, residual_force | 0 |
| `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | `NavierStokesReview` | 49 | 4 | endpoint, moments, residual_force | 0 |
| `NavierStokesReview/src/probes/FiveRowCollisionBoundaryProbe.lean` | `NavierStokesReview` | 53 | 4 | endpoint, moments, residual_force | 0 |
| `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean` | `NavierStokesReview` | 45 | 4 | endpoint, moments, residual_force | 0 |
| `NavierStokesReview/src/extensions/UnforcedBranchSpecification.lean` | `NavierStokesReview` | 43 | 3 | endpoint, pressure, residual_force | 0 |
| `NavierStokesReview/src/extensions/SelectedResidualProvenance.lean` | `NavierStokesReview` | 26 | 1 | endpoint, pressure, residual_force | 0 |
| `NavierStokesReview/src/probes/ActualCandidateAssemblyIsolationProbe.lean` | `NavierStokesReview` | 36 | 1 | endpoint, moments, residual_force | 0 |
| `NavierStokesReview/src/audit/SameDatumAxiomAudit.lean` | `NavierStokesReview` | 8 | 0 | endpoint, residual_force, support_localisation | 0 |
| `NavierStokesReview/src/audit/agent_check_axioms.lean` | `NavierStokesReview` | 3 | 0 | endpoint, residual_force | 0 |
| `NavierStokesReview/src/probes/MainAxiomProbe.lean` | `NavierStokesReview` | 5 | 0 | endpoint, residual_force | 0 |
| `NavierStokesReview/src/probes/SelectedDependencyAxiomProbe.lean` | `NavierStokesReview` | 16 | 0 | endpoint, residual_force | 0 |
| `Euler/EulerProof.lean` | `Euler` | 20755 | 1213 | comparison, geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/CorrectionInitializationNoOptions.lean` | `NavierStokes` | 5573 | 390 | comparison, geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3DifferenceStress.lean` | `NavierStokes` | 145 | 6 | comparison, geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/SignedRequestContinuation.lean` | `NavierStokes` | 751 | 100 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/MeanStageContinuation.lean` | `NavierStokes` | 732 | 73 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3WeakPressure.lean` | `NavierStokes` | 183 | 18 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ComparatorMaximalFields.lean` | `Euler` | 128 | 17 | cmi_paper, comparison, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3SpaceTimeCalculus.lean` | `NavierStokes` | 141 | 15 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3SmoothPressure.lean` | `NavierStokes` | 146 | 14 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3PressureDistribution.lean` | `NavierStokes` | 148 | 13 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketForwardInitializedResidualEquation.lean` | `Euler` | 135 | 11 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketInitializedResidualEquation.lean` | `Euler` | 136 | 11 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3CutoffTestFields.lean` | `NavierStokes` | 96 | 9 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3LocalEnergyEvolution.lean` | `NavierStokes` | 78 | 4 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/Solution.lean` | `Euler` | 75 | 3 | cmi_paper, comparison, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketForwardUniformFlow.lean` | `Euler` | 235 | 1 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketInitializedUniformFlow.lean` | `Euler` | 238 | 1 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/PaperAdditionalResults.lean` | `NavierStokes` | 30 | 0 | cmi_paper, geometry, moments, periodicity, pressure, regularity_energy, residual_force, support_localisation | 0 |
| `NavierStokes/WaveStageContinuation.lean` | `NavierStokes` | 1995 | 162 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/InitialHarmonicContinuation.lean` | `NavierStokes` | 1459 | 159 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/ActualParticularPhysicalData.lean` | `NavierStokes` | 1783 | 151 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/InitialDyadicSource.lean` | `NavierStokes` | 658 | 74 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/CycleContinuationInvariant.lean` | `NavierStokes` | 665 | 57 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/FiniteEnergyTruncation.lean` | `Euler` | 494 | 50 | comparison, geometry, periodicity, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokesReview/src/external-semantic/Gap.lean` | `NavierStokesReview` | 644 | 47 | cmi_paper, comparison, geometry, periodicity, pressure, regularity_energy, residual_force | 0 |
| `NavierStokes/NativeDyadicRegularity.lean` | `NavierStokes` | 407 | 34 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketHistory.lean` | `Euler` | 176 | 31 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/SupportedActualContext.lean` | `NavierStokes` | 391 | 30 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketPrimaryPressure.lean` | `Euler` | 247 | 25 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/LocalPotentialRebundle.lean` | `NavierStokes` | 271 | 25 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketForwardPrimary.lean` | `Euler` | 138 | 21 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketHistoryPressure.lean` | `Euler` | 190 | 20 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketPrimaryField.lean` | `Euler` | 138 | 18 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketProvider.lean` | `Euler` | 177 | 18 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/EulerSingularity.lean` | `Euler` | 153 | 17 | cmi_paper, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3CompactEnergy.lean` | `NavierStokes` | 218 | 16 | comparison, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketChildFieldMatch.lean` | `Euler` | 208 | 15 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketPrimaryPaths.lean` | `Euler` | 122 | 15 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ParentGeometryForwardChoice.lean` | `Euler` | 136 | 14 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ParentGeometryForwardChoiceNoOptions.lean` | `Euler` | 161 | 14 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketForcing.lean` | `Euler` | 108 | 14 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/GaussianHeatDerivative.lean` | `Euler` | 158 | 13 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/PacketForwardPrimaryShear.lean` | `Euler` | 166 | 13 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/SourceCylinderPressureField.lean` | `Euler` | 162 | 13 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketMatching.lean` | `Euler` | 98 | 13 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/MeanLocalDefectBounds.lean` | `NavierStokes` | 333 | 13 | geometry, moments, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/WaveDataReindex.lean` | `NavierStokes` | 269 | 13 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ComparatorSobolevEvolution.lean` | `Euler` | 161 | 12 | cmi_paper, comparison, geometry, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/ComparatorMaximalSolution.lean` | `Euler` | 113 | 11 | comparison, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/CylinderClassicalWordBounds.lean` | `Euler` | 138 | 11 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketForwardFactorization.lean` | `Euler` | 140 | 11 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketJoinedPressureAssembly.lean` | `Euler` | 174 | 11 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TransversePacketJoinedSupport.lean` | `Euler` | 124 | 11 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/CorrectionAssemblyParity.lean` | `Euler` | 130 | 10 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/CylinderReflection.lean` | `Euler` | 113 | 10 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/GevreyForcingComponents.lean` | `Euler` | 122 | 10 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/PacketForwardPressureRemainder.lean` | `Euler` | 155 | 10 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketInitializedPressureRemainder.lean` | `Euler` | 157 | 10 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ScalarEulerVorticity.lean` | `Euler` | 166 | 10 | comparison, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/ModulatedProfileJetRates.lean` | `NavierStokes` | 443 | 10 | geometry, moments, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/TruncationFamilySmooth.lean` | `Euler` | 111 | 9 | comparison, geometry, periodicity, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/LocalPaperTheorem.lean` | `NavierStokes` | 186 | 9 | cmi_paper, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/NaturalAxisJointAnalytic.lean` | `NavierStokes` | 163 | 9 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3CompactIntegration.lean` | `NavierStokes` | 106 | 9 | comparison, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3LocalizedPressure.lean` | `NavierStokes` | 170 | 9 | geometry, moments, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokesReview/src/probes/StageEstimatesMomentBlindnessProbe.lean` | `NavierStokesReview` | 173 | 9 | cmi_paper, geometry, moments, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/CorrectionEnergyTime.lean` | `Euler` | 143 | 8 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/CylinderOrbitSobolev.lean` | `Euler` | 123 | 8 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/GaussianHeatGenerator.lean` | `Euler` | 148 | 8 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/TransversePacketJoinedParity.lean` | `Euler` | 101 | 8 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3EnergyNorms.lean` | `NavierStokes` | 116 | 8 | comparison, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/GaussianHeatSmoothing.lean` | `Euler` | 99 | 7 | geometry, moments, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/GevreyCorrectionBound.lean` | `Euler` | 92 | 7 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/GradientReflection.lean` | `Euler` | 109 | 7 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3Comparison.lean` | `NavierStokes` | 120 | 7 | comparison, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ClassicalPressureCurl.lean` | `Euler` | 215 | 6 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketForwardExactFields.lean` | `Euler` | 155 | 6 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketInitializedExactLifted.lean` | `Euler` | 129 | 6 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketPrimaryGlobalShear.lean` | `Euler` | 127 | 6 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ParentGeometryJoinedChoice.lean` | `Euler` | 92 | 6 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ParentGeometryJoinedChoiceInvestigation.lean` | `Euler` | 128 | 6 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ParentPacketExactDivergence.lean` | `Euler` | 122 | 6 | geometry, moments, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/R3/H3PressureOrthogonality.lean` | `NavierStokes` | 119 | 6 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/DriftCorrectionForcing.lean` | `Euler` | 164 | 5 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/GevreyLowNorms.lean` | `Euler` | 77 | 5 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/PacketInitializedBounds.lean` | `Euler` | 100 | 5 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketJoinedResidualFields.lean` | `Euler` | 71 | 5 | geometry, moments, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketPrimaryGradeBounds.lean` | `Euler` | 158 | 5 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/SourceCylinderPressureMean.lean` | `Euler` | 114 | 5 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/WeightedCylinderEnergy.lean` | `Euler` | 144 | 5 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `NavierStokes/SharpCurrentParticularBounds.lean` | `NavierStokes` | 262 | 5 | comparison, geometry, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/ComparatorSingularityNorms.lean` | `Euler` | 46 | 4 | cmi_paper, comparison, geometry, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/CorrectionEnergyBound.lean` | `Euler` | 117 | 4 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/GevreyCorrectionForcing.lean` | `Euler` | 106 | 4 | comparison, geometry, periodicity, pressure, regularity_energy, residual_force, series_limits | 0 |
| `Euler/GevreyEnergyCutoff.lean` | `Euler` | 57 | 4 | comparison, geometry, periodicity, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketExactGlobalShear.lean` | `Euler` | 140 | 4 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketExactPressureError.lean` | `Euler` | 137 | 4 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketExactShearError.lean` | `Euler` | 118 | 4 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketForwardGlobalShear.lean` | `Euler` | 139 | 4 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |
| `Euler/PacketForwardHessianError.lean` | `Euler` | 135 | 4 | geometry, periodicity, pressure, regularity_energy, residual_force, series_limits, support_localisation | 0 |

## Required interpretation

1. An import or token hit is a navigation signal, not proof of theorem use.
2. A source file outside the selected endpoint closure may belong to Euler,
   a comparator, an alternate theorem, or an independent construction.
3. Admitted-token rows require direct source review and endpoint reachability
   checks; this profile does not infer contamination.
4. A paper-level bridge is cleared only by an inspected declaration and its
   proof term connecting the exact selected field to the claimed observable.
