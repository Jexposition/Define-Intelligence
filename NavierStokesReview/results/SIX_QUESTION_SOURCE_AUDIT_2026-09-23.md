# Six-question source audit of the OpenAI Navier–Stokes claim

Snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`  
Review date: 2026-09-23  
Scope: source-level semantic review, not a compilation-only check.

## Verdict

The six questions do not yet supply a source-backed fatal Lean error. They do
identify several overclaims and two important scope limits. The repository
does not prove an autonomous, force-independent blow-up, does not formalise
the Ladyzhenskaya or hypo-dissipative variants, and the named draft paths do
not match this snapshot. Those facts do not by themselves refute CMI
alternatives (C) and (D), because those alternatives allow an existential
smooth external force for the classical Newtonian equation.

The correct review status remains **NOT ESTABLISHED as a fully verified
mathematical CMI proof**, not **REFUTED**. The load-bearing unresolved audit
is the provenance and non-vacuity of the residual-limit, pressure-flux, and
comparison estimates.

## Question-by-question disposition

| No. | Audit question | Source result | Disposition |
|---|---|---|---|
| 1 | Is `f` functionally independent of `u`? | `CandidateFromLimits.lean:82` constructs `force` from the traced residual of the already constructed `u,p`; `:99-112` identifies it with the residual throughout `0 ≤ t < 1`. | **Confirmed a-posteriori forcing.** This defeats an autonomous-physics interpretation, but is not alone a C/D mismatch because C/D quantify over a suitable smooth force. |
| 2 | Is `f` smooth across `T* = 1`? | `SpacetimeGluing.smoothExtension` is used with normal-jet matching. `CandidateFromLimits.tracedResidual_smooth` consumes derivative recurrences and locally uniform endpoint limits before the gluing theorem applies. | **Not a free cutoff claim.** Smooth extension is explicitly attempted, but its validity depends on the upstream trace and all-jet limit chain. Audit those premises; do not claim either automatic success or a demonstrated failure. |
| 3 | Does the force survive Ladyzhenskaya regularisation? | No theorem in the pinned source tests `S(Du)=2(ν₀+ν₁|Du|^{p-2})Du` for `p≥3`, nor proves divergence of a regularised tracking force. | **Out of scope.** This is a robustness question about a different PDE, not a refutation of the claimed classical forced result. |
| 4 | Does the proof cover `α<1` hypodissipation? | The headline route is the classical positive-viscosity Laplacian route. No formal parameterised theorem covering `α<1` was located. | **Scope limitation.** It cannot be advertised as a proof for hypo-dissipative equations, but absence of that variant does not invalidate a theorem stated for the classical equation. |
| 5 | Is the pressure construction the claimed Fourier/Leray proof? | `NavierStokes/R3PressureFourier.lean` is real and contains Riesz-symbol, Poisson, and `L²` pressure lemmas. The headline uniqueness path instead imports the `R3/RieszTestOperators`, pressure-recovery, and pressure-flux hierarchy. | **Provenance correction.** Pressure machinery is substantial; the supplied claim that the separately named file is the direct headline proof path is not established. Audit the actual imported hierarchy and its hypotheses. |
| 6 | Are singular divisions guarded by `t < T*`? | The cited `Scaling/SingularLimits.lean` is absent. The actual origin formula in `ConstructedSlowBase.lean` uses `(1-t)^(-A)` and requires `t < 1`; inspected moment/scaling divisions carry positivity or nonzero premises. | **No source-confirmed division failure.** Lean’s total division semantics remain an audit obligation, but this specific allegation is not demonstrated in the pinned source. |

## Confirmed issues and overclaims

1. The force is a residual chosen after the candidate fields, and it remains
   active during the entire pre-singular interval. The source only proves
   zero force for `t ≤ 0` and `t ≥ 2`; it does not prove force-off before
   `T* = 1`.
2. The nonlinear-regularisation and `α<1` arguments are not formal findings
   about this repository. They should be labelled unformalised robustness
   tests, not proof failures.
3. Several supplied drafts cite paths absent from the snapshot, including
   `Forcing/Smoothness.lean`, `Pressure/LerayProjection.lean`,
   `Scaling/SingularLimits.lean`, and `EnergyDefect.lean`.
4. The five-moment machinery is present and imported through
   `ModulatedHistories → ModulatedCone → ModulatedProfileAssembly →
   ConstructedSlowBase`. Its local invertibility lemmas are real. They do
   not, without tracing the downstream residual identities, independently
   prove every claimed PDE and far-field consequence.
5. `DiagonalResidual.JetRate` has no `NeBot` premise. The selected endpoint is
   nontrivial, but every derived intersection filter used by the residual
   chain still needs its own non-vacuity proof.

## Required next checks

- Map every `StageEstimates`, endpoint-trace, and residual-rate hypothesis to
  its construction rather than accepting a compiled interface as evidence.
- Prove `NeBot` or an equivalent geometric neighbourhood statement for every
  derived filter in the selected residual chain.
- Audit the actual pressure-recovery and pressure-flux imports against the
  exact global-solution interface and common spatial domain.
- Keep the final claim split into: forced C/D-shaped formal statement,
  unforced A/B claim, and independent human validation of the analytic
  construction.

