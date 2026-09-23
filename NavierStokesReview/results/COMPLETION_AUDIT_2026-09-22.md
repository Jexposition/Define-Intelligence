# Completion audit: OpenAI Navier–Stokes and Euler review

Date: 2026-09-22
Audited source commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
Review branch baseline before this update: `a7f65e2`
Declared toolchain: `leanprover/lean4:v4.34.0-rc2`

## Gate results

| Gate | Result | Evidence and remaining qualification |
|---|---|---|
| Source provenance | COMPLETE | Public fork is pinned; downloaded ZIP is separately compared and preserved. |
| CMI C and D proposition shape | CONFIRMED at elaboration level | `CMIQuantifierProbe` applies the exported whole-space and periodic declarations to the expected existential and negated-solution shapes. |
| CMI source predicate mapping | CONFIRMED at Lean-interface level | The exact whole-space and periodic predicates, force bridge, energy bridge, periodic pressure, and same-force negation have been traced and independently probed. The one-sided `ContDiffOn` convention is explicit; textbook extension equivalence and imported analytic validity remain human-review items. |
| Navier–Stokes kernel trust | CONFIRMED | Four headline declarations report only `propext`, `Classical.choice`, and `Quot.sound`. |
| Euler kernel trust | CONFIRMED | Two headline declarations report only `propext`, `Classical.choice`, and `Quot.sound`. |
| Challenge placeholder reachability | CLOSED for audited exports | Four lexical `sorry` lines remain in the separate challenge files; no audited headline report contains `sorryAx`. |
| Generic residual-rate API | ISSUE RECORDED, not a CMI mismatch | `JetRate` is true on the bottom filter for arbitrary data. The selected `originPast` endpoint and the exact open-past endpoint at `(1, 0)` are independently `NeBot`. Derived premise-filter nontriviality remains a formalisation-quality review item. |
| CMI procedural acceptance | NOT ESTABLISHED | Kernel output cannot substitute for publication, two-year examination, or general community acceptance under CMI rules. |

## What this audit establishes

The formal trust question is answered for the six audited headline exports under
the repository-declared Lean 4.34.0-rc2 environment: the independent kernel
reports contain no `sorryAx`, native-evaluation axiom, or project-specific
axiom. The existence of four `sorry` declarations in `ComparatorChallenges`
does not, on the available dependency evidence, contaminate those exports.

The CMI-facing statements also elaborate with the expected quantifier shape.
The whole-space route uses the same existentially selected initial field and
force in the negated global-solution clause. The periodic route is separate and
includes periodic pressure in the solution structure. The independent force
bridge probe also confirms that compact smooth positive-time forcing implies
the full Comparator decay predicate, rather than only a support marker.

## What this audit does not establish

It does not certify the analytic truth of the many imported PDE lemmas merely
because Lean accepted their interfaces. The remaining peer-review tasks are
the formal textbook-equivalence theorem for the one-sided boundary convention,
the provenance and common-domain coverage of every inverse/correction
premise, and the proof-relevant nontriviality of all derived filters used by
residual-rate consumers. These are specific source-level review targets, not
claims that a counterexample has already been proved.

The strongest concrete formalisation issue found is the generic `JetRate`
interface: its arbitrary-filter form admits vacuous proofs on `⊥`. The
principal endpoint used by the audited base-error path is nontrivial, so this
finding is not currently a disproof of the exported Navier–Stokes theorem.

The derived-filter probe makes the scope precise: `NeBot originPast` does not
imply `NeBot (originPast ⊓ 𝓟 activeᶜ)`. The selected-rate consumer still has a
valid two-branch proof, so the open item is whether the actual exterior branch
is frequent and quantitatively substantive, not whether Lean accepts a
bottom-filter theorem in the abstract. A separate probe now proves the exact
selected open-past endpoint at `(1, 0)` is `NeBot`; that positive result must
not be generalised to the derived branch without another proof.

The raw endpoint evidence is in
`NavierStokesReview/results/OPEN_PAST_NEBOT_4_34_RC2.txt`, with the source-level
interpretation in `OPEN_PAST_FILTER_AUDIT_2026-09-22.md`.

The accompanying load-bearing semantic audit records positive source evidence
for pressure recovery, pressure-flux closure, viscosity scaling, and the force
bridge. It found no concrete CMI-interface mismatch in those lanes. The report
does not substitute source inspection for an independent PDE verification of
the imported analytic lemmas.

See `NavierStokesReview/results/SEMANTIC_LOAD_BEARING_AUDIT_2026-09-22.md`.

## Review disposition

Current disposition: `FORCED CMI C/D THEOREM CONFIRMED AT LEAN LEVEL;
UNFORCED A/B CLAIM NOT PROVED; NO CONFIRMED FORMAL COUNTEREXAMPLE`.

This is the final theorem-level answer: OpenAI has proved the forced CMI C/D
claim formalised in the repository. It has not proved the unforced A/B claim.
The unresolved gates are independent analytic replication, common-domain
coverage for every inverse and derived filter, term-by-term residual review,
whole-space pressure/energy review, and institutional CMI acceptance. None is a
confirmed contradiction in the exported C/D theorem.

The absence of a confirmed counterexample is recorded separately. The present
status is therefore `FORCED C/D THEOREM CONFIRMED; UNFORCED A/B CLAIM NOT
PROVED`, not `THEOREM REFUTED`. The complete decision is in
`NavierStokesReview/results/FINAL_BINARY_VERDICT_2026-09-23.md`.

The appropriate next peer-review action is to continue the line-by-line audit
as replication and documentation. The binary theorem classification is closed
in `NavierStokesReview/results/FINAL_BINARY_VERDICT_2026-09-23.md`.

## Binary claim classification update

The formal-trust result and the public headline are now separated explicitly:

- **YES:** the audited Lean exports formally establish the forced CMI
  Alternative C/D-shaped theorem.
- **NO:** the repository does not establish the unforced three-dimensional
  Navier–Stokes blow-up claim.
- **OPEN:** complete human verification of every analytic certificate in the
  paper remains a separate peer-review task.

See `NavierStokesReview/results/FINAL_CLAIM_CLASSIFICATION_2026-09-22.md`.
