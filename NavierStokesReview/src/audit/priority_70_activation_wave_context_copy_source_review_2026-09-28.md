# Priority-70 source review: activation, wave regularity, common context, and copy/solve compatibility

Date: 2026-09-28
Evidence class: direct Lean source declarations and theorem signatures.
Scope: four reachable priority-70 modules.
Boundary: the report does not convert a missing target declaration into a proof of impossibility or `False`.

## `NavierStokes/ActivationBounds.lean`

The module imports `StressActivation` (line 1) and defines smooth parameter factors, rescaled primitive/control values, angular factors, density error factors, and history coefficients (lines 22-226 and 330-414). It proves compact-parameter jet bounds and uniform jet bounds (lines 63-324 and 453-464), scaled-factor identities (lines 115-226 and 366-414), and continuation/independence results for the activated histories (lines 522-687).

The file therefore contains substantive transformed-integral and jet regularity infrastructure. Its declarations are reduced activation/error factors. No `barMoment`, selected Cartesian field, `FiveRows`, or equality to `(M, I, J, S, C_p)` is stated.

## `NavierStokes/ActualWaveRegularity.lean`

The module imports `CorrectionStep` and `WaveEdgeExtension` (lines 1-2). It defines domain restrictions and native data (lines 27-56), then proves smoothness of common/native potentials, velocities, corrected fields, and zero germs (lines 63-154). It defines translation-on predicates and proves translation compatibility for phase normals, cylindrical curls, common amplitudes, common corrected data, and common velocities, including `tsum` congruence (lines 172-279). Later declarations package finite periodic/support regularity and actual cycle/particular/signed data regularity (lines 291-869).

This is genuine finite-wave regularity and translation/curl support. It does not state the final selected-field five-observable transport theorem or evaluate the radial moments after all local wave operations.

## `NavierStokes/CommonBaseContext.lean`

The module imports `BaseContextAssembly`, `BaseStressClasses`, and `PhysicalResidualNaturality` (lines 1-3). It defines index bounds and radial/fast coefficients (lines 25-103), reconstructs physical operators and proves their match with the physical residual bridge (lines 118-160), then proves cover-lift scaling, physical-to-chart transport, reindexing, pullback derivative identities, and periodicity (lines 165-373). It instantiates a nominal-profile context and proves base bounds, smoothness, physical operator matching, stress properties, cover identities, and primary-coefficient matching (lines 396-625).

These are important reduced-to-chart and physical residual naturality results. They stop at context/operator and stress-class identities. They do not state a global `torusAverage`/`barMoment` equality for the selected Cartesian field.

## `NavierStokes/CopySolveCompatibility.lean`

The file imports `CommonCoverClass` (line 1). It proves geometry refinement and native copy-sum refinement (lines 20-60), transports coefficients, forcing, paths, anchored/copy/localized/common solves, and source periodicity (lines 64-178). It also proves recentering, source scaling, time-clock transport, and `tsum` congruence (lines 181-498). The `transportData`, `transportGeometry`, `commonSolve_transport`, `physicalOutput`, and family-representation declarations occur at lines 507-588. Compatibility and same-input results follow at lines 613-687.

This file is a substantial transport/equivalence layer for copy solves. Its `physicalOutput` is a generic smooth output under transported input data, not the OpenAI selected whole-space candidate endpoint. No theorem here maps that output through `torusAverage` to the paper's five radial observables.

## Cross-file result

The source confirms more genuine intermediate transport than a superficial endpoint scan would show:

\[
\text{activation factors} + \text{wave regularity} + \text{context naturality}
\longrightarrow
\text{smooth transported local/copy fields and residual coefficients}.
\]

It still does not exhibit the distinct global composition required for the paper correspondence:

\[
\text{selected Cartesian field}
\longrightarrow \operatorname{torusAverage}
\longrightarrow \operatorname{barMoment}
\longrightarrow (M,I,J,S,C_p).
\]

This tranche is therefore positive evidence for intermediate mathematical infrastructure and negative evidence only for the presence of the target declarations in these four files. It does not prove that the final moments are nonzero, nor that the construction is impossible.

## Register action

These four modules are to be entered as `evidence_inspected` with the anchors above. The full register and its public mirrors must be regenerated before the tranche is treated as complete.
