# Priority 3-6 source review: cycle parameters, means, torus inversion, and target bounds

Date: 2026-09-27
Scope: ten directly inspected reachable source modules in `NavierStokes/`.
Method: read the import headers, definitions, theorem statements, and proof-facing declarations at the cited ranges. This report records what the source actually establishes. It does not infer endpoint transport from imports or names.

## Executive result

This tranche strengthens the positive audit record. The source contains real
cycle parameter identities, covariance reconstruction, harmonic mean updates,
off-axis similarity-coordinate calculus, signed cross-stress formulas, Volterra
parity, support and germ factorisation, smooth torus Fourier inversion, radial
profile-history bounds, repair rows, and target-cone estimates.

The most important new load-bearing fact is in
`ActualSignedMeanBinding.lean`: `requested_cross_factor` identifies the actual
averaged cross term with a physical requested stress multiplied by an explicit
partition factor, `requested_cross_tail` proves exact equality on the prepared
tail, and `requested_cross_defect` retains the earlier-band missing-weight
remainder. The corresponding family theorem explicitly says its inputs are
ordinary residual/coefficient estimates and do not assume the cross defect
vanishes (`ActualSignedMeanBinding.lean:461-505, 669-695`).

This is a genuine intermediate defect/cancellation structure. It is not yet a
calculation of the final selected Cartesian field's five paper observables and
does not prove a nonzero selected-field remainder or `False`.

## Module findings

### 1. `ActualCycleParameters.lean`

- The header states that the module constructs the current cycle parameters
  from the initialized labels and proves data identities, while explicitly
  stating that it does not assume or assert analytic preservation of a
  correction cycle (`ActualCycleParameters.lean:5-18`).
- The declarations reindex coefficient/state families, establish round trips,
  index and band bounds, and identify the particular source and signed request
  (`:29-116, :124-182, :219-339`).
- Later declarations establish carrier identities for signed, tangent,
  particular, and Gaussian components and define fixed parameters
  (`:351-508`).
- No final Cartesian field, radial observable, `barMoment`, `FiveRows`, or
  `(M,I,J,S,C_p)` equality is defined here.

Classification: real cycle bookkeeping and carrier identity; no endpoint
moment transport.

### 2. `FlatCovariance.lean`

- Defines the edge-scaled matrix, target, inverse coefficients, primary
  amplitude, and signed amplitude (`FlatCovariance.lean:28-51`).
- Proves exact reconstruction of the target, including the edge-zero branch,
  and strict positivity under the cone hypotheses (`:195-255`).
- Proves smoothness and flat weighted derivatives across the edge, including
  the squared-factor convention (`:266-404, :432-551`).

Classification: explicit covariance solve and regularity. It has no radial
moment observable and no selected-field packaging theorem.

### 3. `HarmonicMeanInteraction.lean`

- Defines the mean cross coefficient and the updated residual block
  (`HarmonicMeanInteraction.lean:119-169`).
- Proves that updating the mean changes the harmonic residual coefficients by
  the explicitly defined cross term while the wave and pressure data remain
  separate (`:175-215`).
- Proves wave-class, band-limit, conjugacy, and zero-mode properties for the
  residual difference block (`:245-341, :352-432, :441-582`).
- The module's output is a harmonic residual block and its bounds; no global
  five-observable radial equality is present.

Classification: genuine mean-to-residual interaction; intermediate residual
transport, not endpoint moment transport.

### 4. `SimilarityCoordinates.lean`

- Defines the scalar forward map, unique positive inverse coordinate, slope,
  and triangular coordinate map (`SimilarityCoordinates.lean:22-232`).
- Proves smoothness and derivative identities only on the positive-time/radius
  domain, with hypotheses such as `p.1 > 0` and `t < 1` (`:195-294, :390-455`).
- Defines the rescaled coordinate `coordinateX` and proves its time and spatial
  derivatives under those domain conditions (`:500-559`).

Classification: source-grounded off-axis similarity calculus. It documents a
domain boundary but does not transport a global radial moment tuple.

### 5. `ActualSignedMeanBinding.lean`

- Defines the concrete signed cross tensor from the actual primary and signed
  fields (`ActualSignedMeanBinding.lean:341-344`).
- Proves the averaged cross sum and the exact finite-label reconstruction
  (`:381-438`).
- Proves the physical partition-factor identity
  `meanBar(actualCross) = partitionFactor * requestedStress`
  (`:440-460`).
- Proves exact tail cancellation once the physical scale reaches the prepared
  tail (`:461-471`).
- Proves an explicit earlier-band defect with the missing partition weight
  (`:473-485`), then derives angular and axial tail identities and their jets
  (`:487-516`).
