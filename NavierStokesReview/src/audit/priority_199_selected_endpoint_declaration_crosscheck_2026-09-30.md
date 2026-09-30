# Priority 199: selected-endpoint declaration cross-check

Date: 2026-09-30
Status: source-checked; `CTR-005` retained; no endpoint refutation asserted

## Scope

This tranche rechecks the current raw Lean declarations after the workspace
disposition cleanup. It addresses the recurring apparent contradiction:

1. `Witness` does not visibly contain a named equality
   (operatorname{Moments}(u,p,f)=(M,I,J,S,C_p)).
2. The selected construction nevertheless proves smoothness, residual
   identities, force regularity, and velocity blow-up.

The two statements are compatible because a theorem's result type and the
proof terms used to construct its premises are different layers. The absence
of a named final observable equality is a correspondence limitation. It is
not evidence that the endpoint is empty, that `NativeBounds` was inserted
from thin air, or that the selected field has a proved nonzero defect.

## Raw declaration trace

### 1. Actual physical data reaches the estimate layer

`NavierStokes/ActualCandidateAssembly.lean:1079-1088` defines
`physicalData`. It returns `ActualCycleResidualBounds.PhysicalData` through
`ActualPhysicalPrefixFields.physicalFields_all`, the selected stage
realizations, exterior stages, smoothness proofs, and the cycle
representation. This is an actual physical-data construction, not an
unconstrained `NativeBounds` parameter at the final theorem.

`ActualCandidateAssembly.lean:1090-1098` defines `estimates` by applying
`GluedStageEstimates.actualStageEstimates` to `runData`, mean-cycle input,
signed wave data, coherent cycle state, representations, and
`physicalData`. The endpoint therefore consumes concrete upstream data.

### 2. The residual-rate layer consumes `PhysicalData`

`ActualCycleResidualBounds.lean:1156-1172` defines
`Invariant.residual_jetRate`. Its arguments include

```lean
(d : PhysicalData B N x.state u P)
```

and the proof uses `H.stateRealization`, `selected_residual_jetRate`,
`H.native_residual`, exterior germs, and `base_exterior_jetRate`. This refutes
the wording that `force_smooth` is simply an arbitrary generic rate contract.
The stronger semantic question remains whether these concrete residual-rate
identities are equivalent to the manuscript's complete five-observable
transport argument.

### 3. The force is derived from actual residual limits

`NavierStokes/CandidateFromLimits.lean:45-66` derives
`tracedResidual_smooth` from the actual residual derivative recurrence and
locally uniform limits. `CandidateFromLimits.lean:80-112` defines the force by
smooth extension of that traced residual and proves both smoothness and
agreement with the activated residual on the past domain. Thus the source
does not support the claim that Lean merely assumes force smoothness by
declaring `NativeBounds`.

The remaining audit question is narrower and material: the inspected selected
export does not identify those residual limits and their force extension with
the manuscript's named five cumulative observables. A genuine residual-rate
proof is not automatically a theorem of paper-level observable equivalence.

### 4. The `Witness` contract and its selected projection

`ActualCandidateAssembly.lean:1121-1151` defines `Witness` with:

- a selected stage schedule;
- `ASum`, `BSum`, and `PSum` potential sums;
- away extensions;
- an existential force;
- `CandidateProperties` for the activated velocity, pressure, and force;
- `CandidateConsequences.Consequences`;
- the (H^3)-type blow-up limit;
- all-order force derivative decay; and
- boundary-limit identities.

No conjunct in this definition is a named equality identifying the final
activated Cartesian velocity, pressure, residual, or force with
((M,I,J,S,C_p)). `selected_witness` at
`ActualCandidateAssembly.lean:1177-1181` proves this proposition, and
`selected_candidate` at `1177-1185` projects the force and candidate
properties into `ProblemStatement.candidateStatement`. The endpoint thus
exports a real forced candidate, but not the separate observable-identification
theorem needed to credit the manuscript's full five-moment explanation.

### 5. Blow-up is real in the selected proposition, but local proof scope is not
the whole construction

`GermCandidateAssembly.lean:146-159` proves `origin_blowup` from the selected
axis asymptotic. `GermCandidateAssembly.lean:164-271` then combines finite-stage
data, cut-off divergence, away extensions, and `CandidateConsequences` with
that axis result. Therefore it is incorrect to say that the endpoint has no
blow-up proof merely because the local `origin_blowup` type does not repeat a
five-moment tuple.

It is equally incorrect to infer from that local type that the five-moment
mechanism is dispensable. The whole construction uses upstream correction,
rank, physical-data, residual-rate, and force-extension premises. The raw
source does not establish the counterfactual theorem

\[
\text{remove all moment/rank repair mathematics}
\Longrightarrow
\text{the same selected candidate still exists}.
\]

That counterfactual remains unproved.

### 6. The Fefferman-facing endpoint remains a connected question

`NavierStokes/ProblemStatement.lean:101-122` records smoothness, periodicity,
initial data, force support, incompressibility, the Navier--Stokes residual
identity, and speed unboundedness in `CandidateProperties` and
`candidateStatement`. This is why a literal CMI-shaped forced proposition can
compile and why the current audit must not claim a compiler contradiction.

The paper-to-endpoint question is stronger: whether the selected objects in
that proposition realise the connected manuscript construction, including
the five-moment repair, pressure and stress matching, localisation,
periodisation, infinite summation, residual flatness, and admissibility
conditions. The current source tranche still has not located a theorem that
closes that entire correspondence to the named tuple.

## Adjudication

| Question | Source-supported answer |
| --- | --- |
| Is the selected endpoint empty or based on free `NativeBounds`? | No. Concrete physical data and residual-rate proofs feed the endpoint. |
| Does the local axis blow-up proof prove the whole paper independently of moments? | No. It proves one conjunct through the axis route; it does not prove constructional independence. |
| Does `Witness` export the paper's final five-observable identity? | Not in the inspected declaration. |
| Does that omission prove a wrong selected integral or force nonsmoothness? | No. Those require a field-level mismatch or a failed smoothness theorem. |
| Is complete paper-to-selected-endpoint correspondence established? | No. `CTR-005: NOT ESTABLISHED` remains the controlled status. |
| Was a compiler escape or kernel contradiction found? | No. None is asserted by this tranche. |

## Evidence links

- `NavierStokesReview/evidence/selected_endpoint_compile_boundary_reaudit_2026-09-29.md`
- `NavierStokesReview/src/audit/priority_198_latest_rebuttal_adjudication_2026-09-30.md`
- `NavierStokesReview/src/audit/priority_193_fefferman_semantic_branch_network_2026-09-30.md`
- `docs/SEMANTIC_CORRESPONDENCE_MAP.md`
