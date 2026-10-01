# Priority 239: two-submission semantic differential programme

Date: 2026-10-01

## Purpose

Treat the 8 September object `8937a8f4` and the 10 September object
`f9e8bc5` as two formal submissions, not as one undifferentiated current
checkout. The measured public delta is already recorded separately. This
record defines the semantic comparison needed to determine whether the later
Navier--Stokes expansion was merely paper-facing alignment, a genuine
strengthening, or a repair of an obligation that the earlier route did not
establish.

## Established repository facts

- The raw comparison records 188 changed files, 25,143 insertions, and 81
  deletions; both commit messages are `.`.
- The C route changed from
  `R3CompactCandidate.selected_compact_candidate` to
  `NavierStokesR3.theorem_1_1`.
- The periodic route changed from
  `ActualCandidateAssembly.selected_candidate` to
  `PeriodicPaper.periodic_corollary`.
- The later source tree contains explicit paper-facing R3 candidate,
  comparison, energy, pressure, uniqueness, force, and integrability modules.
- The currently compiled comparator probe establishes only the one-way
  inclusion from the comparator solution class to the R3 global finite-energy
  class. It does not establish reverse inclusion or full specification
  equivalence.

These facts raise provenance priority. They do not prove concealment, a
compiler escape, or mathematical error.

## Differential questions

For each item below, compare the exact declaration and proof-term closure in A
and B. The allowed classifications are:

`already proved in A`; `true but unstated in A`; `absent in A`; `strengthened
in B`; `witness changed`; `paper-facing wrapper`; `not yet determined`.

1. Do both routes use the same selected (u^\circ,p,f), or only separately
   existing witnesses?
2. Does B preserve the same fixed force and initial datum through the
   comparator and uniqueness contradiction?
3. Was candidate uniform energy on (0\leq t<1) already available in A?
4. Was global force regularity, including positive-time support and all-order
   smoothness, already available in A?
5. Did B replace totalised integrals with explicit integrability or finiteness
   hypotheses, and were any A conclusions dependent on the totalised value?
6. Did B change pressure gauge, pressure domain, or non-local pressure
   obligations?
7. Did B weaken or strengthen the hypothetical global competitor class?
8. Did B broaden the manuscript parameter range, and do the C/D endpoints use
   the broader range?
9. Which B declarations dominate the new headline theorem proof term rather
   than merely appearing in its import closure?
10. Which facts remain separate from the selected five-observable bridge
    `CTR-005`?

## Required outputs

- Immutable A/B source snapshots or equivalent raw-object references.
- Declaration-level proof-term closures for C and D at both commits.
- A field-by-field old/new contract table.
- A shared-core graph (A\cap B) and added-route graph (B\setminus A).
- A witness-identity ledger for (u^\circ,u,p,f), pressure, and competitor
  objects.
- A totalisation/interchange ledger for integrals, derivatives, limits, and
  `tsum` operations.
- A final classification of each semantic strengthening and a separate
  conclusion for CMI comparator fidelity, manuscript correspondence, and
  internal Lean correctness.

## Non-claims

This programme does not assume that the September 8 route is false, that the
September 10 route repairs a known failure, or that terse commit messages imply
bad intent. It also does not replace the active selected-field transport,
five-moment, force-smoothness, pressure, limit, energy, uniqueness, and
mutation audits. `CTR-005` remains `NOT ESTABLISHED`; no selected mismatch,
force nonsmoothness, literal CMI failure, impossibility theorem, or `False` is
claimed by this record.

## Evidence routing

- Public delta: `priority_236_public_release_provenance_delta_2026-10-01.md`.
- Comparator edge: `priority_238_cmi_comparator_class_inclusion_2026-10-01.md`.
- Review probe: `../probes/CMIComparatorClassInclusionProbe.lean`.
