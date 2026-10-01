# Priority 242: Comparator boundary, totalisation, and proof-provenance audit

**Date:** 2026-10-01
**Status:** active audit lane; source-level results recorded, kernel/proof-term closure still required
**Scope:** current checkout `review/cmi-first-navier-stokes-reconciled-2026-09-30`

## 1. The challenge `sorry` is not the submitted solution

The challenge and solution files are separate objects and must not be conflated.

| Object | Source evidence | Current interpretation |
|---|---|---|
| `ComparatorChallenges/NavierStokes.lean` | C and D challenge declarations at lines 273–284; placeholder bodies at lines 277 and 284 | Specification/template boundary. The placeholders are expected to be audited, but are not by themselves a defect in the submitted solution. |
| `NavierStokes/ComparatorSolution.lean` | Imports `NavierStokes.ComparatorR3Theorem` and `NavierStokes.ComparatorTheorem` at lines 1–2; C/D theorem wrappers at lines 16–27; no `sorry` lines | Submitted solution wrapper. Source inspection shows no direct import of the challenge module. |
| Comparator configuration and proof-term closure | Must be checked from the exact pinned checkout and elaborated environment | Required before making any claim that the solution is independent of challenge admissions. |

The correct logical distinction is:

\[
\text{challenge placeholder}
\neq
\text{submitted theorem dependency on }\texttt{sorryAx}.
\]

The lexical audit therefore records the placeholder locations but does not label them as a compiler escape. The next gate is an exact Comparator run plus recursive proof-term/axiom evidence for both C and D.

## 2. Targeted source audit instrument

`NavierStokesReview/src/audit/comparator_trust_and_totalization_audit.py` now records:

- challenge/solution file presence, imports, headline declarations, and placeholder lines;
- obvious trust-boundary tokens (`sorry`, `unsafe`, `partial`, `opaque`, native proof admission, custom axioms, and metaprogramming markers);
- selected-route `noncomputable`, `Classical.choice`, conditional fallback, extension, `sInf`/`sSup`, and `Filter.bot` sites;
- exact path and line number for every hit.

The generated record is:

`NavierStokesReview/evidence/comparator_trust_totalization_audit_2026-10-01.json`

The current selected-route run scanned 18 relevant Lean files and found 5 trust-boundary token hits and 46 totalisation/choice hits across 8 files. This is triage evidence only. It is not an AST absence proof, not a proof-term closure, and not evidence that any flagged construction is unsound.

## 3. Positive and unresolved semantic evidence

Several constructions show the exact pattern that requires a semantic follow-up:

- `ValidBandGluing.representative` (`ValidBandGluing.lean:27–29`) chooses a chart value on the covered union and returns `0` outside it. The relevant obligations are coverage of every selected point, chart compatibility, and no accidental promotion of a germ/union result to a global result.
- `SmoothPathFamily.pathFamily` (`SmoothPathFamily.lean:29–31`) and `CompactSmoothFamily` use a conditional fallback to the zero object. The good branch must be proved at each downstream selected use.
- `PreparedOutgoing.prepared` (`PreparedOutgoing.lean:119`) selects an existential witness with `Classical.choice`. The selected object must be tracked as one identity, and later properties must be shown for that same choice.
- `JointResidualLimits` uses choice for one-sided extensions, but also contains `boundaryLimits_eq_extension` and `boundaryLimits_independent` (lines 169–175). Those theorems are positive evidence that the boundary object is intended to be choice-independent. The remaining question is whether the actual selected residual satisfies the hypotheses used by those theorems.

These are not kernel loopholes. They are **semantic provenance edges**:

\[
\text{constructor or choice}
\longrightarrow
\text{branch/coverage/independence theorem}
\longrightarrow
\text{same selected }(u,p,f,K)\text{ use}.
\]

## 4. Required next gates

### Comparator and trust boundary

1. Run Comparator from a clean exact checkout for both C and D.
2. Record the challenge/solution configuration, allowed axioms, and final `#print axioms` output.
3. Recursively verify that no submitted proof term reaches challenge placeholders or `sorryAx`.
4. Repeat the source scan with a syntax-aware/token-aware parser, including build files, generated Lean, plugins, and pinned dependencies.

### Fefferman-to-Comparator variance

The relevant directions are asymmetric:

\[
\text{ComparatorData}(u^\circ,f)
\Longrightarrow
\text{FeffermanAdmissibleData}(u^\circ,f)
\]

for constructed data, and

\[
\text{FeffermanSolution}(v,p)
\Longrightarrow
\texttt{ComparatorSolution}(v,p)
\]

for hypothetical competitors. The second implication is the critical nonexistence-transfer direction. It must be checked for:

- finite-energy integral versus explicit `MemLp`;
- coordinate/multi-index derivative bounds versus iterated Fréchet-derivative norm bounds;
- pressure regularity and gauge treatment;
- initial data, force identity, viscosity, time domain, and PDE scope.

### A/B proof archaeology

For September 8 (`8937a8f4`) and September 10 (`f9e8bc5b`), record separately:

\[
P_A\cap P_B,\qquad P_A\setminus P_B,\qquad P_B\setminus P_A,
\]

where (P_A,P_B) are declaration-level proof-term dependency sets, not import closures. Hash the fully elaborated headline types and comparator predicates. Then classify every B-only strengthening as:

- required for C/D;
- required only for the stronger manuscript theorem;
- semantic ambiguity closure;
- explanatory or paper-facing strengthening;
- unresolved.

The existing positive B result remains: one coherent selected \((u,p,f,K)\) is carried through the R³ theorem and comparator. The A/B witness-identity question is separate and remains open until exact extensional or transformation relations are established.

### Constructor-field provenance

For `CandidateProperties`, `Witness`, comparison structures, and major construction records, build:

\[
\text{field}
\leftarrow
\text{constructor site}
\leftarrow
\text{theorem proving the exact value}
\leftarrow
\text{primitive analytic definitions}.
\]

An interface field is not treated as independently established merely because a later theorem consumes it.

## 5. Boundary with CTR-005

This lane does not replace the selected-field/moment transport audit. It refines it. The current supported state remains:

- the production route uses real upstream physical data and carries one coherent selected tuple;
- the challenge `sorry` placeholders are not, by themselves, evidence of a submitted proof hole;
- the current record still lacks a located theorem identifying the final activated/localised/periodised/summed fields with the manuscript’s \((M,I,J,S,C_p)\);
- no selected-path nonzero defect, kernel contradiction, or literal CMI failure is claimed from that omission alone;
- force smoothness, energy, uniqueness-class transfer, pressure semantics, limit/interchange validity, and manuscript correspondence remain independent load-bearing audit lanes.

The human-readable proof dossier will therefore be generated only after the proof-term dominators and minimal semantic cut points are known. It will show exact Lean type, mathematical rendering, source, dependencies, axioms, and correspondence status side by side.