- Transfers those identities through cycle and family assemblies
  (`:578-667`). The all-exponents theorem consumes ordinary residual/coefficient
  and mean-class hypotheses and explicitly does not assume the cross defect or
  its vanishing (`:669-695`).

Classification: strongest result in this tranche. It confirms that an
intermediate finite-head defect is represented algebraically and that exact
tail cancellation is conditional. It still does not evaluate the final
`selected_witness` Cartesian field against `(M,I,J,S,C_p)`.

### 6. `VolterraParity.lean`

- Defines coefficient/forcing parity, reflection, gluing, and the symmetric
  integral solution (`VolterraParity.lean:22-214, :383-444`).
- Proves that the parity action commutes with the radial inverse and integral
  solution and derives symmetric-solution parity (`:454-661`).
- The integral operator is a finite radial Volterra construction. No theorem
  here connects its parity to a whole-space Cartesian radial observable.

Classification: genuine axis/parity regularity; no endpoint moment theorem.

### 7. `ActualCycleAssembly.lean`

- Proves support, cutoff-source, zero-mode, zero-germ, Gaussian-germ, and
  curl-input-support properties for the actual signed blocks
  (`ActualCycleAssembly.lean:40-321, :354-547`).
- Proves source/copy factorisation and canonical support/germ identities
  (`:610-839`).
- Builds the refined cycle family and final finite assembly, then proves labels,
  primary/tangent identities, and support (`:896-955, :1019-1134`).
- No `barMoment`, `FiveRows`, or selected whole-space five-observable equality
  is exported by this assembly module.

Classification: concrete support and local assembly; no final observable
transport.

### 8. `TorusInverse.lean`

- Defines rapid Fourier coefficients, torus modes, smooth series, derivatives,
  directional inverse, and coefficient multipliers
  (`TorusInverse.lean:21-186, :195-301`).
- Proves smoothness of the infinite series and interchange of differentiation
  with summation (`:106-186, :307-333`).
- Descends the series to the two-dimensional torus and proves the actual Haar
  integral formula: the torus integral extracts the zero Fourier coefficient
  (`:335-420`).
- Proves inverse bounds, zero-mean inverse conditions, and periodicity
  (`:424-439, :503-586`).

Classification: substantive Fourier/torus mean machinery. It supplies an
analytic tool that could participate in a transport proof, but no theorem here
maps the final Cartesian `tsum` field to the paper's five radial observables.

### 9. `ModulatedCone.lean`

- Indexes the five profile-history rows as mass, angular, transport, energy,
  and pressure (`ModulatedCone.lean:623-637`).
- Proves uniform `C/n` localization and history-difference estimates, retaining
  the pressure constant exactly (`:639-730`).
- Constructs the localized profile family and the physical repair, preserving
  radial germs outside the repair patch (`:966-1016`).
- Defines the five-row derivative vector and proves first-jet bounds and
  unchanged exterior shears (`:1018-1080`).

Classification: real five-row profile-history and repair machinery. Its
observables remain profile-level and are not identified with the final selected
Cartesian field.

### 10. `PrimaryTargetBounds.lean`

- Defines the primary covariance model, target directions, pulse ratios, and
  strict-cone quantities (`PrimaryTargetBounds.lean:27-229`).
- Proves compact model-data bounds, covariance reconstruction, target direction
  identities, and positive target amplitudes (`:457-485, :590-631, :802-917`).
- Proves actual/restricted/constructed covariance bounds for the chosen target
  and profile family (`:960-1035`).
- No field-level radial integral or endpoint five-observable equality occurs.

Classification: explicit primary covariance and cone-margin estimates; no
selected-field moment transport.

## Cross-layer disposition

| Question | Finding from this tranche |
|---|---|
| Are the upstream cycle, covariance, Fourier, parity, repair, and stress objects real? | Yes, with direct source declarations and proofs. |
| Is there an intermediate cross defect? | Yes. `requested_cross_defect` retains an explicit missing-weight term on earlier bands. |
| Is tail cancellation proved? | Yes, under the stated prepared-tail hypothesis. |
| Does that prove the final selected Cartesian field has nonzero `Delta m`? | No. |
| Does any reviewed file prove `False`? | No. |
| Does this tranche add the selected `(M,I,J,S,C_p)` transport theorem? | No. |

## Controlled conclusion

The source record is stronger and more nuanced than a generic “missing bridge”
statement: some intermediate defects are explicit, and some tail cancellations
are exact under hypotheses. The remaining audit task is to trace whether those
intermediate identities are actually composed with the final selected
`tsum`/curl/localisation/periodisation field and its exported `Witness`. Until
that value-level composition is found or contradicted, the status remains
`CTR-005: not established as endpoint paper-to-code correspondence`, not
`Delta m != 0` and not `False`.
