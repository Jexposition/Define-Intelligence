# Priority 209 audit: scope and index reconciliation

The current root-explicit source replay found 2,797 Lean files in the
checkout, 817 below `NavierStokes/`, 137 below `NavierStokesReview/`, and 588
modules in the selected endpoint import closure. The previous 2,794-row
register omitted three newer review-side files and included the protected
`NavierStokes/R3/TestPressure.lean`; the regenerated register now covers all
2,797 current Lean paths.

The 588 modules are reachable only from the selected audit roots. The 2,209
outside rows are not labelled dead or unreachable in OpenAI's repository; they
are outside this captured closure. This distinction is now explicit in the
current register and controlling documentation.

The lexical `sorry_token` count is 10, while seven rows carry the
`source_indexed_sorry_token` status. The remaining three lexical rows are
already `evidence_inspected`, so `10 = 7 + 3`. This is a status-accounting
difference, not a contradiction.

The scientific result is unchanged: genuine selected internal invariant and
residual/force/blow-up machinery is present, but the inspected production
closure still has no located final identity connecting the completed selected
Cartesian observables to `(M,I,J,S,C_p)`. `CTR-005` remains
`NOT ESTABLISHED`; no selected defect, force nonsmoothness, literal CMI
failure, impossibility theorem, compiler escape, or `False` is claimed.

Evidence: `../evidence/priority_209_scope_and_index_reconciliation_2026-09-30.md`
and its JSON companion.
