# Reachable initial-mean and moment-repair cluster

Date: 2026-09-27

This source record covers four reachable Lean modules inspected directly:

| Module | Direct result | Boundary not established |
|---|---|---|
| `NavierStokes/ActualInitialMeanEquation.lean` | Initialized angular data, local mean/divergence, periodicity, mean-zero, primary-sum divergence, and initialized full-divergence identities. | No final selected-field `(M,I,J,S,C_p)` transport. |
| `NavierStokes/CyclePhysicalPrefixes.lean` | Cylindrical and local Cartesian velocity/pressure maps, stage updates, finite prefixes, potential/direct splits, and local residual-prefix identities. | Prefix identities require individual curl-realisation hypotheses; no infinite selected-field observable equality. |
| `NavierStokes/FiveProfileMoments.lean` | Five-coordinate profile debt, integrability, exact moment maps, continuous-linear equivalence, compact correction families, and jet bounds. | Reduced-profile moments are not thereby identified with the final Cartesian selected field. |
| `NavierStokes/AngularMomentReset.lean` | Compact translated bump pairs, invertible two-parameter angular/pressure reset, pressure-neutral branch, support and exact endpoint adjustment. | Local reset does not establish whole-space selected-field radial transport. |

Key source anchors:

- `ActualInitialMeanEquation.lean:41-91,104-166,265-332,337-431,462-632`.
- `CyclePhysicalPrefixes.lean:32-141,149-214,216-308,315-458`.
- `FiveProfileMoments.lean:1-120,121-240,569-651,780-805,1115-1200`.
- `AngularMomentReset.lean:20-169,197-279,298-436,542-601,656-766`.

Adjudication: positive intermediate mathematics. This tier does not prove a
nonzero selected-field remainder, an impossibility theorem, or kernel `False`.
The open falsification target remains:

```text
profile certificates -> selected stages -> tsum/potentialSum
-> curl(localised potential) -> periodisation -> torus average
-> radial pullback -> support/integrability -> axis limit
-> (M,I,J,S,C_p).
```
