# Priority-73 tranche: radial jets, chart lifts, extensions, rephasing, and integral infrastructure

**Date:** 2026-09-28
**Scope:** eleven reachable Lean modules selected from the regenerated semantic-coverage queue.
**Method:** direct source inspection of definitions and theorem statements.

## Result

This tranche contains important positive evidence that narrows the audit. `BaseRadialJets` constructs a literal normalized radial component of a summed curl base and proves radial identities; `RadialAlias` uses actual Bochner/interval integrals and proves support-based integration-by-parts formulas; `AllBandBaseJets` proves radial envelopes and polynomial/jet bounds. These are not toy interfaces.

The inspected declarations nevertheless do not, by themselves, state the complete selected-endpoint equality for the paper’s five observables `(M,I,J,S,C_p)`. The evidence status is therefore **partial radial/analytic infrastructure with endpoint transport still unresolved**, not “radial machinery absent”. No `Delta m != 0`, impossibility theorem, or `False` is established here.

## Module findings

### `ActualCurrentCarrierJets.lean`

Defines actual carrier phase/character data and proves smooth-neighbourhood, positivity, and control-patch jet results. This is native carrier parameter regularity; it does not evaluate global radial observables.

**Anchors:** lines 21–71, 75–127, 137–201.

### `AllBandBaseJets.lean`

Proves exact zero/leading-term identities for positive cutoff scales, normalized tangential/error envelopes, actual estimates, polynomial normalized streams, reduced radial polynomial forms, radial envelopes/quotients, uniform radial jets and pullbacks, and final weighted-bundle estimates. This is substantive reduced radial/base-bound machinery. The inspected declarations do not identify the final selected Cartesian field with `(M,I,J,S,C_p)`.

**Anchors:** lines 27–91, 118–185, 221–366, 393–447.

### `AnalyticCoefficientBounds.lean`

Defines complex tubes, holomorphic coefficient bounds, real jets, radius-loss series, axis-space conversion, and normalized exponential bounds. These are analytic coefficient estimates and summability controls, not a physical radial-moment evaluator.

**Anchors:** lines 24–148, 174–243, 255–340.

### `BaseRadialJets.lean`

Defines the averaged axial coefficient sequence, normalized stream, and the literal normalized radial component of the constructed curl base. It proves `radial_eq`, `radial_eq_stream`, reduced radial polynomial/envelope/jet results, and `final_radial_eq`. This is direct positive evidence that part of the radial profile is realised after the base curl construction. The inspected source does not state that the complete selected Cartesian field, including all stages, masks, periodisation, pressure, and endpoint packaging, satisfies the five paper observables.

**Anchors:** lines 23–120, 144–177, 189–329, 363–386.

### `CurrentPhysicalChartJets.lean`

Proves smoothness and positive jets of the physical polar chart, composition and rotation jets, chart scaling/germ identities, and real-vector norm bounds. This is chart-lift regularity, not global radial-moment transport.

**Anchors:** lines 45–141, 159–235, 258–289.

### `FlatZeroExtension.lean`

Defines zero extension and proves local Gaussian bounds, flat edge derivatives, iterated-derivative identities, and joint smoothness of the zero extension. This is endpoint regularity and does not establish any global moment identity.

**Anchors:** lines 30–102, 141–237.

### `ParametricRephase.lean`

Constructs a parameter-dependent phase map and its exact inverse, proves bijectivity, smoothness through the inverse function theorem, periodicity, rephased-family identities, and smooth parameter integrals. This is genuine rephasing/integration infrastructure, but no five-observable radial transport theorem is stated.

**Anchors:** lines 26–69, 106–179, 189–283.

### `RadialAlias.lean`

Defines a translated radial integral and whole-line alias using actual interval/Bochner integrals, a radial-support predicate, directional/slow derivatives, and repeated integration-by-parts/source-jet identities. The support hypotheses produce endpoint cancellations and norm bounds. This is important radial integral infrastructure, but its generic `aliasIntegral`/`wholeAlias` declarations are not the paper’s five-tuple evaluator and are not, in the inspected source, connected to `selected_witness`.

**Anchors:** lines 28–47, 50–132, 161–215, 226–260.

### `ScaledParticularFrameJets.lean`

Proves scaled frame normal/motion/action jets, affine argument geometry, frame-field native jets, selected-frame identities, and native normal bounds. This is particular-frame jet control, not five-observable transport.

**Anchors:** lines 31–55, 96–152, 177–260.

### `SmoothParameterIntegral.lean`

Defines genuine parameter jets and proves differentiation, Taylor expansion, smoothness, and interval-integral regularity under local integrable majorants. This is general integration-under-the-derivative infrastructure. It supplies no selected physical moment equality.

**Anchors:** lines 27–118, 127–214, 227–311.

### `SpacetimeEndpoint.lean`

Defines open/closed past sets and proves trace extension, boundary continuity, periodicity, mixed-jet extension, smooth Taylor families, and joint endpoint extension. This is spacetime boundary regularity and does not state radial-observable transport.

**Anchors:** lines 25–139, 175–262, 277–374.

## Cross-layer interpretation

1. The audit must now record actual positive radial realisation in `BaseRadialJets`, not claim that all radial identities stop before the curl/base layer.
2. `RadialAlias` proves real support-based integration-by-parts identities, but a generic integral alias is not automatically the paper’s `(M,I,J,S,C_p)` map.
3. `AllBandBaseJets` and `BaseRadialJets` establish reduced/base estimates; the remaining question is their composition with every selected stage, localisation, periodisation, summation, pressure, and `Witness` packaging layer.
4. No inspected file in this tranche establishes the full selected-endpoint equality or a nonzero defect.

