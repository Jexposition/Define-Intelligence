# Priority 71 source review: curl realization, diagonal extensions, carrier binding, and finite heads

Date: 2026-09-28

Scope: direct source review of four reachable modules in `NavierStokes/`. This report records what the declarations actually establish. It does not infer a nonzero defect, impossibility, or kernel contradiction from the absence of a theorem.

## `LocalizedCurlRealization.lean`

Source anchors: lines 1-10 imports and module scope; lines 48-58 `RawData`; lines 83-120 localised smoothness, tangency, native potential smoothness, curl realization, divergence zero, and velocity smoothness; lines 124-167 zero-germ inheritance; lines 169-240 common-field curl/divergence/smoothness; lines 244-257 signed coefficient tangency; lines 272-305 complex-copy tangency.

The module has genuine local field-level content. `RawData` requires cylindrical geometry, phase/amplitude/cutoff smoothness, nonzero frequency and normal, and tangency. `native_realizes_curl` identifies a cylindrical curl of the local vector potential with a corrected vector mode, while `native_divergence_zero` proves the corresponding cylindrical divergence vanishes. The common-field declarations lift those facts across covered cells using germ agreement and zero-germ alternatives. The module also proves local smoothness and tangency for signed and complex copy coefficients.

The boundary is exact: these declarations are local/on-patch identities. No declaration in this module mentions `barMoment`, `torusAverage`, the five cumulative observables `(M,I,J,S,C_p)`, `PositiveOrderMoments.Debt`, `FiveRowRank.FiveRows`, `ActualCandidateAssembly.Witness`, or `selected_witness`. Therefore it verifies local curl realization and incompressibility infrastructure, not global radial-moment transport through the selected Cartesian field.

## `MixedDiagonalExtensions.lean`

Source anchors: lines 1-3 imports; lines 29-47 extension transfer; lines 50-79 endpoint behaviour of `physicalQ` and eventual zero of the diagonal potential sum; lines 83-95 off-plane one-sided extension; lines 99-119 `SublevelShrinkingSupport` and eventual-zero theorem; lines 123-130 finite initialization; lines 134-154 support of copy sums/vector sums; lines 158-181 eventual equality of the full potential sum with stage zero; lines 183-210 central and diagonal away-extension assembly.

This module provides support and extension control for the potential-level natural sum. In particular, large-scale cutoffs force the potential sum to vanish eventually on specified endpoint neighbourhoods, and on the central plane positive stages vanish so the sum is eventually equal to the initial stage. It also proves one-sided extensions by combining these eventual equalities with finite raw endpoint extension hypotheses.

These are potential-level support/extension statements. They do not evaluate the curl-localisation commutator, radial integrals, torus averages, weighted moments, or the five-observable tuple. Eventual equality to stage zero is not a theorem that stage-zero or the complete selected field has the paper's five moments.

## `ActualCarrierTransport.lean`

Source anchors: lines 1-10 imports and scope; lines 19-28 exported carrier declarations; lines 32-36 definitional domain/label equalities; lines 38-50 canonical geometry, length, and cutoff identities; lines 52-64 fixed-parameter geometry, length, and cutoff identities.

This module binds primitive carrier transport data to actual cycle/canonical parameter records by definitional equalities and a native-cutoff identity. It contains no field construction, curl, sum, radial observable, moment certificate, or endpoint candidate theorem. Its role is parameter-record identification, not physical-field semantic transport.

## `FiniteHeadClass.lean`

Source anchors: lines 21-50 finite-prefix comparison and exponent transfer; lines 52-64 majorant comparison; lines 65-74 derivative vanishing on an open domain; lines 76-93 finite-prefix jet bounds; lines 95-109 finite-band class transfer; lines 111-127 mean/wave/unweighted class corollaries.

This module proves that a finite initial prefix of bands can change exponents while preserving weighted class membership, with zero tails handled by `jet_eq_zero`. It transfers derivative majorants and class predicates. It does not inspect or calculate the values of any radial moment and does not connect a class predicate to the final selected Cartesian field.

## Cross-file finding

The four modules strengthen the intermediate architecture in four different ways:

| Layer | Verified source content | Missing from this layer |
|---|---|---|
| Local curl realization | Patchwise curl identity, divergence zero, smoothness, tangency, germ inheritance | Global `barMoment`/`torusAverage` transport |
| Diagonal extensions | Support, eventual zero, stage-zero replacement, one-sided extensions | Radial observable evaluation after curl and summation |
| Carrier binding | Canonical/fixed parameter equalities | Physical field or moment equality |
| Finite heads | Finite-prefix jet/class exponent transfer | Five-moment value-level transport |

The direct evidence therefore narrows, but does not close, the audit question. These modules do not show that the moments are destroyed, and they do not show that the moments are preserved. They show that the code has local regularity/support machinery while the global selected-field observable remains unproved in this tranche.

Status: source reviewed; no `Delta m != 0`; no impossibility theorem; no `False`.
