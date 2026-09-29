# Priority 109 source review: carrier, cycle, signed-copy, axis, and pressure-flux modules

Date: 2026-09-28
Scope: twelve reachable Lean modules selected from the semantic coverage register.
Method: direct source inspection of imports, declarations, definitions, and theorem premises.
Classification: this review records what the declarations prove; it does not infer a missing theorem from a missing name.

## Executive result

This tranche contains substantial intermediate transport and regularity results. In particular, it proves:

- current-band Cartesian-radius, native-point, support, germ, and active-field identities;
- signed request, amplitude, pressure, and `tsum` scaling transport;
- cycle-state, temporal-alias, rank-alias, and pressure-alias transport across overlapping bands;
- angular invariance through derivatives, `tsum`, copy solves, and cylindrical curl coefficients;
- finite-support periodised physical-family assembly;
- reduced natural-axis pressure and coefficient integral identities;
- comparative whole-space pressure-flux estimates under `PressureRecovery.Hypotheses`.

The tranche does **not** prove the final selected-field observable

\[
  \operatorname{barMoment}
  \bigl(\operatorname{torusAverage}(u_{\mathrm{selected}})\bigr)
  = (M,I,J,S,C_p),
\]

nor does it prove an absolute selected-pressure Poisson/Leray representation. This is a remaining composition boundary, not evidence that all upstream transport is absent.

## Module findings

### `NavierStokes/ActualCurrentWaveSupport.lean`

Anchors: imports 1–6; band support 111–205; native coordinate identities 273–345; current mode support/germs 356–601; glued-field support 657–706.

The module identifies the physical Cartesian radius with the slow graph radius, proves native-point coordinate and parameter-domain identities, and transfers native zero germs through local potential and pressure modes. `current_modes_zero_off_carrier`, `current_modes_support`, `current_modes_zero`, and `current_mode_annulus` establish support and annular localisation. The final section proves active germs, active zero behaviour, field support, and axis-zero behaviour.

These are pointwise/support and local Cartesian-coordinate results. They do not define `barMoment`, a torus average of the final field, or the five paper-observable tuple.

### `NavierStokes/ActualIterationLedger.lean`

Anchors: imports 1–2; gain and sigma algebra 36–110; physical gaps 145–198; residual rates 228–315.

The module proves the arithmetic of the iteration schedule: monotonicity and divergence of `sigma`, gain inequalities, fixed offsets, residual exponents, and eventual residual-rate growth. The output is rate arithmetic and exponent bookkeeping. It contains no field integral, curl/localisation commutator, pressure recovery, `FiveRows`, or selected-field moment equality.

### `NavierStokes/ActualSignedCoherence.lean`

Anchors: imports 1–4; chart and scale transport 64–296; request transport 296–327; signed vector/pressure transport 331–426; `tsum` amplitude/pressure transport 428–467; germ and exact-block transport 469–559.

This is genuine value-level signed-copy transport. `fullRequest_transport` proves the request scaling under the band chart. `common_amplitude_of_request` and `common_pressure_of_request` push the transported scaling through a `tsum`, using `tsum_congr` and constant scalar extraction. The exact-block theorems continue this transport to amplitude and pressure germs.

The conclusion remains local and label/stage indexed. No theorem here applies `barMoment` to the fully selected Cartesian field or identifies the resulting observables with \((M,I,J,S,C_p)\).

### `NavierStokes/CopyAngularInvariance.lean`

Anchors: imports 1–3; invariant algebra 33–105; copy/pressure invariance 128–289; curl invariance 304–341; actual-copy curl 350–370; corrected fields 491–509.

The module proves that a specified angular/phase invariance is preserved by maps, derivatives, directional operations, `tsum`, copy solves, pressure solves, native cutoffs, cylindrical curl, curl remainders, and realised coefficients. It also derives angular-zero consequences under explicit invariance premises.

This is an important correction to any claim that the code lacks curl-level invariance machinery. It is not a radial five-moment evaluation theorem: invariance under an angular action is not equality of the five cumulative radial observables.

### `NavierStokes/CycleStateCoherence.lean`

Anchors: imports 1–5; primitive state 279–310; reconstruction/alias band 323–356; `CycleTransport` 377–452; iteration declarations 481–656.

`StagePrimitives` packages particular, signed, temporal, ranked, and rank-geometry premises. `CycleTransport` packages band transport for those four stages together with temporal, old-pressure, and current-pressure aliases. `cycle_transport` constructs that certificate from primitive regularity, covariance, rank geometry, and wave-on-band premises.

This proves a substantial local correction-cycle transport chain. Its fields are `StateBand` and `ErrorBand` relations on slow domains and aliases; they are not `barMoment` equalities for the final selected whole-space field.

### `NavierStokes/DependentSignedPhysicalFamily.lean`

Anchors: imports 1; family/diagonal support 23–272; periodised active identities 321–365; identity-chart jets 382–475; wave-data bounds 551–562.

The module constructs dependent physical copy families, proves inactive-label zero results, finite/local diagonal sums, support and smoothness, and identifies active periodised potential and pressure terms with their physical singleton families. The identity-chart theorems show that the local source adapter is an identity and provide finite jet bounds.

These are concrete finite-family and periodisation identities. They stop before a whole-space radial observable is applied.

