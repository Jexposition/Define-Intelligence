# Global cross-layer audit: source-to-claim ledger

Date: 2026-09-27  
Checkout: `review/cmi-first-navier-stokes-2026-09-22`  
Local source tree: `D:/Research Lab/Jexposition/Define Intelligence/Define-Intelligence-github`

This ledger records what the current Lean source actually connects. It does not infer a missing theorem from an import, a filename, a theorem name, or a successful build. `Proved` means that the cited declaration supplies the stated premise. `Not transported` means that the upstream fact exists but no selected-path equality or predicate was found at the cited export boundary. `Open` means that the source inspected so far does not settle the semantic question.

## Endpoint contract

| Source location | Declaration | What it requires | What it does not require |
|---|---|---|---|
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151` | `Witness` | A schedule, three potential sums, away extensions, a smooth forcing, `CandidateProperties`, `CandidateConsequences.Consequences`, H3-norm divergence, all-order force decay, and boundary-jet matching | No `PositiveOrderMoments.Debt`, `FiveRowRank.FiveRows`, `barMoment` equality, or named five-tuple equality on the exported fields |
| `NavierStokes/ActualCandidateAssembly.lean:1153-1175` | `witness` | Constructs the endpoint through `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` | Does not add a selected Cartesian five-moment observable |
| `NavierStokes/ActualCandidateAssembly.lean:1177-1181` | `selected_witness` | Specialises `witness` at the selected budget and threshold | Does not strengthen `Witness` |
| `NavierStokes/R3/ProblemStatement.lean:92-109` | `CandidateProperties` | Smoothness, compact spatial support, smooth positive-time force, zero initial velocity, divergence freedom, residual equality, finite kinetic energy, and speed blow-up | No named five-moment transport, absolute pressure-Poisson representative, or force-independence predicate |

The endpoint is therefore a real formal proposition, but its type is narrower than the paper's full explanatory chain. This is a correspondence result, not a claim that the upstream moment machinery is absent.

## Load-bearing path and transport status

| Layer | Source declarations | Source-supported result | Selected-path transport status |
|---|---|---|---|
| Five-moment/rank algebra | `PositiveOrderMoments.lean:23`; `FiveRowRank.lean:22,241`; `MeanRankUpdate.lean:30,137-168`; `DefectIncrementBounds.lean:214-219,607-646` | Five-dimensional debt, three-dimensional runtime debt, row identities, scaling, and radial moment linearity are formalised | Upstream algebra is reachable. A theorem equating the final selected Cartesian field observables with `(M,I,J,S,Cp)` was not found at `Witness`/`CandidateProperties` |
| Base profile | `EntranceAlignedBase.lean:666-690`; `FinalSlowBase.lean:finiteIdentities` and `speedUnbounded` | Named base-profile moment identities and base regularity/blow-up ingredients exist | These facts enter the germ and residual estimates; their final export as the five named observables is not present in the endpoint type |
| Finite stages | `MixedCandidateAssembly.lean:StageEstimates`; `ActualStageEstimates.lean:399`; `ActualCycleResidualBounds.lean:1190-1199` | Generic stage rates and `NativeBounds` feed the residual-rate construction | `StageEstimates` carries no five-coordinate payload |
| Germ assembly | `GermCandidateAssembly.lean:160-270` | Selects a schedule, builds `potentialSum`, `awayExtensions`, axis data, and invokes `mixed_exists_force_with_consequences` | The call supplies jet-rate, extension, support, and blow-up premises, not a field-level moment equality |
| Cartesian realisation | `PhysicalResidualJetBounds.lean:927-965`; `ActualPhysicalPrefixFields.lean` | Off-axis chart residual identity and local physical germs are proved | The chart identity is a residual-component identity on a positive-radius domain, not a theorem mapping the full selected field to the five scalar observables |
| Curl/localisation/periodisation | `MixedPeriodicAssembly.lean:28-48,51-89,147-164,231-245` | Smoothness, periodicity, local equality, origin equality, divergence freedom, and residual jet transfer are proved | The source does not, in these declarations, evaluate the five moment functional after `curl`, masks, periodisation, and infinite summation |
| Force | `CandidateFromLimits.lean:80-110`; `R3/PositiveTimeForce.lean:46-72` | The force is smooth and agrees with the selected activated residual before the endpoint; cutoff support is proved | This establishes residual provenance/path dependence, not an unconditional CMI contradiction |

## Pressure lane

| Source location | Declaration | Exact scope | Audit status |
|---|---|---|---|
| `NavierStokes/R3/PressureRecovery.lean:33-44` | `PressureRecovery.Hypotheses` | Compares two velocities and two pressures with smoothness, divergence freedom, equal residuals, and finite energy | Comparative premise only |
| `NavierStokes/R3/PressureRecovery.lean:391-419` | `gradient_recovery`, `pressure_gradient_recovery` | Recovers pairings for the gradient of `p-q` against compactly supported tests | Proved relative pressure recovery |
| `NavierStokes/R3/ActualPressureFlux.lean:38-56` | `pressure_flux_eq_canonical` | Identifies the pressure flux of the difference equation with a canonical Riesz pairing | Proved for a comparison difference |
| `NavierStokes/R3/WholeSpaceUniqueness.lean:28-68` | `classical_uniqueness_on_Icc` | Uses the comparison pressure flux and finite-energy bounds to prove equality before time one under the same residual/force | Proved relative uniqueness; not an absolute selected-pressure theorem |
| `NavierStokes/R3/ProblemStatement.lean:99` | `pressure_support` | Compact spatial support of selected pressure slices | Does not itself state the global Poisson equation |

The current source supports the narrower finding: comparison pressure recovery is real and active. The source inspected here does not establish an absolute selected-pressure Leray/Poisson representation. That is an open semantic correspondence question, not a proved contradiction. Compact support alone is not treated as a contradiction.

## Energy lane

| Source location | Declaration | Result |
|---|---|---|
| `NavierStokes/R3/CompactEnergy.lean:201-249` | `energy_balance` | Proves the forced whole-space energy identity with viscous dissipation and force work |
| `NavierStokes/R3/CompactEnergy.lean:323-340` | `hasDerivAt_energy_balance` | Justifies the time derivative on compact-supported slices |
| `NavierStokes/R3/CompactEnergy.lean:343-377` | `uniform_finite_energy` | Derives a uniform pre-singular kinetic-energy bound from compact support, the PDE, and a scalar Gronwall estimate |
| `NavierStokes/R3/ViscousEnergyBalance.lean:22-68` | `energy_balance_viscosity`, `hasDerivAt_energy_balance_viscosity` | Retains arbitrary viscosity explicitly |
| `NavierStokes/R3/WholeSpaceUniqueness.lean:28-68` | `classical_uniqueness_on_Icc` | Uses finite energy as an input for comparison, not as a missing endpoint property |

The earlier “missing energy bound” attack is cleared by source inspection. The remaining question is not whether an energy identity exists, but whether the field that satisfies it is the same selected field described by the paper's complete moment/pressure mechanism.

## Support, localisation, axis, and temporal activation

| Lane | Source evidence | Proved | Still open |
|---|---|---|---|
| Spatial localisation | `MixedPeriodicAssembly.lean:51-89` | Smooth periodisation, local equality to cut/original fields, origin equality | Global selected-field moment transport through masks and periodisation |
| Divergence | `MixedPeriodicAssembly.lean:147-164` | Periodised field is divergence free under the stated smoothness/support premises | No direct five-moment observable is attached to this result |
| Residual jets | `MixedPeriodicAssembly.lean:231-245`; `GlobalBaseError.lean:200-237` | Vanishing joint jets transfer through local equality; actual base error has all-jets flatness | No nonzero/remainder calculation for the selected global field |
| Off-axis chart | `PhysicalResidualJetBounds.lean:927-965` | Cartesian residual component identity on the positive-radius chart domain | Transport across the axis to the global radial observable |
| On-axis route | `GlobalBaseError.lean:200-237` | Separate origin-past vanishing-jets route | A single theorem identifying this route with the off-axis selected-field observable |
| Time activation | `TimeLocalization.lean:27-91,128-160` | Smooth cutoff; zero early; equality to the unactivated field after `3/4`; exact activation residual formula | No discontinuity is supported by this source; the remaining issue is semantic transport, not a cutoff kink |

The activation formula is especially important: before the late region the residual includes cutoff and derivative terms, while after `3/4` it agrees with the unactivated residual. Any critique must account for those terms rather than treat activation as an unproved jump.

## Force provenance lane

| Source location | Declaration | Result |
|---|---|---|
| `NavierStokes/CandidateFromLimits.lean:80-86` | `force` | Defines the force by smooth extension of traced residual jets; the comment explicitly says no force is an input to this definition |
| `NavierStokes/CandidateFromLimits.lean:99-110` | `force_eq_pastResidual`, `force_eq_activated_residual` | Proves equality with the selected activated residual for `0 ≤ t < 1` |
| `NavierStokes/R3/PositiveTimeForce.lean:46-72` | `force`, support and smoothness lemmas | Multiplies a supplied residual-like field by a smooth time cutoff and proves positive-time compact support |
| `CompactFixedForcePerturbation.lean` | Review-side extension | Shows a fixed-force perturbation changes the residual at the test point; this is a path-dependence result |

This supports CTR-012 as a provenance and forward-data objection. It does not by itself negate an existential proposition that permits choosing a smooth force after constructing a trajectory.

## Euler lane kept separate

The companion Euler tree is present under `Euler/`; it is not the Navier–Stokes endpoint. Examples of its own architecture are:

| Source location | Declaration | Scope |
|---|---|---|
| `Euler/PacketInductionStage.lean:23-138` | `Stage`, stage time/horizon/cost bounds | Indexed packet-stage data, not the Navier–Stokes `StageEstimates` interface |
| `Euler/BaseEulerParent.lean:22-159` | parent input, deformation, horizon | Parent-flow construction on an interval |
| `Euler/ChildParticleTime.lean:17-84` | child displacement/velocity/acceleration and time derivatives | Child-particle time-field algebra |
| `Euler/EulerSingularity.lean:29-133` | scalar/vector Euler evolution specifications and singularity theorem | Euler endpoint and its own imported chain |
| `docs/Euler_Parent_Child_Interval_Audit.md` | review record | Separate audit evidence, not a Navier–Stokes source declaration |

No Navier–Stokes conclusion is inferred from the Euler parent-child files. The Euler interval and Zeno questions require their own endpoint trace.

## Current classification

1. `CTR-005`: **Open correspondence failure.** Upstream five-moment and rank algebra is real and reachable. The selected `Witness` boundary does not export the named selected-field equality required to identify that algebra with the final Cartesian fields.
2. `CTR-012`: **Provenance/path-dependence objection, not endpoint `False`.** The force is defined from the residual and fails to remain the same under the review-side perturbation construction.
3. `AX-029/AX-030`: **Open absolute-pressure correspondence question.** Relative recovery and uniqueness are proved; an absolute selected-pressure Poisson/Leray transport theorem was not located in the inspected endpoint path.
4. Energy objection: **Cleared as a missing-bound claim.** The source contains the energy identity and uniform finite-energy theorem.
5. Temporal-cutoff discontinuity objection: **Cleared for the cited activation layer.** The source proves smooth activation and late local equality.
6. Global selected-field remainder: **Not computed.** No claim of a nonzero radial remainder or kernel-level `False` is made by this ledger.

## Reproducibility boundary

The current source map covers the full checkout inventory and declaration census. A fresh aggregate build was not completed within the bounded run; the last completed endpoint closure remains the dated build record in `NavierStokesReview/evidence/fresh_build_status_2026-09-27.md`. This ledger therefore reports source evidence and prior compiled evidence separately from a new build claim.

## Proposed transport-cluster cross-check

The suggested search locations were checked against the live tree and qualified declarations. The result is a correction of names, not a new contradiction.

| Suggested location | Live source result | Relevant role found | Transport conclusion |
|---|---|---|---|
| `LocalPaperTheorem.lean` | Present | Local theorem, uniform jet bounds, selected exterior residual zero | Local schedule and residual facts; no exported five-observable equality |
| `LocalResidualFlatness.lean` | Present | `AllResidualJetRates`, schedule and residual-rate construction | Generic rate contracts; no named five-moment payload |
| `PaperLocalization.lean` | Present | Local compact-candidate theorem and pressure agreement | Localisation/candidate packaging; no final moment identity |
| `StateRealization.lean` | Not a live path | `chartIdentity` is in `PhysicalResidualJetBounds.lean` | Search must follow the declaration, not the guessed filename |
| `PhysicalFields.lean` | Not a live path | Germ and Cartesian physical-field declarations are in `ActualPhysicalPrefixFields.lean` | Search must follow the declaration, not the guessed filename |
| `PhysicalResidualJetBounds.lean` | Present | `NativeBounds`, Cartesian pullback bounds, `chartIdentity` | Off-axis residual estimates; no five-observable export |
| `DefectIncrementBounds.lean` | Present | `barMoment`, shell/radial correction identities, five-row consequences | Correction/local radial data; not an identity for the final `ASum`/`BSum`/`PSum` field |
| `CorrectionState.lean` | Present | Three-coordinate state, increments, covariance and residual decomposition | State/update layer; no selected-witness moment equality |
| `MeanRankUpdate.lean` | Present | `Debt`, `scaleDebt`, scaled row identities | Preserves correction rows under scaling; no final-field observable |
| `ActualCyclePreservation.lean` | Present | Cycle-state recurrence and local invariant propagation | Stage/cycle propagation; no whole-space selected-field equality |
| `ReservedPatches.lean` | Present | Radial windows, support and patch geometry | Support geometry; no Cartesian `barMoment` transport |
| `EntranceAlignedBase.lean` | Present | Base alignment, entrance identities and profile constraints | Base-profile identities; no final selected-field export |
| `FinalSlowBase.lean` | Present | `finiteIdentities`, stress-zero and slow-base estimates | Slow-base identities and bounds; no selected `Witness` strengthening |

This cross-check confirms that the proposed clusters are useful search boundaries, but it does not justify the stronger statement that the moment branch is dead. The active source map records 2,790 current Lean modules and 50,191 source declarations; the compiled endpoint join records 572 source-joined modules and 2,218 current modules not captured in that endpoint environment. Those populations must not be conflated. “Accounted in the source census” means path/hash/import/declaration indexed. It does not mean that every module has been semantically audited or that every paper assertion has been transported.

## Workspace publication boundary

The audit checkout is local at the time of this record. It is on
`review/cmi-first-navier-stokes-2026-09-22`, with origin
`https://github.com/Jexposition/Define-Intelligence.git`. Local `HEAD` is ahead of
the public branch and there are no staged changes or push operations recorded in
this audit pass. Therefore the GitHub branch page does not yet represent the
current local evidence bundle. This is a repository-control fact, not a
mathematical result.
