# Priority 212: live Navier--Stokes environment closure (2026-09-30)

## Purpose

This tranche rebuilds the Lean declaration environment for the selected
Navier--Stokes roots from the current checkout. It is a coverage and replay
record. It is not itself a proof of five-observable transport.

The exporter is
`NavierStokesReview/src/audit/EnvironmentDependencyExportNS.lean`.
It was compiled with:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean \
  NavierStokesReview/src/audit/EnvironmentDependencyExportNS.lean
```

## Roots and result

The exporter loaded these six declarations:

1. `NavierStokesR3.theorem_1_1`
2. `NavierStokesR3.theorem_1_1_with_initial_rest`
3. `NavierStokesR3.theorem_1_1_with_dissipation`
4. `NavierStokes.ActualCandidateAssembly.selected_witness`
5. `NavierStokes.ComparatorBridge.navier_stokes_breakdown_R3`
6. `NavierStokes.PeriodicPaper.periodic_corollary`

The live export reported:

| Measure | Result |
| --- | ---: |
| Project declarations exported | 30,919 |
| Declaration edges exported | 329,127 |
| Missing root names | 0 |
| Missing declaration names | 0 |
| `sorryAx` nodes | 0 |
| `sorryAx` names | 0 |

Raw output:
`NavierStokesReview/evidence/lean_environment_closure_ns_3d_2026-09-30.json`

Raw output SHA-256:
`91C8F7950D31A5BFF7611CA228FD1303CF5C26F27EB36DFB47C0B305EC7C23F`

The raw JSON is a generated, 366,297,217-byte closure artefact. The scoped
audit commit records this report, the exporter, and the digest rather than
blindly adding the large generated graph to the public branch.

## What this establishes

The current environment can resolve the selected Navier--Stokes endpoint
roots and contains no `sorryAx` node in the exported declaration graph. This
removes the earlier stale-environment limitation for these six roots.

The result also confirms that the endpoint is not an isolated empty shell:
the live environment contains the substantial declaration graph used by the
selected construction.

## What this does not establish

This closure does not prove that the selected Cartesian fields satisfy

\[
  \operatorname{barMoment}(u_{\mathrm{selected}})
    = (M,I,J,S,C_p),
\]

or any equivalent paper-level transport identity. The Priority 211 source
census remains the semantic result: production declarations yielded no
positive selected-field transport declaration under the conservative joint
rule, while three review-side candidates were caller-supplied interfaces and
did not instantiate `selected_witness`.

Consequently the controlled disposition remains:

> **CTR-005: NOT ESTABLISHED** for complete manuscript-to-selected-endpoint
> correspondence.

This record does **not** claim a selected-field nonzero defect, an
impossibility theorem, force nonsmoothness, literal CMI failure, a compiler
escape, or `False`. Those stronger outcomes require a connected value-level
countertheorem or a complete positive bridge, neither of which is supplied by
an environment closure.

## Separate Euler build limitation

The all-public `EnvironmentDependencyExport.lean` also exposes Euler roots,
but the current checkout did not have the required Euler root `.olean` files.
Two bounded `lake build Euler` attempts produced intermediate artefacts but
did not produce the required root modules before the processes were stopped.
That is an environment/build limitation only. It is kept separate from this
successful six-root Navier--Stokes closure and is not evidence about the
Navier--Stokes theorem.

## Process and source boundaries

- No OpenAI production source file was edited.
- `NavierStokes/R3/TestPressure.lean` was not touched, staged, moved, or
  deleted.
- The identified orphan Lean/Lake/Python processes from timed-out probes were
  stopped; no relevant process remained after the final check.
- This tranche changes coverage evidence and tooling only. It does not change
  the scientific disposition or open the archive gate.
