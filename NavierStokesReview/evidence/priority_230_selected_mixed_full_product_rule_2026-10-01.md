# Priority 230: selected mixed radial full product-rule composition

Date: 2026-10-01
Status: compiled; integral and five-observable bridge remain open
Disposition: CTR-005: NOT ESTABLISHED

## Result

The review-side completion

NavierStokesReview/src/completions/SelectedMixedProductionFullProductRule.lean

compiles with exit code 0 under:

    elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedMixedProductionFullProductRule.lean

The theorem composes the actual selected potential and direct branches at the
radial section. Under the explicit coordinate and differentiability
hypotheses, it proves:

\[
\begin{aligned}
u_{\mathrm{mixed},1}(p)
={}&c(x)\,(\nabla\times A_{\mathrm{selected}})(p)_1\\
&+\bigl((\nabla c)\times A_{\mathrm{selected}}\bigr)(p)_1\\
&+\operatorname{periodise}
   \bigl(\operatorname{cutDirect}_{\mathrm{selected}}\bigr)(p)_1.
\end{aligned}
\]

The first two terms are the exact cutoff-before-curl product rule. The third
term is the separately cut and periodised direct branch. All three terms are
the actual selected production definitions, not a toy profile or an abstract
debt variable.

## What this establishes

1. The selected mixed radial scalar is not being treated as a black box.
2. The cutoff-gradient commutator is present in the selected formula.
3. The direct branch is not silently discarded.
4. The formula is available before applying torus averaging and radial
   integration.

## What this does not establish

The theorem does not prove:

- that the commutator integral is nonzero;
- that the selected scalar has the support or integrability hypotheses required
  by barMoment;
- that the direct and potential terms cancel or reinforce;
- that the resulting radial integrals equal the manuscript's
  (M,I,J,S,Cp);
- that the selected pressure and residual carry the same five observables.

The next calculation must therefore apply the exact torus-average and radial
integration definitions to this formula, retain all three terms, and prove
either the advertised identity or a concrete selected mismatch. No numerical
or toy substitution is an acceptable replacement.

## Evidence boundary

This is a review-side completion over actual production definitions. It is
positive value-level composition evidence, not a production theorem exported
by ActualCandidateAssembly.Witness. The controlled status remains
CTR-005: NOT ESTABLISHED.

Related evidence:

- priority_229_manuscript_dependency_declaration_ledger_2026-10-01.md
- selected_mixed_production_torus_average in
  SelectedMixedProductionTorusAverage.lean
- selected_mixed_barMoment_radial_reduction in
  SelectedMixedProductionTorusAverage.lean
- selected_potential_production_radial_scalar_eq in
  SelectedPotentialProductionRadialScalar.lean
