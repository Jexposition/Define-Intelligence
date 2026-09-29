# Priority 126: selected-field finite-prefix and radial transport review

## Result

This tranche closes an important potential blindside in the **review
workspace**, not in OpenAI's source tree. The review project now contains a
concrete selected-field transport chain as an auditor-authored completion
target. It is therefore not accurate to say that the review workspace only
has generic `StageEstimates` or that no selected field can be traced to a
radial observable. Conversely, these completion files are not evidence that
OpenAI supplied the corresponding bridge in `NavierStokes/`; they define and
test the obligations that must be checked against that source.

The auditor-authored declarations establish the following test sequence for a
selected schedule `a`:

\[
  \texttt{selectedPotentialSum}
  \longrightarrow \texttt{partialPotential}_N
  \longrightarrow \nabla\times\texttt{partialPotential}_N
  \longrightarrow \texttt{periodicVelocity}
  \longrightarrow \texttt{selectedMixedProductionScalar}
  \longrightarrow \texttt{barMoment}.
\]

They also expose the exact cutoff commutator in the finite-prefix test field:

\[
\operatorname{cutVelocity}(A_N)
 = c\,\nabla\times A_N + (\nabla c)\times A_N.
\]

That is a concrete selected-field identity, not a toy model.

## Declarations reviewed

| Source | What is proved | Boundary |
|---|---|---|
| `SelectedFieldFinitePrefix.lean` | Existence of the selected schedule and local/all-jet finite-prefix equality for `potentialSum`. | Local eventual equality; no radial observable. |
| `SelectedPotentialPrefixCurlExpansion.lean` | Local finite-prefix equality after applying spatial curl. | No radial pullback or `tsum`-integral interchange. |
| `SelectedPotentialStagewiseCurlOnPhysicalDomain.lean` | On the physical domain, the velocity is eventually equal to a finite sum of stage curls. | Domain-local and eventual; no global moment value. |
| `SelectedPotentialProductionProductRule.lean` | Selected potential branch product rule with the `fderiv` cutoff commutator. | No sign or nonzero evaluation of the commutator. |
| `SelectedPotentialProductionFinitePrefix.lean` | Finite-prefix product expansion and a typed finite-prefix `barMoment` application. | Finite `N`; no limit theorem for the selected `tsum`. |
| `SelectedPotentialProductionRadialScalar.lean` | Actual selected potential sum radial component and a schedule-level product-rule transport theorem. | Positive-radius/physical-domain hypotheses; not the five-tuple equality. |
| `SelectedMixedVelocityDecomposition.lean` | Exact order: curl/localised potential branch plus separately cut/periodised direct branch. | Prevents applying a curl identity to the wrong branch. |
| `SelectedMixedProductionRadialComponent.lean` | First Cartesian component of the actual mixed periodic velocity on the radial section. | Defines the scalar; does not evaluate its moment. |
| `SelectedMixedProductionBarMoment.lean` | Explicit scalar-family pullback and generic `barMoment` integral formula. | Requires the supplied point map and scalar family. |
| `SelectedMixedProductionBranchSplit.lean` | Pointwise split into potential and direct scalar branches. | No integral linearity or cancellation theorem. |
| `SelectedMixedProductionTorusAverage.lean` | Auxiliary torus average reduces to the radial scalar. | Leaves the radial integral unevaluated. |
| `SelectedPotentialProductionBarMomentSection.lean` | Positive-radius physical point pullback identity. | Off-axis section; no origin/global chart bridge. |
| `SelectedPotentialProductionTorusAverage.lean` | Finite-prefix torus-average and radial reduction. | Finite prefix only. |
| `SelectedMixedRadialPeriodicity.lean` | Exact radius-periodicity of the mixed radial integrand. | Periodicity is not nonzero value and is not integrability. |

## Correct interpretation

The review workspace therefore supports a stronger testing statement than
the earlier generic interface-only description:

- selected physical data are present;
- the selected potential/direct branches are concretely assembled;
- finite-prefix curl and localisation identities are present;
- the cutoff-gradient term is explicit;
- torus averaging and physical-point pullback are present;
- the mixed radial integrand is defined and its periodicity is proved.

The remaining gap for the OpenAI paper-to-code audit is narrower and more
demanding:

1. a theorem passing the actual selected finite-prefix identities to the
   infinite selected `tsum` under the radial integral;
2. a theorem controlling the cutoff commutator and direct branch in the
   relevant global radial observables;
3. a global/on-axis extension of the positive-radius pullback; and
4. a theorem identifying the resulting five observables with
   \((M,I,J,S,C_p)\), or a concrete theorem proving a nonzero defect.

None of the inspected completion declarations proves \(\Delta m\ne0\), an impossibility
of transport, or kernel-level `False`. Conversely, the existence of this
chain means the audit must not claim that all curl/cutoff/periodisation
transport is absent. The correct status remains `CTR-005`: the complete
paper-level selected-field observable transport is not established by the
inspected record.
