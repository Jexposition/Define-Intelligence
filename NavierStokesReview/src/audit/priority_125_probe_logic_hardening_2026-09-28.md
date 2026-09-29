# Priority 125: hardened selected-transport probe logic

## Purpose

This audit closes a methodological failure mode: a declaration can mention a
selected symbol, a moment operator, and an equality without proving the
paper-level transport statement. The instrument therefore separates source
triage, exact environment types, conditional gates, interface countermodels,
and positive declarations that require manual Lean review.

The source pass is repository-wide. It scans all `.lean` declarations under
the repository source root, removes nested Lean comments before interpreting
terms, and reports only declarations whose code contains relevant selected
field/moment vocabulary. It is not a sample and it is not an absence proof.

## Current machine output

The hardened pass over the repository recorded:

| Measure | Result | Meaning |
|---|---:|---|
| Source declarations indexed | 34,583 | Declaration windows considered after repository-wide source traversal. The parser now accepts attributes and instances and strips nested comments before classification. |
| Joint candidates | 11 | Same declaration contains selected-field and moment vocabulary plus an equality-like term. |
| Positive manual-review candidates | 3 | Declarations also contain a selected component, radial/toroidal transform term, and equality; they are review targets, not proofs. |
| Joint candidates by origin | 8 source / 3 review | The three review-side candidates are auditor-authored completion declarations, not OpenAI source declarations. |
| Positive manual candidates by origin | 0 source / 3 review | No OpenAI `NavierStokes/` declaration was promoted by this detector to a positive manual transport candidate. This is triage, not an absence theorem. |
| Environment declarations reported | 0 current | The supplied snapshot is missing both configured endpoint roots; the fresh Lean export also failed because `NavierStokes/R3/Theorem.olean` is absent. |
| Selected transport proved | No | The instrument deliberately does not promote lexical evidence to a theorem. |
| Selected transport disproved | No | No concrete nonzero defect or impossibility theorem was established by this pass. |
| `Delta m != 0` proved | No | No numerical or symbolic defect result is being smuggled into the audit. |
| Kernel `False` proved | No | No unconditional contradiction is claimed. |
| Absence claim permitted | No | The tool refuses to infer repository-wide absence from this scan. |

Evidence: `NavierStokesReview/evidence/selected_transport_audit_full_2026-09-28.md` and its JSON companion.

## What the three positive candidates actually say

The three declarations are:

1. `completions/SelectedBarMomentInterface.lean:32-45`,
   `selected_component_barMoment_apply`.
2. `completions/SelectedBarMomentInterface.lean:54-67`,
   `selected_component_requires_transport_data`.
3. `completions/SelectedPhysicalPointTransport.lean:28-36`,
   `barMoment_transport_requires_selected_scalar`.

All three operate on `selectedPotentialComponent` and an explicit scalar
pullback or `SelectedBarMomentTransportData`. They rewrite the generic
definition

\[
\operatorname{barMoment}(k,\phi,n,p)
 = \int r^k\,\operatorname{torusAverage}(\phi_n)(r,p)\,dr.
\]

They do **not** prove any of the following:

- that `selected_witness` exports the point-to-space-time map;
- that it exports the scalar profile required by the pullback;
- that the post-curl, localized, periodised, infinite `tsum` field equals that
  scalar profile;
- that the final field satisfies the five paper observables
  \((M,I,J,S,C_p)\);
- that any moment defect is nonzero.

This is a positive result for the audit: the bridge is not being declared
absent merely because a name was not found. The closest declarations have
been located and their exact missing premises are explicit.

## Conditional and adversarial candidates

The remaining joint candidates include:

- `selected_mixed_barMoment_zero_of_positive_pullback`, which is conditional
  on a positive periodic pullback and concludes an undefined/non-integrable
  integral is zero;
- compatibility and endpoint-interface probes involving `Debt` and
  `FiveRows`;
- the selected-witness envelope coexisting with unconstrained external debt.

These are useful adversarial diagnostics. They do not establish that the
concrete selected Cartesian field has a nonzero moment, and they do not yield
`False` without all concrete premises on the selected branch.

## Environment limitation

The environment cross-check is currently blocked, not silently accepted.
The supplied snapshot
`evidence/selected_transport_audit_environment_2026-09-28.json` lacks both
configured roots `NavierStokes.ActualCandidateAssembly.selected_witness` and
`NavierStokesR3.theorem_1_1`. A fresh attempt to run
`NavierStokesReview/src/audit/EnvironmentDependencyExport.lean` failed before
export because the Lean environment lacks
`.lake/build/lib/lean/NavierStokes/R3/Theorem.olean`. Therefore no current
environment-closure claim is used to support the endpoint verdict. The source
pass and the environment pass are reported separately until a successful
dependency export is produced.

## Required next proof obligations

The next probe lane must instantiate the explicit transport data with the
actual selected construction, then calculate rather than infer:

1. the exact Cartesian component or radial pullback used;
2. the contribution of the curl/localisation commutator;
3. the finite-prefix-to-`tsum` passage;
4. periodisation and radial integration domains;
5. the resulting comparison with the paper's five observables.

Until those value-level obligations are discharged, the defensible status is
`CTR-005: selected-field paper-to-code transport not established`, not
`FORMALLY REFUTED` and not `VERIFIED CMI`.
