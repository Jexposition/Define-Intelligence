# Priority 133-134 source review: current curl, endpoint inputs, and periodic limits

Date: 2026-09-27
Scope: ten directly inspected reachable source modules selected from the
authoritative semantic register.
Method: source-first review of definitions and theorem statements at the cited
ranges. No build or axiom result is inferred from source reading alone.

## Executive result

This tranche reaches closer to endpoint assembly. It contains finite label and
harmonic jet bounds, an actual current-band Cartesian curl theorem, initial
native regularity, localised/periodic residual-limit constructions, finite
particular assembly, endpoint input packaging, current-band potential
coherence, and seed periodicity.

The strongest positive result is `CurrentSignedCurl.currentPotential_curl`
and its finite-sum variants: they prove the current-band potential has the
expected physical curl on valid charts. The strongest boundary result is in
`ActualEndpointInputs`: endpoint inputs are explicit packages for the finite
stage construction and are consumed before the generic rate layer. Neither
result is a theorem transporting the final selected whole-space field to
`(M,I,J,S,C_p)`. No concrete selected-field `Delta m != 0`, impossibility
theorem, or kernel-level `False` is recorded.

## Module findings

### `CurrentParticularLabelBounds.lean`

Defines the signed-label/window/chart map, proves refined support inclusion,
finite harmonic mode counts, local potential/pressure jet bounds, and
smoothness/axis-zero-germ statements (`CurrentParticularLabelBounds.lean:21-74,
:94-191, :227-298, :317-417`). These are finite-label rate and support
estimates; they do not evaluate final radial observables.

### `CurrentSignedCurl.lean`

Defines the actual amplitude bound and proves common tangency, potential
smoothness, native exact curl, forward Cartesian curl, finite label-sum curl,
periodicity, overlap agreement, and current pressure-mode identities
(`CurrentSignedCurl.lean:29-119, :197-300, :304-373, :382-461`). This is a
genuine current-band potential-to-velocity bridge. It is local/finite-band and
does not state the final selected `barMoment` or five-observable equality.

### `InitialNativeRegularity.lean`

Defines copied amplitude/potential/pressure coefficients and proves smoothness
across flat radial attachments, positive-time chart coverage, angular
invariance, and nonzero-normal properties (`InitialNativeRegularity.lean:26-141,
:150-181`). This establishes initial native regularity rather than a global
moment transport identity.

### `PeriodicResidualLimits.lean`

Defines original, cut, and periodic residuals, proves smoothness and eventual
equality/extension results, and constructs joint residual-jet limits after
localisation (`PeriodicResidualLimits.lean:24-111`). Its module comment
explicitly says no residual identity or residual limit after periodisation is
assumed. It therefore cannot be used as evidence of a completed periodised
five-moment transport theorem.

### `SubcoverPeriodicity.lean`

Defines subcover/translation data and proves periodicity and agreement of
subcover fields across chart copies (`SubcoverPeriodicity.lean:20-154,
:160-295`). These are geometric deck/cover identities, not radial-observable
calculations.

### `TerminalHistoryBridge.lean`

Defines terminal history/clock and proves profile switching, radial support and
regular-clock derivative identities, plus history transport across terminal
bands (`TerminalHistoryBridge.lean:20-180, :840-1079`). The result remains a
profile/history layer and does not export the final selected field's five
moments.

### `ActualCurrentParticularAssembly.lean`

Proves finite label/harmonic sum formulas for current potential and pressure,
identifies the Cartesian curl with the particular velocity, and proves valid
chart equality for the finite current sum (`ActualCurrentParticularAssembly.lean:25-127,
:137-197, :214-276`). This is direct finite assembly evidence. It does not
cover the final infinite selected envelope or its radial observables.

### `ActualEndpointInputs.lean`

Defines `EndpointInputs` and the initial potential/direct/pressure models,
proves their extensions, and constructs endpoint inputs from concrete stage
representations (`ActualEndpointInputs.lean:28-120, :120-191, :218-264`).
This is an important packaging boundary: it feeds actual stage-zero and
positive-stage data into `candidate_of_finite_stages`/rate consumers. Its
fields concern endpoint smoothness, support, bounds, and representation, not
the paper's five-observable equality.

### `ActualParticularPotentialCoherence.lean`

Proves phase/velocity and pressure scaling identities, current potential and
pressure definitions, band transport, ambient germs, and cylindrical values
(`ActualParticularPotentialCoherence.lean:28-71, :77-121, :123-188,
:192-278`). This is a genuine potential-level transport layer before physical
curl and final packaging. No `barMoment` theorem is present.

### `ActualSeedPeriodicity.lean`

Proves torus deck-shift identities, conjugate pairing, phase periodicity, and
periodicity of primary velocity, pressure, and Gaussian coefficients
(`ActualSeedPeriodicity.lean:24-115`). This confirms seed periodicity for the
actual exact-curl construction but does not establish moment preservation
through the final selected sum.

## Cross-layer disposition

| Question | Source-grounded answer |
|---|---|
| Is there a real finite current-band curl bridge? | Yes. `CurrentSignedCurl` and `ActualCurrentParticularAssembly` prove current finite potential-to-velocity identities on valid charts. |
| Are endpoint input packages actual rather than abstract placeholders? | Yes. `ActualEndpointInputs` builds them from concrete stage models and representations. |
| Does this tranche prove final selected-field `(M,I,J,S,C_p)` transport? | No. |
| Does it prove concrete selected-field `Delta m != 0`? | No. |
| Does it prove impossibility or kernel-level `False`? | No. |

## Controlled conclusion

The audit must now record a narrower, stronger positive fact: the finite
current-band Cartesian curl and endpoint-input handoff are genuinely
implemented. The unresolved correspondence is not “no Cartesian curl exists”;
it is the still-unproved composition from those finite/current objects through
the selected infinite assembly, localisation, periodisation, and global radial
moment engine.
