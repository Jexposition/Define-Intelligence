# Probe-logic re-audit: scope, quantifiers, and admissible conclusions

**Date:** 2026-09-28
**Purpose:** Harden the review against a common failure mode: a valid Lean theorem being given a stronger prose interpretation than its quantifiers support.

## Executive result

The current probes support three different kinds of result:

1. **Interface non-entailment:** the exported `Witness` and generic `StageEstimates` contracts do not themselves contain the selected-field five-moment equality.
2. **Selected-path operator sensitivity:** the selected candidate is not stable under a formally specified same-datum, smooth, compactly supported, divergence-free perturbation while holding the force fixed.
3. **Open value-level question:** no reviewed probe yet computes the actual post-curl, localised, periodised, `tsum`-assembled field against the five paper observables and proves a nonzero defect.

Only (3) would establish a concrete selected-field mismatch. None of these probes, by itself, proves `False` for the exported C/D theorem.

## Scope matrix

| Source | Exact result proved | What it does **not** prove | Correct classification |
|---|---|---|---|
| `StageEstimatesMomentBlindnessProbe.lean:33-176` | A generic `StageEstimates` contract has a zero-field inhabitant and does not determine an arbitrary five-coordinate debt. | It does not show that the concrete `GluedStageEstimates.actualStageEstimates` used by `selected_witness` is zero or independent of upstream profile data. | Valid generic-interface countermodel. |
| `SelectedWitnessAttackBoundaryProbe.lean:32-40` | `Witness ...` does not imply that every externally supplied `Debt` is zero. | It does not mention a moment functional of the selected Cartesian field and does not prove the selected field has a nonzero debt. | Valid type-level non-entailment. |
| `SelectedWitnessInhabitationProbe.lean:31-41` | The witness can coexist with an externally defined nonzero `ghostDebt`; the debt is not a field of the proposition. | A ghost value is not a selected physical observable. It cannot be reported as a field-level counterexample. | Valid packaging diagnostic; weak as a physical refutation. |
| `SelectedEndpointMomentTransportObstruction.lean:37-49` | Same external-payload compatibility and non-entailment statement as above. | It does not establish that no transport theorem exists elsewhere, nor that transport is mathematically impossible. | Valid endpoint-contract diagnostic. |
| `SelectedBarMomentInterface.lean:20-57` | A point-to-spacetime pullback gives an exact `barMoment` rewrite; the required pullback data is explicit. | It does not prove that the production selected field has the required pullback or that its five values equal the paper tuple. | Valid missing-data specification. |
| `SelectedCycleMomentTransport.lean:20-72` | The selected cycle preserves two local zero-mass rows and hence two local `barMoment` values. | It does not identify those two rows with all five paper moments or transport them through the final Cartesian endpoint. | Positive intermediate result; endpoint bridge remains open. |
| `SelectedBaseMomentCompatibilityProbe.lean:26-58` | The selected slow-base construction has genuine positive-order moment identities, finite residual identities, and a speed-unbounded property under its stated hypotheses. | It does not identify the reduced base profiles with the final global Cartesian `barMoment` observables. | Positive upstream result; no endpoint transport. |
| `SelectedTorusLiftImageScope.lean:28-110` | The physical lift image satisfies a radial-coordinate restriction, and an auxiliary integration point lies outside that image. | It does not prove that the omitted region contributes nonzero mass or that the selected moment is wrong. | Exact image-scope obligation. |
| `PressureRecoveryAbsolutePremiseProbe.lean:28-48` | The comparative pressure hypotheses admit identical zero velocity and identical pressure. | It does not prove that the selected pressure lacks an absolute Poisson representative. | Comparative-vs-absolute scope diagnostic only. |
| `SameDatumFixedForcePerturbation.lean:95-159` | A smooth, compactly supported, divergence-free perturbation vanishing at initial time has a nonzero residual defect at an interior switch, so the selected candidate is not stable under the explicitly defined fixed-force perturbation predicate. | It does not show the perturbation is a second solution of the same Cauchy problem, and it does not negate the literal existential C/D proposition. | Formal operator/path-dependence result; causal-provenance criticism. |
| `SelectedWitnessEndpointResidualProbe.lean:23-171` | Selected origin speed tends to infinity while the selected residual tends to zero; a positive residual-to-speed lower bound is incompatible with those two facts. | It does not prove that such a lower bound is a premise of the OpenAI endpoint. | Conditional residual-cancellation result. |

