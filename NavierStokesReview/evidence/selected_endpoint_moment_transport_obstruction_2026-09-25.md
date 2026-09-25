# Selected-endpoint moment transport obstruction

**Date:** 2026-09-25

**Scope:** selected `ActualCandidateAssembly.Witness` interface
**Classification:** proved interface non-implication; not a `False` theorem

## Question

Does the selected exported witness itself determine the five-coordinate debt
or moment payload used in the paper's $(M,I,J,S,C_p)$ argument?

## Source trace

`NavierStokes/ActualCandidateAssembly.lean:1079-1087` proves `physicalData`
for the actual finite-stage fields. `:1090-1098` feeds that record into the
stage estimates. `:1121-1151` defines `Witness`; its fields are the selected
schedule, three assembled sums, away extensions, a force, `CandidateProperties`,
force smoothness, `CandidateConsequences`, H3 growth, force-jet decay, and
endpoint boundary jets. The definition contains no `Debt`,
`PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`,
`FiveRowRank.FiveRows`, or equality to $(M,I,J,S,C_p)$. `:1177-1181` proves
the selected witness by instantiating this contract.

The positive upstream formulae remain real: `PositiveOrderMoments.lean:76-85`
defines the five row densities and `moments`. This evidence therefore tests
their selected export, not their existence upstream.

## Zero-sorry result

`NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
defines

```lean
def witnessDebt : Debt := fun _ => 1

theorem selected_witness_compatible_with_nonzero_five_payload :
    ∃ d : Debt, d ≠ 0 ∧
      Witness selectedBudget selectedThreshold selectedThreshold_geometry
```

and proves it using the actual `selected_witness`. It also proves that the
selected witness does not entail `∀ d : Debt, d = 0`. The module was compiled
directly with the pinned Lean 4.34.0-rc2 toolchain and contains no `sorry`,
`axiom`, or `unsafe` declaration.

## Interpretation

The theorem is a precise non-implication: the exported witness does not
certify the paper's five-moment transport. It does **not** prove that the
selected velocity has incorrect integrals. A contradiction would require a
further source theorem equating the selected mixed fields with the named
moment functions and then proving one of those equalities false.

The publication-level consequence is nevertheless decisive for the present
counter-paper: because OpenAI presents the five-moment construction as part
of its solution, the missing selected-field composition theorem leaves the
advertised solution claim **NOT ESTABLISHED** on the inspected record.
