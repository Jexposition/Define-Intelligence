# Final claim classification: OpenAI Navier–Stokes result

Date: 2026-09-22
Audited source commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

## Binary answer

| Claim being tested | Answer | Reason |
|---|---|---|
| Did the audited Lean development prove its exported forced CMI Alternative C/D theorem? | **Yes, formally.** | The exported theorem has the CMI existential data and same-force negated global-solution conclusion. Independent axiom probes report only `propext`, `Classical.choice`, and `Quot.sound`; no project axiom or `sorryAx` reaches the audited exports. |
| Did it prove global regularity failure for the usual unforced Navier–Stokes problem? | **No.** | The witness uses an existential smooth external force. That is allowed by CMI Alternatives C and D, but it is not the unforced Millennium claim. |
| Has this review certified every analytic argument in the 166-page paper? | **No.** | The formal proof is strong evidence, but a complete independent line-by-line continuum-PDE review of every construction certificate remains separate from Lean kernel checking. |

## Interpretation

The force is defined from the candidate residual. That is not a CMI defect by
itself: the official CMI alternatives explicitly allow a smooth external force.
The correct criticism is therefore not “forcing automatically invalidates the
result”. The correct boundary is that the result is a forced counterexample,
not a proof of blow-up for arbitrary unforced initial data.

The audit found no confirmed formal counterexample in the CMI bridge,
whole-space pressure comparison, viscosity scaling, support/decay map, or
selected endpoint. It did find a generic `JetRate` API hazard because a bound
over the bottom filter is vacuous; the selected endpoint itself was separately
proved nontrivial, so that finding is not a disproof of the exported theorem.

## Final disposition

For the claim as OpenAI formally stated it, the answer is **YES at the Lean
formal-theorem level for C/D**. For the broader claim “the unforced 3D
Navier–Stokes problem is solved”, the answer is **NO**. Human mathematical
peer review should therefore evaluate the paper as a forced CMI-alternative
construction, not as an unforced regularity proof.
