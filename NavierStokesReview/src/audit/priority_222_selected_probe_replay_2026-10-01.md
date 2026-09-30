# Priority 222: selected-path probe replay

Date: 2026-10-01

## Reproducibility gate

The following files were replayed from the live checkout with:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean <file>
```

| File | Exit code | Admission-token scan |
|---|---:|---|
| `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean` | 0 | No `sorry`, `admit`, or `axiom` token |
| `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean` | 0 | No `sorry`, `admit`, or `axiom` token |
| `NavierStokesReview/src/probes/GlobalTransportBridgeProbe.lean` | 0 | No `sorry`, `admit`, or `axiom` token |

## What the replay establishes

The obstruction extension compiles its theorem that the selected witness can
coexist with a nonzero abstract `Debt` payload. The selected-path probe
compiles its theorem that the selected envelope reaches the R3 packaging
through localisation while retaining the abstract debt non-entailment. The
global bridge probe compiles its theorem that the selected consequences bundle
does not imply a same-datum fixed-force perturbation stability predicate.

These are valid endpoint-contract and provenance diagnostics. They do not
identify the abstract `Debt` with the physical radial integrals of the
selected Cartesian field. Consequently they do not prove

\[
\Delta m\ne 0,
\qquad
\text{force nonsmoothness},
\qquad
\text{or }\bot.
\]

## Controlled conclusion

The fresh kernel replay strengthens the evidence that the exported endpoint
does not entail the requested five-observable identity and that residual-force
provenance is path-dependent. It does not overturn the positive source result
that the selected construction has genuine internal invariant, physical-data,
residual-rate, smooth-force, and blow-up machinery.

The scientific disposition remains **`CTR-005: NOT ESTABLISHED`** for complete
paper-to-selected-endpoint correspondence. No literal CMI failure or formal
refutation is claimed by this replay.

Evidence: `NavierStokesReview/evidence/selected_probe_replay_2026-10-01.md`.
