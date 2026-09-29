# Selected support predicate scope

Date: 2026-09-25  
Classification: selected-field calculation gate under CTR-005; no `False` established

## Result

The review completion
`NavierStokesReview/src/completions/SelectedSupportPredicateScope.lean`
compiles without `sorry`, custom axioms, or `unsafe`. It proves an interface
countermodel to the implication needed to remove the production cutoff:

$$
\operatorname{ShrinkingSupport}(h,C,f)
\not\Rightarrow
\bigl(\text{every nonzero point of }f\text{ lies in }\texttt{SpatialLocalization.plateau}\bigr).
$$

The witness has radius zero and axial coordinate one. Hence it satisfies the
radial support predicate for every nonnegative outer-radius constant, while it
is outside the plateau because the plateau additionally requires
$|x_2|<1/8$.

## Source anchors

- `NavierStokes/MixedDiagonalExtensions.lean:99-102` defines
  `SublevelShrinkingSupport` using only `AnnularEndpoint.radius` and
  `AnnularEndpoint.outerRadius`.
- `NavierStokes/AnnularEndpoint.lean:27-28,46-48` identifies the radius as
  distance to the symmetry axis and the outer radius as
  $C\sqrt{\operatorname{physicalQ}}$.
- `NavierStokes/SpatialLocalization.lean:133-147` defines the plateau by
  `radialSquare x < 1 / 32 ∧ |x 2| < 1 / 8` and proves the cutoff is one only
  on that set.
- `NavierStokes/ActualCandidateConstruction.lean:882-885` proves the selected
  angular stages satisfy the radial shrinking-support predicate.

## Interpretation boundary

The countermodel is an interface model, not an assertion that the selected
smooth field equals the witness function. It therefore does not prove that the
selected cutoff-weighted moment is nonzero. It does prove that the source
support theorem cannot, by itself, justify replacing the production field by
the native uncut profile. The remaining calculation is the selected scalar
pullback, torus average, and radial integral with the cutoff retained.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

Result: `Build completed successfully (3716 jobs)`.
