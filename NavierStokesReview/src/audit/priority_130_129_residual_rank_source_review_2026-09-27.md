# Priority 130/129 source review: residual bridges, cycle means, and `FiveRowRank`

Date: 2026-09-27
Scope: six reachable OpenAI source modules selected from the live semantic register.
Method: direct source inspection of declarations and theorem statements.
Status: tranche evidence only; 296 reachable modules remain open after registration.

## Executive result

This tranche contains one of the strongest positive findings in the review so far: `FiveRowRank.lean` genuinely defines the three-coordinate debt, compactly supported repair functions, exact radial moment equations, two zero-mass rows, and the full five-row predicate. The residual bridge modules also prove real Cartesian/cylindrical and coordinate-layout identities, while `CycleMeanEquation.lean` propagates local mean-PDE hypotheses through the cycle.

These facts correct any claim that the rank/moment machinery is absent. They do not, by themselves, establish the selected-field correspondence. The inspected declarations still do not state that the final activated Cartesian `tsum` field after localisation and periodisation satisfies the five paper observables \((M,I,J,S,C_p)\). No concrete selected-field \(\Delta m\neq0\), impossibility theorem, or `False` is proved here.

## 1. `LinearWaveResidual.lean`

Source anchors: `NavierStokes/LinearWaveResidual.lean:498-569,571-626`.

The module defines bilinear advection and the cylindrical and Cartesian linearised residuals (`:498-515`). `cartesianLinearResidual_cylindrical` proves that the Cartesian linearisation is conjugate to the cylindrical expression under C2/differentiability and positive-radius hypotheses (`:531-569`). The later slice results transport space/time derivatives and the Laplacian through local slices (`:571-626`).

Audit result: this is a genuine local operator identity. It is not a theorem about global radial integration or final selected-field moments.

## 2. `PhysicalResidualBridge.lean`

Source anchors: `NavierStokes/PhysicalResidualBridge.lean:314-391,503-525,663-770`.

`pullbackData` packages a scaled graph map with positive-radius and open-domain hypotheses (`:314-332`). `velocity` and `pressure` construct the physical fields from graph data (`:334-345`). `cylindricalResidual_eq` proves the scaled graph residual identity (`:365-377`), and `physical_residual` identifies the local representation with the viscosity-one Cartesian residual (`:379-391`).

The common-graph theorem gives the explicit scale factor and local residual relation (`:503-525`). `MatchesAt` and the context residual formulas connect correction-state components to the graph (`:663-770`).

Audit result: this is a real field-level residual bridge on local off-axis domains. It does not provide the final infinite-sum, localisation, periodisation, or five-observable transport equality.

## 3. `PhysicalResidualTZ.lean`

Source anchors: `NavierStokes/PhysicalResidualTZ.lean:24-157,169-335,385-475`.

The module defines linear isometric coordinate swaps and proves reindexing of derivatives, transport, Laplacian, frame, and graph residual operators (`:24-157`). It reindexes correction-state fields, triples, operators, contexts, oscillations, errors, and states and proves their covariance (`:169-335`).

`graphMapTZ`, `velocityTZ`, and `pressureTZ` express the same scaled graph in `(T,Z)` order, while `graphResidual_swap` proves the exact coordinate-layout identity (`:385-433`). `context_fullResidual_physicalTZ` retains explicit chart and positive-radius hypotheses for the full correction-state residual (`:463-475`).

Audit result: this closes coordinate-layout covariance but remains a local residual statement. It does not identify the exported field with the paper's radial moment tuple.

## 4. `TransitionRamp.lean`

Source anchors: `NavierStokes/TransitionRamp.lean:23-184,195-372,702-820,903-1081,1152-1179`.

The module defines smooth step/damping ramps, integrated slopes, logarithmic and axial fields, and before/after/hold identities (`:23-184`). `StockReference` packages positive-radius reference profiles and proves smoothness, derivative, and control identities (`:195-372`).

The natural-coordinate section defines physical fields and proves activation identities, radial naturality, smoothness, positivity, and physical radial equations (`:702-820,903-1081,1152-1179`).

Audit result: this is substantive transition-profile mathematics. Its outputs are local profile/control identities, not the final selected Cartesian five-observable map.

## 5. `CycleMeanEquation.lean`

Source anchors: `NavierStokes/CycleMeanEquation.lean:189-215,216-255,523-605`.

`StepData` records positivity, domain, primitive data, covariance, rank geometry, operators, regularity, solenoidal blocks, and carrier compatibility (`:189-215`). The module proves particular/signed pressure zero, divergence identities, and exact next-error decomposition (`:216-255`).

`next_meanHypotheses` propagates local mean-PDE hypotheses to the next state, while `iterate_meanHypotheses`, `iterate_divergence_zero`, and `iterate_angularMean_fullGoodResidual` propagate them across natural-number cycle stages (`:523-605`).

Audit result: this demonstrates genuine inductive local mean/residual propagation. The source comment says the step inputs are constructed waves and streams, not mean identities. No final field-level `(M,I,J,S,C_p)` equality is stated.

## 6. `FiveRowRank.lean`

Source anchors: `NavierStokes/FiveRowRank.lean:19-24,93-165,189-246,249-280,311-560`.

The file explicitly defines `Debt := Fin 3 → ℝ` in the order `(P,Jθ,Jz)` (`:21-22`). It constructs compactly supported angular and axial repairs `deltaV` and `gamma` from separated smooth bumps (`:93-134`). `angular_moments` and `axial_moments` prove exact weighted integral equations, and `angular_mass_zero` and `axial_mass_zero` prove the two zero-mass rows (`:146-165`).

`FiveRows` is the full five-equation predicate, with two zero rows and three debt rows (`:240-246`). `five_rows_on_patch` and `five_rows` prove the predicate for the constructed repairs under explicit background hypotheses (`:249-280`). The later declarations prove existence, linearity, rescaling, norm, finite-jet, and joint smoothness properties (`:311-560`).

Audit result: this is genuine and important intermediate five-row repair algebra. It materially narrows the audit: the issue is not absence of local rank/moment construction. The unresolved question is whether these rows are transported into the final selected Cartesian field and endpoint predicate. This module contains no such endpoint theorem.

## Cross-module classification

| Question | Result |
|---|---|
| Is `FiveRowRank` real five-row mathematics? | Yes. It explicitly proves the five local repair equations and two zero rows. |
| Are residual bridges real? | Yes, under local chart, smoothness, and positive-radius hypotheses. |
| Is cycle propagation real? | Yes, for local mean-PDE hypotheses and divergence/good-residual quantities. |
| Does this establish final selected-field `(M,I,J,S,C_p)` transport? | No. |
| Does this prove selected-field `Delta m != 0`, impossibility, or `False`? | No. |

## Register action

These six modules are registered as `evidence_inspected` in the authoritative semantic register. The register must be regenerated and mirrored after this tranche; the local five-row result must not be misreported as endpoint transport.
