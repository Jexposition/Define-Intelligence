# Priority 129: External R3 pressure, localization, and paper-assembly source review

Date: 2026-09-28
Scope: OpenAI source files outside the currently captured `NavierStokesR3.theorem_1_1` import closure.  They are reviewed because their names and declarations are plausible locations for pressure, periodization, local-paper, or hidden transport claims.

This report is source evidence, not a proof of absence.  “Endpoint-external” means only that the current register does not place the file in the captured endpoint closure.  It does not mean dead code, irrelevant mathematics, or uncompiled source.

## Findings that change the probe logic

1. `PeriodizePDE.lean` contains a real conditional PDE transport theorem.  `navier_stokes_periodize` proves that periodizing supported `u`, `p`, and `f` preserves the forced residual, but only under `SupportedInCube`, `r < 1/2`, and a pre-existing whole-space residual identity.  Therefore the audit must not say “periodization is unproved” in general.  The remaining question is whether the selected endpoint supplies the exact hypotheses and whether periodization transports the paper’s five radial observables.  The theorem’s conclusion is residual covariance, not five-moment equality.

2. `LocalPotentialRebundle.lean` contains a concrete selected schedule construction.  Its `sum_eq_first` theorem collapses the `potentialSum` pointwise at an exterior point when stage zero is known and all successor stages vanish there.  `selectedPotential_eq_base`, `selectedDirect_eq_zero`, and `pressure_eq_base` then establish exterior identities under explicit domain and cutoff-smallness hypotheses.  This is stronger than a generic interface countermodel, but it is local/exterior and does not prove a global `barMoment` or a five-tuple equality.

3. `LocalPaperTheorem.lean` packages substantial local properties: smoothness, curl decomposition, divergence-freeness, extensions, jet bounds, residual flatness, exterior residual zero, and angular growth.  Its `Properties` structure contains no field-level `M, I, J, S, C_p` observable.  `local_theorem` proves existence of this local property package, not the paper-to-global-moment transport statement.

4. `R3PressureKernel.lean` proves an explicit integrable majorant and exact scaling for a model kernel.  Its module comment expressly separates that result from identifying the Riesz-transform commutator with the kernel.  It cannot be cited as an absolute pressure-Poisson representation for the selected candidate.

5. `R3PressureNearKernel.lean` extends the majorant/scaling analysis to near and remainder profiles and proves `L^p` bounds.  It contains no selected witness, Cartesian field, `barMoment`, or five-moment transport theorem.

6. `R3SmoothPressure.lean` proves a conditional smooth pressure-gradient representation.  It assumes concrete `U`, `V`, `G`, `p` smoothness, `MemLp` hypotheses, divergence identities, and an exact momentum identity.  The theorem concludes equality of represented distributions for a pressure gradient.  It is not, by its type, a global pressure theorem for `ActualCandidateAssembly.selected_witness`; it also does not establish the five radial moments.

7. `LocalHeatFormula.lean` proves the heat-exterior scalar formulas, the radial heat equation, the angular velocity representation, and a pressure radial integral with integrability.  These are genuine local/exterior identities and must be credited.  They do not by themselves identify the final global Cartesian field or transport the five profile moments through curl, localization, periodization, and `tsum`.

8. `SharpGluedStageBounds.lean`, `SharpParticularGluing.lean`, and `WholeDomainInitializationBounds.lean` prove stagewise `LogBound` estimates for potential, pressure, direct, and spatial-curl fields.  These are quantitative regularity/rate statements.  The inspected declarations do not contain a radial observable or a theorem commuting `barMoment` with the global construction.

9. `R3/ParabolicSupport.lean` proves compact-support preservation under affine time/spatial scaling and placement of compact spatial sets in a cube.  It is support geometry, not moment transport or pressure-Poisson semantics.

