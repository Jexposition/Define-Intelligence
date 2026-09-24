# Burden-of-proof and underclaim audit

**Date:** 2026-09-24  
**Scope:** the published OpenAI Navier–Stokes claim, its paper, and the
selected Lean endpoint

## Review standard

The authors bear the burden of establishing the claim they publish. A
reviewer does not have to prove the negation of an existential proposition in
order to withhold acceptance of a stronger paper claim. The relevant
distinction is:

1. **Endpoint proposition:** what the exported Lean theorem actually states.
2. **Selected construction:** whether the selected fields satisfy the analytic
   and PDE premises used by that theorem.
3. **Paper claim:** whether those fields are the five-moment construction and
   physical interpretation described in the paper.
4. **CMI claim:** whether the construction establishes one of Fefferman's
   alternatives under the official problem statement.

These are not interchangeable propositions.

## Load-bearing obligations not discharged in the inspected corpus

| Obligation | Source observation | Consequence |
|---|---|---|
| Identify the paper tuple `$(M,I,J,S,C_p)$` with the selected fields | `ActualCandidateAssembly.Witness` exports no equality to `PositiveOrderMoments.moments`, `FiveProfileMoments.physicalMoments`, `FiveRowRank.FiveRows`, or the paper tuple | The paper's advertised five-moment construction is not established for the exported candidate. |
| Carry that identity into the residual and force | `CandidateProperties` records the residual identity, but `Witness` does not expose the missing moment-to-residual transport theorem | The selected endpoint cannot by itself certify the paper's stated mechanism. |
| Establish the analytic premises for the same selected fields | The endpoint consumes residual-jet, extension, comparison, energy, and blow-up data, but no single exported composition theorem identifies all of them with the paper's construction | The authors must provide the source-linked composition proof. |
| Justify “given, externally applied force” | The formal candidate predicate contains smoothness, support, residual, energy, and blow-up conditions, but no independence or prescribed-data predicate | Residual provenance is a substantive admissibility objection to the paper's interpretation, not by itself a Lean `False`. |

## Finding

The affirmative review conclusion is:

> The published CMI-level claim is **not established by the inspected
> paper-to-code record**, because the authors have not discharged the
> selected-field correspondence and analytic composition obligations required
> to identify the formal endpoint with the construction described in the
> paper.

The review is **not** claiming that the current source audit has proved
`False` from `selected_witness`. The absence of that contradiction reports
only the state of the current Lean refutation search. It does not supply the
missing bridge, validate the paper's stronger interpretation, or transfer the
burden of proof to the reviewer. The negative review conclusion is already
justified by the authors' failure to establish the affirmative composition
theorem required by the stronger claim.

## Role of the zero-sorry probes

- `StageEstimatesMomentBlindnessProbe.lean` shows that the generic rate
  contract does not determine an arbitrary five-moment certificate.
- `FiveRowPositiveOrderBridgeProbe.lean` shows an algebraic promotion and
  repair identity, but not selected-field transport.
- `SelectedLabelConstructionProbe.lean` closes the selected-label vacuity
  route and prevents an empty-set argument from carrying the verdict.
- `SelectedForceOriginCompositionProbe.lean` closes the simple force-explosion
  route at the origin, rather than validating the complete CMI claim.
- `GlobalTransportBridgeProbe.lean` shows that global consequences can coexist
  with a review-side fixed-force stability obstruction; it does not add a
  force-independence predicate to the endpoint.

These results narrow the review and strengthen the burden-of-proof finding.
They do not reverse it.

## Required author response

Acceptance of the broader published claim requires a theorem, or a chain of
theorems with an explicit composition statement, that starts from the actual
selected fields and establishes the five named moments, their transport
through the correction and germ construction, their use in the residual and
force estimates, and the advertised CMI interpretation. Until that record is
provided, the appropriate status is **not established**, irrespective of the
fact that the exported endpoint compiles.
