# Priority 112 source review: activation stocks, diagonal jet sums, and extended heated profiles

Date: 2026-09-28
Scope: direct source review of three reachable modules in `NavierStokes/`.

This tranche records what the declarations prove and the boundary they do not cross. It does not infer a nonzero defect, a failed theorem, or `False` from the absence of a final observable theorem.

## 1. `NavierStokes/ActivationStocks.lean`

This module is a reduced activation/profile stock layer. It defines `massFlux`, `angularRemainder`, `stockOne`, and `stockTwo`, then proves the corresponding stock equalities, eta/log views, actual/reference identities, pressure and derivative histories, and uniform jet bounds. The declarations are profile-side data and regularity contracts; they are not the exported Cartesian witness.

Evidence anchors: lines 20–72, 93–99, 174–219, 239–312, 334–500, 522–711, 747–785, and 868–1027.

Audit boundary: no inspected declaration contains `barMoment`, `FiveRows`, `PositiveOrderMoments`, `FiveProfileMoments`, or an equality identifying the final selected Cartesian field with `(M,I,J,S,Cp)`. The module therefore supplies real upstream stock/jet evidence but not endpoint transport.

## 2. `NavierStokes/DiagonalJetBounds.lean`

This module addresses the infinite-stage analytic issue at the derivative/rate level. It proves local-finiteness consequences for the `tsum`, derivative identities reducing the infinite sum to a finite active sum, prefix/tail decompositions, scalar and norm tail bounds, potential-tail jet bounds, and uncut prefix/tail orders.

Evidence anchors: lines 1–24, 29–190, and 196–307.

Audit boundary: these are local jet and norm estimates. They do not establish convergence of weighted radial integrals, interchange the final `tsum` with `barMoment`, or prove preservation of the five paper observables after curl, localisation, periodisation, and global assembly.

## 3. `NavierStokes/ExtendedHeatedOutgoing.lean`

This module constructs a compensated outgoing profile over an open parameter neighbourhood. Its `Witness` (lines 59–80) carries positivity, coefficient smoothness, coefficient/derivative/first-jet bounds, and a three-component reduced physical-moment equation combining terminal compensation data with `ExtendedHeatDebts.physicalDebt`.

The module then proves:

- heat/change-row decompositions and integrability (lines 266–347);
- exact change-row integral cancellation (`changeRow_integral_zero`, lines 350–362);
- canonical pressure and energy decompositions and unchanged pressure/energy/renormalised integrals (lines 447–487);
- zero mass, angular, and renormalised reduced moments (lines 489–507 and nearby declarations);
- smoothness, support/positivity, axis limits, and the reduced `Specification` (lines 846–919).

Audit boundary: this is substantive reduced-profile moment machinery, not dead code. Its variables are `(X, eta)` and its observables are reduced profile integrals. The reviewed declarations do not prove that the final assembled Cartesian field, after `SpatialCurl`, localisation, periodisation, and `tsum`, has the paper-level global tuple `(M,I,J,S,Cp)` under the repository's final `barMoment` operator.

## Cross-module result

The current evidence strengthens the audit in two directions at once:

1. The upstream profile and cancellation machinery is real and includes exact integral identities.
2. The remaining correspondence question is narrower than “does any moment code exist?” It is whether those reduced identities are transported through the concrete global field construction and exported at the selected endpoint.

The register therefore records these modules as semantically inspected, while retaining the endpoint `CORRESPONDENCE_GAP` until a declaration-level theorem or a value-level counterexample resolves the final composition.

No claim of `Delta m != 0`, impossibility, or kernel-level `False` is made by this report.
