# Priority 210 audit: selected-endpoint probe replay

The selected review probes were replayed after compiling the missing
`NavierStokes.LocalScheduleWitness` project closure with the repository's
`direct_lean_closure.py` utility. All four endpoint/path probes and the axiom
checkpoint exited successfully under `leanprover/lean4:v4.34.0-rc2`.

The replay strengthens the audit record in two directions at once. It
confirms that the selected construction has genuine residual, force, R3, and
axis-blow-up composition. It also confirms that the public `Witness` contract
does not display a final selected-field equality with `(M,I,J,S,C_p)`.

This is a bounded correspondence finding, not a selected-field defect. The
abstract nonzero-`Debt` result in `SelectedWitnessPathProbe` demonstrates that
the endpoint proposition does not entail an arbitrary five-debt parameter is
zero; it does not identify that parameter with a physical integral of the
selected field. The residual probe similarly does not prove that a residual
term diverges. It records the missing extra lower-bound premise needed for
that stronger argument.

`SelectedDependencyAxiomProbe` reports only `propext`, `Classical.choice`,
and `Quot.sound` for the inspected declarations. That axiom result is
foundational hygiene, not proof of paper-to-endpoint semantic identity.

Controlled disposition: `CTR-005` remains `NOT ESTABLISHED`. No selected
defect, force nonsmoothness, literal CMI failure, impossibility theorem,
compiler escape, or `False` is claimed.

Evidence: `../evidence/priority_210_selected_endpoint_probe_replay_2026-09-30.md`.
