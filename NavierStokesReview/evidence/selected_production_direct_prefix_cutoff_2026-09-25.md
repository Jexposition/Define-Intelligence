# Selected production direct prefix and cutoff defect

Date: 2026-09-25
Classification: selected-field identity; value unresolved
Claim level: supports CTR-005, but does not prove `Δm ≠ 0` or `False`

## Source anchors

| Item | Source |
|---|---|
| Native angular stages | `NavierStokes/ActualCandidateConstruction.lean:392-401` |
| Native finite-prefix telescoping | `NavierStokes/ActualCandidateConstruction.lean:425-437` |
| Production spatial cutoff | `NavierStokes/SpatialLocalization.lean:41-49,165-171` |
| Production cutoff/curl product rule | `NavierStokes/SpatialLocalization.lean:200` |
| Moving annulus | `NavierStokes/NominalConeAssembly.lean:1327-1333`; `NavierStokes/PrimaryTargetBounds.lean:667-678` |
| New zero-sorry completion | `NavierStokesReview/src/completions/SelectedProductionDirectPrefixCutoff.lean:26-79` |

## Verified identities

For every finite prefix `J` and space-time point `w`, the review completion proves

$$
\sum_{j\leq J}(\chi\,u_j)_1(w)
=\chi(w_\mathrm{space})\sum_{j\leq J}(u_j)_1(w).
$$

On a positive-radius radial section, the second completion theorem identifies
the uncut prefix with the selected cycle mean field. The same file proves the
exact shell defect

$$
\sum_{j\leq J}(\chi u_j)_1-\sum_{j\leq J}(u_j)_1
=(\chi-1)\sum_{j\leq J}(u_j)_1.
$$

This is the concrete remainder that must be transported through the radial
projection, torus average, and `barMoment`. The native order-two moment result
does not remove it, because that result applies before production localisation.

## What the source does not establish

The source gives positivity and ordering of the moving annulus radii, but the
review has not proved a selected inequality placing that annulus wholly inside
or outside the fixed spatial cutoff. It also does not expose a selected point
where the cycle mean is nonzero. Therefore the shell identity is not promoted
to a nonzero numerical leak. The burden remains a selected integral calculation,
not a generic statement about cutoffs.

## Verification

Focused command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedProductionDirectPrefixCutoff.lean
```

Result: exit code `0`; no `sorry`, custom axiom, or `unsafe` declaration in
the new review module.
