# Selected-witness falsification attacks

**Date:** 2026-09-24
**Scope:** adversarial review of the selected endpoint, not a compilation-only review.

## Attack 1: force smoothness at the singular interface

`CandidateFromLimits.force_smooth` is conditional. Its decisive input is the
family `hlim` of locally uniform limits of the actual Navier--Stokes residual
derivatives. `SpeedUnboundedAtOne` is not an input to that theorem. The
endpoint jet is then identified with the supplied series `L` by
`force_boundary_jets`.

The correct attack is therefore to prove a selected-field lower bound that
prevents cancellation in

$$
\partial_t u+(u\cdot\nabla)u-\nu\Delta u+\nabla p.
$$

A velocity norm divergence alone does not prove that lower bound. The live
formal target is to disprove one of the actual selected `hlim` premises or to
derive the required residual lower bound. Neither has yet been proved.

## Attack 2: pressure-Poisson and support interface

`NavierStokes/R3/ProblemStatement.lean:92-109` requires compact spatial
support for pre-singular pressure slices and the residual equation, but adds no
pressure-Poisson/Leray equation. The pressure gradient is inside
`navierStokesResidual`, so the force can absorb it at the level of the stated
record. `PressureRecovery` and `ActualPressureFlux` compare fields under
equal-residual hypotheses; they do not add the missing absolute Poisson
identity.

This is an unresolved semantic attack, not a cleared hypothesis. The decisive
formal test is to add the global Poisson premises and prove that the selected
compact-support pressure and selected velocity cannot satisfy them. Compact
support alone is not that theorem.

## Attack 3: selected-witness inhabitation boundary

`ActualCandidateAssembly.Witness` at `ActualCandidateAssembly.lean:1121-1151`
contains the schedule, away extensions, force, `CandidateProperties`,
consequences, H3 limit, force decay, and boundary jets. It contains no
`PositiveOrderMoments.Debt`, no `moments` equality, and no theorem identifying
the five named moments with the runtime debt.

The zero-sorry probe `SelectedWitnessInhabitationProbe.lean` proves that the
already inhabited selected `Witness` can be paired with a concrete nonzero
five-coordinate `ghostDebt`. This is a type-level countermodel to the claim
that the exported witness envelope itself enforces five-moment transport. It
does not yet prove that the actual selected velocity violates those moments,
because the envelope does not expose the field-level moment predicate needed
to state that violation.

## Current status

The selected-witness attack remains open. The strongest machine-checked result
is that the exported endpoint type can be inhabited while an arbitrary
five-debt payload remains unconstrained. The next decisive theorem must add the
field-level moment and pressure equations and derive `False` from the actual
selected fields, not from a detached interface model.

Evidence:

- `NavierStokesReview/src/probes/SelectedWitnessInhabitationProbe.lean`
- `NavierStokesReview/src/probes/ResidualFlatnessCompatibilityProbe.lean`
- `NavierStokes/ActualCandidateAssembly.lean:1121-1185`
- `NavierStokes/R3/ProblemStatement.lean:92-109`
- `NavierStokes/CandidateFromLimits.lean:39-136`
