# Inverse-domain call-site map

Date: 2026-09-22  
Snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

## Purpose

This map separates actual analytic inverses from ordinary coordinate inverses
and records the domain supplied at each load-bearing call site. It tests the
external lead that all inverses and differentiated inverses should share one
common admissible domain.

## Load-bearing analytic inverse interfaces

| Interface | Domain supplied | Conditions carried | Observation |
|---|---|---|---|
| `SmoothFamilyTorusInverse.inverse_finiteJets` | Arbitrary `S : Set P` in the universal parameter cover | `ContDiff ℝ ∞`, periodicity, nonnegative jet bound | Five input derivatives are lost; the theorem is local in `S` and does not require `S` nonempty. |
| `GaugeAliasDecay.familyInverse_finiteJets_fiber` | `fiberShell a b s = Icc a b × {s}` | Smoothness and periodicity of `toProduct f`; source jet bound on the same fibre | Pulls the universal-cover estimate back to the fixed slow fibre. |
| `GaugeAliasDecay.sourceJet_finiteJets_fiber` | Same `fiberShell a b s` after each radial inverse/parameter derivative | `Admissible a b f`, smoothness, source support and zero-mode conditions | Inductively preserves the same radial interval and fibre; later stages pay six source-jet orders per IBP step. |
| `GaugeAliasDecay.totalIntegral_finiteJets_fiber` | Same interval and fibre, with `a ≤ b` | Source support, admissibility, nonzero frequency | Converts the repeated inverse bounds into the transport primitive estimate. |
| `ParametricTorusInverse.mixedJet_inverse_bound` | Arbitrary slow set `S : Set ℝ`; torus variables in the unit square | Smoothness and periodicity; zero-order and two swapped torus jet bounds | Mixed parameter/torus derivatives are controlled on the same `S`; no separate spatial domain is introduced. |
| `UniformFourierAlias.realInverse_finiteJets` | Arbitrary `A : Set P` | Smoothness and parameter periodicity | Real inverse is obtained by complexification on the same `A`. |
| `FourierAlias.fourierSourceJet_properties` | Radial support interval `[a,b]` plus the torus parameter domain | Smoothness, periodicity, zero mean, radial support | Iterated inverse and parameter jets preserve the same support and admissibility predicates. |

## Non-analytic coordinate inverses

`ActualReferenceRebase.inverseCover`, `ParabolicSupport` inverse dilations,
and `Riesz` inverse Fourier terminology are coordinate or transform maps in
their respective interfaces. They are not the same operator as the torus
directional inverse and must not be conflated with its derivative-loss ledger.

## Result of the map

The source shows a coherent local-domain pattern: the torus inverse accepts a
set `S`, the gauge layer specialises it to one `fiberShell`, and the radial
iteration preserves the same interval and fibre. The load-bearing compact-alias
call at `GaugeAliasDecay.lean:294-295` obtains `0 < c`, `c < e`, and the
support-side inequalities from `qLength_reference_bounds` before invoking
`physicalTotal_finiteJets_local`; the inverse/transport interface therefore
does not silently run on an unproved empty radial interval.

No concrete empty-domain failure was found. The remaining open item is not the
local inverse hypothesis but the analytic provenance from these local domains
through the correction construction to the final selected physical witness.
That question remains separate from the CMI predicate match.

## Reproduction searches

```text
rg -n "familyInverse_finiteJets_fiber|sourceJet_finiteJets_fiber|totalIntegral_finiteJets_fiber|mixedJet_inverse_bound|realInverse_finiteJets" NavierStokes --glob '*.lean'
rg -n "inverse_finiteJets|parameterJet_inverse|inverse_solves" NavierStokes --glob '*.lean'
```
