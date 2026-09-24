# Correction-moment transport audit

**Date:** 2026-09-24  
**Finding:** the zero rows preserve two radial correction moments, but the
selected endpoint does not expose their transport into the exported velocity.

## Source ledger

| Location | Exact consequence |
|---|---|
| `NavierStokes/FiveRowRank.lean:240-246` | `FiveRows` constrains `dv` and `ga`: `∫ R, R^2 * dv R = 0` and `∫ R, R * ga R = 0`, followed by three debt equations. |
| `NavierStokes/FiveRowRank.lean:279-284` | `five_rows` constructs the full predicate for arbitrary three-coordinate debt, so the rank interface is not restricted to zero debt. |
| `NavierStokes/MeanRankUpdate.lean:29-34` | `scaleDebt` scales the three debt coordinates `(P,Jθ,Jz)`; it does not introduce the paper's five named moments. |
| `NavierStokes/CorrectionState.lean:149-165` | `addIncrement` updates the mean state and `totalVelocity_addIncrement` exposes the corresponding total velocity update. |
| `NavierStokes/CorrectionState.lean:241-251` | `debt` is `Fin 3 → ℝ`; `ZeroMasses` means `radialMoment 2` of the angular mean and `radialMoment 1` of the axial mean are zero. These are not kinetic-energy definitions. |
| `NavierStokes/CorrectionState.lean:444-458` | `rankStage` is built from `rankIncrement`; `rank_model_rows` proves the five-row equations for that constructed increment. |
| `NavierStokes/DefectIncrementBounds.lean:621-646` | `fiveRows_mass_zero` and `fiveRows_preserve_masses` prove the two radial-moment consequences and their preservation under `updated`. |
| `NavierStokes/DefectIncrementBounds.lean:799-813` | `RankGeometry.preserve_masses` and `RankGeometry.zeroMasses` transport those consequences through the generic rank stage. |
| `NavierStokes/ActualPhysicalPrefixFields.lean:342-356,475-491` | `StageRealizations` and `physicalFields_all` expose stage/germ/pressure data, but no five-moment equality or `ZeroMasses` field. |
| `NavierStokes/ActualCyclePreservation.lean:768-771,826-833` | `RunInvariant` contains `analytic`, `coherent`, and `periodic`; the selected cycle induction does not carry `ZeroMassesOn`. |
| `NavierStokes/ActualCandidateAssembly.lean:1121-1151,1177-1185` | `Witness` and `selected_witness` contain fields, residual/force properties, jets, decay, energy, and blow-up consequences, but no rank debt, correction-moment, kinetic-energy identity, or paper tuple `(M,I,J,S,C_p)`. |
| `NavierStokes/ActualInitialization.lean:1387-1389` | An initial zero-moment fact exists, but this is not a selected-cycle transport theorem. |

## Formal result

`NavierStokesReview/src/completions/CorrectionInvariantScope.lean` compiles
without `sorry`, `axiom`, or `unsafe`. It proves:

1. the two zero rows imply zero `barMoment 2` angular correction and zero
   `barMoment 1` axial correction;
2. either corresponding nonzero correction moment yields `False` under the
   complete `FiveRows` hypotheses;
3. the generic `RankGeometry.preserve_masses` theorem preserves those two
   radial moments through `rankStage`.

The last result is the exact usable obstruction. A compact perturbation would
produce a selected-path contradiction only after a further theorem identified
that perturbation with `rankIncrement` and proved one of the two radial moments
nonzero. No such theorem is present in the `Witness` or `RunInvariant` types.

## Boundary of the claim

The source does **not** establish that the zero rows freeze total mass, kinetic
energy, or the full Cartesian velocity. It also does not establish that the
two radial moments are the paper's `(M,I,J,S,C_p)`. Accordingly, this audit
strengthens CTR-005 as a missing selected-path transport theorem; it does not
yet supply a selected-witness `False` theorem.