### `NavierStokes/FuturePressureBounds.lean`

Anchors: imports 1–3; future clock and square-integral bounds 36–219; future mass/pressure identities 226–301; derivatives and ideal integral 316–489; corrected future integral/pressure equalities 508–566.

This module proves future-tail integrability, pressure-source mass identities, derivative bounds, and that a future-supported zero-total-integral correction leaves the future integral unchanged. `ideal_left_integral` is explicitly tied to `PressureDatum.ideal_prefix_mass`; `corrected_future_pressure_eq` is a reduced pressure-history identity.

These are reduced radial/history pressure results. They do not establish an absolute global pressure representation for the selected Cartesian candidate and do not evaluate the five selected-field observables.

### `NavierStokes/NaturalAxisBridge.lean`

Anchors: definitions 28–44; radial evaluation algebra 48–210; parameter/source structures 221–321; remainder and natural-operator identities 344–521; integrated solution 521–716.

The module defines partial and mixed derivatives, radial evaluation, radially constant inputs, parameter data, pressure sources, reconstructed reduced profiles, remainders, and an integrated reduced solution. It proves the pressure equation and pressure integral for this reduced axis system.

This is a genuine reduced-axis bridge. It is not a theorem that the selected Cartesian `tsum` field, after localisation and periodisation, has the paper's five global moments.

### `NavierStokes/NaturalAxisCoefficients.lean`

Anchors: imports 1–7; analytic rational fields 27–190; coefficient family 299–429; phase/amplitude inputs 445–577.

The module constructs analytic complex and real coefficient fields, proves real-axis restriction, common analytic neighbourhoods, radially constant coefficient families, ideal-prefix coefficients, phase derivatives, and amplitude bounds. The pressure input is supplied by `PressureDatum.complexPressure`.

This is analytic coefficient infrastructure. It contains no selected endpoint, no `barMoment`, and no five-observable transport statement.

### `NavierStokes/PhysicalStageBounds.lean`

Anchors: imports 1–3; `WaveData` 51–135; `MeanData` 154–213; increments 286–369; stages 398–518; joint inputs 528–571.

`WaveData` and `MeanData` package native smoothness, support, and derivative-rate information. The module constructs potential and pressure increments, proves smoothness and rate bounds, then builds potential, direct, and pressure stage sequences. `derived_stage_inputs` returns smoothness and `RawStageBounds` for the three stage families.

The comments and types make the boundary explicit: these are local physical stage estimates. They do not contain a selected-field five-moment equality or a radial-integral convergence theorem.

### `NavierStokes/R3/PressureFlux.lean`

Anchors: imports 1–7; canonical flux 125–209; comparative actual flux 211–232; commutator decomposition 235–376; uniform pressure-flux bound 576–600.

The module defines canonical pressure pairings against compact smooth comparison tests and proves integrability and norm bounds. `actual_flux_eq_canonicalCutoffFlux` and `exists_uniform_actual_pressure_flux_bound` require `PressureRecovery.Hypotheses T u v p q`, so they compare \(p-q\) and \(u-v\) under equal-residual hypotheses. They do not select an absolute pressure for one candidate and do not evaluate the paper's radial moments.

This strengthens the comparative-pressure classification: the pressure-flux chain is real, but it is not an absolute selected-pressure Poisson theorem.

### `NavierStokes/SignedCopyBounds.lean`

Anchors: imports 1–3; local operations 54–188; quotient jets 192–240; native covariance 386–483; signed amplitude/pressure 494–589; actual/localised coefficient bounds 600–648; uniform covariance 711–828.

The module proves local jet closure for signed quotients, native covariance invertibility, signed scalar/vector jets, projected pressure jets, and uniformised/localised coefficient bounds. Its output is `LocalJets` and `UniformLocalJets` data suitable for periodisation.

No theorem here integrates the resulting coefficients into `barMoment`, and no theorem identifies the final selected Cartesian field with \((M,I,J,S,C_p)\).

## Cross-module audit classification

| Question | Result in this tranche |
|---|---|
| Are there genuine Cartesian/curl/`tsum` transport theorems? | Yes: especially `ActualSignedCoherence`, `CopyAngularInvariance`, `DependentSignedPhysicalFamily`, and `ActualCurrentWaveSupport`. |
| Are there genuine cycle and alias transport certificates? | Yes: `CycleStateCoherence.CycleTransport`. |
| Are there pressure integral and pressure-flux theorems? | Yes, but reduced or comparative: `NaturalAxisBridge`, `FuturePressureBounds`, and `R3/PressureFlux`. |
| Is an absolute selected-pressure Poisson/Leray theorem present here? | Not in the inspected declarations. |
| Is the final selected Cartesian field evaluated by `barMoment` here? | No inspected declaration does so. |
| Is \((M,I,J,S,C_p)\) exported from these modules into `Witness`? | No. |
| Does this tranche prove a nonzero defect or `False`? | No. It narrows the unresolved composition boundary but does not establish a defect. |

## Status

This report changes the status of all twelve source rows from `reachable_not_semantically_inspected` to `evidence_inspected`. It does not change the global verdict: the final selected-field moment transport remains unestablished, while intermediate transport is demonstrably present.
