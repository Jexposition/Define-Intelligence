# Priority 231: conditional selected mixed radial integral composition

Date: 2026-10-01
Status: compiled; pointwise composition hypothesis remains explicit
Disposition: strengthens CTR-005; final transport remains not established

## Result

The review-side completion

NavierStokesReview/src/completions/SelectedMixedProductionBarMomentProductRule.lean

compiles with exit code 0 under the pinned Lean 4.34.0-rc2 toolchain after
the previously compiled review completion is emitted to the Lake build path.

The theorem applies the exact torus-average/radial reduction to the selected
mixed scalar and transports the complete three-term product-rule formula under
the weighted radial integral:

\[
\operatorname{barMoment}_k(u_{\mathrm{mixed}})
 =
 \int r^k\left[
 c(\nabla\times A_{\mathrm{selected}})_1
 +((\nabla c)\times A_{\mathrm{selected}})_1
 +(\operatorname{periodise}(\operatorname{cutDirect}_{\mathrm{selected}}))_1
 \right]\,dr.
\]

## Important hypothesis boundary

The theorem requires an explicit pointwise hypothesis giving the composed
three-term formula at every integration radius. That hypothesis is not
silently discharged by selected_witness. This is deliberate: the current
production endpoint does not export the required global differentiability and
coordinate conditions for every radial integration point.

The result therefore establishes the exact form of the remaining integral
calculation, while preserving the missing assumptions rather than hiding
them.

## What remains open

This theorem does not prove:

- radial support or integrability for the selected mixed scalar;
- a sign or nonzero value for the commutator;
- cancellation or reinforcement between the three terms;
- equality with the manuscript's (M,I,J,S,Cp);
- pressure and residual transport for the five observables.

The next scientific gate must either discharge the pointwise hypotheses and
evaluate the integral from the actual selected definitions, or prove that a
required hypothesis cannot hold. A toy profile or generic abstract debt
countermodel is not a substitute.

## Reproduction

The dependency completion was emitted with:

    elan run leanprover/lean4:v4.34.0-rc2 lake env lean -o .lake/build/lib/lean/completions/SelectedMixedProductionFullProductRule.olean NavierStokesReview/src/completions/SelectedMixedProductionFullProductRule.lean

The target was then replayed with:

    elan run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/completions/SelectedMixedProductionBarMomentProductRule.lean

Both Lean invocations returned exit code 0. No source admission or axiom
declaration was added.

Related evidence is Priority 230 and the exact torus-average reduction in
SelectedMixedProductionTorusAverage.lean.
