# Priority 118: selected mixed-moment residual decomposition

**Date:** 2026-09-28
**Status:** source-reviewed; new completion is not compiler-verified because the
repository-level `NavierStokesReview` build timed out while reconstructing
missing `.olean` files.

## Proves

`SelectedMixedProductionRadialComponent.lean:31-44` defines the actual selected
mixed radial scalar and proves its pointwise split into:

\[
  m_{\mathrm{mixed}}(a,p)
  =m_{\mathrm{potential}}(a,p)+m_{\mathrm{direct}}(a,p).
\]

`SelectedMixedProductionBranchSplit.lean:43-49` transports that split to the
`ScalarField` domain consumed by `barMoment`.
`SelectedMixedProductionBarMomentLinearity.lean:25-44` then proves conditional
linearity under the source `Shell α β` hypotheses.

The new completion
`SelectedMixedMomentResidualDecomposition.lean` records the exact order-two
residual identity:

\[
 \operatorname{barMoment}_2(m_{\mathrm{mixed}})-
 \operatorname{barMoment}_2(m_{\mathrm{potential}})=
 \operatorname{barMoment}_2(m_{\mathrm{direct}}).
\]

Under the additional selected direct-branch zero premise it records the
consequence:

\[
  \operatorname{barMoment}_2(m_{\mathrm{mixed}})=
  \operatorname{barMoment}_2(m_{\mathrm{potential}})
\]

**only when** both branch `Shell` hypotheses and the selected direct-branch
zero-moment theorem are supplied.  It also records the corresponding
zero-equivalence.

## Does not prove

- It does not prove the selected direct production branch has zero moment.
- It does not identify `selectedDirectProductionPointScalar` with
  `angularNativeStages` or with `selectedDirectScalar` from
  `SelectedDirectRadialMomentBridge.lean`.
- It does not evaluate the potential branch.
- It does not evaluate any of the five paper observables.
- It does not derive `False`, a nonzero defect, or a CMI refutation.

## Missing hypotheses exposed by the composition

The existing native-stage result
`SelectedDirectRadialMomentBridge.lean:31-53` proves a zero order-two moment
for `angularNativeStages`.  The actual selected mixed direct branch is instead
the periodised, cut-potential expression built from `selectedDirectSum` in
`SelectedMixedProductionRadialComponent.lean:26-35`.  A theorem connecting
those two objects is still required before the native zero result can be
reused.

This is a concrete blindside check: the branch names are similar, but the
terms are not definitionally equal.  The audit therefore keeps the direct
branch as an explicit residual rather than silently substituting the native
stage theorem.

## Compiler record

The direct file check initially failed because review `.olean` files were
missing.  A bounded `lake build NavierStokesReview` was then attempted with
the repository's pinned Lean 4.34.0-rc2 toolchain, but exceeded 120 seconds
while rebuilding the dependency closure.  The spawned `lake`/`lean` workers
were terminated.  No compiler success is claimed for the new completion until
that build is rerun to completion.
