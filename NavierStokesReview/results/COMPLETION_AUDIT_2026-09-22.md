# Completion audit: OpenAI Navier–Stokes and Euler review

Date: 2026-09-22
Audited source commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
Review branch commit: `d22a07e66928213ecec94baa3165857431b13869`
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
| Generic residual-rate API | ISSUE RECORDED, not a CMI mismatch | `JetRate` is true on the bottom filter for arbitrary data. The selected `originPast` endpoint is independently `NeBot`, and the final theorem returns a rate on that endpoint. Derived premise-filter nontriviality remains a formalisation-quality review item. |
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

## Review disposition

Current disposition: `FORMAL TRUST PASS; CMI PREDICATE MATCH CONFIRMED AT LEAN
INTERFACE LEVEL; HUMAN PDE PEER REVIEW OPEN; NO NEGATIVE CMI FINDING
ESTABLISHED`.

The appropriate next peer-review action is to discharge the three remaining
semantic items with explicit theorem-to-CMI correspondence proofs or an
independent mathematician's line-by-line verification. Compilation is not a
review result and is recorded only as the means of obtaining kernel evidence.
