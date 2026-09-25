# Selected mixed velocity decomposition

**Tree:** review branch at the source tree audited on 2026-09-25
**Review theorem:** `NavierStokesReview/src/completions/SelectedMixedVelocityDecomposition.lean`
**Build:** `lake build NavierStokesReview` — 3702 jobs, successful; the new
module contains no `sorry`, custom `axiom`, or `unsafe`.

## Result

The selected mixed velocity is not defined as the curl of one combined
potential.  The exact production definition is

$$
u_{\mathrm{mixed}}
=\operatorname{curl}\!\left(\sum_j \chi_j A_j\right)
 +\sum_j\chi_j B_j.
$$

`MixedDiagonalResidual.velocity` at
`NavierStokes/MixedDiagonalResidual.lean:26-29` defines the first term with
`SolenoidalDiagonal.velocitySum` and the second with
`SolenoidalDiagonal.potentialSum`.  The review theorem
`selected_velocity_decomposition` proves this exact equality for
`selectedPotentialStages` and `selectedDirectStages`; its pointwise form is
`selected_velocity_decomposition_at`.

The downstream periodic field is also split.  At
`NavierStokes/MixedPeriodicAssembly.lean:36-38`,
`periodicVelocity A v` is

$$
\operatorname{periodicVelocity}(A,v)
=\operatorname{periodicVelocity}(A)+
  \operatorname{periodize}(\operatorname{cutPotential}(v)).
$$

The review theorem `selected_periodic_velocity_decomposition` records the
selected instance.  The local-equality theorems at lines 67–84 of the same
source file show that this split is preserved near the inner cube/plateau;
they do not identify the direct summand with a curl.

## Consequence for the counter-paper

The cutoff-curl commutator

$$
\nabla\times(\chi A)=\chi(\nabla\times A)+(\nabla\chi)\times A
$$

is a valid target for the potential summand only.  It cannot be applied to
the direct angular summand without a separately proved representation of that
summand as a curl.  Therefore the scratch-space proposal that treats the
whole selected field as one localised curl is too strong and has been
corrected in the review plan.

This result narrows, rather than closes, the live disproof route.  A selected
`\Delta m \ne 0` still requires a field-level map for both summands through
cylindrical projection, torus averaging, radial integration, and boundary
terms.  The decomposition itself is not a contradiction.

## Source map

| Object | Source |
|---|---|
| Cut stage and potential sum | `NavierStokes/SolenoidalDiagonal.lean:32-38` |
| Curl-derived velocity sum | `NavierStokes/SolenoidalDiagonal.lean:188-190` |
| Mixed velocity | `NavierStokes/MixedDiagonalResidual.lean:26-29` |
| Residual identity | `NavierStokes/MixedDiagonalResidual.lean:45-49` |
| Periodic split | `NavierStokes/MixedPeriodicAssembly.lean:36-38` |
| Selected aliases | `NavierStokes/ActualCandidateAssembly.lean:1165-1175` |
| Selected witness gate | `NavierStokes/ActualCandidateAssembly.lean:1177-1181` |
