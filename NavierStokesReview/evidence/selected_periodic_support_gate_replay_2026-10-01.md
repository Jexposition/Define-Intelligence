# Evidence: selected periodic-support gate replay

This record accompanies
`../src/audit/priority_227_selected_periodic_support_gate_replay_2026-10-01.md`.

## Verified result

`SelectedPeriodicSupportTransportGate.lean` compiled under
`leanprover/lean4:v4.34.0-rc2` with no `sorry`, `admit`, or new axiom. Its
selected-field theorem proves that bounded radial support and a nonzero value
cannot coexist for the exact unit-periodic selected mixed radial pullback.

## Boundary retained

The proof does not derive bounded radial support from the compact R3 candidate,
because the source distinguishes the compact representative from the
periodised field and proves only local equality in the inner cube. It also
does not derive a nonzero value for the exact first-component radial pullback
from the full-velocity norm blow-up. The existing angular-growth result is a
promising route, but the required pointwise transport equality remains to be
proved. A separate compiled completion now proves the weaker statement that
the selected raw mixed velocity is nonzero at some spacetime point. That result
does not identify the point, component, or periodised radial pullback required
by this gate.

Evidence for the narrower result:
`../src/completions/SelectedRawVelocityNonzero.lean`.

## Status

This is a verified conditional obstruction, not a selected-field refutation.
`CTR-005: NOT ESTABLISHED` remains the controlled disposition for the complete
manuscript-to-selected-endpoint correspondence.
