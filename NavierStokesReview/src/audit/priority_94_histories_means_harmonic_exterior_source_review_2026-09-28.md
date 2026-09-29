# Priority 94 source review: histories, initial means, harmonic support, exterior prefixes, and signed families

Date: 2026-09-28
Method: direct declaration-level inspection of seven reachable Lean source files.

## Source findings

### `NavierStokes/ModulatedHistories.lean`

This module imports parametric modulation, shape transition, five-profile moments, and activation stocks. It defines five-coordinate density/history fields, periodic density families, smooth localisations, axis histories, profile rows, repair debt, edited fields, and repaired histories. Its declarations prove smoothness, periodicity and zero-mean properties, physical density identities, localised history differences, repair support/germ preservation, integrability, explicit repair identities, and restored actual histories.

This is strong reduced-profile history and moment-repair evidence. It does not identify the histories with the final Cartesian `barMoment` tuple after the complete potential/curl/localisation/periodisation/tsum path, and it does not export the result through `Witness`.

### `NavierStokes/ActualInitialMean.lean`

This module assembles initial base, primary, temporal, ranked, and initial states. It proves nonzero angular modes, phase/cutoff identities, smoothness and periodicity, Gaussian mean-zero facts, covariance regularity and bounds, matched fluxes, and `PrimaryData`, `initial_bounds`, `initial_cumulative_bounds`, `initial_mean_bounds`, `initial_debt_bounds`, and `initial_zeroMasses`.

These are concrete initial-stage physical-data and rank/mean results. They are below the final selected whole-space endpoint and do not prove global five-observable transport.

### `NavierStokes/HarmonicSourceSupport.lean`

This module imports periodised wave bounds and formalises coefficient support, support under differentiation, angular operations, Laplacians, transport, gradients, nonlinear residuals, real projections, native unions, and source-family coverage. It proves residual source support, complement germs and jets, supported sums/products, native support of coefficients and block velocities, and zero unlocalised-wave error under its hypotheses.

This is genuine harmonic/source localisation and support infrastructure. It establishes support/germ statements, not the radial integral identities of the final selected Cartesian velocity or pressure.

### `NavierStokes/HarmonicFields.lean`

This module defines finitely supported harmonic coefficient algebra, characters, evaluation, fields, angular means, convolution, conjugate symmetry, band limitation, quadratic iteration/envelopes, waves, derivative coefficients, angular differentiation, and the associated support and regularity identities.

It provides the analytic harmonic representation layer and angular-mean calculus. No declaration inspected here identifies the public selected field with the five paper observables or an absolute whole-space pressure representative.

### `NavierStokes/ActualExteriorPrefix.lean`

This module imports actual cycle residual bounds, mixed diagonal residuals, tail gauge potential, and physical curl covariance. It defines an exterior domain and `ExteriorStages`, then proves potential/direct/pressure prefix agreement and germs, velocity prefix agreement, and exterior prefix/germ results.

This is positive exterior matching and prefix-localisation evidence. It does not provide the global selected-field moment evaluation after the infinite assembled endpoint.

### `NavierStokes/ActualParticularMeanGain.lean`

This module defines input/result propositions for a particular mean update and proves a covariance class from the lower bound on the parameter, moving-field covariance, and the post-particular gain result.

This is a local cycle-level covariance gain. It is not a theorem about the final Cartesian `Witness` or global radial moment tuple.

### `NavierStokes/ActualSignedFamilySupport.lean`

This module imports positive-time signed data and defines potential and pressure copy families. It proves their support, smoothness, and source-domain properties.

This is concrete signed-family support and regularity evidence. It does not by itself prove pressure Poisson semantics, five-observable transport, or endpoint packaging.

## Classification

| Module | Classification | Final selected observable transport? | Contradiction? |
|---|---|---:|---:|
| `ModulatedHistories.lean` | Positive reduced history/repair identities | No | No |
| `ActualInitialMean.lean` | Positive initial mean/covariance/rank data | No | No |
| `HarmonicSourceSupport.lean` | Positive harmonic residual support/germ layer | No | No |
| `HarmonicFields.lean` | Positive finite harmonic calculus and angular means | No | No |
| `ActualExteriorPrefix.lean` | Positive exterior prefix and germ agreement | No | No |
| `ActualParticularMeanGain.lean` | Positive local covariance-gain result | No | No |
| `ActualSignedFamilySupport.lean` | Positive signed potential/pressure support layer | No | No |

## Controlled conclusion

Priority 94 adds real local and reduced construction evidence. It does not close the composition from reduced moments and histories through the assembled Cartesian field into `Witness`, and it does not establish a nonzero moment defect, impossibility theorem, or kernel `False`.

Evidence is registered in `semantic_coverage_register.py` and regenerated into the authoritative JSON/Markdown/HTML register and public mirrors.
