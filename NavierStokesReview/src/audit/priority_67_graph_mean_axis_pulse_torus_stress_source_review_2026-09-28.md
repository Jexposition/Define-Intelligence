# Priority-67 Source Review: graph, interaction, axis, pulse, rebasing, and stress modules

Date: 2026-09-28
Scope: direct source inspection of six queued reachable modules in `NavierStokes/`.
Classification: source evidence only; no Lean build or endpoint axiom result is inferred here.

## Result

The six modules contain real mathematical infrastructure, but none is the missing endpoint transport theorem

\[
  \operatorname{barMoment}(u_{\mathrm{selected}})
  = (M,I,J,S,C_p).
\]

They divide into three roles:

| Role | Modules | What is actually established | Endpoint relevance |
|---|---|---|---|
| Coordinate and axis control | `GraphCalculus.lean`, `NaturalAxisRange.lean` | Off-axis derivative identities, mixed derivative commutation, root/cutoff parameter existence | Supplies hypotheses for local calculations; no global radial observable |
| Local interaction and pulse algebra | `LocalizedMeanInteraction.lean`, `PulseGrowth.lean`, `TorusMeanRequestRebase.lean` | Local class/rate estimates, scalar growth signs, request-coordinate equalities | Does not identify the final `tsum` field with radial moments |
| Reduced stress and jet control | `BaseStressClasses.lean` | Weighted chart composition, edge-distance growth, leading/higher/virtual stress classes | Real upstream stress control; no selected Cartesian `barMoment` theorem |

## Source findings

### `GraphCalculus.lean`

- Lines 6–12 document an auxiliary graph with physical variables `(r,t)` and an explicit off-axis restriction.
- Lines 22–51 define `radialSpeed`, `graph`, `pullback`, and the radial/time operators.
- Lines 69–105 prove the radial and time graph derivative identities and all-order graph regularity away from `r = 0`.
- Lines 181–209 prove mixed pullback derivative identities.

This is a genuine coordinate-calculus layer. It is not a torus-average, radial-integral, or selected-field moment theorem. The explicit `r ≠ 0` premise is also a scope boundary that must be transported separately if an endpoint observable integrates through the axis.

### `LocalizedMeanInteraction.lean`

- Lines 25–40 define `LocalMean`, `LocalMeanVector`, and component extraction.
- Lines 326–342 prove a uniform local real-mean cross class under operator, support, frequency, and zero-germ hypotheses.
- Lines 378–398 define/prove an interaction-block class for localised mean/wave interactions.
- Lines 451–469 package a residual-difference block after a mean update.

These declarations prove local regularity and rate contracts. They do not quantify a global Cartesian field, a radial averaging operator, or the five paper observables.

### `NaturalAxisRange.lean`

- Lines 12–23 define and instantiate the small parameter range.
- Lines 121–131 prove existence and uniqueness of the negative root of `H` in the specified interval.
- Lines 133–139 give a source lower bound at that root under pressure hypotheses.
- Lines 212–229 prove existence of positive cutoff parameters and smoothness of the cutoff.
- Lines 241–250 prove a strict base-source margin.

This is substantive axis/cutoff parameter control. It does not prove that cutoff commutator terms have zero or nonzero radial moment, and it does not compose the cutoff with the selected Cartesian `tsum` field.

### `PulseGrowth.lean`

- Lines 18–35 define the damped scalar `netGrowth` and establish denominator positivity.
- Lines 108–127 prove the positive/zero/negative classification relative to the threshold `|s| = |u|`.

This is scalar pulse-growth algebra. It is not a proof of the full Navier–Stokes residual, a global force-provenance theorem, or a five-moment transport theorem.

### `TorusMeanRequestRebase.lean`

- Lines 164–176 prove identity/rebase equalities for the coordinate maps.
- Lines 267–291 prove exact state-request and reference-request equalities, including the full-request coordinate swap.

The module does contain torus/request vocabulary and exact coordinate binding, but the inspected declarations stop at request data. No `torusAverage` followed by `barMoment` evaluation of the selected field is stated.

### `BaseStressClasses.lean`

- Lines 31–104 prove finite-prefix weighted composition classes.
- Lines 111–143 control rescaled jets.
- Lines 147–233 establish chart coordinates, edge-distance comparison, growth, and coordinate-range bounds.
- Lines 294–326 prove leading stress composition classes.
- Lines 455–524 prove raw, virtual, and component stress classes.

This is genuine reduced stress/jet infrastructure. `MeanClass` controls weighted functions and derivatives on the native strip; it is not itself an integrated moment identity. No declaration inspected here has the endpoint type `CandidateProperties`, `Witness`, `selected_witness`, or a final `barMoment` equality.

## Correspondence classification

| Question | Source result |
|---|---|
| Are these modules empty or merely names? | No. They contain real definitions and proved local identities/bounds. |
| Do they prove the final selected Cartesian field is wrong? | No. No nonzero defect is established here. |
| Do they prove the final selected Cartesian field preserves the five paper moments? | No. No such declaration was found in these six modules. |
| Do they strengthen the endpoint audit? | Yes, by closing six additional plausible hiding places for a transport theorem and by documenting the exact local results actually present. |

## Register action

The six modules are entered into `semantic_coverage_register.py` as `evidence_inspected` rows with anchors and conservative findings. The generated JSON, Markdown, and HTML registers must be regenerated after this source-review report is added.

