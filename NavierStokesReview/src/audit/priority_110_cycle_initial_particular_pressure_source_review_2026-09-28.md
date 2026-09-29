# Priority 110 source review: cycle coherence, initial construction, particular-cycle data, and corrected pressure

Date: 2026-09-28
Scope: direct reading of the four reachable Priority 110 source files, not a filename-only scan.
Classification: intermediate correspondence evidence; no endpoint refutation is inferred.

## Executive result

This tranche contains substantial value-level construction and transport:

- `ActualCycleCoherence.lean` defines and iterates a three-part coherence proposition for state, wave blocks, and axisymmetric aliases. It proves support-based zero identities, particular-source identities, wave transport, and coherent cycle iteration.
- `ActualInitialCoherence.lean` constructs the initial seed, primary, temporal, ranked, and initialized states. It proves band coordinate identities, primitive reconstruction, smoothness, support, periodicity, and finite block assembly.
- `ActualParticularCycleData.lean` converts a coherent cycle state into native particular-cycle data and proves source, pressure, Gaussian, residual, smoothness, support, periodicity, coefficient, covariance, solenoidal, and cancellation properties.
- `CorrectedPressureBounds.lean` constructs a corrected reduced pressure from a finite partial reset and proves before/after matching, joint smoothness, derivative and size bounds, and an axis-pressure decomposition.

These results narrow the audit boundary. They do not expose a theorem evaluating the final selected whole-space field through `barMoment`, nor an equality with the paper tuple `(M,I,J,S,C_p)`. They also do not establish an absolute whole-space pressure-Poisson representative. No nonzero defect, impossibility theorem, or `False` classification is justified by this tranche.

## Direct source findings

### 1. `ActualCycleCoherence.lean`

Imports at lines 1-9 connect mean physical data, cycle parameters, correction steps, reference rebasing, core support, wave regularity, signed coherence, signed Gaussian coherence, and particular coherence.

The exported coherence boundary is explicit:

- `StateCoherent` is defined at lines 36-40.
- `BlocksCoherent` is defined at lines 43-47.
- `AxisCoherent` is defined at lines 50-53.
- `structure Coherent` at lines 56-60 contains exactly `state`, `blocks`, and `axis`.

The file then proves initial coherence (lines 73-87), reindexing and particular/reference projections (lines 90-116), support-induced zero fields (lines 120-184), the particular source definition and equality (lines 187-203), carrier ordering and positive radius (lines 205-225), wave-on identities (lines 227-250), and particular field/pressure identities (lines 253-304).

The iterative part is substantive: source smoothness and support hypotheses occur at lines 321-454; covariance, rank geometry, stage primitives, pressure, signed-cycle wave, and particular-wave results occur at lines 455-680; coherent iteration is packaged at lines 681-735 and the indexed state at lines 786-861. This is a real cycle-coherence bridge. It is not a final radial observable bridge: direct declaration search in this file finds no `barMoment`, `FiveRows`, `PositiveOrderMoments`, `FiveProfileMoments`, or `(M,I,J,S,C_p)` endpoint theorem.

### 2. `ActualInitialCoherence.lean`

Imports at lines 1-6 connect primary coherence/covariance, base residuals, mean-stage regularity, wave-state regularity, and rank-state coherence.

The state construction at lines 27-51 is layered as `pieces`, `baseError`, `seed`, `primary`, `temporal`, `ranked`, and `initialized`. Coordinate and band identities are proved at lines 53-250. Primitive reconstruction and rank/debt regularity are proved at lines 266-325, including the `DebtRegular` property at line 315.

The seed-regularity and actual-seed sections (lines 417-653) prove smoothness, support, covariance regularity, finite block representation, periodicity, and primitive/band facts. The final-state section (lines 700-752) proves the corresponding initialized primitives, aliases, overlap openness, and overlap band identities.

This establishes a genuine initial-state and band-transport layer. The visible debt occurrence is a regularity interface, not the paper's five cumulative radial tuple, and no final Cartesian `barMoment` transport appears in the file.

### 3. `ActualParticularCycleData.lean`

Imports at lines 1-6 connect cycle assembly, particular mean gain, cycle coherence, periodicity, dynamics, and Gaussian data.

The `Data` proposition at lines 34-72 packages uniform wave/pressure bounds, smooth coefficient fields, angular smoothness, pressure-field smoothness, periodicity, support, and a residual-field property. `nativeData` is defined at lines 102-108, with carrier preservation and input-support transport at lines 110-119.

The native source/pressure boundary identities and residual transport appear at lines 133-286. Native source, raw, pressure, Gaussian, and corrected classes and smoothness are proved at lines 286-356. Periodicity, native modes, finite block regularity, and assembled velocity/pressure coefficient smoothness occur at lines 370-563.

The output section constructs `goodBlock` and proves amplitude, pressure, Gaussian, solenoidal, carrier, cancellation, and linear bounds at lines 573-731. The pressure-assembly section proves particular pressure equality to modes, smoothness, and `actual_data`/`actual_inputs` at lines 731-814.

This is an important selected-stage data handoff. It still terminates in local stage/coefficient/cancellation properties. It does not calculate the global selected field's five radial observables or prove their equality with the reduced profile certificate.

### 4. `CorrectedPressureBounds.lean`

Imports at lines 1-2 are `FuturePressureBounds` and `TransportPrimitive`; lines 5-8 describe the corrected pressure as an improper/finite partial-reset integral.

The reduced objects `correctedPi`, `editDensity`, `releaseSquare`, and `editSize` are defined at lines 23-36. The file proves coefficient, square, smoothness, zero-outside, joint-continuity, and integral identities at lines 39-235. The before/after/partial matching results are at lines 236-280:

\[
\texttt{correctedPi} = \texttt{Pi} + \frac12\int \texttt{editDensity}.
\]

The pressure change is zero before the reset and after the flattening interval (lines 283-298), and joint smoothness/derivative results appear at lines 301-426. Bounds and endpoint estimates are proved at lines 434-671. The final identity at lines 672-681 is explicitly an axis-pressure decomposition, `axisPressure +` a finite correction integral.

This is positive reduced pressure-correction evidence. It is not an absolute global pressure-Poisson theorem and does not connect to the selected Cartesian `Witness` or to `(M,I,J,S,C_p)`.

## Cross-module audit conclusion

| Layer | What this tranche establishes | What remains unproved |
|---|---|---|
| Initial state | Seed-to-initialized state, bands, support, periodicity, primitives | Final selected-field observable identity |
| Cycle coherence | State/block/axis coherence and iterative transport | Global five-observable transport |
| Particular data | Native source, pressure, Gaussian, residual, smoothness, support, coefficients, solenoidality | `barMoment` evaluation after all sums/localisation/periodisation |
| Corrected pressure | Reduced finite-reset pressure matching and bounds | Absolute whole-space pressure semantics |

The correct status is therefore **evidence inspected, intermediate bridges present, final selected-field correspondence still open**. This tranche strengthens the construction record; it neither proves nor disproves `Delta m != 0`.

