# Priority 128: adversarial probe-contract review

## Purpose

The earlier transport search was hardened for source provenance, but that does
not by itself prove that the review probes make only the inference their Lean
statements support. This pass audits the review-authored declarations for the
opposite blindside: over-reading a valid local theorem as a theorem about the
selected endpoint.

The instrument is
`NavierStokesReview/src/audit/probe_logic_contract_audit.py`. It is a static
contract audit, not a substitute for Lean elaboration or kernel checking.

## Current machine result

The instrument reviewed **262 declarations** under `NavierStokesReview/src`:

| Measure | Result | Interpretation |
| --- | ---: | --- |
| Selected-term declarations | 91 | A selected-looking symbol occurs in the declaration window. This is not transport. |
| Explicit premise-marker declarations | 20 | These require direct premise tracing before their conclusions can be applied. |
| Strong-conclusion-marker declarations | 88 | These contain `False`, inequality, negation, obstruction, or similar syntax. They are not automatically unconditional. |
| Unconditional endpoint claims authorised | 0 | The audit deliberately authorises none. |

The machine-readable result is
`NavierStokesReview/evidence/probe_logic_contract_audit_2026-09-28.json`,
with the human-readable matrix in the same directory as `.md`.

## Scope classes that must not be conflated

| Scope | What it can establish | What it cannot establish |
| --- | --- | --- |
| `interface_level` | A generic interface does not determine a payload; a zero countermodel is admissible. | The concrete selected field has that countermodel or wrong moments. |
| `type_boundary_or_ghost_payload` | The exported proposition can coexist with an externally supplied nonzero `Debt` because that payload is not a field of the proposition. | The ghost `Debt` equals a physical moment of the selected field. |
| `conditional_conclusion` | A contradiction follows if the named support, positivity, transport, or nonzero premises hold. | Those premises hold for the selected branch. |
| `fixed_force_path_dependence` | A specified admissible perturbation changes the residual when the force is fixed. | The literal existential CMI alternative is false. |
| `review_completion_identity` | A review-side finite-prefix, pointwise, or local identity has been stated/proved in its own module. | The declaration is an OpenAI source theorem or a global `tsum`/radial-observable theorem. |
| `requires_manual_scope_review` | The declaration needs direct inspection. | Lexical markers alone do not determine its mathematical scope. |

## Probe-specific adversarial checks

1. `StageEstimatesMomentBlindnessProbe` is an interface countermodel. It must
   never be cited as evidence that the concrete selected velocity is zero or
   that its physical moments are arbitrary.
2. `SelectedEndpointMomentTransportObstruction` uses an externally supplied
   `Debt`. It diagnoses a missing field in `Witness`; it does not calculate a
   selected-field integral.
3. `CompactFixedForcePerturbation` proves a fixed-force residual defect for a
   constructed perturbation. It establishes path dependence, not negation of
   an existential force statement.
4. `SelectedPeriodicSupportTransportGate` is a conditional gate. Its support
   and nonvanishing hypotheses must be derived from the selected field before
   it can produce `False`.
5. Selected finite-prefix completions expose real curl, cutoff commutator,
   radial-reduction, and torus-average identities. They still require a
   finite-prefix-to-`tsum` theorem, integration-domain control, and the
   five-observable comparison.

## Mandatory escalation contract

No probe may be promoted to a selected-field contradiction unless all of the
following are present:

1. the declaration is compiled in the exact current Lean environment;
2. the source path is identified as OpenAI source or explicitly labelled
   review completion;
3. the selected expression is the actual exported field, not a ghost payload,
   generic interface, or renamed proxy;
4. every premise is traced to the selected construction;
5. the conclusion is a concrete tuple equality, a concrete nonzero defect, or
   `False` with no uninstantiated assumptions;
6. for an integrated defect, convergence, interchange, periodisation, axis,
   and whole-space domain obligations are discharged.

Numerical work has the same provenance rule. A synthetic one-dimensional
profile, even with CUDA, high resolution, or a convergence plot, is not a
measurement of `selected_witness`. A numerical result may be used as a sanity
check only unless its inputs are generated from the exact selected three-
dimensional definitions and its discretisation, truncation, radial-domain,
periodisation, and summation errors are independently bounded.

The current environment is not available for this final promotion: the fresh
endpoint export is blocked by the missing
`.lake/build/lib/lean/NavierStokes/R3/Theorem.olean`, and the follow-up build
timed out before producing it. Therefore this review records a strengthened
anti-blindside method, not a new mathematical verdict.

## Controlled conclusion

The probe suite is not being treated as a free-standing refutation. It now
has explicit scope classes and a machine-generated contract matrix that makes
the known inference failures visible. The live status remains:

\[
\text{selected-field five-observable transport} = \text{not established},
\]

with no promoted `\Delta m \ne 0`, impossibility theorem, `False`, or formal
refutation.
