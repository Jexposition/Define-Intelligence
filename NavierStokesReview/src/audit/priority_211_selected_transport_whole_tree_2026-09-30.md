# Priority 211: selected transport whole-tree audit

Date: 2026-09-30
Status: completed source triage; selected-field theorem status unchanged

## Scope

The hardened `selected_transport_audit.py` pass was run over both `NavierStokes/`,
the production Lean source tree, and `NavierStokesReview/src/`, the review-side
probes, completions, extensions, and refutations.

The run indexed 31,831 declaration blocks. It is a declaration-level source
triage, not a theorem prover and not a grep sample. Its conservative rule asks
whether one declaration itself binds a selected-field expression, a moment
operator or payload, a transformation term, and an equality or transport
conclusion. Conditional and obstruction declarations are kept separate.

Machine-readable output:
`NavierStokesReview/evidence/selected_transport_audit_2026-09-30_review_sources.json`

Human-readable output:
`NavierStokesReview/evidence/selected_transport_audit_2026-09-30_review_sources.md`

## Results

The production-only pass over `NavierStokes/` indexed 31,472 declarations and
found zero joint candidates under the rule above. The combined production plus
review-side pass found 11 joint candidates, of which 3 were classified as
manual transport candidates:

1. `SelectedBarMomentInterface.selected_component_barMoment_apply`
   (`SelectedBarMomentInterface.lean:32-45`)
2. `SelectedBarMomentInterface.selected_component_requires_transport_data`
   (`SelectedBarMomentInterface.lean:54-67`)
3. `SelectedPhysicalPointTransport.barMoment_transport_requires_selected_scalar`
   (`SelectedPhysicalPointTransport.lean:28-36`)

These three declarations prove caller-supplied pullback identities. They make
the missing data explicit: a point-to-spacetime map and a scalar profile equal
to a selected potential component. They do not provide the production
`selected_witness` with that data, do not evaluate the completed mixed field,
and do not identify the result with `(M,I,J,S,C_p)`.

The other joint candidates are not positive transport results. They include
the direct-branch order-two zero identity, selected-witness non-entailment
probes, and conditional compatibility or obstruction results.

## What this establishes

The run strengthens the bounded `CTR-005` finding: no production declaration
located by the whole-tree source census supplies the missing final identity
connecting the completed selected Cartesian velocity/pressure/residual/force
construction to `(M,I,J,S,C_p)`. The review-side code shows exactly what a
caller must still provide for a `barMoment` comparison.

This is not an impossibility theorem. It does not prove a nonzero selected
moment defect, force nonsmoothness, literal CMI failure, a compiler escape, or
`False`. It also does not erase the genuine production invariant, residual-rate,
force-extension, and axis blow-up machinery already traced in the selected
route. The correct disposition remains:

> `CTR-005: NOT ESTABLISHED` for complete manuscript-to-selected-endpoint
> correspondence.

## Manual review conclusion

The three positive-looking declarations were inspected directly. Their
mathematical shape is

\[
  \operatorname{barMoment}(\text{pullback}(\phi,g))
  = \int r^k\,\operatorname{torusAverage}(g\circ\phi),
\]

or a direct-branch specialisation. None has the stronger form

\[
  \operatorname{barMoment}(u_{\mathrm{selected}})
  = (M,I,J,S,C_p),
\]

nor does any prove that the production `selected_witness` exports the
point-to-spacetime map, scalar profile, and equality needed to instantiate the
caller-supplied interface.

## Reproducibility and boundaries

- No OpenAI production source file was edited.
- The protected untracked `NavierStokes/R3/TestPressure.lean` was not touched,
  staged, moved, or deleted.
- No generated source-side file was added.
- The audit tool's environment pass was not used for this run; no stale Lean
  environment snapshot is presented as current proof evidence.

## Lean replay of the manual candidates

The first replay attempt used `leanprover/lean4:v4.32.0` against `.olean`
artefacts built by the repository's pinned toolchain. That produced header
incompatibility errors, not theorem failures. The replay was then repeated
with the repository-pinned `leanprover/lean4:v4.34.0-rc2` toolchain.

The three manual candidate files compiled with exit codes `0,0,0` under that
toolchain. This confirms that the review-side interfaces are valid Lean
declarations. It does not upgrade them into a production selected-field
transport theorem: their types still require caller-supplied maps/profiles
and do not conclude the five-observable identity for `selected_witness`.
