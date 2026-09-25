# Selected angular component formula

`NavierStokesReview/src/completions/SelectedAngularComponentFormula.lean`
compiles without `sorry`, `axiom`, or `unsafe` and proves the exact selected
angular component identity

```lean
(meanAngularField B N0 degree f w) 1 =
  meanField B N0 degree f w *
    ((PhysicalGraphBounds.radialProjection w).1 /
      PhysicalClassBounds.cartesianRadius
        (PhysicalGraphBounds.radialProjection w))
```

## Source ledger

| Source | Lines | Role |
|---|---:|---|
| `ActualCandidateConstruction.lean` | 358-366 | Defines `meanField` and `meanAngularField`. |
| `PhysicalMeanJetBounds.lean` | 518-521 | Defines the totalised Cartesian angular frame. |
| `ActualMeanStageData.lean` | 64-74 | Identifies coherent-family angular fields with the same frame. |
| `ActualCandidateConstruction.lean` | 392-401,425-427 | Builds angular stages and their selected finite prefix. |
| `SelectedAngularComponentFormula.lean` | 17-27 | Review-side component theorem. |

## Consequence for the live calculation

The selected field is now exposed one component deeper than the prefix
identity. The coefficient is still wrapped by the physical atlas and the
radial projection; no scalar `barMoment` equality follows automatically.
The next calculation must evaluate this coefficient and the corresponding
cutoff/curl terms on a positive-radius band, then account for axis and tail
terms. No nonzero `Delta m` is claimed by this theorem.

Build result: `lake build NavierStokesReview` passed with 3697 jobs using
Lean `v4.34.0-rc2`.
