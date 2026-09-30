# Priority 225: selected mixed `barMoment` shell gate

Date: 2026-10-01
Status: compiled review-side completion; value transport remains open
Scientific disposition: `CTR-005: NOT ESTABLISHED`

## Question

Can the selected mixed production field be reduced to the repository's
`barMoment` operator with the support and smoothness premises required for
linearity, rather than only through a caller-supplied interface?

## Source-level result

The production operators are explicit:

\[
A_{\mathrm{sum}}=\sum_j \chi_jA_j,
\qquad
u_{\mathrm{pot}}=\nabla\times A_{\mathrm{sum}},
\qquad
u_{\mathrm{loc}}=\nabla\times(cA).
\]

The source proves the cutoff product rule

\[
u_{\mathrm{loc}}
=c(\nabla\times A)
 +\operatorname{curlLinear}\big((Dc)\,A\big)
\]

at `NavierStokes/SpatialLocalization.lean:199-207`. The mixed production
field then adds the separately cut and periodised direct branch through
`NavierStokes/MixedPeriodicAssembly.lean:29-38`.

The review-side completions prove the following exact facts:

- `SelectedMixedVelocityFinitePrefix.lean` gives separate local finite-prefix
  representatives for the potential-curl and direct branches.
- `SelectedMixedProductionBarMoment.lean` pulls the mixed first component back
  to the scalar-family domain consumed by `barMoment` and proves the exact
  integral application formula.
- `SelectedMixedProductionBranchSplit.lean` proves the pointwise mixed
  production scalar equals the potential branch plus the direct branch.
- `SelectedMixedProductionBarMomentLinearity.lean` proves `barMoment` additivity
  only under `Shell` hypotheses for both branches.
- `SelectedDirectNativePrefixMoment.lean` proves an order-two zero moment for
  the native direct prefix on the selected carrier, before Cartesian
  localisation. It does not identify that native scalar with the final mixed
  production field.
- `SelectedProductionDirectPrefixCutoff.lean` proves the finite-prefix cutoff
  identity and exposes the factor `(spatialCutoff - 1)`. It does not prove the
  resulting weighted moment is zero or nonzero.

## Exact remaining gate

The source definition of `Shell` requires, for each scalar-family index,

\[
\operatorname{ContDiff}^{\infty}(f_n)
\quad\text{and}\quad
\operatorname{RadiallySupported}_{[a,b]}(f_n).
\]

`barMoment_add` consumes those hypotheses. The selected mixed completion does
not derive them for the final mixed Cartesian pullback. In particular,
`SelectedMixedRadialSupportObstruction.lean` proves only the conditional fact
that a unit-periodic radial pullback with bounded radial support must vanish.
It explicitly leaves the required radial-support premise unproved. The
periodic global-integral completion separately records the conditional
`integral_undef` behaviour of a periodic function that is positive on one
fundamental interval; it does not assert that the selected field has that
sign.

Therefore the compiled bridge currently has this logical form:

\[
\begin{aligned}
&\operatorname{Shell}(f_{\mathrm{pot}})
\land\operatorname{Shell}(f_{\mathrm{dir}})\\
&\qquad\Longrightarrow
\bar M_k(f_{\mathrm{mixed}})
 =\bar M_k(f_{\mathrm{pot}})+\bar M_k(f_{\mathrm{dir}}),
\end{aligned}
\]

not the unconditional selected-field identity required to identify the
paper's complete `(M,I,J,S,C_p)` mechanism.

## Compilation record

The following six review-side files compiled with exit code 0 under
`leanprover/lean4:v4.34.0-rc2`, with no `sorry`, `admit`, or `axiom` additions:

```text
NavierStokesReview/src/completions/SelectedMixedProductionBarMomentLinearity.lean
NavierStokesReview/src/completions/SelectedMixedMomentResidualDecomposition.lean
NavierStokesReview/src/completions/SelectedMixedProductionBranchSplit.lean
NavierStokesReview/src/completions/SelectedMixedProductionBarMoment.lean
NavierStokesReview/src/completions/SelectedMixedVelocityFinitePrefix.lean
NavierStokesReview/src/completions/SelectedDirectNativePrefixMoment.lean
```

## Disposition

This closes a finite-prefix and conditional-linearity subtask. It does not
prove a selected nonzero defect, an impossibility theorem, force
nonsmoothness, literal CMI failure, or `False`. It strengthens the audit by
locating the exact support/integrability premises that must be derived before
any final selected `barMoment` value can be claimed.

`CTR-005: NOT ESTABLISHED` remains the controlled status for complete
manuscript-to-selected-endpoint fidelity.

## Evidence

- `../evidence/selected_mixed_barmoment_shell_gate_2026-10-01.md`
- `priority_218_selected_endpoint_crosswalk_replay_2026-10-01.md`
- `priority_223_source_only_transport_replay_2026-10-01.md`
- `../completions/SelectedMixedProductionBarMomentLinearity.lean`
- `../completions/SelectedMixedRadialSupportObstruction.lean`
