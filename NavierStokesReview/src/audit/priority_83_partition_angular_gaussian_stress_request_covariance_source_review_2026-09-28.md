# Priority 83 source review: partitions, angular fields, Gaussian tails, stress weights, signed requests, and covariance

Date: 2026-09-28
Scope: direct source review of the six highest-priority reachable modules in the regenerated semantic register.

## Reviewed source

1. `NavierStokes/SquaredPartition.lean`
2. `NavierStokes/DirectAngularDiagonal.lean`
3. `NavierStokes/GaussianTailFlat.lean`
4. `NavierStokes/LeadingStressWeights.lean`
5. `NavierStokes/LocalSignedRequest.lean`
6. `NavierStokes/PulseCovariance.lean`

## Findings

### `SquaredPartition.lean`

The module constructs smooth compactly supported translated bumps, grid/product masks, dyadic masks, physical slow masks, and label masks. It proves local finiteness, compact support, finite derivative support, and exact squared partition identities. In particular, `gridMask_sum_sq`, `dyadicMask_tail_sum_sq`, `labelMask_tail_sum_sq`, and `labelMask_tail_total_sum_sq` are exact algebraic/finite-support results rather than numerical approximations.

This is important for the localisation audit: the partition machinery is real and normalised. It does not by itself prove that the final curl-localised `tsum` preserves any of the paper's radial observables.

### `DirectAngularDiagonal.lean`

The module defines the literal angular field and locally finite angular sum, then defines

\[
u_{\mathrm{mixed}}=u_{\mathrm{potential\ sum}}+u_{\mathrm{angular\ sum}}.
\]

`mixedVelocity_smooth`, `mixedVelocity_divergence`, and the actual diagonal/cutoff theorems prove smoothness and divergence-free composition under explicit hypotheses. The module also proves axis vanishing, physical graph pullback, spatial-cut transport, finite-prefix/all-order jet identities, and preservation of axis germs when the potentials vanish near the axis.

This is concrete Cartesian field realisation and directly rebuts any claim that the construction is only an unconnected scalar profile. It still does not export a theorem evaluating the final field against `(M,I,J,S,C_p)`.

### `GaussianTailFlat.lean`

The constructed slot cutoff has an exact plateau and compact support. The source proves derivative-support localisation, compact support of every derivative, uniform jet bounds, and the Gaussian off-plateau estimate. `gaussian_beats_Q_power` proves that polynomial factors in the scale are dominated by every real power of the dyadic `Q` scale.

These are rigorous tail and jet estimates. They control local regularity and decay; they are not a weighted radial-integral transport theorem.

### `LeadingStressWeights.lean`

This module defines nominal and modulated leading stress in logarithmic and physical radial charts. It proves exterior stress vanishing before and after the active annulus, strict nonvanishing in a full cone, `kappa_lt_one`, exact edge joins, weighted bounds, radial pullback identities, and derivative-dependent physical jet bounds. The final weighted-profile existence theorem retains a complete finite-modulation witness and edge-direction certificates.

This is substantial reduced profile and stress evidence. The output remains a profile/stress witness, not the public selected whole-space Cartesian field with a proved five-observable equality.

### `LocalSignedRequest.lean`

The module proves exact profile-map and inverse-map identities, smoothness and positive jets, MeanClass transport, compact signed primitive estimates, torus-average transport, physical radial scaling, and chart coherence. It defines the actual signed stress request and proves radial divergence formulas for angular and axial components. `physicalAdjusted_moment_zero` proves the adjusted primitive's prescribed moment vanishes; support, compact-slice, and smoothness results are also explicit.

These are direct local radial/moment bridges and must be counted as such. They remain conditional on local chart/support hypotheses and are not composed here with the final global `tsum`/curl/periodisation endpoint.

### `PulseCovariance.lean`

The module constructs Gaussian pulse weights and actual tangent/covariance columns. It proves integrability, positive mass, first weighted moment bounds, directional concentration, exact covariance factorisation, signed strict-cone identities, and compact positive inverse results. This is a real pulse covariance construction, not a placeholder interface.

## Correspondence result

Priority 83 strengthens the positive source record at the localisation, Cartesian, tail, stress, signed-radial, and covariance layers:

- partition masks are smooth, locally finite, compactly supported, and exactly normalised;
- the mixed field is an actual sum of solenoidal potential velocity and direct angular velocity, with divergence and axis-germ theorems;
- Gaussian slot errors have all-order support and quantitative decay bounds;
- leading stress has exact edge/exterior and weighted profile controls;
- signed requests have torus-average, radial-divergence, support, and zero-adjusted-moment results;
- pulse covariance is integrated and placed inside a strict cone.

The audit must not describe these layers as absent or generic-only. At the same time, none of the six reviewed modules states the complete value-level composition

\[
\operatorname{Obs}_{\mathrm{radial}}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
=(M,I,J,S,C_p)
\]

after all selected-stage curls, localisation, `tsum`, periodisation, and public `Witness` packaging. This tranche therefore adds positive evidence without proving `Delta m != 0`, impossibility, `False`, or full CMI correspondence.
