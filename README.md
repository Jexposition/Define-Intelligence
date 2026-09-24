# Finite time blowup for Navier–Stokes and Euler equations

This repository contains Lean 4 formalizations of the results presented in
“[Finite time blowup for Navier–Stokes](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)” and
“[Finite time blowup for the Euler equation](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf)” by OpenAI.

- [Read the blog post](https://openai.com/index/navier-stokes-solution/)
- [Read the Navier-Stokes paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
- [Read the Euler paper](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf)

## Independent review status

This fork contains a separate, source-level formal review of the claims above.
It does not treat successful compilation as proof that the implementation
matches the published mathematical construction.

- **CTR-005, specification drift:** the repository contains substantial
  five-moment and rank machinery, but the selected endpoint does not expose a
  theorem transporting the paper's tuple `(M, I, J, S, C_p)` into the final
  `selected_witness` residual and force predicates. The live finding is a
  missing selected-endpoint correspondence theorem, not an allegation that
  every upstream moment module is dead code.
- **CTR-012, fixed-force path dependence:** the zero-sorry review modules derive
  the exact perturbation identity for a fixed force. They also construct a
  smooth, spatially compactly supported, divergence-free perturbation whose
  defect at the origin is the nonzero first coordinate vector. Thus a residual
  selected from one velocity path cannot remain the same force after this
  perturbation.
- **CTR-017, temporal index boundary:** a zero-sorry theorem constructs unequal
  raw entries at indices zero and one of `initializedSeries`. The source does
  not identify the natural-number stage index with time, and its selected sums
  and smooth activation have `ContDiff` and late-jet theorems. This is an open
  interface obligation, not a proved temporal PDE discontinuity.

The runtime rank audit also narrows the moment objection. `FiveRows` constrains
two radial moments of correction functions and carries three debt coordinates;
it does not hard-code total kinetic energy to zero. The missing result is the
selected-path theorem transporting those internal moments into the paper's
five named quantities and the exported mixed field. See
[`MeanRankUpdateAudit.lean`](NavierStokesReview/src/completions/MeanRankUpdateAudit.lean)
and [`mean_rank_update_scope_2026-09-24.md`](NavierStokesReview/evidence/mean_rank_update_scope_2026-09-24.md).

The two findings are related but distinct. The selected construction has the
form `f = navierStokesResidual u p` along its chosen path, so the residual
identity is part of the witness predicates rather than an independently
transported forcing datum. `IndependentDataPerturbationProbe.lean` and
`CompactFixedForcePerturbation.lean` then prove, without `sorry`, that holding
`p` and `f` fixed while changing `u` by the displayed smooth perturbation
produces a nonzero residual defect. This is a machine-checked path-dependence
and correspondence objection.

The formal review therefore establishes a machine-checked causality and
correspondence objection. It has not yet derived `False` from the literal
existential C/D endpoint. The evidence and exact scope are maintained in
[`docs/OpenAI_NavierStokes_Peer_Review_v1.md`](docs/OpenAI_NavierStokes_Peer_Review_v1.md),
[`docs/OpenAI_NavierStokes_Research_Paper.md`](docs/OpenAI_NavierStokes_Research_Paper.md),
and [`NavierStokesReview/evidence/compact_fixed_force_perturbation_2026-09-24.md`](NavierStokesReview/evidence/compact_fixed_force_perturbation_2026-09-24.md).

## Navier Stokes

For every positive viscosity, we prove two results:

- **Whole space $\mathbb{R}^3$:** There exist smooth initial data and forcing for
  which no global smooth solution with uniformly bounded kinetic energy exists.
- **Periodic torus $\mathbb{R}^3/\mathbb{Z}^3$:** There exist smooth periodic
  initial data and forcing for which no global smooth solution exists.

These are alternatives [**(C)**](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf#page=2) “Breakdown of Navier–Stokes solutions on ℝ³”
and [**(D)**](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf#page=2) “Breakdown of Navier–Stokes Solutions on ℝ³/ℤ³”
in the Clay Mathematics Institute’s [official problem description](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)
of the [Navier–Stokes existence and smoothness](https://www.claymath.org/millennium/navier-stokes-equation/)
[Millennium Prize Problem](https://www.claymath.org/millennium-problems/).

## Euler

We construct smooth, compactly supported, divergence-free initial velocity on
$\mathbb{R}^3$ whose solution to the unforced incompressible Euler equations
develops a singularity in finite time. The velocity’s $C^1$ norm becomes unbounded
near that time, and the time integral of the vorticity’s $L^\infty$ norm diverges.

## Building the formalizations

The project uses Lean 4.34.0-rc2, Mathlib, and Lake. With
[elan](https://github.com/leanprover/elan) installed, fetch the mathlib cache and build the formalizations with:

```sh
lake exe cache get
lake build
```

## Independent proof checking

For instructions on checking the formalizations with Comparator, see the
[ComparatorChallenges README](ComparatorChallenges/README.md).
