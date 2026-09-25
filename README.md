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
  The stronger `SameDatumFixedForcePerturbation.lean` version also makes the
  perturbation vanish at the initial time, so this objection does not rely on
  changing the selected zero initial datum.
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
transported forcing datum. `IndependentDataPerturbationProbe.lean`,
`CompactFixedForcePerturbation.lean`, and
`SameDatumFixedForcePerturbation.lean` then prove, without `sorry`, that holding
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

The upstream formalisation exports two C/D-shaped results for every positive
viscosity:

- **Whole space $\mathbb{R}^3$:** There exist smooth initial data and forcing for
  which no global smooth solution with uniformly bounded kinetic energy exists.
- **Periodic torus $\mathbb{R}^3/\mathbb{Z}^3$:** There exist smooth periodic
  initial data and forcing for which no global smooth solution exists.

These are alternatives [**(C)**](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf#page=2) “Breakdown of Navier–Stokes solutions on ℝ³”
and [**(D)**](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf#page=2) “Breakdown of Navier–Stokes Solutions on ℝ³/ℤ³”
in the Clay Mathematics Institute’s [official problem description](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)
of the [Navier–Stokes existence and smoothness](https://www.claymath.org/millennium/navier-stokes-equation/)
[Millennium Prize Problem](https://www.claymath.org/millennium-problems/).

The review does not treat that export as sufficient evidence for every claim in
the accompanying paper. In particular, the selected endpoint does not expose
the theorem identifying the paper's five named moments `(M, I, J, S, C_p)` with
the final mixed velocity, pressure, residual, and force. The authors bear the
burden of supplying that selected-field correspondence before the stronger
published solution claim is accepted. See the
[`official claim transport matrix`](NavierStokesReview/evidence/official_claim_transport_matrix_2026-09-24.md).

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

## Review status

The independent review fork contains a separate `NavierStokesReview` library.
Its fixed-force extension proves that the selected residual construction is
not stable under smooth, compactly supported, divergence-free velocity
perturbations when the force and pressure are held fixed. This is a formal
provenance objection under a stronger forward-data interpretation. It is not
presented as a literal `False` derivation from the C/D existential endpoint,
which does not encode force independence or perturbation stability. See
[`docs/OpenAI_NavierStokes_Peer_Review_v1.md`](docs/OpenAI_NavierStokes_Peer_Review_v1.md)
and
[`NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md`](NavierStokesReview/evidence/fixed_force_stability_extension_2026-09-24.md).

The current review also tracks the remaining field-level test rather than
assuming that upstream profile identities apply to the exported field. The
selected natural-indexed `tsum` must be followed through spatial curl,
localisation, Cartesian-to-cylindrical projection, and `barMoment`. A concrete
nonzero remainder would combine with the correction invariant to give a
kernel-level contradiction; until then, the result is a load-bearing
correspondence failure and the affirmative solution claim remains
**NOT ESTABLISHED**. The companion Euler interval audit found controlled
contraction and explicit value/first-derivative seam matching, so its proposed
Zeno and first-order-jump objections are not currently source-supported.
See [`docs/Euler_Parent_Child_Interval_Audit.md`](docs/Euler_Parent_Child_Interval_Audit.md)
and [`NavierStokesReview/tools/radial_profile_integrals.py`](NavierStokesReview/tools/radial_profile_integrals.py).

## Current selected-field calculation

The selected potential series is not an empty-limit artefact. A review-side
Lean completion proves that `selected_witness` supplies a concrete schedule,
that the selected `tsum` is locally equal to a finite prefix at every positive
preterminal point, and that the same prefix represents every iterated jet.
This closes the vacuity route without supplying the authors' missing physical
calculation.

The remaining question is whether that concrete Cartesian finite prefix,
including cutoff derivatives and curl terms, has the five radial moments used
in the paper. The repository still exposes no theorem transporting the
selected `VelocityField` into the scalar `barMoment` input. A symbolic helper
can calculate an explicitly supplied radial profile, but it cannot silently
identify that profile with the selected field. The review therefore records a
live route to a kernel contradiction, not a fabricated one.

The selected-field trace is now concrete at the direct-stage level:
`SelectedDirectPrefixField.lean` proves that the selected direct stages are
the actual angular mean stages and that each uncut finite prefix equals the
corresponding selected cycle-state mean angular field. This strengthens the
counter-paper's source claim. It still stops before the Cartesian-to-radial
`barMoment` equality, so no nonzero `Delta m` or `False` theorem is
claimed without that missing calculation.

The review has also checked the selected recurrence itself. A zero-sorry
completion proves that every selected cycle state carries the source
`ZeroMassesOn` invariant, so a stage-level leak cannot be alleged merely from
the two zero correction rows. A second completion exposes component one of
the selected angular field as the physical-atlas coefficient times the
corresponding angular-frame component. These results narrow the live test to
the actual coefficient, cutoff derivatives, curl, axis/tail terms, and
`barMoment`; they do not establish a nonzero remainder or `False`.

The selected direct stages are now also transported through the source's
positive-radius chart by `selected_direct_stage_eq_chart`. This removes a
generic or vacuous-stage explanation while leaving the decisive calculation
unchanged: localisation, Cartesian curl, axis/tail terms, torus averaging,
and the scalar `barMoment` must still be related by an explicit theorem.

The latest selected-field completion makes this gate concrete: on the
positive-radius chart, the atlas scalar coefficient is recovered from
component one of the selected angular field, with the radius nonvanishing
proved from the chart coordinate. This is not yet a radial-moment calculation.
The selected cutoff derivatives, Cartesian curl, torus average, axis, and
outer-tail terms still require an exact field-level theorem. See
[`NavierStokesReview/evidence/selected_cartesian_radial_gate_2026-09-25.md`](NavierStokesReview/evidence/selected_cartesian_radial_gate_2026-09-25.md).

The next exact term is now isolated. For a localised potential, the review
proves

$$
\mathrm{curl}(\chi A)
=\chi\mathrm{curl}(A)
+\mathrm{curlLinear}\big((D\chi).\mathrm{smulRight}(A)\big).
$$

This cutoff-gradient commutator must be included before a selected radial
moment can be evaluated. It is not being presented as a nonzero leak without
the remaining selected integral calculation.

The review now also has a selected radial-section identity: for positive
radius, the first Cartesian component of the actual angular field recovers its
scalar coefficient. At the axis the source uses a totalised zero angular
frame, so the recovery requires a separate boundary treatment. This narrows
the live calculation without asserting a nonzero remainder prematurely.

The axis branch is now source-verified as well: the first component of every
selected direct angular stage is exactly zero when both radial Cartesian
coordinates vanish. This is a totalised boundary value, not evidence of a
discontinuity. The live counter-paper calculation remains the full
Cartesian-to-radial composition, including localisation, curl, torus averaging,
and `barMoment`.

The production order of that composition is now source-verified too. The
selected velocity is

$$
\mathrm{curl}\!\left(\sum_j\chi_j A_j\right)
 +\sum_j\chi_j B_j,
$$

not one curl of a combined potential. The direct angular branch is added after
the potential curl, and periodic localisation preserves the split. The
cutoff-gradient commutator is therefore mandatory for the potential branch,
but cannot be used as a defect claim about the direct branch without a new
transport theorem. This correction keeps the counter-paper focused on the
actual selected field rather than a stronger surrogate.

Evidence: [`selected_mixed_velocity_decomposition_2026-09-25.md`](NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md).

The latest selected-path completion proves that every native direct angular
stage has zero order-2 radial `barMoment` on the selected region. This removes
that scalar branch as the source of a selected nonzero remainder. It does not
yet transport the identity to the final mixed Cartesian field or prove
`False`; the active target remains the potential/curl branch and the complete
Cartesian-to-radial calculation.

Evidence: [`selected_direct_stage_moment_transport_2026-09-25.md`](NavierStokesReview/evidence/selected_direct_stage_moment_transport_2026-09-25.md).

The latest selected-path completion also proves the potential-stage curl
equality on the actual Cartesian chart domain. This closes a local field
correspondence for the potential branch, but not the radial `barMoment`
transport. The remaining calculation must still include the separate direct
branch, torus average, axis/support limits, and boundary terms before any
`Delta m` or `False` result can be claimed. See
[`selected_potential_stage_chart_transport_2026-09-25.md`](NavierStokesReview/evidence/selected_potential_stage_chart_transport_2026-09-25.md).
