# Priority 135-139 source review: terminal, periodised, harmonic, and pulse layers

Date: 2026-09-27
Review mode: direct source inspection of the current `NavierStokes/` tree.
Scope: ten reachable modules selected from the open semantic-coverage queue.

This report records what the source actually proves.  Import reachability,
local mathematical identities, and endpoint semantic transport are kept as
separate claims.

## Files reviewed

### `NavierStokes/RadialSchedule.lean`

- `147-160`: `two_moment_reset` proves an exact two-parameter radial reset.
- `177-218`: pulse-energy debt and the scalar release equation are bounded and
  solved under explicit hypotheses.
- Finding: this is a genuine reduced schedule/profile mechanism.  It is not a
  theorem identifying the final Cartesian field with
  \((M,I,J,S,C_p)\).

### `NavierStokes/PressureStream.lean`

- `121-185`: defines `pressureMass`, its interval representation, smoothness,
  and `pressureSource_mass_zero`.
- `596-707`, `800-813`: derives periodic and weighted-source consequences.
- Finding: this is real torus-averaged pressure normalisation.  It is not an
  absolute whole-space Poisson representation for the exported candidate and
  is not the final five-observable transport theorem.

### `NavierStokes/TerminalEdgeFactor.lean`

- `158-239`: proves the edge-coordinate derivative and improper-FTC identity
  for `radialFlatDensity`.
- `394-429`, `588-603`: evaluates time/correction and scalar flat-density
  integrals.
- `643-690`, `980-1072`: constructs smooth pressure/axial coefficients and
  primitive factorisations.
- Finding: terminal edge radial integrals and pressure factors are explicitly
  formalised.  They remain reduced edge calculations, not a selected-field
  whole-space moment evaluation.

### `NavierStokes/ActualPeriodizedSignedRealization.lean`

- `46-145`: proves finite native support, `tsum` collapse, and smooth masked
  sums.
- `261-374`: defines common/native masks and proves coefficient transport.
- `480-519`: defines physical potential, velocity, and pressure; `physicalVelocity`
  is explicitly a spatial curl and `actual_wave_physical` transports the local
  wave value through the chart.
- Finding: this is substantive periodised Cartesian/cylindrical assembly.  No
  `barMoment` or \((M,I,J,S,C_p)\) equality for the final selected field is
  present in the inspected declarations.

### `NavierStokes/ActualSignedPhysicalBinding.lean`

- `103-220`: constructs actual selected primary data and proves domain,
  phase, and radial transport facts.
- `602-773`: proves reference/common amplitude, pressure, cutoff, `tsum`, and
  curl-potential equalities.
- `785-808`: binds the post-particular cycle state.
- Finding: exact local binding across native/reference/common periodisation is
  proved.  The five radial paper observables are not transported to the
  endpoint here.

### `NavierStokes/ParticularWaveAssembly.lean`

- `79-183`, `268-323`: constructs signed harmonic blocks and proves
  reconstruction and mean-zero identities.
- `619-659`: propagates invariants through complex copies and `tsum`.
- `802-854`: proves native-copy uniqueness, weighted single-copy reduction,
  and germ transport.
- `1565-1617`: proves exact local curl, divergence, germ, and cancellation
  identities.
- Finding: the mode/block and local residual mechanisms are real and
  non-vacuous.  They do not compute the final Cartesian radial five-moment
  tuple.

### `NavierStokes/ActualCurrentParticularPhysical.lean`

- `31-122`, `135-335`: defines current particular potentials/pressures and
  proves full-turn periodic chart identities.
- `347-463`: proves native and local smoothness on the valid domain.
- `620-706`: proves the native curl identity, including radial faces and the
  invariant boundary condition.
- `778-887`: proves cylindrical-to-Cartesian local curl transport and its
  invariant specialisation.
- Finding: this is strong local field realisation.  It is not the global
  selected-field moment bridge.

### `NavierStokes/HarmonicResidual.lean`

- `1006-1195`: defines residual coefficients and proves field, band,
  conjugacy, and extraction identities.
- `1438-1604`: defines the grouped residual block, proves zero mode, smoothness,
  mean-zero, and full residual reconstruction.
- Finding: exact harmonic residual algebra is present.  No declaration here
  identifies the selected Cartesian field with \((M,I,J,S,C_p)\).

### `NavierStokes/PhysicalMeanJetBounds.lean`

- `782-812`: proves spatial-curl jet bounds and smoothness for the coherent
  angular field.
- `838-870`: proves fibre-local pressure/stream coherence and reconstructs
  pressure from the coherent source.
- Finding: this supplies local regularity and pressure operators.  It does not
  export a selected-field radial five-moment equality.

### `NavierStokes/PulseCone.lean`

- `1039-1074`: proves the actual pulse mass expansion.
- `1094-1192`: proves quantified cone margins and error-budget bounds.
- `1194-1223`: proves the axial-history error bound from actual profile data.
- Finding: the reduced pulse and energy mechanism is substantive.  It is not a
  calculation of the assembled Cartesian `tsum` field against the five paper
  observables.

## Cross-layer result

This tranche strengthens the positive side of the audit: the source contains
real profile, pressure, harmonic, periodisation, curl, and residual identities.
It also narrows the unresolved boundary.  The reviewed modules prove local or
intermediate identities, but no reviewed declaration composes

\[
\text{profile moments}
\to \text{Cartesian curl}
\to \text{localisation/periodisation}
\to \texttt{tsum}
\to \text{final selected field}
\to \text{barMoment}(M,I,J,S,C_p).
\]

Therefore this tranche supports **CTR-005: endpoint correspondence not yet
established**.  It does not prove a non-zero selected-field defect
\(\Delta m\ne0\), an impossibility theorem, or `False`.  The numerical
`cutoff_commutator_scan.py` remains a declared-profile diagnostic and is not
substituted for a theorem about `selected_witness`.

## Register action

The ten files are recorded as `evidence_inspected` in
`semantic_coverage_register_full_2026-09-27.{json,md,html}`.  The full source
closure remains open after this tranche; the route-only historical register is
not overwritten.
