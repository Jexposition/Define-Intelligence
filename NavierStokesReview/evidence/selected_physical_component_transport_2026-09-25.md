# Selected physical component transport

**Date:** 2026-09-25  
**Tree:** review worktree, upstream `NavierStokes/` unchanged  
**Claim level:** selected-path positive evidence; not a contradiction

## Result

`NavierStokesReview/src/completions/SelectedPhysicalComponentTransport.lean`
compiles without `sorry`, custom axioms, or `unsafe` declarations.  It proves
the map-level identity

$$
\bigl(\operatorname{polarVelocityMap}(v)(w)\bigr)_1
=\sin(\theta(w))\,v_0(\operatorname{polarCoordinates}(w))
 +\cos(\theta(w))\,v_1(\operatorname{polarCoordinates}(w)).
$$

The selected direct branch is then transported on its actual chart domain.  Its
first Cartesian component is

$$
u^{\mathrm{direct}}_{j,1}(w)
=\cos(\theta(w))\,Q_n^{-A(h)}
\,a_j\!\left(\operatorname{swapCylinder}\bigl(G_n(\operatorname{polarCoordinates}(w))\bigr)_1\right),
$$

where `a_j` is `angularNativeStages ... j n` and `G_n` is the selected graph.
The `swapCylinder` factor is material: omitting it gives the wrong slow-point
coordinate and does not type-check against the source definition.

## Source anchors

- `NavierStokes/CyclePhysicalPrefixes.lean:32-38`: `velocityMap`.
- `NavierStokes/CyclePhysicalPrefixes.lean:158-178`: `polarVelocityMap` and
  `velocity_polar_forward`.
- `NavierStokes/PhysicalCurlCovariance.lean:666-726`: polar input,
  coordinates, and valid-chart transport.
- `NavierStokes/PhysicalResidualTZ.lean:44-51, 385-419`: `swapCylinder`,
  `graphMapTZ`, and `velocityTZ`.
- `NavierStokes/ActualCandidateConstruction.lean:358-406, 543-566`:
  `meanField`, `angularNativeStages`, and chart realization.
- Review theorem: `SelectedPhysicalComponentTransport.lean:20-31` and
  `:33-94`.

## Interpretation

This closes a genuine component-level transport step.  It does not yet identify
the full mixed Cartesian field with the scalar input of `barMoment`; it also
does not evaluate the torus average, the axis branch, the outer support term,
or the potential/curl summand.  No nonzero remainder and no `False` are claimed.

## Verification

Command:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedPhysicalComponentTransport.lean
```

Result: exit code `0`.

The review target and upstream target were also built together:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokes NavierStokesReview
```

Result: exit code `0`; 9,606 jobs completed.  The only endpoint axiom report
was the standard Lean foundation set `[propext, Classical.choice, Quot.sound]`.
