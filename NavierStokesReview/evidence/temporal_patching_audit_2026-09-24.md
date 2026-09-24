# Temporal patching audit

## Result

The requested discontinuity has not been proved. The inspected source does not
construct the selected field by switching between time intervals at stage
boundaries. It constructs an indexed family of stage fields and then applies
smooth spatial cutoffs and a scale-weighted sum. The constructor leaves an
adjacent-stage matching obligation open in the abstract, but that is not
evidence that the selected spacetime field has a temporal jump.

## Source ledger

| Source | Coordinates | What is proved | Boundary that remains |
|---|---:|---|---|
| `NavierStokes/GermCandidateAssembly.lean` | 52--61 | `initializedSeries` maps index `0` to `base + initial` and index `j+1` to `stages j`. | No relation between adjacent raw stage fields is imposed by this definition. |
| `NavierStokes/GermCandidateAssembly.lean` | 75--95 | `potentialSum_eq_base_germ` reduces the local sum to the base when the initial and later stages are eventually zero near a point. | This is a spatial/local filter statement, not a time-interface matching theorem. |
| `NavierStokes/GermCandidateAssembly.lean` | 146--159 | `origin_blowup` transfers the late origin behaviour of `FinalSlowBase` to the mixed sum. | It does not assert a temporal discontinuity between indexed stages. |
| `NavierStokes/ActualCandidateConstruction.lean` | 419--433 | `uncutPrefix_succ` makes a finite prefix additive, and `angularMeanStages_prefix` reconstructs the cycle mean. | No energy-gradient identity is attached to the prefix boundary. |
| `NavierStokes/ActualCandidateConstruction.lean` | 492--502 | Successor stage families are defined by the cycle's increment families. | The source does not identify these indices with disjoint time slices. |
| `NavierStokes/ActualCandidateConstruction.lean` | 638--653 | Chart potential parts split successor data into wave and stream components by algebraic addition. | No derivative mismatch follows from this algebraic split. |
| `NavierStokes/LocalPotentialRebundle.lean` | 78--119 | The selected potential and direct fields are `ContDiffOn ℝ ∞` on the preterminal domain when the summed schedule is smooth. | The theorem applies to the selected sums, not to an asserted piecewise-time glue. |
| `NavierStokes/TimeLocalization.lean` | 27--41 | The actual time activation is multiplication by a globally smooth `timeSwitch`; it preserves `ContDiffOn ℝ ∞`. | No non-smooth conditional or indicator cutoff is used here. |
| `NavierStokes/TimeLocalization.lean` | 74--96, 144--164 | After `t > 3/4`, activated fields and temporal derivatives agree locally with the incoming fields; the residual agrees as well. | This establishes late local jet agreement, not an independent Cauchy stability theorem. |
| `NavierStokes/MixedPeriodicAssembly.lean` | 166--177, 231--238 | Spatially cut residuals are smooth and inherit `VanishingJointJets` by local equality. | The inheritance is conditional on the incoming residual-jet premise. |
| `NavierStokes/MixedPeriodicAssembly.lean` | 283--320 | Boundary limits and locally uniform jet convergence follow from the residual-jet premise and away extensions. | The theorem does not derive those premises from an energy jump calculation. |

## Zero-sorry probe

`NavierStokesReview/src/probes/TemporalPatchingDiscontinuityProbe.lean`
compiles with exit code 0 and contains no `sorry`, `axiom`, or `unsafe`.
It records four facts:

1. The indexed `initializedSeries` constructor does not itself enforce equality
   between `base + initial` and the first raw stage.
2. Finite uncut prefixes change additively at `N + 1`.
3. The selected time activation is presingularly smooth.
4. Late temporal derivatives agree because the switch is locally constant at
   one after `3/4`.

The first fact is a real interface obligation. It is not a proof that the
actual selected sums jump, because the endpoint smoothness theorems apply to
the summed fields and their cutoffs. No theorem in the inspected files turns
the stage index into a time partition, and no theorem was found equating a
stage boundary jump with a kinetic-energy jump.

## Audit classification

`CTR-017` is therefore retained as an open verification question, not promoted
to a proved defect:

* confirmed: the raw indexed constructor has no adjacent-stage matching field;
* confirmed: the selected activation and summed fields have smoothness lemmas;
* not proved: a temporal discontinuity of the selected velocity or force;
* not proved: a higher-order energy-gradient jump;
* remaining target: derive a selected-field theorem that identifies a genuine
  temporal boundary with a nonzero derivative mismatch, or close this route.
