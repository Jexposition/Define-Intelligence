# Priority 90 source review: moment matrices, prepared profiles, Gaussian integrability, and smooth repair

## Scope

This tranche reviews five reachable modules at the next high-priority moment/profile boundary. It distinguishes general finite-dimensional solvability and profile scheduling from the public selected Cartesian endpoint.

## Findings

| Module | Source-grounded result | Boundary |
|---|---|---|
| `PowerMomentMatrix.lean` | Proves nonsingularity of exponential and positive-power evaluation matrices, existence of zeros from vanishing interval integrals, exact integral expansion for power sums, and nonsingularity of interval/bump moment matrices under injectivity, positivity, separation, and nonzero-mass hypotheses. | This is a genuine general repair-matrix theorem. It does not instantiate the final selected field or the five paper observables. |
| `PreparedOutgoing.lean` | Defines `PreparedProfile`, proves existence from the scheduled family, proves that the nominal matching radius can exceed any prescribed floor while keeping the prepared profile and schedule fixed, and packages a chosen profile via `prepared`. | This establishes profile preparation and late matching, not endpoint Cartesian transport. |
| `R3/GaussianMoments.lean` | Proves integrability on \(\mathbb R^3\) of Gaussian, first norm, and second norm-weighted Gaussian functions using an explicit half-decay estimate. | This supports whole-space analytic estimates; it is not a selected moment identity or pressure representation. |
| `ScheduledProfileChoice.lean` | Constructs scheduled cores and profiles below caller-supplied positive bounds, proves height-cap positivity/bounds, and packages an additional small-tail condition. | This is genuine schedule/profile existence. It does not connect its output to `ActualCandidateAssembly.Witness`. |
| `SmoothMomentRepair.lean` | Defines a quadratic repair equation on a normed space, proves local analytic/smooth solution branches by an inverse-function argument, supplies norm bounds, uniqueness in a correction ball, compact-parameter inverse bounds, and uniform small-correction existence. | This is a strong abstract nonlinear repair theorem. Its variables are generic continuous-linear/bilinear operators and a debt vector, not the selected Cartesian radial observables. |

## Controlled conclusion

These files strengthen the positive mathematical record. In particular, `PowerMomentMatrix` and `SmoothMomentRepair` show that repair solvability is not merely an informal claim, while `PreparedOutgoing` and `ScheduledProfileChoice` show that profile selection and late matching are formally packaged. `GaussianMoments` supplies the whole-space integrability needed by downstream estimates.

They do not close the selected-path question:

\[
\text{general moment-matrix/repair solvability}
\;\not\Rightarrow\;
\text{the final selected Cartesian field has }(M,I,J,S,C_p).
\]

No declaration reviewed here composes these results through the selected potential sums, curl/localisation, infinite stage assembly, periodisation, radial averaging, and public `Witness`. No nonzero defect, impossibility theorem, or kernel-level `False` is established.

## Register action

The five modules are to be marked `evidence_inspected` in the authoritative register after adding their bounded source records to `semantic_coverage_register.py` and regenerating the JSON, Markdown, HTML, and public mirror files.
