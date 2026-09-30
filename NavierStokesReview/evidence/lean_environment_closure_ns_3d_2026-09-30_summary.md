# Lean environment closure summary: Navier--Stokes 3D (2026-09-30)

The current checkout was exported with the pinned toolchain
`leanprover/lean4:v4.34.0-rc2` from
`NavierStokesReview/src/audit/EnvironmentDependencyExportNS.lean`.

| Item | Result |
| --- | ---: |
| Selected roots | 6 |
| Project declarations | 30,919 |
| Declaration edges | 329,127 |
| Missing roots/names | 0 |
| `sorryAx` nodes/names | 0 |

Raw closure:
`lean_environment_closure_ns_3d_2026-09-30.json`

SHA-256:
`91C8F7950D31A5BFF7611CA228FD1303CF5C26F27EB36DFB47C0B305EC7C23F0`

This is endpoint-environment coverage, not a five-moment transport theorem.
The Priority 211 source census still found no production declaration that
connects the selected production field to
`(M,I,J,S,C_p)`. The controlled disposition remains
**CTR-005: NOT ESTABLISHED**. No nonzero defect, impossibility theorem, force
nonsmoothness, literal CMI failure, compiler escape, or `False` is inferred.

See:
`NavierStokesReview/src/audit/priority_212_ns_environment_closure_2026-09-30.md`.
