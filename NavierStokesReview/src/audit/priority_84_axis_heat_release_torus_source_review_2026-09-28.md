# Priority 84 source review: axis, heat, release, and torus-average modules

Date: 2026-09-28
Scope: direct source inspection of six reachable `NavierStokes` modules.
Purpose: classify the actual mathematical bridges before updating the semantic coverage register.

## Executive result

This tranche adds positive evidence, not a refutation. The inspected modules contain exact reduced radial, heat, pulse-release, axis-regularity, periodisation, Jacobian, and angular-average theorems. They therefore rule out the broad claim that the repository has no moment mathematics or no averaging infrastructure.

The remaining correspondence question is narrower and still open: the inspected declarations do not state the complete composition

`reduced profile moments -> Cartesian potential/curl field -> localisation -> tsum -> periodisation -> final selected field -> paper five-observable tuple`.

Accordingly, this tranche does not establish `Delta m != 0`, impossibility, or `False`. It records exact intermediate bridges and the boundary at which a final selected-field transport theorem would still have to be found or proved.

## Source findings

### `PositiveAxisExistence.lean`

The module imports the actual Volterra and positive-axis systems. It states that the six-component convergent construction connects to an explicit positive-order system and proves squared-radius smoothness, parity, axis vanishing, and axis jets. The real-compatible six-profile system is constructed in the later declarations.

Relevant source regions:

- lines 1-13: imports and module scope;
- lines 435-488: `xProfile_smooth`, parity, axis value and axis-jet results;
- lines 543-661: real coefficients/profiles and compatible positive-system witnesses.

Classification: genuine reduced axis/profile existence and regularity; no final selected Cartesian five-observable export found in this module.

### `PulseLag.lean`

The module defines the actual exponential kernel, convolution, and lag. It proves kernel positivity, differentiability, two integration-by-parts expansions, exact affine-lag identities, lag ODE/derivative identities, and quantitative remainder/reset estimates.

Relevant source regions:

- lines 1-14: actual pulse-lag construction;
- lines 16-120: kernel, convolution, and integration-by-parts infrastructure;
- lines 140-260: lag identities, derivative equations, and tail regimes;
- lines 289-395: normalised lag, power weight, integrability, and radial-history consequences.

Classification: concrete pulse/lag mechanism with moment-relevant reduced identities; no public `Witness` transport.

### `RadialHeatProfile.lean`

The module defines radial heat profiles and moment integrals. Its `moment_ode` theorem gives an exact improper integration-by-parts identity, while the profile-jet and half-line theorems derive the corresponding radial ODEs and endpoint forms.

Relevant source regions:

- lines 300-345: `moment_ode` and boundary-term control;
- lines 384-455: profile-jet ODE and strict slope estimates;
- lines 600-650: half-line/endpoint radial heat identities;
- lines 700-730: scaled/forward radial heat-equation relations.

Classification: exact reduced radial PDE mathematics; no final Cartesian/cutoff/series/endpoint transport theorem found here.

### `ReleaseMoments.lean`

The module constructs a corrected angular release history. It proves smoothness, release and hold regimes, tail behaviour, renormalised radial integrability, and exact cancellation of the renormalised angular moment. `complete_release_moments` packages the scheduled reduced correction together with eventual history identities.

Relevant source regions:

- lines 23-132: corrected/release weights and history regularity;
- lines 140-225: moment candidate, derivative, release, and hold identities;
- lines 247-332: tail, normalised-lag, and eventual-zero results;
- lines 340-395: power weights and renormalised-log integrability;
- lines 408-529: radial history, integrability, and exact renormalised angular moment;
- lines 531-540: `complete_release_moments`.

Classification: strong positive reduced-moment bridge; not the complete five-observable selected-field bridge.

### `RenormalizedHeatMoment.lean`

This module is a substantial positive result. It proves renormalised heat/profile moment integrability, physical scaling, differentiation and support controls, axial viscosity moment cancellation, and a heated nominal axial-viscosity zero theorem under explicit compensation hypotheses. It also identifies the reduced `X`-moment through the squared-radius change of variables.

Relevant source regions:

- lines 109-182: renormalised moment definition, support, differentiation, and axial cancellation;
- lines 274-347: heat-carrier scaling and profile-moment scaling;
- lines 367-496: axis/infinity integrability and physical axial-viscosity cancellation;
- lines 518-627: `X`-integral, `xMoment`, and exact zero conditions;
- lines 699-788: outgoing/heated identities and `heated_nominal_axial_viscosity`.

Classification: concrete reduced/physical radial moment evidence; no final Cartesian curl/localisation/`tsum`/periodisation composition to `Witness` found here.

### `TorusAverages.lean`

This module supplies real averaging infrastructure. It defines the covering matrix, torus map, square average, lattice periodisation, native linear charts, determinant/Jacobian factors, transverse stretching, product-profile factorisation, pulse-column averages, and angular cosine covariance.

Relevant source regions:

- lines 36-138: torus covering and square-average identities;
- lines 140-207: lattice/fundamental-domain facts;
- lines 228-411: periodisation, integrals, and covering invariance;
- lines 419-555: native charts, determinant factors, and transverse scaling;
- lines 570-679: product separation, pulse columns, and angular covariance.

Classification: genuine torus/coordinate-average machinery. These theorems show that averaging is formalised in meaningful cases, but they do not state that the final selected Cartesian field has the paper's complete tuple `(M,I,J,S,C_p)`.

## Correspondence boundary

The evidence now supports the following calibrated map:

```text
Reduced axis/heat/release moments       [proved in this tranche]
        |\
        |  radial changes of variables, pulse schedules,
        |  torus/Jacobian/average components
        v
Intermediate physical/profile fields    [proved in several modules]
        |
        |  unresolved full composition: curl + localisation + tsum
        |  + periodisation + selected endpoint observable tuple
        v
Public selected Cartesian Witness        [transport theorem not located here]
```

The presence of exact intermediate identities is evidence against an “all moment code is dead” narrative. It does not discharge the selected-path correspondence obligation. Conversely, no nonzero defect follows merely from the absence of a theorem in these six files: cancellation may still be proved elsewhere or may require a new value-level calculation.

## Register action

The six modules are entered as `evidence_inspected` in the semantic coverage register. The source register remains the authority for the exact row status and reachable-module counts; generated JSON, Markdown, and HTML mirrors must be regenerated after this report is added.

## Verdict for this tranche

`CTR-005`: remains **not established at the selected-field correspondence boundary**, with stronger positive intermediate evidence.
`Delta m != 0`: **not demonstrated**.
Kernel-level `False`: **not demonstrated**.