## Corrections to unsafe prose

The following formulations are prohibited in the audit unless a new field-level theorem supplies the missing premises:

- “The five moments are absent from the code.”  The source contains real upstream moment and rank machinery.
- “The endpoint uses only generic rates.”  The concrete selected construction also consumes concrete stage and physical data; the precise finding is that the exported contract does not expose the final moment equality.
- “Curls and cutoffs destroy the moments.”  They introduce derivative and boundary terms. Exact cancellation remains possible until the actual integral is evaluated.
- “The ghost-debt probe proves the selected field is wrong.”  It proves only that the `Witness` proposition does not constrain an external debt variable.
- “The fixed-force perturbation disproves CMI Alternative (C) or (D).”  It proves failure of the explicitly defined fixed-force stability predicate, not failure of the literal existential theorem.
- “The pressure probe proves compact pressure is impossible.”  The probe is comparative. A separate absolute Poisson/pressure theorem is required.
- “Zero percent of the paper is formalised.”  Substantial local profile, correction, curl, localisation, energy, and comparison results are formally present. The unresolved point is the complete selected-field correspondence.

## Required next probe, with a non-toy target

The next calculation must define, using the actual selected declarations rather than a surrogate profile,

\[
\Delta m_k =
 \operatorname{barMoment}_k\!left(
   \operatorname{torusAverage}(\operatorname{periodise}
   (\nabla\!\times\operatorname{tsum}(A_j)\;\text{with the actual localisation}))
 \right)-m_k^{\mathrm{paper}}.
\]

The probe must expose every required map and hypothesis:

1. the actual `potentialSum`/stage family;
2. the actual spatial localisation and curl order;
3. convergence or finite-support justification for exchanging derivatives, sums, and integrals;
4. the physical-to-auxiliary point map used by `torusAverage`;
5. the five named target quantities;
6. a proved equality, a proved nonzero defect, or an explicit unresolved assumption.

Until this is completed, `CTR-005` remains a correspondence failure / not-established status, not a concrete field contradiction.

## Audit rule added

Every future probe report must contain separate headings **Proves**, **Does not prove**, and **Missing hypotheses**. A theorem may not be promoted from interface-level evidence to a selected-field refutation merely because it imports the selected witness or compiles without `sorry`.

## Newly audited conditional obstruction

The selected completion layer contains a stronger, but still conditional,
periodicity-support route. `SelectedMixedProductionRadialComponent` defines a
real mixed periodic scalar, `SelectedMixedRadialPeriodicity` transports unit
periodicity through the radial pullback, and
`SelectedMixedRadialSupportObstruction` proves that bounded radial support would
force that pullback to vanish. This does **not** yet combine with the R3
compact-support theorem: `R3CompactCandidate.Properties.velocity_support`
belongs to the compact localised field, while the radial pullback is defined
from `MixedPeriodicAssembly.periodicVelocity`. The missing steps are a global
field identity and support transport to `RadialAlias.RadiallySupported`.

The detailed source review is
[`priority_116_selected_periodic_radial_support_gate_source_review_2026-09-28.md`](priority_116_selected_periodic_radial_support_gate_source_review_2026-09-28.md).
This is now the priority falsification gate. It may produce `False` only if
the two missing hypotheses are proved for the same field; it does not justify a
premature nonzero-defect or contradiction claim.
