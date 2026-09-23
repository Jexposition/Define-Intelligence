# Force cutoff and residual-extension audit

Date: 2026-09-23  
Audited tree: `Define-Intelligence-github`, branch `review/cmi-first-navier-stokes-2026-09-22`  
Method: direct source inspection plus the zero-sorry Lean probe
`NavierStokesReview/src/probes/ForceActivityProbe.lean`.

## Finding

The proposed discontinuous-cutoff objection is not supported by the source.
`NavierStokes/R3/PositiveTimeForce.lean` defines

```lean
timeCutoff t := SmoothCutoffs.cutoff ((8 / 5 : ℝ) * (t - 11 / 16))
```

and proves `ContDiff ℝ ∞ timeCutoff`. The underlying cutoff is a smooth bump,
not an `if` or indicator function. The source proves that it equals one on
`[3/8, 1]` and vanishes outside `[1/16, 21/16]`. The probe independently
proves `timeCutoff 1 = 1`, `force f (1,x) = f (1,x)`, and continuity of the
time trace at one for every globally smooth `f`.

This establishes that the wrapper is active at the singular time but does not
create a boundary discontinuity. Activity at `t = 1` is not, by itself, a C/D
failure: the R³ statement requires a globally smooth force and only requires
the PDE identity on `0 < t < 1`.

## Residual provenance

The wrapper `PositiveTimeForce.force` does not itself calculate the momentum
residual. The substantive construction is in
`NavierStokes/CandidateFromLimits.lean`:

- `force` is a smooth extension of `tracedResidual`;
- `force_eq_activated_residual` identifies it with the activated
  Navier–Stokes residual for `0 ≤ t < 1`;
- `force_smooth` and `force_boundary_jets` use the locally uniform endpoint
  limits `hlim` and the boundary jet `L`;
- `force_time_support` proves vanishing from time `2` onwards.

The selected witness exposes the resulting `forcing`, its `CandidateProperties`,
global smoothness, decay, and endpoint jets in
`NavierStokes/ActualCandidateAssembly.lean:1121-1185`. The upstream theorem
`PeriodicResidualLimits.exists_candidate_force` constructs `L` and `hlim`
from `VanishingJointJets` and away-extension data. Therefore the force is
residual-driven before the singular time, but the current source audit does
not show a force-norm divergence or a failed smooth-extension obligation.

## What this does and does not prove

The audit confirms a real semantic concern: the force is engineered from the
candidate residual rather than supplied as an independently specified driver.
That is relevant to physical interpretation and to the paper's narrative.
It is not a formal contradiction of the written forced C/D predicate, which
allows a smooth force. The claim that “blow-up of the velocity automatically
forces blow-up of `f`” is also not a proof: residual terms may cancel, and the
repository explicitly makes cancellation and endpoint jet limits obligations.

The decisive unresolved test is a zero-sorry theorem showing either that the
selected residual cannot have the required locally uniform limits, or that the
selected witness's force fails one of the global smoothness/support/decay
properties. The suggested `Tendsto ... atTop` theorem with `sorry` is not
evidence and was not added.

## Probe result

Compiled successfully with Lean 4.34.0-rc2 using the repository's Lake
environment. The probe contains no `sorry`, `axiom`, or `admit`.