10. `ComparatorR3Theorem.lean` and `ComparatorTheorem.lean` translate candidate properties into CMI-style comparator quantifiers.  They are important endpoint bridges, but their conclusions are existential comparator statements.  They do not repair the missing paper-observable equality.

11. `NaturalAxisJointAnalytic.lean` and `InitialHarmonicContinuation.lean` establish analyticity, periodicity, and harmonic continuation data for their own inputs.  Their declarations are not selected-witness moment certificates merely because they mention pressure, periodicity, or continuation.

## File-level source matrix

| Source file | Direct role established by declarations | What it does not establish for this audit |
|---|---|---|
| `R3PressureKernel.lean` | Kernel majorant, integrability, exact (R^{-1}) moment scaling, (L^{4/3}) norm | Selected pressure identity; Riesz transform identification; five moments |
| `R3PressureNearKernel.lean` | Near/remainder radial profiles, scaling, (L^p) bounds | Selected field or global radial observable |
| `R3SmoothPressure.lean` | Conditional distributional pressure-gradient representation | Binding to selected witness; absolute global candidate Poisson theorem; five moments |
| `LocalHeatFormula.lean` | Heat exterior velocity, radial pressure integral, integrability | Global Cartesian transport |
| `NaturalAxisJointAnalytic.lean` | Analytic coefficient/amplitude/pressure profiles | Selected endpoint transport |
| `InitialHarmonicContinuation.lean` | Periodic/harmonic continuation objects and field periodicity | Five-moment equality after global assembly |
| `LocalPotentialRebundle.lean` | Concrete selected stage rebundling; exterior finite-sum collapse; exterior field identities | Global `tsum`/radial integral interchange; five-moment tuple |
| `PeriodizePDE.lean` | Conditional translation covariance and forced residual preservation under periodization | Observable transport; endpoint reachability of its hypotheses |
| `ComparatorR3Theorem.lean` | CMI option-C comparator packaging | Physical provenance; five-moment transport |
| `ComparatorTheorem.lean` | CMI option-D comparator packaging | Physical provenance; five-moment transport |
| `LocalPaperTheorem.lean` | Local smoothness, divergence, decomposition, residual flatness, exterior zero, angular growth | Five cumulative radial observables |
| `R3/ParabolicSupport.lean` | Affine support scaling and cube placement | Pressure semantics; moment transport |
| `SharpGluedStageBounds.lean` | Stagewise potential/pressure/curl log bounds | Integral observables and tuple equality |
| `SharpParticularGluing.lean` | Local potential/pressure gluing bounds | Global selected-field identity |
| `WholeDomainInitializationBounds.lean` | Initial potential/pressure/direct bounds and base-field rate bounds | Five-moment transport |

## Adversarial correction to existing probes

The probes must now carry three separate tests:

* **Concrete local identity test:** accept `LocalPotentialRebundle` and `LocalPaperTheorem` as genuine selected-field evidence, but record their domain hypotheses and conclusion scope.
* **Global transport test:** require a theorem whose conclusion contains the selected global field, the actual radial observable, and the interchange/limit hypotheses for `tsum`, periodization, and radial integration. A type-level “ghost debt” countermodel cannot substitute for this.
* **Pressure semantic test:** distinguish (i) kernel majorants, (ii) conditional distributional pressure-gradient recovery, (iii) relative pressure comparison, and (iv) an absolute selected-candidate Poisson/Leray representation. Only (iv) answers the strongest CMI correspondence question.

No declaration in this tranche authorises `False`, a nonzero selected-field defect, or a formally refuted verdict. The correct status remains an unresolved correspondence gate pending the exact selected-field global calculation.

## Reproducibility record

The tranche navigation report is generated by:

`NavierStokesReview/src/audit/source_tranche_summary.py`

Output:

`NavierStokesReview/evidence/source_tranche_summary_2026-09-28.json`

The output records 15 files, imports, declaration lines, keyword lines, and sorry-token lines. It is a navigation index, not a proof or absence detector.
