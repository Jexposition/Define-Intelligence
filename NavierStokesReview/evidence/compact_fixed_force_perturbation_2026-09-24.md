# Compact fixed-force perturbation: verified result

## Question

Can a nonzero, smooth, spatially localised, divergence-free perturbation be
added to a velocity field while retaining the same pressure and the same
fixed force in the concrete residual equation?

## Lean construction

`NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` defines
a compactly supported potential, takes its spatial curl, and uses

$$
e_{t_0}(t,x)=(t-t_0)\,\operatorname{curl} A(x).
$$

The potential is `scalarPotential x = x 1 * bump x`, with a `ContDiffBump`
of inner radius `1/2` and outer radius `1` (lines 12--21). The curl is
smooth (lines 70--85), has compact spatial support on each time slice
(lines 96--105), and is divergence-free (lines 87--121).

At the switch time, the perturbation is zero, its spatial derivative and
spatial Laplacian are zero, while its time derivative is the curl field
(lines 123--160). The local curl calculation gives

$$
\operatorname{curl}A(t,0)=e_0
$$

where `e₀` is the first coordinate vector (lines 54--68 and 168--183).
Consequently the full fixed-force perturbation defect at the origin is
nonzero (lines 173--183).

## Main theorem

`compactPerturbation_breaks_any_fixed_force_at_origin` (lines 185--226)
proves, without `sorry`, that if

$$
\mathcal R(u,p)=f
$$

holds for the base field and the same equation is required for
`u + compactPerturbation t₀`, then the residual-addition identity forces the
nonzero coordinate vector to equal zero. The assumptions are local
differentiability of the base velocity and pressure at `(t₀,0)` plus the
global base residual identity.

## Interpretation

This is a stronger and more relevant version of the earlier affine test: the
perturbation has compact spatial support on every time slice and is exactly
divergence-free. It proves path dependence of the residual-designed force
under a fixed-data perturbation.

It does not by itself prove `False` from the repository's existential C/D
theorem. The C/D endpoint quantifies over one force and one candidate; it does
not assert invariance under all perturbations. A formal disproof still needs a
theorem that the selected endpoint is required to satisfy the added
independence/stability condition, or a direct contradiction in its selected
premises.

## Verification

- Toolchain: Lean 4.34.0-rc2 via elan.
- Result: exit code 0.
- `sorry`, `axiom`, and `unsafe` scan: none in this module.
- Source module: `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean`.
