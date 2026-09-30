# Evidence record: selected-path probe replay

Date: 2026-10-01

Under the repository-pinned `leanprover/lean4:v4.34.0-rc2` toolchain, these
three files all returned exit code 0:

- `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
- `NavierStokesReview/src/probes/SelectedWitnessPathProbe.lean`
- `NavierStokesReview/src/probes/GlobalTransportBridgeProbe.lean`

A lexical scan found no `sorry`, `admit`, or `axiom` token in any of the three
probe files.

The replay validates the stated review probes. The abstract nonzero `Debt`
payload remains a type-boundary diagnostic, not a claim about the actual
selected physical integrals. The fixed-force result remains a provenance
objection, not a contradiction of the literal existential forced comparator.

Current disposition:

> `CTR-005: NOT ESTABLISHED` for complete paper-to-selected-endpoint fidelity.

Audit companion:
`NavierStokesReview/src/audit/priority_222_selected_probe_replay_2026-10-01.md`.
