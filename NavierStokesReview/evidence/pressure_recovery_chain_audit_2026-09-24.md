# Pressure-recovery chain audit

Date: 2026-09-24  
Scope: selected R3 candidate and whole-space comparison path  
Method: source inspection plus the existing zero-sorry pressure-support probe

## Result

The pressure-support/trivialisation objection is not a proved contradiction.
The selected R3 candidate does compactly localise each pre-singular pressure
slice, but the candidate predicate does not impose a pressure Poisson equation
independent of the external force. The force is allowed to equal the residual,
so compact pressure support alone cannot force the pressure or velocity to
vanish.

## Source ledger

| Code footprint | Exact role | Audit result |
|---|---|---|
| `NavierStokes/R3/ProblemStatement.lean:92-109` | `CandidateProperties.pressure_support` | Only `tsupport p(t,·) ⊆ K` with compact `K`; no pressure-Poisson or pressure-normalisation field. |
| `NavierStokes/R3CompactCandidate.lean:23-37` | Whole-space compact candidate record | Pressure support and force support are separate properties. The record permits an arbitrary smooth force satisfying the residual identity. |
| `NavierStokes/R3/ActualCandidate.lean:59-65,104-109` | Selected R3 localisation | `cutPressure` and `localized_pressure_tsupport` supply compact pressure support. The same construction supplies the residual-defined positive-time force. |
| `NavierStokes/R3/PressureRecovery.lean:33-44` | Comparison hypotheses | Requires smooth fields, divergence-free velocities, equal residuals, and uniform finite energy. |
| `NavierStokes/R3/PressureRecovery.lean:286-305` | Harmonic functional vanishing | Uses an H³-bounded compact-test functional; this is a comparison theorem, not a selected pressure-support contradiction. |
| `NavierStokes/R3/PressureRecovery.lean:391-438` | Gradient recovery | Recovers pressure-gradient pairings at interior times from the stated comparison hypotheses. |
| `NavierStokes/R3/ActualPressureFlux.lean:28-52` | Actual flux identity | Converts the pressure flux to canonical Riesz pairings using compact cutoff tests and the recovered gradient identity. |
| `NavierStokes/R3/PressureFluxIdentity.lean:114-190` | Integration-by-parts bridge | Requires an explicit gradient-identification premise and divergence-free difference; it does not assume pressure compactness implies zero. |
| `NavierStokes/R3/WholeSpaceUniqueness.lean:35-101` | Selected comparison closure | Constructs `PressureRecovery.Hypotheses` and invokes the actual pressure-flux bound before applying the closure theorem. |

## Formal test

`NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean:37-50`
proves without `sorry`:

```text
¬ (∀ f, HasCompactSupport f → f = 0)
```

The witness is the repository's own smooth compact spatial cutoff, which has
value `1` at the origin. Therefore the inference

```text
compact pressure support → pressure = 0 → velocity = 0
```

is not derivable from the source declarations.

## What this does not establish

The presence of `PressureRecovery` and `ActualPressureFlux` is not accepted as
proof that the selected pressure has the global meaning used by the paper.
Those theorems operate on explicit comparison hypotheses and compact test
pairings. `StateRealization.chartIdentity` is a local chart reconstruction
from local germs and a base-equation premise. The inspected source does not
provide a single paper-linked theorem identifying the compactly localised
selected pressure with a global Poisson/Leray pressure object on all of R³.

## Adversarial conclusion

This route does not yet falsify the C/D proposition. It does expose a
semantic burden: the paper's physical pressure interpretation must be
connected to the selected compactly localised pressure and residual force.
The source contains comparison recovery infrastructure, but the present audit
found no theorem that turns that local infrastructure into the paper's global
pressure-Poisson semantics, and no theorem that turns compact support alone
into a pressure-Poisson contradiction.

The live formal target remains the selected-path moment/residual bridge. The
zero-sorry `StageEstimatesMomentBlindnessProbe` proves a narrower but genuine
negative result: the generic stage-rate interface admits zero fields and does
not encode blow-up or the paper's five named moments.
