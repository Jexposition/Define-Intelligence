# Priority 135 source review: external moment, realisation, pressure, and summation junctions

**Date:** 2026-09-28
**Scope:** Twelve OpenAI Navier–Stokes source files outside the already reviewed endpoint packaging files.  This tranche tests both positive construction evidence and the exact final-field transport boundary.

## Audit rule

This review does not infer a theorem from an import edge, a name, or a numerical pattern.  A final five-observable transport claim would require a declaration whose inputs and output connect the actual selected Cartesian field, after the relevant lift, curl, localisation, summation, and pressure construction, to the paper-level observables

\[
  (M,I,J,S,C_p).
\]

The absence statement below is bounded to these twelve files and their inspected declarations.  It is not a repository-wide impossibility theorem.

## Source identity

| Source | Lines | SHA-256 | Review result |
|---|---:|---|---|
| `ActualCorrectionModels.lean` | 985 | `695f3c8b45c457e0ef4bca87eb60a61d9bcd45d71af9149408958d8bded2d451` | local model/fibre and differential-operator agreement |
| `ClosedIntervalMomentRepair.lean` | 236 | `18851a9865cfa2a977864baa433114eb5b7ffd95817df9bbcc11f42cb73abccb` | exact interval profile correction branch |
| `ExponentialMomentMatrix.lean` | 124 | `a2564d016df62d730ff3a29e5d011df48a9e3dd5899a6b3cd2a285abc32957cc` | exponential moment-matrix invertibility |
| `GenericAngularRecovery.lean` | 162 | `a27c91489cd0f59ca181468acbf4212e7dc70dee50d0d246c77b3b99237b4df4` | angular recovery, smoothness, and divergence |
| `GenericSolenoidalRealization.lean` | 229 | `ea59a93821cb70b5a002111c2aa13dee3fc15cbb2a8a9d21f36a56b64bd05ad3` | smooth Cartesian solenoidal realisation and germ facts |
| `GenericSummationRealization.lean` | 133 | `fa6cffeb0295506ab02696cacfe4e808609c570985bbcbdb018ed2ef114da91d` | raw-rate to flat-residual summation interface |
| `LocalHeatExterior.lean` | 153 | `15d4d97dba4b8ff2b947a273e4f9247f1688ef7961b912096ebda2df8813481a` | local heat-exterior axial/curl identities |
| `LocalHeatPressure.lean` | 107 | `e4ba79ca0b2409865dc26cc33319a74ce5438670a9ab59699ca0b808f46a25f6` | positive-radius pressure tail integrals |
| `LocalResidualFlatness.lean` | 131 | `1c0360f772cfbc7842d045c6221afecd628d4fa8a64524a2f52556530986ae0b` | all-order residual jet-rate schedule |
| `MeanLocalDefectBounds.lean` | 333 | `a01f1e7beb81c00239dca107afc5c66a9a6148f09749c7438499fbaadd956091` | three-component local rank/debt remainder classes |
| `MeanStageContinuation.lean` | 732 | `d7a13c389d6afbb0122142ac8ca15567ac27802b6bba6ba8b9ebae00e608acd2` | periodic primitive and pressure continuation |
| `ModulatedProfileJetRates.lean` | 443 | `6b9fb69986b1fb9ae35e90977b6cc53c4fe43f795e01265a65190f55c5258ae4` | exact reduced-profile moment repair/restoration plus rates |

## Positive evidence found

### Reduced-profile moment repair is real

`ModulatedProfileJetRates.lean` defines a `SmoothRepairFamily` whose `solves` field explicitly states an exact `FiveProfileMoments.physicalMoments ... = d N eta` equation.  `exists_smooth_repair_family` constructs smooth repaired profiles, and `exists_with_moment_repair_all_jets` proves repaired profiles remain in the cone, agree with the target `profileRows` outside the patch, and satisfy the required derivative-rate bounds.  This is genuine five-moment repair at the reduced profile/history layer.

`ClosedIntervalMomentRepair.lean` independently supplies a local smooth branch for a quadratic interval correction equation, including the pointwise equation, smoothness, and local uniqueness within the stated \(C^0\) ball.  `ExponentialMomentMatrix.lean` proves the relevant exponential moment matrices are invertible under its hypotheses.

