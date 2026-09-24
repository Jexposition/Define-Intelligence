# State-realisation axis-scope audit

## Result

The requested contradiction is not established. A stronger, source-backed
scope limitation is established: the `StateRealization`/`chartIdentity`
route is an off-axis chart argument and does not itself verify the singular
origin where `origin_blowup` is proved.

## Exact source footprints

| Source | Lines | Consequence |
|---|---:|---|
| `NavierStokes/PhysicalResidualJetBounds.lean` | 885-905 | `StateRealization` requires `radius_ne : ∀ x ∈ U, x.1.1 ≠ 0`; `base_equation` is quantified only over `x ∈ U`. |
| `NavierStokes/PhysicalResidualJetBounds.lean` | 906-923 | `physical_velocity_smooth`, `physical_pressure_differentiable`, `velocity_germ`, and `pressure_germ` are restricted to `graphSourceTZ ... U`. |
| `NavierStokes/PhysicalResidualTZ.lean` | 388-389 | `graphSourceTZ G U = {p | 0 < p.2 0 ∧ graphMapTZ G p ∈ U}`; every source point has strictly positive radial coordinate. |
| `NavierStokes/PhysicalResidualJetBounds.lean` | 927-966 | `StateRealization.chartIdentity` derives the residual identity only after constructing a positive-radius source point and an off-axis chart point. |
| `NavierStokes/ActualCycleResidualBounds.lean` | 915-954 | `selected_residual_jet_bound` applies `chartIdentity.germ` on an annular/sector domain; its input includes `w ∈ S` and a positive-radius annulus. |
| `NavierStokes/ActualCycleResidualBounds.lean` | 956-1000 | The selected JetRate is assembled by combining the off-axis bound with a separate `GlobalBaseError.originPast` bound outside `S`. |
| `NavierStokes/GermCandidateAssembly.lean` | 146-159 | `origin_blowup` is a separate origin argument, obtained from the base profile at spatial origin. |

## Zero-sorry probe

`NavierStokesReview/src/probes/StateRealizationAxisExclusionProbe.lean`
compiles with the pinned Lean toolchain. It proves:

1. `StateRealization.radius_ne` excludes every zero-radius point from `U`.
2. `graphSourceTZ` excludes `((1 : ℝ), (0 : Space))` because its first
   condition is `0 < p.2 0`.

## Audit disposition

This is a load-bearing correspondence gap, not yet a formal contradiction.
The repository may still establish origin residual limits through
`GlobalBaseError` and then use those limits in the gluing construction. To
upgrade this finding to a refutation, a zero-sorry theorem must show either:

- the separate origin residual estimate is false for the selected fields; or
- the off-axis `chartIdentity` is being used as if it supplied the missing
  origin identity; or
- the selected five-moment/pressure data force a nonzero origin residual,
  contradicting `VanishingJointJets`.

The probe therefore narrows CTR-005/CTR-038. It prevents the paper from citing
`StateRealization.chartIdentity` as an origin-valid global pressure/PDE bridge
without an additional axis-extension theorem.

## Independent re-audit of the piecewise rate theorem

The stronger claim that the two regions are merely patched without being
forced to agree is not established by the source. `selected_residual_jetRate`
does a case split on membership in `S`. On `S`, it uses the off-axis chart
bound. Outside `S`, it uses `houtside`, which states eventual equality of the
selected fields with the base fields, followed by `base_exterior_jetRate`.
That is a valid conditional piecewise estimate and does not by itself imply a
derivative discontinuity or a contradiction at the axis.

The surviving objection is an interface one: the theorem does not expose the
paper's five-moment identities or an absolute pressure-Poisson identity as
premises of this assembled rate. The source may be intentionally localising
the correction support away from the origin. Any formal disproof must therefore
show that this localisation is incompatible with the actual selected fields,
not merely observe that `chartIdentity` has a positive-radius domain.
