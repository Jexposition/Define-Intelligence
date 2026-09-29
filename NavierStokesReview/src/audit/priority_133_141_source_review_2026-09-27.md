# Priority 133-141 source review: signed profiles, covariance, waves, and prefix fields

Date: 2026-09-27
Scope: ten directly inspected reachable source modules selected from the
authoritative semantic register.
Method: source-first review of definitions and theorem statements at the cited
ranges. No build or axiom result is inferred from source reading alone.

## Executive result

This tranche confirms substantial implementation of the selected signed
profile family, covariance and scale identities, particular-wave envelopes,
periodic Navier--Stokes comparison, actual cycle periodicity, and finite-prefix
Cartesian/polar field agreement. In particular, `ActualPhysicalPrefixFields`
contains a real `StageRealizations` record and derives `PhysicalData` for the
same literal finite prefix.

The same source also makes the remaining boundary explicit: the prefix record
contains stage agreement and regularity fields, while `physicalFields_all`
feeds finite-prefix fields into downstream residual-rate consumers. The
inspected declarations do not state or prove that the final selected
whole-space `tsum` field has the paper tuple `(M,I,J,S,C_p)`. No concrete
selected-field `Delta m != 0`, impossibility theorem, or kernel-level `False`
is established here.

## Module findings

### `ActualSignedNativeProfiles.lean`

Defines active native label regions, signed profile pairs, profile domains,
polynomial jets, native profile families, and support/closure coverage
(`ActualSignedNativeProfiles.lean:31-63, :100-184, :206-251`). The module
provides genuine prepared-region profile and jet data. It does not export a
final Cartesian radial-moment tuple.

### `ActualPrimaryCovariance.lean`

Proves common-cover and wave transport identities, pair covariance, active
label support, native-point geometry, scale and mask properties, tangent sums,
partition factors, missing-weight decomposition, and mean-class bounds
(`ActualPrimaryCovariance.lean:26-115, :128-204, :352-384, :632-856`). These
are real covariance/coverage results. The `averagedDefect` and
`missingWeight` objects remain intermediate mean/covariance quantities; the
inspected declarations do not identify them with the final selected
five-observable radial field.

### `ActualCurrentParticularBounds.lean`

Builds literal current particular-wave potential and pressure coefficients from
actual current state data and proves local/common source, envelope, and native
control bounds (`ActualCurrentParticularBounds.lean:39-130, :141-244`). The
module is an actual coefficient/rate layer, not a radial-moment transport
theorem.

### `ActualSignedNativeBounds.lean`

Defines native potential/pressure sources, label selection, inactive-label
zero results, source identification, and uniform/native/source bounds
(`ActualSignedNativeBounds.lean:35-128, :152-205, :426-480, :566-704`). It
does use concrete signed physical data and `GaugeMomentBalances.MovingField`
as an upstream hypothesis, but the exported results are source and jet bounds;
no final `(M,I,J,S,C_p)` equality is present.

### `ActualSignedPhysicalCoherence.lean`

Proves finite-support/finsum reindexing, active physical index selection,
potential/pressure term and sum labels, native chart identities, reference
cutoff formulas, canonical potential/pressure values, current zero behaviour,
and measured potential/pressure equality to finite physical sums
(`ActualSignedPhysicalCoherence.lean:39-161, :167-342, :437-575,
:608-761, :768-831`). This is important concrete coherence evidence for the
signed physical family. It still does not compose the final selected Cartesian
field with `barMoment` or the paper's five cumulative observables.

### `ParticularWaveBounds.lean`

Provides actual forced/copy/modal wave envelope jets, copy-solve pressure
cancellation, pressure and velocity regularity, exact curl/divergence
realisation, support after curl, and constructed particular-wave residual
classes (`ParticularWaveBounds.lean:35-461, :657-810, :846-945,
:1932-2110, :2172-2217`). These are substantive wave and residual bounds.
They control local construction before final endpoint packaging and do not
evaluate selected global radial moments.

### `PeriodicUniqueness.lean`

Derives the periodic difference equation, periodic integration-by-parts energy
identities, pressure cancellation, Gronwall zero, and classical uniqueness on
closed preterminal intervals (`PeriodicUniqueness.lean:110-154, :316-441,
:470-616, :638-705`). This is a real same-force periodic comparison theorem.
It is not a five-moment transport result and does not independently establish
absolute pressure semantics for the selected witness.

### `ActualCyclePeriodicity.lean`

Tracks coefficient translation, angular periodicity, finite-prefix agreement,
valid chart domains, pressure periodicity, and stage-realisation fields
(`ActualCyclePeriodicity.lean:34-195, :204-338, :342-483`). Its
`StageRealizations` structure records potential/direct/pressure agreement on
concrete chart domains, and the derived `physicalFields_of_stages`/`physicalFields_all`
construct finite-prefix `PhysicalData`. The type contains no five-observable
endpoint equality.

### `ActualParticularStageControls.lean`

Reindexes the selected phase/frame, constructs reference/native/background
particular data, proves common phase bounds, clock-envelope transport, and
active label/parameter control (`ActualParticularStageControls.lean:31-167,
:209-338, :342-560`). These are genuine selected particular-stage controls
and parameter transport identities. They are upstream of final global
packaging and do not state selected-field radial moment preservation.

### `ActualPhysicalPrefixFields.lean`

Defines source and Cartesian chart domains, proves chart existence and source
sublevel control, and defines `StageRealizations` with explicit finite-stage
potential/direct/pressure agreement. Its `velocity_prefix`, `pressure_prefix`,
`velocity_germ`, and `pressure_germ` connect the finite Cartesian prefix to
the cylindrical physical fields; `physicalFields_of_stages` and
`physicalFields_all` derive the corresponding `PhysicalData`
(`ActualPhysicalPrefixFields.lean:240-320, :327-386, :438-499`). This is a
load-bearing finite-prefix bridge, but it is not the final selected infinite
sum and contains no theorem of the form
`moments(selected_field) = (M,I,J,S,C_p)`.

## Cross-layer disposition

| Question | Source-grounded answer |
|---|---|
| Is the signed profile/covariance/wave infrastructure substantive? | Yes. The inspected declarations construct actual objects and prove local, periodic, support, covariance, regularity, and residual identities. |
| Is there a genuine finite-prefix Cartesian/polar bridge? | Yes. `ActualPhysicalPrefixFields` supplies explicit stage-agreement and germ theorems and derives `PhysicalData` for the same literal prefix. |
| Does this tranche prove final selected-field five-observable transport? | No. |
| Does it prove a concrete selected-field `Delta m != 0`? | No. |
| Does it prove impossibility or kernel-level `False`? | No. |

## Controlled conclusion

The correct update is not “the profile machinery is absent”. It is that the
repository contains substantial selected intermediate mathematics and a real
finite-prefix field bridge, while the final selected whole-space composition
to `(M,I,J,S,C_p)` remains unestablished in the inspected declarations.
