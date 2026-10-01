# Priority 227: selected periodic-support gate replay

Date: 2026-10-01
Status: source-checked and compiler-verified; premises remain open
Scientific disposition: `CTR-005: NOT ESTABLISHED`

## Purpose

This replay follows the active P2 task after the workspace corpus
re-grounding. It checks the existing review-side contradiction gate against
the actual selected periodic field, rather than treating the compact R3
support theorem as if it automatically applied after periodisation.

## Exact gate proved

`NavierStokesReview/src/refutations/SelectedPeriodicSupportTransportGate.lean`
proves, for the exact selected mixed radial pullback,

\[
\begin{aligned}
&\operatorname{RadiallySupported}_{[\alpha,\beta]}(g_a)
\land \exists(r,p),\;g_a(r,p)\ne0\\
&\qquad\Longrightarrow\bot,
\end{aligned}
\]

where `g_a` is `selectedMixedRadialPullback a`. The proof is not an abstract
debt countermodel: it uses the selected pullback and its proved unit radial
periodicity. The periodic-support lemma first forces `g_a` to vanish at every
radial point, then contradicts the explicit nonzero premise.

The schedule-level theorem in the same file destructs the repository's own
`ActualCandidateAssembly.selected_witness` and binds the gate to its selected
schedule. It still leaves the support and nonzero assumptions explicit.

## Source facts checked

1. `MixedPeriodicAssembly.periodicVelocity` is the periodised mixed field. It
   is not definitionally the compact R3 field.
2. `R3CompactCandidate.velocity` and
   `R3CompactCandidate.periodicVelocity` are distinct definitions
   (`NavierStokes/R3CompactCandidate.lean:201-212`).
3. Compact support is proved for the compact representative, while the source
   only proves local/eventual equality between periodic and compact fields in
   the inner cube (`R3CompactCandidate.lean:214-238`).
4. The selected scalar used by the review pullback is the first component of
   `MixedPeriodicAssembly.periodicVelocity` after the selected potential and
   direct sums (`SelectedMixedProductionRadialComponent.lean:26-44`).
5. The review has proved the exact unit-period radial pullback identity
   (`SelectedMixedRadialPeriodicity.lean:28-73`).
6. The selected speed blow-up route is genuine, but it is a norm statement
   for the full velocity (`MixedPeriodicAssembly.lean:322-334` and
   `LocalScheduleWitness.lean:110-118`). It does not by itself prove that the
   first-component radial pullback is nonzero at a specified point.
7. The selected angular-growth result gives a first-component asymptotic for a
   related raw/local field (`LocalAngularGrowth.lean:180-228`). Transporting
   that nonzero value to the exact periodised radial pullback still requires a
   pointwise equality with the correct time, radial section, cutoff plateau,
   and activation hypotheses.

8. `completions/SelectedRawVelocityNonzero.lean` now compiles a narrower
   selected-path result: the selected schedule has a spacetime point at which
   the full raw mixed velocity is nonzero. This closes the weaker norm-to-value
   step for the raw field, but it does not identify the nonzero component with
   the first-component periodised radial pullback used by the gate.

## Compiler record

The following file compiled with exit code 0 under
`leanprover/lean4:v4.34.0-rc2`:

```text
NavierStokesReview/src/refutations/SelectedPeriodicSupportTransportGate.lean
```

The following narrower completion also compiled with exit code 0:

```text
NavierStokesReview/src/completions/SelectedRawVelocityNonzero.lean
```

No `sorry`, `admit`, or new axiom was introduced. No Lean, Lake, Elan, or
Python process remained after the check.

## What this establishes

The gate is now a verified, selected-field conditional obstruction. It rules
out silently combining:

\[
\text{compact support of the R3 representative}
\quad+\quad
\text{local periodic/compact equality}
\]

as if they implied bounded radial support of the global selected periodic
pullback.

It does not establish either of the following:

- `RadiallySupported α β selectedMixedRadialPullback a`;
- `∃ r p, selectedMixedRadialPullback a (r,p) ≠ 0`.

Consequently it does not yet prove a selected contradiction, a nonzero
five-moment defect, force nonsmoothness, literal Fefferman-CMI failure, or
`False`.

## Next value-level test

Attempt the missing nonzero transport directly from the proved angular-growth
route. The test must establish equality to the exact periodised first
component on one radial section; it must not substitute the compact field,
the raw field, or an abstract norm blow-up theorem. If that equality is not
derivable, record the mismatch as an additional correspondence obstruction
rather than asserting a nonzero selected moment.

## Evidence links

- `../refutations/SelectedPeriodicSupportTransportGate.lean`
- `../completions/SelectedMixedRadialSupportObstruction.lean`
- `../completions/SelectedMixedRadialPeriodicity.lean`
- `../../evidence/selected_mixed_barmoment_shell_gate_2026-10-01.md`
- `priority_117_periodic_compact_field_identity_review_2026-09-28.md`
- `priority_225_selected_mixed_barmoment_shell_gate_2026-10-01.md`

## Axis component check

The completion
`NavierStokesReview/src/completions/SelectedMixedRadialAxisZero.lean` compiles
with exit code 0 under `leanprover/lean4:v4.34.0-rc2`. It proves

\[
\exists a\;[\mathrm{Selected}(a)\land
  \forall^{\mathrm{eventually}}_{t\to1^-},
  g_a(0,(1-t,0))=0],
\]

for the exact selected radial pullback `g_a`. This is a correction to the
invalid inference \(\|u(t,0)\|\to\infty\Rightarrow g_a(0,(1-t,0))\ne0\):
the source asymptotic is in `coordinateVector 2`, whereas `g_a` samples
component `1`.

The result does not prove global vanishing, bounded radial support, an off-axis
nonzero value, or a five-moment defect. The next value-level test must
transport the selected angular-growth route to the exact periodised
first-component radial pullback off-axis. `CTR-005` remains unchanged.
