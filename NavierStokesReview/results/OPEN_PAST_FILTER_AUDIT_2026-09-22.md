# Concrete open-past filter audit

Date: 2026-09-22
Toolchain: `leanprover/lean4:v4.34.0-rc2` via `C:\Users\Admin\.elan\bin\elan.exe`
Probe: `NavierStokesReview/src/probes/OpenPastNeBotProbe.lean`

## Question

The generic `DiagonalResidual.JetRate` interface permits a vacuous witness on
the bottom filter. Does the selected R3 endpoint use such a filter?

## Concrete check

`SpacetimeEndpoint.openPast T` is the set `Iio T ×ˢ univ`. The selected schedule
uses the neighbourhood-within filter at `(1, 0)`. The zero-sorry probe proves

```text
(nhdsWithin ((1 : ℝ), (0 : Space)) (openPast 1)).NeBot
```

by taking, for every neighbourhood radius `ε > 0`, the point
`(1 - min (ε / 2) (1 / 2), 0)`. Its product-metric distance from `(1, 0)` is
less than `ε`, and its time coordinate is strictly below `1`.

## Disposition

This is positive evidence for the selected endpoint and removes the specific
claim that the endpoint filter itself is bottom. It does not repair the
generic API. Any other filter used by a rate consumer still requires its own
`NeBot` or equivalent domain-coverage proof. The derived-filter audit remains
an API-quality finding, not a demonstrated CMI mismatch.

Raw compiler output is in `OPEN_PAST_NEBOT_4_34_RC2.txt`.
