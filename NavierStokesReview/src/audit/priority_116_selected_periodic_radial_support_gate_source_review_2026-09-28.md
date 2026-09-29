# Priority 116: selected periodic radial-support gate

Date: 2026-09-28

Status: source-grounded conditional obstruction; no selected-path `False`.

## Question

Can the selected whole-space compact-support theorem be combined with the
selected periodic radial pullback to trigger the generic theorem
`periodic_radiallySupported_eq_zero`?

## Proves

1. `NavierStokes/ProblemStatement.lean:101-113` defines the periodic
   `CandidateProperties` contract. It requires periodicity, smoothness,
   incompressibility, the residual identity, and blow-up-related properties;
   it does not require a compact spatial support set for the velocity.

2. `NavierStokes/R3CompactCandidate.lean:24-37` defines a different
   whole-space `R3CompactCandidate.Properties` contract. Its
   `velocity_support` field is a compact Cartesian support statement for its
   `u` argument.

3. `NavierStokes/R3/ActualCandidate.lean:80-122` constructs the whole-space
   candidate from the periodic candidate. The selected periodic fields enter
   `R3CompactCandidate.of_localized_fields`; the exported whole-space velocity
   is `R3CompactCandidate.velocity A B`, while the periodic endpoint velocity
   is `MixedPeriodicAssembly.periodicVelocity A B`.

4. `NavierStokes/MixedPeriodicAssembly.lean:35-65` proves unit spatial
   periodicity for `MixedPeriodicAssembly.periodicVelocity`. This is a genuine
   property of the periodic endpoint field.

5. `NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean:31-46`
   defines the selected mixed production scalar from the periodic velocity,
   including both the potential and direct branches.

6. `NavierStokesReview/src/completions/SelectedMixedRadialPeriodicity.lean:28-73`
   transports unit spatial periodicity through the radial-section pullback.
   Therefore `selectedMixedRadialPullback` is period-one in its radial
   coordinate.

7. `NavierStokesReview/src/completions/SelectedMixedProductionTorusAverage.lean:25-43`
   reduces the auxiliary torus average and exposes the actual weighted radial
   integral used by `barMoment`.

8. `NavierStokesReview/src/completions/SelectedMixedRadialSupportObstruction.lean:31-47`
   proves the exact conditional obstruction:

   ```text
   periodic radial pullback + RadiallySupported α β
       -> radial pullback = 0 everywhere.
   ```

9. `NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean:31-75`
   proves a separate conditional result: strict positivity on one fundamental
   interval makes a periodic scalar non-integrable, and Mathlib's global
   Bochner integral then evaluates through `integral_undef`. The required
   positivity premise is not proved for the selected pullback.

## Does not prove

- It does not prove that the selected mixed radial pullback has bounded radial
  support.
- It does not convert the compact Cartesian support of the R3 wrapper into
  `RadialAlias.RadiallySupported` support for the periodic pullback.
- It does not prove that the periodic endpoint field and the compact R3 field
  are globally equal. The source supplies local/plateau agreement, not an
  equality on the entire unbounded radial integration domain.
- It does not prove a nonzero radial moment, a nonzero cutoff defect, an
  impossibility theorem, or `False`.
- It does not show that the paper's five named moments equal any selected
  `barMoment` value.

## Missing hypotheses that would change the verdict

The conditional obstruction becomes a selected-path contradiction only if the
source proves both of the following for the same field and same time slice:

1. **Field identity:** the radial observable is the pullback of the compact
   whole-space velocity, not merely a separately defined periodic production
   scalar or a local germ.
2. **Support transport:** the compact Cartesian support supplied by
   `R3CompactCandidate.Properties.velocity_support` implies bounded radial
   support of that exact pullback.

Alternatively, a selected-field sign/nonzero theorem on one fundamental radial
interval would activate the conditional global-integral result, but that sign
theorem is also absent from the inspected declarations.

## Blindside control

The earlier probe family was too easy to misread if treated as one block. This
report separates four levels:

| Level | Actual evidence | Safe interpretation |
|---|---|---|
| Contract | `CandidateProperties` and `Witness` omit the final five-moment equality | Correspondence gap only |
| Field | Selected periodic mixed scalar and curl/cutoff product rule are explicit | Real selected-field pipeline exists |
| Observable | Torus average and `barMoment` reduce to a concrete radial integral | The remaining calculation is now well-typed |
| Obstruction | Periodicity plus bounded radial support forces zero | Conditional route; support and field identity are still required |

The audit must not call the periodic-support route a contradiction until the
two missing hypotheses are supplied and checked against the exact exported
candidate.

## Next source-level probe

The next probe should attempt the two missing hypotheses directly, using the
actual definitions rather than a surrogate:

1. trace `R3CompactCandidate.velocity_locally_eq` and the selected schedule to
   determine its exact domain;
2. attempt to construct `RadiallySupported` for the pullback of that compact
   velocity, recording the first type/domain mismatch if construction fails;
3. if support transport succeeds, combine it with
   `selected_mixed_bounded_radial_support_forces_zero`;
4. independently search for a selected-field nonzero/sign theorem before using
   `PeriodicGlobalIntegral`.

Until these checks succeed, the strongest supported status remains
`CTR-005: correspondence failure / not established`, with a sharper
periodicity-support obstruction recorded as an active falsification target.