These facts correct the overclaim that the five-moment machinery is absent or dead.  They do not, by themselves, identify the final global Cartesian field with the repaired reduced profile observables.

### Local rank and continuation machinery is real

`MeanLocalDefectBounds.lean` proves support and component-specific remainder classes for the actual rank increments, then derives three-component physical debt/rank-stage bounds.  `MeanStageContinuation.lean` propagates periodic primitives, pressure primitives, radial sources, and continuation agreements.  These are substantive local transport results, not empty interfaces.

The reviewed output remains local or stage-level: it does not state a final equality

\[
  \operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p)
\]

for the exported Cartesian field.

### Cartesian realisation and residual control are real

`GenericSolenoidalRealization.lean` proves smoothness, divergence-free properties, cutoff-before-curl/germ behaviour, and outer-region agreement for its constructed velocity.  `GenericAngularRecovery.lean` proves angular recovery and axis-aware divergence facts.  These results refute any claim that this tranche is merely a scalar or purely axial toy.

`GenericSummationRealization.lean` and `LocalResidualFlatness.lean` provide rate-to-realisation and all-order residual-jet conclusions under their explicit hypotheses.  The conclusion is residual regularity/flatness, not global radial-moment preservation.

`LocalHeatExterior.lean` proves local axial-potential/curl identities.  `LocalHeatPressure.lean` proves a positive-radius canonical radial pressure-tail integral and its integrability conditions.  Therefore the correct criticism is not “there is no pressure formula”; it is that this tranche does not establish the absolute global selected-field pressure semantics or the five-observable transport theorem.

## Boundary test: does this tranche close the selected-field bridge?

The inspected declarations in these files do not have an output target of `ActualCandidateAssembly.Witness`, `selected_witness`, `CandidateProperties`, or the final exported `VelocityField` together with a theorem identifying its five paper-level observables.  The source-level results terminate at one of four narrower layers:

| Layer | What is proved | What is not proved here |
|---|---|---|
| Profile repair | exact reduced `physicalMoments` equation and restored `profileRows` | equality for the final Cartesian field |
| Rank/debt stage | local three-component debt and remainder classes | identification with the five paper observables after global assembly |
| Cartesian realisation | smooth/divergence-free curl and germ properties | preservation of the five radial observables through the complete pipeline |
| Summation/pressure/residual | rate, pressure-tail, continuation, and residual-flatness facts | final `selected_witness` moment/pressure transport |

The relevant pipeline remains a required value-level calculation:

\[
\text{profile}
\to \text{potential}
\to \text{curl/localisation}
\to \text{stage sum}
\to \text{Cartesian field}
\to \text{radial observable}.
\]

The presence of commutator terms or tails is not itself a proof that the defect is nonzero.  A cancellation theorem could still exist elsewhere.  This tranche found no such final theorem, but it also does not prove that such a theorem is impossible.

## Classification

| Issue | Status after this tranche | Reason |
|---|---|---|
| CTR-005, selected-field correspondence | **Not established at the inspected final-field boundary** | genuine upstream profile/rank/curl/rate results are present, but no inspected declaration closes them to the final five-observable Cartesian equality |
| Transformation defect \(\Delta m\neq0\) | **Open calculation** | no nonzero numerical or Lean theorem was obtained here |
| Impossibility of transport | **Not proved** | no contradiction or impossibility theorem was obtained |
| CTR-012 force provenance | **No new escalation** | this tranche does not change the separate residual-force evidence |
| Kernel-level `False` | **Not derived** | no contradiction was constructed |

## Required next source checks

1. Trace every concrete output of `ModulatedProfileJetRates` and `MeanLocalDefectBounds` into the actual selected potential/sum declarations.
2. Inspect the exact declarations that consume the resulting objects in `ActualCandidateConstruction`, `ActualCandidateAssembly`, `CandidateFromLimits`, and `R3/ActualCandidate`.
3. Search those declaration bodies for a value-level radial observable, not merely imported moment symbols or local profile equalities.
4. If no bridge is found, keep CTR-005 as a correspondence failure.  Escalate only after a concrete field-level nonzero defect or formal impossibility theorem is proved.

**Tranche conclusion:** the source supports a stronger and more accurate statement than “the moments are missing”: OpenAI has real reduced-profile and local correction machinery, but this tranche does not establish its transport into the final exported Cartesian witness.
