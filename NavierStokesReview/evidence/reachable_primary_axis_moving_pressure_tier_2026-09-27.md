# Reachable primary-bound, slow-axis, moving-moment, and pressure-test tier

**Date:** 2026-09-27  
**Scope:** direct source review of four further modules reachable from the
selected candidate closure.

| Module | Verified source result | Boundary of result |
|---|---|---|
| `NavierStokes/ActualPrimaryBounds.lean:40-91,287-305,439-499,732-832` | Actual signed labels, native velocity/pressure jet bounds, periodised copy sums, cutoff-copy identities, and uniform chart-level wave classes. | Supports stage construction; no final selected Cartesian five-moment evaluation. |
| `NavierStokes/ActualSlowAxis.lean:24-70,104-221,287-357,361-485` | Holomorphic/natural slow-axis elements, real-domain regularity, base and positive-order collar identities, initial/stock fields, smooth profiles, axis vanishing, and axis jets. | Reduced profile/axis layer; no Cartesian endpoint observable transport. |
| `NavierStokes/MovingMomentBounds.lean:30-104,118-228,298-359` | Moving-strip pressure-mass and radial-moment class bounds, support closure under differential operators, and rank-stage defect classes under explicit local hypotheses. | Local moving-profile/correction estimates; no selected whole-space five-tuple. |
| `NavierStokes/R3/PressureTestBounds.lean:20-79,86-116,118-253` | Fourier weighted estimates, (H^3) control, derivative/Riesz-test bounds, and a uniform pressure-test constant. | Comparative pressure-test support; not an absolute selected-pressure Poisson representative. |

## Adjudication

This tier supplies more concrete estimates and axis/profile transport. It does
not show that the final selected field has a nonzero moment remainder, nor that
the required transport is impossible. It also does not turn comparative
pressure-test estimates into absolute pressure semantics.

The classification remains **not established as a paper-to-endpoint
correspondence under CTR-005**, with no selected-path `False` theorem found.
