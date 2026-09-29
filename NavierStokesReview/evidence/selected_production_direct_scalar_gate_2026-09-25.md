# Selected production direct scalar gate

**Date:** 2026-09-25
**Classification:** selected source identity; no contradiction claimed
**Review tree:** `NavierStokesReview/src/completions/SelectedProductionDirectScalarGate.lean`

## Result

The selected direct branch is not passed to the production field as its native
radial scalar. At a positive radial section, its first Cartesian component is
multiplied by the spatial localisation factor before periodisation:

$$
\bigl(\operatorname{cutPotential}(D_j)(t,x)\bigr)_1
=\chi(x)\,m_j(t,x),
$$

where `m_j` is the selected native angular mean field and
`χ = SpatialLocalization.spatialCutoff`. On the radial section used by the
review, the factor is exactly

$$
\chi(r,z)=\operatorname{cutoff}(16r^2)\operatorname{cutoff}(4z).
$$

The native order-two `barMoment` theorem applies to the unweighted scalar
family. It does not imply that the cutoff-weighted integral is zero. The
remaining calculation is therefore the selected weighted remainder, not a
generic missing-bridge complaint.

## Source anchors

| Source | Anchor | Role |
|---|---:|---|
| `NavierStokes/ActualCandidateAssembly.lean` | 553–556 | `directStages` is identified with `angularMeanStages`. |
| `NavierStokes/ActualMeanStageData.lean` | 23–24 | `radialSection` embeds a positive radial point into Cartesian space. |
| `NavierStokes/SpatialLocalization.lean` | 48–53 | Definition and smoothness of `spatialCutoff`. |
| `NavierStokes/SpatialLocalization.lean` | 164–172 | `cutPotential` multiplies before the production velocity is formed. |
| `NavierStokes/SpatialLocalization.lean` | 200–207 | Curl product rule retains the cutoff derivative term for potential fields. |
| `NavierStokes/DefectIncrementBounds.lean` | 214–220 | `barMoment_apply` integrates the native scalar family after torus averaging. |
| `NavierStokesReview/src/completions/SelectedProductionDirectScalarGate.lean` | 21–36 | Zero-sorry selected component identity with cutoff factor. |
| same | 38–46 | Zero-sorry radial expression for the cutoff. |

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean \
  NavierStokesReview/src/completions/SelectedProductionDirectScalarGate.lean
```

Result: exit code `0`; no `sorry`, custom `axiom`, or `unsafe` was used.

## Claim boundary

This establishes a concrete selected-field weighting that must be included in
the moment calculation. It does not yet prove that the weighted remainder is
nonzero. The next admissible promotion is an exact evaluation or inequality
for that remainder using the selected scalar family and its support data.
