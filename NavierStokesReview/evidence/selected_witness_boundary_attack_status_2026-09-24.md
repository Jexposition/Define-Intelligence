# Selected-witness boundary attack status

## Scope

This ledger records the three direct falsification attacks against the
selected witness. It separates a proved contradiction from a missing theorem.
All Lean results below compile without `sorry` under Lean 4.34.0-rc2.

## Force-jet attack

`CandidateFromLimits.force_smooth` proves smoothness from the supplied family
of locally uniform residual-jet limits. `FinalSlowBase.residual_identity`
decomposes the residual into `stressForce + error`, while
`FinalSlowBase.error_allJetsFlat` proves flatness for the error in the core.
The selected endpoint therefore does not expose an automatic implication
from velocity growth to residual growth.

The probe
`NavierStokesReview/src/probes/SelectedResidualLowerBoundObstructionProbe.lean`
proves the exact conditional obstruction. On the actual non-bottom past
filter, if some `c > 0` satisfies

$$c\lVert u(t,0)\rVert \leq \lVert\mathcal R(u,p)(t,0)\rVert$$

eventually before time one, then the residual limit zero and origin velocity
blow-up derive `False`. No theorem establishing this lower bound was found in
the selected source. The attack is therefore live and load-bearing, not
cleared.

## Pressure-Poisson attack

`NavierStokes/R3/ProblemStatement.lean:92-109` requires compact pressure
support and the residual equation, but does not state a global pressure
Poisson/Leray identity. `PhysicalResidualJetBounds.StateRealization` and
`ActualCycleResidualBounds.PhysicalFields` provide local pressure germs and
comparison identities, not that global equation. Compact support alone does
not imply zero pressure or zero velocity, so it is not yet a contradiction.
The decisive test remains a zero-sorry theorem deriving the global Poisson
identity for the selected field and showing incompatibility with its support
or residual limits.

## Moment-blind ghost-model attack

`StageEstimates` contains smoothness, growth, finite-prefix residual rates,
and scheduling data, but no five-moment field or equality. The zero-sorry
`SelectedWitnessInhabitationProbe.lean` proves that the exported `Witness`
envelope can coexist with an arbitrary nonzero five-debt value. This formally
refutes the claim that the witness type itself enforces the paper's five
moments. It does not prove that the concrete selected velocity violates them.
The live target is a field-level moment evaluation on the selected sums.

## Current verdict

No zero-sorry `False` theorem from the selected witness has been obtained in
these three attacks. The strongest proved result is the conditional residual
lower-bound obstruction plus the missing selected-field five-moment and
global pressure transport theorems. The review must not describe these routes
as cleared merely because a weaker probe failed.
