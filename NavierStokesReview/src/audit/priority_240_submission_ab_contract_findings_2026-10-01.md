# Priority 240: Submission A/B contract findings

Date: 2026-10-01

## Scope

This is the first source-backed result from the September 8 versus September
10 differential. It compares the old public declarations at `8937a8f4` with
the current declarations at `f9e8bc5`. It is deliberately narrower than a
proof-term closure: it records contract changes directly visible in the two
source snapshots.

## Established source facts

### C route

Submission A's `NavierStokes/ComparatorR3Theorem.lean` proves
`navier_stokes_breakdown_R3` by obtaining
`R3CompactCandidate.selected_compact_candidate` and applying
`option_C_of_compact_candidate`.

Submission B's current `NavierStokes/ComparatorR3Theorem.lean` obtains the
selected data from `NavierStokesR3.theorem_1_1` and applies
`NavierStokesR3.comparator_of_breakdown`. The old compact-candidate route is
still present as a declaration, so this is a route change, not evidence that
the old route was deleted or refuted.

### D route

Submission A's `NavierStokes/ComparatorTheorem.lean` obtains
`ActualCandidateAssembly.selected_candidate` and applies
`option_D_of_candidate`.

Submission B's `NavierStokes/PeriodicPaperTheorem.lean` exports
`periodic_corollary`, while `PeriodicPaperComparator.lean` provides the
paper-facing same-force adapter. This establishes a changed advertised route;
it does not yet establish that the A and B witnesses are definitionally or
extensionally identical.

### Candidate contract strengthening

Submission A's `NavierStokes/R3CompactCandidate.lean:24` `Properties` record
contains smoothness, support, residual, incompressibility, initial data, and
speed-unboundedness fields. Its force smoothness field is
`ContDiffOn ℝ ∞ f futureDomain`; the inspected record has no explicit
`UniformFiniteEnergy (Ico 0 1) u` field.

Submission B's `NavierStokes/R3/ProblemStatement.lean:92-108`
`CandidateProperties` contains:

\[
\texttt{energy\_bounded : UniformFiniteEnergy (Ico\ 0\ 1)\ u},
\]

and uses global `ContDiff ℝ ∞ f` together with
`CompactPositiveTimeSupport f`. The `Ico 0 1` interval is the pre-singular
domain \(0\leq t<1\), not an all-time energy claim.

This is a verified contract-level strengthening in B. It does not by itself
show that A's route was mathematically invalid: A may have proved related facts
elsewhere, or B may be a paper-facing aggregation. The next required step is
to trace the exact A proof term and determine whether the stronger facts were
already derivable from A's selected object.

### Comparator class edge

The independent review probe
`src/probes/CMIComparatorClassInclusionProbe.lean` compiles with exit 0 and
re-establishes only:

\[
\text{Comparator solution class}
\longrightarrow
\text{R3 GlobalFiniteEnergySolution class}.
\]

This one-way inclusion supports the nonexistence transfer used by the
comparator bridge. It does not prove reverse inclusion, equivalence with every
semantic reading of Fefferman's class, or complete paper correspondence.

## Status table

| Question | Current disposition |
|---|---|
| Was pre-singularity candidate energy explicit in A's old R3 contract? | Not in the inspected `Properties` record; other A declarations still require tracing. |
| Did B strengthen force regularity/support at the contract boundary? | Yes: `ContDiffOn` future-domain force became global `ContDiff` plus compact positive-time support in the R3 candidate contract. |
| Did B prove A false? | No. Not established. |
| Are A and B selected fields the same? | Not yet determined. |
| Is the comparator-to-R3 class inclusion proved? | Yes, one-way; independently compiled. |
| Does this resolve `CTR-005`? | No. `CTR-005` remains `NOT ESTABLISHED`; the selected five-observable bridge still needs its own end-to-end audit. |

## Next work

1. Extract declaration-level proof-term closures for A and B C/D endpoints.
2. Compare the actual witness tuples \((u^\circ,u,p,f)\), not only record names.
3. Trace whether A's force regularity, energy, integrability, and uniqueness
   premises are independently available before B's aggregation layer.
4. Continue the selected-field, five-moment, residual-jet, pressure,
   limit/interchange, and mutation lanes in parallel.

Evidence: `evidence/priority_240_submission_ab_contract_findings_2026-10-01.json`.
