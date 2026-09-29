# Priority 117: periodic versus compact selected-field identity review

**Date:** 2026-09-28
**Status:** source-grounded separation of fields; no contradiction asserted

## Question

Can the compact-support theorem for the R3 candidate be applied directly to
the periodic radial pullback used by the new `barMoment` probes?

## Source facts

1. `NavierStokes/R3CompactCandidate.lean:201-209` defines two different
   velocity expressions:

   - `velocity A B`, built from `cutVelocity` and `cutPotential`;
   - `periodicVelocity A B`, built from `SpatialLocalization.periodicVelocity`
     and `PeriodicLocalization.periodize`.

2. `NavierStokes/R3CompactCandidate.lean:214-222` proves support only for
   `velocity A B`, outside `SpatialLocalization.supportCylinder`.

3. `NavierStokes/R3CompactCandidate.lean:231-238` proves only an eventual
   neighbourhood equality between `periodicVelocity A B` and `velocity A B`
   at points inside `PeriodicLocalization.innerCube (1/4)`.

4. `NavierStokes/R3CompactCandidate.lean:248-252` transfers periodic candidate
   properties to the compact field through `of_periodic_local_model`; it does
   not state a global equality between the periodic and compact velocity
   functions.

5. `NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean:31-35`
   defines the selected mixed scalar from `MixedPeriodicAssembly.periodicVelocity`.
   Therefore the current radial pullback is a periodic-field observable.

6. `NavierStokesReview/src/completions/SelectedMixedRadialPeriodicity.lean:28-73`
   proves period-one behaviour in the radial Cartesian coordinate. This is a
   genuine property of the selected periodic field, not a support statement.

7. `NavierStokesReview/src/completions/SelectedMixedRadialSupportObstruction.lean:38-47`
   proves that period-one plus an explicit `RadiallySupported` premise forces
   the selected pullback to vanish. The support premise is not exported by the
   current endpoint.

## Logic result

The existing gate in
`NavierStokesReview/src/refutations/SelectedPeriodicSupportTransportGate.lean`
is correctly conditional. It cannot be strengthened to a selected-path
contradiction merely by combining:

\[
\operatorname{supp}(u_{\mathrm{R3}})\subset K
\quad\text{and}\quad
u_{\mathrm{periodic}}=u_{\mathrm{R3}}
\text{ locally on an inner cube}.
\]

The missing implication would have to transport both the field identity and
the support statement to the exact pullback
`selectedMixedRadialPullback`. Local equality on an inner cube is insufficient
for a global support predicate, and periodisation can contribute translated
copies outside the compact representative.

## What this rules out

- It rules out the earlier shortcut “R3 compact support immediately gives
  bounded radial support for the selected periodic pullback”.
- It rules out treating the current periodic-support gate as a proof of
  `False`.
- It does not show that the selected pullback is nonzero, nor that its global
  moment differs from an upstream profile moment.

## Required next source test

Trace the concrete selected `A`, `B`, and `P` through
`ActualCandidateAssembly.selected_witness`, and search for a theorem with the
global type needed to rewrite the selected periodic pullback to the compact
R3 field at every radial point. If no such theorem exists, record that as a
correspondence gap. Do not replace it with local eventual equality.

## Verification boundary

This report is based on direct source declarations and line ranges. A direct
check of the new file was attempted with the repository toolchain
`leanprover/lean4:v4.34.0-rc2`. It stopped before theorem elaboration because
the imported review object
`.lake/build/lib/lean/completions/SelectedMixedRadialSupportObstruction.olean`
does not exist. The earlier package rebuild under the same toolchain timed out
during dependency reconstruction. Therefore this gate is source-reviewed but
not compiler-verified in this workspace; no compiler result is inferred from
the source inspection.

## Source-wide symbol cross-check

A source search over `NavierStokesReview/src` and `NavierStokes` was performed
for the exact selected pullback, radial-support predicates, and compact versus
periodic velocity identities. The selected pullback occurs in its definition,
its periodicity/support obstruction, the periodic-integral diagnostics, and
the `barMoment` reductions. The repository source contains the compact-field
theorems `R3CompactCandidate.velocity_supported` and
`R3CompactCandidate.velocity_locally_eq`, but the search did not find a
theorem whose conclusion directly supplies
`RadiallySupported α β (selectedMixedRadialPullback a)` from the compact field
support. The only such implication currently present is the conditional
premise of the new gate itself.

This is a scoped source-search result, not a proof that no theorem can ever be
added and not a proof that the selected pullback is nonzero. It establishes the
next exact obligation: either locate a global compact-to-periodic support
transport theorem missed by the search, or formalise the nonzero selected
pullback and show that the required support premise is false or unavailable.

The gate now also contains `selected_witness_schedule_support_gate`. This
destructs the actual exported `selected_witness` to bind its schedule `a`, then
applies the same two explicit premises to that schedule. It closes a smaller
logic gap in the first version of the probe: the conditional theorem is no
longer only parameterised by an arbitrary schedule. The universal support and
nonzero assumptions in this schedule-level theorem are still not supplied by
the endpoint.
