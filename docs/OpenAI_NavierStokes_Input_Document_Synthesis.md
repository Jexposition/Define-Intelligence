# Input-document synthesis for the Navier–Stokes peer review

Status: incorporated into the audit corpus on 2026-09-22. The exact paths,
sizes, line counts, and SHA-256 hashes are recorded in
`NavierStokesReview/evidence/input_documents_manifest.json`. The source files
remain outside the fork; the review branch records their provenance rather
than duplicating the PDF and ZIP.

## Reading rule

The supplied documents are hypotheses and audit proposals, not authorities.
Each claim is tested against the current fork at commit
`9b9a7092a42c5f376bb7e4bfed84200c528360d5`, the official Clay statement, and
the exported Lean declarations. A proposal is retained when it identifies a
checkable dependency; it is not promoted to a finding merely because it is
phrased as a verdict.

## Disposition of every supplied input

| Input | Main contribution | Disposition in this review |
|---|---|---|
| `Technical Audit Report_ Evaluating the Validity and Mathematical Utility of the OpenAI Astra Proof Certificates.md` | Calls for transitive axiom extraction, isolation of challenge `sorry`s, semantic CMI checks, guarded scaling/zero-division review, and independent kernel verification. It also argues that forced C/D is physically less central than A/B and raises a hypo-dissipative concern. | The audit protocol and the axiom/placeholder tests are adopted. The forced-versus-unforced point is recorded as scope, not a CMI defect, because the official CMI statement explicitly includes alternatives C and D. The hypo-dissipative point is not a refutation of a classical Newtonian result: changing the dissipation exponent changes the PDE. |
| `01-Comprehensive Audit ... Mathe.md` | Extends the same “proof inflation” and hidden-axiom concerns to the wider Astra release, and proposes checking the Navier–Stokes scaling and singular-limit files. | The wider-ten-proofs allegations are out of scope for this repository-specific review unless a dependency enters the exported Navier–Stokes theorem. Its proposed Navier–Stokes checks are retained as audit items. |
| `02-Navier-Stokes Research Paper Refinement.md.md` | Supplies a paper-oriented reconstruction of the candidate, residual/force, scaling, and regularity narrative. | Used as an interpretive cross-check against the Lean definitions. Claims are treated as hypotheses until tied to exact definitions or proved declarations. |
| `03-Note on the Logical Inconsistencies in the Formalised Navier-Stokes Blowup Construction (2).md.md` | Focuses on possible gaps between a finite-time local candidate and the global CMI solution class, including endpoint smoothness, pressure, energy, and the force construction. | Converted into the load-bearing audit lanes: candidate-to-global uniqueness, pressure-flux comparison, force decay/support, and the exact energy predicate. |
| `04-navier-stokes.pdf.md` | Text extraction of the supplied paper, including construction stages, scaling parameters, residuals, support, and regularity claims. | Used only as a searchable research aid. The raw `navier-stokes.pdf` and Lean source control the mathematical audit because extraction can alter notation or polarity. |
| `Navier-Stokes Research Paper Refinement.md` | Earlier paper refinement and exposition of the proposed mechanism. | Cross-referenced; not treated as proof evidence. |
| `Note on the Logical Inconsistencies in the Formalised Navier-Stokes Blowup Construction*.md` | Earlier critique variants concerning logical bridges and formalised blow-up. | Consolidated with the backup critique; duplicate or superseded wording is retained in the manifest but does not create separate findings. |
| `navier-stokes.pdf` | Primary supplied manuscript. | Preserved by path and hash; raw source and CMI statement take precedence over PDF text extraction for formal claims. |
| `NavierStokesAndEuler-main.zip` | User’s downloaded repository snapshot. | Used for provenance and version-drift comparison only; it is not the authoritative current source after the fork sync. |

## Immediate review consequences

1. “It compiles” is not the question. The critical question is whether the
   exported theorem has the CMI quantifiers and whether its nonexistence proof
   is supported by proved analytic bridges rather than hidden assumptions.
2. Smooth forcing is not automatically disqualifying. It must be checked
   against the exact CMI derivative-decay predicates, and the CMI alternative
   being claimed must be identified.
3. An a-posteriori force is mathematically relevant to interpretation, but it
   is not by itself a statement mismatch for C/D. The audit must test whether
   that force is smooth, positive-time supported, and mapped to the official
   force class.
4. The wider Astra claims and any altered-dissipation claims are not silently
   imported into the Navier–Stokes verdict. They become relevant only if the
   current repository’s exported theorem depends on them.
5. The backup material correctly identifies the need for `#print axioms`, but
   a repository-wide `sorry` count is insufficient. Challenge placeholders
   must be separated from the exported theorem dependency graph.

## Current status

The document corpus is inventoried and incorporated. The remaining decisive
lanes are the exact transitive axiom output, independent quantifier probes,
and source-level inspection of the pressure/energy/force bridges.
